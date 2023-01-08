import cv2
import numpy as np
import os
def show(img):
    cv2.imshow("image", img)
    cv2.waitKey(0)
    
    
def main():

    PATH = '/Users/haochenyu/Desktop/AprilWs/apriltag-generation/data/Tag16h1_counting'
    OUTPUT = "/Users/haochenyu/Desktop/AprilWs/apriltag-generation/data/Tag16h1_mask"
    gray = (127, 127, 127)
    for i in range(len(os.listdir(PATH))):
        if os.listdir(PATH)[i].endswith("png") and (os.listdir(PATH)[i])[-5].isnumeric():
            img_path = os.path.join(PATH, os.listdir(PATH)[i])
            img = cv2.imread(img_path, 1)
            # roi = cv2.selectROI(img)
            # print(roi)
            roi = (32, 33, 48, 50)
            img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])] = gray
            roi = (78, 75, 46, 48)
            img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])] = gray
            
            
            w,h = img.shape[:2]
            for _ in range(200):
                x = np.random.randint(0, w)
                y = np.random.randint(0, h)
                img[x,y] = (225, 110 ,110)
            output_path = os.path.join(OUTPUT, os.listdir(PATH)[i])
            # cv2.imwrite(output_path, img)
            show(img)
            
    # add noise
    

    # img = cv2.imread("/Users/haochenyu/Desktop/AprilWs/apriltag-generation/data/Tag16h1_counting/tag16_01_00000.png")
    # roi = cv2.selectROI(img)
    # print(roi)
    
    # show(img)
if __name__ == '__main__':
    main()