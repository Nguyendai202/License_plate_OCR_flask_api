from DNN_model import conv_model
import tensorflow as tf
from keras.callbacks import TensorBoard 
from datetime import datetime
from data_preprocessing import X_train,X_test,y_train,y_test
train_dataset = tf.data.Dataset.from_tensor_slices(( X_train,y_train)).batch(64)
test_dataset = tf.data.Dataset.from_tensor_slices((X_test, y_test)).batch(64)
if __name__ == "__main__":
    print("start training model: ")
    log_dir="logs/fit/"+ datetime.now().strftime("%Y%m%d-%H%M%S")
    tensorboard_callback = TensorBoard(log_dir=log_dir,histogram_freq=1)
    history = conv_model.fit(train_dataset, epochs=10, validation_data=test_dataset, callbacks=[tensorboard_callback])
    conv_model.save("resnet_50.h5") 