import cv2
from lane_detection import detect_lane
from obstacle_detection import detect_obstacles
from car_control import control_steering
import numpy as np

def main():
    cap = cv2.VideoCapture("test.mp4")  # Replace with 0 for webcam input

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Step 1: Detect lanes
        lane_frame = detect_lane(frame)
        
        # Step 2: Detect obstacles
        obstacle_frame = detect_obstacles(lane_frame)
        
        # Step 3: Get control commands
        # Placeholder: Define lane and obstacle positions manually for now
        lane_position = 0.5  # center lane (adjust dynamically if detected)
        obstacle_position = None  # add logic to determine if obstacle is detected

        command = control_steering(lane_position, obstacle_position)
        print("Control Command:", command)
        
        # Display the frame
        cv2.imshow("Self-Driving Car", obstacle_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
