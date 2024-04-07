import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)
kernel1 = np.ones((5, 5), np.uint8)

# img = cv2.imread('colorcolor.jpg')
img = cv2.imread('11.jpg')
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# 將彩色圖像轉換為灰度圖像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 對圖像進行高斯模糊。這有助於減少圖像中的噪聲，使後續的處理更準確。
# (15, 15) 是高斯核的大小，表示模糊的程度。
# 10 是標準差，控制模糊的程度。 
blur = cv2.GaussianBlur(img, (15, 15), 10)

# 使用Canny邊緣檢測器來檢測圖像的邊緣。
# 200 和 250 是Canny演算法中的低閾值和高閾值，用於確定邊緣的強度。
canny = cv2.Canny(img, 30, 70)

# 對Canny邊緣檢測結果進行膨脹操作。這有助於連接邊緣，填充邊緣之間的空隙。
# kernel 是膨脹操作的核（矩陣），iterations=1 表示執行一次膨脹。
dilate = cv2.dilate(canny, kernel, iterations=1)

# 膨脹後的圖像進行侵蝕操作。這有助於消除小的噪聲和細小的不連續區域。
# kernel1 是侵蝕操作的核，iterations=1 表示執行一次侵蝕。
erode = cv2.erode(dilate, kernel1, iterations=1)


cv2.imshow('img', img)
#cv2.imshow('gray', gray)
#cv2.imshow('blur', blur)
cv2.imshow('canny', canny)
#cv2.imshow('dilate', dilate)
#cv2.imshow('erode', erode)
cv2.waitKey(0)
