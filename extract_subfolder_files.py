'''
 Function :
     1. move files in sub-folders to current folder
         - default move all file
         - use 'end_str' as file filter
     2. try to delete sub-folders
'''
from os import getcwd, rmdir, walk
from os.path import  join, exists, splitext
from shutil import move

def rename_file(dst_path, base_name):
    head, tail = splitext(base_name)   
    count = 0     
    dst_file = join(dst_path, base_name)
    #
    while exists(dst_file):
        count += 1
        dst_file = join(dst_path, '%s-%d%s' % (head, count, tail))
    #print('Renaming %s to %s' % (src_file, dst_file))
    #
    return dst_file


def extract_all_files(working_path, end_str='', overwrite=True):
    for root, dirs, files in walk(working_path, topdown=False):
        if root != working_path:
            #print("current root：", root)
            if files:
                for f in files:
                    if f.endswith(end_str):
                        src_file = join(root, f)
                        dst_file = join(working_path, f)
                        
                        if not overwrite:
                            dst_file = rename_file(working_path, f)

                        print("move file: " + src_file)
                        move(src_file, dst_file)
            else:
                pass
            print('remove foder: ' + root)
            try:
                rmdir(root)
            except OSError as e:
                print(e)
    print("Done")


def main():
    default_path = getcwd()
    print('woring folder: ' + default_path)
    # call example 1
    extract_all_files(default_path)
    # call example 2
    #extract_all_files(default_path, end_str='.txt', , overwrite=False)

if __name__ == '__main__':
    main()
