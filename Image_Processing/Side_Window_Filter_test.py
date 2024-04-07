import cv2
import matplotlib.pyplot as plt
from SideWindowFilter import SideWindowFiltering_3d, SideWindowFiltering 

# for RGB image
# img = cv2.imread('aiaceo.jpg')
# swf_img = SideWindowFiltering_3d(img, kernel=3, mode='mean')

# for Gray image
img = cv2.imread('E:\\Lab\\share\\dataset\\two_label_data_forCNN_v21\\final\\apical lesion\\037_5.jpg', 0)


# mode = 'mean', 'gaussian', 'median'
swf_img = SideWindowFiltering(img, kernel=13, mode='median')  

# 顯示結果
plt.figure(figsize=(12, 6))

plt.subplot(121)
plt.imshow(img, cmap='gray')
plt.title('Original Image')

plt.subplot(122)
plt.imshow(swf_img, cmap='gray')
plt.title('SideWindowFiltering Image')

plt.show()