
% 設定原始圖片資料夾
original_folder = "E:\Lab\share\dataset\two_label_data_forCNN_v24\origin_crop_x20_y40\train\normal";
%original_folder = "E:\Lab\share\dataset\two_label_data_forCNN_v24\origin_crop_x20_y40\train\apical lesion";
%original_folder = "E:\Lab\share\dataset\two_label_data_forCNN_v24\origin_crop_x20_y40\train\peri endo";
%original_folder = "E:\Lab\share\dataset\two_label_data_forCNN_v24\origin_crop_x20_y40\valid\normal";
%original_folder = "E:\Lab\share\dataset\two_label_data_forCNN_v24\origin_crop_x20_y40\valid\apical lesion";
%original_folder = "E:\Lab\share\dataset\two_label_data_forCNN_v24\origin_crop_x20_y40\valid\peri endo";




% 設定增強後圖片保存資料夾
enhanced_folder = "E:\Lab\share\dataset\two_label_data_forCNN_v24\origin_crop_x20_y40_padding_enhanced.4\train\normal";
%enhanced_folder = "E:\Lab\share\dataset\two_label_data_forCNN_v24\origin_crop_x20_y40_padding_enhanced.4\train\apical lesion";
%enhanced_folder = "E:\Lab\share\dataset\two_label_data_forCNN_v24\origin_crop_x20_y40_padding_enhanced.4\train\peri endo";
%enhanced_folder = "E:\Lab\share\dataset\two_label_data_forCNN_v24\origin_crop_x20_y40_padding_enhanced.4\valid\normal";
%enhanced_folder = "E:\Lab\share\dataset\two_label_data_forCNN_v24\origin_crop_x20_y40_padding_enhanced.4\valid\apical lesion";
%enhanced_folder = "E:\Lab\share\dataset\two_label_data_forCNN_v24\origin_crop_x20_y40_padding_enhanced.4\valid\peri endo";







% 確保保存資料夾存在
if ~exist(enhanced_folder, 'dir')
    mkdir(enhanced_folder);
end

% 取得原始資料夾下所有圖片
image_files = dir(fullfile(original_folder, '*.jpg'));

% 迴圈處理每張圖片
for i = 1:length(image_files)
    % 讀取原始圖片
    original_image = imread(fullfile(original_folder, image_files(i).name));

    % 將原始圖片轉換成灰階
    gray_image = rgb2gray(original_image);

    % 將灰階圖像的通道複製兩次以產生三個相同的通道
    color_image = repmat(gray_image, [1, 1, 3]);

    % 調整圖片大小至224*, NaN
    resized_image = imresize(color_image, [224, NaN]);

    % 計算填充黑色的寬度和高度
    padding_width = floor((224 - size(resized_image, 2)) / 2);
    padding_height = floor((224 - size(resized_image, 1)) / 2);
    
    % 填充黑色
    resized_image_padded = padarray(resized_image, [padding_height, padding_width], 0, 'both');

    % 保存處理後的圖片至resized_folder
    imwrite(resized_image_padded, fullfile(enhanced_folder, strcat(image_files(i).name)));
end

% 迴圈處理每張圖片
for i = 1:length(image_files)
    % 讀取原始圖片
    original_image = imread(fullfile(enhanced_folder, image_files(i).name));

    % 資料增強：水平翻轉
    flipped_horizontal = flip(original_image, 2);
    imwrite(flipped_horizontal, fullfile(enhanced_folder, strcat(image_files(i).name, '_flipped_horizontal.jpg')));


    % 資料增強：垂直翻轉
    flipped_vertical = flip(original_image, 1);
    imwrite(flipped_vertical, fullfile(enhanced_folder, strcat( image_files(i).name,'_flipped_vertical.jpg')));

    % 資料增強：水平和垂直翻轉
    flipped_both = flip(flipped_horizontal, 1);
    imwrite(flipped_both, fullfile(enhanced_folder, strcat( image_files(i).name,'_flipped_both.jpg')));

    %  % 資料增強：逆時針旋轉90度
    rotated_90 = imrotate(original_image, 90);
    %imwrite(rotated_90, fullfile(enhanced_folder, strcat(image_files(i).name, '_rotated_90.jpg')));
    % 
    % % 資料增強：逆時針旋轉270度
    rotated_270 = imrotate(original_image, 270);
    %imwrite(rotated_270, fullfile(enhanced_folder, strcat(image_files(i).name, '_rotated_270.jpg')));

end