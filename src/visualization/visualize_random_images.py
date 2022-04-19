import numpy as np
import matplotlib.pyplot as plt

def visualize_random_images(images, labels, classes):
    # Randomisation des indices et affichage de 9 images alétoires de la base d'apprentissage
    indices = np.arange(images.shape[0])
    np.random.shuffle(indices)
    plt.figure(figsize=(12, 12))
    for i in range(0, 9):
        plt.subplot(3, 3, i+1)
        plt.title(classes[int(labels[indices[i]])])
        plt.imshow(images[indices[i]])
    plt.tight_layout()
    plt.show()