import numpy as np
import cv2
def alignChannels(red, green, blue):
    r_g_x, r_g_y = compare(red, green)
    r_b_x, r_b_y = compare(red, blue)
    return -r_b_x, -r_b_y, -r_g_x, -r_g_y


def cal_SSD(x, y, num_pixel):
    dist = np.linalg.norm(x - y)/num_pixel
    return dist

def compare(x_old, y_old):
    dist = 10000
    x_trans = 0
    y_trans = 0
    for i in range(-30, 30):
        for j in range(-30, 30):
            if(i<=0 & j<=0):
                x_new = x_old[0:(810 - abs(i)), 0:(943-abs(j))]
                y_new = y_old[abs(i):810, abs(j):943]
            elif (i <= 0 & j > 0):
                x_new = x_old[0:(810 + i), j:943]
                y_new = y_old[abs(i):810, 0:(943 - j)]
            elif (i > 0 & j <= 0):
                x_new = x_old[i:810, 0:(943 - abs(j))]
                y_new = y_old[0:(810 - i), abs(j):943]
            else:
                x_new = x_old[i:810, j:943]
                y_new = y_old[0:(810 - i), 0:(943 - j)]

            num_pixel = (810 - np.abs(i)) * (943 - np.abs(j))

            dist1 = cal_SSD(x_new, y_new, num_pixel)
            if(dist1<dist):
                x_trans = i
                y_trans = j
                dist = dist1
    return x_trans, y_trans

