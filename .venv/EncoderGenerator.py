import cv2
import face_recognition
import pickle
import os
#importing student images
folderPath = 'Images'
pathList = sorted(os.listdir(folderPath))
imgList = []
studentIDs = []
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIDs.append(os.path.splitext(path)[0])
print(studentIDs)

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
print('Encoding Started...')
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIDs = [encodeListKnown, studentIDs]
print('Encoding Complete')
file = open('EncodeFile.p', 'wb')
pickle.dump(encodeListKnownWithIDs, file)
file.close()
print("File Saved")


