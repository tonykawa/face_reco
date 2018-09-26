import face_recognition
import os
from params import common
import File
import datetime

def main(filename):
    step1_anaylseFaceFeature(filename)

def step1_anaylseFaceFeature(filename):
    knowPath = common.imagePath.known + filename
    picture_of_me = face_recognition.load_image_file(knowPath)
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

    filename_w_ext = os.path.basename(filename)
    ppl_name, file_extension = os.path.splitext(filename_w_ext)
    # my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

    for f in File.importUnknownImages():
        startTime = datetime.datetime.now()
        if File.isImage(f) == False: continue

        unknownPath = common.imagePath.unknown + f
        unknown_picture = face_recognition.load_image_file(unknownPath)
        unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

        if step2_comparsion(my_face_encoding, unknown_face_encoding) == True:

            File.createFolder(filename, f, True)
            endTime = datetime.datetime.now()
            print("Clone " + f + " to " + ppl_name + "; Time Used:", endTime - startTime)




# Now we can see the two face encodings are of the same person with `compare_faces`!
def step2_comparsion(my_face_encoding, unknown_face_encoding):
    results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)
    return results[0]
