def simpleColumnarEncrypt(pt, rows, cols, key = 0):
	actualKey = ''
	if key == 0:
		for i in range(cols):
			actualKey = actualKey + str(i + 1)
	else:
		actualKey = key.replace(" ", "")
	pt = pt.replace(" ", "").lower()
	ptList = list(pt)
	numOfEle = rows * cols
	for i in range(numOfEle - len(ptList)):
		ptList.append('x')
	mat = [ptList[i : i + cols] for i in range(0, numOfEle, cols)]
	st = ''
	for i in actualKey:
		for j in range(rows):
			st = st + mat[j][int(i) - 1]
	return st.upper()

def simpleColumnarDecrypt(ct, rows, cols, key = 0):
	actualKey = ''
	if key == 0:
		for i in range(cols):
			actualKey = actualKey + str(i + 1)
	else:
		actualKey = key.replace(" ", "")
	ct = ct.replace(" ", "").lower()
	ctList = [ct[i : i + rows] for i in range(0,rows*cols,rows)]
	pt = ''
	dic = {}
	for index,value in enumerate(actualKey):
		dic[int(value)] = index
	for i in range(rows):
		for j in range(1,cols+1):
			pt = pt + ctList[dic[j]][i]
	return pt

while(True):
	ch = input("\nFor Encryption: Enter 1\nFor Decryption: Enter 2\n")
	if ch == '1':	
		pt = input("Enter Plain Text: ")
		key = 0
		keyd = input("Do you wish to enter a key? If yes enter 'Y' else enter 'N'\n")
		if keyd == 'Y' or keyd == 'y':
			key = input("Enter Key: ")
		rows = input("Enter number of rows: ")
		cols = input("Enter number of columns: ")
		ct = simpleColumnarEncrypt(pt, int(rows), int(cols), key)
		print("\nPlain Text : '{0}'\nCipher Text: '{1}'".format(pt, ct))
		
	elif ch == '2':
		ct = input("Enter Cipher Text: ")
		key = 0
		keyd = input("Do you wish to enter a key? If yes enter 'Y' else enter 'N'\n")
		if keyd == 'Y' or keyd == 'y':
			key = input("Enter Key: ")
		rows = input("Enter number of rows: ")
		cols = input("Enter number of columns: ")
		pt = simpleColumnarDecrypt(ct, int(rows), int(cols), key)
		print("\nCipher Text : '{0}'\nPlain Text: '{1}'".format(ct, pt))
			
	else:
		print("Invalid choice!!")
	ch = input("\nPress 'Y' to continue, else press 'N'\n")
	if ch == 'N' or ch == 'n':
		break
