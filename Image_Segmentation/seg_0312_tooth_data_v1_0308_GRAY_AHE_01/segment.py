import cv2
import math
import numpy as np
from ultralytics import YOLO
from PIL import Image
import os

def resize_with_padding(image, target_size):
    h, w = image.shape[:2]
    target_h, target_w = target_size

    # 計算縮放比例
    scale = min(target_w / w, target_h / h)

    # 縮放圖片
    resized_image = cv2.resize(image, None, fx=scale, fy=scale)

    # 創建一個目標大小的黑色畫布
    padded_image = np.zeros((target_h, target_w, 3), dtype=np.uint8)

    # 計算圖片應該放置的位置
    y_offset = (target_h - int(h * scale)) // 2
    x_offset = (target_w - int(w * scale)) // 2

    # 將縮放後的圖片放入畫布的中心
    padded_image[y_offset:y_offset+resized_image.shape[0], x_offset:x_offset+resized_image.shape[1]] = resized_image

    return padded_image

# 初始化 YOLOv8 模型
model = YOLO("F:\\Lab\\share\\YOLO_segmentation\\seg_0312_tooth_data_v1_0308_GRAY_AHE_01\\train3\\weights\\best.pt")

# 處理整個資料夾中的圖像
folder_path = "F:\\Lab\\share\\dataset\\two_label_data_combine\\GRAY_AHE"
for filename in os.listdir(folder_path):
    if filename.endswith(".jpg"):
        image_path = os.path.join(folder_path, filename)
        # 讀取圖片
        image = cv2.imread(image_path)

        # 調整大小至 640x640，不變形
        resized_image = resize_with_padding(image, (640, 640))

        # 執行預測
        results = model(resized_image)

        # 獲取第一個結果
        result = results[0]

        # 獲取 OBB 信息
        obb_info = result.obb

        # 對每個邊界框進行處理
        sorted_indices = sorted(range(len(obb_info.xyxyxyxy)), key=lambda i: obb_info.xyxyxyxy[i][0][0].item())  # 根據 orbit_center_x 排序的索引列表
        for i, idx in enumerate(sorted_indices):
            # 獲取邊界框的四個角點座標
            pts = obb_info.xyxyxyxy[idx].numpy().reshape(-1, 2).astype(np.int32)
            # 計算邊界框的中心點座標
            center_x = int((pts[0][0] + pts[2][0]) / 2)
            center_y = int((pts[0][1] + pts[2][1]) / 2)
            # 計算邊界框的寬和高
            width = int(math.sqrt((pts[1][0] - pts[0][0])**2 + (pts[1][1] - pts[0][1])**2))
            height = int(math.sqrt((pts[2][0] - pts[1][0])**2 + (pts[2][1] - pts[1][1])**2))
            # 計算旋轉角度
            angle = math.atan2(pts[1][1] - pts[0][1], pts[1][0] - pts[0][0]) * 180 / math.pi
            # 獲取旋轉矩形的四個角點
            rect = ((center_x, center_y), (width, height), angle)
            box = cv2.boxPoints(rect)
            # 將角點轉換為整數類型
            box = np.int0(box)
            # 繪製遮罩
            mask = np.zeros(resized_image.shape[:2], dtype=np.uint8)
            cv2.drawContours(mask, [box], 0, (255), -1)
            # 裁剪圖像
            masked_image = cv2.bitwise_and(resized_image, resized_image, mask=mask)
            # 保存遮罩圖像，使用原始圖片的檔名加上排序索引 i
            original_filename = os.path.splitext(os.path.basename(image_path))[0]
            output_folder = 'F:\\Lab\\share\\YOLO_segmentation\\seg_0312_tooth_data_v1_0308_GRAY_AHE_01\\mask_images'
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            cv2.imwrite(os.path.join(output_folder, f'{original_filename}_{i}.jpg'), masked_image)

        # 保存預測結果
        output_folder = 'F:\\Lab\\share\\YOLO_segmentation\\seg_0312_tooth_data_v1_0308_GRAY_AHE_01\\predicts'
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        for r in results:
            im_array = r.plot()  # plot a BGR numpy array of predictions
            im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
            im.save(os.path.join(output_folder, f'{original_filename}.jpg'))  # save image
