import cv2
import numpy as np
from patchify import patchify 

def show(img):
    cv2.imshow("image", img)
    cv2.waitKey(0)

def main():
    PATH = '/Users/haochenyu/Desktop/AprilWs/apriltag-generation/data/Tag16h1_counting/tag16_01_00000.png'
    gray = cv2.imread(PATH, 0)
    color = cv2.imread(PATH, 1)
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
    resized_tag = bin_img[x+1:x+w-1, y+1:y+h-1]
    
    # 4. mask portion of the tag
    mask = np.zeros(resized_tag.shape)
    half_height,half_width = mask.shape[0] // 2, mask.shape[1] // 2
    mask[half_height//2:half_height, :] = -255
    
    final = resized_tag + mask
    
    
    ring_x, ring_y = (gray.shape[0] - final.shape[0]) //2, (gray.shape[1] - final.shape[1]) //2

    color[ring_x: -ring_x, ring_y: -ring_y, 0] = final
    color[ring_x: -ring_x, ring_y: -ring_y, 1] = final
    color[ring_x: -ring_x, ring_y: -ring_y, 2] = final
    
    
    # cv2.imwrite("mased_tag.png", color)
    show(color)
if __name__ == '__main__':
    main()
    
# 0b 1001 0000 0010 1011
