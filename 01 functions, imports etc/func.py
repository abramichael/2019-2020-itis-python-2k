def f(x):
	return x + 1
	
	
g = f

print(g(5))

def apply(fun, x):
	return fun(x)
	
print(h(f, 10))

def t(f, g, x):
	if (x > 0):
		return f(x)
	else:
		return g(x)
		

y = apply(lambda x: x * x, 10)

def sqr(x):
	return x * x
	
sqr = lambda x: x * x



		
		
		
		
		
		
		
		
		