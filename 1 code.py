from pickletools import uint8
from PIL import Image
import numpy as np
w,h=1000, 1000
data=np.zeros((h,w,3), dtype=np.uint8)
data[0:1000, 0:1000]=[0,0,0]
img=Image.fromarray(data, 'RGB')
img.save('my.png')
img.show()