import time
import os.path
from os import path
import datetime
import shutil
import glob

Start_Time = time.time()
# Filename and placement on converting csv file
convert_csv = '/home/rune/Dokumenter/import/XRoads.csv'

# import csv catalog file
road_connect = []
with open(convert_csv, encoding='utf-8') as s:
    road_connect = s.readlines()
    s.close()
count = 0


def copy_file():
    shutil.copy2(filename1, file_out1)
    shutil.copy2(filename2, file_out2)
    file_out1_t1 = ("Copied file to: ", file_out1, "\n")
    file_out2_t2 = ("Copied file to: ", file_out2, "\n")
    XTX.writelines(file_out1_t1)
    XTX.writelines(file_out2_t2)
    return


def move_old():
    test_catalog = (one_drive + data_a1 + "/")
    dmi = "*"
    old_file_name_1 = (one_drive + data_a1 + "/" + data_a4 + "_" + dmi + ".dmi")
    old_file_name_2 = (one_drive + data_a1 + "/" + data_a4 + "_" + dmi + ".dmr")
    destination_onedrive_1 = (one_drive + data_a1 + "/old/")
    destination_onedrive_2 = (one_drive + data_a1 + "/old/")
    if not os.listdir(test_catalog):
        return
    else:
        if path.isfile(file_onedrive_1):
            return
        else:
            old_file_name_1a = glob.glob(old_file_name_1)
            old_file_name_1a = ''.join(old_file_name_1a)
            if old_file_name_1a == '':
                return
            if not path.isdir(one_drive + data_a1 + "/old"):
                os.makedirs(one_drive + data_a1 + "/old")
            shutil.move(old_file_name_1a, destination_onedrive_1)
            old_file_name_2a = glob.glob(old_file_name_2)
            old_file_name_2a = ''.join(old_file_name_2a)
            shutil.move(old_file_name_2a, destination_onedrive_2)


def robo_copy():
    shutil.copy2(file_out1, file_onedrive_1)
    shutil.copy2(file_out2, file_onedrive_2)
    file_onedrive_1t = ("Copied file to: ", file_onedrive_1, "\n")
    file_onedrive_2t = ("Copied file to: ", file_onedrive_2, "\n")
    XTX.writelines(file_onedrive_1t)
    XTX.writelines(file_onedrive_2t)
    return


# Prosjekt places
project_folder = '/home/rune/Dokumenter/Qg4/'  # folder of quadri base
# Copy to Onedrive
one_drive = '/home/rune/Dokumenter/onedrive/'
temp_folder = '/home/rune/Dokumenter/TEMP/'
file_Log = (temp_folder + "logfile " + time.strftime("%Y%m%d") + ".log")

if not path.isdir(temp_folder):
    os.makedirs(temp_folder)

with open(file_Log, "w") as XTX:
    for fileconvert in road_connect:
        data_y = road_connect[count]
        splitting = data_y.split(',')
        data_a1 = splitting[0]
        data_a2 = splitting[1]
        data_a3 = splitting[2]
        data_a4 = splitting[3]
        data_a4 = data_a4.strip("\n")
        data_a1 = data_a1.replace('"', '')
        data_a2 = data_a2.replace('"', '')
        data_a3 = data_a3.replace('"', '')
        data_a4 = data_a4.replace('"', '')

        file_in = data_a3
        file_ut = data_a4
        folder_ut = temp_folder + data_a1 + "/"
        partial_folder = data_a2

        filename1 = (project_folder + partial_folder + file_in + ".dmi")
        filename2 = (project_folder + partial_folder + file_in + ".dmr")
        if not path.isfile(filename1):
            file_out_1t = "Did not find file: ", filename1, "\n"
            file_out_2t = "Did not find file: ", filename2, "\n"
            XTX.writelines(file_out_1t)
            if not path.isfile(filename2):
                XTX.writelines(file_out_2t)
        else:
            t = os.path.getmtime(filename1)
            v = datetime.datetime.fromtimestamp(t)
            x = v.strftime('%Y%m%d')
            file_out1 = (folder_ut + data_a4 + "_" + x + ".dmi")
            file_out2 = (folder_ut + data_a4 + "_" + x + ".dmr")
            file_onedrive_1 = (one_drive + data_a1 + "/" + data_a4 + "_" + x + ".dmi")
            file_onedrive_2 = (one_drive + data_a1 + "/" + data_a4 + "_" + x + ".dmr")

            if not path.isdir(folder_ut):
                os.makedirs(folder_ut)

            if not path.isdir(one_drive + data_a1):
                os.makedirs(one_drive + data_a1)

            if not path.isfile(file_onedrive_1):
                copy_file()
                move_old()
                robo_copy()
        count = (count + 1)


XTX.close()
End_Time = (time.time() - Start_Time)
End_Time = round(End_Time, 2)
print(End_Time, "sek")
