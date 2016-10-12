# Whenever you create DIO files, it makes those extraneous DIO_..._..._-1_CH0
# files. This script will recursively look in all of the files of root_dir
# and removes all those extraneous files.


# Deletes files in the following format
# DIO_1_SCAN_000000-1_CH0
# DIO_2_SCAN_000000-1_CH0.txt
# DIO_3_SCAN_000000-1_CH0.COLOR.txt

import datetime
import os
import re

root_dir = 'C:\\Users\\mroesch\\Desktop\\SaGT_Chemo_Stage'
log_file = 'C:\\Users\\mroesch\\Desktop\\SaGT_Chemo_Stage\\delete_scans_log.txt'
time = datetime.datetime.today()

with open(log_file, 'a') as log:

    for dirpath, dirnames, filenames in os.walk(root_dir):

        # remove at most 2 files in any folder
        removed = 0
        
        for f in filenames:
            if removed == 2:
                break
            m = re.match(r'[\w]*SCAN_000000-\d{1,2}_CH0[\w.]*', f)
            if m:
                removed += 1
                os.remove(dirpath + '\\' + m.group())
                log.write(str(time) + ' -> DELETED: ' + dirpath + '\\' + m.group() + '\n')
                

