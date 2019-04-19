import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)

data = pd.read_csv('')

# get data csv file, segregate train and test data. do model coding later. 
# knn.fit(X, y)