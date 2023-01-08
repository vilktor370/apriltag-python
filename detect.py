import cv2
import numpy as np
from patchify import patchify 
from tag_family import CLASSIC16h5, TAG16h5
def main():
    PATH = "/Users/haochenyu/Desktop/AprilWs/New/apriltag-generation/data/Tag16h5/tag16_05_00000.png"
    # PATH = '/Users/haochenyu/Desktop/AprilWs/New/apriltag-generation/data/TagClassic16h5/tag16_05_00000.png'
    HAMMING_DIS = 5
    gray = cv2.imread(PATH, 0)
    rot1 = cv2.rotate(gray, cv2.ROTATE_90_CLOCKWISE)
    rot2 = cv2.rotate(rot1, cv2.ROTATE_90_CLOCKWISE)
    rot3 = cv2.rotate(rot2, cv2.ROTATE_90_CLOCKWISE)
    
    
    cv2.imshow("image", gray)
    cv2.waitKey(0)
    
    cv2.imshow("image", rot1)
    cv2.waitKey(0)
    
    cv2.imshow("image", rot2)
    cv2.waitKey(0)
    
    cv2.imshow("image", rot3)
    cv2.waitKey(0)
    
    
    

    tag_shape = (6,6)
    
    # 1. binarize
    bin_img = np.zeros(gray.shape)
    bin_img[gray > 127] = 255
    bin_img = bin_img.astype(np.uint8)
    
    # 2. find contour
    contour, _   = cv2.findContours(bin_img, 3, 1)
    
    # 3. classify rectangle
    bbox = cv2.boundingRect(contour[1])
    x,y,w,h = bbox
    resized_tag = bin_img[x:x+w, y:y+h]
    
    # 4. separate resized tag image into smaller patches
    patch = resized_tag.shape[0] // tag_shape[0]
    img_list = patchify(resized_tag, (patch, patch), step=patch)
    
    
    # 5. extract binary string
    blackVal = []
    whiteVal = []
    rows, cols = img_list.shape[:2]
    for i in range(rows):
        for j in range(cols):
            if (i == 0 or i == rows - 1) or (j ==0 or j == cols - 1):
                blackVal.append(img_list[i, j, :, :])
            elif (i == 1 or i == rows - 2) or (j ==1 or j == cols - 2):
                whiteVal.append(img_list[i, j, :, :])
            else:
                continue  
    threshold = (np.array(blackVal).mean() + np.array(whiteVal).mean()) / 2
    print(f"threshold:{threshold}")
    tagCode = 0
    tagCode_str = ""
    for i in range(1, rows-1, 1):
        for j in range(1, cols-1, 1):
            small_img = img_list[i, j, :, :]
            avg_val = small_img.mean()
            tagCode = tagCode << 1
            if avg_val > 127.5:
                tagCode |= 1
    print(f"CSDN:{bin(tagCode)}, {tagCode}")



    cv2.imshow("image", resized_tag)
    cv2.waitKey(0)
    
if __name__ == "__main__":
    main()