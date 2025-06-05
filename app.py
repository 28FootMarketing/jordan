import streamlit as st

# Page configuration
st.set_page_config(page_title="Jordan Bot - Onboarding Specialist")

# Title and header
st.title("🏀 Jordan Bot: The Closer")
st.subheader("Helping You Start Strong in Your Recruiting Journey")

# Style of Play
st.markdown("**Style of Play:** Dominant, confident, and precise")

# Introduction
st.markdown("""
Jordan Bot is here to walk you through the very first steps of your recruiting journey.  
From creating your profile to selecting your target schools, this onboarding assistant ensures you're set up for success from Day One.

Just like MJ made his mark early in every game, Jordan Bot ensures every family starts strong.
""")

# Step 1: Basic Profile Setup
st.header("Step 1: Basic Profile Setup")
name = st.text_input("Student-Athlete Full Name")
graduation_year = st.selectbox("Graduation Year", [2025, 2026, 2027, 2028, 2029])
sport = st.text_input("Primary Sport")
position = st.text_input("Primary Position")

# Step 2: Film Upload
st.header("Step 2: Upload Highlight Video")
video_link = st.text_input("Paste Your Highlight Video Link (YouTube, Hudl, etc.)")

# Step 3: Target Schools
st.header("Step 3: Identify Target Schools")
target_schools = st.text_area("List Your Target Colleges (separate by commas)")

# Summary Output
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
def run():
    # Move your entire app logic into this function.
    st.title("Agent Name")
    # ... rest of the agent's interface ...
