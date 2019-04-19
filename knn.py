import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv('TESTdata.csv')

data.drop(['Emp_ID'], axis=1)

# get data csv file, segregate train and test data. do model coding later. 
# knn = KNeighborsClassifier(n_neighbors=1)
# knn.fit(X, y)