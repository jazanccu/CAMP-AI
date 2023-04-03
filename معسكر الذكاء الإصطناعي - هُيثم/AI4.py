#استيراد مكتبات OpenCV و NumPy و Matplotlib و requests و PIL
import cv2
import numpy as np
import matplotlib.pyplot as plt
import requests
from PIL import Image

#قراءة الصورة من الرابط المحدد وتغيير حجمها إلى 450x250 وتخزينها في متغير image
image = Image.open(requests.get('https://a57.foxnews.com/media.foxbusiness.com/BrightCove/854081161001/201805/2879/931/524/854081161001_5782482890001_5782477388001-vs.jpg', stream=True).raw)
image = image.resize((450,250))
image_arr=np.array(image)

#تحويل الصورة إلى الدرجات الرمادية وتخزينها في متغير grey
grey = cv2.cvtColor(image_arr,cv2.COLOR_BGR2GRAY)

#تطبيق Gaussian Blur على الصورة الرمادية وتخزين النتيجة في متغير blur وعرض الصورة المعدلة باستخدام مكتبة PIL
blur = cv2.GaussianBlur(grey,(5,5),0)
Image.fromarray(blur)

#توسيع الصورة المعدلة بواسطة dilate وتخزين النتيجة في متغير dilated وعرض الصورة المعدلة باستخدام مكتبة PIL
dilated = cv2.dilate(blur,np.ones((3,3)))
Image.fromarray(dilated)

#إنشاء مصفوفة kernel بحجم (2, 2) وشكل بيضوي وتطبيق عملية Closing على الصورة التي تم توسيعها وتخزين النتيجة في متغير closing وعرض الصورة المعدلة باستخدام مكتبة PIL
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
closing = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)
Image.fromarray(closing)

#قراءة ملف haarcascade_car.xml وتخزينه في متغير car والكشف عن السيارات في الصورة المعدلة وتخزين نتيجة الكشف في متغير cars
car_src = 'haarcascade_car.xml'
car = cv2.CascadeClassifier(car_src)
cars = car.detectMultiScale(closing, 1.1, 1)

#إعداد متغير لتحديد عدد السيارات وعرض الصورة المعدلة باستخدام مكتبة PIL
cnt = 0
for(x,y,w,h) in cars:
    cv2.rectangle(image_arr,(x,y),(x+w,y+h),(255,0,0),2)
cnt += 1
print(cnt,"CARS")
Image.fromarray(image_arr)

#عرض الصورة المعدلة على الشاشة باستخدام مكتبة OpenCV وانتظار الضغط على أي مفتاح على لوحة المفاتيح للخروج من البرنامج
cv2.imshow('image',image_arr)
cv2.waitKey()
cv2.destroyAllWindows()