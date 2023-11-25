import cv2
grey_1=cv2.cvtColor(cv2.imread("1.jpg"),cv2.COLOR_BGR2GRAY)
grey_2=cv2.cvtColor(cv2.imread("2.jpg"),cv2.COLOR_BGR2GRAY)
cv2.imwrite("grey1.jpg",grey_1)
cv2.imwrite("grey2.jpg",grey_2)
from deepface import DeepFace
for i in range(100):
    k=DeepFace.verify(img1_path="grey1.jpg",img2_path="grey2.jpg",enforce_detection=False)
    print(k)