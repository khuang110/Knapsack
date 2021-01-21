# Recursive solution for Knapsack problem
# By: Kyle Huang
#
#           { 0,                                         n <= 0
# F(n, W) = { F(n - 1, W),                               Wn > W
#           { max(F(n - 1, W), valn + F(n - 1, W - Wn)), Wn <= W
#


# Function to solve knapsack problem
def knapsack(W, wt, val, n):


# Driver function
if __name__=="__main__":
    val = [40, 50, 80]
    wt = [5, 10, 15]
    W = 20
    n = len(val)