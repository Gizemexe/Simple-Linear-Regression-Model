## Simple Regression
#     Make sure you add the bias feature to each training and test example.
#     Standardize the features using the mean and std computed over training data.

import sys
import numpy as np
from matplotlib import pyplot as plt
import scaling


# Read data matrix X and labels y from text file.
def read_data(file_name):
  data = np.loadtxt(file_name)
  X = data[:, :-1]
  y = data[:, -1]

  return X, y


# Implement gradient descent algorithm to compute w = [w0, w1].
def train(X, y, lamda, epochs):
  cost_past = []
  w = np.zeros(X.shape[1])

  for epoch in range(epochs):
      grad = compute_gradient(X, y, w)
      w = w - lamda * grad
      cost = compute_cost(X, y, w)
      cost_past.append(cost)

  return w, cost_past


# Compute Root mean squared error (RMSE)).
def compute_rmse(X, y, w):
  predictions = X @ w
  rmse = np.sqrt(np.mean((predictions-y)**2))
  return rmse


# Compute objective (cost) function.
def compute_cost(X, y, w):
  m = len(y)
  predictions = X @ w
  cost = (1/(2*m)) * np.sum((predictions - y)**2)

  return cost


# Compute gradient descent Algorithm.
def compute_gradient(X, y, w):
  grad = np.zeros(w.shape)

  m = len(y)
  predictions = X @ w
  error = predictions - y

  for i in range(len(w)):
    grad[i] = (1/m)*np.sum(error * X[:, i])
  return grad



##======================= Main program =======================##

# Read the training and test data.
Xtrain, ttrain = read_data("train.txt")
Xtest, ttest = read_data("test.txt")


# Bias özelliğinin eklendiği kısım.
Xtrain = np.column_stack((np.ones((Xtrain.shape[0], 1)), Xtrain))
Xtest = np.column_stack((np.ones((Xtest.shape[0], 1)), Xtest))

mean, std = scaling.mean_std(Xtrain[:, 1:])

#Standardize the features
Xtrain[:, 1:] = scaling.standardize(Xtrain[:, 1:], mean, std)
Xtest[:, 1:] = scaling.standardize(Xtest[:, 1:], mean, std)


# Modeli eğit
lamda = 0.1 #learning rate
epochs = 500
w, cost_past = train(Xtrain, ttrain, lamda, epochs)

# Eğitim ve test setlerinde RMSE hesapla
train_rmse = compute_rmse(Xtrain, ttrain, w)
test_rmse = compute_rmse(Xtest, ttest, w)
print("Train RMSE:", train_rmse)
print("Test RMSE:", test_rmse)

# Maliyet fonksiyonunu çiz
plt.plot(range(epochs), cost_past)
plt.xlabel("Epoch")
plt.ylabel("Cost J(w)")
plt.title("Cost Function")
plt.show()


# Eğitim ve test verilerini çiz
plt.scatter(Xtrain[:, 1], ttrain, color="blue", label="Training Data")
plt.scatter(Xtest[:, 1], ttest, color="green", marker="x", label="Test Data")
plt.plot(Xtrain[:, 1], Xtrain @ w, color="red", label="Linear Solution")
plt.xlabel("Floor Size")
plt.ylabel("House Prices")
plt.title("House Prices - Floor Size ")
plt.legend()
plt.show()