import cv2
import numpy as np
import matplotlib
from math import sqrt, log, exp


def img_write(img):
    cv2.imwrite("result.jpg", img)


def show_wait(img, delay):
    cv2.imshow("image", img)
    cv2.waitKey(delay)


def img_divide(img, size):
    """Divide an image into images blocks of 'size' pixels each
    :rtype : nd array
    """
    for column in range(0, img.shape[0], size):
        height = column+size
        for row in range(0, img.shape[1], size):
            width = row+size
            img[column:height, row:width] = img_adaptive_otsu(img[column:height, row:width])
    return img


# def nd_array_value_replace(block, value):
#     for ind1, value1 in enumerate(block):
#         for ind2, value2 in enumerate(value1):
#             block[ind1][ind2] = value
#     return block


def img_adaptive_otsu(block):
    # print type(block)
    """This is where the adaptive threshold implementation occurs based on local otsu threshold value for each block """
    # standard defined
    set_mean = 90
    set_sd = 20
    mean_block = np.mean(block)
    sd_block = np.std(block)
    if sd_block > set_sd:
        ret, block = cv2.threshold(block, 0, 255, cv2.THRESH_OTSU)
    elif sd_block < set_sd:
        if mean_block > set_mean:
            block[:] = 255
        else:
            block[:] = 0
    return block


