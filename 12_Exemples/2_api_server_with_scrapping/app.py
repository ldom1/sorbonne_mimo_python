# streamlit_frontend.py
import json
import requests
import streamlit as st

api_url = "http://localhost:8088"

st.title("Web Scraper and Summarizer")

# Add button check API health
check_health = st.button("Check API Health")
if check_health:
    try:
        response = requests.get(f"{api_url}/health")
        health_info = response.json()
        if response.status_code == 200:
            st.success(f"API is running! (Status code: {health_info['status_code']})")
        else:
            st.error(
                f"API is not reachable ! (Status code: {health_info['status_code']}"
            )
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to API: {e}")


# Add Main part
st.subheader("Get the summary of a webpage with ease !")
url = st.text_input("Enter URL to scrape:")

if st.button("Scrape and Summarize"):
    if url:
        response = requests.post(
            f"{api_url}/scrape_and_summarize",
            data=json.dumps({"url": url}),
            headers={"Content-Type": "application/json"},
        )
        if response.status_code == 200:
            summary = response.json().get("summary", "")
            st.subheader("Summary")
            st.write(summary)
        else:
            st.error("Failed to get summary")
    else:
        st.warning("Please enter a URL")
