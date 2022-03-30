import os

def get_classes():
    data_path = "../data/"
    classes = os.listdir(data_path + 'train/')

    return classes