# File: app.py

import streamlit as st
from modules.strategy_generator import generate_strategy_prompt
from modules.product_roadmap import generate_product_prompt
from modules.marketing_plan import generate_marketing_prompt
# from utils.gemini_api import generate_gemini_response  # Gemini temporarily disabled

try:
    st.set_page_config(page_title="Intellium Client Brain", layout="wide", page_icon="🧠")
except Exception as e:
    st.error(f"Error setting page config: {e}")
    st.set_page_config(page_title="Intellium Client Brain", layout="wide")  # Fallback without page_icon

st.title("🧠 Intellium Client Brain")
st.subheader("Generate AI-Powered Strategies, MVP Plans & Content That Close Deals")

client_type = st.sidebar.selectbox(
    "Select Client Type",
    ["Tech Startup", "Healthcare Company", "E-commerce Brand", "Logistics Firm", "SaaS Platform"]
)

use_case = st.sidebar.radio(
    "What do you want to generate?",
    ["Client Strategy Draft", "Product MVP Roadmap", "Marketing Content Plan"]
)

prompt = ""

if use_case == "Client Strategy Draft":
    user_input = st.text_area("Describe the client's business, problem, or idea:", height=200)
    if st.button("🧠 Generate Prompt"):
        if not user_input:
            st.warning("Please describe the client or business first.")
        else:
            prompt = generate_strategy_prompt(user_input, client_type)

elif use_case == "Product MVP Roadmap":
    idea = st.text_area("Describe your product idea")
    industry = st.text_input("Industry")
    target_user = st.text_input("Target User Persona")
    if st.button("🧠 Generate Prompt"):
        if not idea:
            st.warning("Please describe the product idea.")
        else:
            prompt = generate_product_prompt(idea, industry, target_user)

elif use_case == "Marketing Content Plan":
    topic = st.text_input("Content Topic")
    platform = st.selectbox("Platform", ["LinkedIn", "Twitter/X", "Instagram", "YouTube"])
    tone = st.selectbox("Tone", ["Professional", "Conversational", "Witty", "Story-driven"])
    if st.button("🧠 Generate Prompt"):
        if not topic:
            st.warning("Please enter a topic.")
        else:
            prompt = generate_marketing_prompt(topic, platform, tone)

if prompt:
    st.markdown("### 📋 Generated Prompt")
    st.code(prompt, language="markdown")

    # Use Streamlit's native copy-to-clipboard instead of custom HTML/JS
    if st.button("📋 Copy Prompt to Clipboard"):
        st.copy_to_clipboard(prompt)
        st.success("Prompt copied to clipboard!")

    # Gemini functionality disabled for now
    # if st.button("🚀 Run with Gemini AI"):
    #     with st.spinner("Thinking with Gemini..."):
    #         response = generate_gemini_response(prompt)
    #         st.markdown("### 🤖 Gemini Response")
    #         st.write(response)
