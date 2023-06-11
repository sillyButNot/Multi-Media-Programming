import tensorflow as tf
from tensorflow.keras import layers, models, optimizers
import numpy as np
from sklearn.metrics import confusion_matrix
import cv2
import tensorflow as tf

tf.random.set_seed(42)
np.random.seed(42)


# tr_file = input('Enter list file for training:')
tr_file = 'list_tr'
# ts_file = input('Enter list file for testing:')
ts_file = 'list_te'
# n_epochs = int(input('Enter number of epochs:'))
n_epochs = int(30)
# b_size = int(input('Enter number of classes:'))
b_size = int(32)

# n_tag = int(input('Enter number of classes : '))
n_tag = int(6)
# l_rate = float(input('Enter learning rate:'))
l_rate = float(0.1)
SX = 252
SY = 142


def Getdata(list_file):
    fp = open(list_file, 'r')
    lines = fp.read().splitlines()
    inp = []
    tag = []
    for line in lines:
        img_file, id = line.split(' ')
        print(img_file, id)
        img = cv2.imread(img_file)

        img = cv2.resize(img, (SY, SX))
        inp.append(img / 255)
        tag.append(np.uint8(id))
    fp.close()
    return inp, tag


[tr_inp, tr_tag] = Getdata(tr_file)
tr_inp = np.array(tr_inp)
tr_tag = np.array(tr_tag)
[ts_inp, ts_tag] = Getdata(ts_file)
ts_inp = np.array(ts_inp)
ts_tag = np.array(ts_tag)

model = models.Sequential()
model.add(layers.Conv2D(5, (11, 11), activation='relu', input_shape=(SX, SY, 3)))
model.add(layers.MaxPooling2D((4, 4)))
model.add(layers.Conv2D(7, (7, 7), activation='relu'))
model.add(layers.MaxPooling2D((4, 4)))
model.add(layers.Flatten())
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(n_tag, activation='softmax'))
model.summary()
adam = optimizers.Adam(learning_rate=l_rate)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(tr_inp, tr_tag, batch_size=b_size, epochs=n_epochs, verbose=1, shuffle=1)
test_loss, test_acc = model.evaluate(ts_inp, ts_tag, verbose=0)
print("Results for test data=")
print(test_acc)
pred = model.predict(ts_inp)
y_pred = np.argmax(pred, axis=1)
conf_mat = confusion_matrix(ts_tag, y_pred)
print(conf_mat)
