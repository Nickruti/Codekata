user_input_a = input()
user_input_b = input()
try:
  a = int(user_input_a)
  b = int(user_input_b)
  if a<1 or b<1 :
    print("Not a Natural Number")
  else :
    area = a * b
    print("{:.1f}".format(area))
except ValueError:
  print("Not a number")