import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Jordan Bot Onboarding", layout="centered")

# --- Header ---
st.title("🏀 Jordan Bot: The Closer")
st.subheader("Start Your Recruiting Journey")

st.markdown("**Style of Play:** Dominant, confident, and precise")
st.markdown("Jordan Bot helps student-athletes take the first step in the college recruiting process.")

# --- Embed GoHighLevel Form ---
st.markdown("""<iframe src="https://connect.28footmarketing.com/widget/form/Muy6TJKltd0NNdPq13Lv"
width="100%" height="800" frameborder="0" style="border: none;"></iframe>
""", unsafe_allow_html=True)

st.markdown("---")
st.info("Need help completing the form? Our team will reach out once your submission is received.")
