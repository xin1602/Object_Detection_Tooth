import os


folder_path = "F:\\Lab\\share\\dataset\\two_label_data_combine\\origin"
file_names = os.listdir(folder_path)
file_names.sort(key=lambda x: int(os.path.splitext(x)[0]))


# 將文件名編號為001到410，使用字符串格式化來實現
count = 1
for filename in file_names:
    new_filename = f"{count:03d}.jpg"
    os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
    count += 1



# def rename_files(folder_path):
#     count = 88
#     files = sorted(os.listdir(folder_path))
#     print("Files in folder:", files)  # 打印文件名列表
#     for filename in files:
#         if filename.endswith(".jpg"):
#             new_filename = str(count) + ".jpg"
#             os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
#             count += 1
#             if count > 497:
#                 break

# rename_files(folder_path)

