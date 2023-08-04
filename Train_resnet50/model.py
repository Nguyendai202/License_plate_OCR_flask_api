import tensorflow as tf 
from keras.models import Model
from keras.applications import InceptionResNetV2, MobileNetV2
from keras.layers import Dense, Flatten, Input, Layer
from keras.preprocessing.image import ImageDataGenerator
from data_augement import augmenter

IMG_SIZE = (160, 160, 3)

def convolutional_model(input_shape):
    # Load the ResNet50 model pre-trained on ImageNet without the top layer
    moblienetv3 = InceptionResNetV2(weights="imagenet", include_top=False, input_tensor=input_shape)
    
    # Đóng băng các trọng số của InceptionResNetV2
    for layer in  moblienetv3.layers:
        layer.trainable = False
    
    # Thêm lớp đầu ra để phân loại 
    x = Flatten()(moblienetv3.output)
    x = Dense(300, activation="relu")(x)
    x = Dense(150, activation="relu")(x)
    output = Dense(5, activation="softmax")(x)
    
    # Tạo mô hình
    model = Model(inputs= moblienetv3.input, outputs=output)
    return model

def alpaca_model(image_shape=IMG_SIZE):
    #Load Mobilenet V2 được huấn luyện trước trên ImageNet mà không có top layers
    base_model = MobileNetV2(input_shape=image_shape,
                             include_top=False, 
                             weights='imagenet')
    
    base_model.trainable = False 
    inputs = Input(shape=image_shape) 
    
    data_augmentation = augmenter
    x = data_augmentation(inputs)
    x = tf.keras.applications.mobilenet_v2.preprocess_input(x) 
    x = base_model(x, training=False) 
    x = tf.keras.layers.GlobalAveragePooling2D()(x)
    x = tf.keras.layers.Dropout(0.2)(x)
    x =  Dense(20)(x)
    outputs = Dense(5, activation='softmax')(x)
    model = Model(inputs=inputs, outputs=outputs)
    
    return model

model2 = alpaca_model(IMG_SIZE)
base_learning_rate = 0.001
model2.compile(optimizer=tf.keras.optimizers.Adam(lr=base_learning_rate),
              loss=tf.keras.losses.CategoricalCrossentropy(),
              metrics=['accuracy'])

finetune_model = model2
base_model = model2.layers[4]
finetune_model.trainable = True
fine_tune_at = 50

# Đóng băng tất cả các lớp trước lớp `fine_tune_at`
for layer in base_model.layers[:fine_tune_at]:
    layer.trainable = False

optimizer = tf.keras.optimizers.Adam(lr=0.1 * base_learning_rate)

finetune_model.compile(optimizer=optimizer,
                       loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True),# đầu ra ko qua softmax 
                       metrics=['accuracy'])

finetune_model.summary()
