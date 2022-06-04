people = [
    {"name": "Harry", "house": "Griffyndor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"},
]

people.sort(key=lambda person: person["name"])

print(people)