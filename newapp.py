import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM  # ✅ Updated import
from langchain_core.output_parsers import StrOutputParser

# Set page title
st.title("Prasanna's Show Chat Bot")

# Input field for user query
input_txt = st.text_input("Please enter your queries here...")

# Define the chatbot prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant. Your name is Prasanna's Assistant."),
    ("user", "User query: {query}")
])

# Load the Ollama model (updated version)
llm = OllamaLLM(model="llama3.2")  # ✅ Updated model

# Output parser
output_parser = StrOutputParser()

# Create the chat pipeline
chain = prompt | llm | output_parser

# Process user input and display response
if input_txt:
    response = chain.invoke({"query": input_txt})
    st.write(response)
