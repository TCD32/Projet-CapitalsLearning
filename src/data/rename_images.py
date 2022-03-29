import sys, os

if __name__ == "__main__":
    data_path = os.path.join(os.getcwd(), "../../data/")

    if(len(sys.argv) != 2):
        raise ValueError("Usage : python " + sys.argv[0] + " <city>")
    else:
        city = sys.argv[1]
    
    if(not os.path.isdir(data_path + 'train/' + city)):
        raise ValueError("Error : Could not find " + sys.argv[1] + ", available cities are : " + str(os.listdir(data_path + 'train')))
    
    datasets = os.listdir(data_path)

    idx_image = 0;
    for dataset in datasets:
        city_path = os.path.join(data_path, dataset+'/', city)
        images = os.listdir(city_path)
        for image in images:
            image_path = os.path.join(city_path, image)
            if(not image.endswith('.jpeg')):
                os.remove(image_path)
            else:
                os.rename(image_path, os.path.join(city_path, str(idx_image).join([city, '.jpeg'])))
                idx_image += 1