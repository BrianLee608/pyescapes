import os

root_dir = 'C:\\Users\\mroesch\\Desktop\\py_csv\\'
log_file = 'C:\\Users\\mroesch\\Desktop\\py_csv\\pad_zeros_log.txt'

processed = set()

with open(log_file, 'a+') as log:

    # get the files that have already been processed so
    # we don't process them redundantly
    for p in log:
        f = p.rstrip()
        if f not in processed:
            processed.add(f)

    all_files = os.listdir(root_dir)

    for f in all_files:
        # startswith will depend on the experiment
        if f.startswith('GS') and f.endswith('.txt') and f not in processed:
            print(f)
            f2 = f[:-4] + '_truncated.txt'
            
            with open(root_dir + f) as input_file:
                data = [[item.strip() or '0' for item in line.split('\t')]
                                             for line in input_file]

                # delete lines that are only zeroes in the end
                while set(data[-1]) == {'0'}:
                    del data[-1]

                # write truncated data to a new file
                with open(root_dir + f2, 'wt') as output_file:
                    output_file.writelines('\t'.join(line) + '\n' for line in data) 

            # delete old file. then rename truncated file with old file
            os.remove(root_dir + f)
            os.rename(root_dir + f2, root_dir + f)
            processed.add(f)
            log.write(f + '\n')


raw_input("Press ENTER to exit")
            

