import os
import numpy as np
import matplotlib.pyplot as plt

def plot_classes_repartition():
    # Datasets
    testImagesPath = os.path.normpath(os.path.join(os.getcwd(), '../data/test'))
    trainImagesPath = os.path.normpath(os.path.join(os.getcwd(), '../data/train'))
    validationImagesPath = os.path.normpath(os.path.join(os.getcwd(), '../data/validation'))
    datasetImagesPaths = [trainImagesPath, testImagesPath, validationImagesPath]

    # Cities
    classes = os.listdir(trainImagesPath)

    # Figures
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])

    colors = ['r', 'g', 'b']

    datasetData = []
    bottom = [0, 0, 0]
    for i, dataset in enumerate(datasetImagesPaths):
        datasetData.append([])

        for city in classes:
            currentPath = os.path.normpath(os.path.join(dataset, city))
            datasetData[i].append(len(os.listdir(currentPath)))
        
        datasetBar = ax.bar(classes, datasetData[i], bottom=bottom, color=colors[i])
        ax.bar_label(datasetBar, label_type='center')
        bottom = np.add(bottom, datasetData[i])

    # Plot
    ax.bar_label(datasetBar)
    ax.legend(labels=['Train', 'Test', 'Validation'])
    
    plt.show()