import os
import shutil

def copy_files(source_folder, target_folder, filenames):
    for filename in filenames:
        source_path = os.path.join(source_folder, filename)
        target_path = os.path.join(target_folder, filename)
        shutil.copyfile(source_path, target_path)
        print(f"Copied file: {filename}")

#我要去A資料夾中讀取所有.jpg的檔名，再去B資料夾找到[A資料夾所有.jpg的檔名]的檔案，複製一份到C資料夾
def main():
    # 原始資料夾 A
    folder_a = "E:\\Lab\\share\dataset\\two_label_data_forCNN_v24\\origin\\train\\normal"
    # folder_a = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin\\train\\apical lesion"
    # folder_a = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin\\train\\peri endo"
    # folder_a = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin\\valid\\normal"
    # folder_a = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin\\valid\\apical lesion"
    # folder_a = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin\\valid\\peri endo"

    # 目標資料夾 B
    folder_b = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\cropped_images_x20_y0"

    # 目標資料夾 C
    folder_c = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_crop_x20_y0\\train\\normal"
    # folder_c = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_crop_x20_y0\\train\\apical lesion"
    # folder_c = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_crop_x20_y0\\train\\peri endo"
    # folder_c = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_crop_x20_y0\\valid\\normal"
    # folder_c = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_crop_x20_y0\\valid\\apical lesion"
    # folder_c = "E:\\Lab\\share\\dataset\\two_label_data_forCNN_v24\\origin_crop_x20_y0\\valid\\peri endo"

    if not os.path.exists(folder_c):
        os.makedirs(folder_c)

    # 讀取資料夾 A 中所有 .jpg 檔案
    filenames = [f for f in os.listdir(folder_a) if f.endswith('.jpg')]

    # 將每個檔案名稱進行 split() 操作，取得 "_" 之前的部分
    # filenames = [f.split("_")[0] + ".jpg" for f in filenames]

    # 複製文件到資料夾 C
    copy_files(folder_b, folder_c, filenames)




if __name__ == "__main__":
    main()
