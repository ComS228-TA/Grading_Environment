import os
from pathlib import Path

#Adds methods to a specific file in Java
def addMethods(filename, methods):
    replacedFileList = list()
    firstTime = True

    with open(filename, "rt") as fin:
        for line in fin:
            replacedFileList.append(line)
            if firstTime and "{" in line:
                replacedFileList.extend(methods)
                firstTime = False

        fin.close()

    with open(filename, "wt") as fout:
        for line in replacedFileList:
            fout.write(line)
        fout.close()

#Creates a directory if it does not exist already
def makeDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

#Reads the first line of a file and returns it if not empty, otherwise None
def readFirstLine(fileName):
    f = open(fileName, 'r')
    line = f.read()
    f.close()
    return line if line.strip() else None

#Finds all the places in a file where the string toBeReplaced is
#and replaces it with toBeReplaced
def replaceStringsInFile(filename, toBeReplaced, replacors):
    if not len(toBeReplaced) == len(replacors):
        raise ValueError("toBeReplaced Array and replacors Array are not the same size")

    replacedFileList = list()

    with open(filename, "rt") as fin:
        for line in fin:
            newLine = line
            for replaced, replacor in zip(toBeReplaced, replacors):
                newLine = newLine.replace(replaced, replacor)
            replacedFileList.append(newLine)
        fin.close()

    with open(filename, "wt") as fout:
        for line in replacedFileList:
            fout.write(line)
        fout.close()

#Saves the string toSave in a file if toSave is not None
#Otherwise saves an empty file
def saveFirstLine(fileName, toSave):
    f = open(fileName, 'w')
    if not toSave:
        f.write('');
    else:
        f.write(toSave);
    f.close()

#Creates a file based on the fileName
#If the file already exists, nothing happens
def setupFile(fileName):
    myFile = Path(fileName)
    if myFile.is_file():
        return
    file = open(fileName,'w')
    file.write('')
    file.close()
