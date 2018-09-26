import os
from params import common
import pathlib
import shutil
import gc

def importKnownImages():
    try:
        return os.listdir(common.imagePath.known)
    except OSError as e:
        print("Known file not found")
        print("[loop] importKnownImages: ", e)
        return ""


def importUnknownImages():
    try:
        return os.listdir(common.imagePath.unknown)
    except OSError as e:
        print("unknown file not found")
        print("[loop] importUnknownImages: ",e)
        return ""

def createFolder(knownFilename,unknownFilename, isCopy):
    unknownPath = common.imagePath.unknown + unknownFilename
    moveToPath = common.imagePath.classified + removeFileExtension(knownFilename)

    pathlib.Path(moveToPath).mkdir(parents=True, exist_ok=True)
    if isCopy:
        shutil.copy(unknownPath, moveToPath)
    else:
        shutil.move(unknownPath, moveToPath)
    gc.collect()

def isImage(file):
    filename_w_ext = os.path.basename(file)
    filename, file_extension = os.path.splitext(filename_w_ext.lower())
    return common.fileExtension.image.__contains__(file_extension.strip('.'))

def removeFileExtension(file):
    filename_w_ext = os.path.basename(file)
    filename, file_extension = os.path.splitext(filename_w_ext.lower())
    return filename
