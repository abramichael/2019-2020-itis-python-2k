f = open("my_main.py")
import string
def is_letter(c):
	#return c >= 'a' and c <= 'z'
	return c in string.ascii_lowercase
	
d = {}
c = 'a'
while c <= 'z':
	d[c] = 0
	c = chr(ord(c) + 1)

for line in f:
	line = line.lower()
	for c in line:
		if (is_letter(c)):
			d[c] += 1
		
print d