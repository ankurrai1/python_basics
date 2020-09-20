# TASK : is to write a program to do matrix multiplication


#  Global matrixs


m1 = [ [1,2,3],
       [4,5,6],
       [7,8,9] ]

m2 = [ [5,6,7],
       [6,1,2],
       [3,2,1] ]


def printMatrix(result):
    for ele in result:
        print(ele)

def matrixMultiplication(a, b):
    result = [ [0,0,0],
               [0,0,0],
               [0,0,0] ]
    
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    
    return result

res = matrixMultiplication(m1, m2)
printMatrix(res)




