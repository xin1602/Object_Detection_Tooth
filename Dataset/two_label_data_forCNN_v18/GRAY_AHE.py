import os
import cv2

# 文件夾路徑
folder_path = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v18\\final\\apical lesion"
output_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v18\\ffinal_AHE_c8_t8-8\\apical lesion"

# folder_path = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v18\\final\\peri endo"
# output_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v18\\final_AHE_c8_t8-8\\peri endo"

# folder_path = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v18\\final\\normal"
# output_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v18\\final_AHE_c8_t8-8\\normal"

# 文件夾路徑
# folder_path = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v18\\test\\apical lesion"
# output_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v18\\test_AHE_c8_t8-8\\apical lesion"

# folder_path = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v18\\test\\peri endo"
# output_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v18\\test_AHE_c8_t8-8\\peri endo"

# folder_path = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v18\\test\\normal"
# output_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v18\\test_AHE_c8_t8-8\\normal"


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
        clahe = cv2.createCLAHE(clipLimit=8.0, tileGridSize=(8, 8))
        adaptive_equalized_img = clahe.apply(gray_img)


        # 將灰度圖像轉換為彩色圖像
        color_img = cv2.cvtColor(adaptive_equalized_img, cv2.COLOR_GRAY2BGR)


        # 保存直方图均衡化后的图像到输出文件夹
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, color_img)
