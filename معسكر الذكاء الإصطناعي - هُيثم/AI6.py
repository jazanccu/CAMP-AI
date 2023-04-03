#استيراد مكتبة OpenCV
import cv2

#فتح الكاميرا وتخزينها في متغير camera
camera = cv2.VideoCapture(0)

#دوران الكود داخل حلقة while حتى يتم الضغط على حرف "s" من لوحة المفاتيح
while(True):
    
    # قراءة الإطار الحالي من الكاميرا وتخزينه في متغير frame
    ret, frame = camera.read()

    # عرض الإطار الحالي على الشاشة باستخدام مكتبة [OpenCV](poe://www.poe.com/_api/key_phrase?phrase=OpenCV&prompt=Tell%20me%20more%20about%20OpenCV.)
    cv2.imshow('frame',frame)

    # إذا تم الضغط على حرف "s" من لوحة المفاتيح، فإن الحلقة تتوقف والكاميرا تتم إغلاقها
    if cv2.waitKey(1) & 0xff == ord('s'):
        break

#إغلاق الكاميرا وإغلاق جميع النوافذ المفتوحة باستخدام مكتبة OpenCV
camera.release()
cv2.destroyAllWindows()