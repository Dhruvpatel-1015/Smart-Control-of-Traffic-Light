# src/detect.py

from ultralytics import YOLO
import cv2
from utils import draw_boxes, count_vehicles_by_lane


class VehicleDetector:
    def __init__(self, model_path: str, conf_thresh: float = 0.4):
        self.model = YOLO(model_path)
        self.conf_thresh = conf_thresh

    def detect(self, frame):
        results = self.model(frame, conf=self.conf_thresh)[0]
        return results

    def process_frame(self, frame, lane_regions=None):
        results = self.detect(frame)
        annotated_frame = draw_boxes(frame.copy(), results)

        lane_counts = {}
        if lane_regions:
            lane_counts = count_vehicles_by_lane(results, lane_regions)

        return annotated_frame, lane_counts


if __name__ == "__main__":

    detector = VehicleDetector("models/best.pt")
    img = cv2.imread("C:\AI Projects\Smart Control of Traffic Light\sample data\Copy of India_Traffic_cover-1.jpg")

    output, counts = detector.process_frame(img)
    print("Vehicle counts:", counts)

    cv2.imshow("Detection Output", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

