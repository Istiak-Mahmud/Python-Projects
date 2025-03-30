## Original Image:
![aws bootstrap](Test.jpg 'Original')  

## Converted Image:
![aws bootstrap](converted.png 'Output')  

## How the RGB to Black and White Image Converter Code Works:

To run this image processing code, you first need to install OpenCV using Anaconda by opening the Anaconda Prompt and running the 'command conda install -c menpo opencv'. This installs the OpenCV library from the menpo channel, which is commonly used with Anaconda environments. Once installed, the code begins by importing the OpenCV library using import cv2. It then reads an image file named 'Test.jpg' in grayscale mode using the cv2.imread() function, where the second argument 0 specifies that the image should be loaded as grayscale. After reading the image, it is displayed in a window titled "Grayscale Image" using the cv2.imshow() function. The program then pauses and waits for the user to press any key with cv2.waitKey(0), ensuring that the image window doesn't close immediately. Once a key is pressed, all OpenCV windows are closed using cv2.destroyAllWindows(). This simple script demonstrates how to read, display, and handle basic grayscale images in Python using OpenCV.