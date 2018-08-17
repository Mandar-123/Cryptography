import math

def vernamCipherEncrypt(pt, key):
	pt = pt.replace(" ", "").lower()
	key = key.replace(" ", "").lower()
	alphabets = [chr(i) for i in range(97, 123)]
	st = ''
	for c1, c2 in zip(pt, key):
		st = st + alphabets[(alphabets.index(c1) + alphabets.index(c2)) % 26]
	return st.upper()

pt = input("Enter Plain Text: ")
key = input("Enter Key: ")
ct = vernamCipherEncrypt(pt, key)
print("\nPlain Text : '{0}'\nEncrypted Text: '{1}':".format(pt, ct))