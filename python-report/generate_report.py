import pandas as pd
import glob, json

files = glob.glob("output/*.json")
all_data = []

for file in files:
    with open(file) as f:
        all_data.extend(json.load(f))

df = pd.DataFrame(all_data)

pivot = df.pivot(index="station", columns="app", values="status")
pivot["Issue"] = pivot.apply(lambda x: "Mismatch" if len(set(x))>1 else "OK", axis=1)

pivot.to_excel("EV_Daily_Report.xlsx")
print("Report Generated")
