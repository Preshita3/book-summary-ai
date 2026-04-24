import streamlit as st
from openai import OpenAI

client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)

st.title("📚 AI Book Summary Generator")

book_name = st.text_input("Enter the book name:")

if st.button("Generate Summary"):
    if book_name:
        prompt = f"""
        Give a detailed 1000-word summary of the book "{book_name}".

        Structure:
        1. Overview
        2. Key Concepts
        3. Practical Lessons
        4. Final Takeaway
        """

        response = client.chat.completions.create(
           model="meta-llama/llama-3-8b-instruct",
            messages=[{"role": "user", "content": prompt}]
        )

        st.write(response.choices[0].message.content)
    else:
        st.warning("Please enter a book name.")