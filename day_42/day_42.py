import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB # lebelled dataset / continuous data
from sklearn.naive_bayes import MultinomialNB # text mining
from sklearn.naive_bayes import BernoulliNB # labelled dataset which has binary features(True or False, 1 or 0)
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("Iris.csv")
x = df.drop(columns = ["Species"])
y = df["Species"]

le = LabelEncoder()
y = le.fit_transform(y)
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, random_state = 42)
model = GaussianNB()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print(y_pred)

test = model.predict([[151, 3.5, 4.5, 6.1, 6.5]])
print(test)

from sklearn.metrics import accuracy_score, confusion_matrix

acc = accuracy_score(y_test, y_pred)
print(acc*100)

print("Confusion matrix")
print(confusion_matrix(y_test, y_pred))

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

df = pd.read_csv("Iris.csv")

x = df.drop(columns = ["Species"])
y = df["Species"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

model = SVC(kernel = "linear", C = 1.0)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print(y_pred)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.datasets import load_wine

data = load_wine()
df = pd.DataFrame(data.data, columns = data.feature_names)
df["target"] = data.target
x = df.drop(columns = ["target"])
y = df["target"]

le = LabelEncoder()
y = le.fit_transform(y)
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, random_state = 42)
model = GaussianNB()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print(y_pred)

test = model.predict([[13.2, 2.7, 2.5, 15.0, 100.0, 2.0, 2.5, 0.3, 1.5, 5.0, 1.0, 3.0, 1000]])
print(test)

from sklearn.metrics import accuracy_score, confusion_matrix

acc = accuracy_score(y_test, y_pred)
print(acc*100)

print("Confusion matrix")
print(confusion_matrix(y_test, y_pred))

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.datasets import load_wine

data = load_wine()
df = pd.DataFrame(data.data, columns = data.feature_names)
df["target"] = data.target
x = df.drop(columns = ["target"])
y = df["target"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

model = SVC(kernel = "linear", C = 1.0)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print(y_pred)