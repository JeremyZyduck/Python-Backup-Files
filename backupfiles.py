import os
import zipfile
import shutil

def Compress_Files(source_folder, target_zip):
    zipped = zipfile.ZipFile(target_zip, 'w')
    for subdir, dirs, files in os.walk(source_folder):
        for file in files:
            zipped.write(os.path.join(subdir, file))
    zipped.close()

def Copy_Files(source_folder, target_folder):
    for subdir, dirs, files in os.walk(source_folder):
        for file in files:
            shutil.copy(os.path.join(subdir, file), target_folder)

if __name__ == "__main__":
    choice = input("Enter 'Z' to zip and 'C' to copy\n > ")

    if choice.lower() == 'z':
        print ("Compressing files...")
        #Compresses files in source folder to target zip file
        source_folder = "F:\\Important Files\\Important Files"
        target_zip = "D:\\Backup\\Backup.zip"
        Compress_Files(source_folder, target_zip)
    elif choice.lower() == 'c':
        print ("Copying files...")
        #Copies files in source folder to target folder
        source_folder = "F:\\Important Files\\Important Files"
        target_folder = "D:\\Backup"
        Copy_Files(source_folder, target_folder)
    else:
        print("Invalid input")
        exit()

    print ("Completed.")
    exit()