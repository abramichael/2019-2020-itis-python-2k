def buter(f):
	def wrapper():
		print("bread")
		f()
		print("bread")
	return wrapper

@buter
def meat():
	print("meat")

@buter
def cheese():
	print("cheese")
	
meat()