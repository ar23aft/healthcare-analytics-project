"""
Healthcare Data Analytics Project.
Computer Science Project
By: Abdul Rafay Ahsan
"""

'''
Main analysis, working and EDA along with prediction of datasets is done in the Jupyter notebook labeled:
FYP_Healthcare_Analysis_working
'''


# main.py

import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
patients = pd.read_csv("PatientDataset_updated.csv")

# Select features
X = patients[['Age', 'Consultancy_Fee', 'Hospital_Fee']]
y = patients['Total_Cost']

# Train model
model = LinearRegression()
model.fit(X, y)

# Example prediction
new_data = [[40, 5000, 2000]]
prediction = model.predict(new_data)

print("Predicted Treatment Cost:", round(prediction[0]))

