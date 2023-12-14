# Image Processing from ZIP File

## Description
This Python project involves processing images within a provided ZIP file containing newspaper images. The task is to search through these images for occurrences of keywords and faces. The script will utilize various libraries to perform tasks such as face detection, optical character recognition (OCR), and image composition to create contact sheets.

## Requirements
- Python
- [zipfile](https://docs.python.org/3/library/zipfile.html): Python's built-in library for working with ZIP files. Used to extract images from the provided ZIP file.
- [PIL](https://pillow.readthedocs.io/en/stable/): Python Imaging Library. Utilized for image processing tasks such as image opening, manipulation, and contact sheet creation.
- [pytesseract](https://github.com/madmaze/pytesseract): Python wrapper for Google's Tesseract OCR engine. Enables optical character recognition to search for keywords within images.
- [OpenCV (cv2)](https://opencv.org/): Open Source Computer Vision Library. Used for face detection within images and other computer vision tasks.


## Installation
1. Clone the repository:
    ```
    git clone https://github.com/Talhamuhammadali/Image-Processing-from-zipfile
.git
    ```
2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
   
## Usage
1. Place the ZIP file containing newspaper images in the designated folder.
2. Run the script `image_processing.py`.
    ```
    python image_processing.py --keyword "pizza"
    ```
   Replace `"pizza"` with the desired keyword to search for.

## Features
- **Face Detection:** Utilizes OpenCV for detecting faces within images.
- **Keyword Search:** Performs OCR using Tesseract to search for specific keywords within the images.
- **Contact Sheet Generation:** Uses PIL to composite images with detected faces into contact sheets.

## Example
Include an example or screenshot demonstrating how to run the script and what the output looks like.

## Contributors
- [Your Name](link_to_profile): Role in the project

## License
This project is licensed under the [License Name](link_to_license).
