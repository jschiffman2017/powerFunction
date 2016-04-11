def power(base, exponent):
	if exponent == 0:
		return(1)
	else:
		return(base * power(base, exponent - 1))
		
userBase = input("What is the base? ")
userBase = float(userBase)
userExponent = input("What is the exponent? ") 
userExponent = float(userExponent)

userPower = power(userBase, userExponent)

print(userPower)