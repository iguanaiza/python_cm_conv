print("This program will calculate how many meters or inches is in provided centimeter value.")
print("Provide value in cm:")
cm = int(input())
m = cm / 100
cal = cm / 2.54

print("{:1.2f} cm = {:1.2f} m or {:1.2f} in.". format(cm, m, cal))
