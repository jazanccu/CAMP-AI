#استيراد مكتبات NumPy و OpenCV و pyplot من مكتبة matplotlib
import numpy as np
import cv2
from matplotlib import pyplot as plt

#تحميل ملفات التعرف على الكلاب والبشر والقطط وتخزينها في متغيرات منفصلة
face_cascade=cv2.CascadeClassifier('mydogdetector.xml')
face_cascade2=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_cascade3=cv2.CascadeClassifier('mycatdetector2.xml')

#قراءة الصورة وتخزينها في متغير img، ثم تحويلها إلى الدرجات الرمادية وتخزينها في متغير gray
img=cv2.imread('family.bmp')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#تحديد نوع الخط الذي سيستخدم للكتابة على الصورة
font=cv2.FONT_HERSHEY_SIMPLEX

#الكشف عن الكلاب في الصورة الرمادية وتخزينها في متغير faces
faces=face_cascade.detectMultiScale(gray,1.345,5,75)

#الكشف عن البشر في الصورة الرمادية وتخزينها في متغير faces2
faces2=face_cascade2.detectMultiScale(gray,1.3,5)

#الكشف عن القطط في الصورة الرمادية وتخزينها في متغير faces3
faces3=face_cascade3.detectMultiScale(gray,1.3,2,75)

#رسم مربع حول كل كلب مكتشف في الصورة وكتابة كلمة "Dog" بجواره
for(x,y,w,h) in faces:
	img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
	cv2.putText(img,'Dog',(x,y),font,0.9,(0,255,0),2)

#رسم مربع حول كل بشر مكتشف في الصورة وكتابة كلمة "Human" بجواره
for(z,v,b,n) in faces2:
	img=cv2.rectangle(img,(z,v),(z+b,v+n),(0,0,255),2)
	cv2.putText(img,'Human',(z,v),font,0.9,(0,0,255),2)

#رسم مربع حول كل قطة مكتشفة في الصورة وكتابة كلمة "Cat" بجوارها
for(q,w,e,r) in faces3:
	img=cv2.rectangle(img,(q,w),(q+e,w+r),(255,0,0),2)
	cv2.putText(img,'Cat',(q,w),font,0.9,(255,0,0),2)
	
#تغيير ترتيب القنوات اللونية في الصورة من BGR إلى RGB	
p,l,m=cv2.split(img)
img=cv2.merge([m,l,p])

#عرض الصورة المعدلة باستخدام pyplot من مكتبة matplotlib
plt.imshow(img)
plt.show()

#انتظار الضغط على أي مفتاح على لوحة المفاتيح لإغلاق النوافذ المفتوحة
cv2.waitKey(0)
cv2.destroyAllWindows()

