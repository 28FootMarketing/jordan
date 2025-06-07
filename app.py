import streamlit as st

# --- Agent Metadata (Hidden from display) ---
AGENT_NAME = "Jordan"
AGENT_ROLE = "Onboarding Specialist"
AGENT_NICKNAME = "The Closer"
AGENT_WORKFLOW_FILE = "jordan_onboarding.json"
AGENT_RESPONSIBILITIES = [
    "Welcome new athletes",
    "Collect profile information",
    "Guide through the recruiting timeline"
]

# --- Page Configuration ---
st.set_page_config(page_title=f"{AGENT_NAME} Bot - {AGENT_ROLE}", layout="centered")

# --- Header ---
st.title(f"🏀 {AGENT_NAME}: The Closer")
st.subheader("Helping You Start Strong in Your Recruiting Journey")

# --- Agent Style ---
st.markdown("**Style of Play:** Dominant, confident, and precise")

# --- Agent Introduction ---
st.markdown("""
Jordan is here to walk you through the very first steps of your recruiting journey.  
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
    st.success("✅ Profile Summary Generated")
    st.markdown(f"""
    **Student Name:** {name}  
    **Graduation Year:** {graduation_year}  
    **Sport:** {sport}  
    **Position:** {position}  
    **Highlight Video:** [Watch Video]({video_link})  
    **Target Schools:** {target_schools}
    """)
    st.balloons()
    st.info("Jordan Bot says: Great start! Now keep building your recruiting momentum.")

# (Optional) Uncomment this if needed for debugging or admin view
# st.markdown("---")
# st.caption(f"""
# 🧍 {AGENT_NAME}  
# **Role:** {AGENT_ROLE}  
# **Nickname:** "{AGENT_NICKNAME}"  
# **Workflow File:** `{AGENT_WORKFLOW_FILE}`  
# **Responsibilities:** {', '.join(AGENT_RESPONSIBILITIES)}  
# Trigger Command: `trigger_agent("{AGENT_NAME}")`
# """)
{
    
            "fallback": "Missed a step? No worries\u2014great players refocus fast. Let us start the onboarding again and take the next shot.",
            "avatar": "jordan.png"
        }
