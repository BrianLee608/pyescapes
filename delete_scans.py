# Whenever you create DIO files, it makes those extraneous DIO_1_..._-1_CH0
# files. This script will recursively look in all of the files of root_dir
# and removes all those extraneous files.

import datetime
import os


root_dir = 'C:\\Users\\mroesch\\Desktop\\SaGT_Chemo_Stage'
log_file = 'C:\\Users\\mroesch\\Desktop\\SaGT_Chemo_Stage\\delete_scans_log.txt'
time = datetime.datetime.today()

with open(log_file, 'a') as log:

    for dirpath, dirnames, filenames in os.walk(root_dir):
        if 'DIO_1_SCAN_000000-1_CH0' in filenames:
            os.remove(dirpath + '\\DIO_1_SCAN_000000-1_CH0')
            log.write(str(time) + ' -> DELETED: ' + dirpath + '\\DIO_1_SCAN_000000-1_CH0\n')
        if 'DIO_1_SCAN_000000-1_CH0.txt' in filenames:
            os.remove(dirpath + '\\DIO_1_SCAN_000000-1_CH0.txt')
            log.write(str(time) + ' -> DELETED: ' + dirpath + '\\DIO_1_SCAN_000000-1_CH0.txt\n')
        if 'DIO_1_SCAN_000000-1_CH0_COLOR.txt' in filenames:
            os.remove(dirpath + '\\DIO_1_SCAN_000000-1_CH0_COLOR.txt')
            log.write(str(time) + ' -> DELETED: ' + dirpath + '\\DIO_1_SCAN_000000-1_CH0_COLOR.txt\n')
