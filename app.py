import streamlit as st
import json

with open("products.json","r", encoding="utf-8") as f:
    products = json.load(f)
# --------------------
# CONFIG
# --------------------
st.set_page_config(
    page_title="FoodSense AI",
    page_icon="🥗",
    layout="centered"
)
st.markdown("""
<h1 style='text-align: center;'>🥗 FoodSense AI</h1>
<p style='text-align: center; color: grey;'>
Understand food ingredients in plain language
</p>
<hr>
""", unsafe_allow_html=True)
st.markdown("""
<style>
.card {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.badge-ok {
    background-color: #e8f5e9;
    padding: 15px;
    border-radius: 10px;
    font-weight: bold;
}

.badge-caution {
    background-color: #fff8e1;
    padding: 15px;
    border-radius: 10px;
    font-weight: bold;
}

.badge-avoid {
    background-color: #fdecea;
    padding: 15px;
    border-radius: 10px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)
# --------------------
# USER INPUT
# --------------------

product_names = [p["name"] for p in products]

selected_product_name = st.selectbox(
    "🛒 Choose a product (or paste manually below)",
    ["-- Select a product --"] + product_names
)

ingredients = ""

if selected_product_name != "-- Select a product --":
    selected_product = next(
        p for p in products if p["name"] == selected_product_name
    )
    ingredients = selected_product["ingredients"]

ingredients = st.text_area(
    "📦 Ingredients",
    value=ingredients,
    placeholder="Paste ingredients here if product not listed"
)

goal = st.selectbox(
    "🎯 Who is this food for?",
    ["Daily eating", "Children", "Fitness / Weight loss"]
)

st.markdown("</div>", unsafe_allow_html=True)
# --------------------
# PROMPT FUNCTION
# --------------------
def mock_ai_response(ingredients, goal):
    ingredients_lower = ingredients.lower()

    mild_risks = []
    moderate_risks = []
    high_risks = []
    benefits = []

    # Mild (acceptable daily)
    if "sugar" in ingredients_lower:
        mild_risks.append("Contains added sugar")

    if "wheat" in ingredients_lower or "atta" in ingredients_lower:
        benefits.append("Provides basic carbohydrates for energy")

    # Moderate (limit frequency)
    if "palm oil" in ingredients_lower:
        moderate_risks.append("Uses palm oil, which is higher in saturated fat")

    if "glucose syrup" in ingredients_lower:
        moderate_risks.append("Contains glucose syrup")

    # High risk (strong warning)
    if "caffeine" in ingredients_lower:
        high_risks.append("Contains caffeine, not ideal for children")

    # 🎯 Decision logic based on GOAL
    if goal == "Children":
        if high_risks:
            decision = "AVOID"
        elif moderate_risks:
            decision = "CAUTION"
        else:
            decision = "OK"

    elif goal == "Fitness / Weight loss":
        if "sugar" in ingredients_lower or high_risks:
            decision = "CAUTION"
        elif moderate_risks:
            decision = "CAUTION"
        else:
            decision = "OK"

    else:  # Daily eating
        if high_risks:
            decision = "AVOID"
        elif len(moderate_risks) >= 2:
            decision = "CAUTION"
        else:
            decision = "OK"

    response = f"""
Decision: {decision}

Why:
- This decision considers ingredient type and consumption frequency

What’s Good:
- {', '.join(benefits) if benefits else 'No major nutritional benefits'}

What to Limit:
- {', '.join(moderate_risks) if moderate_risks else 'Nothing significant'}

What to Watch:
- {', '.join(high_risks) if high_risks else 'No high-risk ingredients detected'}

Trade-offs:
- Some ingredients improve taste, shelf life, and affordability

Uncertainty:
- Exact ingredient quantities are not disclosed on labels
"""

    return decision, response
# --------------------
# AI CALL
# --------------------
# --------------------
# AI CALL + RESULT
# --------------------
if st.button("🤖 Explain Like a Human"):
    if ingredients.strip() == "":
        st.warning("Please paste ingredients first.")
    else:
        with st.spinner("Thinking like a smart co-pilot..."):
            decision, answer = mock_ai_response(ingredients, goal)

        st.subheader("📊 Result")
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        if decision == "OK":
            st.markdown(
                "<div class='badge-ok'>🟢 OK for daily consumption</div>",
                unsafe_allow_html=True
            )
        elif decision == "CAUTION":
            st.markdown(
                "<div class='badge-caution'>🟡 Consume with caution</div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                "<div class='badge-avoid'>🔴 Better to avoid</div>",
                unsafe_allow_html=True
            )

        st.markdown("### 🧠 Explanation")
        st.write(answer)

        st.caption(
            "ℹ️ This explanation is based on common ingredient patterns. "
            "Exact quantities are not disclosed on food labels."
        )

        st.markdown("</div>", unsafe_allow_html=True)
st.markdown("""
<div class="card">
<strong>Why this helps:</strong><br>
Instead of reading long ingredient lists, this system explains:
<ul>
<li>What matters</li>
<li>What to be cautious about</li>
<li>What is uncertain</li>
</ul>
So decisions can be made faster.
</div>
""", unsafe_allow_html=True)