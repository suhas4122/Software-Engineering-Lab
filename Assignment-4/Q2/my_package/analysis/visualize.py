#Imports
from PIL import Image, ImageDraw, ImageFont

def plot_boxes(image, boxes, names, path): # Write the required arguments
  image = Image.fromarray(image)
  img1 = ImageDraw.Draw(image)

  font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 25)

  for i, box in enumerate(boxes[:5]):
    box = tuple(box)
    img1.rectangle(box, outline ="black")
    img1.text((box[0][0], box[0][1]-25), names[i], fill = "black" ,font = font, stroke_width = 1)

  image.save(fp = path)
  return image
  # The function should plot the predicted boxes on the images and save them.
  # Tip: keep the dimensions of the output image less than 800 to avoid RAM crashes.
  
