
def max_wis(a):
	max_sums = {-1:(0,[]), 0:(0,[])}	# createcache 

	def _max_wis(a):
		n = len(a)	#keys are  length of a
	 
		if n not in max_sums:	#if key is not in dict 
		
			minus_one,set_one = _max_wis(a[:n-1])	#get n-1 max and set
			minus_two,set_two = _max_wis(a[:n-2])	#get n-2
		
			if minus_one > minus_two + a[n-1]:	#if n-1 greater than n-2
				max_sums[n] = (minus_one,set_one)
			else:					#if n-2 greater than n-1
				max_sums[n] = (minus_two + a[n-1],set_two + [a[n-1]])

		return max_sums[n]

	return _max_wis(a)


