# Text to Image and Image to Text Converter
This Python project allows you to convert text into an ASCII image and back from an ASCII image to text. The code was inspired by the blog post "Compressing Text into Images" by Terence Eden's. (https://shkspr.mobi/blog/2024/01/compressing-text-into-images/).

# Usage

## Text to Image (text_to_image.py)
Place the text you want to convert in a file named text_input.txt in the same directory as text_to_image.py.
Run text_to_image.py to convert the text into an ASCII image.
The ASCII image will be saved as ascii_grey.png.

## Image to Text (image_to_text.py)
Ensure you have an ASCII image named ascii_grey.png in the same directory as image_to_text.py.
Run image_to_text.py to convert the ASCII image back to text.
The text will be saved in a file named text_output.txt.
Customization

You can customize the width of the ASCII image by modifying the width variable in text_to_image.py. Adjusting this value will affect the width of the resulting image.

## Dependencies
This project uses the Python Imaging Library (PIL) for image processing. You can install it using pip if you don't already have it:

```bash
pip install pillow
```

## Example
An example input text file text_input.txt and the resulting ASCII image ascii_grey.png are provided in this repository for demonstration purposes.

## License
This project is open-source and available under the MIT License. Feel free to use and modify the code as needed.

