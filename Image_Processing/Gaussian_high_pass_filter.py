# libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

# open the image f
f = cv2.imread('F:\\Lab\\share\\dataset\\two_label_data_v1\\origin\\31.jpg',0)

# transform the image into frequency domain, f --> F
F = np.fft.fft2(f)
Fshift = np.fft.fftshift(F)

# Create Gaussin Filter: Low Pass Filter
M,N = f.shape
H = np.zeros((M,N), dtype=np.float32)
D0 = 5
for u in range(M):
    for v in range(N):
        D = np.sqrt((u-M/2)**2 + (v-N/2)**2)
        H[u,v] = np.exp(-D**2/(2*D0*D0))

# Image Filters
Gshift = Fshift * H
G = np.fft.ifftshift(Gshift)
g = np.abs(np.fft.ifft2(G))

# Gaussian: High pass filter
HPF = 1 - H

# Image Filters
Gshift = Fshift * HPF
G = np.fft.ifftshift(Gshift)
g = np.abs(np.fft.ifft2(G))


# 將 g 轉換為整數型別
g = g.astype(np.uint8)
# 差值圖像
result = cv2.subtract(f, g)

# 顯示結果
plt.figure(figsize=(12, 6))

plt.subplot(131)
plt.imshow(f, cmap='gray')
plt.title('Original Image')

plt.subplot(132)
plt.imshow(g, cmap='gray')
plt.title('High Pass Filtered Image')

plt.subplot(133)
plt.imshow(result, cmap='gray')
plt.title('Difference Image')

plt.show()