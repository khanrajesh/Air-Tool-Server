from inspect import currentframe
import cv2
import os

def extract_image(video_path):
    cam = cv2.VideoCapture(video_path)

    try:
        if not os.path.exists('video_extract'):
            os.makedirs('video_extract')
    except OSError:
        print('Error: Creating directory of images')

    currentframe = 0

    while(True):
        ret,frame = cam.read()
        if ret:
            name = './video_extract/frame_' + str(currentframe)+'.jpg'
            cv2.imwrite(name,frame)
            currentframe += 1
            print('creating..'+name)
        else:
            break
    cam.release()
    cv2.destroyAllWindows()







def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    extract_image('data/video/VID.mp4')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
