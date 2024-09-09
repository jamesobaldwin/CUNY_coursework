# you should fill in the functions in this file,
# do NOT change the name, input and output of these functions

import numpy as np
import time
import matplotlib.pyplot as plt

# first function to fill, compute distance matrix using loops
def compute_distance_naive(X):
    N = X.shape[0]      # num of rows
#    print("N: ", N)
    D = X[0].shape[0]   # num of cols
#    print("Shape of X[0]: ", X[0].shape)
#    print("D: ", D)

    M = np.zeros([N,N])
    for i in range(N):
        for j in range(N):
            xi = X[i,:]
            xj = X[j,:]
            '''
            Euclidean Distance is defined by 
            || x_i - x_j || = square root of the sum of the square of the difference between all the points
            
            '''
            dist = np.sqrt(np.sum((xi - xj)**2))     # you have to change it to distance between xi and xj
            M[i,j] = dist

    return M

# second function to fill, compute distance matrix without loops
def compute_distance_smart(X):
    N = X.shape[0]  # num of rows
    D = X[0].shape[0]  # num of cols
    
    # use X to create M
    M = np.zeros([N, N]) 

    # compute the sum of squares for each row (i.e., ||x_i||^2 for all i)
    X_squared = np.sum(X**2, axis=1).reshape(-1, 1)  # Shape becomes (N, 1)
    
    # use Euclidean distance formula without loops
    # ||x_i - x_j||^2 = ||x_i||^2 + ||x_j||^2 - 2 * x_i * x_j
    M = X_squared + X_squared.T - ( 2 * np.dot( X, X.T ) )
    
    # take the square root to get the actual Euclidean distance
    M = np.sqrt(np.maximum(M,0))

    return M

# third function to fill, compute correlation matrix using loops
def compute_correlation_naive(X):
    N = X.shape[0]  # num of rows
    D = X[0].shape[0]  # num of cols

    # use X to create M
    M = np.zeros([D, D])

    # create a vector to store standard deviations 
    sigmas = np.zeros(D)

    for i in range(D):
        for j in range(D):
            xi = X[:, i]
            xj = X[:, j]
            
            # calulate the mean of the row vector x_i, calculated across N rows 
            mui = (1 / N) * np.sum(xi)
            muj = (1 / N) * np.sum(xj)
            # calculate s_ij 
            M[i][j] = (1 / (N - 1)) * np.sum((xi - mui) * (xj - muj)) 
            # store the standard deviations in a vector
            if i == j:
                sigmas[i] = np.sqrt( M[i][j] )

            M[i][j] /= (sigmas[i]*sigmas[j])
            # you have to change it to correlation between xi and xj
    return M

# fourth function to fill, compute correlation matrix without loops
def compute_correlation_smart(X):
    N = X.shape[0]  # num of rows
    D = X[0].shape[0]  # num of cols

    # use X to create M
    M = np.zeros([D, D])
    print("This is a test") 

    return M

def main():
    print('starting comparing distance computation .....')
    np.random.seed(100)
    params = range(10,141,10)   # different param setting
    nparams = len(params)       # number of different parameters

    perf_dist_loop = np.zeros([10,nparams])  # 10 trials = 10 rows, each parameter is a column
    perf_dist_cool = np.zeros([10,nparams])
    perf_corr_loop = np.zeros([10,nparams])  # 10 trials = 10 rows, each parameter is a column
    perf_corr_cool = np.zeros([10,nparams])

    counter = 0

    for ncols in params:
        nrows = ncols * 10

        print( "matrix dimensions: ", nrows, ncols )

        for i in range(10):
            X = np.random.rand(nrows, ncols)   # random matrix

            # compute distance matrices
            st = time.time()
            dist_loop = compute_distance_naive(X)
            et = time.time()
            perf_dist_loop[i,counter] = et - st              # time difference

            st = time.time()
            dist_cool = compute_distance_smart(X)
            et = time.time()
            perf_dist_cool[i,counter] = et - st

            assert np.allclose(dist_loop, dist_cool, atol=1e-06) # check if the two computed matrices are identical all the time

            # compute correlation matrices
            st = time.time()
            corr_loop = compute_correlation_naive(X)
            et = time.time()
            perf_corr_loop[i,counter] = et - st              # time difference
 
            st = time.time()
            corr_cool = compute_correlation_smart(X)
            et = time.time()
            perf_corr_cool[i,counter] = et - st
 
            assert np.allclose(corr_loop, corr_cool, atol=1e-06) # check if the two computed matrices are identical all the time
 
        counter = counter + 1
 
    mean_dist_loop = np.mean(perf_dist_loop, axis = 0)    # mean time for each parameter setting (over 10 trials)
    mean_dist_cool = np.mean(perf_dist_cool, axis = 0)
    std_dist_loop = np.std(perf_dist_loop, axis = 0)      # standard deviation
    std_dist_cool = np.std(perf_dist_cool, axis = 0)
 
    plt.figure(1)
    plt.errorbar(params, mean_dist_loop[0:nparams], yerr=std_dist_loop[0:nparams], color='red',label = 'Loop Solution for Distance Comp')
    plt.errorbar(params, mean_dist_cool[0:nparams], yerr=std_dist_cool[0:nparams], color='blue', label = 'Matrix Solution for Distance Comp')
    plt.xlabel('Number of Cols of the Matrix')
    plt.ylabel('Running Time (Seconds)')
    plt.title('Comparing Distance Computation Methods')
    plt.legend()
    plt.savefig('CompareDistanceCompFig.pdf')
    # plt.show()    # uncomment this if you want to see it right way
    print("result is written to CompareDistanceCompFig.pdf")
 
    mean_corr_loop = np.mean(perf_corr_loop, axis = 0)    # mean time for each parameter setting (over 10 trials)
    mean_corr_cool = np.mean(perf_corr_cool, axis = 0)
    std_corr_loop = np.std(perf_corr_loop, axis = 0)      # standard deviation
    std_corr_cool = np.std(perf_corr_cool, axis = 0)
 
    plt.figure(2)
    plt.errorbar(params, mean_corr_loop[0:nparams], yerr=std_corr_loop[0:nparams], color='red',label = 'Loop Solution for Correlation Comp')
    plt.errorbar(params, mean_corr_cool[0:nparams], yerr=std_corr_cool[0:nparams], color='blue', label = 'Matrix Solution for Correlation Comp')
    plt.xlabel('Number of Cols of the Matrix')
    plt.ylabel('Running Time (Seconds)')
    plt.title('Comparing Correlation Computation Methods')
    plt.legend()
    plt.savefig('CompareCorrelationCompFig.pdf')
    # plt.show()    # uncomment this if you want to see it right way
    print("result is written to CompareCorrelationCompFig.pdf")
 
if __name__ == "__main__": main()
