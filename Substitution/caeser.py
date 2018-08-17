def caesarCipherEncrypt(pt):
        pt = pt.replace(" ", "").lower()
        alphabets = [chr(i) for i in range(97, 123)]
        mapping = {i: alphabets[(alphabets.index(i) + 3) % 26] for i in alphabets}
        ct = ''
        for ch in pt:
            ct = ct + mapping[ch]
        return ct.upper()
		
pt = input("Enter Plain Text: ")
ct = caesarCipherEncrypt(pt)
print("\nPlain Text : '{0}'\nEncrypted Text: '{1}'".format(pt, ct))