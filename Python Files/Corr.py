import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel("plotproject.xlsx", skiprows=2) #removed top 2 empty rows in the excel sheet
data = data.iloc[:, 1:] #removed leftmost empty column in excel sheet
data = data.set_index("Date") #Removes counter as index and sets date as index

data["Workout"] = data["Workout"].map({"Yes": 1, "No": 0}) #Map Yes/no strings into boolean values in dictionary
data["100+ g Protein taken"] = data["100+ g Protein taken"].map({"Yes": 1, "No": 0})
data["8+ hours sleep"] = data["8+ hours sleep"].map({"Yes": 1, "No": 0})

print(data.corr())
sns.heatmap(data.corr(), annot = True, cmap="YlGnBu") # provides a visual heatmap for the data correlation
plt.show()
