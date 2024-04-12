import pandas as pd
import numpy as np
from flask import Flask, render_template

app = Flask(__name__)

# read in csv
games_details_path = "resources/games_details_cleaned.csv"
games_details_df = pd.read_csv(games_details_path)

# format df
games_details_df = games_details_df.drop(['TEAM_ABBREVIATION', 'TEAM_CITY', 'NICKNAME', 'COMMENT', 'MIN'], axis=1)
games_details_clean = games_details_df.dropna()

# get filtered df's for forwards, guards, and centers
forwards_df = games_details_df.loc[games_details_df['START_POSITION'] == 'F']
guards_df = games_details_df.loc[games_details_df['START_POSITION'] == 'G']
center_df = games_details_df.loc[games_details_df['START_POSITION'] == 'C']

# drop unneccesary columns for the three df's
center_df = center_df.drop(['games_details_PK', 'GAME_ID', 'TEAM_ID', 'PLAYER_ID', 'PLAYER_NAME', 'START_POSITION', 'FGA - field goals attempted', 'FGA - field goals attempted', 'FG_PCT field goal percentage', 'FG3A - 3 point field goals attempted', 'FG3_PCT - field goal 3 point percentage', 'FTA - free throws attempted', 'FT_PCT - free throws percentage', 'PF - personal fouls', 'PTS - points', 'PLUS_MINUS'], axis=1)
forwards_df = forwards_df.drop(['games_details_PK', 'GAME_ID', 'TEAM_ID', 'PLAYER_ID', 'PLAYER_NAME', 'START_POSITION', 'FGA - field goals attempted', 'FGA - field goals attempted', 'FG_PCT field goal percentage', 'FG3A - 3 point field goals attempted', 'FG3_PCT - field goal 3 point percentage', 'FTA - free throws attempted', 'FT_PCT - free throws percentage', 'PF - personal fouls', 'PTS - points', 'PLUS_MINUS'], axis=1)
guards_df = guards_df.drop(['games_details_PK', 'GAME_ID', 'TEAM_ID', 'PLAYER_ID', 'PLAYER_NAME', 'START_POSITION', 'FGA - field goals attempted', 'FGA - field goals attempted', 'FG_PCT field goal percentage', 'FG3A - 3 point field goals attempted', 'FG3_PCT - field goal 3 point percentage', 'FTA - free throws attempted', 'FT_PCT - free throws percentage', 'PF - personal fouls', 'PTS - points', 'PLUS_MINUS'], axis=1)

# now that all the unnecessary things are out (and non-numbers), get average stats for each position. these all return arrays of the averages.
guard_avgs = guards_df.mean().values
center_avgs = center_df.mean().values
forward_avgs = forwards_df.mean().values

# define variable for team structure
length_all = guard_avgs.__len__()
g6 = 6 * guard_avgs
f2 = 2 * forward_avgs
c2 = 2 * center_avgs
sum_g6_f2_c2 = g6 + f2 + c2
g6_f2_c2 = sum_g6_f2_c2 / length_all

@app.route("/win_lose")
def win_lose():
    randoms = []
    columns = ['FGM - field goals made', 'FG3M - 3 point field goals made', 'FTM - free throws made', 'OREB - offensive rebound', 'DREB - defensive rebound', 'REB - rebound', 'AST - assist', 'STL - steal', 'BLK - block', 'TO - turnover']

    for c in columns:
        random_figure = games_details_clean[c].sample(n=1).values[0]
        randoms.append(random_figure)

    indv_value = [x-y for x,y in zip(g6_f2_c2, randoms)]

    wins = []
    for value in indv_value:
        if value > 0:
            wins.append('w')
        elif value < 0:
            wins.append('L')
        else:
            wins.append('T')

    count_wins = wins.count('w')
    count_losses = wins.count('L')
    count_ties = wins.count('T')

    if count_wins > count_losses:
        return_stuff = "<p>You won!</span></p><input type='button' onclick='document.location.href=\"http://127.0.0.1:5000/win_lose\"' value=\"click here\"></button><p></p><p></p><p></p><p></p><img src=\"https://c8.alamy.com/comp/M4RBC1/basketball-award-vector-red-ribbon-big-sport-game-win-banner-background-M4RBC1.jpg\" width=900 height=900/>"
    elif count_losses > count_ties:
        return_stuff = "<p>You lost!</p><input type='button' onclick='document.location.href=\"http://127.0.0.1:5000/win_lose\"' value=\"click here\"></button><p></p><p></p><p></p><p></p><img src=\"https://ih1.redbubble.net/image.473641510.8089/flat,750x,075,f-pad,750x1000,f8f8f8.u5.jpg\" width=700 height=800/>"
    else:
        return_stuff = "<p>You tied!</p><input type='button' onclick='document.location.href=\"http://127.0.0.1:5000/win_lose\"' value=\"click here\"></button>"
    
    return(return_stuff)

@app.route("/normal")
def index():
    result = win_lose()
    return result

if __name__ == '__main__':
    app.run(debug=True)