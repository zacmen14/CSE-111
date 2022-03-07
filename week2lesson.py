import math

def compute_circle_area(radius):
    area = radius**2 * math.pi
    return area

user_radius = float(input("Please enter a radius: "))

print(round(compute_circle_area(5), 2))
print(compute_circle_area(user_radius))
print(round(compute_circle_area(user_radius)))