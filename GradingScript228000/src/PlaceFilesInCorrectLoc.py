import os
from shutil import copytree
from FileManipulation import makeDirectory

def doesDirContainCode(folder):
    try:
        print(folder)
        for file in os.listdir(os.fsencode(folder)):
            filename = os.fsdecode(file)
            if filename.endswith(".java"):
                if not filename.endswith("Test.java"):
                    return True
        return False
    except OSError as e:
        return False

def placeFilesInCorrectLoc(studentDir, folderWhereSrcShouldBe):
    inCorrectPlace = doesDirContainCode("./" + studentDir + "/" + folderWhereSrcShouldBe)
    if inCorrectPlace:
        return True

    for root, dirs, files in os.walk("./" + studentDir):
        if doesDirContainCode(root):
            copytree(root, './' + studentDir + "/" + folderWhereSrcShouldBe)
            return True
    return False
