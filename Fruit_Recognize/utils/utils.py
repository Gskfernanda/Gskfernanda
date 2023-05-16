import random 
import matplotlib.pyplot as plt
import os
import matplotlib.image as mimg

class Utils:
    
    def __init__(self) -> None:
        pass
    
    def view_random_img(target_dir, target_class):
        target_folder = target_dir+"/"+target_class
        
        #Get a random image path
        random_image = random.sample(os.listdir(target_folder), 1)
        
        #Read the img and plot using matplotlib
        img = mimg.imread(target_folder + "/" + random_image[0])
        plt.imshow(img)
        plt.title(target_class)
    
        
        print(f'Image shape: {img.shape}')
        return img