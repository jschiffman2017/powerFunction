from powerFunction import power

error = True
while error == True:
	userBase = input("Type a base: ")
	userExponent = input("Type an exponent: ")
	
	try: 
		userBase = float(userBase)
	except ValueError:
		print("Sorry, your base is not a number.")
		error = True
	try:
		userExponent = int(userExponent)
	except ValueError:
			print("Sorry, your exponent is not an integer.")
			error = True
			
	else:
		userPower = power(userBase, userExponent)
		print("{} to the power of {} is {}".format(userBase, userExponent, userPower))
		error = False
