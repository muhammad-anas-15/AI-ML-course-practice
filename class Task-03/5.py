import numpy as np

# (a) Sigmoid Function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# (b) ReLU Function
def relu(x):
    return np.maximum(0, x)


# (c) Forward Pass
def forward_pass(weights, inputs, bias):
    z = np.dot(weights, inputs) + bias
    output = sigmoid(z)
    return output


# (d) Softmax Function
def softmax(x):
    exp_x = np.exp(x)
    return exp_x / np.sum(exp_x)


# (e) Mean Squared Error
def mse(predicted, actual):
    return np.mean((predicted - actual) ** 2)


# -------- Test Data --------

weights = np.array([
    [0.1, 0.2],
    [0.3, 0.4],
    [0.5, 0.6]
])

inputs = np.array([1.0, 0.5])
bias = np.array([0.1, 0.2, 0.3])


# -------- Testing --------

print("Sigmoid(0):", sigmoid(0))   # should be 0.5
print("ReLU(-3):", relu(-3))       # should be 0
print("ReLU(5):", relu(5))         # should be 5


# Forward Pass
output = forward_pass(weights, inputs, bias)
print("\nForward Pass Output:")
print(output)


# Softmax
softmax_output = softmax(output)
print("\nSoftmax Output:")
print(softmax_output)


# MSE Example
actual = np.array([0.2, 0.4, 0.6])
error = mse(output, actual)

print("\nMean Squared Error:", error)