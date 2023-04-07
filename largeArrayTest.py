import numpy as np
import os
import cv2
import matplotlib.pyplot as plt
def load_tif(path):
    tif = []
    for filename in os.listdir(path):
        #check if file is image, and digit in filename
        if (filename.endswith(".tif") or filename.endswith(".png")) and any(char.isdigit() for char in filename):
            tif.append(path+"/"+filename)

    #sort the list by the number in the filename
    tif.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
    return tif

basePath = "../slices"
tifs = load_tif(basePath)
#imread first slice to get dimensions
firstSlice = cv2.imread(tifs[0], cv2.IMREAD_GRAYSCALE)

#get type of first slice
dtype = firstSlice.dtype
bigArrShape = (len(tifs), firstSlice.shape[0], firstSlice.shape[1])

bigArr = np.memmap("bigArr.dat", dtype=dtype, mode="r", shape=bigArrShape)

plt.imshow(bigArr[2000], cmap="gray")
plt.show()
#works!