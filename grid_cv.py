import numpy as np
import cv2 

cap = cv2.VideoCapture(2)
while True:
    if cap.isOpened():
        ret, image = cap.read()
        height, width, channels = image.shape   # 先取得影像尺寸
        break
        # print(height, width, channels)
cols, rows = (width, height)

# image = np.zeros((rows, cols, 3), dtype = "uint8")
step = 20       # grid的密度
thickness = 1 
v_xy = []
h_xy = []
x = np.linspace(start=0, stop=cols, num=step)
y = np.linspace(start=0, stop=rows, num=step)
cv2.namedWindow('grid', 0)

while cap.isOpened():
    ret, image = cap.read()

    for i in range(step):
        v_xy.append( [int(x[i]), 0, int(x[i]), rows-1] )
        h_xy.append( [0, int(y[i]), cols-1, int(y[i])] )
        [x1, y1, x2, y2] = v_xy[i]
        [x1_, y1_, x2_, y2_] = h_xy[i]
        cv2.line(image, (x1,y1), (x2, y2), (255,0,255), thickness)       # vertical
        cv2.line(image, (x1_,y1_), (x2_, y2_), (255,0,255), thickness)   # horizontal
        cv2.imshow('grid', image)
        # cv2.waitKey(50) # 觀察grid掃蕩
    if cv2.waitKey(1) == ord('q'):
       break

# cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()