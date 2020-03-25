user_input = input()
try:
    number = int(float(user_input))
    if number==0:
        print("1")

    elif number==1:
        print("1")
    
    elif number<0:
        print("Negative Number")
    else:
        fact = 1
        for i in range(1, number+1):
            fact = fact * i
        print(fact)

except:
  print("Not a Number")