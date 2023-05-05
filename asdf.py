import cv2


#img = cv2.imread("/Users/abhijoy/Desktop/Visual Studio: Coding/Python/Byjus 2.0/PRO-c116-OpenCV-Image-Assets/butterfly.jpg")
#cv2.imshow("displayImage", img)
#grey = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

#cv2.putText(grey, "Hello", (20,220), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color = (0,0,255))

#cv2.imshow("display image", grey)

#print(img)
#cv2.waitKey(0)

solarImg = cv2.imread("/Users/abhijoy/Desktop/Visual Studio: Coding/Python/Byjus 2.0/solar-system.jpg")
solar1 = cv2.putText(solarImg, "sun", (10,220), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color = (255,255,255))
solar2 = cv2.putText(solar1, "mercury", (100,200), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color = (255,255,255))
solar3 = cv2.putText(solar2, "Venus", (200,200), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color = (255,255,255))
solar4 = cv2.putText(solar3, "Earth", (300,150), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color = (255,255,255))
solar5 = cv2.putText(solar4, "Mars", (400,200), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color = (255,255,255))
solar6 = cv2.putText(solar4, "JUPITER", (600,200), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color = (255,255,255))
solar6 = cv2.putText(solar4, "Saturn", (700,200), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color = (255,255,255))
solar6 = cv2.putText(solar4, "Uranus", (900,200), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color = (255,255,255))
solar6 = cv2.putText(solar4, "Neptune", (1200,200), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color = (255,255,255))
cv2.imshow("Solar System", solar5)
cv2.waitKey(0)



