import json, datetime, random, os

apps = ["TataPower","Statiq","Zeon","JioBP","Electreefi"]
stations = ["DLF Phase 3","Cyber Hub","Select Citywalk"]
statuses = ["Available","Charging","Offline","Faulted"]

os.makedirs("output", exist_ok=True)

for app in apps:
    data = []
    for st in stations:
        data.append({
            "time": str(datetime.datetime.now()),
            "app": app,
            "station": st,
            "status": random.choice(statuses)
        })
        
    with open(f"output/{app}.json","w") as f:
        json.dump(data,f,indent=2)

print("Fake app data generated")
