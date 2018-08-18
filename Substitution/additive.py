def additiveCipherEncrypt(pt, numberOfShits):
        pt = pt.replace(" ", "").lower()
        alphabets = [chr(i) for i in range(97, 123)]
        mapping = {i: alphabets[(alphabets.index(i) + numberOfShits) % 26] for i in alphabets}
        ct = ''
        for ch in pt:
            ct = ct + mapping[ch]
        return ct.upper()

def additiveCipherDecrypt(ct, numberOfShits):
	ct = ct.replace(" ", "").lower()
	alphabets = [chr(i) for i in range(97, 123)]
	mapping = {i: alphabets[(alphabets.index(i) - numberOfShits) % 26] for i in alphabets}
	pt = ''
	for ch in ct:
		pt = pt + mapping[ch]
	return pt

while(True):
	ch = input("\nFor Encryption: Enter 1\nFor Decryption: Enter 2\n")
	if ch == '1':	
		pt = input("Enter Plain Text: ")
		n = input("Enter number of rotations: ")
		ct = additiveCipherEncrypt(pt, int(n))
		print("\nPlain Text : '{0}'\nCipher Text: '{1}'".format(pt, ct))
	elif ch == '2':
		ct = input("Enter Cipher Text: ")
		n = input("Enter number of rotations: ")
		pt = additiveCipherDecrypt(ct,int(n))
		print("\nCipher Text : '{0}'\nPlain Text: '{1}'".format(ct, pt))
	else:
		print("Invalid choice!!")
	ch = input("\nPress 'Y' to continue, else press 'N'\n")
	if ch == 'N' or ch == 'n':
		break