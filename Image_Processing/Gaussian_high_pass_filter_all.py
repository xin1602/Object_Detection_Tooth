import cv2
import numpy as np
import os

def process_images_recursively(folder_path, output_folder, D0=4):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each item in the folder
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path) and item_path.endswith(".jpg"):
            # Read the image
            f = cv2.imread(item_path, cv2.IMREAD_GRAYSCALE)

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
            output_path = os.path.join(output_folder, item)
            cv2.imwrite(output_path, result_rgb)

            print(f'Processed: {item}')

        elif os.path.isdir(item_path):
            # Recursively process images in subfolder
            sub_output_folder = os.path.join(output_folder, item)
            process_images_recursively(item_path, sub_output_folder)

    print(f'Finished processing folder: {folder_path}')

# 文件夾路径
base_folder = "F:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin"
output_base_folder = "F:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_0405test"

# 处理图像（包括子文件夹）
process_images_recursively(base_folder, output_base_folder)
