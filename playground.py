import numpy as np
import cv2 

rows = 500
cols = 500
newMat_3ch = np.zeros((rows, cols, 3), dtype = "uint8") #3channel

step = 4       # grid的密度
thickness = 1 
v_xy = []
h_xy = []
# x = np.linspace(start=0, stop=rows, num=step)
# y = np.linspace(start=0, stop=cols, num=step)

# for i in range(step):
#     v_xy.append( [int(x[i]), 0, int(x[i]), rows-1] )
#     h_xy.append( [0, int(y[i]), cols-1, int(y[i])] )

cv2.namedWindow('newMat_3ch',0)
i = 0   # initialize
while True:
    if i == step - 1:
        break
    x = np.linspace(start=0, stop=rows, num=step)
    y = np.linspace(start=0, stop=cols, num=step)
    v_xy.append( [int(x[i]), 0, int(x[i]), rows-1] )
    h_xy.append( [0, int(y[i]), cols-1, int(y[i])] )
    [x1, y1, x2, y2] = v_xy[i]
    [x1_, y1_, x2_, y2_] = h_xy[i]
    cv2.line(newMat_3ch, (x1,y1), (x2, y2), (0,0,255), thickness)       # vertical
    cv2.line(newMat_3ch, (x1_,y1_), (x2_, y2_), (255,0,0), thickness)   # horizontal
    cv2.imshow('newMat_3ch', newMat_3ch)
    cv2.waitKey(40) # 觀察grid掃蕩
    i = i + 1
    if step <= 70:
        step = step + 1

# for i in range(step):
#     [x1, y1, x2, y2] = v_xy[i]
#     [x1_, y1_, x2_, y2_] = h_xy[i]
#     cv2.line(newMat_3ch, (x1,y1), (x2, y2), (0,0,255), thickness)     # vertical
#     cv2.imshow('newMat_3ch', newMat_3ch)
#     cv2.waitKey(50) # 觀察grid掃蕩
#     cv2.line(newMat_3ch, (x1_,y1_), (x2_, y2_), (255,0,0), thickness)   # horizontal
#     cv2.imshow('newMat_3ch', newMat_3ch)
#     cv2.waitKey(50) # 觀察grid掃蕩

cv2.waitKey(0)
cv2.destroyAllWindows()