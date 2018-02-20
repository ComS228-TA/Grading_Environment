from os import remove
from shutil import copy2
from FileManipulation import readFirstLine

def main(assignment):
    student = readFirstLine(currentStudentFile)
    studentsFolder = assignment + '_Submissions_unzipped/' + student
    fileToReplace = studentsFolder + '/' + student + '.txt'
    remove(fileToReplace)
    templateName = assignment + 'GradingTemplate_18S.txt'
    copy2(templateName, fileToReplace)

if __name__ == '__main__':
    if not len(sys.argv) == 2:
        print('Missing specific homework arguement')
    else:
        os.chdir('../' + sys.argv[1])
        main(sys.argv[1])
