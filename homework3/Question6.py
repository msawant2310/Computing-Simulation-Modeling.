#Q.6
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('/Users/mrunalisawant/Downloads/20220917_111622.jpg')
plt.imshow(img)
bilateral_img = cv2.bilateralFilter(img, 15, 75, 75)
plt.imshow(bilateral_img)