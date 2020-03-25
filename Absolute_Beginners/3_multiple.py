try:
  N = int(float(input()))
  if N<1 :
    print("Error")
    
  else :
    for i in range (1,4):
    	print(N*i, end=" ")
    
except ValueError:
  print("Not a number")