import numpy as np
from re import T
import view

def vector(matrix):
    matSum = np.zeros(len(matrix))
    for i in range(0, len(matrix)):
        vect = matrix[:, i]
        w = vect / vect.sum()
        for j in range(0, len(matrix)):
            matSum[j] += w[j] 
    matSum = matSum / len(matrix)
    return matSum

def matrix(number, matrType, criterionNumber=0):
    #Function for creating a pairwise matrix
    A = np.ones([number, number])
    importance = [i for i in range(1, 10)] # list of allowed importance values
    importance2 = [i/10 for i in range(1, 10)]
    value = importance + importance2
    for i in range(0, number):
        for j in range(0, number):
            if i < j:
                if criterionNumber > 0:
                    a = str(input(f'Compare importance of {matrType} {i+1} to {matrType} {j+1} in criterion {criterionNumber}:\n '))
                else:
                    a = str(input(f'How much {matrType} {i+1} is more important than {matrType} {j+1}? Type an integer from 0.1 to 9: '))
                if float(a) in value: # error handling
                    A[i,j] = float(a)
                    A[j, i] = 1 / float(a)
                else:
                    print("It is an incorrect value. Let's start again \n")
                    main()
    return consistencyCheck(A)

def consistencyCheck(initialMatrix, recursionNumber = 0): # function checks the consistency of the matrix
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
    """print(A)
    print('eigenvalue='+str(eigenvalue))
    print('featurevector='+str(featurevector))
    print('max(eigenvalue)='+str(max(eigenvalue)))
    print('len(A)='+str(len(A)))
    print('meanConsistensyIndex='+str(meanConsistencyIndex[len(A)]))"""
    consistensyIndex = (max(eigenvalue)-len(A))/(len(A)-1)
    print('consistensyIndex='+str(consistensyIndex))
    consistencyRelation = consistensyIndex/meanConsistencyIndex[len(A)]
    print('consistencyRelation='+str(consistencyRelation)+'\n')
    if (consistencyRelation <= 0.1):
        return (A)
    elif (recursionNumber < len(initialMatrix)):
        return (consistencyCheck(consistencyOptimization(A),recursionNumber+1))
    else:
        return (A)

def consistencyOptimization(initialMatrix): # function helps to get the correct consistency of the matrix
    A = initialMatrix 
    weights = vector(A)
    array_sum = [] 
    for i in range(len(A)): 
        array_sum.append(0) 
        for j in range(len(A)): 
            array_sum [i] += (A[i,j] - weights[i] / weights[j]) 

    print("\nchanged elements in string number " + str(np.argmax(np.absolute(array_sum))) + ": ")
    for j in range(len(A)): # for each element in the row, that is not correlated, we change aij to wi/wj
        print(str(A[np.argmax(np.absolute(array_sum)),j])+" element to: ")
        A[np.argmax(np.absolute(array_sum)),j] = weights[np.argmax(np.absolute(array_sum))]/weights[j]
        print(A[np.argmax(np.absolute(array_sum)),j])
    print ("\noptimized matrix is:\n"+str(A)+"\n")
    return (A)

def main(): 
    #A = np.array([[1,4,3,1,3,4],[1/4,1,7,3,1/5,1],[1/3,1/7,1,1/5,1/5,1/6],[1,1/3,5,1,1,1/3],[1/3,5,5,1,1,3],[1/4,1,6,3,1/3,1]])
    #numberCrit = len(A)
    
    
    numberCrit = str(input("How many criteria do you want to enter? Type an integer: "))
    if ((numberCrit.isdigit()) & (int(numberCrit) < 11)): # error handling
        A = matrix(number= int(numberCrit), matrType= 'criterion')
        print(A)
        weights = vector(A)
        for i in range(len(weights)):
            print(f'Criterion {i} = {np.round(weights[i], 2)}')
    else:
        print("You passed a wrong character. Let's try again \n")
        main()
    
    numberAlt = str(input("How many alternatives do you want to enter? Type an integer: "))
    if ((numberAlt.isdigit()) & (int(numberAlt) < 11)): # error handling
        leftTable = np.zeros([int(numberAlt),int(numberCrit)])
        print(leftTable)
        for i in range(int(numberCrit)):
            print(f'table  {i+1}' )
            A = matrix(number= int(numberAlt), matrType='alternative', criterionNumber=i+1)
            print(A)
            leftTable[:, i] = vector(A)

        print("\nTable of indicators of selected alternatives:")
        print(leftTable)
    else:
        print("You passed a wrong character. Let's try again \n")
        main()
    
    result = np.matmul(leftTable, weights)
    print('\n')
    print(result)
    print('\n')
    for i in range(len(result)):
            print(f'Alternative {i+1} = {np.round(result[i], 2)}')
    print('\nthe best alternative is ' + str(np.argmax(result)+1))
if __name__ == "__main__":
    main()