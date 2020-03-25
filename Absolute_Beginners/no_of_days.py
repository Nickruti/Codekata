user_input = input()
try:
  number = int(float(user_input))
  if number>12 :
    print("Error")
  elif number<1:
    print("Error")
  else :
    months_31 = [1, 3, 5, 7, 8, 10, 12]
    months_30 = [4, 6, 9, 11]
    if number==2:
      print("28")
    elif number in months_31:
      print("31")
    else:
      print("30")
      
except ValueError:
  print("Not a Number")