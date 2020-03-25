user_input = input()
try:
  number = int(float(user_input))
  if number==0 :
    print("Error")
  elif number<0:
    print("Error")
  else :
    print(number*number)
except ValueError:
  print("Not a number")