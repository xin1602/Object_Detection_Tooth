% 設定原始圖片資料夾
% original_folder = 'D:\lxh\dataset\train_single\original_images\normal';
original_folder = 'D:\lxh\dataset\test_single\original_images\normal';

% 設定調整固定大小並遮罩後圖片保存資料夾
% enhanced_folder = 'D:\lxh\dataset\train_single\enhancement_images\normal';
enhanced_folder = 'D:\lxh\dataset\test_single\enhancement_images\normal';

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
    
    % 計算填充黑色的寬度和高度
    padding_width = floor((224 - size(resized_image, 2)) / 2);
    padding_height = floor((224 - size(resized_image, 1)) / 2);
    
    % 填充黑色
    resized_image_padded = padarray(resized_image, [padding_height, padding_width], 0, 'both');
    
    % 保存處理後的圖片至resized_folder
    imwrite(resized_image_padded, fullfile(enhanced_folder, image_files(i).name));
end