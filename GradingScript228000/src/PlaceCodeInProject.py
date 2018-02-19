import os
import sys
import json
import shutil
from pathlib import Path
from FileManipulation import setupFile, replaceStringsInFile, addMethods, saveFirstLine, readFirstLine

REPLACEMENTS_JSON_FILENAME = 'json_attributes/replacements.json'
EXTRA_METHODS = 'json_attributes/extraMethods.json'

#Modifies files when placing into HW_Student project.
#Will Replace code (either changing access modifiers)
#Will Add methods if methods need to be added
def modifyFiles(directory):
    with open(REPLACEMENTS_JSON_FILENAME) as data_file:
        data = json.load(data_file)
        for className, replacements in data.items():
            classFile = directory + '/' + className + '.java'
            toBeReplaced = replacements["toBeReplaced"]
            replacors = replacements["replacors"]
            replaceStringsInFile(classFile, toBeReplaced, replacors)
        data_file.close()

    with open(EXTRA_METHODS) as data_file:
        data = json.load(data_file)
        for className, methodsToAdd in data.items():
            classFile = directory + '/' + className + '.java'
            addMethods(classFile, methodsToAdd)
        data_file.close()

#Will get the list of students the way the OS retrieves names
#TODO Should probably change this to be alphabetical
def getListOfStudents(studentsDir):
    students = list()
    for file in os.listdir(os.fsencode(studentsDir)):
        fileName = os.fsdecode(file)
        if os.path.isdir(studentsDir + '/' + fileName):
            students.append(fileName)
    return students

#Will choose the next student to have their code placed in HW_Student project
def getNextStudent(studentsDir, currentStudentFile, lastStudentFile):
    currentStudent = readFirstLine(currentStudentFile)
    allStudents = getListOfStudents(studentsDir)
    if len(allStudents) == 0:
        return None
    if not currentStudent:
        return allStudents[0]
    getNext = False
    for student in allStudents:
        if getNext:
            return student
        getNext = currentStudent == student
    return None

#Setup file names and folders to be used
#Grabs file in counter if students should be updated or not
def setup(assignment):
    currentStudentFile = 'counters/student_counter.txt'
    updateFileName = "counters/shouldUpdate.txt"
    setupFile(currentStudentFile)
    setupFile(updateFileName)
    studentsDir = assignment + '_Submissions_unzipped'
    studentToTest = getNextStudent(studentsDir, currentStudentFile, updateFileName)
    shouldUpdate = readFirstLine(updateFileName)
    return currentStudentFile, studentsDir, studentToTest, shouldUpdate

#Program to place the following students code in HW_Student
#Will not update if counters/shouldUpdate.txt is False
def main(assignment):
    currentStudentFile, studentsDir, studentToTest, shouldUpdate = setup(assignment)
    if shouldUpdate and shouldUpdate == 'False':
        print("Not Updated")
        return
    packageName = '/edu/iastate/cs228/' + assignment.lower()
    testDirectory = '../HW_Student/src/main/java' + packageName

    if studentToTest:
        studentFiles = studentsDir + '/' + studentToTest + packageName
        print(studentToTest)
        if not os.path.isdir(studentFiles):
            print('Fix Error in File Location!')
            return
        shutil.rmtree(testDirectory)
        shutil.copytree(studentFiles, testDirectory)
        modifyFiles(testDirectory)
    saveFirstLine(currentStudentFile, studentToTest)

if __name__ == '__main__':
    if not len(sys.argv) == 2:
        print('Missing specific homework arguement')
    else:
        os.chdir('../' + sys.argv[1])
        main(sys.argv[1])
