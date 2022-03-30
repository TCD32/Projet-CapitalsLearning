import os

import numpy as np
from PIL import Image

def load_data(dataset='train', image_size=64):
    data_path = "../data/"
    classes = os.listdir(data_path + dataset)

    num_images = 0
    for i in range(len(classes)):
        image_files = sorted(os.listdir(data_path + dataset + '/' + classes[i]))
        num_images += len(image_files)

    x = np.zeros((num_images, image_size, image_size, 3))
    y = np.zeros((num_images, 1))
    
    current_index = 0
    
    # Parcours des différents répertoires pour collecter les images
    for idx_class in range(len(classes)):
        image_files = sorted(os.listdir(data_path + dataset + '/' + classes[idx_class]))
    
        # Chargement des images, 
        for idx_img in range(len(image_files)):
            item = image_files[idx_img]
            if os.path.isfile(data_path + dataset + '/' + classes[idx_class] + '/' + item):
                # Ouverture de l'image
                img = Image.open(data_path + dataset + '/' + classes[idx_class] + '/' + item)
                # Conversion de l'image en RGB
                img = img.convert('RGB')
                # Redimensionnement de l'image et écriture dans la variable de retour x 
                img = img.resize((image_size,image_size))

                x[current_index] = np.asarray(img)
                # Écriture du label associé dans la variable de retour y
                y[current_index] = int(idx_class)
                current_index += 1
                
    return x, y.astype(int)

# Exemple utilisation
# x_train, y_train = load_data(dataset='train', image_size=64)
# x_val, y_val = load_data(dataset='validation', image_size=64)
# x_test, y_test = load_data(dataset='test', image_size=64)