# src/traffic_controller.py

import time


class TrafficController:
    def __init__(self, min_green=10, max_green=60):
        self.min_green = min_green
        self.max_green = max_green

    def compute_green_time(self, vehicle_count):
        """
        Maps vehicle count → green light duration.
        """
        return min(self.max_green, max(self.min_green, vehicle_count * 3))

    def choose_lane(self, lane_counts: dict):
        """
        Selects the lane with maximum vehicles.
        """
        if not lane_counts:
            return None
        return max(lane_counts, key=lane_counts.get)

    def run_cycle(self, lane_counts):
        lane = self.choose_lane(lane_counts)
        green_time = self.compute_green_time(lane_counts.get(lane, 0))

        print(f"🟢 Lane {lane} GREEN for {green_time} seconds")
        time.sleep(green_time)
        print(f"🔴 Lane {lane} RED")

        return lane, green_time


if __name__ == "__main__":
    controller = TrafficController()
    demo_counts = {"lane1": 12, "lane2": 5, "lane3": 18, "lane4": 7}
    controller.run_cycle(demo_counts)
