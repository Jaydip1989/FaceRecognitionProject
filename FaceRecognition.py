import cv2
import face_recognition


img = cv2.imread('lionel-messi.jpeg')
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding = face_recognition.face_encodings(rgb_img)[0]

img2 = cv2.imread('images/Elon Musk.jpeg')
rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]


img3 = cv2.imread('images/Dwayne_Johnson.jpeg')
rgb_img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
img_encoding3 = face_recognition.face_encodings(rgb_img3)[0]


img4 = cv2.imread('images/jeff bezos.jpeg')
rgb_img4 = cv2.cvtColor(img4, cv2.COLOR_BGR2RGB)
img_encoding4 = face_recognition.face_encodings(rgb_img4)[0]

img5 = cv2.imread('images/Messi.jpeg')
rgb_img5 = cv2.cvtColor(img5, cv2.COLOR_BGR2RGB)
img_encoding5 = face_recognition.face_encodings(rgb_img5)[0]

result = face_recognition.compare_faces([img_encoding], img_encoding5)
print("Result: ", result)

cv2.imshow("Img", img)
cv2.imshow("Img 5", img5)
cv2.waitKey(0)
