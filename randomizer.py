import json
from random import randrange

file = open("students.json", "r")
students_json = json.load(file)

print(students_json['students'])

rand_students = []
curr_students = students_json['students'].copy()

while len(curr_students) > 0:
    rand_index = randrange(0, len(curr_students), 1)
    rand_students.append(curr_students[rand_index])
    del curr_students[rand_index]


print(curr_students, rand_students)

# with open("students.json", "w") as write_file:
#     json.dump(students, write_file)
