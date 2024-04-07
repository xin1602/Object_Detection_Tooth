# import cv2
# import numpy as np
# from ultralytics import YOLO  # or OBBPredictor

# # 加載圖片
# image = cv2.imread('F:\\Lab\\share\\dataset\\multi_coco_json_1112_01\\test\\117_jpg.rf.bf2829db272438406ab3710bee89b31f.jpg')

# # 使用 OBB 模型進行預測
# model = YOLO('F:\\Lab\\share\\YOLO_segmentation\\best.pt')
# results = model(image)

# # 創建一個空白的 640x640 黑色圖像
# mask = np.zeros((640, 640, 3), dtype=np.uint8)

# # 提取每個邊界框內的圖像，將其放置在遮罩中
# for box in results.xyxy.cpu().numpy():
#     x_min, y_min, x_max, y_max = box[:4]
#     cropped_image = image[int(y_min):int(y_max), int(x_min):int(x_max)]
    
#     # 將圖像放置在遮罩中
#     mask[int(y_min):int(y_min) + cropped_image.shape[0], int(x_min):int(x_min) + cropped_image.shape[1]] = cropped_image

# # 將其他位置填充為黑色
# mask[~np.any(mask, axis=2)] = [0, 0, 0]

# # 將遮罩保存為圖像文件
# cv2.imwrite('masked_image.jpg', mask)



# import cv2
# import numpy as np
# from ultralytics import YOLO  # or OBBPredictor
# from ultralytics.engine.results import Results

# # 加載圖片
# image = cv2.imread('F:\\Lab\\share\\dataset\\multi_coco_json_1112_01\\test\\117_jpg.rf.bf2829db272438406ab3710bee89b31f.jpg')

# # 使用 OBB 模型進行預測
# model = YOLO('F:\\Lab\\share\\YOLO_segmentation\\best.pt')
# results = model(image)

# # 創建一個空白的 640x640 黑色圖像
# mask = np.zeros((640, 640, 3), dtype=np.uint8)

# # 提取每個邊界框內的圖像，將其放置在遮罩中
# for result in results:
#     for obb_info in result.obb:
#         obb_info_tensor = obb_info.data.squeeze()
#         x_min, y_min, x_max, y_max, r, conf, cls = obb_info_tensor[:7].tolist()

#         # Verify bounding box coordinates
#         print("Bounding Box Coordinates:", x_min, y_min, x_max, y_max)
#         if x_min < 0 or y_min < 0 or x_max > image.shape[1] or y_max > image.shape[0]:
#             print("Error: Bounding box coordinates out of bounds.")
#             continue

#         # Scale bounding box coordinates to match original image size
#         x_min_scaled = int(x_min * image.shape[1] / 640)
#         y_min_scaled = int(y_min * image.shape[0] / 640)
#         x_max_scaled = int(x_max * image.shape[1] / 640)
#         y_max_scaled = int(y_max * image.shape[0] / 640)

#         # Extract cropped image
#         cropped_image = image[y_min_scaled:y_max_scaled, x_min_scaled:x_max_scaled]

#         # Check if cropped image contains content
#         print("Cropped Image Shape:", cropped_image.shape)
#         if cropped_image.size == 0:
#             print("Error: Cropped image is empty.")
#             continue

#         # Overlay cropped image onto mask
#         mask[y_min_scaled:y_min_scaled + cropped_image.shape[0], x_min_scaled:x_min_scaled + cropped_image.shape[1]] = cropped_image

# # Fill remaining areas of mask with black
# mask[mask.sum(axis=2) == 0] = [0, 0, 0]

# # Save masked image
# cv2.imwrite('masked_image.jpg', mask)



import pkg_resources

installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])
print(installed_packages_list)




# import cv2
# import numpy as np
# from ultralytics.models.yolo.obb.predict import OBBPredictor

# # Load the image
# image = cv2.imread('F:\\Lab\\share\\dataset\\multi_coco_json_1112_01\\test\\117_jpg.rf.bf2829db272438406ab3710bee89b31f.jpg')

# # Initialize the OBB predictor
# predictor = OBBPredictor()

# # Perform prediction
# results = predictor(image)

# # Create a blank mask
# mask = np.zeros((640, 640, 3), dtype=np.uint8)

# # Extract cropped images based on the predictions and place them on the mask
# for obb_info in results[0].obb:
#     x_min, y_min, x_max, y_max, r, conf, cls = obb_info[:7]

#     # Extract the cropped image
#     cropped_image = image[int(y_min):int(y_max), int(x_min):int(x_max)]

#     # Place the cropped image on the mask
#     mask[int(y_min):int(y_max), int(x_min):int(x_max)] = cropped_image

# # Fill other regions with black color
# mask[mask.sum(axis=2) == 0] = [0, 0, 0]

# # Save the mask as an image file
# cv2.imwrite('masked_image.jpg', mask)



