#Imports
from PIL import Image 

class RescaleImage(object):
    '''
        Rescales the image to a given size.
    '''

    def __init__(self, output_size):
        '''
            Arguments:
            output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
        '''
        self.output_size = output_size
        # Write your code here

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)

            Note: You do not need to resize the bounding boxes. ONLY RESIZE THE IMAGE.
        '''
        width, height = image.size
        if(isinstance(self.output_size, float)):
            width = int(width*self.output_size)
            height = int(height*self.output_size)
            out = image.resize((width, height))
        
        elif(isinstance(self.output_size, int)):
            if width < height:
                width1 = self.output_size
                height1 = round(height / width * width1)
            else:
                height1 = self.output_size
                width1 = round(width / height * height1)
            out = image.resize((width1, height1))

        else:
            out = image.resize(self.output_size)

        return out