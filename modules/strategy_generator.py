def generate_strategy_prompt(user_input, client_type):
    return f"""
You are a senior strategy consultant with McKinsey-style precision.

Your client is a {client_type}. They described their situation as follows:
\"\"\"{user_input}\"\"\"

Generate a complete strategic plan with the following sections:

1. **Executive Summary** – 2-3 bullet overview of the business opportunity or challenge.
2. **Problem Analysis** – What is holding them back? Root causes and context.
3. **Opportunity Mapping** – Where is growth or impact possible?
4. **Strategic Initiatives** – 3–5 initiatives with justification and KPIs
5. **Tools/Technologies to Leverage**
6. **Risks to Mitigate**
7. **90-Day Action Roadmap**

Make the tone concise, data-driven, and decision-oriented. Include headings.
"""
