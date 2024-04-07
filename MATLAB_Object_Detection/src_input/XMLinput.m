%% XML Label File Read 
% Fred liu 2022.3.1

%%  Load XML File & String Normalization(載入XML標記資訊 & 字串正規化)
ds = fileDatastore('D:\lxh\dataset\multi_xml_1112_01\train\train_labels','ReadFcn',@readFcn);
T_bbox= readall(ds);
ds2 = fileDatastore('D:\lxh\dataset\multi_xml_1112_01\train\train_labels','ReadFcn',@readFcn2);
T_file= readall(ds2);

gTruth_labeler = table(T_file,T_bbox);

% Test==============================================
dsTest = fileDatastore('D:\lxh\dataset\multi_xml_1112_01\test\test_labels','ReadFcn',@readFcn);
dsTest_bbox= readall(dsTest);
dsTest2 = fileDatastore('D:\lxh\dataset\multi_xml_1112_01\test\test_labels','ReadFcn',@readFcn2);
dsTest_file= readall(dsTest2);

Test_gTruth_labeler = table(dsTest_file,dsTest_bbox);

%% String Normalization(字串正規化)
PathTrain = 'D:\lxh\dataset\multi_xml_json_1112_01\train\train_images';
PathTrain2 = [PathTrain,'\'];
TrainImg = strcat(PathTrain2,string(gTruth_labeler.T_file));
gTruth_labeler_SN = table(TrainImg,T_bbox);

PathTest = 'D:\lxh\dataset\multi_xml_json_1112_01\test\test_images';
PathTest2 = [PathTest,'\'];
TestImg = strcat(PathTest2,string(gTruth_labeler2.T_file2));
Test_gTruth_labeler_SN = table(TestImg,T_bbox2);

