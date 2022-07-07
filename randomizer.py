import json
import sys
import os
from random import randrange

class Randomizer:
    def __init__(self):
        self.students_json = self.__get_students_json()
        self.args = sys.argv[1:]

    def __get_students_json(self):
        '''
            returns the students json from file
        '''
        # open students file and pull data out as needed
        students_json = {}
        with open(os.path.dirname(__file__) + "/students.json", "r") as file:
            students_json = json.load(file)

        return students_json

    def __write_students_json(self):
        '''
            writes the students json to file
        '''
        with open(os.path.dirname(__file__) + "/students.json", "w") as write_file:
            json.dump(self.students_json, write_file)

    def make_rand(self):
        '''
            generates a new random list of students
        '''
        # new list in random order
        rand_students = []
        # preserve the list of students 
        curr_students = self.students_json['students'].copy()

        # create a random index, remove from curr_students and add to rand_students
        while len(curr_students) > 0:
            rand_index = randrange(0, len(curr_students), 1)
            rand_students.append(curr_students[rand_index])
            del curr_students[rand_index]

        # write file with new data
        self.students_json['random'] = rand_students
        self.__write_students_json()

        return self

    def get_next(self):
        '''
            prints the new student and advances the random list. if the random list is empty, it will be populated
        '''
        # create a random list if not present
        if len(self.students_json['random']) <= 0:
            self.make_rand()

        # display whose turn it is
        print(f'{self.students_json["random"][0].replace("-", " ")} is up now.')

        # inform the next student/that the list is empty
        if len(self.students_json['random']) <= 1:
            print("A new random list will be made next time!")
        else:
            print(f'{self.students_json["random"][1].replace("-", " ")} is up next time.')

        # remove the person whose turn it is
        del self.students_json['random'][0]

        # write the new list  
        self.__write_students_json()

        return self

    def print_rand(self):
        '''
            print out the students in order
        '''
        for student in self.students_json['random']:
            print(student)

        return self

    def list_upcoming(self):
        print("upcoming students:")
        for i, student in enumerate(self.students_json["random"]):
            print(f'{i + 1} {student}')

        return self

    def execute_arg(self, arg):

        # match arg:
        #     case '--next':
        #         self.get_next()
        #     case '--make':
        #         self.make_rand()
        #     case '--print':
        #         self.print_rand()
        #     case '--list':
        #         self.list_upcoming()
        #     case _:
        #         print(f'Invalid script argument: {arg}')
        switch = {
            '--next': self.get_next,
            '--make': self.make_rand,
            '--print': self.print_rand,
            '--list': self.list_upcoming,
        }

        if arg in switch:
            switch[arg]()
        else:
            print(f'Invalid script argument: {arg}')

        return self

    def evaluate_args(self):
        for arg in self.args:
            self.execute_arg(arg)

        return self

randomizer = Randomizer()
randomizer.evaluate_args()
