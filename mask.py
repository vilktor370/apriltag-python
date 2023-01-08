import cv2
import numpy as np
import os
def show(img):
    cv2.imshow("image", img)
    cv2.waitKey(0)
    
def generate_mask(n = 6):
    tq = np.arange(-n/2 + 1,n/2+1); xq,yq = np.meshgrid(tq,tq); 

    # The centers are produced by:
    tc = np.arange(-(n-1)/2,(n-1)/2+1); xc,yc = np.meshgrid(tc,tc); z = xc + 1j*yc

    # The mask corners for e.g. the right side are:
    q_rt = tq.max()+1j*tq

    # The masks are:
    m_rt = [ (z/qk).real >= 0 for qk in q_rt ]

    rot1 = [np.rot90(i) for i in m_rt]
    rot2 = [np.rot90(i) for i in rot1]
    rot3 = [np.rot90(i) for i in rot2]
    masks = m_rt + rot1 + rot2 + rot3
    return masks


def main():

    PATH = '/Users/haochenyu/Desktop/AprilWs/apriltag-generation/data/Tag16h1_counting'
    OUTPUT = "/Users/haochenyu/Desktop/AprilWs/apriltag-generation/data/Tag16h1_big_mask"
    gray = (127, 127, 127)
    masks = generate_mask(n = 120)
    for i in range(len(os.listdir(PATH))):
        file_path = os.listdir(PATH)[i]
        if file_path.endswith("png") and (file_path)[-5].isnumeric():
            img_path = os.path.join(PATH, file_path)
            img = cv2.imread(img_path, 1)
            # roi = cv2.selectROI(img)
            # print(roi)
            # roi = (32, 33, 48, 50)
            # img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])] = gray
            # roi = (78, 75, 46, 48)
            # img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])] = gray
            w,h = img.shape[:2]
            resized_img = img[:][20:w-20, 20:h-20]
            for j in range(len(masks)):
                resized_img[masks[j]] = gray
                img[20:w-20, 20:h-20] = resized_img
                img[:21, :21] = (255,255,255)
                img[w-20:, h-20:] = (255,255,255)
                for _ in range(200):
                    x = np.random.randint(0, w)
                    y = np.random.randint(0, h)
                    img[x,y] = (225, 110 ,110)
                output = os.path.join(OUTPUT, file_path[:-4] + f"_{j}.png")
                cv2.imwrite(output, img)
                # show(img)
            
    # add noise
    

    # img = cv2.imread("/Users/haochenyu/Desktop/AprilWs/apriltag-generation/data/Tag16h1_counting/tag16_01_00000.png")
    # roi = cv2.selectROI(img)
    # print(roi)
    
    # show(img)
if __name__ == '__main__':
    main()