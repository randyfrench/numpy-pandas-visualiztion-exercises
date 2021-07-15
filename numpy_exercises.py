import numpy as np
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
a
array([ 4, 10, 12, 23, -2, -1,  0,  0,  0, -6,  3, -7])

# 1. How many negative numbers are there? 4
a[a < 0].size
4

# 2. How many positive numbers are there? 6
a[a > 0].size
5

# 3. How many even positive numbers are there? 3
a[(a % 2 == 0) & (a > 0)].size
3

# 4. If you were to add 3 to each data point, how many positive numbers would there be? 4
a + 3
array([ 7, 13, 15, 26,  1,  2,  3,  3,  3, -3,  6, 10])
b = np.array([7, 13, 15, 26,  1,  2,  3,  3,  3, -3,  6, 10])
b
d = b[(b % 2 == 0) & (b > 0)]
d
array([26,  2,  6, 10])

# 5. If you squared each number, what would the new mean and standard deviation be?
b ** 2
array([ 49, 169, 225, 676,   1,   4,   9,   9,   9,   9,  36, 100])
