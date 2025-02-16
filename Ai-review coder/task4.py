import streamlit as st
import google.generativeai as genai

# Set API key 
API_KEY = "AIzaSyC4DJCI1yp8W7Kzb72lFHTclD12jGLb9ao"

# Configure Gemini API
genai.configure(api_key=API_KEY)

def review_code(user_code):
    gemini = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")
    response = gemini.generate_content([user_code])
    return response.text

# Streamlit part
st.title("AI Code Reviewer")
st.write("Submit your Python code for analysis and feedback.")

user_code = st.text_area("Paste your Python code here:")

if st.button("Review Code"):
    if not user_code.strip():
        st.error("Please enter some Python code.")
    else:
        feedback = review_code(user_code)
        st.subheader("Review Feedback:")
        st.write(feedback)

