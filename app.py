import google.generativeai as genai
import streamlit as st

# Read Gemini API key from file
f = open("keys/.gemini.txt")
key = f.read()

# Configure Gemini API
genai.configure(api_key=key)

# Set Streamlit app title and subheader
st.title("🤖 Data Science tutor - AI chatbot 📝")

st.chat_message("ai").write("Hi, How may I help you?")

# Initialize Gemini model
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    system_instruction="""You are a helpful AI teaching assistant.
                        Please provide polite answers to user queries related to data science and artificial intelligence topics , 
                        give the all information and links also and offer helpful insights. If the query is unrelated, 
                        respond with 'I'm sorry, I'm not able to assist with that topic at the moment."""
)

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Start chat with model
chat = model.start_chat(history=st.session_state['chat_history'])

# Display chat history
for msg in chat.history:
    st.chat_message(msg.role).write(msg.parts[0].text)

# Get user input
user_prompt = st.chat_input()

# Process user input
if user_prompt:
    st.chat_message("user").write(user_prompt)
    response = chat.send_message(user_prompt)
    st.chat_message("ai").write(response.text)
    st.session_state["chat_history"] = chat.history