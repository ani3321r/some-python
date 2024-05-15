import math

def circle_stats(radius):
    area = math.pi*radius**2
    cir = 2*math.pi*radius
    return area, cir

a, c = circle_stats(6)

print("area:", round(a,3), "circumference:", round(c,3))