import numpy as np

# Inputs
inputs = np.array([1, 2, 3, 4])

# Weights and biases for the first layer
weights1 = np.array([[0.2, 0.8, -0.5, 1.0],
                     [0.5, -0.91, 0.26, -0.5],
                     [-0.26, -0.27, 0.17, 0.87],
                     [0.1, -0.14, 0.5, -0.2],
                     [0.1, 0.3, -0.2, 0.5]])
bias1 = np.array([2, 3, 0.5, 1.0, -1.5])

# Weights and biases for the second layer
weights2 = np.array([[0.1, -0.14, 0.5, -0.2, 0.5],
                     [-0.1, 0.5, -0.2, 0.5, 0.3],
                     [0.2, -0.3, 0.2, -0.5, 0.5]])
bias2 = np.array([1, 2, -0.5])

# Weights and biases for the third layer
weights3 = np.array([[0.3, -0.2, 0.6],
                     [-0.2, 0.5, -0.4]])
bias3 = np.array([1, -1])

# Outputs for the first layer
layer1_outputs = np.dot(weights1, inputs) + bias1

# Outputs for the second layer
layer2_outputs = np.dot(weights2, layer1_outputs) + bias2

# Outputs for the third layer
layer3_outputs = np.dot(weights3, layer2_outputs) + bias3

print(layer3_outputs)
