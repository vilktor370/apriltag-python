import numpy as np
import cv2
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

masks = generate_mask(n=6)
img = np.zeros((6, 6, 3))
for i in masks:
    img[i] = (127, 127, 127)
    cv2.imshow("img", img)
    cv2.waitKey(0)