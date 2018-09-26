import File
import FaceReco
import datetime

def main():
    startTime = datetime.datetime.now()
    for f in File.importKnownImages():
        FaceReco.main(f)

    endTime = datetime.datetime.now()
    print("Total Time Usage:",endTime - startTime)

main()