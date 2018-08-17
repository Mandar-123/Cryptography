def additiveCipherEncrypt(pt, numberOfShits):
        pt = pt.replace(" ", "").lower()
        alphabets = [chr(i) for i in range(97, 123)]
        mapping = {i: alphabets[(alphabets.index(i) + numberOfShits) % 26] for i in alphabets}
        ct = ''
        for ch in pt:
            ct = ct + mapping[ch]
        return ct.upper()
		
pt = input("Enter Plain Text: ")
n = input("Enter number of rotations: ")
ct = additiveCipherEncrypt(pt, int(n))
print("\nPlain Text : '{0}'\nEncrypted Text: '{1}'".format(pt, ct))