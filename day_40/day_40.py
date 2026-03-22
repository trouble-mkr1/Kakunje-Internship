# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.metrics import accuracy_score

# df = pd.read_csv("email_data.csv")
# print(df.columns)
# x = df.drop(columns = ["Category"])
# y = df["Category"]

# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)
# knn = KNeighborsClassifier(n_neighbors = 5)
# knn.fit(x_train, y_train)
# y_pred = knn.predict(x_test)
# acc = accuracy_score(y_test, y_pred)
# print(acc*100)
# y_p = knn.predict([x.iloc[0]])

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# print("Task 1: Study Time Analyzer\n")
# subs = ["Python", "JAVA", "C++"]
# hrs = [2, 6, 3]
# df = pd.DataFrame({"Subject": subs, "Hours": hrs})
# total = np.sum(df["Hours"])
# avg = np.mean(df["Hours"])
# print("Total:", total)
# print("Average:", avg)
# plt.bar(df["Subject"], df["Hours"])
# plt.title("Study Time")
# plt.show()

# print("==========================================================")
# ###################################################################
# ###################################################################

# print("Task 2: Daily Calorie Tracker\n")
# food = ["Rice", "Egg", "Milk"]
# cal = [200, 150, 100]
# df = pd.DataFrame({"Food": food, "Calories": cal})
# total = np.sum(df["Calories"])
# print("Total Calories:", total)
# plt.pie(df["Calories"], labels=df["Food"])
# plt.show()

# print("==========================================================")
# ###################################################################
# ###################################################################

# print("Task 3: Inventory Stock Analyzer\n")

# products = ["Mouse", "Keyboard", "Monitor"]
# qty = [30, 50, 15]
# df = pd.DataFrame({"Product": products, "Quantity": qty})
# total = np.sum(df["Quantity"])
# print("Total Stock:", total)
# plt.bar(df["Product"], df["Quantity"])
# plt.show()

# print("==========================================================")
# ###################################################################
# ###################################################################

# print("Task 4: Number Comparison Tool\n")

# num = np.random.randint(1, 100, 10)
# df = pd.DataFrame({"Numbers": num})
# print("list of numbers are: ", num)
# print("Max:", np.max(num))
# print("Min:", np.min(num))
# print("Avg:", np.mean(num))
# plt.plot(num)
# plt.show()

# print("==========================================================")
# ###################################################################
# ###################################################################

# print("Task 5: Game Score Tracker\n")

# players = ["Abdul", "Ash", "Rand"]
# scores = [91, 100, 60]
# df = pd.DataFrame({"Player": players, "Score": scores})
# print("Highest Score:", np.max(scores))
# plt.bar(df["Player"], df["Score"])
# plt.show()

# print("==========================================================")
# ###################################################################
# ###################################################################

print("Task 6: Traffic Count Analyzer\n")

hours = [1, 2, 3, 4, 5]
traffic = [50, 80, 120, 90, 60]
df = pd.DataFrame({"Hour": hours, "Traffic": traffic})
peak = df.iloc[np.argmax(traffic)]
print("Peak Hour:", peak["Hour"])
plt.plot(df["Hour"], df["Traffic"])
plt.show()

print("==========================================================")
###################################################################
###################################################################







