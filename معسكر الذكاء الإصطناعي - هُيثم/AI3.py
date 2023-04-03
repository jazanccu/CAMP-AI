#استيراد مكتبات OpenCV و NumPy و Matplotlib
import cv2
import numpy as np
import matplotlib.pyplot as plt

#قراءة الصورة من ملف img.jpg وتخزينها في متغير img
img = cv2.imread("img.jpg")

#تحويل الصورة إلى الدرجات الرمادية وتخزينها في متغير gray
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

#تحويل الصورة الرمادية إلى float32
gray = np.float32(gray)

#الكشف عن النقاط الزاوية في الصورة باستخدام Harris corner detector وتخزين النتائج في متغير des
des = cv2.cornerHarris(gray,2,5,0.07)

#توسيع النقاط الزاوية المكتشفة باستخدام dilate
des = cv2.dilate(des,None)

#تغيير لون النقاط الزاوية المكتشفة في الصورة إلى اللون الأحمر
img[des>0.01 *des.max()]=[0,0,255]

#عرض الصورة المعدلة على الشاشة باستخدام مكتبة Matplotlib
plt.imshow(img)

#انتظار الضغط على أي مفتاح على لوحة المفاتيح للخروج من البرنامج
plt.waitforbuttonpress()