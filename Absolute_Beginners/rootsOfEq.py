from math import *
user_input_a, user_input_b, user_input_c = input().split()

try:
    a = float(user_input_a)
    b = float(user_input_b)
    c = float(user_input_c)
    root1 = (-b + sqrt((b*b) - (4*a*c))) / (2*a)
    root2 = (-b - sqrt((b*b) -(4*a*c))) / (2*a)
    print("{:.2f}".format(root1))
    print("{:.2f}".format(root2))
except ValueError:
  	print("Not a Number")