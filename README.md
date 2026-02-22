# Gesture_LED_Control
# Gesture-Controlled 4 LEDs

Control 4 LEDs using hand gestures with **Arduino + Python**.  
This project uses a camera or gesture sensor to detect the number of fingers shown and lights up corresponding LEDs.

---

## Overview
- 1 finger → LED1  
- 2 fingers → LED2  
- 3 fingers → LED3  
- 4 fingers → LED4  

The Python code detects gestures and communicates with Arduino via **Serial** to control LEDs.

---

## Components Used
- Arduino Uno / ESP32  
- 4 LEDs + Resistors  
- Wires, Breadboard  
- Camera (for OpenCV + MediaPipe) **or** APDS-9960 Gesture Sensor  

---


## Software
- Python 3.x with OpenCV / MediaPipe  
- Arduino IDE

---

## How to Run
1. Connect the Arduino with LEDs and gesture sensor or camera.  
2. Open **led_gesture_control.ino** in Arduino IDE → Upload to the board.  
3. Open Python environment → Run **gesture_led_control.py**.  
4. Show gestures to camera or sensor → corresponding LEDs light up.

---


---

## Challenges & Improvements
- Reduce detection latency  
- Improve gesture recognition under low-light  
- Add more gestures for additional LED patterns  

---

## License
MIT License
