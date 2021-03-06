import time
import shelve

def calculate(func):
	def inside(*args, **kwargs):
		
		start=time.time()
		time.sleep(1)
		result=func(*args, **kwargs)
		end=time.time()
		print("Total time taken in : ", func.__name__, end - start)
		print(result)
		return result
	return inside

@calculate	
def dictionary_encrypt(text1,cipher):
	ciphertext=''
	for i in text1:
		if i in cipher:
			ciphertext=ciphertext+cipher[i]
		else:
			ciphertext=ciphertext+i
	return ciphertext

@calculate
def dictionary_decrypt(text2,cipher):
	plaintext=''
	dcipher = dict([(value, key) for key, value in cipher.items()])
	for i in text2:
		if i in dcipher:
			plaintext=plaintext+dcipher[i]
		else:
			plaintext=plaintext+i
	return plaintext

@calculate
def shelve_encrypt(text1,cipher):
	s=shelve.open('test')
	s['text']=cipher
	ciphertext=''
	for i in text1:
		if i in s['text']:
			ciphertext=ciphertext+s['text'][i]
		else:
			ciphertext=ciphertext+i
	s.close()
	return ciphertext

@calculate
def shelve_decrypt(text2,cipher):
	s=shelve.open('test')
	plaintext=''
	s['text']=cipher
	s['dtext']=dict([(value,key) for key,value in s['text'].items()])
	for i in text2:
		if i in s['dtext']:
			plaintext=plaintext+s['dtext'][i]
		else:
			plaintext=plaintext+i
	s.close()
	return plaintext
			
	

input_text = "HI WELCOM TO PYTHON"
cipher ={"A": "T", "B": "D", "C": "L", "D": "O", "E": "F","F": "A", "G": "G", "H": "J", "I": "K", "J": "R","K": "I", "L": "C", "M": "V", "N": "P", "O": "W","P": "U", "Q": "X", "R": "Y", "S": "B", "T": "E","U": "Z", "V": "Q", "W": "S", "X": "N", "Y": "M","Z": "H"}
citext=dictionary_encrypt(t,cipher)
pltext=dictionary_decrypt(citext,cipher)
cis=shelve_encrypt(t,cipher)
pis=shelve_decrypt(cis,cipher)