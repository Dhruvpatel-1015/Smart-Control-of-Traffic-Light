# src/utils.py

import cv2
import numpy as np


def draw_boxes(frame, results):
    """
    Draws bounding boxes from YOLOv8 results on frame.
    """
    for box in results.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        label = f"{results.names[cls_id]} {conf:.2f}"

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, label, (x1, y1 - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return frame


def count_vehicles_by_lane(results, lane_regions):
    """
    lane_regions = {
        "lane1": [(x1,y1), (x2,y2), (x3,y3), (x4,y4)],
        ...
    }
    """
    lane_counts = {lane: 0 for lane in lane_regions}

    for box in results.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cx, cy = int((x1 + x2) / 2), int((y1 + y2) / 2)

        for lane, polygon in lane_regions.items():
            if cv2.pointPolygonTest(np.array(polygon), (cx, cy), False) >= 0:
                lane_counts[lane] += 1
                break

    return lane_counts
