function z=histogram_equalization(pic)
%I = imread('..\dataset\根尖合併牙周病灶\31.jpg'); 
I = imread(pic); 
I2 = histeq(I);
imwrite(I2,'31_HE.jpg');

z="31_HE.jpg";

% subplot(2,2,1); 
% imshow(I);
% title('Original Image');
% 
% subplot(2,2,2); 
% imshow(I2);
% title('Histogram Equalized Image');
% 
% subplot(2,2,3); 
% imhist(I);
% title('Histogram of Original Image');
% 
% subplot(2,2,4); 
% imhist(I2);
% title('Histogram of Equalized Image');

