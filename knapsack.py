from time import perf_counter# sys time
from numpy import random # random num generator
import sys # cmd line args

# solution for Knapsack problem
# By: Kyle Huang

# Recursive function to solve knapsack problem
#
#            { 0,                                           n <= 0
# F(n, wt) = { F(n - 1, wt),                                wtn > W
#            { max(F(n - 1, wt), valn + F(n - 1, W - wtn)), wtn <= W
#
# O(2^n)
def knapsack_rec(w, wt, val, n):
    # Base case where val is empty.
    if n < 1:
        return 0

    # if item n is too big
    if wt[n - 1] > w:
        return knapsack_rec(w, wt, val, n - 1)
    else:
        return max(knapsack_rec(w, wt, val, n - 1),                             # Don't use item n
                   (val[n - 1] + knapsack_rec(w - wt[n - 1], wt, val, n - 1)))  # use item n


# Dynamic programming solution for knapsack problem
def knapsack_dp(k, wt, val, n):
    # Base case if not enough elements
    if n < 1 or k < 1:
        return

    w = max(wt)
    # init matrix for n elements X k
    v = [[0 for weight in range(k + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for weight in range(k + 1):
            if wt[i - 1] > weight:
                v[i][weight] = v[i - 1][weight]
            else:
                v[i][weight] = max(v[i - 1][weight], v[i - 1][weight - wt[i - 1]] + val[i - 1])
    return v[n][k]


# Driver function
def main(argv):
    # raise value to recurse further
    sys.setrecursionlimit(2000)

    arg = int(argv[0])
    itr = int(argv[1])
    w = int(argv[2])
    rec_time = []
    dp_time = []

    # print all all values given in cmd line args
    for n in range(arg, arg * itr + 1, arg):
        wt = random.randint(100, size=n)
        val = random.randint(100, size=n)

        t1_start = perf_counter()
        dp = knapsack_dp(w, wt, val, n)
        t1_stop = perf_counter()
        dp_time.append(t1_stop-t1_start)

        t2_start = perf_counter()
        rec = knapsack_rec(w, wt, val, n)
        t2_stop = perf_counter()
        rec_time.append(t2_stop-t2_start)
        print("N = %d   W = %d   Rec time = %f   DP time = %f    max Rec = %d   max DP = %d"
              % (n, w, (t2_stop - t2_start), (t1_stop - t1_start), rec, dp))




# knapsack.py <N items> <increment value> <W value>
if __name__=="__main__":
    main(sys.argv[1:])

