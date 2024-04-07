import os
import cv2

def process_images(folder_path, output_folder):
    # 確保輸出資料夾存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 處理輸入資料夾中的每張圖片
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isdir(file_path):  # 檢查是否為資料夾
            # 遞歸處理子資料夾中的圖片
            subfolder_output = os.path.join(output_folder, filename)
            process_images(file_path, subfolder_output)
        elif filename.endswith(".jpg"):
            # 讀取圖片
            original_image = cv2.imread(file_path)

            # 轉換成灰階圖像
            gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

            # 轉換成彩色圖像 (3通道)
            color_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)

            # 計算原始圖片的寬高比例
            aspect_ratio = original_image.shape[1] / original_image.shape[0]

            # 設定目標高度為224，計算目標寬度並調整圖片大小
            target_height = 224
            target_width = int(aspect_ratio * target_height)
            resized_image = cv2.resize(color_image, (target_width, target_height))

            # 計算填充黑色的寬度和高度
            padding_width = (224 - resized_image.shape[1]) // 2
            padding_height = (224 - resized_image.shape[0]) // 2

            # 進行黑色填充
            resized_image_padded = cv2.copyMakeBorder(resized_image, padding_height, padding_height,
                                                      padding_width, padding_width, cv2.BORDER_CONSTANT, value=(0, 0, 0))

            # 保存處理後的圖片
            cv2.imwrite(os.path.join(output_folder, filename), resized_image_padded)

            # 資料增強：水平翻轉
            flipped_horizontal = cv2.flip(resized_image_padded, 1)
            cv2.imwrite(os.path.join(output_folder, filename.replace('.jpg', '_flipped_horizontal.jpg')), flipped_horizontal)

            # 資料增強：垂直翻轉
            flipped_vertical = cv2.flip(resized_image_padded, 0)
            cv2.imwrite(os.path.join(output_folder, filename.replace('.jpg', '_flipped_vertical.jpg')), flipped_vertical)

            # 資料增強：水平和垂直翻轉
            flipped_both = cv2.flip(flipped_horizontal, 0)
            cv2.imwrite(os.path.join(output_folder, filename.replace('.jpg', '_flipped_both.jpg')), flipped_both)

            # 資料增強：逆時針旋轉90度
            rotated_90 = cv2.rotate(resized_image_padded, cv2.ROTATE_90_CLOCKWISE)
            cv2.imwrite(os.path.join(output_folder, filename.replace('.jpg', '_rotated_90.jpg')), rotated_90)

            # 資料增強：逆時針旋轉270度
            rotated_270 = cv2.rotate(resized_image_padded, cv2.ROTATE_90_COUNTERCLOCKWISE)
            cv2.imwrite(os.path.join(output_folder, filename.replace('.jpg', '_rotated_270.jpg')), rotated_270)

    print(f'已完成圖片處理，保存至資料夾: {output_folder}')

# 設定原始資料夾和輸出資料夾的路徑
original_folder = "F:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_crop_x20_y40"
output_folder = "F:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_crop_x20_y40_padding_enhanced.4_test"

# 遞歸處理圖片
process_images(original_folder, output_folder)
