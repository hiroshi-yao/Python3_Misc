'''
 Function :
     1. move all files in sub-folders to current folder
     2. than delete sub-folders

'''
from os import chdir, getcwd, listdir, rmdir, walk
from os.path import isfile, isdir, join
from shutil import move


def extract_all_files(mypath):
    print('woring folder: ' + mypath)
    for root, dirs, files in walk(mypath,topdown=False):
        if root != mypath:
            #print("current root：", root)
            if files:
                for f in files:
                    file_path = join(root, f)
                    print("move file: " + file_path)
                    move(file_path, join(mypath, f))
            else:
                pass
            print('remove empty foder: ' + root)
            rmdir(root)
    print("Done")


def main():
    default_path = getcwd()
    extract_all_files(default_path)

if __name__ == '__main__':
    main()
