import cv2
import math
import numpy as np
from ultralytics import YOLO
from PIL import Image
import os

# Rotation matrix function
def rotate_matrix (x, y, angle, x_shift=0, y_shift=0, units="DEGREES"):
    """
    Rotates a point in the xy-plane counterclockwise through an angle about the origin
    https://en.wikipedia.org/wiki/Rotation_matrix
    :param x: x coordinate
    :param y: y coordinate
    :param x_shift: x-axis shift from origin (0, 0)
    :param y_shift: y-axis shift from origin (0, 0)
    :param angle: The rotation angle in degrees
    :param units: DEGREES (default) or RADIANS
    :return: Tuple of rotated x and y
    """

    # Shift to origin (0,0)
    x = x - x_shift
    y = y - y_shift

    # Convert degrees to radians
    if units == "DEGREES":
        angle = math.radians(angle)

    # Rotation matrix multiplication to get rotated x & y
    xr = (x * math.cos(angle)) - (y * math.sin(angle)) + x_shift
    yr = (x * math.sin(angle)) + (y * math.cos(angle)) + y_shift

    return xr, yr


# 初始化 YOLOv8 模型
model = YOLO("F:\\Lab\\share\\YOLO_segmentation\\seg_0313_tooth_data_v1_0308_GRAY_AHE_01\\best.pt")

# 處理整個資料夾中的圖像
folder_path = "F:\\Lab\\share\\dataset\\two_label_data_combine\\GRAY_AHE"
for filename in os.listdir(folder_path):
    if filename.endswith(".jpg"):
        image_path = os.path.join(folder_path, filename)
        # 讀取圖片
        image = cv2.imread(image_path)
        # 執行預測
        results = model(image)
        # 獲取第一個結果
        result = results[0]
        # 獲取 OBB 信息
        obb_info = result.obb
        # 獲取圖像的寬度和高度
        height, width, channels = image.shape
        center_x = width//2
        center_y = height//2

        # 對每個邊界框進行處理
        sorted_indices = sorted(range(len(obb_info.xyxyxyxy)), key=lambda i: obb_info.xyxyxyxy[i][0][0].item())  # 根據 orbit_center_x 排序的索引列表
        for i, idx in enumerate(sorted_indices):
            # 保存遮罩圖像，使用原始圖片的檔名加上排序索引 i
            original_filename = os.path.splitext(os.path.basename(image_path))[0]

            # 獲取邊界框的四個角點座標
            pts = obb_info.xyxyxyxy[idx].numpy().reshape(-1, 2).astype(np.int32)
            # print(pts)

            # 計算旋轉角度
            angle = math.atan2(pts[1][1] - pts[0][1], pts[1][0] - pts[0][0]) * 180 / math.pi

            rotation_center = (center_x, center_y)

            # 將圖像旋轉至水平位置，並指定旋轉中心
            rotated_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)).rotate(angle, expand=True, center=rotation_center)

            # 圖像旋轉 擴展後 圖像寬度、長度、中心點位置
            width_expand ,height_expand= rotated_image.size
            center_x_expand = width_expand//2
            center_y_expand = height_expand//2
  

            ax, ay = rotate_matrix(pts[0][0]+(center_x_expand-center_x), pts[0][1]+(center_y_expand-center_y), -angle, center_x_expand, center_y_expand)
            bx, by = rotate_matrix(pts[1][0]+(center_x_expand-center_x), pts[1][1]+(center_y_expand-center_y), -angle, center_x_expand, center_y_expand)
            cx, cy = rotate_matrix(pts[2][0]+(center_x_expand-center_x), pts[2][1]+(center_y_expand-center_y), -angle, center_x_expand, center_y_expand)
            dx, dy = rotate_matrix(pts[3][0]+(center_x_expand-center_x), pts[3][1]+(center_y_expand-center_y), -angle, center_x_expand, center_y_expand)

            # print(original_filename,pts[0][0],pts[1][0],pts[2][0],pts[3][0])
            # print(original_filename,ax,bx,cx,dx)
            # print(original_filename,pts[0][1],pts[1][1],pts[2][1],pts[3][1])
            # print(original_filename,ay,by,cy,dy)


            # 將旋轉後的圖像根據範圍裁剪
            cropped_image = rotated_image.crop((int(ax), int(cy), int(cx), int(ay)))
            
            # 將裁剪後的圖像resize((224, 224))
            # resized_image = cropped_image.resize((224, 224))

            # 保存提取的图像部分
            output_folder = 'F:\\Lab\\share\\YOLO_segmentation\\seg_0313_tooth_data_v1_0308_GRAY_AHE_01\\cropped_images'
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            cropped_image.save(os.path.join(output_folder, f'{original_filename}_{i+1}.jpg'))

        # 保存预测结果
        output_folder = 'F:\\Lab\\share\\YOLO_segmentation\\seg_0313_tooth_data_v1_0308_GRAY_AHE_01\\predicts'
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        for r in results:
            im_array = r.plot()  # plot a BGR numpy array of predictions
            im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
            im.save(os.path.join(output_folder, f'{original_filename}.jpg'))  # save image

