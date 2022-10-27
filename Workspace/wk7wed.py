import pandas as pd
from pathlib import Path 


datapath = Path("data") / "records.txt"
df = pd.read_csv(datapath, sep=",")
print(df["W"][5])
print(df.loc[5, "W"])
print(df.iloc[5, 1])

def ratio(row):
    w = row["W"]
    l = row["L"]
    return int(w)/int(l)

df["newcol"] = 0

df["ratio"] = df.apply(lambda row: ratio(row), axis=1)
idx_max = df["ratio"].idxmax()
print(df.loc[idx_max, "Team"])

outfile = Path("data") / "baseball_edited.csv"

df.to_csv(outfile, index = False)

