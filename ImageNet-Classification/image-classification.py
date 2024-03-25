from google.colab import drive
drive.mount('/content/drive')

import os
import numpy as np
import shutil
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions


model = MobileNetV2(weights='imagenet')

def categorize_images(image_folder, target_folder):
    for img_name in os.listdir(image_folder):
        img_path = os.path.join(image_folder, img_name)
        
        img = image.load_img(img_path, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

       
        preds = model.predict(x)
        decoded = decode_predictions(preds, top=1)[0][0]
        category = decoded[1]

        category_folder = os.path.join(target_folder, category)
        if not os.path.isdir(category_folder):
            os.makedirs(category_folder)

        shutil.move(img_path, os.path.join(category_folder, img_name))


source_folder = '/content/drive/MyDrive/images-board'
sorted_folder = '/content/drive/MyDrive/sorted-images'

if not os.path.isdir(sorted_folder):
    os.makedirs(sorted_folder)

categorize_images(source_folder, sorted_folder)
