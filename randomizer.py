import json
import sys
import os
from random import randrange

# script args
args = sys.argv[1:]

# open students file
file = open(os.path.dirname(__file__) + "/students.json", "r")
students_json = json.load(file)


def get_next():
    if len(students_json['random']) <= 0:
        make_rand()

    print(f'{students_json["random"][0].replace("-", " ")} is up now.')
    
    if len(students_json['random']) <= 1:
        print("A new random list will be made next time!")
    else:
        print(f'{students_json["random"][1].replace("-", " ")} is up next time.')
    del students_json['random'][0]

    with open(os.path.dirname(__file__) + "/students.json", "w") as write_file:
        json.dump(students_json, write_file)
def print_rand():
    for student in students_json['rand']:
        print(student)

def make_rand():

    # new list in random order
    rand_students = []
    # preserve the list of students 
    curr_students = students_json['students'].copy()
    
    while len(curr_students) > 0:
        rand_index = randrange(0, len(curr_students), 1)
        rand_students.append(curr_students[rand_index])
        del curr_students[rand_index]
    
    # write file with new data
    students_json['random'] = rand_students
    with open(os.path.dirname(__file__) + "/students.json", "w") as write_file:
        json.dump(students_json, write_file)

switch = {
    '--next': get_next,
    '--make': make_rand,
    '--print': print_rand
}

for arg in args:
    if arg in switch:
        switch[arg]()
