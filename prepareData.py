from collections import Counter

import cv2
import numpy as np
import pandas as pd

df = pd.read_csv('data/fer2013.csv', header=0)

labels = list(df['emotion'])
print "Label frequencies: {0}".format(dict(Counter(labels)))

X = []
Y = []

for i in range(df.shape[0]):
    img_pixels = df['pixels'][i]
    label = df['emotion'][i]
    img_pixels = img_pixels.split(' ')
    img = np.reshape(np.array(img_pixels, dtype=np.uint8), (48, 48))
    # Little preprocessing
    img = cv2.equalizeHist(img)
    img = np.reshape(img, (1, 48, 48))

    X.append(img)
    Y.append(label)

    if i % 1000 == 0:
        print "{0} rows done!".format(i)

X = np.array(X)
Y = np.array(Y)

print X.shape
print Y.shape

np.save("data/X_train.npy", X)
np.save("data/Y_train.npy", Y)

print "Arrays are saved!"
