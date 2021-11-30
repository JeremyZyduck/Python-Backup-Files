import os
import zipfile
import shutil
import hashlib

def compress_files(source_folder, target_zip):
    zipped = zipfile.ZipFile(target_zip, 'w')
    for subdir, files in os.walk(source_folder):
        for file in files:
            zipped.write(os.path.join(subdir, file))
    zipped.close()

def copy_files(source_folder, target_folder):
    for subdir, files in os.walk(source_folder):
        for file in files:
            shutil.copy(os.path.join(subdir, file), target_folder)

def md5_check(file_name):
    with open(file_name, 'rb') as file_to_check:
        # read contents of the file
        data = file_to_check.read()
        # pipe contents of the file through
        md5_returned = hashlib.md5(data).hexdigest()
    return md5_returned

#check md5 of all files in target folder, replace with source files if different
def md5_check_folder(source_folder, target_folder):
    for subdir, files in os.walk(target_folder):
        for file in files:
            if md5_check(os.path.join(subdir, file)) != md5_check(os.path.join(source_folder, file)):
                shutil.copy(os.path.join(source_folder, file), target_folder)


if __name__ == "__main__":
    choice = input("'Z' to zip\n'C' to copy\n'H' to check hash\n > ")

    if choice.lower() == 'z':
        print ("Compressing files...")
        #Compresses files in source folder to target zip file
        source_folder = "F:\\Important Files\\Important Files"
        target_zip = "D:\\Backup\\Backup.zip"
        compress_files(source_folder, target_zip)
    elif choice.lower() == 'c':
        print ("Copying files...")
        #Copies files in source folder to target folder
        source_folder = "F:\\Important Files\\Important Files"
        target_folder = "D:\\Backup"
        copy_files(source_folder, target_folder)
    else:
        print("Invalid input")
        exit()

    print ("Completed.")
    exit()