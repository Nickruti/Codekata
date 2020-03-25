
user_input = input()
try:
    radius = int(user_input)
    if radius<0:
        print("Error")
    else:
        circum = 2*3.1415926*radius
        print("{:.2f}".format(circum))
      
except:
  	print("Not a number")