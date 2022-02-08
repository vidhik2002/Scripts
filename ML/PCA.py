import numpy as np
from numpy.linalg import eig
from tabulate import tabulate

print("Enter the number of rows:")
num_of_attrs = int(input())

print("Enter Space Seperated values for X1:")
X1 = np.array([float(x) for x in input().split(" ")])

print("Enter Space Seperated values for X2:")
X2 = np.array([float(x) for x in input().split(" ")])

X1_mean = np.mean(X1)
X2_mean = np.mean(X2)

print('\n')
print(f'Mean of X1: {X1_mean}')
print(f'Mean of X2: {X2_mean}')
print('\n')

X_1 = np.array([(x-X1_mean) for x in X1])
X_2 = np.array([(x-X2_mean) for x in X2])

ab = [num1*num2 for num1, num2 in zip(X_1,X_2)]
asq = [x**2 for x in X_1]
bsq = [x**2 for x in X_2]

print(tabulate({
    'X1': X1,
    'X2': X2,
    'X1-Mean(X1)': X_1,
    'X2-Mean(X2)': X_2,
    '(X1-Mean(X1))*(X2-Mean(X2))': ab,
    '(X1-Mean(X1))^2': asq,
    '(X2-Mean(X2))^2': bsq
}, headers="keys", tablefmt="github"))
print('\n')

print(f'Σ (X1-Mean(X1))*(X2-Mean(X2)): {np.sum(ab)}')
print(f'Σ (X1-Mean(X1))^2: {np.sum(asq)}')
print(f'Σ (X2-Mean(X2))^2: {np.sum(bsq)}')
print('\n')

def variance(arr,mean):
    return (np.sum([(x-mean)**2 for x in arr])/(len(arr)-1))

covariance = np.sum(ab)/(len(X1)-1)

covariance_matrix = np.array([[variance(X1,X1_mean),covariance],[covariance,variance(X2,X2_mean)]])

print(f'The covariance matrix is: {covariance_matrix}')

polynoimial = np.convolve([-1,covariance_matrix[0][0]],[-1,covariance_matrix[1][1]])

polynoimial[-1] = polynoimial[-1]-(covariance**2)

print(f'The eigen value polynomial is: {polynoimial[0]}x^2  {polynoimial[1]}x  {polynoimial[2]}')
print('\n')

w,_ = eig(covariance_matrix)

print(f'Eigen Values are: {w}')
print(f'Total Variance (λ1+λ2): {sum(w)}')
print(f'We have to select the maximum eigen value to find our eigen vector i.e, {max(w)}')
print('\n')

eigen_matrix = covariance_matrix - max(w)*np.identity(2)

print(f'A-λI = {eigen_matrix}')
print('\n')

eigen_vectors = [(eigen_matrix[0][1]/((-1)*eigen_matrix[0][0]))/(((eigen_matrix[0][1]/((-1)*eigen_matrix[0][0]))**2+1)**(1/2)), 1/(((eigen_matrix[0][1]/((-1)*eigen_matrix[0][0]))**2+1)**(1/2))]

print(f'The desired eigen vectors are: {eigen_vectors}')
print('\n')

principle_component = [(num1*eigen_vectors[0])+(num2*eigen_vectors[1]) for num1, num2 in zip(X1,X2)]
print(principle_component)