import cv2
import numpy as np
import matplotlib.pyplot as plt

# 讀取原始影像
img = cv2.imread('..\\dataset\\data_v1\\31.jpg')

# 將影像轉換為灰度
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 使用自適應直方圖均衡化處理影像
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
adaptive_equalized_img = clahe.apply(gray_img)

# 設置 Matplotlib 子圖
plt.figure(figsize=(10, 8))

# 原始影像和直方圖
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

plt.subplot(2, 2, 3)
plt.hist(gray_img.ravel(), 256, [0, 256])
plt.title('Histogram of Original Image')

# 自適應直方圖均衡化後的影像和直方圖
plt.subplot(2, 2, 2)
plt.imshow(adaptive_equalized_img, cmap='gray')
plt.title('Adaptive Histogram Equalized Image')

plt.subplot(2, 2, 4)
plt.hist(adaptive_equalized_img.ravel(), 256, [0, 256])
plt.title('Histogram of Equalized Image')

plt.show()
