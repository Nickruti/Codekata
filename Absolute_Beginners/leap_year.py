user_input = input()
try:
	year = int(user_input)
	if year%100==0:
		if year%400==0:
			print("Y")
		else:
			print("N")
	elif year%4==0:
		print("Y")
	else:
		print("N")

except ValueError:
  	print("Not a number")