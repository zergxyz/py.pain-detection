import keras
from keras import regularizers
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D

NUM_CLASSES = 6
PICTURE_DIM = 48

def print_metadata(x_train, x_test):
    print('x_train shape:', x_train.shape)
    print(x_train.shape[0], 'train samples')
    print(x_test.shape[0], 'test samples')


def build_model(x_train):
    model = Sequential()

    model.add(Conv2D(32, (3, 3), padding='same', input_shape=x_train.shape[1:]))
    model.add(Activation('relu'))
    
    model.add(Dropout(0.25))
        
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Conv2D(32, (3, 3), activity_regularizer= regularizers.l2(0.0003)))
    model.add(Activation('relu'))
    
    model.add(Dropout(0.25))
    
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Conv2D(64, (3, 3), padding='same', activity_regularizer= regularizers.l2(0.0003)))
    model.add(Activation('relu'))
    
    model.add(Dropout(0.25))
    
    model.add(Conv2D(128, (3, 3)))
    model.add(Activation('relu')) 
    
    model.add(Flatten())
    
    model.add(Dense(512))
    model.add(Activation('relu'))
    
    model.add(Dense(NUM_CLASSES))
    model.add(Activation('softmax'))

    return model
    
