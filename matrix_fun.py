import numpy as np
import scipy.linalg as li


def matrix_multi(m1, m2):
    mul_result = np.dot(m1, m2)
    return mul_result


def matrix_trans(cal):
    return np.transpose(cal)


def matrix_inv(cal):
    return np.linalg.inv(cal)


def gaussian_elm(cal):
    return np.triu(cal)


def matrix_eigenvalues(cal):
    return li.eig(cal)


def rotation_matrix(deg, cal):
    theta = np.radians(deg)
    cos_theta, sin_theta = np.cos(theta), np.sin(theta)
    rot_array = np.array(((cos_theta, -sin_theta), (sin_theta, cos_theta)))
    return np.dot(cal, rot_array)


def matrix_diagonalize(cal):
    eigvals, eigvecs = matrix_eigenvalues(cal)
    eigvals = eigvals.real
    d = np.diag(eigvals)
    return eigvecs, d, matrix_inv(eigvecs)


def matrix_power(cal, n):
    eigvecs, eigvals, eig_inv = matrix_diagonalize(cal)
    eigvals_power = np.power(eigvals, n)
    return eigvecs @ eigvals_power @ matrix_inv(eigvecs)


if __name__ == "__main__":

    a1 = int(input("Enter the No of column for the matrix1: "))
    b1 = int(input('Enter the No of row for the matrix1: '))

    mat1 = []
    for i in range(0, a1):
        for j in range(0, b1):
            x1 = int(input("Element:"))
            mat1.append(x1)

    my_matrix1 = np.reshape(np.array(mat1), (a1, b1))
    print(np.floor(my_matrix1))

    a2 = int(input("Enter the No of column for the matrix2: "))
    b2 = int(input("Enter the No of row for the matrix2: "))

    mat2 = []
    for i in range(0, a2):
        for j in range(0, b2):
            x2 = int(input("Element:"))
            mat2.append(x2)

    my_matrix2 = np.reshape(np.array(mat2), (a2, b2))
    print(np.floor(my_matrix2))

print(matrix_multi(my_matrix1, my_matrix2))
print(rotation_matrix(30, my_matrix1))
print(matrix_diagonalize(my_matrix1))
