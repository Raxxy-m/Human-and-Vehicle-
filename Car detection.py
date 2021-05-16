# import the libraries
import cv2
import imutils
# captures frames from a video
cap = cv2.VideoCapture('vehicle_vid.mp4')

# Trained XML classifiers describes some features of some object we want to detect
car_cascade = cv2.CascadeClassifier('cars.xml')

while True:
    # reads frames from a video
    check, frame = cap.read()

    if (check != True):
        break
    # convert to grayscale of each frame
    frame = imutils.resize(frame, width=min(800, frame.shape[1]))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    # detect cars of different sizes in the input
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    # create car var to maintain count
    car = 0

    # draw rectangles on each car
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(frame, f'Car {car}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        car += 1
        cv2.putText(frame, 'Status : Detecting', (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 255, 0), 1)
        cv2.putText(frame, f'Total Cars : {car}', (40, 70), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (255, 255, 0), 1)

    # display frames in a video
    cv2.imshow('output', frame)

    # wait for Esc to stop
    if cv2.waitKey(33) == 27:
        break;

cap.release()
# de-allocate any associated memory usage
cv2.destroyAllWindows()