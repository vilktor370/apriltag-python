import cv2
import numpy as np
def show(img):
    cv2.imshow("image", img)
    cv2.waitKey(0)
    
    
def main():
    # img = cv2.imread('/Users/haochenyu/Desktop/AprilWs/apriltag-generation/data/Tag16h1_counting/tag16_01_00001.png', 1)
    img = cv2.imread("masked_tag.png")
    roi = cv2.selectROI(img)
    print(roi)
    # roi = (34, 36, 51, 87)
    img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])] = (255,255,255)
    cv2.imwrite("masked_tag.png", img)

        
    
    # show(img)
if __name__ == '__main__':
    main()