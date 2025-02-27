import streamlit as st
import google.generativeai as genai
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

# Set your Google GenAI API key
GOOGLE_GENAI_API_KEY = "AIzaSyC4DJCI1yp8W7Kzb72lFHTclD12jGLb9ao"

# Initialize Google GenAI
genai.configure(api_key=GOOGLE_GENAI_API_KEY)

# Initialize LangChain Google GenAI Chat Model
chat_model = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash-latest", google_api_key=GOOGLE_GENAI_API_KEY)

def get_travel_recommendations(source, destination):
    """Fetch AI-generated travel recommendations between source and destination."""
    messages = [
        SystemMessage(content="You are an AI travel assistant providing travel recommendations."),
        HumanMessage(content=f"Suggest the best travel options from {source} to {destination}, with estimated costs.")
    ]
    try:
        response = chat_model.invoke(messages)
        return response.content  # Extract the AI-generated response
    except Exception as e:
        return f"Error fetching travel recommendations: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="AI Travel Planner", layout="centered")

st.title("✈️ AI-Powered Travel Planner")
st.markdown("Enter your travel details below to get recommendations!")

# User Inputs
source = st.text_input("🗺️ Source Location", placeholder="Enter starting location")
destination = st.text_input("📍 Destination Location", placeholder="Enter destination")

if st.button("Get Travel Options 🚀"):
    if source and destination:
        with st.spinner("🔍 Fetching travel recommendations..."):
            travel_info = get_travel_recommendations(source, destination)
            st.subheader("📌 Recommended Travel Options")
            st.write(travel_info)
    else:
        st.error("❌ Please enter both source and destination.")
