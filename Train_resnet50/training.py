from model import finetune_model,model2
from keras.callbacks import EarlyStopping,TensorBoard
import tensorflow as tf
from datetime import datetime
from data_procesing_done import X_train1,X_test1,y_train1,y_test1


X_train, X_test, y_train,y_test =X_train1,X_test1,y_train1,y_test1
train_dataset = tf.data.Dataset.from_tensor_slices((  X_train,y_train)).batch(64)
test_dataset = tf.data.Dataset.from_tensor_slices((X_test, y_test)).batch(64)
if __name__ == "__main__":
    print("start training model: ")
    log_dir="logs/fit/"+ datetime.now().strftime("%Y%m%d-%H%M%S")
    tensorboard_callback = TensorBoard(log_dir=log_dir,histogram_freq=1)
    early_stopping = EarlyStopping(monitor='val_loss', patience=20, verbose=1, mode='auto') # trong20 epoch liên tiếp mà ko có sự tiến bộ thì dừng ,verbose=1: cách hiện thị thông tin khi huấn luyện 
    history = model2.fit(train_dataset, epochs=25 , validation_data=test_dataset, callbacks=[tensorboard_callback,early_stopping])

    history_fine = finetune_model.fit(train_dataset,
                         epochs=300,
                         initial_epoch=history.epoch[-1], # epoch[-1]: nhận chỉ mục epoch cuối cùng đc trả về trước đó , thêm 50epoch nữa , tổng là 300 bắt đầu đến khi save mô hình 
                         validation_data=test_dataset)
    finetune_model.save("mobilenetv2_1_tranfer.h5") 

    