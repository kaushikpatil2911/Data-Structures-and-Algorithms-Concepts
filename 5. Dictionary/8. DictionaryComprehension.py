import random

my_dict = {'name': 'Edy','age': 27,'address': 'Austin','education':'masters'}

city_names = ['Paris','Rome','Mumbai','New York','Berlin']

city_dict = {city:random.randint(20,30) for city in city_names}
print(city_dict)

city_temp = {city:temp for (city,temp) in city_dict.items() if temp > 25}
print(city_temp)