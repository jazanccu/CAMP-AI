#استيراد مكتبات OpenCV و NumPy و Matplotlib
import cv2
import numpy as np
import matplotlib.pyplot as plt

#قراءة الصورة من ملف img.jpg وتخزينها في متغير image
image = cv2.imread("img.jpg")

#تحويل الصورة إلى الدرجات الرمادية وتخزينها في متغير gray
gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

#حفظ الصورة الرمادية في ملف جديد بإسم "Photo.jpg"
cv2.imwrite("Photo.jpg" , gray)

#عرض الصورة الأصلية على الشاشة في إطار يحمل اسم "Photo"
cv2.imshow('Photo',image)

#انتظار الضغط على أي مفتاح على لوحة المفاتيح وتخزين القيمة المرتبطة به في المتغير I
I = cv2.waitKey(0)

#إذا تم الضغط على مفتاح الـ escape (الرمز 27 في لوحة المفاتيح) أو الحرف S في لوحة المفاتيح (ملاحظة: هنا تم استخدام حرف كبير بدلًا من حرف صغير)
#فإن جميع النوافذ المفتوحة في البرنامج ستتم إغلاقها
if I == 27 or I == ord('S'):
    cv2.destroyAllWindows()
    
#ملاحظة: لم يتم استخدام مكتبة NumPy و Matplotlib في هذا الكود بعد، ولكن يمكن استخدامهما في مراحل أخرى للتلاعب بالصورة وعرضها بصورة أخرى على الشاشة.