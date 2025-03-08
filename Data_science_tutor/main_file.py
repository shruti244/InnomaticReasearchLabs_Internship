import streamlit as st
import json
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Initialize the Streamlit app
st.set_page_config(page_title="Conversational AI Data Science Tutor", layout="wide")
st.title("📚 AI Data Science Tutor 🤖")

# Sidebar for history management
st.sidebar.header("⚙️ Options")

def save_chat_history():
    with open("chat_history.json", "w") as f:
        json.dump(st.session_state.messages, f)
    st.sidebar.success("Chat history saved!")

def load_chat_history():
    try:
        with open("chat_history.json", "r") as f:
            loaded_messages = json.load(f)
            # Append loaded messages instead of replacing
            st.session_state.messages.extend(loaded_messages)
        st.sidebar.success("Chat history loaded!")
    except FileNotFoundError:
        st.sidebar.error("No saved chat history found.")


def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "Hello! I’m your AI Data Science Tutor. Ask me anything related to Data Science!"}]
    st.sidebar.success("Chat history cleared!")

st.sidebar.button("Save Chat History", on_click=save_chat_history)
st.sidebar.button("Load Chat History", on_click=load_chat_history)
st.sidebar.button("Clear Chat History", on_click=clear_chat_history)

# Setup Google Gemini Pro
API_KEY = "AIzaSyC4DJCI1yp8W7Kzb72lFHTclD12jGLb9ao"  # Replace with your actual API key
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=API_KEY)

# Memory to retain conversation history
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Define a prompt template
prompt = PromptTemplate(input_variables=["chat_history", "user_input"],
                        template="""
                        You are a helpful AI Data Science tutor. You only answer data science-related questions.
                        Conversation History: {chat_history}
                        User: {user_input}
                        AI:""")

# Create an LLM chain with memory
qa_chain = LLMChain(llm=llm, prompt=prompt, memory=memory)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! I’m your AI Data Science Tutor. Ask me anything related to Data Science!"}]

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
user_input = st.chat_input("Ask a Data Science question...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)
    
    # Get AI response
    response = qa_chain.run(user_input)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)
