from PIL import Image
import textwrap

# Leggi il testo da 'rj.txt'
with open('text_input.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Converti il testo in una lista di valori ASCII
ascii_values = [ord(char) for char in text]

# Calcola la larghezza e l'altezza dell'immagine
width = 1800 #256  # Puoi regolare questa larghezza
height = (len(ascii_values) + width - 1) // width  # Altezza per contenere tutti i caratteri

# Crea un'immagine in scala di grigi con i valori ASCII
image = Image.new('L', (width, height))
image.putdata(ascii_values[:width*height])  # Tronca o riempie i dati per adattarsi all'immagine

# Salva l'immagine
image.save('ascii_grey.png')

