import os
import cv2

# 文件夾路徑
# folder_path = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v11\\final\\normal"
# output_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v11\\final\\normal"
# folder_path = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v11\\final\\apical lesion"
# output_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v11\\final\\apical lesion"
# folder_path = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v11\\final\\peri endo"
# output_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v11\\final\\peri endo"

folder_path = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v11\\test\\normal"
output_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v11\\test\\normal"
# folder_path = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v11\\test\\apical lesion"
# output_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v11\\test\\apical lesion"
# folder_path = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v11\\test\\peri endo"
# output_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v11\\test\\peri endo"



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

        # 對灰度影像進行直方圖均衡化
        equalized_img = cv2.equalizeHist(gray_img)

        # 將影像轉換為彩色（BGR）
        equalized_img = cv2.cvtColor(equalized_img, cv2.COLOR_GRAY2BGR)

        # 保存直方图均衡化后的图像到输出文件夹
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, equalized_img)
