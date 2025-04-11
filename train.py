import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
from sklearn.datasets import load_iris
import os

iris = load_iris()
X, y = iris.data, iris.target
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)
os.makedirs('model', exist_ok=True)
joblib.dump(model, 'model/model.pkl')
print("✅ Model trained and saved.")
