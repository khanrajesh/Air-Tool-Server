
#python -m pip install lxml
#python -m pip install PyQt5
#cd labelImg
#pyrcc5 -o libs/resources.py resources.qrc
#python labelImg.py

import os 


def launch_labelImg():
    cwd = os.getcwd() 
    print("Current working directory:", cwd) 
    os.system('cmd /k "venv/Scripts/activate & cd labelImg & python labelImg.py"') 


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    launch_labelImg()
   