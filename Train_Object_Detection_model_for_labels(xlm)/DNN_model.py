import tensorflow as tf 
from keras.layers import Dense,Flatten,Input
from keras.models import Model
from keras.applications import ResNet50

def convolutional_model(input_shape):
# Load the ResNet50 model pre-trained on ImageNet without the top layer
    resnet = ResNet50(weights="imagenet", include_top=False, input_tensor=input_shape)
    # Freeze the weights of the ResNet50 layers
    for layer in resnet.layers:
        layer.trainable = False
    # Add your top layer for classification
    x = Flatten()(resnet.output)
    x = Dense(500, activation="relu")(x)
    x = Dense(250, activation="relu")(x)
    output = Dense(4, activation="softmax")(x)
    # Create your model
    model = Model(inputs=resnet.input, outputs=output)
    return model

conv_model = convolutional_model(Input(shape=(224,224,3)))
conv_model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
conv_model.summary()


