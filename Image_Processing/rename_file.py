import os

def rename_files(folder_path):
    count = 1
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg"):
            new_filename = str(count) + ".jpg"
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
            count += 1
            if count > 150:
                break

folder_path = "F:\\Lab\\share\\dataset\\tooth_data_v1\\origin"
rename_files(folder_path)
