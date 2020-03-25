user_input_a = input()
user_input_b = input()
user_input_c = input()
try:
  a = int(float(user_input_a))
  b = int(float(user_input_b))
  c = int(float(user_input_c))
  
  if  a>b:
    if a>c:
      print(a)
    elif c>b:
        print(c)
    else:
        print(b)
      
      
  elif b>c:
    print(b)
    
  else :
    print(c)
except ValueError:
  print("Not a number")