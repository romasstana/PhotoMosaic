from PIL import Image
import numpy as np
w,h=1000, 1000
data=np.zeros((h,w,3), dtype=np.uint8)
for h in range(0,499):
    for w in range(0,499):
        data[h,w]=[255,255,0]
for h in range(499,1000):
    for w in range(0,499):
        data[h,w]=[0,128,0]
for h in range(0,499):
    for w in range(499,1000):
        data[h,w]=[255,0,0]
for h in range(499,1000):
    for w in range(499,1000):
        data[h,w]=[0,0,0]
img=Image.fromarray(data, 'RGB')
img.save('my.png')
img.show()
