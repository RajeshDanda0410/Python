import hashlib

original_url = input("enter the url to shorten :")

def shorten_url(newurl):

	result = hashlib.md5(newurl.encode()) # using hashlib MD5 function to generate unique code 
	x = result.hexdigest()
	z = list(x)    # listing the generated hast value to copy first few letters from the value
	
	return "".join(z[:7])

y = shorten_url(original_url)
print("the shorten url is \n https://bit.ly/" + y) 
short_url = input("enter the url to find original:")

def get_original_url(m,n):
	newresult = hashlib.md5(n.encode())
	x = newresult.hexdigest()
	z = list(x)
	k = "https://bit.ly/" + "".join(z[:7])
	if (k == m):
		return n
	else :
		return "404 not found"
print(get_original_url(short_url,original_url))

""" 
UUID:
UUID is used for generating unique numbers . 
This module provides immutable UUID objects  and there are  functions like uuid1(), uuid3(), uuid4(), uuid5() for generating version 1, 3, 4, and 5 UUIDs as specified in RFC 4122.
For getting unique id call  uuid1() and uuid4().
uuid3() Generate a UUID based on the MD5 hash of a namespace identifier 
uuid5() generate a UUID based on the SHA-1 hash of a namespace identifier

MD5 hash:
There are many hash functions defined in the “hashlib” library in python.
This article deals with explanation and working of MD5 hash.
This hash function accepts sequence of bytes and returns 128 bit hash value, usually used to check data integrity but has security issues.

Functions associated :

encode() : Converts the string into bytes to be acceptable by hash function.
digest() : Returns the encoded data in byte format.
hexdigest() : Returns the encoded data in hexadecimal format."""
