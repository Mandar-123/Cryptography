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
		
pt = input("Enter Plain Text: ")
ct = railFenceEncrypt(pt)
print("\nPlain Text : '{0}'\nEncrypted Text: '{1}'".format(pt, ct))