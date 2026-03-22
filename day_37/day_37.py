# m = [
#     [2, 4, 6],
#     [1, 3, 5],
#     [7, 9, 8]
# ]

# for row in m:
#     print(row)
# print()
# for i in range(2):
#     print(m[i][2])
# print()
# m[2][0] = 700
# for row in m:
#     print(row)
# print()
# sum = 0
# for row in m:
#     for num in row:
#         sum += num
# print("\nSum of elements:", sum)
# print()
# print(m[1][0], m[1][2], m[2][1])

import pandas as pd
# from sklearn.datasets import load_iris
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# iris = load_iris()
# df = pd.read_csv("Iris.csv")
# x = df.drop(columns = ["Species"])
# y = df["Species"]
data = load_digits()
df = pd.DataFrame(data.data)
df["Species"] = data.target
x = df.drop(columns=["Species"])
y = df["Species"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)
acc = accuracy_score(y_test, y_pred)
print(acc*100)
y_p = knn.predict([x.iloc[0]])
# print(df)