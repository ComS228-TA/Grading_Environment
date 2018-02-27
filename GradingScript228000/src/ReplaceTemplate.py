import sys
from os import remove, chdir
from shutil import copy2
from FileManipulation import readFirstLine

def main(assignment):
    currentStudentFile = 'counters/student_counter.txt'
    student = readFirstLine(currentStudentFile)
    studentsFolder = assignment + '_Submissions_unzipped/' + student
    fileToReplace = studentsFolder + '/' + student + '.txt'
    print(fileToReplace)
    remove(fileToReplace)
    templateName = assignment + 'GradingTemplate_18S.txt'
    copy2(templateName, fileToReplace)

if __name__ == '__main__':
    if not len(sys.argv) == 2:
        print('Missing specific homework arguement')
    else:
        chdir('../' + sys.argv[1])
        main(sys.argv[1])
