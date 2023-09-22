import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as MultipleLocator
import seaborn as sns

data = pd.read_excel("plotproject.xlsx", skiprows=2) #removed top 2 empty rows in the excel sheet
data = data.iloc[:, 1:] #removed leftmost empty column in excel sheet
data = data.set_index("Date") #Removes counter as index and sets date as index

data["Workout"] = data["Workout"].map({"Yes": 1, "No": 0}) #Map Yes/no strings into boolean values in dictionary
data["100+ g Protein taken"] = data["100+ g Protein taken"].map({"Yes": 1, "No": 0})
data["8+ hours sleep"] = data["8+ hours sleep"].map({"Yes": 1, "No": 0})

fig, axs = plt.subplots(4, 1) #show 4 separate graphs in a single column

axs[0].bar(data.index, data["Workout"])
axs[0].set_title("Did I workout today?")
axs[0].set_xlabel("Date")
axs[0].set_yticklabels(labels = ["No", "Yes"]) #Sets y axis labels to yes and no rather than 0 and 1

axs[1].plot(data.index, data["Water consumption"])
axs[1].set_title("How much water did I drink today?")
axs[1].set_xlabel("Date")
axs[1].set_ylabel("Water (cups)")

axs[2].bar(data.index, data["100+ g Protein taken"])
axs[2].set_title("Did I get enough protein today?")
axs[2].set_xlabel("Date")
axs[2].set_yticklabels(labels = ["No", "Yes"])

axs[3].bar(data.index, data["8+ hours sleep"])
axs[3].set_title("Did I get enough sleep?")
axs[3].set_xlabel("Date")
axs[3].set_yticklabels(labels = ["No", "Yes"])

plt.tight_layout()
plt.show()




