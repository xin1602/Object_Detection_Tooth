% Load the trained model
% load('alexnet_1119_01.mat', 'trainedNetwork_1');

% 設定使用的模型
net = trainedNetwork_1;


% 指定測試資料夾路徑
testFolderPath = 'E:\Lab\share\dataset\two_label_data_forCNN_v23\clean_test\normal';
%testFolderPath = 'E:\Lab\share\dataset\two_label_data_forCNN_v23\clean_final_v8\valid\normal';

% 取得資料夾中所有影像的檔案列表
imgFiles = dir(fullfile(testFolderPath, '*.jpg'));

% 循環處理每個影像
for i = 1:numel(imgFiles)
     % 讀取影像
     imgPath = fullfile(testFolderPath, imgFiles(i).name);
     img = imread(imgPath);
    
     % 調整影像大小
     img_resized = imresize(img, [227, 227]);
    
     % 使用模型進行分類
     label = classify(net, img_resized);
    
     % 顯示分類結果
     fprintf('normal Image: %s, Predicted Label: %s\n', imgFiles(i).name, char(label));
    
     % 在這裡，你可以選擇將結果儲存到一個陣列或檔案中，以便進一步分析
end


% 指定測試資料夾路徑
testFolderPath = 'E:\Lab\share\dataset\two_label_data_forCNN_v23\clean_test\apical lesion';
%testFolderPath = 'E:\Lab\share\dataset\two_label_data_forCNN_v23\clean_final_v8\valid\apical lesion';

% 取得資料夾中所有影像的檔案列表
imgFiles = dir(fullfile(testFolderPath, '*.jpg'));

% 循環處理每個影像
for i = 1:numel(imgFiles)
     % 讀取影像
     imgPath = fullfile(testFolderPath, imgFiles(i).name);
     img = imread(imgPath);
    
     % 調整影像大小
     img_resized = imresize(img, [227, 227]);
    
     % 使用模型進行分類
     label = classify(net, img_resized);
    
     % 顯示分類結果
     fprintf('apical lesion Image: %s, Predicted Label: %s\n', imgFiles(i).name, char(label));
    
     % 在這裡，你可以選擇將結果儲存到一個陣列或檔案中，以便進一步分析
end

% 指定測試資料夾路徑
testFolderPath = 'E:\Lab\share\dataset\two_label_data_forCNN_v23\clean_test\peri endo';
%testFolderPath = 'E:\Lab\share\dataset\two_label_data_forCNN_v23\clean_final_v8\valid\peri endo';


% 取得資料夾中所有影像的檔案列表
imgFiles = dir(fullfile(testFolderPath, '*.jpg'));

% 循環處理每個影像
for i = 1:numel(imgFiles)
     % 讀取影像
     imgPath = fullfile(testFolderPath, imgFiles(i).name);
     img = imread(imgPath);
    
     % 調整影像大小
     img_resized = imresize(img, [227, 227]);
    
     % 使用模型進行分類
     label = classify(net, img_resized);
    
     % 顯示分類結果
     fprintf('peri endo Image: %s, Predicted Label: %s\n', imgFiles(i).name, char(label));
    
     % 在這裡，你可以選擇將結果儲存到一個陣列或檔案中，以便進一步分析
end