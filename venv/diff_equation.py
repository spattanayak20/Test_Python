import numpy as np
import scipy.linalg as la

def diffeq(pro):
    coeffArray = []
    powerArray = []

    print(pro)
    sep1 = pro.split("=")
    print(sep1)
    lhs = sep1[0].split(" + ")
    rhs = sep1[1].split(" + ")
    print(lhs)
    print(rhs)

    for i in lhs:
        lcoef = i.split("F")
        print(lcoef)
        if lcoef[0] != ' ':
            coeffArray.append(lcoef[0].strip())
        else:
            coeffArray.append('0')
        powerArray.append(lcoef[1].strip().split("+")[1].split(")")[0])
        print(coeffArray)
        print(powerArray)

    for rhsvar in rhs:
        rhsCoef = rhsvar.split("F")
        # print(rhsCoef)
        if rhsCoef[0] != '':
            coeffArray.append(rhsCoef[0].strip())
        else:
            coeffArray.append('0')
        if (rhsCoef[1] != '(K)'):
            powerArray.append(rhsCoef[1].strip().split("+")[1].split(")")[0])
        else:
            powerArray.append('0')
    print(coeffArray)
    print(powerArray)

    coeffArray = [int(i) for i in coeffArray]
    powerArray = [int(i) for i in powerArray]
    coeffArray = [x for i,x in sorted(zip(powerArray, coeffArray))]
    print(coeffArray)
    print(powerArray)

    highestCoeff = coeffArray[0]
    newList = [x / highestCoeff for x in coeffArray[1:]]
    lastrow = np.array(newList)
    print(lastrow)

    b = np.identity(len(powerArray) - 1)
    b = np.roll(b, 1)
    b[0][0] = 0
    print(b)

    b[lastrow.size-1:]= lastrow[:]
    print("Matrix")
    print(b)

    eigvals, eigvecs = la.eig(b)
    eigvals = eigvals.real
    print("eigvals")
    print(eigvals)
    for x in eigvals:
        if x > 1 or x < -1:
            return False
    else:
        return True



if __name__== "__main__":
    input = "2F(K+2)=3F(K+2) + 4F(K+1) + 2F(K)"
    print(diffeq(input))
