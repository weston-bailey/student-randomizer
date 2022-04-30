import json
import sys
import os
from random import randrange

# script args
args = sys.argv[1:]

# open students file and pull data out as needed
students_json = {}
with open(os.path.dirname(__file__) + "/students.json", "r") as file:
    students_json = json.load(file)

def make_rand():
    '''
        generates a new random list of students
    '''
    # new list in random order
    rand_students = []
    # preserve the list of students 
    curr_students = students_json['students'].copy()
    
    # create a random index, remove from curr_students and add to rand_students
    while len(curr_students) > 0:
        rand_index = randrange(0, len(curr_students), 1)
        rand_students.append(curr_students[rand_index])
        del curr_students[rand_index]
    
    # write file with new data
    students_json['random'] = rand_students
    with open(os.path.dirname(__file__) + "/students.json", "w") as write_file:
        json.dump(students_json, write_file)

def get_next():
    '''
        prints the new student and advances the random list. if the random list is empty, it will be populated
    '''
    # create a random list if not present
    if len(students_json['random']) <= 0:
        make_rand()

    # display whose turn it is
    print(f'{students_json["random"][0].replace("-", " ")} is up now.')
    
    # inform the next student/that the list is empty
    if len(students_json['random']) <= 1:
        print("A new random list will be made next time!")
    else:
        print(f'{students_json["random"][1].replace("-", " ")} is up next time.')

    # remove the person whose turn it is
    del students_json['random'][0]

    # write the new list 
    with open(os.path.dirname(__file__) + "/students.json", "w") as write_file:
        json.dump(students_json, write_file)

def print_rand():
    '''
        print out the students in order
    '''
    for student in students_json['rand']:
        print(student)

switch = {
    '--next': get_next,
    '--make': make_rand,
    '--print': print_rand
}

for arg in args:
    if arg in switch:
        switch[arg]()