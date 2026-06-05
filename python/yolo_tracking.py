from ultralytics import YOLO
import cv2
import serial
import time

model = YOLO("C:/Users/samue/Dropbox/My PC (DESKTOP-IB4HC17)/Downloads/turret project/python/models/custom_model1.pt")
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

ser = serial.Serial("COM3", 115200)
time.sleep(2)

last_send = 0

# Smoothed target coordinates
smooth_cx = None
smooth_cy = None

# Smoothing factor
alpha = 0.8

while True:
    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame, verbose=False)

    # Frame center (RED)
    frame_height, frame_width = frame.shape[:2]
    frame_cx = frame_width // 2
    frame_cy = frame_height // 2

    cv2.circle(frame, (frame_cx, frame_cy), 5, (0, 0, 255), -1)

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            cx = int((x1 + x2)/2)
            cy = int((y1 + y2)/2)

            # Initialize smoothing
            if smooth_cx is None:
                smooth_cx = cx
                smooth_cy = cy

            smooth_cx = alpha * cx + (1 - alpha) * smooth_cx
            smooth_cy = alpha * cy + (1 - alpha) * smooth_cy

            smooth_cx_int = int(smooth_cx)
            smooth_cy_int = int(smooth_cy)

            # Green smoothed target dot
            cv2.circle(
                frame,
                (smooth_cx_int, smooth_cy_int),
                6,
                (0, 255, 0),
                -1
            )

            x_error = smooth_cx_int - frame_cx
            y_error = smooth_cy_int - frame_cy

            
            if time.time() - last_send > 0.02:

                message = f"{x_error},{y_error}\n"

                ser.write(message.encode())

                last_send = time.time()

            break

    frame = results[0].plot(img=frame)

    cv2.imshow("YOLO", frame)

    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
ser.close()
cv2.destroyAllWindows()