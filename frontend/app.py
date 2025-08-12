import streamlit as st
import requests

st.title("Social Media Post Generator (Mistral)")

topic = st.text_input("Enter topic:")
tone = st.selectbox("Select tone:", ["Casual", "Formal", "Friendly", "Professional", "Humorous"])
platform = st.selectbox("Select platform:", ["LinkedIn", "Twitter", "Instagram"])

if st.button("Generate Posts"):
    with st.spinner("Generating posts..."):
        res = requests.post(
            "http://localhost:8000/generate/",
            data={"topic": topic, "tone": tone, "platform": platform}
        )
        posts = res.json().get("posts", "Error")
        st.subheader("Generated Posts:")
        st.write(posts)
