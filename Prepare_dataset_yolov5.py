import streamlit as st
import tkinter as tk
from tkinter import filedialog
import os
import shutil
root = tk.Tk()
root.withdraw()
root.wm_attributes('-topmost', 1)
st.title('Folder Picker')
st.write('Please select a folder:')
clicked = st.button('Folder Picker for Train Valid Split')

if clicked:
    dirname = st.text_input('Selected folder:', filedialog.askdirectory(master=root))
    path = str(dirname)
    maindir = os.listdir(dirname)
    j = 0
    try:
        os.mkdir('coco')
    except Exception as FileExistsError:
        st.write("There is already a prepared dataset of a folder named Coco in present in this folder")
        pass
    try:

        os.mkdir('coco/images/')
    except:
        pass
    try:

        os.mkdir('coco/labels/')
    except:
        pass
    try:
        os.mkdir('coco/labels/Valid/')
    except:
        pass
    try:
        os.mkdir('coco/labels/Train/')
    except:
        pass
    try:
        os.mkdir('coco/images/Train/')
    except:
        pass
    try:
        os.mkdir('coco/images/Valid/')
    except:
        pass

    for i in maindir:
        OriginalName = os.path.splitext(i)[0]
        extensionsss = os.path.splitext(i)[1]

        if(extensionsss == '.jpg' or extensionsss == '.png'):
            print(OriginalName+extensionsss)
            try:
                if(j%5):
                    shutil.copy2(f'{dirname}/{OriginalName+extensionsss}',f'coco/images/Train/{OriginalName+extensionsss}')
                    shutil.copy2(f'{dirname}/{OriginalName}.txt',f'coco/labels/Train/{OriginalName}.txt')
                else:
                    shutil.copy2(f'{dirname}/{OriginalName+extensionsss}',f'coco/images/Valid/{OriginalName+extensionsss}')
                    shutil.copy2(f'{dirname}/{OriginalName}.txt',f'coco/labels/Valid/{OriginalName}.txt')
            except:
                pass
        else:
            pass

        j+=1
