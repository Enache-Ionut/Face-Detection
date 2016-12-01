import cv2

class FaceDetection:

    def __init__(self):

        # xml ce contine date despre detectarea fetei
        self.cascPath = "haarcascade_frontalface_default.xml"

        self.faceCascade = cv2.CascadeClassifier(self.cascPath)

        # se seteaza ca sursa video sa fie WebCam-ul
        self.video_capture = cv2.VideoCapture(0)

    # Captureaza imaginea frame cu frame
    # ret nu este folosit in program dar este necesar deoarece functia returneaza 2 valori
    def setRetFrame(self ):
        self.ret, self.frame = self.video_capture.read()

    def setDetection(self ):
        self.detection = self.cascade_detect()

    def cascade_detect(self):
        # se converteste fiecare frame la grayscale
        # grayscale reprezinta scara nuantelor cenusii
        self.gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)

        # detectMultiScale() este o functi generala ce detecteaza obiecte
        return self.faceCascade.detectMultiScale(
            self.gray,
            # unele fete pot fi mai aproape de camera si se vor vedeam mai mari decat cele aflate mai departe de camera
            # factorul de scara remediaza acest lucru si permite detectarea fiecareia
            scaleFactor = 1.15,

            # detecteaza cate obiecte sunt detectate langa cel curent inainte sa declare gasirea fetei
            minNeighbors = 5,

            # defineste marimea fiecarei ferestre
            minSize = (30, 30),

            # anunta detectarea fetei
            flags = cv2.cv.CV_HAAR_SCALE_IMAGE
        )

    # Se va desena un dreptunghi in jurul fetei in caz ca este gasita
    def detection_draw(self):
        for (x, y, w, h) in self.detection:
             cv2.rectangle(self.frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Afiseaza rezultatul fiecarui frame
    def display(self):
         cv2.imshow('Video', self.frame)

    # la terminarea programului se va elibera captura si se va inchide fereastra de WebCam
    def close(self):
        self.video_capture.release()
        cv2.destroyAllWindows()

def main():

    faceDetection = FaceDetection()

    while True:
        faceDetection.setRetFrame()

        faceDetection.setDetection()

        faceDetection.detection_draw()

        faceDetection.display()

        # 27 este codul ascii pentru ESC
        if cv2.waitKey(1) == 27:
             break

    faceDetection.close()

if __name__ == "__main__":
    main()