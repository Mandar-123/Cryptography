def findInMatrix(mat, val, rows, cols):
        for i in range(rows):
            for j in range(cols):
                if(mat[i][j] == val):
                    return i,j
    
def getEnc(l, mat):
	s = ''
	for [c1, c2] in l:
		xpos1, ypos1 = findInMatrix(mat, c1, 5, 5)
		xpos2, ypos2 = findInMatrix(mat, c2, 5, 5)
		
		if xpos1 != xpos2 and ypos1 != ypos2:
			c1 = mat[xpos1][ypos2]
			c2 = mat[xpos2][ypos1]
		elif xpos1 == xpos2:
			c1 = mat[xpos1][(ypos1 + 1)%5]
			c2 = mat[xpos2][(ypos2 + 1)%5]
		else:
			c1 = mat[(xpos1 + 1)%5][ypos1]
			c2 = mat[(xpos2 + 1)%5][ypos2]
		s = s + c1 + c2 
	return s

def getDec(l, mat):
	s = ''
	for [c1, c2] in l:
		xpos1, ypos1 = findInMatrix(mat, c1, 5, 5)
		xpos2, ypos2 = findInMatrix(mat, c2, 5, 5)
		
		if xpos1 != xpos2 and ypos1 != ypos2:
			c1 = mat[xpos1][ypos2]
			c2 = mat[xpos2][ypos1]
		elif xpos1 == xpos2:
			c1 = mat[xpos1][(ypos1 - 1)%5]
			c2 = mat[xpos2][(ypos2 - 1)%5]
		else:
			c1 = mat[(xpos1 - 1)%5][ypos1]
			c2 = mat[(xpos2 - 1)%5][ypos2]
		s = s + c1 + c2 
	return s
    
def playFairEncrypt(pt, key):
	matrix = []
	pt = pt.replace(" ", "").lower()
	pt = pt.replace('j','i')
	key = key.replace(" ", "").lower()
	charactersInKey = list()
	[charactersInKey.append(i) for i in key if i not in charactersInKey]
	[charactersInKey.append(chr(i)) for i in range(97, 123) if chr(i) not in charactersInKey]
	minPos = min(charactersInKey.index('i'), charactersInKey.index('j'))
	charactersInKey = list(filter(lambda ch: ch != 'i' and ch != 'j', charactersInKey))
	charactersInKey.insert(minPos, 'i')
	for i in range(0,25, 5):
		matrix.append(charactersInKey[i:i+5])
	
	listOfDoubles = list()
	i = 0
	
	while i!= len(pt):
		if i == len(pt) - 1:
			if i%2 == 0:
				pt = pt + 'x'
				listOfDoubles.append(pt[i] + pt[i+1])
			break
		if i%2 == 0:
			if pt[i] == pt[i + 1]:
				pt = pt[0:i+1] + 'x' + pt[i+1:]
			listOfDoubles.append(pt[i] + pt[i+1])
		i = i + 1
	ct = getEnc(listOfDoubles,matrix).upper()
	return ct, matrix

def playFairDecrypt(ct, key):
	matrix = []
	ct = ct.replace(" ", "").lower()
	key = key.replace(" ", "").lower()
	charactersInKey = list()
	[charactersInKey.append(i) for i in key if i not in charactersInKey]
	[charactersInKey.append(chr(i)) for i in range(97, 123) if chr(i) not in charactersInKey]
	minPos = min(charactersInKey.index('i'), charactersInKey.index('j'))
	charactersInKey = list(filter(lambda ch: ch != 'i' and ch != 'j', charactersInKey))
	charactersInKey.insert(minPos, 'i')
	for i in range(0, 25, 5):
		matrix.append(charactersInKey[i:i+5])
	
	listOfDoubles = list()
	i = 0
	
	while i != len(ct):
		if i%2 == 0:
			listOfDoubles.append(ct[i] + ct[i+1])
		i = i + 1
	
	pt = getDec(listOfDoubles,matrix)
	return pt, matrix    
		
while(True):
	ch = input("\nFor Encryption: Enter 1\nFor Decryption: Enter 2\n")
	if ch == '1':	
		pt = input("Enter Plain Text: ")
		keyd = input("Do you wish to enter a key? If yes enter 'Y' else enter 'N'\n")
		if keyd == 'Y' or keyd == 'y':
			key = input("Enter Key: ")
		else:
			key = ""
		obj = playFairEncrypt(pt, key)
		ct = obj[0]
		matrix = obj[1]
		print("\nPlain Text : '{0}'\nEncrypted Text: '{1}'\nKey Matrix:".format(pt, ct))
		for l in matrix:
			print(l)

	elif ch == '2':
		ct = input("Enter Cipher Text: ")
		keyd = input("Do you wish to enter a key? If yes enter 'Y' else enter 'N'\n")
		if keyd == 'Y' or keyd == 'y':
			key = input("Enter Key: ")
		else:
			key = ""
		obj = playFairDecrypt(ct, key)
		pt = obj[0]
		matrix = obj[1]
		print("\nCipher Text : '{0}'\nPlain Text: '{1}'\nKey Matrix:".format(ct, pt))
		for l in matrix:
			print(l)
			
	else:
		print("Invalid choice!!")
	ch = input("\nPress 'Y' to continue, else press 'N'\n")
	if ch == 'N' or ch == 'n':
		break