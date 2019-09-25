#!encoding: utf-8

def factorial(n):
	"""
	We are calculating factorial of number n
	"""
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)
	
	
def s(x=1, n=1):
	s = 1.0
	k = 1
	d = 1.0
	f = 1
	while (k <= n):
		f *= k
		d *= x
		s += d / f
		k += 1 
	return s
	
	
def sum(*args, **kwargs):
	s = 0
	for x in args:
		s += x
	s += kwargs["special"]
	return s
	
	
#Main метод в Python
if __name__ == "__main__":	
	print(help(factorial))