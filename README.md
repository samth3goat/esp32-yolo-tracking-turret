# ESP32 YOLO Object Tracking Turret

A real-time computer vision tracking system featuring a custom-designed and 3D-printed two-axis pan/tilt turret. The system uses a custom-trained YOLO11 model to detect and track a target object while an ESP32 microcontroller controls the turret through closed-loop PD control.

The project integrates mechanical design, computer vision, embedded systems, serial communication, and feedback control into a fully autonomous object tracking platform.

---

## Project Overview

The system captures live video using a webcam, processes each frame with OpenCV and a custom-trained YOLO11 model, computes the target's position relative to the center of the frame, and sends tracking commands to an ESP32. The ESP32 executes a PD controller to drive the pan and tilt servos, allowing the custom-designed turret to continuously maintain target lock through visual feedback.

---

## Skills Demonstrated

- Mechanical Design (CAD)
- 3D Printing
- Embedded Systems
- Computer Vision
- Control Systems (PD)
- Python
- C++
- OpenCV
- YOLO11
- ESP32
---

## Demo

<img width="408" height="434" alt="Untitled - 05 juin 2026 à 16 11 36" src="https://github.com/user-attachments/assets/bc4024de-7969-480d-bd7c-d36b02986683" />

---

## System Architecture

<img width="1163" height="637" alt="final system" src="https://github.com/user-attachments/assets/51c3713d-aaf5-4003-b6c9-d9d5a01a3f26" />


Figure 1. High-level architecture of the closed-loop object tracking system. The webcam captures real-time video, the desktop computer performs YOLO11 inference and computes the tracking error, the ESP32 executes the PD controller and generates PWM signals, and the servos reposition the pan/tilt mechanism. The updated camera view provides continuous visual feedback, closing the control loop.

---

## Features

- Custom-designed and 3D-printed pan/tilt turret
- Real-time object tracking using a custom-trained YOLO11 model
- Two-axis servo control with an ESP32 microcontroller
- OpenCV webcam integration
- Python ↔ ESP32 serial communication
- Closed-loop PD tracking controller
- Target coordinate extraction and smoothing
- Real-time visual debugging overlay
- External servo power system

---


## Hardware

- Custom 3D-printed pan/tilt mechanism
- ESP32 DevKit V1
- 2 × DS3218 high-torque servo motors
- Logitech C922 USB webcam
- 5V 5A regulated external power supply

---

## Software Stack

- Python
- C++
- OpenCV
- Ultralytics YOLO11
- ESP32 Arduino Framework
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
│   ├── camera_test.py
│   └── models/
│       └── custom_model.pt
│
├── esp32/
│   └── turret_control.ino
│    
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

- Training a custom YOLO model that could reliably identify the target while minimizing false detections.
- Balancing tracking accuracy and responsiveness to maintain smooth real-time performance.
- Establishing reliable serial communication between Python and the ESP32.
- Providing sufficient power for servo motors without causing instability or stalling.
- Tuning the tracking controller to reduce oscillation and improve target lock.

---

## Lessons Learned

This project is being used as a learning platform for:

- Computer vision using OpenCV and YOLO.
- Embedded systems programming with the ESP32.
- Serial communication between software and hardware.
- Servo control and power management.
- Control systems and real-time tracking.
- Debugging and integrating multi-component engineering systems.

---

## Notes

YOLO inference runs on the host PC, not the ESP32.

The ESP32 acts as the hardware controller for:
- servo movement
- future peripheral control

This architecture keeps computer vision processing separate from real-time hardware control.

---
