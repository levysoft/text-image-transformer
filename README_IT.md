# Text to Image and Image to Text Converter
Questo progetto Python ti consente di convertire il testo in un'immagine ASCII e viceversa, da un'immagine ASCII a testo. Il codice è stato ispirato dall'articolo del blog "Comprimere il Testo in Immagini" di Terence Eden (https://shkspr.mobi/blog/2024/01/compressing-text-into-images/).

# Utilizzo

## Da Testo a Immagine (`text_to_image.py`)
1. Metti il testo che desideri convertire in un file chiamato `text_input.txt` nella stessa directory di `text_to_image.py`.
2. Esegui `text_to_image.py` per convertire il testo in un'immagine ASCII.
3. L'immagine ASCII verrà salvata come `ascii_grey.png`.

## Da Immagine a Testo (`image_to_text.py`)
1. Assicurati di avere un'immagine ASCII chiamata `ascii_grey.png` nella stessa directory di `image_to_text.py`.
2. Esegui `image_to_text.py` per convertire l'immagine ASCII nuovamente in testo.
3. Il testo verrà salvato in un file chiamato `text_output.txt`.

## Personalizzazione
Puoi personalizzare la larghezza dell'immagine ASCII modificando la variabile `width` in `text_to_image.py`. Modificando questo valore influenzerai la larghezza dell'immagine risultante.

## Dipendenze
Questo progetto utilizza la libreria Python Imaging Library (PIL) per l'elaborazione delle immagini. Puoi installarla utilizzando `pip` se non l'hai già installata:

```bash
pip install pillow
```

## Esempio
Un file di testo di input di esempio text_input.txt e l'immagine ASCII risultante ascii_grey.png sono forniti in questo repository a scopo dimostrativo.

## Licenza
Questo progetto è open-source ed è disponibile sotto la Licenza MIT. Sentiti libero di utilizzare e modificare il codice a tuo piacimento.
