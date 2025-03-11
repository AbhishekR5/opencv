# Import Libraries
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from zipfile import ZipFile
from urllib.request import urlretrieve
from IPython.display import Image
%matplotlib inline

def download_and_unzip(url,save_path):
  print(f"downloading and unzipping assets",end="")

  urlretrieve(url,save_path)

  try:
    with ZipFile(save_path) as z:
      z.extractall(os.path.split(save_path)[0])

    print("done")

  except Exception as e:
    print("\n invalid file.",e)


cb_img = cv2.imread("checkerboard_18x18.png",0)

print("Image size (H, W) is:", cb_img.shape)
print("Data type of image is:", cb_img.dtype)

plt.imshow(cb_img)
plt.imshow(cb_img, cmap="gray")


coke_img=cv2.imread("coca-cola-logo.png", 1)
print("Image size (h,w,c) is: ",coke_img.shape)
print("Datatypes of image s:",coke_img.dtype)

coke_img_channels_reversed = coke_img[:, :, ::-1]
plt.imshow(coke_img_channels_reversed)

### Splitting and Merging Color Channels
img_nz_bgr=cv2.imread("New_Zealand_Lake.jpg",cv2.IMREAD_COLOR)
b,g,r=cv2.split(img_nz_bgr)

plt.figure(figsize=[20,5])

plt.subplot(141);plt.imshow(r,cmap="gray");plt.title("red channel")
plt.subplot(142);plt.imshow(g,cmap="gray");plt.title("Green channel")
plt.subplot(143);plt.imshow(b,cmap="gray");plt.title("Blue channel")
plt.subplot(144);plt.imshow(img_merged[:,:,::-1]);plt.title("merged RGB output")


## Changing from BGR to RGB
img_nz_bgr = cv2.cvtColor(img_nz_bgr, cv2.COLOR_BGR2RGB)
plt.imshow(img_nz_bgr)

## Changing to HSV color space
img_hsv = cv2.cvtColor(img_nz_bgr, cv2.COLOR_BGR2HSV)

# Split the image into the B,G,R components
h,s,v = cv2.split(img_hsv)

# Show the channels
plt.figure(figsize=[20,5])
plt.subplot(141);plt.imshow(h, cmap="gray");plt.title("H Channel");
plt.subplot(142);plt.imshow(s, cmap="gray");plt.title("S Channel");
plt.subplot(143);plt.imshow(v, cmap="gray");plt.title("V Channel");
plt.subplot(144);plt.imshow(img_nz_bgr);   plt.title("Original");

## Modifying individual Channel
h_new = h + 10
img_NZ_merged = cv2.merge((h_new, s, v))
img_NZ_rgb = cv2.cvtColor(img_NZ_merged, cv2.COLOR_HSV2RGB)

plt.figure(figsize=[20,5])
plt.subplot(141);plt.imshow(h, cmap="gray");plt.title("H Channel");
plt.subplot(142);plt.imshow(s, cmap="gray");plt.title("S Channel");
plt.subplot(143);plt.imshow(v, cmap="gray");plt.title("V Channel");
plt.subplot(144);plt.imshow(img_nz_bgr);   plt.title("Original");

## Saving Images
cv2.imwrite("New_Zealand_Lake_SAVED.png", img_nz_bgr)
Image(filename='New_Zealand_Lake_SAVED.png') 

img_NZ_bgr = cv2.imread("New_Zealand_Lake_SAVED.png", cv2.IMREAD_COLOR)
print("img_NZ_bgr shape (H, W, C) is:", img_NZ_bgr.shape)

# read the image as Grayscaled
img_NZ_gry = cv2.imread("New_Zealand_Lake_SAVED.png", cv2.IMREAD_GRAYSCALE)
print("img_NZ_gry shape (H, W) is:", img_NZ_gry.shape)
