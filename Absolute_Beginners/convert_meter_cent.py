user_input=input()
try:
	A=int(user_input)
	meter=A*1000
	centi=A*100000
	print(meter)
	print(centi)
except ValueError:
  	print("Not a Number")