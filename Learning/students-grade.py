import numpy as np

# Suppose five students report hours studied (x) and a grade (y):
# Student i 1 2 3 4 5
# x (hours) 1 2 3 4 5
# y (grade) 2 4 5 4 5

# Defining the data
x = np.array([1,2,3,4,5]);
y = np.array([2,4,5,4,5]);

# Calculating the mean of x and y
x_mean, y_mean = np.mean(x), np.mean(y);

# Calculating the sume of squares --> Reasoning: S_xx = sum of squares of x, S_xy = sum of products of deviations of x and y
S_xx = np.sum((x - x_mean)**2);
S_xy = np.sum((x- x_mean)*(y - y_mean));
