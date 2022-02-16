#Imports
from my_package.model import ObjectDetectionModel
from my_package.data import Dataset
from my_package.analysis import plot_boxes
from my_package.data.transforms import FlipImage, RescaleImage, BlurImage, CropImage, RotateImage
import matplotlib.pyplot as plt

def experiment(annotation_file, detector, transforms, outputs):
    '''
        Function to perform the desired experiments

        Arguments:
        annotation_file: Path to annotation file
        detector: The object detector
        transforms: List of transformation classes
        outputs: path of the output folder to store the images
    '''

    #Create the instance of the dataset.
    obj = Dataset(annotation_file)
    final_images = []

    #Iterate over all data items.
    for i, dict in enumerate(obj):
        print(i)
        #Get the predictions from the detector.
        pred_boxes, pred_class, pred_score = detector(dict['image'])
        image = dict["image"] * 255
        image = image.transpose(1, 2, 0)
        image = image.astype('uint8')
        #Draw the boxes on the image and save them.
        temp = plot_boxes(image, pred_boxes, pred_class, outputs + "/" +str(i) + ".jpg")
        if i == 8:
            final_images.append(temp)

    #Do the required analysis experiments.
    for i in range(6):
        print("test" +str(i+1))
        obj_new = Dataset(annotation_file, [transforms[i]])
        pred_boxes, pred_class, pred_score = detector(obj_new[8]['image'])
        image = obj_new[8]["image"] * 255
        image = image.transpose(1, 2, 0)
        image = image.astype('uint8')
        #Draw the boxes on the image and save them.
        temp = plot_boxes(image, pred_boxes, pred_class, outputs + "/test" +str(i+1) + ".jpg")
        final_images.append(temp)

    #Showing the 7 asked photos in matplotlib 
    fig, axs = plt.subplots(2, 4)
    axs[0, 0].imshow(final_images[0])
    axs[0, 0].set_title('Normal Image')
    axs[0, 1].imshow(final_images[1])
    axs[0, 1].set_title('Horizontally Flipped Image')
    axs[0, 2].imshow(final_images[2])
    axs[0, 2].set_title('Blurred Image')
    axs[0, 3].imshow(final_images[3])
    axs[0, 3].set_title('2X Rescaled Image')
    axs[1, 0].imshow(final_images[4])
    axs[1, 0].set_title('0.5X Rescaled Image')
    axs[1, 1].imshow(final_images[5])
    axs[1, 1].set_title('90 degree Right Rotated Image')
    axs[1, 2].imshow(final_images[6])
    axs[1, 2].set_title('45 degree Left Rotated Image')
    plt.show()
    
def main():
    detector = ObjectDetectionModel()
    experiment('./data/annotations.jsonl', detector, [FlipImage("horizontal"), BlurImage(1), RescaleImage(2.0), RescaleImage(0.5), RotateImage(-90), RotateImage(45)], "/home/suhas/Desktop/Semester-4/SL/Lab-4/AssignmentQs2/Output") # Sample arguments to call experiment()

if __name__ == '__main__':
    main()