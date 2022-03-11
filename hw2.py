from operator import itemgetter
from os import name

users_count = int(input("Enter users count: "))
users = []

if users_count > 0 :
    for i in range(0 , users_count):
        username = input("Enter user.name: ")
        user_age = input("Enter user.age: ")
        users.append({'name': username, 'age': user_age})
print(users)

search_name = input("Enter name to search: ")
search_age = next((item for item in users if item["name"] == search_name), None)
if search_age in users:
    print("age:", search_age['age'])
else:
    print("There is no user with given name!")

