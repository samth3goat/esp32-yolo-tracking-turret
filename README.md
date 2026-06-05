# ESP32 YOLO Object Tracking Turret

A real-time computer vision tracking system that uses a custom-trained YOLO11 model to detect and track a target object while controlling a two-axis pan/tilt turret through an ESP32 microcontroller.

The system combines machine learning, computer vision, embedded systems, serial communication, and closed-loop control to autonomously maintain target lock using a webcam and servo-actuated turret platform.
---

## Project Overview

The system uses a webcam to capture live video, processes frames using OpenCV and YOLO object detection, determines the target position relative to the screen center, and sends movement commands to an ESP32 which controls the servos.

---

## Demo
*In progress*

---

## Features

### Current
-ESP32 pan/tilt control
-Real-time YOLO11 object detection
-Custom-trained object tracking model
-OpenCV webcam integration
-Python ↔ ESP32 serial communication
-Two-axis target tracking
-Target coordinate extraction
-Exponential target smoothing
-Proportional-Derivative (PD) control
-Visual debugging overlay
-Red center reference point
-Green tracked target point
-External servo power system

---

## System Architecture

```text
Webcam
   ↓
OpenCV Video Capture
   ↓
YOLO Object Detection
   ↓
Target Coordinate Extraction
   ↓
Tracking Logic
   ↓
Serial Communication
   ↓
ESP32
   ↓
Pan/Tilt Servos
```

---

## Hardware

- ESP32 DevKit V1
- DS3218 Servo motors
- Logitech C922 USB webcam 
- External 5V 5A power supply

---

## Software Stack

- Python
- OpenCV
- Ultralytics YOLO
- Arduino IDE

---

## Repository Structure
*In progress*
```text
esp32-yolo-tracking-turret/
│
├── README.md
├── requirements.txt
│
├── python/
│   ├── yolo_tracking.py
│   ├── serial_control.py
│   └── models/
│       └── custom_model.pt
│
├── esp32/
│   ├── turret_control.ino
│   └──  servo_test.ino
│
├── images/
│   ├── setup.jpg
│   └── wiring_diagram.png
│
└── docs/
    ├── pid_notes.md
    ├── architecture.md
    └── troubleshooting.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/samth3goat/esp32-yolo-tracking-turret.git
cd esp32-yolo-tracking-turret
```

---

### Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

### Python Requirements

`requirements.txt`

```txt
opencv-python
ultralytics
pyserial
numpy
```

---

## Usage

### Run Object Detection

```bash
python python/yolo_tracking.py
```

---

### Upload ESP32 Firmware

1. Open Arduino IDE
2. Select board:

```text
ESP32 Dev Module
```

3. Select correct COM port
4. Upload:

```text
esp32/turret_control.ino
```

---

## Current Development Progress

### Completed
- [x] ESP32 setup and firmware upload
- [x] OpenCV webcam feed
- [x] YOLO object detection
- [x] Custom model loading
- [x] Initial ESP32 serial communication
- [x] Coordinate extraction from detections
- [x] Python to ESP32 movement commands
- [x] Pan tracking
- [x] Tilt tracking
- [x] PD control tuning
- [x] Final turret assembly

---

## Engineering Challenges

Some issues encountered during development:

-Training a custom YOLO model that could reliably identify the target while minimizing false detections.
-Balancing tracking accuracy and responsiveness to maintain smooth real-time performance.
-Establishing reliable serial communication between Python and the ESP32.
-Providing sufficient power for servo motors without causing instability or stalling.
-Tuning the tracking controller to reduce oscillation and improve target lock.

---

## Lessons Learned

This project is being used as a learning platform for:

-Computer vision using OpenCV and YOLO.
-Embedded systems programming with the ESP32.
-Serial communication between software and hardware.
-Servo control and power management.
-Control systems and real-time tracking.
-Debugging and integrating multi-component engineering systems.

---

## Notes

YOLO inference runs on the host PC, not the ESP32.

The ESP32 acts as the hardware controller for:
- servo movement
- future peripheral control

This architecture keeps computer vision processing separate from real-time hardware control.

---
