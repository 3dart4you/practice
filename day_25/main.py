# import csv
#
# with open('weather_data.csv') as data_file:
#     csv_file = csv.reader(data_file)
#     temperatures = []
#     for row in csv_file:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas

# data = pandas.read_csv('weather_data.csv')
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].to_list()
#
# average_temp = data['temp'].mean()
# print(average_temp)
#
# max_temp = max(data['temp'])
# print(max_temp)
#
# print(data['condition'])
# print(data.condition)
#
# print(data[data.day == 'Monday'])

# print(data[data.temp == max(data['temp'])])

# monday = data[data.day == 'Monday']
# print(monday.condition)
# print(monday.temp * 9/5 + 32)
# data_dict = {'students': ['Amy', 'James', 'Angela'],
#              'score': [76, 56, 65]
#              }

# data = pandas.DataFrame(data_dict)
# data.to_csv('new_data.csv')

import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
grey_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv('Squirrel_count.csv')