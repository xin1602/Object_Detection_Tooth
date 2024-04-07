I = imread('..\dataset\根尖合併牙周病灶\31.jpg'); 
I2 = histeq(I);


subplot(2,2,1); 
imshow(I);
title('Original Image');

subplot(2,2,2); 
imshow(I2);
title('Histogram Equalized Image');

subplot(2,2,3); 
imhist(I);
title('Histogram of Original Image');

subplot(2,2,4); 
imhist(I2);
title('Histogram of Equalized Image');


