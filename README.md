Food Sense AI

Problem
Reading food labels is confusing.
Ingredient names are long, technical, and it’s hard to quickly understand whether a product is okay to eat regularly or not.
Most apps just show ingredients or nutrition tables and leave the decision to the user.

What this project does
Food Sense AI helps explain food ingredients in simple language and gives a basic decision like OK, Caution, or Avoid.
The goal is not to be medically accurate, but to make labels easier to understand at the moment of choice.

How it works
User selects a product or pastes ingredients
User chooses who the food is for (daily use, children, fitness)
The system analyzes common ingredient patterns
A short explanation and decision is shown

Data
A small JSON file is used to store common food products and their ingredients.
This keeps the demo consistent and easy to understand.

Demo note
The reasoning is simulated to keep the prototype stable during demos.
The structure allows an actual AI model to be added later without changing the interface.

Tech used
Python
Streamlit
JSON

Limitations
Ingredient quantities are not available
The logic is simplified
This is a prototype, not a health advisory tool

Future improvements
Connect to a real language model
Scan labels using camera
Compare similar products

Hackathon prototype focused on clarity and usability.