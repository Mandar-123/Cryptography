import math

def vigenereCipherEncrypt(pt, key):
	pt = pt.replace(" ", "").lower()
	key = key.replace(" ", "").lower()
	keyDup = ''
	for i in range(math.ceil(len(pt) / len(key))):
		keyDup = keyDup + key
	for i in range(len(keyDup) - len(pt)):
		pt = pt + 'x'
	alphabets = [chr(i) for i in range(97, 123)]
	st = ''
	for c1, c2 in zip(pt, keyDup):
		st = st + alphabets[(alphabets.index(c1) + alphabets.index(c2)) % 26]
	return st.upper()
	
pt = input("Enter Plain Text: ")
key = input("Enter Key: ")
ct = vigenereCipherEncrypt(pt, key)
print("\nPlain Text : '{0}'\nEncrypted Text: '{1}':".format(pt, ct))