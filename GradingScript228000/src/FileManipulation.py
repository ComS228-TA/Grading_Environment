import os
from pathlib import Path

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

def makeDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

def readFirstLine(fileName):
    f = open(fileName, 'r')
    line = f.read()
    f.close()
    return line if line.strip() else None

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

def saveFirstLine(fileName, toSave):
    f = open(fileName, 'w')
    if not toSave:
        f.write('');
    else:
        f.write(toSave);
    f.close()

def setupFile(fileName):
    myFile = Path(fileName)
    if myFile.is_file():
        return
    file = open(fileName,'w')
    file.write('')
    file.close()
