import os
import shutil

#我要去A資料夾中讀取所有.jpg的檔名，再去B資料夾找到[A資料夾所有.jpg的檔名]的檔案，複製一份到C資料夾

def copy_files(source_folder, target_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # List files in target folder for debugging
    print("Files in target folder B:")
    for root, dirs, files in os.walk(target_folder):
        for file in files:
            print(os.path.relpath(os.path.join(root, file), target_folder))

    # Recursively copy files from source folder to output folder while maintaining structure
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            source_path = os.path.join(root, file)
            relative_path = os.path.relpath(source_path, source_folder)
            target_path = os.path.join(target_folder, os.path.basename(relative_path))
            output_path = os.path.join(output_folder, relative_path)

            # Check if file exists in target folder
            if os.path.exists(target_path):
                # Copy file from target folder to output folder with same structure
                target_dir = os.path.dirname(output_path)
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)
                shutil.copyfile(target_path, output_path)
                print(f"Copied file from B: {relative_path}")
            else:
                print(f"File not found in B folder: {relative_path}")
                print(f"Source path: {source_path}")
                print(f"Target path: {target_path}")

def main():
    # 原始資料夾 A
    folder_a = "F:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_test"

    # 目標資料夾 B
    folder_b = "F:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\cropped_images_x20_y0"

    # 目標資料夾 C
    folder_c = "F:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_crop_x20_y0_test"

    # Copy files while maintaining folder structure from B to C
    copy_files(folder_a, folder_b, folder_c)
    print("All images copied successfully.")

if __name__ == "__main__":
    main()



