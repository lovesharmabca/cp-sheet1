
angle1 = int(input("Enter first angle: "))
angle2 = int(input("Enter second angle: "))
angle3 = int(input("Enter third angle: "))
if angle1 + angle2 + angle3 != 180 or angle1 <= 0 or angle2 <= 0 or angle3 <= 0:
    print("Invalid triangle angles (must sum to 180° and each angle > 0)")
else:
    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        print("Right-angled triangle (one 90° angle)")
    elif angle1 > 90 or angle2 > 90 or angle3 > 90:
        print("Obtuse triangle (one angle > 90°)")
    else:
        print("Acute triangle (all angles < 90°)")