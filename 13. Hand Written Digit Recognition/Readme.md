## Hand Written Digit:
![aws bootstrap](digit.png 'Hand Written Digit')  

## Detected Output:
![aws bootstrap](output.png 'Detected Hand Written Digit')  

## How Code Works:

The training code uses PyTorch to build and train a simple fully connected neural network on the MNIST dataset, which contains 28×28 grayscale images of handwritten digits (0–9). The model consists of an input layer flattened from the 28×28 image, a hidden layer with 128 neurons and ReLU activation, and an output layer with 10 neurons representing digit classes. It is trained using the Adam optimizer and cross-entropy loss for five epochs. After training, the model’s accuracy is evaluated on a separate test set, and the trained weights are saved to a file named mnist_model.pth.

To test the model with a custom image of a handwritten digit (e.g., digit 6), the image is first preprocessed using OpenCV by converting it to grayscale, inverting colors, resizing it to 28×28, padding it to maintain MNIST-style dimensions, and normalizing pixel values. This processed image is then converted into a PyTorch tensor and passed to the previously trained and loaded model. The model outputs a prediction, and the class with the highest probability (e.g., “6”) is returned as the detected digit.