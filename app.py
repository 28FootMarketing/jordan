
import streamlit as st

# --- Agent Info ---
AGENT_NAME = "Jordan"
AGENT_NICKNAME = "The Closer"
AGENT_ROLE = "Onboarding Specialist"

# --- Page Configuration ---
st.set_page_config(page_title=f"{AGENT_NAME} - {AGENT_ROLE}", layout="centered")

# --- Header ---
st.title(f"🏀 {AGENT_NAME}: {AGENT_NICKNAME}")
st.subheader("Helping You Start Strong in Your Recruiting Journey")
st.markdown("**Style of Play:** Dominant, confident, and precise")

# --- Agent Introduction ---
st.markdown("""
Jordan is ready to help you take the first step toward getting recruited.  
To begin, please fill out our official intake form.
""")

# --- GHL Direct Form Link ---
st.header("🚀 Start Your Recruiting Journey")
st.markdown("""
🟢 **[Click here to open the Jordan Recruiting Intake Form](https://connect.28footmarketing.com/widget/form/Muy6TJKltd0NNdPq13Lv)**  
It opens in a new tab and takes less than 2 minutes to complete.
""")
