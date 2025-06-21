def generate_marketing_prompt(topic, platform, tone):
    return f"""
You are a senior AI-powered content strategist.

Generate a high-converting post for **{platform}** on the topic:
\"\"\"{topic}\"\"\"

Tone: {tone}

The post should include:

1. **Hook (first 10 words)** – Scroll-stopper
2. **1–2 Valuable Insights** – Specific, no fluff
3. **Mini CTA** – “DM me”, “Save this”, “Tag a friend”, etc.
4. **Format Optimization** – Line breaks, hashtags (if needed), emojis (if platform allows)
5. **Optional Carousel/Thread Outline** – If suitable for platform

Also suggest **visual angle**, e.g., diagram, meme, case study, screenshot.

Goal: Maximize shares, saves, replies or click-through.
"""
