from PIL import Image
import numpy as np
w,h=1000, 1000
data=np.zeros((h,w,3), dtype=np.uint8)
y=0
z=8
while z<=1000:
    data[0:1000, y:z-4]=[255]
    z=z+8
    y=y+8
img=Image.fromarray(data, 'RGB')
img.save('my.png')
img.show()
