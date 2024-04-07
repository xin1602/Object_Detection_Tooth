import cv2
import numpy as np
import matplotlib.pyplot as plt

import os

# 讀取原始影像
img = cv2.imread('F:\\Lab\\share\\dataset\\two_label_data_v1\\origin\\31.jpg')

# 將影像轉換為灰度
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 對灰度影像進行直方圖均衡化
equalized_img = cv2.equalizeHist(gray_img)

# 設置 Matplotlib 子圖
plt.figure(figsize=(10, 8))

# 原始影像和直方圖
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

plt.subplot(2, 2, 3)
plt.hist(gray_img.ravel(), 256, [0, 256])
plt.title('Histogram of Original Image')

# 直方圖均衡化後的影像和直方圖
plt.subplot(2, 2, 2)
plt.imshow(equalized_img, cmap='gray')
plt.title('Histogram Equalized Image')

plt.subplot(2, 2, 4)
plt.hist(equalized_img.ravel(), 256, [0, 256])
plt.title('Histogram of Equalized Image')

plt.show()
