# MY ORIGINAL POWER FUNCTION WAS RECURSIVE; THIS ONE IS NOT RECURSIVE

def power(base, exponent):
	if exponent == 0:
		return 1
	else:
		total = 1
		while exponent > 0:
			total = total * base
			exponent -= 1
		return total
