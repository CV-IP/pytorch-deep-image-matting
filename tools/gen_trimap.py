import cv2
import os
import numpy as np
import random

def main():
    alpha_dir = '/home/liuliang/Desktop/dataset/matting/xuexin/complex_segmentation_deeplabv3'
    sav_dir = '/home/liuliang/Desktop/dataset/matting/xuexin/complex_segmentation_deeplabv3_gentrimap'
    img_ids = os.listdir(alpha_dir)
    print("Images count: {}".format(len(img_ids)))
    for img_id in img_ids:
        alpha = cv2.imread(os.path.join(alpha_dir, img_id), 0)

        #k_size = random.choice(range(20, 40))
        k_size = 3
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (k_size, k_size))
        dilated = cv2.dilate(alpha, kernel, iterations=10)
        #eroded = cv2.erode(alpha, kernel)

        trimap = np.zeros(alpha.shape)
        trimap.fill(128)
        trimap[alpha >= 255] = 255 
        trimap[dilated <= 0] = 0 

        save_name = os.path.join(sav_dir, img_id)
        print("Write to {}".format(save_name))
        cv2.imwrite(save_name, trimap)

if __name__ == "__main__":
    main()


