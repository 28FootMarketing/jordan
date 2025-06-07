import streamlit as st
import os
import requests

# --- Agent Metadata ---
AGENT_NAME = "Jordan"
AGENT_ROLE = "Onboarding Specialist"
AGENT_NICKNAME = "The Closer"
AGENT_WORKFLOW_FILE = "jordan_onboarding.json"
AGENT_AVATAR = "jordan.png"
AGENT_FALLBACK = (
    "Missed a step? No worries—great players refocus fast. Let us start the onboarding again and take the next shot."
)
AGENT_RESPONSIBILITIES = [
    "Welcome new athletes",
    "Collect profile information",
    "Guide through the recruiting timeline"
]

# GoHighLevel Webhook URL (replace with your actual form ID)
GHL_FORM_URL = "https://webhooks.leadconnectorhq.com/form/submit/https://connect.28footmarketing.com/widget/form/Muy6TJKltd0NNdPq13Lv"

# --- Page Configuration ---
st.set_page_config(page_title=f"{AGENT_NAME} Bot - {AGENT_ROLE}", layout="centered")

# --- Header ---
if os.path.exists(AGENT_AVATAR):
    st.image(AGENT_AVATAR, width=120)
else:
    st.warning(f"⚠️ Agent avatar '{AGENT_AVATAR}' not found. Please upload the image.")

st.title(f"🏀 {AGENT_NAME}: {AGENT_NICKNAME}")
st.subheader("Helping You Start Strong in Your Recruiting Journey")
st.markdown("**Style of Play:** Dominant, confident, and precise")

# --- Agent Introduction ---
st.markdown("""Jordan is here to walk you through the very first steps of your recruiting journey.  
From creating your profile to selecting your target schools, this onboarding assistant ensures you're set up for success from Day One.

Just like MJ made his mark early in every game, **Jordan Bot** ensures every family starts strong.
""")

# --- Step 1: Basic Profile Setup ---
st.header("Step 1: Basic Profile Setup")
name = st.text_input("Student-Athlete Full Name")
phone = st.text_input("Phone Number")
graduation_year = st.selectbox("Graduation Year", [2025, 2026, 2027, 2028, 2029])
sport = st.text_input("Primary Sport")
position = st.text_input("Primary Position")

# --- Step 2: Film Upload ---
st.header("Step 2: Upload Highlight Video")
video_link = st.text_input("Paste Your Highlight Video Link (YouTube, Hudl, etc.)")

# --- Step 3: Target Schools ---
st.header("Step 3: Identify Target Schools")
target_schools = st.text_area("List Your Target Colleges (separate by commas)")

# --- Summary Output and GHL Submission ---
if st.button("Generate Onboarding Summary"):
    if not name or not phone or not sport or not position:
        st.warning(AGENT_FALLBACK)
    else:
        st.success("✅ Profile Summary Generated")
        st.markdown(f"""**Student Name:** {name}  
**Phone Number:** {phone}  
**Graduation Year:** {graduation_year}  
**Sport:** {sport}  
**Position:** {position}  
**Highlight Video:** [Watch Video]({video_link})  
**Target Schools:** {target_schools}
""".strip())
        st.balloons()

        # Send to GoHighLevel
        payload = {
            "name": name,
            "phone": phone,
            "grad_year": graduation_year,
            "sport": sport,
            "position": position,
            "video_link": video_link,
            "target_schools": target_schools,
            "lead_source": "JordanBot"
        }

        try:
            response = requests.post("https://connect.28footmarketing.com/widget/form/Muy6TJKltd0NNdPq13Lv", json=payload)
            if response.status_code == 200:
                st.success("📬 Jordan Bot successfully sent your info to the recruiting team!")
            else:
                st.error(f"❌ Failed to connect to GoHighLevel. Status Code: {response.status_code}")
        except Exception as e:
            st.error(f"⚠️ Error while sending data to GoHighLevel: {e}")
