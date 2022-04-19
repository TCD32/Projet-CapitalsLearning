
from tensorflow.keras.utils import Sequence
import numpy as np

class LSPDSequence(Sequence):
    # Initialisation de la séquence avec différents paramètres
    def __init__(self, x_set, y_set, batch_size,augmentations):
        self.x, self.y = x_set, y_set # Données et labels d'apprentissage 
        self.batch_size = batch_size  # Taille de mini-batch
        self.augment = augmentations  # Fonction d'augmentation à appliquer
        self.indices1 = np.arange(x_set.shape[0]) 
        np.random.shuffle(self.indices1) # Les indices permettent d'accéder
        # aux données et sont retirés aléatoirement à chaque epoch pour varier 
        # la composition des batches au cours de l'entraînement

    # Fonction calculant le nombre de pas de descente du gradient par epoch
    def __len__(self):
        return int(np.ceil(len(self.x) / float(self.batch_size)))

    # Application de l'augmentation de données à chaque image du batch et aux
    # cartes de probabilités associées
    def apply_augmentation(self, bx):
        batch_x = np.zeros(bx.shape)

        # Pour chaque image du batch
        for i in range(len(bx)):

            img = bx[i]

            # Application de l'augmentation à l'image et aux masques
            transformed = self.augment(image=img)
            batch_x[i] = transformed['image']

        return batch_x

    # Fonction appelée pour chaque nouveau batch : sélection et augmentation des données
    def __getitem__(self, idx):
        batch_x = self.x[self.indices1[idx * self.batch_size:(idx + 1) * self.batch_size]]
        batch_y = self.y[self.indices1[idx * self.batch_size:(idx + 1) * self.batch_size]]
        
        batch_x = self.apply_augmentation(batch_x)

        return np.array(batch_x), np.array(batch_y)

    # Fonction appelée à la fin d'un epoch ; on randomise les indices d'accès aux données
    def on_epoch_end(self):
        np.random.shuffle(self.indices1)
        
