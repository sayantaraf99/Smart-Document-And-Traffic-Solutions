# Importing necessary libraries
import random

# Simulating traffic camera feed data
class TrafficCamera:
    def _init_(self, camera_id):
        self.camera_id = camera_id

    # Simulating real-time incident detection
    def detect_incident(self):
        # Randomly generate incidents (0: no incident, 1: minor, 2: severe)
        return random.choice([0, 1, 2])

# Traffic Control System to manage detected incidents
class TrafficControlSystem:
    def _init_(self):
        self.incident_log = []

    # Function to process and manage detected incidents
    def manage_incident(self, camera, incident_level):
        if incident_level == 0:
            print(f"Camera {camera.camera_id}: No incidents detected.")
        elif incident_level == 1:
            print(f"Camera {camera.camera_id}: Minor incident detected. Alerting traffic control and dispatching team.")
            self.incident_log.append((camera.camera_id, "Minor Incident"))
        elif incident_level == 2:
            print(f"Camera {camera.camera_id}: Severe incident detected. Immediate response required! Alerting emergency services.")
            self.incident_log.append((camera.camera_id, "Severe Incident"))

# Main function to simulate real-time data
def main():
    # Initialize the traffic control system
    traffic_system = TrafficControlSystem()

    # Create a few camera objects
    cameras = [TrafficCamera(i) for i in range(1, 6)]

    # Simulate the detection of incidents
    for camera in cameras:
        incident_level = camera.detect_incident()
        traffic_system.manage_incident(camera, incident_level)

    print("\nIncident Log:")
    for log in traffic_system.incident_log:
        print(f"Camera ID: {log[0]}, Incident: {log[1]}")

    # Print team details at the end
    print("\nTeam Name: DevOps Ninjas")
    print("Member 1: Sayan Som")
    print("Member 2: Shankha Shubhra Chatterjee")
    print("Member 3: Sayan Tarafdar")

# Custom input for hackathon submission
if _name_ == "_main_":
    main()