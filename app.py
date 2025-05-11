
import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import textstat

st.title("AI-Powered SEO Analysis Tool")

url = st.text_input("Enter Website URL to Analyze")

if st.button("Analyze"):
    if url:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            # Extract Website Text
            text = soup.get_text()
            readability = textstat.flesch_reading_ease(text)
            word_count = len(text.split())

            # Extract Title and Meta Description
            title = soup.title.string if soup.title else "No Title Found"
            meta_desc = soup.find("meta", {"name": "description"})
            meta_desc = meta_desc["content"] if meta_desc else "No Meta Description Found"

            # Display Results
            st.subheader("SEO Analysis Results")
            st.write(f"Title: {title}")
            st.write(f"Meta Description: {meta_desc}")
            st.write(f"Readability Score: {readability}")
            st.write(f"Word Count: {word_count}")
        except:
            st.error("Unable to analyze the website. Please check the URL.")
    else:
        st.warning("Please enter a valid URL.")
