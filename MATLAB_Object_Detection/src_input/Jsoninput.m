%% Json Label File Read
% Fred liu 2022.3.1

%% Json Read(載入Json標記資訊 & 字串正規化)
% Train
filename = 'D:\lxh\dataset\multi_coco_json_1112_01\train\_annotations.coco.json';
strData = fileread(filename);
DecodeData = jsondecode(strData);
%
idx = findgroups([DecodeData.annotations.image_id]);
T_bbox = splitapply(@(x){x},[DecodeData.annotations.bbox],idx)';
T_file = {DecodeData.images.file_name}';
% arrayfun(@(x)getfield(x,'file_name'),DecodeData.images,'UniformOutput',false);
gTruth_labeler = table(T_file,T_bbox);

% Test
filename2 = 'D:\lxh\dataset\multi_coco_json_1112_01\test\_annotations.coco.json';
strData2 = fileread(filename2);
DecodeData2 = jsondecode(strData2);
%
idx2 = findgroups([DecodeData2.annotations.image_id]);
T_bbox2 = splitapply(@(x){x},[DecodeData2.annotations.bbox],idx2)';
T_file2 = {DecodeData2.images.file_name}';
% arrayfun(@(x)getfield(x,'file_name'),DecodeData.images,'UniformOutput',false);
gTruth_labeler2 = table(T_file2,T_bbox2);

%% String Normalization(字串正規化)
PathTrain = 'D:\lxh\dataset\multi_coco_json_1112_01\train';
PathTrain2 = [PathTrain,'\'];
TrainImg = strcat(PathTrain2,string(gTruth_labeler.T_file));
gTruth_labeler_SN = table(TrainImg,T_bbox);

PathTest = 'D:\lxh\dataset\multi_coco_json_1112_01\test';
PathTest2 = [PathTest,'\'];
TestImg = strcat(PathTest2,string(gTruth_labeler2.T_file2));
gTruth_labeler2_SN = table(TestImg,T_bbox2);


