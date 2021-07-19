import cv2
import time
import numpy as np

SRC_FILE_NAME = "./img/input.jpg"
TARGET_FILE_NAME = "./img/target.jpg"
OUTPUT_FILE_NAME = "./result/" + str(time.time()) + ".jpg"


def computeMeans(input_img):
    (l, a, b) = cv2.split(input_img)

    lMean = l.mean()
    aMean = a.mean()
    bMean = b.mean()

    output_mean = [lMean, aMean, bMean]
    return output_mean


def computeStd(input_img):
    (l, a, b) = cv2.split(input_img)

    lstd = l.std()
    astd = a.std()
    bstd = b.std()

    output_std = [lstd, astd, bstd]
    return output_std


def computeResult(input_img, src_std, target_std, src_mean, target_mean):

    dataTemp = np.divide(target_std, src_std)
    input_img = input_img - src_mean

    input_img = dataTemp * input_img

    resultImg = input_img + target_mean

    return resultImg


src = cv2.imread(SRC_FILE_NAME)
target = cv2.imread(TARGET_FILE_NAME)

# BGR2Lab
src_lab = cv2.cvtColor(src, cv2.COLOR_BGR2LAB).astype("float32")
target_lab = cv2.cvtColor(target, cv2.COLOR_BGR2LAB).astype("float32")

# computeMeans
src_mean = computeMeans(src_lab)
target_mean = computeMeans(target_lab)

# computeStandardDeviations
src_std = computeStd(src_lab)
target_std = computeStd(target_lab)

# ColorTransfer
resultImg = computeResult(src_lab, src_std, target_std, src_mean, target_mean)
resultImg = np.clip(resultImg, 0, 255)

# Lab2BGR
resultImg = cv2.cvtColor(resultImg.astype("uint8"), cv2.COLOR_LAB2BGR)

cv2.imwrite(OUTPUT_FILE_NAME, resultImg)
cv2.imshow("result", resultImg)

cv2.waitKey(0)
