#include <ESP32Servo.h>

Servo panServo;
Servo tiltServo;

float panAngle = 90;
float tiltAngle = 110;

// ===== TUNE THESE =====

float Kp = 0.005;
float Kd = 0.015;

// ======================

int prevXError = 0;
int prevYError = 0;

void setup() {

  Serial.begin(115200);

  panServo.attach(13);
  tiltServo.attach(12);

  panServo.write(panAngle);
  tiltServo.write(tiltAngle);
}

void loop() {

  if (Serial.available()) {

    String msg = Serial.readStringUntil('\n');

    int commaIndex = msg.indexOf(',');

    if (commaIndex > 0) {

      int xError =
          msg.substring(0, commaIndex).toInt();

      int yError =
          msg.substring(commaIndex + 1).toInt();

      int dx = xError - prevXError;
      int dy = yError - prevYError;

      // Deadzone

      if (abs(xError) > 5) {

        float panMove =
            (Kp * xError) +
            (Kd * dx);

        panMove = constrain(
            panMove,
            -7,
            7);

        panAngle -= panMove;
      }

      if (abs(yError) > 5) {

        float tiltMove =
            (Kp * yError) +
            (Kd * dy);

        tiltMove = constrain(
            tiltMove,
            -7,
            7);

        tiltAngle -= tiltMove;
      }

      prevXError = xError;
      prevYError = yError;

      panAngle = constrain(
          panAngle,
          20,
          160);

      tiltAngle = constrain(
          tiltAngle,
          20,
          160);

      panServo.write((int)panAngle);
      tiltServo.write((int)tiltAngle);
    }
  }
}