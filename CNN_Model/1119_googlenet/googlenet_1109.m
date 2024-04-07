% 加载预训练模型
load('googlenet_1119.mat', 'netTransfer');

% 指定测试文件夹路径
testFolderPath = 'D:\lxh\dataset\test_single\apical lesion';

% 获取文件夹中所有图像的文件列表
imgFiles = dir(fullfile(testFolderPath, '*.jpg'));

% 循环处理每个图像
for i = 1:numel(imgFiles)
    % 读取图像
    imgPath = fullfile(testFolderPath, imgFiles(i).name);
    img = imread(imgPath);
    
    % 调整图像大小
    img_resized = imresize(img, [224, 224]);
    
    % 使用模型进行分类
    label = classify(netTransfer, img_resized);
    
    % 显示分类结果
    fprintf('Image: %s, Predicted Label: %s\n', imgFiles(i).name, char(label));
    
    % 在这里，你可以选择将结果存储到一个数组或文件中，以备进一步分析
end