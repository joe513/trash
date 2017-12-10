import os
import shutil

common_directory = 'D:\MAIN_DESK'

first_files_directory = 'D:\Your_Files'
second_files_directory = 'D:\My_Files'


def check(file_directory):
    if os.listdir(file_directory):
        return os.listdir(file_directory)
    else:
        return False


def first_load():
    if not check(second_files_directory):
        if check(first_files_directory):
            if check(common_directory):
                for i in check(common_directory):
                    shutil.move((common_directory + r'\\' + i), second_files_directory)
                for i in check(first_files_directory):
                    shutil.move((first_files_directory + r'\\' + i), common_directory)

    return 'Done'


def second_load():
    if not check(first_files_directory):
        if check(second_files_directory):
            if check(common_directory):
                for i in check(common_directory):
                    shutil.move((common_directory + '\\' + i), first_files_directory)
                for i in check(second_files_directory):
                    shutil.move((second_files_directory + r'\\' + i), common_directory)


    return "Done"


def main():

    wallpapers_dirs = {'first': first_load, 'second': second_load}
    enter = input('Выберите каталог: "first", "second": ')
    try:
        wallpapers_dirs[enter]()
    except:
        main()
    input('Каталог "{}" был успешно загружен!'.format(enter))


main()
