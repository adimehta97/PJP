import pandas as pd

data = pd.read_csv('TESTdata.csv')
data = data.drop(['Emp_ID'], axis=1)

# print(data)
totalHours = data.sum(axis=1,skipna=True)
averageHours = totalHours.mean()

data['total_hours']= totalHours
data.to_csv('sample_test_data.csv')
print(data)