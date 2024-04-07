% 設定使用的模型
net = trainedNetwork_1;

% 指定測試資料夾路徑
testFolderPath = 'E:\Lab\share\dataset\two_label_data_forCNN_v24\origin_padding_enhanced.4_GH_d4_AHE_c4_t4-4\valid';

% 調用遞歸函數處理測試文件夾
processFolder(testFolderPath, net);

% 定義 processFolder 函數
function processFolder(folderPath, net)
    % 取得資料夾中所有影像的檔案列表
    imgFiles = dir(fullfile(folderPath, '*.jpg'));

    % 循環處理每個影像
    for i = 1:numel(imgFiles)
        % 讀取影像
        imgPath = fullfile(folderPath, imgFiles(i).name);
        img = imread(imgPath);

        % 調整影像大小
        img_resized = imresize(img, [227, 227]);

        % 使用模型進行分類
        [label, scores] = classify(net, img_resized);

        % 獲取預測的類別及其概率
        predictedLabel = char(label);
        maxScore = max(scores);

        % 獲取真實標籤
        [~, folderName, ~] = fileparts(folderPath);
        trueLabel = folderName;

        % 比較預測和真實標籤，顯示結果
        if strcmpi(predictedLabel, trueLabel)
            fprintf('%s影像：%s，預測標籤：%s，概率：%.2f%%，預測結果：正確\n', trueLabel, imgFiles(i).name, predictedLabel, maxScore*100);
        else
            fprintf('%s影像：%s，預測標籤：%s，概率：%.2f%%，預測結果：錯誤\n', trueLabel, imgFiles(i).name, predictedLabel, maxScore*100);
        end
    end

    % 檢查是否存在子資料夾
    subfolders = dir(folderPath);
    subfolders = subfolders([subfolders.isdir]);  % 過濾出資料夾
    subfolders = subfolders(~ismember({subfolders.name}, {'.', '..'}));  % 移除 '.' 和 '..'

    % 遞歸處理每個子資料夾
    for i = 1:numel(subfolders)
        subfolderPath = fullfile(folderPath, subfolders(i).name);
        processFolder(subfolderPath, net);  % 遞歸調用處理子資料夾
    end
end