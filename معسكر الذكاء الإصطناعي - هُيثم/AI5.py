import cv2

# تعليقات لشرح المراحل المختلفة في الكود
# تحميل ملف تعريف الوجه
face_detector = cv2.CascadeClassifier('myfacedetector.xml') 

# فتح ملف الفيديو
cape = cv2.VideoCapture('Elon Musk.mp4')

# التحقق من نجاح فتح ملف الفيديو
if not cape.isOpened():
    print("Could not open video file")
    exit()

# إعداد متغيرات للون وحجم المربع المستخدم في تحديد الوجوه
color = (255, 0, 0) # اللون الأزرق
thickness = 5 # سمك الخط

# حلقة الفيديو
while True:
    # قراءة الإطار التالي من الفيديو
    ret, img = cape.read()

    # التحقق من نجاح قراءة الإطار
    if not ret:
        print("Could not read frame")
        break

    # تحويل الإطار إلى grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # الكشف عن الوجوه في الإطار
    faces = face_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

    # رسم مربع حول كل وجه مكتشف
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), color, thickness) 

    # عرض الإطار الحالي
    cv2.imshow('Video', img)

    # انتظر حتى يتم الضغط على ESC لإنهاء البرنامج
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# إغلاق ملف الفيديو وإغلاق نافذة العرض
cape.release()
cv2.destroyAllWindows()