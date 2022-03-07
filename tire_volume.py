import math

print("This program is here to help you find the")
print("volume of space inside a tire.")

print()

width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

pie = math.pi * width**2 * aspect_ratio
abriviation = width * aspect_ratio + 2540 * diameter
volume = pie * abriviation / 10000000000
print()

print(f"The approximate volume is {volume:.2f} liters")

from datetime import datetime
current_date_and_time = datetime.now()

with open("volumes.txt", mode="at") as volumes_file:
    print(f"{current_date_and_time:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}", file=volumes_file)
    print(f"{current_date_and_time:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}")
