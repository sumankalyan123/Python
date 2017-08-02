dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
brics = pd.DataFrame(dict)
brics.index = ["BR", "RU", "IN", "CH", "SA"]
#print(brics)

cars = pd.read_csv('sample.csv')
#print(cars)

cars = pd.read_csv('sample.csv', index_col = 0)
# Print out cars
#print(cars)

# Print out cars

#print(cars['email'])
#print(cars[['email']])
#print(cars[['first_name', 'last_name']])
print(cars[0:4])
#print(cars[2:4])
print(cars.loc[3])

print(cars.loc[['Lorin', 'Gundry']])

#print(cars)