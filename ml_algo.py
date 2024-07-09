from sklearn.ensemble import IsolationForest
import pandas as pd
import json

with open('starwars_sample_network_data.json') as f:
    json_data = json.load(f)

print(json.dumps(json_data, indent=4))

data = pd.DataFrame(json_data)
print(data)
features = data.drop('label', axis=1)
labels = data['label']

model = IsolationForest(n_estimators=100, contamination=0.01)
model.fit(features)

predictions = model.predict(features)
anomalies = data[predictions == -1]

print(anomalies)
