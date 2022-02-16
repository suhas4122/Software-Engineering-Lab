#Imports
import random 
from PIL import Image

class CropImage(object):
    '''
        Performs either random cropping or center cropping.
    '''

    def __init__(self, shape, crop_type='center'):
        '''
            Arguments:
            shape: output shape of the crop (h, w)
            crop_type: center crop or random crop. Default: center
        '''
        self.w = shape[0]
        self.h = shape[1]
        self.crop = crop_type
        # Write your code here

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''
        # Write your code here
        width, height = image.size
        print(width,)
        if(self.crop == "center"):
            centerW = width/2
            centerH = height/2            
            
        if(self.crop == "random"):
            centerW = random.randint(0, width-self.w) + self.w/2
            centerH = random.randint(0, height-self.h) + self.h/2

        return image.crop((centerW - self.w/2 , centerH-self.h/2 , centerW + self.w/2 ,  centerH+self.h/2))
            
 