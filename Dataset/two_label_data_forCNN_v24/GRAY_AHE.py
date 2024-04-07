import os
import cv2

# 文件夾路徑
# folder_path = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_crop_x20_y40_padding_enhanced.4_GH_d4\\train\\apical lesion"
# output_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_crop_x20_y40_padding_enhanced.4_GH_d4_AHE_c4_t4-4\\train\\apical lesion"

# folder_path = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_crop_x20_y40_padding_enhanced.4_GH_d4\\train\\peri endo"
# output_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_crop_x20_y40_padding_enhanced.4_GH_d4_AHE_c4_t4-4\\train\\peri endo"

# folder_path = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_crop_x20_y40_padding_enhanced.4_GH_d4\\train\\normal"
# output_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_crop_x20_y40_padding_enhanced.4_GH_d4_AHE_c4_t4-4\\train\\normal"

# folder_path = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_crop_x20_y40_padding_enhanced.4_GH_d4\\valid\\apical lesion"
# output_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_crop_x20_y40_padding_enhanced.4_GH_d4_AHE_c4_t4-4\\valid\\apical lesion"

# folder_path = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_crop_x20_y40_padding_enhanced.4_GH_d4\\valid\\peri endo"
# output_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_crop_x20_y40_padding_enhanced.4_GH_d4_AHE_c4_t4-4\\valid\\peri endo"

# folder_path = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_crop_x20_y40_padding_enhanced.4_GH_d4\\valid\\normal"
# output_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_crop_x20_y40_padding_enhanced.4_GH_d4_AHE_c4_t4-4\\valid\\normal"

#########################
# folder_path = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_enhanced.4\\train\\apical lesion"
# output_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_enhanced.4_AHE_c4_t4-4\\train\\apical lesion"

# folder_path = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_enhanced.4\\train\\peri endo"
# output_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_enhanced.4_AHE_c4_t4-4\\train\\peri endo"

# folder_path = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_enhanced.4\\train\\normal"
# output_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_enhanced.4_AHE_c4_t4-4\\train\\normal"

# folder_path = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_enhanced.4\\valid\\apical lesion"
# output_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_enhanced.4_AHE_c4_t4-4\\valid\\apical lesion"

# folder_path = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_enhanced.4\\valid\\peri endo"
# output_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\origin_enhanced.4_AHE_c4_t4-4\\valid\\peri endo"

folder_path = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_enhanced.4\\valid\\normal"
output_folder = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_enhanced.4_AHE_c4_t4-4\\valid\\normal"


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
        # clahe = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(2, 2))
        clahe = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(4, 4))
        adaptive_equalized_img = clahe.apply(gray_img)


        # 將灰度圖像轉換為彩色圖像
        color_img = cv2.cvtColor(adaptive_equalized_img, cv2.COLOR_GRAY2BGR)


        # 保存直方图均衡化后的图像到输出文件夹
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, color_img)
