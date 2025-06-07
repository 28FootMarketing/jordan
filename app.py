import streamlit as st
import os

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
graduation_year = st.selectbox("Graduation Year", [2025, 2026, 2027, 2028, 2029])
sport = st.text_input("Primary Sport")
position = st.text_input("Primary Position")

# --- Step 2: Film Upload ---
st.header("Step 2: Upload Highlight Video")
video_link = st.text_input("Paste Your Highlight Video Link (YouTube, Hudl, etc.)")

# --- Step 3: Target Schools ---
st.header("Step 3: Identify Target Schools")
target_schools = st.text_area("List Your Target Colleges (separate by commas)")

# --- Summary Output ---
if st.button("Generate Onboarding Summary"):
    if not name or not sport or not position:
        st.warning(AGENT_FALLBACK)
    else:
        st.success("✅ Profile Summary Generated")
        st.markdown(f"""**Student Name:** {name}  
**Graduation Year:** {graduation_year}  
**Sport:** {sport}  
**Position:** {position}  
**Highlight Video:** [Watch Video]({video_link})  
**Target Schools:** {target_schools}
""".strip())
        st.balloons()
        st.info("Jordan Bot says: Great start! Now keep building your recruiting momentum.")

# --- Optional Debug/Trainer View ---
with st.expander("🔧 Agent Metadata (Trainer View)"):
    st.caption(f"""🧍 **Agent:** {AGENT_NAME}  
🎯 **Role:** {AGENT_ROLE}  
🏷️ **Nickname:** "{AGENT_NICKNAME}"  
📂 **Workflow File:** `{AGENT_WORKFLOW_FILE}`  
✅ **Responsibilities:** {', '.join(AGENT_RESPONSIBILITIES)}  
💬 **Fallback:** {AGENT_FALLBACK}
""")
