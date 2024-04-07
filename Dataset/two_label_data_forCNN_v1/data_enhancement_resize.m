% 設定原始圖片資料夾
original_folder = "E:\Lab\share\dataset\two_label_data_forCNN_v1\peri endo";
% original_folder = 'D:\lxh\dataset\test_single\original_images\apical lesion';

% 設定增強後圖片保存資料夾
enhanced_folder = "E:\Lab\share\dataset\two_label_data_forCNN_v1\peri endo";
% enhanced_folder = 'D:\lxh\dataset\test_single\enhancement_images\apical lesion';

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
    
    % 調整圖片大小至224*224，保持原比例
    resized_image = imresize(original_image, [224, NaN]);
        
    % 保存處理後的圖片至resized_folder
    imwrite(resized_image, fullfile(enhanced_folder, strcat(image_files(i).name)));
end

% 迴圈處理每張圖片
for i = 1:length(image_files)
    % 讀取原始圖片
    original_image = imread(fullfile(enhanced_folder, image_files(i).name));
    
    % 資料增強：水平翻轉
    flipped_horizontal = flip(original_image, 2);
    imwrite(flipped_horizontal, fullfile(enhanced_folder, strcat(image_files(i).name, '_flipped_horizontal.jpg')));
    
end

% % 設定原始圖片資料夾
% original_folder = "E:\Lab\share\dataset\two_label_data_forCNN_v1\apical lesion";
% % original_folder = 'D:\lxh\dataset\test_single\original_images\apical lesion';
% 
% % 設定增強後圖片保存資料夾
% enhanced_folder = "E:\Lab\share\dataset\two_label_data_forCNN_v1\apical lesion";
% % enhanced_folder = 'D:\lxh\dataset\test_single\enhancement_images\apical lesion';
% 
% % 確保保存資料夾存在
% if ~exist(enhanced_folder, 'dir')
%     mkdir(enhanced_folder);
% end
% 
% % 取得原始資料夾下所有圖片
% image_files = dir(fullfile(original_folder, '*.jpg'));
% 
% % 迴圈處理每張圖片
% for i = 1:length(image_files)
%     % 讀取原始圖片
%     original_image = imread(fullfile(original_folder, image_files(i).name));
% 
%     % 調整圖片大小至224*224，保持原比例
%     resized_image = imresize(original_image, [224, NaN]);
% 
%     % 保存處理後的圖片至resized_folder
%     imwrite(resized_image, fullfile(enhanced_folder, strcat(image_files(i).name)));
% end
% 
% % 迴圈處理每張圖片
% for i = 1:length(image_files)
%     % 讀取原始圖片
%     original_image = imread(fullfile(enhanced_folder, image_files(i).name));
% 
%     % 資料增強：水平翻轉
%     flipped_horizontal = flip(original_image, 2);
%     imwrite(flipped_horizontal, fullfile(enhanced_folder, strcat(image_files(i).name, '_flipped_horizontal.jpg')));
% 
% 
%     % 資料增強：垂直翻轉
%     flipped_vertical = flip(original_image, 1);
%     imwrite(flipped_vertical, fullfile(enhanced_folder, strcat( image_files(i).name,'_flipped_vertical.jpg')));
% 
%     % 資料增強：水平和垂直翻轉
%     flipped_both = flip(flipped_horizontal, 1);
%     imwrite(flipped_both, fullfile(enhanced_folder, strcat( image_files(i).name,'_flipped_both.jpg')));
% 
% end