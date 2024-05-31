import cv2
import time
from hand_detection import HandTracker
from color_detection import detect_color

def main():
    hand_tracker = HandTracker()
    cap = cv2.VideoCapture(0)
    pTime = 0
    colors = ["red", "green", "blue"]
    color_index = 0
    last_keypress_time = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = hand_tracker.findHands(frame)
        cx, cy = hand_tracker.getPosition(frame)

        if cx is not None and cy is not None:
            cTime = time.time()
            if cTime - pTime > 1:
                pTime = cTime
                print(f"Coordonnées du doigt mis en avant : x={cx}, y={cy}")

        # Define the region of interest (ROI) - a square in the middle of the frame
        height, width, _ = frame.shape
        roi_size = 200
        x1, y1 = width // 2 - roi_size // 2, height // 2 - roi_size // 2
        x2, y2 = x1 + roi_size, y1 + roi_size
        roi = frame[y1:y2, x1:x2]

        mask = detect_color(roi, colors[color_index])
        cv2.imshow("Mask", mask)

        # Draw the ROI rectangle on the frame
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

        # Check if there is any detection in the mask
        if cv2.countNonZero(mask) > 0:
            print(f"Détection de {colors[color_index]}!")

        cv2.imshow("Hand Detection", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord(' '):  # Press space to change color
            current_time = time.time()
            if current_time - last_keypress_time > 0.5:  # Debounce to avoid multiple triggers
                last_keypress_time = current_time
                color_index = (color_index + 1) % len(colors)
                print(f"Couleur actuelle : {colors[color_index]}")

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
