import streamlit as st
import time
from datetime import datetime, timedelta
import firebase_admin
from firebase_admin import credentials, firestore
import os ,requests
from streamlit_session_browser_storage import SessionStorage
sessionBrowserS = SessionStorage()

st.cache_data.clear()
st.cache_resource.clear()
st.set_page_config(page_title="Real-Time Traffic & Weather API Status", page_icon="🚦",layout ="wide")

# Simulated state (in real app, replace with actual checks)
api_status = "DOWN"

saved_individual = sessionBrowserS.getAll()

if "show_api_info" not  in saved_individual:
    sessionBrowserS.setItem("show_api_info", False)
    show_api_info=False
    
else:    
    show_api_info=sessionBrowserS.getItem("show_api_info")
    
    

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1358363882833313882/TIip_rNgIAj5uIxAYJbmZ2YAHOQ-C9iwi-bFQ3qqY5FNqMcTUVD7udJM8_9ZMZzCDIVv"  # Replace with your webhook
firebase_creds = st.secrets["firebase"]
class ApiMonitor:
    def __init__(self, cred_path, collection="api_usage"):
        if not firebase_admin._apps:
            cred = credentials.Certificate(dict(firebase_creds))
            firebase_admin.initialize_app(cred)

        self.db = firestore.client()
        self.collection = collection

    def _get_today_key(self):
        return datetime.utcnow().strftime("%Y-%m-%d")

    def get_status(self, api_name):
        key = self._get_today_key()
        doc = self.db.collection(self.collection).document(key).get()
        if doc.exists:
            data = doc.to_dict().get(api_name, {})
            return data.get("count", 0), data.get("failures", 0), data.get("is_down", False)
        return 0, 0, False

    def increment_api_count(self, api_name):
        key = self._get_today_key()
        print(key)
        self.db.collection(self.collection).document(key).set(
            {f"{api_name}.count": firestore.Increment(1)}, merge=True
        )

    def increment_failure(self, api_name):
        key = self._get_today_key()
        self.db.collection(self.collection).document(key).set(
            {f"{api_name}.failures": firestore.Increment(1)}, merge=True
        )

    def reset_failure_count(self, api_name):
        key = self._get_today_key()
        self.db.collection(self.collection).document(key).set(
            {f"{api_name}.failures": 0}, merge=True
        )

    def mark_api_status(self, api_name, is_down):
        key = self._get_today_key()
        self.db.collection(self.collection).document(key).set(
            {f"{api_name}.is_down": is_down}, merge=True
        )
# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
monitor = ApiMonitor("firebase_config.json")  # adjust path if needed
today = datetime.utcnow().date()
reservations = monitor.db.collection("reservations") \
        .where("reserved_at", ">=", datetime(today.year, today.month, today.day)) \
        .order_by("reserved_at") \
        .stream()

queue = [doc.to_dict().get("username") for doc in reservations]
count, failures, is_down = monitor.get_status("tomtom")
is_down=False
if count >= 2500 or is_down:
   api_status = "DOWN"
   if count >= 2500:
      api_down_reason = "API usage exceeded daily limit of 2500 calls."
   else:
      api_down_reason = "API marked as unavailable by system health check."
else:
      api_status = "UP"
      api_down_reason = None

def send_to_discord(name,email, role, purpose, message):
    embed = {
        "title": "🚀 Streamlit form user Info",
        "color": 3447003,
        "fields": [
            {"name": "🧑 Name", "value": name, "inline": True},
            {"name": "📫 Email/Linkedin", "value": email if email else "Not provided", "inline": True},
            {"name": "🎯 Role / Interest", "value": role if role else "Not provided", "inline": False},
            {"name": "📝 purpose", "value": purpose if purpose else "Not provided", "inline": False},
            {"name": "📝 Message", "value": message if message else "Not provided", "inline": False},

        ]
    }
    if message:
        embed["fields"].append({"name": "💬 Feedback / Comment", "value": message, "inline": False})

    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json={"embeds": [embed]})
        if response.status_code != 204:
            st.warning(f"⚠️ Discord webhook failed with status {response.status_code}")
    except Exception as e:
        st.warning(f"⚠️ Could not send to Discord: {e}")     
        
def send_skip_alert_to_discord():
    embed = {
        "title": "⏭️ streamlit Info Form Skipped",
        "color": 15158332,
        "description": "Someone **ran the container** and skipped the info form.",
    }
    try:
        requests.post(DISCORD_WEBHOOK_URL, json={"embeds": [embed]})
    except Exception as e:
        st.warning(f"⚠️ Could not send to Discord: {e}")
      
# Main Header
st.markdown("<h1 style='text-align: center;'>🚦 Real-Time Traffic & Weather API Status </h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>check live API status before pulling docker image", unsafe_allow_html=True)
st.write("")
def show_user_form():
    # Time left calculation    
    st.title("🚪 Knock knock...")
    st.markdown("---")
    st.markdown("Before jumping into the app, I'd love to know a bit about who's visiting. \
                 Whether you're a recruiter, dev, or just curious, this helps me improve and connect. 🚀")

    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Your Name")

    with col2:
        contact = st.text_input("Email or LinkedIn (optional)")

    # 2️⃣ Role + Purpose side-by-side
    col3, col4 = st.columns(2)
    with col3:
        role = st.selectbox("You're here as a...", ["Recruiter", "Developer", "Friend", "Just Curious 👀", "Other"])

    with col4:
        purpose = st.selectbox("What brings you here?", ["Hiring", "Checking out portfolio", "Collaboration", "Giving Feedback", "Other"])

    # 3️⃣ Feedback - full width
    message = st.text_area("Anything you'd like to share? (Optional)", height=100)

    col1, col2 = st.columns([2, 2])
    with col1:
        if st.button("Submit"):
            if name:
                send_to_discord(name, contact, role, purpose, message)
                sessionBrowserS.setItem("show_api_info", True)

                return ("🙌 That was kind of you! Thanks for dropping in", "success")
            else:
                st.error("Please enter your name at minimum.")

    with col2:
        if st.button("Skip for now"):
            send_skip_alert_to_discord()
            sessionBrowserS.setItem("show_api_info", True)

            return ("😎 Totally cool — no pressure at all.\n\n🔄 Just refresh and jump right in.", "info")

    return None, None
# Initial Form
#if not show_api_info:
 #   show_user_form()
# === Main Routing ===
if not show_api_info:
    msg, msg_type = show_user_form()
    if msg:
        if msg_type == "success":
            st.success(msg)
            time.sleep(5)
            st.rerun()

        elif msg_type == "info":
            st.info(msg)
            time.sleep(5)
            st.rerun()
        else:
            st.write(msg)
        st.stop()
    else:
        st.stop()

else:
    if 'queue' not in st.session_state:
        st.session_state.queue = []

    today = datetime.utcnow().date()
    if api_status == "DOWN":
        col1, col2 = st.columns([2, 5])

        with col1:
            st.subheader("🔢 Priority Queue for Tomorrow")
            queue_container = st.empty()
            if queue:
                queue_container.markdown("#### Reserved Users")
                queue_container.markdown("\n".join([f"{i+1}. {user}" for i, user in enumerate(queue)]))
            else:
                queue_container.info("No users have reserved access yet.")

        with col2:
            
            st.markdown("""
<div style="
    width: 100%;
    background: rgba(255, 255, 255, 0.15);
    border-radius: 10px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    padding: 25px;
    margin-bottom: 25px;
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.3);
">

  <h5 style="font-size: 1.25rem; margin-bottom: 20px;">🛰 API Status:
    <span style="
      background-color: #dc3545;
      color: white;
      padding: 6px 14px;
      border-radius: 1rem;
      font-size: 0.95rem;
      font-weight: 500;
    ">
      DOWN
    </span>
  </h5>

  <div style="
    background-color: rgba(255, 243, 205, 0.8);
    border: 1px solid #ffeeba;
    color: #856404;
    padding: 15px 20px;
    border-radius: 8px;
    margin-bottom: 25px;
    font-size: 0.95rem;
  ">
    🚨 <strong>Oops! The API is currently unavailable.</strong><br>
    This project runs on a free-tier API with limited daily requests (2,500 max). Today’s quota has been used up or the system marked it as temporarily down due to health checks.<br><br>
    ⏳ <strong>But good news:</strong> You can <span style="color: green; font-weight: bold;">reserve your access for tomorrow</span> right now to get early access when the system is back!
  </div>
""", unsafe_allow_html=True)

            
            # st.error("🚨 Oops! The API is currently unavailable.")
            # st.markdown("""
            # This project runs on a free-tier API with limited daily requests (2,500 max).  
            # Today’s quota has been used up or the system marked it as temporarily down due to health checks.

            # ⏳ **Good news:** You can **reserve your access for tomorrow** right now to get early access when the system is back!
            # """)
            with st.form("reserve_form"):
                username = st.text_input("Create a unique username", placeholder="e.g. your_custom_id")
                reserve_submit = st.form_submit_button("Reserve API Access for Tomorrow")
                reservations_collection = monitor.db.collection("reservations")
                # Check for duplicate reservation
                docs = reservations_collection.where("username", "==", username).stream()
                if reserve_submit:
                    for doc in docs:
                         data = doc.to_dict()
                         if "reserved_at" in data and data["reserved_at"].date() == today and data["username"]==username:
                                st.warning("🚫 Username already reserved. Try a different one.")
                                st.stop()
                    reservations_collection.add({
                                "username": username,
                                "reserved_at": datetime.utcnow(),
                                "expire_at": datetime.utcnow() + timedelta(days=1)
                               })
                    st.success(f"✅ Reserved successfully as **{username}**")
                    queue.append(username)
                    col1.empty()
                    with col1:
                        if queue:
                            queue_container.markdown("\n".join([f"{i+1}. {user}" for i, user in enumerate(queue)]))
                        else:
                            queue_container.info("No users have reserved access yet.")

                    
    else:
        col1, col2 = st.columns([2, 4])

        with col1:
            st.subheader("🐳 Docker Access Now Live!")
            st.success("The API is online and ready for action.")
            st.markdown("#### Pull the image and get started:")
            st.code("""
            docker pull animesh/api-traffic-weather:latest
            """, language="bash")
            st.info("Containers don’t wait — and neither should you!")

        with col2:
            
            st.markdown("""
            <h3>🛰 API Status:
              <span style="
        background-color: green;
        color: white;
        padding: 4px 10px;
        border-radius: 5px;
        font-size: 0.7em;
        font-weight: 100;
    ">
        UP
    </span>
            </h3>
            """, unsafe_allow_html=True)
            
            st.markdown("""
<div style="
    background: black;
    border-left: 5px solid #198754;
    border-radius: 10px;
    padding: 25px;
    margin-bottom: 25px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    font-family: 'Segoe UI', sans-serif;
    color: #212529;  /* Ensures text is visible in both themes */
">


  <div style="
      background-color: #d1e7dd;
      color: #0f5132;
      border: 1px solid #badbcc;
      padding: 15px 20px;
      border-radius: 8px;
      margin-bottom: 15px;
  ">
    ✅ <strong>Great news!</strong><br>
    The API is <strong>live and healthy</strong>. You're good to go!<br><br>
  </div>

  <p style="color: white; font-size: 0.875rem; margin-bottom: 20px;">Use it while it lasts 😅</p>

  <hr style="border-top: 1px solid #dee2e6; margin: 20px 0;">

  <p style="margin-bottom: 0.75rem;color:white;">
    ⚠️ <strong>Heads-up:</strong> This is a free-tier project, so API calls are limited (because I’m not made of money 💸).
  </p>
  <p style="margin-bottom: 0.75rem; color:white;">
    When the quota hits the fan, you’ll see the “Reserve for Tomorrow” screen again.
  </p>
  <p style="margin-bottom: 0.05rem; color:white;">
    Until then — <strong>code away 🚀</strong> and may your requests be fast and your rate limits merciful.
  </p>

</div>
""", unsafe_allow_html=True)


            # st.success("✅ The API is live and healthy. You're good to go!")
            # st.write("Use it while it lasts 😅")
            # st.markdown("---")
            # st.warning("⚠️ Heads-up: This is a free-tier project, so API calls are limited.")
            # st.markdown("When the quota hits the fan, you’ll see the “Reserve for Tomorrow” screen again.")
            # st.markdown("Until then — **code away 🚀** and may your requests be fast and your rate limits merciful.")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Made with ❤️ by <strong>Animesh</strong></p>", unsafe_allow_html=True)
