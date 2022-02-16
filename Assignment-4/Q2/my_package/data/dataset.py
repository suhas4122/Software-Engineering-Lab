#Imports
import jsonlines
import numpy as np
from PIL import Image

class Dataset(object):
    '''
        A class for the dataset that will return data items as per the given index
    '''

    def __init__(self, annotation_file, transforms = []):
        '''
            Arguments:
            annotation_file: path to the annotation file
            transforms: list of transforms (class instances)
                        For instance, [<class 'RandomCrop'>, <class 'Rotate'>]
        '''
        self.img_paths = []
        self.bboxes = []
        with jsonlines.open(annotation_file) as f:
            for line in f.iter():
                self.img_paths.append(line["img_fn"]) 
                self.bboxes.append(line["bboxes"])
        self.transforms = transforms


    def __len__(self):
        '''
            return the number of data points in the dataset
        '''
        return len(self.img_paths)

        

    def __getitem__(self, idx):
        '''
            return the dataset element for the index: "idx"
            Arguments:
                idx: index of the data element.

            Returns: A dictionary with:
                image: image (in the form of a numpy array) (shape: (3, H, W))
                gt_bboxes: N X 5 array where N is the number of bounding boxes, each 
                            consisting of [class, x1, y1, x2, y2]
                            x1 and x2 lie between 0 and width of the image,
                            y1 and y2 lie between 0 and height of the image.

            You need to do the following, 
            1. Extract the correct annotation using the idx provided.
            2. Read the image and convert it into a numpy array (wont be necessary
                with some libraries). The shape of the array would be (3, H, W).
            3. Scale the values in the array to be with [0, 1].
            4. Create a dictonary with both the image and annotations
            4. Perform the desired transformations.
            5. Return the transformed image and annotations as specified.
        '''

        edit_path = "/home/suhas/Desktop/Semester-4/SL/Lab-4/AssignmentQs2/data/"
        img = Image.open(edit_path + self.img_paths[idx])
        for x in self.transforms:
            img = x(img)

        gt_bboxes = []
        for x in self.bboxes[idx]:
            arr = []
            arr.append(x["category"])
            arr = [*arr, *x["bbox"]] 
            gt_bboxes.append(arr)
        
        img_arr = np.array(img)
        img_arr = img_arr.transpose(2, 0, 1)
        img_arr = img_arr.astype('float32')
        img_arr /= 255.0
        
        my_dict = {"image" : img_arr, "gt_bboxes" : gt_bboxes}
        return my_dict

# cropper = crop.CropImage((200, 200), "center")
# flipper = flip.FlipImage("vertical")
# rescaler = rescale.RescaleImage(2.0)
# blurrer = blur.BlurImage(3)
# rotater = rotate.RotateImage(10)
# c = Dataset("/home/suhas/Desktop/Semester-4/SL/Lab-4/AssignmentQs2/data/annotations.jsonl", [cropper])
# print(c[8])