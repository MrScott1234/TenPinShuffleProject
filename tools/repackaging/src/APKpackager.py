import tkinter.filedialog
import tkinter as tk
import shutil
from pathlib import Path

#create and hide the default TK window
root = tk.Tk()
root.withdraw()

#get the directories for the target folder and destination folder
folder_toPackage = tkinter.filedialog.askdirectory()
file_saveAs = tkinter.filedialog.askdirectory()

if folder_toPackage != '' and file_saveAs != '':
    print("Creating archive...")

    try:
        #create the zip archive of the game assets
        shutil.make_archive(file_saveAs+"/10_Pin_Shuffle_base", 'zip', folder_toPackage)
        print("Archive created!")

        print("Creating APK...")
        try:
            #change the file extension from .zip to .apk
            p = Path(file_saveAs+"/10_Pin_Shuffle_base.zip")
            p.rename(p.with_suffix('.apk'))
            print("APK Created!")
        except:
            print("Failed to create APK file!\nTry making sure there isn't an apk file with the same name already there.")

    except:
        print("Failed to create archive!")

else:
    print("Failed! One of the target directories was empty!")
