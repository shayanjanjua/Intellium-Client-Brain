import streamlit as st
from PIL import Image
from modules.strategy_generator import generate_strategy_prompt
from modules.product_roadmap import generate_product_prompt
from modules.marketing_plan import generate_marketing_prompt
# from utils.gemini_api import generate_gemini_response  # Gemini temporarily disabled

st.set_page_config(page_title="Intellium Client Brain", layout="wide")

# ✅ Add logo to sidebar (top position)
try:
    logo = Image.open("logo.png")  # Make sure logo.png is in the same folder as app.py
    st.sidebar.image(logo, use_container_width=True)
except Exception:
    st.sidebar.markdown("## 🧠 Intellium")

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

    # 📋 Show true copy-to-clipboard button via custom Streamlit markdown + JS hack
    st.markdown("""
    <button onclick="navigator.clipboard.writeText(document.getElementById('copy-target').innerText)"
            style="margin-top: 10px; padding: 0.5em 1em; background-color: #4CAF50; color: white; border: none; border-radius: 5px; cursor: pointer;">
        📋 Copy Prompt to Clipboard
    </button>
    <pre id='copy-target' style='display: none;'>
    {}</pre>
    """.format(prompt), unsafe_allow_html=True)

    # Gemini functionality disabled for now
    # if st.button("🚀 Run with Gemini AI"):
    #     with st.spinner("Thinking with Gemini..."):
    #         response = generate_gemini_response(prompt)
    #         st.markdown("### 🤖 Gemini Response")
    #         st.write(response)
