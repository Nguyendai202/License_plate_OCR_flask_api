import tensorflow as tf
from keras.layers import RandomFlip, RandomRotation,RandomContrast,RandomTranslation

def data_augmenter():
    data_augmentation = tf.keras.Sequential([
        RandomFlip("horizontal"),
        RandomRotation(0.2),
        # RandomContrast(factor=0.1),
        # RandomTranslation(height_factor=0.1,width_factor=0.1)
    ])

    return data_augmentation
augmenter = data_augmenter()

# def display_images(image, augmented_image):
#     fig, ax = plt.subplots(1, 2, figsize=(10, 5))
#     ax[0].imshow(image)
#     ax[0].set_title('Original image')
#     ax[1].imshow(augmented_image)
#     ax[1].set_title('Augmented image')
#     plt.show()

# # Load an example image from X_train1
# image = X_train1[1]

# # Use data augmenter to generate an augmented image
# # augmented_image = data_augmentation(tf.expand_dims(image, axis=0))
# augmented_image = data_augmentation(image)
# augmented_image = tf.squeeze(augmented_image)

# # Display the images side by side
# display_images(image, augmented_image)

if __name__ == "__main__":
    augmenter = data_augmenter()

