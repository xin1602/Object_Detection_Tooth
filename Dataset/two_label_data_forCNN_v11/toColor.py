import os
import cv2

# 定義文件夾路徑
folder_path = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v11\\final\\normal"
output_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v11\\final\\normal"


# 如果輸出文件夾不存在，則創建
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 讀取資料夾下的所有檔案
for filename in os.listdir(folder_path):
    if filename.endswith(".jpg"):
        # 讀取原始影像
        img = cv2.imread(os.path.join(folder_path, filename))

        # 將影像轉換為彩色（BGR）
        color_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

        # 保存彩色影像到輸出文件夾
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, color_img)