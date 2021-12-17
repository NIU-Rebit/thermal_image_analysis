import cv2
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
try:
    from PIL import Image
except ImportError:
    import Image

# Open image file
# image = Image.open(r'D:\OneDrive - ems.niu.edu.tw\文件\Python Scripts\Thermal_Imaging\flir.jpg')
# width, height = image.size
width, height = (640, 480)
my_dpi, part = 100, 16

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, image = cap.read()
    image = cv2.resize(image, (640, 480))
    Image.open(image)
    image = Image.fromarray(image)

    # Set up figure
    fig=plt.figure(figsize=(float(image.size[0])/my_dpi,float(image.size[1])/my_dpi),dpi=my_dpi)
    ax=fig.add_subplot(111)

    # Remove whitespace from around the image
    # fig.subplots_adjust(left=0,right=1,bottom=0,top=1)

    # Set the gridding interval: here we use the major tick interval
    myInterval_x= width*1.0 / part
    myInterval_y= height*1.0 / part
    loc_x = plticker.MultipleLocator(base=myInterval_x)
    loc_y = plticker.MultipleLocator(base=myInterval_y)
    ax.xaxis.set_major_locator(loc_x)
    ax.yaxis.set_major_locator(loc_y)

    # Add the grid
    ax.grid(which='major', axis='both', linestyle='-')

    # Add the image
    # ax.imshow(image)
    # plt.show()  # to show the result
    cv2.imshow("test", image)

    # Find number of gridsquares in x and y direction
    nx=abs(int(float(ax.get_xlim()[1]-ax.get_xlim()[0])/float(myInterval_x)))
    ny=abs(int(float(ax.get_ylim()[1]-ax.get_ylim()[0])/float(myInterval_y)))

    # Add some labels to the gridsquares
    for j in range(ny):
        y = myInterval_y/2+j*myInterval_y
        for i in range(nx):
            x = myInterval_x/2.+float(i)*myInterval_x
            ax.text(x,y,'{:d}'.format(i+j*nx),color='w',ha='center',va='center',fontsize=5)

    if cv2.waitKey(1) == ord('q'):
       break

# # Save the figure
# fig.savefig('grid_thermal.png',dpi=my_dpi)

cap.release()
cv2.destroyAllWindows()