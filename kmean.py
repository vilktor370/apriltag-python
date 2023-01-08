import cv2
from sklearn.cluster import KMeans
import numpy as np

def main():
    color = cv2.imread("Haochen.jpg", 1)
    bgr = color.reshape((-1, 3)).astype(np.float64)
    model = KMeans(n_clusters= 10)
    result = model.fit(bgr)
    label, center = result.labels_, result.cluster_centers_.astype(np.uint8)
    segmented_data = center[label.flatten()]
    segmented_image = segmented_data.reshape(color.shape)
    cv2.imshow("img", np.hstack([segmented_image, color]))
    cv2.waitKey(0)

if __name__ == '__main__':
    main()