# Turimas "users" masyvas.

# Parašykite funkcijas, kurios atlikas nurodytas užduotis:
# 1. funkcija "getUserAverageAge" - kaip argumentą priims masyvą ir duoto masyvo
# atveju grąžins visų "users" amžiaus visurkį kaip skaičių.
# 2. funkcija "getUsersNames" -  kaip argumentą priims masyvą ir duoto masyvo
# atveju grąžins visų "users" vardus naujame list'e pvz., ['Alex John', 'Ann Smith'...].

# Pastaba: rezultatai turi būti išrikiuoti abėcėlės tvarka
from functools import reduce

users = [
    {"id": '1', "name": 'John Smith', "age": 20},
    {"id": '2', "name": 'Ann Smith', "age": 24},
    {"id": '3', "name": 'Tom Jones', "age": 31},
    {"id": '4', "name": 'Rose Peterson', "age": 17},
    {"id": '5', "name": 'Alex John', "age": 25},
    {"id": '6', "name": 'Ronald Jones', "age": 63},
    {"id": '7', "name": 'Elton Smith', "age": 16},
    {"id": '8', "name": 'Simon Peterson', "age": 30},
    {"id": '9', "name": 'Daniel Cane', "age": 51},
]


def getUserAverageAge(users):
    # suma = 0
    # for user in users:
    #     age = user.get('age')
    #     suma = suma + age
    # vidurkis = suma / len(users)
    # print(vidurkis)
    amziai = list(map(lambda user: user.get('age'), users))
    vidurkis = reduce(lambda x, y: x + y, amziai) / len(amziai)
    print(vidurkis)


getUserAverageAge(users)


def getUsersNames(users):
    # user_names = []
    # for user in users:
    #     user_name = user.get('name')
    #     user_names.append(user_name)
    # return user_names
    user_names = list(map(lambda user: user.get('name'), users))
    user_names.sort()
    return user_names


print(getUsersNames(users))
