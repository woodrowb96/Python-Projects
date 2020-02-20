

def bsts(n):

	n_node_bsts = {0:1,1:1} #create cache

	def _bsts(n):

		count = 0	#start sum at 0

		if n not in n_node_bsts:# if n not in dict add it to cach

			for i in  range(1,n+1):	#sum from i = 1 to n	
				count += _bsts(i - 1)*_bsts(n - i)	

			n_node_bsts[n] = count  # add to cache

		return n_node_bsts[n]

	return _bsts(n)


