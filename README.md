# ⚽ Football Match Predictor

An AI-powered web app that predicts international football 
match outcomes using Machine Learning.

## Demo
![App Screenshot](screenshot.png)

## How It Works
1. Select home and away teams from 333 international teams
2. AI predicts the match outcome
3. See win probabilities for all three outcomes

## Technologies Used
- Python & Django (Backend)
- Scikit-learn Random Forest (ML Model)
- Pandas & NumPy (Data Processing)
- 49,287 historical matches (Dataset)

## ML Concepts Used
- Feature Engineering
- Random Forest Classifier
- Probability Prediction
- Model Persistence (Pickle)

## Model Performance
- Accuracy: 52.9%
- Baseline (random guessing): 33%
- Improvement over baseline: +19.9%

## How to Run Locally
1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate: `venv\Scripts\activate`
4. Install: `pip install -r requirements.txt`
5. Run: `python manage.py runserver`
6. Open: `http://127.0.0.1:8000`

## Author
Srijan Pradhan