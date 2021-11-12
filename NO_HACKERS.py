# Creating an Automated security system.
import cv2
import dropbox
import time
import random

start_time = time.time()

#Function to take a face shot of all the user(s).

def take_snapshot():
    number = random.randint(0, 100)
    #imgae_path = r""
    # initializing cv2.
    # Variable to store the first image array in the Video Capture.
    videCaptureobject = cv2.VideoCapture(0)
    # The result will be true when the image result has been captured.
    result = True
    while(result):
        # This guy right there yes, ret is a dummy variable
        ret, frame = videCaptureobject.read()
        img_name = "img"+str(number)+".png"

        # cv2.imright is used to save the image in a specific folder
        cv2.imshow(img_name, frame)
        start_time = time.time
        # The image file extension should be in jpg, png or jpeg.
        result = False
    return img_name
    print("snapshot taken")
    # Release the Krak-...., Sorry Release the Camera.
    videCaptureobject.release()
    # Close all the windows when this happens, noone wants to see this.
    cv2.destroyAllWindows()


def upload_file(img_name):
    accessToken = ""
    file = img_counter
    file_from = file
    file_to = ""+(img_name)
    dbx = dropbox.Dropbox(acessToken)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,
                         mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")


def main():
    while(True):
        if((time.time() - start_time) >= 300):
            name = take_snapshot()
            upload_file(name)


main()
    