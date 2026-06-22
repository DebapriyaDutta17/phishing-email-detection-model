# phishing_detector.py

import pandas as pd
import re

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import FeatureUnion
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

import seaborn as sns
import matplotlib.pyplot as plt


# ---------------------------
# URL Feature Extractor
# ---------------------------

class URLFeatureExtractor(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        features = []

        for text in X:
            url_count = len(re.findall(r'http[s]?://', str(text)))
            features.append([url_count])

        return features


# ---------------------------
# Load Dataset
# ---------------------------

df = pd.read_csv("emails.csv")

X = df["text"]
y = df["label"]


# ---------------------------
# Feature Engineering
# ---------------------------

from sklearn.pipeline import Pipeline

combined_features = FeatureUnion([
    ("tfidf", TfidfVectorizer(stop_words="english")),
    ("url_features", Pipeline([
        ("extract", URLFeatureExtractor())
    ]))
])

X_features = combined_features.fit_transform(X)


# ---------------------------
# Train-Test Split
# ---------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X_features,
    y,
    test_size=0.2,
    random_state=42
)


# ---------------------------
# Model Training
# ---------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)


# ---------------------------
# Prediction
# ---------------------------

y_pred = model.predict(X_test)


# ---------------------------
# Evaluation
# ---------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# ---------------------------
# Confusion Matrix
# ---------------------------

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6,4))
sns.heatmap(
    cm,
    annot=True,
    fmt='d'
)

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()


# ---------------------------
# Email Testing
# ---------------------------

while True:

    email = input("\nEnter Email Text (or 'quit'): ")

    if email.lower() == "quit":
        break

    sample = combined_features.transform([email])

    prediction = model.predict(sample)[0]

    if prediction == 1:
        print("⚠️ Phishing Email Detected")
    else:
        print("✅ Safe Email")
