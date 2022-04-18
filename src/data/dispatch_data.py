import os
import sys
import random
import shutil

def dispatch_data(pTrain, pTest, pValidation):
    try:
        assert 0 <= pTest <= 100
        assert 0 <= pTrain <= 100
        assert 0 <= pValidation <= 100
    except AssertionError as e:
        e.args += "Value of percentages must be between 0 and 100."

    try:
        assert pTest + pTrain + pValidation == 100
    except AssertionError as e:
        e.args += "Value of total percentage must be 100."
    
    # Percentages
    percTest = pTest / 100
    percTrain = pTrain / 100
    percValidation = pValidation / 100

    # Datasets
    testImagesPath = os.path.normpath(os.path.join(os.getcwd(), '../data/test'))
    trainImagesPath = os.path.normpath(os.path.join(os.getcwd(), '../data/train'))
    validationImagesPath = os.path.normpath(os.path.join(os.getcwd(), '../data/validation'))
    datasetImagesPaths = [testImagesPath, trainImagesPath, validationImagesPath]

    # Cities
    classes = os.listdir(trainImagesPath)

    for city in classes:
        nbImages = 0
        imagesToMove = []

        for dataset in datasetImagesPaths:
            currentPath = os.path.normpath(os.path.join(dataset, city))

            for image in os.listdir(currentPath):
                nbImages += 1
                imagesToMove.append(os.path.normpath(os.path.join(currentPath, image)))
        
        # Dispatching images
        imagesToTest = random.sample(imagesToMove, int(nbImages * percTest))
        imagesToMove = [img for img in imagesToMove if img not in imagesToTest]

        imagesToValidation = random.sample(imagesToMove, int(nbImages * percValidation))
        imagesToMove = [img for img in imagesToMove if img not in imagesToValidation]

        imagesToTrain = random.sample(imagesToMove, int(nbImages * percTrain))
        imagesToMove = [img for img in imagesToMove if img not in imagesToTrain]
        imagesToTrain.extend(imagesToMove) # Dispatching the rest into Training dataset
        imagesToMove = [img for img in imagesToMove if img not in imagesToTrain]

        # Moving images
        for image in imagesToTrain:
            imageFile = os.path.basename(image)
            destPath = os.path.normpath(os.path.join(trainImagesPath, city, imageFile))
            shutil.move(image, destPath)
        
        for image in imagesToTest:
            imageFile = os.path.basename(image)
            destPath = os.path.normpath(os.path.join(testImagesPath, city, imageFile))
            shutil.move(image, destPath)
        
        for image in imagesToValidation:
            imageFile = os.path.basename(image)
            destPath = os.path.normpath(os.path.join(validationImagesPath, city, imageFile))
            shutil.move(image, destPath)

    print('\nImages successfully dispatched.', flush=True)