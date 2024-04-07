import cv2
import os

def process_images_recursive(folder_path, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each item in the folder
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path) and item_path.endswith(".jpg"):
            # Read the image
            img = cv2.imread(item_path)

            # Convert to grayscale
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Apply adaptive histogram equalization
            clahe = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(4, 4))
            adaptive_equalized_img = clahe.apply(gray_img)

            # Convert grayscale image to color image
            color_img = cv2.cvtColor(adaptive_equalized_img, cv2.COLOR_GRAY2BGR)

            # Save the processed image
            output_path = os.path.join(output_folder, item)
            cv2.imwrite(output_path, color_img)

            print(f'Processed: {item}')

        elif os.path.isdir(item_path):
            # Recursively process images in subfolder
            sub_output_folder = os.path.join(output_folder, item)
            process_images_recursive(item_path, sub_output_folder)

    print(f'Finished processing folder: {folder_path}')

# 文件夾路径
base_folder = "F:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin"
output_base_folder = "F:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_0405testAHE"

# 处理图像（包括子文件夹）
process_images_recursive(base_folder, output_base_folder)
