import cv2
face_cascade = cv2.CascadeClassifier('haarface.xml')
video_capture = cv2.VideoCapture('Akarsh.mp4' )

scale_factor = 1

while True:
   
    ret, frame = video_capture.read()

    if not ret:
      
        break

    height, width, _ = frame.shape
    desired_width = int(width * scale_factor)
    desired_height = int(height * scale_factor)

    resized_frame = cv2.resize(frame, (desired_width, desired_height))


    gray = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2 )

   
    for (x, y, w, h) in faces:
        cv2.rectangle(resized_frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        cv2.putText(resized_frame, 'Face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

   
    cv2.imshow('Face Detection', resized_frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()
