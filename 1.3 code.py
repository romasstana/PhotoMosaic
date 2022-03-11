from PIL import Image
import numpy as np
w,h=1000, 1000
data=np.zeros((h,w,3), dtype=np.uint8)
for h in range(1000):
    for w in range(1000):
        data[h,w]=[h/2]
        data[h,w]=[w/4]
img=Image.fromarray(data, 'RGB')
img.save('my.png')
img.show()
