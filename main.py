"""
Healthcare Data Analytics Project.
Computer Science Project
By: Abdul Rafay Ahsan
"""

'''
Main analysis, working and EDA along with prediction of datasets is done in the Jupyter notebook labeled:
FYP_Healthcare_Analysis_working
Refer to this file^^ for main source code

The main.py file was just for initialization.
'''


# main.py

import pandas as pd
from sklearn.linear_model import LinearRegression

patients = pd.read_csv("PatientDataset_updated.csv")

X = patients[['Age', 'Consultancy_Fee', 'Hospital_Fee']]
y = patients['Total_Cost']

#regr model training
model = LinearRegression()
model.fit(X, y)

#example
new_data = [[40, 5000, 2000]]
prediction = model.predict(new_data)

print("Predicted Treatment Cost:", round(prediction[0]))

