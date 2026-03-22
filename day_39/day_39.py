# m=[
#    [1,2,3],
#    [4,5,6],
#    [7,8,9]
# ]

# row_sum=[sum(row) for row in m]
# print(row_sum,end=" ")
# print()

# col_sum=[]
# for i in range(len(m[0])):
#    total=0
#    for row in m:
#        total+=row[i]
#    col_sum.append(total)
# print("Column Sum:", col_sum)


# from sklearn.preprocessing import LabelEncoder
# color=["black","white","red","yellow","white","black"]

# le=LabelEncoder()
# en=le.fit_transform(color)

# print("Original :",color)
# print("Encoded: ",en)


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd

data=pd.read_csv("Housing.csv")
data=data.replace(['yes','no','furnished','semi-furnished','unfurnished'],
                  [True,False,1,0.5,0])
data=data.infer_objects(copy=False)
x=data.drop(['price'],axis=1)
y=data['price']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
model=LinearRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print(model.predict(pd.DataFrame([[16200,3,2,2,False,True,True,False,True,3,False,1.5]],columns=x.columns)))




from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd

data=pd.read_csv("iris.csv")
data=data.replace(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'], [0, 1, 2])
data=data.infer_objects(copy = False)
x = data.drop(['Species', 'Id'], axis = 1)
y = data['Species']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)
model = LinearRegression()
model.fit(x_train, y_train)
y_pred=model.predict(x_test)
print(model.predict(pd.DataFrame([[5.1, 3.5, 1.4, 0.2]],columns=x.columns)))

