import cv2
import numpy as np

def auto_crop_image(image, points):
    if len(points) != 4:
        return None
    src = np.float32(points)
    dst = np.float32([[0, 0], [image.shape[1], 0], [image.shape[1], image.shape[0]], [0, image.shape[0]]])
    M = cv2.getPerspectiveTransform(src, dst)
    warped = cv2.warpPerspective(image, M, (image.shape[1], image.shape[0]))
    return warped

def define_display(event, x, y, flags, param):
    global display_points
    if event == cv2.EVENT_LBUTTONDOWN:
        display_points.append((x, y))
        if len(display_points) == 4:
            cv2.destroyWindow("Select Display Area")

display_points = []

def select_display_area():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Select Display Area", frame)
        cv2.setMouseCallback("Select Display Area", define_display)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    return display_points
