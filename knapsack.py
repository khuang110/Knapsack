# Recursive solution for Knapsack problem
# By: Kyle Huang
#
#            { 0,                                           n <= 0
# F(n, wt) = { F(n - 1, wt),                                wtn > W
#            { max(F(n - 1, wt), valn + F(n - 1, W - wtn)), wtn <= W
#
# O(2^n)


# Function to solve knapsack problem
def knapsack(W, wt, val, n):
    # Base case where val is empty.
    if n < 1:
        return 0

    # if item n is too big
    if wt[n - 1] > W:
        return knapsack(W, wt, val, n - 1)
    else:
        return max(knapsack(W, wt, val, n - 1),                             # Don't use item n
                   (val[n - 1] + knapsack(W - wt[n - 1], wt, val, n - 1)))  # use item n


# Driver function
if __name__=="__main__":
    val = [40, 50, 80]
    wt = [5, 10, 15]
    W = 20
    n = len(val)
    print(val)
    print(knapsack(W, wt, val, n))
