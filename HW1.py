import hashlib
#input is a string (for starting hash)
#return (s,t,n)
#s, t are different ASCII strings
#with same high order 40 bits
#n is the number of calls to SHA-1
def func(a):
	n = 0
	hashes = []
	
	h2 = hashlib.sha1(a).hexdigest()[0:10]
	n = n+1
	hashes.append((a,h2))
	while True:
		h3 = hashlib.sha1(h2).hexdigest()[0:10]
		n = n+1
		for (string,hash) in hashes:
			if hash == h3:
				return (string,h2,n)
		hashes.append((h2,h3))
		h2 = h3

print ""
(s,t,n) = func("a")
print s
print t
print n
