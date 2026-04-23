# Streamlit Groq Chatbot with History

This project is a simple chatbot web application built with Streamlit, Groq, and LangChain. It allows the user to send messages through a chat-style interface and receive AI-generated replies. The application also keeps chat history during the session and provides a clear chat button to reset the conversation.

The project uses Streamlit for the frontend interface, LangChain for message handling, and Groq for generating responses from the language model. The API key is loaded securely from a `.env` file.

## Features

- Chat-based user interface
- Conversation history in the same session
- Clear Chat button to reset messages
- Groq model integration
- Simple and beginner-friendly structure

## Files

- `app.py` - main Streamlit chatbot application
- `requirements.txt` - required Python libraries

## Installation

First, install all required packages:

```bash
pip install -r requirements.txt
