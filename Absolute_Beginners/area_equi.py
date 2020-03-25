from math import *
user_input = input()
try:
  a = float(user_input)
  area = (1/4)*(sqrt(3)*a*a)
  print("{:.2f}".format(area))
except ValueError:
  print("Not a number")