# file for dataset preprocessing; cleaning/formating/analyzing..
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Medicines.csv')

print(df.to_string())

#Visualization
df.plot()
plt.show()

# Different factors relation
# number 1: Age with BP
df.plot(kind = "scatter", x = "Age", y = "BP")
plt.show()
