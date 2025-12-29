# Food Sense AI

## Problem
Reading food labels is confusing. Ingredient names are long, technical, and it’s hard to quickly understand whether a product is okay to eat regularly or not. Most apps simply show ingredients or nutrition tables and leave the decision to the user.

## What This Project Does
Food Sense AI explains food ingredients in simple language and gives a basic decision:
- **OK**
- **Caution**
- **Avoid**

The goal is not medical accuracy, but to make food labels easier to understand at the moment of choice.

## How It Works
1. User selects a product or pastes ingredients  
2. User chooses who the food is for (daily use, children, fitness)  
3. The system analyzes common ingredient patterns  
4. A short explanation and decision is shown  

## Data
A small JSON file stores common food products and their ingredients.  
This keeps the demo consistent and easy to understand.

## Demo Note
The reasoning is simulated to keep the prototype stable during demos.  
The structure allows a real AI model to be added later without changing the interface.

## Tech Used
- Python  
- Streamlit  
- JSON  

## Limitations
- Ingredient quantities are not available  
- Logic is simplified  
- This is a prototype, not a health advisory tool  

## Future Improvements
- Connect to a real language model  
- Scan labels using camera  
- Compare similar products