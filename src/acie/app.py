import streamlit as st
import requests
import json

st.set_page_config(page_title="ACIE - Market Research", layout="wide")

st.title("Autonomous Competitive Intelligence Engine (ACIE)")
st.markdown("Enter a company name or URL to generate a strategic market research report.")

response = requests.get("http://localhost:8000/greet")
# Input
topic = st.text_input("Company Name or URL", placeholder="e.g., Linear or https://linear.app")

if st.button("Generate Report"):
    if not topic:
        st.warning("Please enter a company name or URL.")
    else:
        with st.spinner("Dispatching AI agents... This may take a few minutes."):
            try:
                # Call FastAPI backend
                response = requests.post(
                    "http://localhost:8000/research",
                    json={"topic": topic}
                )
                
                if response.status_code == 200:
                    result = response.json().get("result")
                    st.success("Research completed!")
                    st.markdown("### Strategic Report")
                    st.markdown(result)
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
            except requests.exceptions.ConnectionError:
                st.error("Could not connect to the backend server. Is it running?")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
