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

def get_travel_recommendations(source, destination, mode, budget, time, travelers):
    """Fetch AI-generated travel recommendations between source and destination."""
    messages = [
        SystemMessage(content="You are an AI travel assistant providing travel recommendations."),
        HumanMessage(content=f"Find me travel options from {source} to {destination} by {mode}. "
                         f"My budget is {budget} USD, I prefer traveling in the {time}, "
                         f"and we are {travelers} people.")
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

# Travel mode selection
mode = st.selectbox("🚌✈️🚖 Select Travel Mode", ["Any", "Flight", "Train", "Bus", "Cab"])

# Budget input
budget = st.slider("💰 Select Your Budget (in USD)", 50, 5000, 500)

# Preferred travel time
time = st.selectbox("🕒 Preferred Travel Time", ["Morning", "Afternoon", "Night"])

# Number of travelers
travelers = st.number_input("👥 Number of Travelers", min_value=1, max_value=10, value=1, step=1)

if st.button("Get Travel Options 🚀"):
    if source and destination:
        with st.spinner("🔍 Fetching travel recommendations..."):
            travel_info = get_travel_recommendations(source, destination, mode, budget, time, travelers)
            st.subheader("📌 Recommended Travel Options")
            st.write(travel_info)
    else:
        st.error("❌ Please enter both source and destination.")
