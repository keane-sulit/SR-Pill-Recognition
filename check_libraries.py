# Check if OpenCV and PyTorch are working

# Import libraries and print versions
try:
    import numpy as np
    import cv2
    print(f"OpenCV Version: {cv2.__version__}")
    # Perform a basic OpenCV operation: create a black image
    # Perform a basic OpenCV operation: create a black image of size 100x100 pixels
    black_image = np.zeros((1000, 1000, 3), np.uint8)
    cv2.imshow("Black Image", black_image)
    cv2.waitKey(0)  # Wait for a key press to close the window
    cv2.destroyAllWindows()
    print("OpenCV is working: Successfully created and displayed a black image.")
except ImportError:
    print("OpenCV is not installed.")
except Exception as e:
    print(f"An error occurred with OpenCV: {e}")

# Check PyTorch installation and functionality
try:
    import torch
    print(f"PyTorch Version: {torch.__version__}")
    # Perform a basic PyTorch operation: create a tensor
    tensor = torch.tensor([1, 2, 3])
    print(f"PyTorch is working: Created a tensor {tensor}")
except ImportError:
    print("PyTorch is not installed.")
except Exception as e:
    print(f"An error occurred with PyTorch: {e}")
