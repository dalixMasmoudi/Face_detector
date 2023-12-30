
import cv2
from simple_facerec import SimpleFacerec
import time
from datetime import datetime


# Encode faces from a folder
#print(cv2.cuda.getCudaEnabledDeviceCount())
#import dlib
#print(dlib.DLIB_USE_CUDA)
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Load Camera
cap = cv2.VideoCapture(0)

ptime=0
while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        current_time = datetime.now()

        print("Personne détectée :", name, "à l'heure suivante :", current_time.strftime("%H:%M:%S"))
     #   y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

      #  cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
       # cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 200, 200), 4)
        ctime=time.time()
        print('Fps', 1/(ctime-ptime))
        ptime=ctime


    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()