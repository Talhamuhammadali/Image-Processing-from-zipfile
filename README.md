# Image Processing from ZIP File

## Description
This Python project involves processing images within a provided ZIP file containing newspaper images. The task is to search through these images for occurrences of names and faces. The script will utilize various libraries to perform tasks such as face detection, optical character recognition (OCR), and image composition to create contact sheets. This was done to complete Courseas Python3 Specilization.

## Requirements
- Python
- [zipfile](https://docs.python.org/3/library/zipfile.html): Python's built-in library for working with ZIP files. Used to extract images from the provided ZIP file.
- [PIL](https://pillow.readthedocs.io/en/stable/): Python Imaging Library. Utilized for image processing tasks such as image opening, manipulation, and contact sheet creation.
- [pytesseract](https://github.com/madmaze/pytesseract): Python wrapper for Google's Tesseract OCR engine. Enables optical character recognition to search for keywords within images.
- [OpenCV (cv2)](https://opencv.org/): Open Source Computer Vision Library. Used for face detection within images and other computer vision tasks.


## Installation
1. Clone the repository:
    ```
       gh repo clone Talhamuhammadali/Image-Processing-from-zipfile
    ``` 
2. Setup Virtual Envirnoment:
       ```
    python3 -m venv myenv
   ```
       ON Windows:
           ```
               myenv\Scripts\activate
           ```
       ON Linux:
           ```
               source myenv/bin/activate
           ```
4. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
    
   
## Usage
1. Place the ZIP file containing newspaper images in the files folder.
2. Run the script `image_processing.py`.
    ```
    python image_processing.py --name "anyname"
    ```
   Replace `"anyname"` with the desired name to search for.

## Features
- **Face Detection:** Utilizes OpenCV for detecting faces within images.
- **Keyword Search:** Performs OCR using Tesseract to search for specific keywords within the images.
- **Contact Sheet Generation:** Uses PIL to composite images with detected faces into contact sheets.

## Example
A zip file is included in the files folder. Use script to find 'Christopher' by using:
```
    python image_processing.py files/project.zip --name "Christopher"
```
The processing takes ~15-20m for me.
The results are saved in the main folder. the result for this case is:
![image](https://github.com/Talhamuhammadali/Image-Processing-from-zipfile/assets/46277852/733db39f-11d9-405c-ab31-0024dbcdc4e7)

Try the following example:
```
    python image_processing.py files/project.zip --name "Mark"
```


