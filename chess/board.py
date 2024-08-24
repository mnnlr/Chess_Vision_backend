import cv2
import numpy as np

def order_points(pts):
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    return rect

def detect_and_crop_chessboard(image):
    if image is None:
        raise ValueError("Input image is None")
        
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    chessboard_contour = contours[0]
    epsilon = 0.02 * cv2.arcLength(chessboard_contour, True)
    approx = cv2.approxPolyDP(chessboard_contour, epsilon, True)
    if len(approx) == 4:
        ordered_points = order_points(approx.reshape(4, 2))
        side = max([
            np.linalg.norm(ordered_points[0] - ordered_points[1]),
            np.linalg.norm(ordered_points[1] - ordered_points[2]),
            np.linalg.norm(ordered_points[2] - ordered_points[3]),
            np.linalg.norm(ordered_points[3] - ordered_points[0])
        ])
        pts2 = np.float32([[0, 0], [side, 0], [side, side], [0, side]])
        matrix = cv2.getPerspectiveTransform(ordered_points, pts2)
        chessboard = cv2.warpPerspective(image, matrix, (int(side), int(side)))
        return chessboard
    else:
        raise ValueError("Chessboard contour could not be found or is not a quadrilateral.")
