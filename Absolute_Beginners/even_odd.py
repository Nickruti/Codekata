user_input = input()
try:
  number = int(float(user_input))
  if number==0 :
    print("Zero")
  elif number%2==0:
    print("Even")
  else :
    print("Odd")
except ValueError:
  print("Not a number")