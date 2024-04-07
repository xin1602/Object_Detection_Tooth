%% 实现高斯高通濾波器
A = imread('..\dataset\根尖合併牙周病灶\31.jpg');
A= rgb2gray(A);
A = im2double(A);
[a,b] = size(A);

% 原圖像
subplot(141), imshow(A), title('(a)');

F = fft2(A, 2*a, 2*b);
F3 = fftshift(F);

[a, b] = size(A);
W = zeros(2*a, 2*b);
D0 = 20;

for u = 1:2*a
    for v = 1:2*b
        D_square = (u-a) * (u-a) + (v-b) * (v-b);
        W(u, v) = 1 - exp(-D_square / (2*D0*D0));
    end
end

G = F3.*W;
F4 = ifftshift(G);
F1 = abs(ifft2(F4));
% F1 = ifft2(F4);
%F1 = max(abs(ifft2(F4)), 0);
F1 = F1(1:size(A, 1), 1:size(A, 2));
% 經由高通高通濾波器處理的結果
subplot(142), imshow(F1), title('(b)');


% 原圖像與經由高通高通濾波器處理之圖像的差值
result = A-F1;
result = imsubtract( A,F1);
subplot(143), imshow(result), title('(c)');

disp(['min(A): ', num2str(min(A(:)))]);
disp(['max(A): ', num2str(max(A(:)))]);
disp(['min(F1): ', num2str(min(real(F1(:))))]);
disp(['max(F1): ', num2str(max(real(F1(:))))]);


% 原圖像與經由高通高通濾波器處理之圖像的差值 再進行自適應直方圖均衡化
I_adapt = adapthisteq(result);

subplot(144),imshow(I_adapt),title('(d)');
