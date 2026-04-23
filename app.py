import streamlit as st
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("GROQ_API_KEY not found in .env file")
    st.stop()

llm = ChatGroq(
    model="groq/compound-mini",
    groq_api_key=GROQ_API_KEY
)

st.title("Groq Chatbot with History")

if "messages" not in st.session_state:
    st.session_state.messages = []

if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Enter your message")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    conversation = [SystemMessage(content="You are a chatbot")]

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            conversation.append(HumanMessage(content=msg["content"]))
        else:
            conversation.append(AIMessage(content=msg["content"]))

    response = llm.invoke(conversation)
    assistant_reply = response.content

    st.session_state.messages.append(
        {"role": "assistant", "content": assistant_reply}
    )

    with st.chat_message("assistant"):
        st.markdown(assistant_reply)

 
