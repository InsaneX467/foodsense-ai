import streamlit as st
import json

with open("products.json","r", encoding="utf-8") as f:
    products = json.load(f)
# --------------------
# CONFIG
# --------------------
st.set_page_config(page_title="AI Health Co-Pilot", page_icon="🧠")



st.title("🧠 AI Health Co-Pilot")
st.write("Understand food ingredients without the confusion.")

# --------------------
# USER INPUT
# --------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

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

st.markdown('</div>', unsafe_allow_html=True)
# --------------------
# PROMPT FUNCTION
# --------------------
def mock_ai_response(ingredients, goal):
    ingredients_lower = ingredients.lower()

    risky = []
    good = []

    if "sugar" in ingredients_lower:
        risky.append("High sugar content can affect long-term health")
    if "palm oil" in ingredients_lower:
        risky.append("Palm oil is linked to higher saturated fat intake")
    if "e211" in ingredients_lower or "preservative" in ingredients_lower:
        risky.append("Preservatives should be limited for frequent consumption")

    if "wheat" in ingredients_lower or "oats" in ingredients_lower:
        good.append("Provides basic energy")

    if len(risky) >= 2:
        decision = "AVOID"
    elif len(risky) == 1:
        decision = "CAUTION"
    else:
        decision = "OK"

    response = f"""
Decision: {decision}

Reasoning:
- This decision is based on ingredient balance and frequency of consumption

What’s Good:
- {', '.join(good) if good else 'No major benefits'}

What’s Risky:
- {', '.join(risky) if risky else 'No major risks'}

Trade-offs:
- These ingredients are commonly used to improve taste, shelf life, and cost

Uncertainty:
- Exact quantities of ingredients are not disclosed on the label
"""
    return response

# --------------------
# AI CALL
# --------------------
if st.button("Explain like a Human"):
    if ingredients.strip() == "":
        st.warning("Please paste ingredients first.")
    else:
        with st.spinner("Thinking like a smart co-pilot..."):
            answer = mock_ai_response(ingredients, goal)

            lines = answer.split("\n")
            decision_line = lines[0].lower()

            st.markdown('<div class="card">', unsafe_allow_html=True)

            if "ok" in decision_line:
                st.markdown('<div class="badge-ok">🟢 OK to consume</div>', unsafe_allow_html=True)
            elif "caution" in decision_line:
                st.markdown('<div class="badge-caution">🟡 Consume with caution</div>', unsafe_allow_html=True)
            elif "avoid" in decision_line:
                st.markdown('<div class="badge-avoid">🔴 Better to avoid</div>', unsafe_allow_html=True)

            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown("---")
            st.write(answer)

st.markdown("""
<div class="card">
<strong>Why this helps:</strong><br>
Instead of reading long ingredient lists, this AI explains:
<ul>
<li>What matters</li>
<li>What to be cautious about</li>
<li>What is uncertain</li>
</ul>
So you can decide faster.
</div>
""", unsafe_allow_html=True)
