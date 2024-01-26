from PIL import Image
image  = Image.open("ascii_grey.png")
pixels = list(image.getdata())
ascii  = "".join([chr(pixel) for pixel in pixels])
with open("text_output.txt", "w") as file:
    file.write(ascii)
