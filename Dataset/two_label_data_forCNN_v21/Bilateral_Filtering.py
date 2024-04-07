import cv2 
import matplotlib.pyplot as plt

import os
import cv2

# 文件夾路徑
# folder_path = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v21\\final\\apical lesion"
# output_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v21\\final_BF_15_10_10\\apical lesion"

# folder_path = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v21\\final\\peri endo"
# output_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v21\\final_BF_15_10_10\\peri endo"

folder_path = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v21\\final\\normal"
output_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v21\\final_BF_15_10_10\\normal"

# 文件夾路徑
# folder_path = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v21\\test\\apical lesion"
# output_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v21\\test_AHE_c8_t8-8\\apical lesion"

# folder_path = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v21\\test\\peri endo"
# output_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v21\\test_AHE_c8_t8-8\\peri endo"

# folder_path = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v21\\test\\normal"
# output_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v21\\test_AHE_c8_t8-8\\normal"

# cv2.bilateralFilter(圖片, d, sigmaColor, sigmaSpace)
# d：濾波器的窗口大小
# sigmaColor：越小，濾波器對色彩變化的敏感度越低，類似色彩的像素會被視為同一區域，進而減少色彩噪點
# sigmaSpace：越小，濾波器對空間變化的敏感度越低，空間上較近的像素會被視為同一區域，進而減少空間噪點


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

        # 將影像轉換為雙邊濾波
        bilateral = cv2.bilateralFilter(gray_img, 15, 15, 15) 


        # 將灰度圖像轉換為彩色圖像
        color_img = cv2.cvtColor(bilateral, cv2.COLOR_GRAY2BGR)


        # 保存直方图均衡化后的图像到输出文件夹
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, color_img)

