user_input = input()
try:
  celsius = float(user_input)
  fahrenheit = (celsius * (9/5)) + 32 
  print("{:.2f}".format(fahrenheit))
except ValueError:
  print("Not a number")