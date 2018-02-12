import os
import sys
from FileManipulation import setupFile, readFirstLine, replaceStringsInFile, saveFirstLine

def findStartAndEndTestOutput(filename, startString, endString):
    start = -1
    end = -1

    with open(filename, "rt") as fin:
        for index, line in enumerate(fin):
            if startString in line:
                start = index + 1
            elif endString in line:
                end = index - 1
        fin.close()

    return start, end

def createStudentTemplateFileName(student, assignment):
    return assignment + '_Submissions_unzipped/' + student + '/' + student + '.txt'

def starEndFileToString(filename, start, end):
    stringList = list()

    with open(filename, "rt") as fin:
        for index, line in enumerate(fin):
            if index > end:
                break
            elif index >= start:
                stringList.append(line)

    return '\n'.join(stringList)


def main(assignment):
    outputFileName = 'counters/output.txt'
    updateFileName = 'counters/shouldUpdate.txt'
    currentStudentFile = 'counters/student_counter.txt'
    setupFile(outputFileName)
    start, end = findStartAndEndTestOutput(outputFileName, ':testStudentCode', 'BUILD SUCCESSFUL')

    if start == -1 or end == -1:
        saveFirstLine(updateFileName, str(False))
        print('Did not compile or pass tests')
        return
    else:
        saveFirstLine(updateFileName, str(True))

    currentStudent = readFirstLine(currentStudentFile)
    sutdentTemplateFileName = createStudentTemplateFileName(currentStudent, assignment)
    testOutput = starEndFileToString(outputFileName, start, end)
    replaceStringsInFile(sutdentTemplateFileName, ['[PUT OUTPUT HERE]'], [testOutput])

if __name__ == '__main__':
    if not len(sys.argv) == 2:
        print('Missing specific homework arguement')
    else:
        os.chdir('../' + sys.argv[1])
        main(sys.argv[1])
