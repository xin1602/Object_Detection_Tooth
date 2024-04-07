#!/usr/bin/env python
"""
Sample script that uses the addd module created using MATLAB Compiler SDK.
Refer to the MATLAB Compiler SDK documentation for more information.
"""
import cv2
import histogram_equalization

my_histogram_equalization = histogram_equalization.initialize()

# 使用編譯後的函式
result = my_histogram_equalization.histogram_equalization('..\\..\\..\\dataset\\根尖合併牙周病灶\\31.jpg')
print(result)  

img = cv2.imread(result) 
cv2.imshow('Histogram Equalization:'+result, img)  # 使用名為 'Histogram Equalization:'+result 的視窗開啟圖片
cv2.waitKey(0)                 # 按下任意鍵停止
cv2.destroyAllWindows()        # 結束所有圖片視窗