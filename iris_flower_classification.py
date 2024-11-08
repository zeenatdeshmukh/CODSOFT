# -*- coding: utf-8 -*-
"""Iris Flower Classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10l9jI-b4w0XQU4cPJ1OQgiZ2LwQeZlor
"""

# Importing required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

# Load the Iris dataset
file_path = 'IRIS.csv'
data = pd.read_csv(file_path)

# Data Exploration
print("Dataset shape:", data.shape)
print("First few rows of the dataset:\n", data.head())
print("Class distribution:\n", data['species'].value_counts())

# Separate features and target
# Assuming the columns "sepal_length", "sepal_width", "petal_length", and "petal_width" are features
# and "species" is the target variable
X = data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y = data['species']

# Data Preprocessing
# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Model Training
# Initialize the Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Model Prediction
y_pred = model.predict(X_test)

# Model Evaluation
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print("Model Accuracy:", accuracy)
print("\nClassification Report:\n", classification_rep)
print("\nConfusion Matrix:\n", conf_matrix)