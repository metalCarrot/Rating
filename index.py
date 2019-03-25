import json
import csv
from pprint import pprint
from operator import itemgetter, attrgetter

def getAbit():
    with open('rating.json') as f:
        data = json.load(f)

    students = []

    for key in data:
        points = list(key.get('subjects').values())
        marks = []
        for word in points:
            marks.append(int(word))

        avg = sum(marks) // len(marks)
        abit = [key.get('name'), key.get('surname'), avg]
        students.append(abit)

    return students    


def addPlace(students):
    for (index, student) in enumerate(students):
        student.insert(0, index + 1)
    
    return students


def sortAbit(students):
    students = sorted(students, key=itemgetter(2))
    students.reverse()
    students = addPlace(students)
    return students


def printInCsv():
    pass


students = getAbit()
sortStudent = sortAbit(students)
pprint(sortStudent)