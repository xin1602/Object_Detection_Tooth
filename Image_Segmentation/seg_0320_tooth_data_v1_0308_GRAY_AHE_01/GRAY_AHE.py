import os
import cv2

# 文件夾路徑
folder_path = "E:\\Lab\share\\YOLO_segmentation\\seg_0320_tooth_data_v1_0308_GRAY_AHE_01\\images"
output_folder = "E:\\Lab\share\\YOLO_segmentation\\seg_0320_tooth_data_v1_0308_GRAY_AHE_01\\GRAY_AHE"


# 如果输出文件夹不存在，则创建
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 讀取資料夾下的所有檔案
for filename in os.listdir(folder_path):
    if filename.endswith(".jpg"):
        # 讀取原始影像
        img = cv2.imread(os.path.join(folder_path, filename))

        # 將影像轉換為灰度
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 使用自適應直方圖均衡化處理影像
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        adaptive_equalized_img = clahe.apply(gray_img)

        # 將影像轉換為彩色（BGR）
        adaptive_equalized_img = cv2.cvtColor(adaptive_equalized_img, cv2.COLOR_GRAY2BGR)

        # 保存直方图均衡化后的图像到输出文件夹
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, adaptive_equalized_img)
