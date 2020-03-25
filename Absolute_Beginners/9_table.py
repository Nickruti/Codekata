
try:
  N = int(float(input()))
  if N==0 :
    print("NULL")
    
  elif N<0:
    print("Error")
    
  else :
    for i in range (1,N+1):
    	print(9*i, end=" ")
    
except ValueError:
  print("Not a number")