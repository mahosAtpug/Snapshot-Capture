import cv2
import time
import dropbox
import random

start_time = time.time()


def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while (result):
        ret,frame = videoCaptureObject.read()
        image_name = "img" + str (number) + ".png"
        cv2.imwrite(image_name, frame)
        start_time = time.time()
        result = False
    print("Snapshot Captured")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    return image_name
take_snapshot()

def upload_file(image_name):
    access_token = "bZYAhv3Ez94AAAAAAAAAAXh9pLtNu8wI-xvBtcbkn1pNSKA84i9_cjsNSp9vPUXl"
    file = image_name
    file_from = file
    file_to = "/python_codes/" + image_name
    dbx = dropbox.Dropbox(access_token)

    with open (file_from , "rb") as f:
        dbx.files_upload(f.read() , file_to , mode= dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while (True):
        if ((time.time() - start_time ) >= 3):
            name = take_snapshot()
            upload_file (name)

main()
            
    
