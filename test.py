import joblib
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

model = joblib.load("model/model.pkl")
iris = load_iris()
X, y = iris.data, iris.target
preds = model.predict(X)
print(f"✅ Accuracy: {accuracy_score(y, preds):.2f}")
