#استيراد مكتبة OpenCV
import cv2

#تحميل ملف myfacedetector.xml وتخزينه في متغير face
face = cv2.CascadeClassifier('myfacedetector.xml')

#فتح الكاميرا وتخزينها في متغير camera
camera = cv2.VideoCapture(0)

#إنشاء نافذة باسم 'frame' باستخدام مكتبة OpenCV
cv2.namedWindow('frame', cv2.WINDOW_NORMAL)

#دوران الكود داخل حلقة while حتى يتم الضغط على حرف "z" من لوحة المفاتيح
while True:

     # قراءة الإطار الحالي من الكاميرا وتخزينه في متغير frame
    read_ok, frame = camera.read()

    # إذا فشل قراءة الإطار، فإن الحلقة تتوقف
    if not read_ok:
        break
    
    # تحويل الإطار الحالي إلى الدرجات الرمادية وتخزينه في متغير gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray)
    
    # الكشف عن الوجوه في الإطار الحالي وتخزينها في متغير faces
    for (x, y, w, h) in faces:
        # رسم مربع حول كل وجه مكتشف في الإطار الحالي
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)

    ## عرض الإطار الحالي على الشاشة باستخدام مكتبة OpenCV
    cv2.imshow('frame', frame)

    # إذا تم الضغط على حرف "z" من لوحة المفاتيح، فإن الحلقة تتوقف والكاميرا تتم إغلاقها
    if cv2.waitKey(1) & 0xFF == ord('z'):
        break

#إغلاق الكاميرا وإغلاق جميع النوافذ المفتوحة باستخدام مكتبة OpenCV
camera.release()
cv2.destroyAllWindows()