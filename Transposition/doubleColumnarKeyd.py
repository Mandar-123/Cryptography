def simpleColumnarEncrypt(pt, rows, cols, key = 0):
        actualKey = ''
        if key == 0:
            for i in range(cols):
                actualKey = actualKey + str(i + 1)
        else:
            actualKey = key
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
    
def doubleColumnarEncrypt(pt, rows, cols, key = 0):
	st = simpleColumnarEncrypt(simpleColumnarEncrypt(pt, rows, cols, key), rows, cols, key)
	return st.upper()
	
pt = input("Enter Plain Text: ")
key = input("Enter Key: ")
rows = input("Enter number of rows: ")
cols = input("Enter number of columns: ")
ct = doubleColumnarEncrypt(pt, int(rows), int(cols),key)
print("\nPlain Text : '{0}'\nEncrypted Text: '{1}':".format(pt, ct))