import zipfile
import matplotlib.pyplot as plt
import argparse
import pytesseract
import cv2 as cv
import numpy as np
from PIL import Image,ImageDraw
# loading the face detection classifier
face_cascade = cv.CascadeClassifier('myenv/lib/python3.10/site-packages/cv2/data/haarcascade_frontalface_default.xml')

class ImageProccessing:
    def __init__(self, path, keyword) -> None:
        self.data = {}
        self.path = path
        self.keyword = keyword

    def load_data(self):
        """
        The load_data function takes a path to a zip file as input and returns
        a dictionary of the form {filename: [PIL.Image, text, faces]} where filename is
        the name of the image file in the zip archive without its extension (e.g., 'A' or 'B'), 
        PIL.Image is an instance of PIL Image class corresponding to that image, 
        text is a string containing all text present in that image extracted using pytesseract's 
        image_to_string function and faces is an array containing bounding boxes for each face detected by OpenCV's detectMultiScale
        
        :param path: Specify the path to the zip file
        :return: Processed data from image including faces, text etc
        """
        with zipfile.ZipFile(self.path,'r') as file:
            fnames = [name for name in file.namelist()]
            for n in fnames:
                with file.open(n) as img_data:
                    img = cv.imdecode(np.frombuffer(img_data.read(), np.uint8),1)
                    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
                    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                    im = Image.open(img_data)
                    text = pytesseract.image_to_string(im)
                    self.data[n] = [im,text,faces]
        return self.data

    def search(self):
        #pasted crops dimension
        pw = 120
        ph = 120
        
        for key in self.data.keys():
            if self.keyword in self.data[key][1]:
                img = self.data[key][0]
                faces = self.data[key][2]
                rows = int(np.ceil(len(faces)/5))
                sheet = Image.new(self.data[key][0].mode,(pw*5,ph*rows))#rx5 sheet for 120x120 image
                if len(faces) == 0:
                    print("Results found in file {}".format(key))
                    print("But there were no faces in that file!")
                else:
                    #sheet location for pasting
                    sx = 0
                    sy = 0
                    for x,y,w,h in faces:
                        face = img.crop((x,y,x+w,y+h))
                        if face.width > pw:
                            face = face.resize((pw,ph))
                            sheet.paste(face,(sx,sy))
                        else:
                            sheet.paste(face,(sx,sy))
                        if sx + pw == sheet.width:
                            sx = 0
                            sy += face.height
                        else:
                            sx += pw
                            
                    print("Results found in file {}".format(key))
                self.show_sheet(sheet)
                sheet.save(f"result_{key}.png")          
        return 0
    
    def show_sheet(self, sheet):
        plt.imshow(sheet)
        plt.axis('off')
        plt.show()


if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description='Search for a name in images within a ZIP file')
    # parser.add_argument('zip_file', help='Path to the ZIP file containing images')
    # parser.add_argument('--name', help='name to search for in the images', required=True)
    # # example search 'Christopher' path 'files/project'
    # args = parser.parse_args()
    proccessor = ImageProccessing(
        path='files/project.zip',
        keyword='Christopher'
    )
    proccessor.load_data()
    proccessor.search()