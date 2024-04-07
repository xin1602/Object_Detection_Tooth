# libraries
import cv2
import numpy as np
import os

# Define the folder paths
# input_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v3\\origin\\apical lesion"
# output_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v3\\final\\apical lesion"

# input_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v3\\origin\\peri endo"
# output_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v3\\final\\peri endo"

input_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v3\\origin\\normal"
output_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v3\\final\\normal"

# Ensure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Define the Gaussian filter parameters
D0 = 20

# Process each image in the input folder
for filename in os.listdir(input_folder):
    # Read the image
    f = cv2.imread(os.path.join(input_folder, filename), cv2.IMREAD_GRAYSCALE)
    
    # Transform the image into frequency domain
    F = np.fft.fft2(f)
    Fshift = np.fft.fftshift(F)

    # Create Gaussian Filter: High Pass Filter
    M, N = f.shape
    H = np.zeros((M, N), dtype=np.float32)
    for u in range(M):
        for v in range(N):
            D = np.sqrt((u - M / 2) ** 2 + (v - N / 2) ** 2)
            H[u, v] = 1 - np.exp(-D ** 2 / (2 * D0 * D0))

    # Apply the filter
    Gshift = Fshift * H
    G = np.fft.ifftshift(Gshift)
    g = np.abs(np.fft.ifft2(G))

    # Convert to uint8
    g = g.astype(np.uint8)
    
    # Convert the processed grayscale image to RGB
    g_rgb = cv2.cvtColor(g, cv2.COLOR_GRAY2RGB)
    
    # Compute the difference image
    result = cv2.subtract(f, g)

    # Convert the processed grayscale image to RGB
    result_rgb = cv2.cvtColor(result, cv2.COLOR_GRAY2RGB)

    # Save the processed image
    output_path = os.path.join(output_folder, filename)
    cv2.imwrite(output_path, result_rgb)

    print(f'Processed: {filename}')

print('All images processed successfully.')
