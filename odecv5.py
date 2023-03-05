import cv2
import torch
import glob
import numpy as np
from matplotlib import pyplot as plt
import sys
from pprint import pprint
class Odec:

    def __init__(self,model_path:str = 'odec/best_x_380_hyp_16_10.pt',model_conf:int=0.5,target_cam:int = 0):
        self.model_path:str = model_path
        self.target_cam:int = target_cam
        self.win_name:int = 'ODEC'
        self.model_conf:int = model_conf
        model = torch.hub.load('odec','custom', source='local', path=self.model_path, force_reload=True)
        model.conf = self.model_conf
        self.model = model


    def detect_by_cam(self):
        model = torch.hub.load('odec','custom', source='local', path=self.model_path, force_reload=True)
        print('starting camera .....')
        cap = cv2.VideoCapture(self.target_cam)
        while cap.isOpened():
            ret,frame = cap.read()
            result = model(frame)
            print('result: ')
            print(result)
            cv2.imshow(self.win_name,np.squeeze(result.render()))
           

        cv2.waitKey(0)
        close_cam()

        def close_cam():
            cap.release()
            cv2.destroyAllWindows()



    def detect_by_capture_image(self, frame):
        # model = torch.hub.load('odec','custom', source='local', path=self.model_path, force_reload=True)
        # print("Please wait, Processing ...")
        # cap = cv2.VideoCapture(self.target_cam)
        # ret,frame = cap.read()
        result = self.model(frame)
        # cap.release()
        # cv2.imshow(self.win_name,np.squeeze(result.render()))

        # print("Printing result vars")
        # pprint(vars(result))

        missing_count = result.xyxyn[0].size(dim=0)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        return missing_count



    def detect_by_image(self,image_path:str):
        print("Please wait, Processing ...")
        image = glob.glob(image_path)
        result = self.model(image)      
        missing_count = result.xyxyn[0].size(dim=0)
        return missing_count
        # while True:
        #     img = np.squeeze(result.render())
        #     res = cv2.resize(img, dsize=(900,900), interpolation=cv2.INTER_CUBIC)
        #     cv2.namedWindow(self.win_name, cv2.WINDOW_NORMAL)
        #     cv2.imshow(self.win_name, res)
        #     print('result: ')
        #     pprint(vars(result))
        #     breakpoint()
        #     cv2.waitKey(0)
        #     sys.exit()
        # cv2.destroyAllWindows()



    def detect_by_video(self,video_path:str):
        #not completed yet
        # model = torch.hub.load('odec','custom', source='local', path=self.model_path, force_reload=True)
        cap = cv2.VideoCapture(video_path)
        print("Please wait, Processing ...")
        while cap.isOpened():
            ret,frame = cap.read()

            if ret == True:
                result = self.model(frame)
                cv2.imshow(self.win_name,np.squeeze(result.render()))
                print(result)
                cv2.waitKey(0)            
        close_cam()

        def close_cam():
            cap.release()
            cv2.destroyAllWindows()

    def detectByUrl(self,imageUrl:str):
        # image = glob.glob(imageUrl)
        result = self.model(imageUrl)      
        missing_count = result.xyxyn[0].size(dim=0)
        return missing_count

    def detectByUploadImage(self,image:str):
        print("Please wait, Processing ...")
        # image = glob.glob(image_path)
        result = self.model(image)      
        missing_count = result.xyxyn[0].size(dim=0)
        return missing_count

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # detect_by_image('odec/best_x_300_hyp_27_9.pt','test_data/t2.jpg')
    od = Odec()
    od.detectByUrl('https://firebasestorage.googleapis.com/v0/b/doro-phoenix.appspot.com/o/kitten.jpg?alt=media&token=79a0dc78-1a5c-4ce8-9e22-848094bc814d')



# #AI coordinator
# class_name_count = 'cars'
# l = s[1:s.find(class_name_count)].split()[-1]
# if class_name_count in s:
#     print(1,class_name_count)
#     cv2.rectangle(im0, (0, 0), (1100, 250), (0,0,0), -1)
#     cv2.putText(im0,l + class_name_count,(0,200), cv2.FONT_HERSHEY_SIMPLEX, 8, (255,255,255), 24,cv2.LINE_AA)