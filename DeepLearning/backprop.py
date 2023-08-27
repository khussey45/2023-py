import torch

# Set the random seed for reproducibility
torch.manual_seed(0)

# Inputs and target outputs
inputs = torch.tensor([[1.0, 2.0]], dtype=torch.float32)
target = torch.tensor([[2.0]], dtype=torch.float32)

# Initialize weights and biases
weights1 = torch.randn(2, 2, requires_grad=True)
bias1 = torch.randn(1, 2, requires_grad=True)
weights2 = torch.randn(2, 1, requires_grad=True)
bias2 = torch.randn(1, 1, requires_grad=True)

# Learning rate
learning_rate = 0.01

# Training loop
for i in range(100):
    # Forward pass
    hidden = torch.mm(inputs, weights1) + bias1
    output = torch.mm(hidden, weights2) + bias2
    
    # Compute loss
    loss = torch.mean((output - target)**2)
    
    # Backward pass (compute gradients)
    loss.backward()
    
    # Update weights and biases
    with torch.no_grad():
        weights1 -= learning_rate * weights1.grad
        bias1 -= learning_rate * bias1.grad
        weights2 -= learning_rate * weights2.grad
        bias2 -= learning_rate * bias2.grad
    
    # Zero the gradients
    weights1.grad.zero_()
    bias1.grad.zero_()
    weights2.grad.zero_()
    bias2.grad.zero_()
    
    # Print the loss
    if (i+1) % 10 == 0:
        print(f'Epoch [{i+1}/100], Loss: {loss.item():.4f}')

# Print the final output
print(f'Final Output: {output.detach().numpy()}')
