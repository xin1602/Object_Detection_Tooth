import cv2 
import matplotlib.pyplot as plt

# Read the image. 
# img = cv2.imread('E:\\Lab\\share\\dataset\\two_label_data_forCNN_v21\\final\\apical lesion\\083_2.jpg') 
# img = cv2.imread('E:\\Lab\\share\\dataset\\two_label_data_forCNN_v21\\final\\normal\\038_1.jpg') 
img = cv2.imread('E:\\Lab\\share\\dataset\\two_label_data_forCNN_v21\\final\\peri endo\\017_2.jpg') 

# cv2.bilateralFilter(圖片, d, sigmaColor, sigmaSpace)
# d：濾波器的窗口大小
# sigmaColor：越小，濾波器對色彩變化的敏感度越低，類似色彩的像素會被視為同一區域，進而減少色彩噪點
# sigmaSpace：越小，濾波器對空間變化的敏感度越低，空間上較近的像素會被視為同一區域，進而減少空間噪點
bilateral = cv2.bilateralFilter(img, 15, 20, 20) 

# # Save the output. 
# cv2.imwrite('taj_bilateral.jpg', bilateral) 

# 顯示結果
plt.figure(figsize=(12, 6))

plt.subplot(121)
plt.imshow(img, cmap='gray')
plt.title('Original Image')

plt.subplot(122)
plt.imshow(bilateral, cmap='gray')
plt.title('BilateralFilter Image')

plt.show()