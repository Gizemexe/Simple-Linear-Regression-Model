import numpy as np

# Compute the sample mean and standard deviations for each feature (column)
# across the training examples (rows) from the data matrix X.
def mean_std(X):
  mean = np.zeros(X.shape[1])
  std = np.ones(X.shape[1])

  for i in range(X.shape[1]):
    mean[i] = np.mean(X[:, i])
    std[i] = np.std(X[:, i])

  return mean, std


# Standardize the features of the examples in X by subtracting their mean and 
# dividing by their standard deviation, as provided in the parameters.
def standardize(X, mean, std):
  S = np.zeros(X.shape)

  for i in range(X.shape[1]):
    S[:, i] = (X[:, i] - mean[i]) / std[i]

  return S
