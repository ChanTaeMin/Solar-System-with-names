import cv2

img = cv2.imread('Images/solar-system.jpg');




cv2.putText(img,
          "Sun",
          (20,300),
          cv2.FONT_HERSHEY_COMPLEX,
          0.5,
          (255,235,255),
          )



cv2.putText(img,
          "Mecury",
          (100,250),
          cv2.FONT_HERSHEY_COMPLEX,
          0.5,
          (255,235,255),
          )

cv2.putText(img,
          "Venus",
          (200,250),
          cv2.FONT_HERSHEY_COMPLEX,
          0.5,
          (255,235,255),
          )

cv2.putText(img,
          "Earth",
          (300,260),
          cv2.FONT_HERSHEY_COMPLEX,
          0.5,
          (255,235,255),
          )

cv2.putText(img,
          "Moon",
          (310,200),
          cv2.FONT_HERSHEY_COMPLEX,
          0.5,
          (255,235,255),
          )

cv2.putText(img,
          "Mars",
          (400,250),
          cv2.FONT_HERSHEY_COMPLEX,
          0.5,
          (255,235,255),
          )

cv2.putText(img,
          "Jupiter",
          (520,250),
          cv2.FONT_HERSHEY_COMPLEX,
          0.5,
          (0,0,0),
          )

cv2.putText(img,
          "Saturn",
          (700,250),
          cv2.FONT_HERSHEY_COMPLEX,
          0.5,
          (255,235,255),
          )

cv2.putText(img,
          "Uranus",
          (970,250),
          cv2.FONT_HERSHEY_COMPLEX,
          0.5,
          (255,235,255),
          )

cv2.putText(img,
          "Nuptune",
          (1100,250),
          cv2.FONT_HERSHEY_COMPLEX,
          0.5,
          (255,235,255),
          )





cv2.imshow('solar-system',img)


cv2.waitKey(0)

cv2.imwrite('solarsystemwithname.jpg',img)