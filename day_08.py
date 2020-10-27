import json

class Persons:
    def __init__(self, id, name, fname, county, age, is_teen):
        self.id = id
        self.name = name
        self.fname = fname
        self.county = county
        self.age = age
        self.is_teen = is_teen

    # Получить всех пользователей из указанной страны.
    def from_same_county(self, county):
        return self.county == county

    # Получить всех пользователей указанного возраста.
    def same_age(self, age):
        return self.age == age

    # Получить всех пользователей старше указанного возраста.
    def older_then(self, age):
        return self.age > age

    # Получить всех пользователей младше указанного возраста или равного ему.
    def same_or_younger(self, age):
        return self.age <= age

    # Получить всех совершеннолетних. Россия (с 18 лет), Япония (с 20 лет), США (с 21 года) и Тайланд (с 20 лет)
    def get_adults(self):
        return (self.age >= 18 and self.county == "Russia") or \
               (self.age >= 20 and self.county == "Japan") or \
               (self.age >= 21 and self.county == "USA") or \
               (self.age >= 20 and self.county == "Thailand")

    # Получить всех тинов.
    def get_teen(self):
        return not self.get_adults()

    # wrong age group
    def wrong_age_group(self):
        return self.get_adults() == self.is_teen


with open('users_ds.json') as in_file:
    users = json.load(in_file)

current_county = input("Find users from same country. Enter county: ")
for person in users:
    user = Persons(person.get('id'), person.get('name'), person.get('fname'), person.get('county'), person.get('age'), person.get('is_teen'))
    if user.from_same_county(current_county):
        print(user.name, user.fname, user.county, user.age, user.is_teen)

print("Find users with same age or younger. Enter age: ")
s_age = int(input())
for person in users:
    user = Persons(person.get('id'), person.get('name'), person.get('fname'), person.get('county'), person.get('age'), person.get('is_teen'))
    if user.same_or_younger(s_age):
        print(user.name, user.fname, user.county, user.age)

print("Users with same age. ")
same_age = int(input())
for person in users:
    user = Persons(person.get('id'), person.get('name'), person.get('fname'), person.get('county'), person.get('age'), person.get('is_teen'))
    if user.same_age(same_age):
        print(user.name, user.fname, user.county, user.age, user.is_teen)

print("Users older than: ")
old_age = int(input())
for person in users:
    user = Persons(person.get('id'), person.get('name'), person.get('fname'), person.get('county'), person.get('age'), person.get('is_teen'))
    if user.older_then(old_age):
        print(user.name, user.fname, user.county, user.age, user.is_teen)

print("There are teenagers. ")
for person in users:
    user = Persons(person.get('id'), person.get('name'), person.get('fname'), person.get('county'), person.get('age'), person.get('is_teen'))
    if user.get_teen():
        print(user.name, user.fname, user.county, user.age)

print("There are adults.")
for person in users:
    user = Persons(person.get('id'), person.get('name'), person.get('fname'), person.get('county'), person.get('age'), person.get('is_teen'))
    if user.get_adults():
        print(user.name, user.fname, user.county, user.age)

print("Wrong age group. ")
for person in users:
    user = Persons(person.get('id'), person.get('name'), person.get('fname'), person.get('county'), person.get('age'), person.get('is_teen'))
    if user.wrong_age_group():
        print(user.name, user.fname, user.county, user.age, user.is_teen)
