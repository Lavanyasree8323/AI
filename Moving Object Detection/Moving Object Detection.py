import cv2
import time
import imutils
cam = cv2.VideoCapture(0)

firstFrame=None
area=250

while True:
    _,org = cam.read()
    text = "Normal"
    img = imutils.resize(org, width=700)
    gry = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)
    gaus= cv2.GaussianBlur(gry, (21,21), 0)
    if firstFrame is None:
        firstFrame = gaus
        continue
    dif = cv2.absdiff(firstFrame, gaus)
    thrs = cv2.threshold(dif, 25,255, cv2.THRESH_BINARY)[1]
    thrs = cv2.dilate(thrs, None, iterations=2)
    ctrs = cv2.findContours(thrs.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    ctrs = imutils.grab_contours(ctrs)
    for c in ctrs:
        if cv2.contourArea(c) < area:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(org, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Moving Object Detected"
    print(text)
    cv2.putText(org, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255),2)
    cv2.imshow("display", org)

    key = cv2.waitKey(10)
    print(key)
    if key == ord("s"):
        break
cam.release()
cv2.destroyAllWindows()
