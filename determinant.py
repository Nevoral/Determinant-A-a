import numpy as np

def getSubMatrix(i, j, m):
    return [row[:j] + row[j+1:] for row in (m[:i] + m[i+1:])]

def retOne(i):
    if i % 2 == 0:
        return 1
    else:
        return -1
    
def getDeterminant(m):
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    det = 0.0
    for i in range(len(m)):
        det += (retOne(i)) * m[i][0] * getDeterminant(getSubMatrix(i, 0, m))
    return det

def controlSquare(m):
    row, columns = 0, 0
    if len(m) > 0:
        row = len(m)
        columns = len(m[0])
    if row == columns:
        return getDeterminant(m)
    else:
        print("Matice nemá stejný počet řádků a sloupců")
        return None

def matrixFromTXT(adressFile):
    txt = []
    f = open(adressFile, "r")
    for i in f:
        txt.append(i[1:])
    f.close()
    matrix = []
    for i in txt:
        row = i.split(" ")
        row = convertFloat(row)
        matrix.append(row)
    det = controlSquare(matrix)
    print("Determinant je: {}".format(det))
    y=np.array([np.array(xi) for xi in matrix])
    detn = np.linalg.det(y)
    print("determinant od numpy je: {}".format(detn))

def convertFloat(row):
    matrix = []
    for i in row:
        matrix.append(float(i))
    return matrix

if __name__ == "__main__":
    while True:
        prompt = "Zadej název/adresu txt souboru s matici. "
        k = input(prompt)
        matrixFromTXT(k)
        i = input("Chceš to ukončit? Press p")
        if i == "p":
            break
