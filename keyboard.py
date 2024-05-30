import cv2
from hand_detection import HandTracker
from perspective import auto_crop_image, select_display_area
from color_detection import detect_red_color

class Keyboard:
    def __init__(self):
        self.hand_tracker = HandTracker()
        self.display_points = select_display_area()

    def run(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Détection des mains
            frame = self.hand_tracker.findHands(frame)
            lmList = self.hand_tracker.getPosition(frame)
            if lmList:
                # Process landmarks
                pass

            # Changement de perspective
            if len(self.display_points) == 4:
                frame = auto_crop_image(frame, self.display_points)

            # Détection de couleur
            mask = detect_red_color(frame)
            cv2.imshow("Mask", mask)

            cv2.imshow("Frame", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
