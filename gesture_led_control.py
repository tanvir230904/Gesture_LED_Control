import cv2
import mediapipe as mp
import serial
import time

# Connect to Arduino
arduino = serial.Serial('COM7', 9600)   # CHANGE COM PORT
time.sleep(2)

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

tip_ids = [4, 8, 12, 16, 20]   # Thumb, Index, Middle, Ring, Pinky

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        hand = results.multi_hand_landmarks[0]
        lm = hand.landmark

        # THUMB (special case: x comparison)
        if lm[tip_ids[0]].x < lm[tip_ids[0] - 2].x:
            arduino.write(b'1')   # LED1 ON
        else:
            arduino.write(b'A')   # LED1 OFF

        # INDEX
        if lm[tip_ids[1]].y < lm[tip_ids[1] - 2].y:
            arduino.write(b'2')
        else:
            arduino.write(b'B')

        # MIDDLE
        if lm[tip_ids[2]].y < lm[tip_ids[2] - 2].y:
            arduino.write(b'3')
        else:
            arduino.write(b'C')

        # RING
        if lm[tip_ids[3]].y < lm[tip_ids[3] - 2].y:
            arduino.write(b'4')
        else:
            arduino.write(b'D')

        # PINKY
        if lm[tip_ids[4]].y < lm[tip_ids[4] - 2].y:
            arduino.write(b'5')
        else:
            arduino.write(b'E')

        # Draw hand on screen
        mpDraw.draw_landmarks(img, hand, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Finger LED Control", img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


