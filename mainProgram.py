from powerFunction import power

error = True
while error == True:
	userBase = input("Type a base: ")
	userExponent = input("Type an exponent: ")
	
	try: 
		userBase = float(userBase)
		userExponent = float(userExponent)
	except ValueError:
			print("Sorry, at least one of those is not a number.")
			error = True
			
	else:
		userPower = power(userBase, userExponent)
		print("{} to the power of {} is {}".format(userBase, userExponent, userPower))
		error = False
