# -*- coding: utf-8 -*-
"""Sales Prediction Using Python.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12wC-yFLvTna0PK42JNbK4ums6kbzveIv
"""

# Importing required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler

# Load the advertising dataset
file_path = 'advertising.csv'
data = pd.read_csv(file_path)

# Data Exploration
print("Dataset shape:", data.shape)
print("First few rows of the dataset:\n", data.head())
print("Summary statistics:\n", data.describe())

# Separate features and target
# Assuming the columns "TV", "Radio", "Newspaper" are advertising expenditures, and "Sales" is the target
X = data[['TV', 'Radio', 'Newspaper']]
y = data['Sales']

# Data Preprocessing
# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Model Training
# Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Model Prediction
y_pred = model.predict(X_test)

# Model Evaluation
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)
r2 = r2_score(y_test, y_pred)

print("Model Evaluation Metrics:")
print("Mean Squared Error (MSE):", mse)
print("Mean Absolute Error (MAE):", mae)
print("Root Mean Squared Error (RMSE):", rmse)
print("R-squared (R2) Score:", r2)