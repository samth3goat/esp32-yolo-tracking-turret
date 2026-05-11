# ESP32 YOLO Object Tracking Turret

A computer vision tracking turret that detects and follows a custom target object using a YOLO model running on a PC, while an ESP32 controls the pan/tilt servo system.

This project combines embedded systems, computer vision, serial communication, and control systems into a real-time autonomous tracking platform.

---

## Project Overview

The system uses a webcam to capture live video, processes frames using OpenCV and YOLO object detection, determines the target position relative to the screen center, and sends movement commands to an ESP32 which controls the servos.

---

## Demo
*In progress*

---

## Features

### Current
- ESP32 firmware control
- Servo motor control
- OpenCV live webcam feed
- YOLO object detection
- Custom YOLO model support
- Python ↔ ESP32 serial communication

### Planned
- Pan/tilt turret tracking
- PID motion smoothing
- Distance estimation

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
- External power supply

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

### In Progress
- [ ] Coordinate extraction from detections
- [ ] Python to ESP32 movement commands
- [ ] Pan tracking
- [ ] Tilt tracking

### Planned
- [ ] PID control tuning
- [ ] Distance estimation
- [ ] Dual servo stabilization
- [ ] Final turret assembly

---

## Engineering Challenges

Some issues encountered during development:

- False positives during YOLO custom model training
- Serial timing/debugging between Python and ESP32
- Power requirements for high-torque servos

---

## Lessons Learned

This project is being used as a learning platform for:

- embedded systems programming
- computer vision
- real-time object tracking
- serial communication
- servo motor control
- control systems (PID)
- machine learning model integration

---

## Future Improvements

Potential future upgrades:

- Full PID tracking controller
- Object re-identification
- Multi-object selection
- Mobile/web dashboard
- Autonomous scanning mode
- Battery-powered portable turret

---

## Notes

YOLO inference runs on the host PC, not the ESP32.

The ESP32 acts as the hardware controller for:
- servo movement
- future peripheral control

This architecture keeps computer vision processing separate from real-time hardware control.

---

## Author

Built as a personal robotics/computer vision project to learn embedded systems and autonomous tracking.
