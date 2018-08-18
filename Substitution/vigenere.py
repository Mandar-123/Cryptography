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

def vigenereCipherDecrypt(ct, key):
        ct = ct.replace(" ", "").lower()
        key = key.replace(" ", "").lower()
        keyDup = ''
        for i in range(math.ceil(len(ct) / len(key))):
            keyDup = keyDup + key
        alphabets = [chr(i) for i in range(97, 123)]
        pt = ''
        for c1, c2 in zip(ct, keyDup):
            pt = pt + alphabets[(alphabets.index(c1) - alphabets.index(c2)) % 26]
        return pt
		
while(True):
	ch = input("\nFor Encryption: Enter 1\nFor Decryption: Enter 2\n")
	if ch == '1':	
		pt = input("Enter Plain Text: ")
		key = input("Enter Key: ")
		ct = vigenereCipherEncrypt(pt, key)
		print("\nPlain Text : '{0}'\nCipher Text: '{1}'".format(pt, ct))
	elif ch == '2':
		ct = input("Enter Cipher Text: ")
		key = input("Enter Key: ")
		pt = vigenereCipherDecrypt(ct,key)
		print("\nCipher Text : '{0}'\nPlain Text: '{1}'".format(ct, pt))
	else:
		print("Invalid choice!!")
	ch = input("\nPress 'Y' to continue, else press 'N'\n")
	if ch == 'N' or ch == 'n':
		break