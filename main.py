import face_recognition
import os
from params import common
import File
import datetime

def face_reco(filename):
    print(datetime.datetime.now())
    knowPath = common.imagePath.known + filename
    picture_of_me = face_recognition.load_image_file(knowPath)
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

    filename_w_ext = os.path.basename(filename)
    ppl_name, file_extension = os.path.splitext(filename_w_ext)
    # my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

    # list of file
    for f in File.importUnknownImages():
        if File.isImageFile(f) == False: continue

        unknownPath = common.imagePath.unknown + f
        print(unknownPath)
        unknown_picture = face_recognition.load_image_file(unknownPath)
        unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

        # Now we can see the two face encodings are of the same person with `compare_faces`!
        results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

        if results[0] == True:
            print(f + " have \"" + ppl_name + "\" face!")
            File.createFolder(filename, f, True)
        else:
            print(f + " have't \"" + ppl_name + "\" face!")

        print(datetime.datetime.now())

face_reco("ice.jpg")