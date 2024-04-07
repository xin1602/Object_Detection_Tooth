% 设置测试数据文件夹路径
test_folder = "F:\Lab\share\dataset\two_label_data_forCNN_v23\clean_final_v8\valid";

% 加载已训练的模型
% load('trainedNetwork_1.mat');  % 假设模型已保存为 trainedNetwork_1.mat

% 获取测试数据文件夹中的子文件夹（类别）
subfolders = dir(test_folder);
subfolders = subfolders(3:end);  % 忽略 '.' 和 '..' 

% 初始化预测结果和真实标签
predicted_labels = [];
true_labels = [];

% 遍历每个类别文件夹
for i = 1:length(subfolders)
    class_folder = fullfile(test_folder, subfolders(i).name);
    image_files = dir(fullfile(class_folder, '*.jpg'));
    
    % 遍历每张图片进行预测
    for j = 1:length(image_files)
        image_path = fullfile(class_folder, image_files(j).name);
        img = imread(image_path);
        
        % 调整图像大小为 [227 227 3]
        img_resized = imresize(img, [227, 227]);
        
        % 在此处对图像进行其他预处理，例如归一化等
        
        % 使用模型进行预测
        predicted_label = classify(trainedNetwork_1, img_resized);  % 使用训练好的模型进行预测
        predicted_labels = [predicted_labels; string(predicted_label)];  % 预测标签列表
        
        % 将真实标签添加到列表中
        true_labels = [true_labels; string(subfolders(i).name)];  % 真实标签列表
    end
end

% 计算混淆矩阵
conf_mat = confusionmat(true_labels, predicted_labels);

% 获取类别名称
labels = unique(true_labels);

% 计算精确率、召回率和 F1 分数
precision = diag(conf_mat) ./ sum(conf_mat, 1)';
recall = diag(conf_mat) ./ sum(conf_mat, 2);
f1_score = 2 * (precision .* recall) ./ (precision + recall);


% 显示混淆矩阵
disp('Confusion Matrix:');
disp(array2table(conf_mat, 'RowNames', labels, 'VariableNames', labels));

% 显示精确率、召回率和 F1 分数
metrics_table = table(precision, recall, f1_score, 'RowNames', labels);
disp('Metrics:');
disp(metrics_table);

% 计算总体准确率、总体精确率、总体召回率和总体 F1 分数
accuracy_total = sum(diag(conf_mat)) / sum(conf_mat, 'all');
precision_total = mean(precision);
recall_total = mean(recall);
f1_score_total = mean(f1_score);

% 显示总体指标
disp('Total Metrics:');
total_metrics_table = table(accuracy_total, precision_total, recall_total, f1_score_total);
disp(total_metrics_table);
