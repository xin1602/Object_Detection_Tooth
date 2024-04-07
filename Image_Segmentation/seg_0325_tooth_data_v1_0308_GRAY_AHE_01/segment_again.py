import numpy as np
from PIL import Image
import os


# 處理整個資料夾中的圖像
folder_path = "F:\\Lab\\share\\YOLO_segmentation\\seg_0325_tooth_data_v1_0308_GRAY_AHE_01\\rotated_images"
for filename in os.listdir(folder_path):
    if filename.endswith(".jpg"):

        new_file_name = filename.split("_rotated.jpg")[0]
        image_path = os.path.join(folder_path, filename)


        rotated_image_path = f"{os.path.splitext(image_path)[0]}.jpg"
        bbox_info_path = f"F:\\Lab\\share\\YOLO_segmentation\\seg_0325_tooth_data_v1_0308_GRAY_AHE_01\\bbox_info\\{new_file_name}_bbox_info.npy"


        if os.path.exists(rotated_image_path) and os.path.exists(bbox_info_path):

            rotated_image = Image.open(rotated_image_path)
            bbox_info = np.load(bbox_info_path)

            output_folder_cropped = 'F:\\Lab\\share\\YOLO_segmentation\\seg_0325_tooth_data_v1_0308_GRAY_AHE_01\\cropped_images_x20_y20'
            if not os.path.exists(output_folder_cropped):
                os.makedirs(output_folder_cropped)

            for idx, bbox in enumerate(bbox_info):
                cropped_image = rotated_image.crop((int(bbox[0])-20, int(bbox[1])-20, int(bbox[2])+20, int(bbox[3])+20))
                cropped_image.save(os.path.join(output_folder_cropped, f'{new_file_name}.jpg'))
