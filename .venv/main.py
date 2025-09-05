import cv2
import os

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

imgBackground = cv2.imread('Resources/background.png')
#importing the mode images into a list
folderModePath = 'Resources/Modes'
modePathList = sorted(os.listdir(folderModePath))
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))
#print(len(imgModeList))

while True:
    success, img = cap.read()

    img_resized = cv2.resize(img, (640, 480))

    imgBackground[162:162+480, 55:55+640] = img_resized
    imgBackground[44:44+633, 808:808+414] = imgModeList[0]

    # cv2.imshow("Webcam", img_resized)
    cv2.imshow("Background", imgBackground)
    cv2.waitKey(1)
