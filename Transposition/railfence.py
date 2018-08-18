import math

def railFenceEncrypt(pt):
        pt = pt.replace(" ", "")
        pt = pt.lower()
        s1 = ''
        s2 = ''
        for i, ch in enumerate(pt):
            if i % 2 == 0:
                s1 = s1 + ch
            else:
                s2 = s2 + ch
        return (s1 + s2).upper()

def railFenceDecrypt(ct):
        ct = ct.replace(" ", "").lower()
        s1 = ct[0:math.ceil(len(ct)/2)]
        s2 = ct[math.ceil(len(ct)/2):]
        pt = ''
        for c1,c2 in zip(s1,s2):
            pt = pt + c1 + c2
        if len(s1) > len(s2):
            pt = pt + s1[-1]
        return pt

while(True):
	ch = input("\nFor Encryption: Enter 1\nFor Decryption: Enter 2\n")
	if ch == '1':	
		pt = input("Enter Plain Text: ")
		ct = railFenceEncrypt(pt)
		print("\nPlain Text : '{0}'\nCipher Text: '{1}'".format(pt, ct))
	elif ch == '2':
		ct = input("Enter Cipher Text: ")
		pt = railFenceDecrypt(ct)
		print("\nCipher Text : '{0}'\nPlain Text: '{1}'".format(ct, pt))
	else:
		print("Invalid choice!!")
	ch = input("\nPress 'Y' to continue, else press 'N'\n")
	if ch == 'N' or ch == 'n':
		break