import streamlit as st
from google import genai

st.title("🤖 Enoda Sondha AI Chatbot")

api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("API Key set panna villai!")
else:
    client = genai.Client(api_key=api_key)
    user_input = st.text_input("Enkitta edhavadhu kelungal:")
    
    if user_input:
        with st.spinner("Yosikkiren..."):
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=user_input,
            )
            st.write("**AI Answer:**", response.text)
          
