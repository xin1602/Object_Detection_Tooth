I = imread('..\dataset\根尖合併牙周病灶\31.jpg');
I_gray = rgb2gray(I); % 將彩色影像轉換為灰度影像

I_adapt = adapthisteq(I_gray);
% I_adapt = adapthisteq(I_gray, 'ClipLimit', 0.02);
% I_adapt = adapthisteq(I_gray, 'NumTiles', [8, 8]);
% I_adapt = adapthisteq(I_gray, 'Alpha', 0.1);

subplot(2,2,1);
imshow(I);
title('Original Image');

subplot(2,2,2);
imshow(I_adapt);
title('Adaptive Histogram Equalized Image');

subplot(2,2,3);
imhist(I_gray);
title('Histogram of Original Image');

subplot(2,2,4);
imhist(I_adapt);
title('Histogram of Equalized Image');