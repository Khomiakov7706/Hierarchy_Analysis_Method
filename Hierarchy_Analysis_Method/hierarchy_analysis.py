import numpy as np
from re import T
import view

def vector(matrix):
    newMatrix = np.zeros(len(matrix))
    matSum = np.zeros(len(matrix))
    for i in range(0, len(matrix)):
        vect = matrix[:, i]
        w = vect / vect.sum()
        for j in range(0, len(matrix)):
            matSum[j] += w[j] 
    matSum = matSum / len(matrix)
    return matSum

def matrix(number, matrType, criterionNumber=0):
    """Function for creating a pairwise matrix"""
    A = np.ones([number, number])
    importance = [i for i in range(1, 10)] # list of allowed importance values
    importance2 = [i/10 for i in range(1, 10)]
    value = importance + importance2
    for i in range(0, number):
        for j in range(0, number):
            if i < j:
                if criterionNumber > 0:
                    a = str(input(f'Compare importance of {matrType} {i+1} to {matrType} {j+1} in criterion {criterionNumber}. \nType an integer from 0.1 to 9: '))
                else:
                    a = str(input(f'How much {matrType} {i+1} is more important than {matrType} {j+1}? Type an integer from 0.1 to 9: '))
                if float(a) in value: # error handling
                    A[i,j] = float(a)
                    A[j, i] = 1 / float(a)
                else:
                    print("It is an incorrect value. Let's start again \n")
                    main()
    return A

def consistencyCheck(initialMatrix): # Here will be the function that checks the consistency of the matrix
    A = initialMatrix
    meanConsistencyIndex = {
        1 : 0,
        2 : 0,
        3 : 0.58,
        4 : 0.9,
        5 : 1.12,
        6 : 1.24,
        7 : 1.32,
        8 : 1.41,
        9 : 1.45,
        10 : 1.49
    }
    eigenvalue,featurevector=np.linalg.eig(A)
    print(A)
    print('eigenvalue='+str(eigenvalue))
    print('featurevector='+str(featurevector))
    print('max(eigenvalue)='+str(max(eigenvalue)))
    print('len(A)='+str(len(A)))
    print('meanConsistensyIndex='+str(meanConsistencyIndex[len(A)]))
    consistensyIndex = (max(eigenvalue)-len(A))/(len(A)-1)
    print('consistensyIndex='+str(consistensyIndex))
    consistencyRelation = consistensyIndex/meanConsistencyIndex[len(A)]*100
    return consistencyRelation


def main():
    A = np.array([[4,1,-1],[1,4,-1],[-1,-1,4]])
    print (consistencyCheck(A))
    """numberCrit = str(input("How many criteria do you want to enter? Type an integer: "))
    if numberCrit.isdigit(): # error handling
        A = matrix(number= int(numberCrit), matrType= 'criterion')
        print(A)
        weights = vector(A)
        for i in range(len(weights)):
            print(f'Criterion {i} = {np.round(weights[i], 2)}')
    else:
        print("Something went wrong. Let's try again \n")
        main()

    numberAlt = str(input("How many alternatives do you want to enter? Type an integer: "))
    if numberAlt.isdigit(): # error handling
        leftTable = np.zeros([int(numberAlt),int(numberCrit)])
        print(leftTable)
        for i in range(0, int(numberCrit)):
            print(f'table  {i+1}' )
            A = matrix(number= int(numberAlt), matrType='alternative', criterionNumber= i+1)
            print(A)
            leftTable[:, i] = vector(A)
        print()
        print("Table of indicators of selected alternatives:")
        print(leftTable)
    else:
        print("Something went wrong. Let's try again \n")
        main()
    
    result = np.matmul(leftTable, weights)
    print()
    print(result)
    print()
    for i in range(len(result)):
            print(f'Alternative {i+1} = {np.round(result[i], 2)}')
            """


if __name__ == "__main__":
    main()