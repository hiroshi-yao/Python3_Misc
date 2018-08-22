'''
 Function :
     1. move files in sub-folders to current folder
         - default move all file
         - use 'end_str' as file filter
     2. try to delete sub-folders
'''
from os import chdir, getcwd, listdir, rmdir, walk
from os.path import isfile, isdir, join
from shutil import move


def extract_all_files(mypath, end_str=''):
    print('woring folder: ' + mypath)
    for root, dirs, files in walk(mypath,topdown=False):
        if root != mypath:
            #print("current root：", root)
            if files:
                for f in files:
                    if f.endswith(end_str):
                        file_path = join(root, f)
                        print("move file: " + file_path)
                        move(file_path, join(mypath, f))
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
    # call example 1
    #extract_all_files(default_path)
    # call example 2
    #extract_all_files(default_path, end_str='.txt')


if __name__ == '__main__':
    main()
