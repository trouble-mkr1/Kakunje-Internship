import pandas as pd

l = [1, 2, 3, 4, 5, 6]
s = pd.Series(l)
print(s)

print(s[4])

s = pd.Series(l, index = ['a', 'b', 'c', 'd', 'e', 'f'])
print(s)
print(s['c'])


# data frame

data = {"Name": ["Alice", "Bob", "Charles"],
        "Age": [20, 25, 22]
        }
df = pd.DataFrame(data)
print(df)
print(df.loc[2])
print(df.loc[1:])


# Load files into a database

df = pd.read_csv("data.csv")
print(df)
print(df.info())
print(df.head(15))
print(df.tail(15))
print(df.sample(20)) # to pick random "20" rows
print(df.describe()) # gives statistical value
print(df.columns)
print(df.dtypes)
print(df.shape) #gives rows x colums, eg: (45, 70)
print(df['Pulse'])
print(df[['Pulse', 'Calories']])
print(df['Pulse'].unique())
print(df['Pulse'].value_counts())
df.rename(columns = {'Calories': 'Calories_burnt'}, inplace = True)
print(df)
null = df.isna().sum()
print(f"number of null values is: {null}")


'''
· LoadCSVfile
· Display summary statistics
· Fetch age column
· Rename age → student_age
· Fill NULL score using mean
· Fill NULL age using median
· Remove duplicates
· Fetch top 5 students
· Fetch bottom 5 students
· Fetch random 3 students
· Removerowswith invalid data
· Save cleaned CSV
'''
print("task outputs\n")

df = pd.read_csv("students.csv")
print(df, "\n")
print(df.info(), "\n")
print(df["age"], "\n")
df.rename(columns = {"age": "student_age"}, inplace = True)
print(df, "\n")
df["marks"] = pd.to_numeric(df["marks"], errors="coerce")
df["marks"] = df["marks"].fillna(df["marks"].mean())
df["student_age"] = df["student_age"].fillna(df["student_age"].median())
print(df, "\n")
df.drop_duplicates(inplace=True)
print(df, "\n")
print(df.head(5), "\n")
print(df.tail(5), "\n")
print(df.sample(3), "\n")
df = df[(df["student_age"] > 0) & (df["marks"] >= 0)]
print(df, "\n")
df.to_csv("students_cleaned.csv", index=False)