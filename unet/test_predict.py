'''
from unet import *
from data import *

mydata = dataProcess(512,512)

imgs_test = mydata.load_test_data()

myunet = myUnet()

model = myunet.get_unet()

model.load_weights('unet.hdf5')

imgs_mask_test = model.predict(imgs_test, verbose=1)

np.save('imgs_mask_test.npy', imgs_mask_test)
'''
from unet import *
from data import *
import numpy as np
import cv2
im=cv2.imread('../data/train/0a1b0b7df2918d543347050ad8b16051.jpg',0)
im=cv2.resize(im,(512,512))
x=np.zeros([1,512,512,1])
x[0,:,:,0]=im;
x=x/255;

myunet = myUnet()

model = myunet.get_unet()

model.load_weights('unet.hdf5')

imgs_mask_test = model.predict(x, verbose=1)
print imgs_mask_test
print np.shape(imgs_mask_test)
imgs_mask_test=np.reshape(imgs_mask_test,[512,512])
imgs_mask_test=imgs_mask_test*255
cv2.imshow('ccc',imgs_mask_test)
cv2.waitKey(0)

np.save('imgs_mask_test.npy', imgs_mask_test)