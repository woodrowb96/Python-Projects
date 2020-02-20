
def num_no(n):

	bits_strings = {0:1,1:2}

	def _num_no(n):

		if n not in bits_strings:
			bits_strings[n] = _num_no(n-1) + _num_no(n-2)

		return bits_strings[n]


	return _num_no(n)



def num_yes(n):

	return (2**n) - num_no(n)


