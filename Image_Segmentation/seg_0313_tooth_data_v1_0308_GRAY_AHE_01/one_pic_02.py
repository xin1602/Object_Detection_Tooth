import cv2
from ultralytics import YOLO
import numpy as np
import math

# 讀取圖片
image_path = 'F:\\Lab\\share\\dataset\\two_label_data_combine\\GRAY_AHE\\088.jpg'
image = cv2.imread(image_path)

# 初始化 YOLOv8 模型
model = YOLO('F:\\Lab\\share\\YOLO_segmentation\\seg_0312_tooth_data_v1_0308_GRAY_AHE_01\\train3\\weights\\best.pt')


# 執行預測
results = model(image)

# # 提取預測結果中的旋轉矩形的信息
# obb_info = results.obb[0].cpu().numpy()  # 將 OBB 結果轉換為 NumPy 格式

# # 打印每個旋轉矩形的信息
# for obb in obb_info:
#     # 獲取旋轉矩形的坐標、角度和其他相關信息
#     x, y, w, h, angle, confidence, class_id = obb
#     class_name = model.names[int(class_id)]  # 獲取類別名稱

#     print(f"Bounding Box: ({x}, {y}), Width: {w}, Height: {h}, Angle: {angle}, Confidence: {confidence}, Class: {class_name}")

# # 獲取 xyxy 格式的邊界框信息
# xyxy_boxes = results.xyxy.cpu().numpy()

# # 打印每個邊界框的信息
# for box in xyxy_boxes:
#     x_min, y_min, x_max, y_max = box[:4]
#     print(f"Bounding Box: ({x_min}, {y_min}, {x_max}, {y_max})")


# 獲取第一個結果
result = results[0]

# 確認結果的類型
print(type(result))

# 根據結果的類型，獲取相應的屬性
if isinstance(result, dict):
    obb_info = result['obb']
else:
    obb_info = result.obb


# 打印結果
print(obb_info)



def rotate_image(image, angle):
    # 獲取圖像中心
    center = tuple(np.array(image.shape[1::-1]) / 2)
    # 旋轉矩陣
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    # 進行旋轉
    rotated_image = cv2.warpAffine(image, rotation_matrix, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return rotated_image

def crop_tooth(image, center, width, height, angle, target_size=(224, 224)):
    # 將圖像旋轉到正確的方向
    rotated_image = rotate_image(image, angle)
    # 計算旋轉後的牙齒位置
    x, y = center
    x_offset = int(max(0, x - width / 2))
    y_offset = int(max(0, y - height / 2))
    width = int(min(image.shape[1] - x_offset, width))
    height = int(min(image.shape[0] - y_offset, height))

    print(x_offset, y_offset, width, height,sep="，")
    
    # 裁剪圖像
    cropped_image = rotated_image[y_offset:y_offset+height, x_offset:x_offset+width]
    # # 調整大小為目標大小
    # cropped_image = cv2.resize(cropped_image, target_size, interpolation=cv2.INTER_LINEAR)
    return cropped_image


# 對每個邊界框進行處理
sorted_indices = sorted(range(len(obb_info.xyxyxyxy)), key=lambda i: obb_info.xyxyxyxy[i][0][0].item())  # 根據 orbit_center_x 排序的索引列表
for i, idx in enumerate(sorted_indices):
    # 獲取邊界框的四個角點座標
    pts = obb_info.xyxyxyxy[idx].numpy().reshape(-1, 2).astype(np.int32)
    # 計算邊界框的中心點座標
    # center_x = int((abs(pts[0][0]) + abs(pts[2][0])) / 2)
    # center_y = int((abs(pts[0][1]) + abs(pts[2][1])) / 2)
    center_x = int((pts[0][0] + pts[2][0]) / 2)
    center_y = int((pts[0][1] + pts[2][1]) / 2)
    # 計算邊界框的寬和高
    width = int(math.sqrt((pts[1][0] - pts[0][0])**2 + (pts[1][1] - pts[0][1])**2))
    height = int(math.sqrt((pts[2][0] - pts[1][0])**2 + (pts[2][1] - pts[1][1])**2))
    # 計算旋轉角度
    angle = math.atan2(pts[1][1] - pts[0][1], pts[1][0] - pts[0][0]) * 180 / math.pi
    # 切割牙齒圖像
    tooth_image = crop_tooth(image, (center_x, center_y), width, height, angle)

    print(center_x, center_y, width, height, angle,sep="/")