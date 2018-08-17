def multiplicativeCipherEncrypt(pt, numberOfShits):
        pt = pt.replace(" ", "").lower()
        alphabets = [chr(i) for i in range(97, 123)]
        mapping = {i: alphabets[(alphabets.index(i) * numberOfShits) % 26] for i in alphabets}
        ct = ''
        for ch in pt:
            ct = ct + mapping[ch]
        return ct.upper()

pt = input("Enter Plain Text: ")
n = input("Enter n: ")
ct = multiplicativeCipherEncrypt(pt, int(n))
print("\nPlain Text : '{0}'\nEncrypted Text: '{1}'".format(pt, ct))