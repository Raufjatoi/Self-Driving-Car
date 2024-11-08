def control_steering(lane_position, obstacle_position):
    # Basic proportional control (could be more complex, but keeping it simple)
    if obstacle_position:
        print("Obstacle detected, slowing down or stopping.")
        return "STOP"
    
    if lane_position < 0.4:
        print("Steering Left")
        return "LEFT"
    elif lane_position > 0.6:
        print("Steering Right")
        return "RIGHT"
    else:
        print("Going Straight")
        return "STRAIGHT"
