# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# image_path='/Users/tzuuu/Documents/112-2 三下/大專生研究計畫/根尖合併牙周病灶/test_image/2_8.jpg'
# image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


# # 閉運算
# kernel=np.ones((2, 2),np.uint8)
# mask3 = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel, iterations=4)

# # 開運算
# # kernel=np.ones((2, 2), np.uint8)
# # mask2 = cv2.morphologyEx(mask3, cv2.MORPH_OPEN, kernel, iterations=2)
# # mask2 = cv2.morphologyEx(mask2, cv2.MORPH_OPEN, kernel, iterations=1)


# # 原始影像和直方圖
# plt.figure(figsize=(10, 8))  
# plt.subplot(3, 1)
# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# plt.title('Original Image')

# # 自適應直方圖均衡化後的影像和直方圖
# plt.subplot(3, 2)
# plt.imshow(mask2, cmap='gray')
# plt.title('2+open')

# plt.subplot(3, 3)
# plt.imshow(mask3, cmap='gray')
# plt.title('2+close')

# plt.show()

# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# import os

# def equalize_and_save(image_path, output_folder):
#     # 讀取原始影像
#     img = cv2.imread(image_path)

#     if img is None:
#         print(f"Error: Unable to read the image {image_path}")
#         return

#     kernel=np.ones((2, 2),np.uint8)
#     # mask = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=4)
#     # mask = cv2.dilate(img,kernel,iterations = 20)
#     mask = cv2.erode(img,kernel,iterations = 10)

#     # 將 equalized_img 存儲在指定的輸出資料夾中
#     filename = os.path.basename(image_path)
#     result_path = os.path.join(output_folder, filename)
#     cv2.imwrite(result_path, mask)

#     print(f"Processed: {filename}")

# # 資料夾路徑
# # input_folder = 'E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_GH_d2.5\\valid\\apical lesion'
# # output_folder = 'E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_GH_d2.5_CEO\\valid\\apical lesion'
# input_folder = 'E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_GH_d2.5\\valid\\normal'
# output_folder = 'E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_GH_d2.5_CEO\\valid\\normal'

# # 確保輸出資料夾存在
# os.makedirs(output_folder, exist_ok=True)

# # 處理資料夾中的所有圖片
# for filename in os.listdir(input_folder):
#     if filename.endswith(".jpg"):
#         image_path = os.path.join(input_folder, filename)
#         equalize_and_save(image_path, output_folder)


import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def equalize_and_save(image_path, output_folder):
    # 讀取原始影像
    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Unable to read the image {image_path}")
        return

    kernel=np.ones((2, 2),np.uint8)
    # mask = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=4)
    # mask = cv2.dilate(img,kernel,iterations = 20)
    mask = cv2.erode(img,kernel,iterations = 10)

    # 將處理後的影像存儲在指定的輸出資料夾中
    filename = os.path.basename(image_path)
    result_path = os.path.join(output_folder, filename)
    cv2.imwrite(result_path, mask)

    print(f"Processed: {filename}")

def process_folder(folder_path, output_folder):
    # 確保輸出資料夾存在
    os.makedirs(output_folder, exist_ok=True)

    # 處理資料夾中的所有檔案和子資料夾
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            # 如果是資料夾，遞歸處理子資料夾
            process_folder(item_path, os.path.join(output_folder, item))
        elif item.endswith(".jpg"):
            # 如果是圖片檔案，進行處理並保存結果
            equalize_and_save(item_path, output_folder)

# 資料夾路徑
input_folder = 'E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_GH_d2.5'
output_folder = 'E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_GH_d2.5_CEO'

# 遞歸處理資料夾中的所有圖片
process_folder(input_folder, output_folder)
