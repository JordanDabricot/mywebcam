import cv2

def show_webcam(mirror = False):
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        if mirror:
            img = cv2.flip(img,1)
        cv2.imshow("my webcam", img)
        if cv2.waitKey(1) == 27:
            break #esc to quit
    cv2.destroyAllWindows()

def main():
    show_webcam()

if __name__ == '__main__':
    main()