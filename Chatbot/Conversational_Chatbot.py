#Python-dotenv reads key-value pairs from a .env file and can set them as environment variables. 
from dotenv import load_dotenv
load_dotenv()
# Streamlit is an open source python framework for machine learning that helps in creating interactive apps
import streamlit as st
#OS module in python helps you interact with operating system
import os
# For using google's generative ai model gemini
import google.generativeai as genai
#Passing api key for configuring
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
#Creating a gemini-pro model for this chatbot
model=genai.GenerativeModel("gemini-pro")
#For storing chatbot conversation history
chat=model.start_chat(history=[])
#Creating a function for generating the response of question
def get_gemini_response(question):
    response=chat.send_message(question,stream=True)
    return response
#Configuring default setting of page
#st.set_page_config(page_title="Q&A")
#Giving name to chatbot
st.header("Mayank")
#Session State is a way to share variables between reruns, for each user sessions.
if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]
#To get text input from user
input=st.text_input("Input:",key="input")
#Creating submit button
submit=st.button("Submit")
#Checking whether input is empty after submit
if submit and input:
    #Saving response based on input
    response=get_gemini_response(input)
    #Using session state varible to keep track of all chats
    st.session_state['chat_history'].append(("You",input))
    #Giving header to the response
    st.subheader("The Response is")
    for chunk in response:
        #Writing response in chunks or small piece of data
        st.write(chunk.text)
        #Using Session state varible to keep record of all responses
        st.session_state['chat_history'].append(("Bot",chunk.text))
#Giving header to chat history
st.subheader("Chat history")
for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")