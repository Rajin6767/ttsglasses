import os
import cv2
import pytesseract
from gtts import gTTS
from playsound import playsound
from google.cloud import translate_v2 as translate

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:\\Users\\rajin\\Downloads\\pythonocrtts-c792a2d7a26c.json'

client = translate.Client()

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

video = cv2.VideoCapture("http://152.23.75.84:8081/video")
video.set(3, 640)
video.set(4, 480)

img1 = cv2.imread('Capture_1.JPG')
img2 = cv2.imread('Capture_2.JPG')
img3 = cv2.imread('Capture_3.JPG')
img4 = cv2.imread('Capture_4.jpg')

h1Img, w1Img, _ = img1.shape
h2Img, w2Img, _ = img2.shape
h3Img, w3Img, _ = img3.shape
h4Img, w4Img, _ = img4.shape

box1 = pytesseract.image_to_boxes(img1)
box2 = pytesseract.image_to_boxes(img2)
box3 = pytesseract.image_to_boxes(img3)
box4 = pytesseract.image_to_boxes(img4)

data1 = pytesseract.image_to_data(img1)
data2 = pytesseract.image_to_data(img2)
data3 = pytesseract.image_to_data(img3)
data4 = pytesseract.image_to_data(img4)

with open("string.txt", "w") as filewrite:
    for z, a in enumerate(data4.splitlines()):
        if z != 0:
            a = a.split()
            if len(a) == 12:
                x, y = int(a[6]), int(a[7])
                w, h = int(a[8]), int(a[9])
                cv2.rectangle(img4, (x, y), (x + w, y + h), (255, 0, 0), 1)
                cv2.putText(img4, a[11], (x, y + 25), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
                filewrite.write(a[11] + " ")

# Check if the file exists before opening it
if os.path.exists("string.txt"):
    fileread = open("string.txt", "r")
else:
    print("File does not exist")

lang = 'fr'
line = fileread.read()
if line != " ":
    result = client.translate(line, target_language='en')
    translated_text = result['translatedText']

    speech = gTTS(text=translated_text, lang='en', slow=False)
    speech.save("test.mp3")
cv2.imshow('gtts', img4)
cv2.waitKey(0)
playsound("test.mp3")

# while True:
#     check, frame = video.read()
#     data4 = pytesseract.image_to_data(frame)
#     for z, a in enumerate(data4.splitlines()):
#         if z != 0:
#             a = a.split()
#             if len(a) == 12:
#                 x, y = int(a[6]), int(a[7])
#                 w, h = int(a[8]), int(a[9])
#                 cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 1)
#                 cv2.putText(frame, a[11], (x, y + 25), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
#     cv2.imshow('Video Capture', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#             video.release()
#             cv2.destroyAllWindows()
#             break

# for z, a in enumerate(data1.splitlines()):
#     if z != 0:
#         a = a.split()
#         if len(a) == 12:
#             x, y = int(a[6]), int(a[7])
#             w, h = int(a[8]), int(a[9])
#             cv2.rectangle(img1, (x, y), (x + w, y + h), (255, 0, 0), 1)
#             cv2.putText(img1, a[11], (x, y + 25), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
#
# for z, a in enumerate(data2.splitlines()):
#     if z != 0:
#         a = a.split()
#         if len(a) == 12:
#             x, y = int(a[6]), int(a[7])
#             w, h = int(a[8]), int(a[9])
#             cv2.rectangle(img2, (x, y), (x + w, y + h), (255, 0, 0), 1)
#             cv2.putText(img2, a[11], (x, y + 25), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
#
# for z, a in enumerate(data3.splitlines()):
#     if z != 0:
#         a = a.split()
#         if len(a) == 12:
#             x, y = int(a[6]), int(a[7])
#             w, h = int(a[8]), int(a[9])
#             cv2.rectangle(img3, (x, y), (x + w, y + h), (255, 0, 0), 1)
#             cv2.putText(img3, a[11], (x, y + 25), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
#
# cv2.imshow('capture 1', img1)
# cv2.imshow('capture 2', img2)
# cv2.imshow('capture 3', img3)
# cv2.waitKey()

# for a in box1.splitlines():
#     a = a.split()
#     x, y = int(a[1]), int(a[2])
#     w, h = int(a[3]), int(a[4])
#
#     cv2.rectangle(img1, (x, h1Img - y), (w, h1Img - h), (255, 0, 0), 1)
#     cv2.putText(img1, a[0], (x, h1Img - y + 25), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
# for a in box2.splitlines():
#     a = a.split()
#     x, y = int(a[1]), int(a[2])
#     w, h = int(a[3]), int(a[4])
#     cv2.rectangle(img2, (x, h2Img - y), (w, h2Img - h), (255, 0, 0), 1)
#     cv2.putText(img2, a[0], (x, h2Img - y + 25), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
#
# for a in box3.splitlines():
#     a = a.split()
#     x, y = int(a[1]), int(a[2])
#     w, h = int(a[3]), int(a[4])
#
#     cv2.rectangle(img3, (x, h3Img - y), (w, h3Img - h), (255, 0, 0), 1)
#     cv2.putText(img3, a[0], (x, h3Img - y + 25), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
#
# cv2.imshow('image1', img1)
# cv2.imshow('image2', img2)
# cv2.imshow('image3', img3)
#
# cv2.waitKey()
