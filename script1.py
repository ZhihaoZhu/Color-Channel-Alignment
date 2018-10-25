from alignChannels import alignChannels
# Problem 1: Image Alignment
import numpy as np
import matplotlib.pyplot as plt
import cv2
# 1. Load images (all 3 channels)
red = np.load( "./data/red.npy" )
blue = np.load( "./data/blue.npy" )
green = np.load( "./data/green.npy" )


# 810 943
# numpy.ndarry
width = red.shape[0]
height = red.shape[1]

# 2. Find best alignment
r_g_x, r_g_y, r_b_x, r_b_y = alignChannels(red, green, blue)


blank_image = 255*np.ones((width+60,height+60,3), np.uint8)
blank_image[30:width+30, 30:height+30, 0] = red
blank_image[30+r_g_x:width+30+r_g_x, 30+r_g_y:height+30+r_g_y, 1] = green
blank_image[30+r_b_x:width+30+r_b_x, 30+r_b_y:height+30+r_b_y, 2] = blue

plt.imshow(blank_image)
plt.savefig('./rgb_output.jpg')

plt.show()


# 3. save result to rgb_output.jpg (IN THE "results" FOLDER)
