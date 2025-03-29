import math
def calculate_angle(x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1

    angle_rad = math.atan2(dy,dx)

    angle_deg = math.degrees(angle_rad)

    return angle_deg