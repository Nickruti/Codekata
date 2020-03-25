user_input_a, user_input_b = input().split()

try:
  a = int(float(user_input_a))
  b = int(float(user_input_b))
  
  if  a<b:
    print(a)    
  else:
    print(b)
except ValueError:
  print("Not a number")