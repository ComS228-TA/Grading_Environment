import os
import sys
import errno
import json
from zipfile import ZipFile
from shutil import copy2, move
from datetime import datetime
from FileManipulation import replaceStringsInFile, makeDirectory
from PlaceFilesInCorrectLoc import placeFilesInCorrectLoc

#Extracts the students zip folder and moves it into HWX_Submissions_Unzipped
def extractAndCopyFiles(filename, zipFileDir, templateName, students, folderWhereSrcShouldBe):
    student = filename.replace('.zip', '')
    if student not in students:
        students[student] = 0
    else:
        students[student] += 1
        student += '_' + str(students[student])
    studentDir = zipFileDir + '_unzipped/' + student
    makeDirectory(studentDir)
    zip = ZipFile(zipFileDir + '/' + filename)
    zip.extractall(studentDir)
    copy2(templateName, studentDir + '/' + student + '.txt')
    return placeFilesInCorrectLoc(studentDir, folderWhereSrcShouldBe), studentDir, student

#Edits the grading template with the graders specific attributes
def setupGradingTemplateWithGraderAttributes(jsonFileName, templateName):
    toBeReplaced = list()
    replacors = list()
    with open(jsonFileName) as data_file:
        data = json.load(data_file)
        data_file.close()
        for key, value in data.items():
            toBeReplaced.append(key)
            replacors.append(value)

    replaceStringsInFile(templateName, toBeReplaced, replacors)

#Program to Unzip student files, place them in HWX_Submissions_Unzipped and then
#add the template to each student folder
#If there are errors with the student zip files, will place in error folders
def main(assignment):
    students = {}
    zipFileDir = assignment + '_Submissions'
    templateName = assignment + 'GradingTemplate_18S.txt'
    folderWhereSrcShouldBe = 'edu/iastate/cs228/' + assignment.lower() + '/'

    setupGradingTemplateWithGraderAttributes("json_attributes/GraderAttributes.json", templateName)

    for file in os.listdir(os.fsencode(zipFileDir)):
        filename = os.fsdecode(file)
        if filename.endswith(".zip"):
            foundCode, studentDir, student = extractAndCopyFiles(filename, zipFileDir, templateName, students, folderWhereSrcShouldBe)
            if not foundCode:
                makeDirectory('Errors')
                move(studentDir, './Errors/' + student)
        else:
            makeDirectory('Errors')
            copy2(zipFileDir + '/' + filename, 'Errors/' + filename)

if __name__ == '__main__':
    if not len(sys.argv) == 2:
        print('Missing specific homework arguement')
    else:
        os.chdir('../' + sys.argv[1])
        main(sys.argv[1])
