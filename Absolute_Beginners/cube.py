user_input = input()
try:
  number = int(float(user_input))
  cube = number*number*number
  print(cube)
except:
  print("Not a Number")