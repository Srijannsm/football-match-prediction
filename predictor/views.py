import os
import pickle
import numpy as np
from django.shortcuts import render

with open('football_model.pkl','rb') as f:
    model = pickle.load(f)
    
with open('team_stats.pkl','rb') as f:
    team_stats = pickle.load(f)
    
all_teams = sorted(team_stats.keys())

def predict(request):
    result = None
    home_team = None
    away_team = None
    error = None
    
    if request.method == 'POST':
        home_team = request.POST['home_team']
        away_team = request.POST['away_team']
        
        if home_team == away_team:
            error = "Please select two different teams."
            
        elif home_team not in team_stats or away_team not in team_stats:
            error = "One or both teams not found in the database."
        
        else:
            home = team_stats[home_team]
            away = team_stats[away_team]
            
            feature = np.array([[
                home['win_rate'] - away['win_rate'],
                home['avg_goals_scored'] - away['avg_goals_scored'],
                home['avg_goals_conceded'] - away['avg_goals_conceded'],
            ]])
            
            prediction = model.predict(feature)[0]
            probabilties = model.predict_proba(feature)[0]
            classes = model.classes_
            
            prob_dict = dict(zip(classes, probabilties))
            
            home_win_prob = round(prob_dict.get('home_win', 0) * 100, 1)
            away_win_prob = round(prob_dict.get('away_win', 0) * 100, 1)
            draw_prob = round(prob_dict.get('draw', 0) * 100, 1)
            
            if prediction == 'home_win':
                result = f"{home_team} is likely to win! (Home Win: {home_win_prob}%, Draw: {draw_prob}%, Away Win: {away_win_prob}%)"
            elif prediction == 'away_win':
                result = f"{away_team} is likely to win! (Away Win: {away_win_prob}%, Draw: {draw_prob}%, Home Win: {home_win_prob}%)"  
            else:
                result = f"A draw is likely! (Draw: {draw_prob}%, Home Win: {home_win_prob}%, Away Win: {away_win_prob}%)"        
                                
    return render(request, 'predictor/predict.html', {
        'result': result,
        'home_team': home_team,
        'away_team': away_team,
        'error': error,
        'all_teams': all_teams,
        'home_win_prob': home_win_prob if result else None,
        'away_win_prob': away_win_prob if result else None,
        'draw_prob': draw_prob if result else None,
    })