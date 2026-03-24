import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("Iris.csv")
x = df.drop(columns = ["Species"])
y = df["Species"]

le = LabelEncoder()
y = le.fit_transform(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)
model = DecisionTreeClassifier(criterion = "gini", max_depth = 3)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print(y_pred)
print("=============")
df = pd.read_csv("Iris.csv")
x = df.drop(columns = ["Species"])
y = df["Species"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)
model = RandomForestClassifier(criterion = "gini", n_estimators = 10)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print(y_pred)
###############################################################
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("email_data.csv")
x = df.drop(columns = ["Category"])
y = df["Category"]

le = LabelEncoder()
y = le.fit_transform(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)
model = DecisionTreeClassifier(criterion = "gini", max_depth = 2)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print(y_pred)
print("=============")
df = pd.read_csv("email_data.csv")
x = df.drop(columns = ["Category"])
y = df["Category"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)
model = RandomForestClassifier(criterion = "gini", n_estimators = 10)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print(y_pred)

##############################
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("email_data.csv")

x = df["Message"]
y = df["Category"]

le = LabelEncoder()
y = le.fit_transform(y)

vectorizer = TfidfVectorizer()
x = vectorizer.fit_transform(x)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier(criterion="gini", max_depth=3)
model.fit(x_train, y_train)
pred = model.predict(x_test)
print("Decision Tree Predictions:")
print(pred)

print("=============")

model = RandomForestClassifier(criterion="gini", n_estimators=10)
model.fit(x_train, y_train)
pred = model.predict(x_test)
print("Random Forest Predictions:")
print(pred)