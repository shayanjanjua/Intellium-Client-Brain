def generate_product_prompt(idea, industry, target_user):
    return f"""
You are a lean startup product advisor.

Client idea:
\"\"\"{idea}\"\"\"

Industry: {industry}  
Target user persona: {target_user}

Write a product MVP roadmap:

1. **Problem Summary**
2. **Unique Value Proposition**
3. **Core Features (MVP only)** – Max 4. No fluff.
4. **Suggested Tech Stack** – Mention tools/languages.
5. **Build Timeline** – Phase-wise in 30-60-90 days.
6. **How to Validate MVP (with real users)**
7. **Metrics to Measure (North Star, activation, retention)**

End with: “If you had to build this MVP with $5k in 30 days, how would you prioritize?”
"""
