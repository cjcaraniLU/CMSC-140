import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd

def plot_temps(filepath):
    temps = []
    hats = []
    filepath = Path("data") / "hats.txt"
    with open(filepath) as f:
        next(f)
        for line in f.readlines():
            t, h = line.strip().split(" ")
            temps.append(int(t))
            hats.append(int(h))
    plt.scatter(temps, hats)
    plt.show()

def get_temp(filename):
    max_hats = 0
    max_temp = 0
    with open(filename) as f:
        next(f)
        for line in f.readlines():
            t, h = line.strip().split(" ")
            t = int(t)
            h = int(h)
            if h > max_hats:
                max_hats = h
                max_temp = temps
    return max_temp

filepath_bb = Path("data") / "records.txt"
def get_team (filepath_bb): 
    with open(filepath_bb) as f: 
        next(f)
        best_p = 0.0
        best_team = " "
        for line in f.readlines():
            name, wins, loss = line.strip().split(",")
            wins = int(wins)
            loss = int(loss)
            p = wins/loss
            if(best_p < p):
                best_team = name
                best_p = p
    return best_team

#winner = get_team(filepath_bb)
#print(winner)
    

prof_info = {
    "Ackles" : {
        "classes": ["Python", "Algorithms"],
        "office": "Steitz 131",
        "firstname": "Acacia"
    },
    "Krebsbach" : {
        "classes": ["Java", "FYS"],
        "office": "Briggs 411"
    },
    "Gregg" : {
        "classes": ["Web Devel", "Algorithms"],
        "office": "Briggs 413"

    }
}
df = pd.DataFrame(data=prof_info)
#print(df)

#print(df.loc["classes", "Ackles"])
#print(df.iloc[1,2])

teams_df = pd.read_csv(filepath_bb, sep = ',')
print(teams_df)

def win_loss(row):
    win = row["W"]
    loss = row["L"]
    return int(win)/int(loss)
teams_df["ratio"] = df.apply(lambda row: win_loss(row), axis = 1)