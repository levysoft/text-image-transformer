# Text to Image and Image to Text Converter
Questo progetto Python consente di convertire testo in immagini ASCII e viceversa, da immagini ASCII a testo. Il codice è ispirato all'articolo del blog "Compressing Text Into Images" di Terence Eden (https://shkspr.mobi/blog/2024/01/compressing-text-into-images/).

# Utilizzo

## Da Testo a Immagine (`text_to_image.py`)
1. Inserisci il testo che desideri convertire in un file denominato `text_input.txt` nella stessa directory di `text_to_image.py`.
2. Esegui `text_to_image.py` per convertire il testo in un'immagine ASCII.
3. L'immagine ASCII verrà salvata con il nome `ascii_grey.png`.

## Da Immagine a Testo (`image_to_text.py`)
1. Assicurati di avere un'immagine ASCII denominata `ascii_grey.png` nella stessa directory di `image_to_text.py`.
2. Esegui `image_to_text.py` per convertire l'immagine ASCII nuovamente in testo.
3. Il testo verrà salvato in un file denominato `text_output.txt`.

## Personalizzazione
Puoi personalizzare la larghezza dell'immagine ASCII modificando la variabile `width` in `text_to_image.py`. Modificare questo valore influenzerà la larghezza dell'immagine risultante.

## Test con Immagini di Grandi Dimensioni
Se hai la necessità di eseguire test con immagini di grandi dimensioni, puoi fare riferimento a questo repository: [dscape/spell - test/resources/big.txt](https://github.com/dscape/spell/blob/master/test/resources/big.txt). Troverai un esempio di file di testo di grandi dimensioni che può essere utilizzato per valutare le prestazioni dello script.

## Dipendenze
Questo progetto utilizza la libreria Python Imaging Library (PIL) per l'elaborazione delle immagini. Puoi installarla utilizzando `pip` se non l'hai già installata:

```bash
pip install pillow
```

## Esempio
Un file di testo di esempio denominato `text_input.txt` e l'immagine ASCII risultante `ascii_grey.png` sono inclusi in questo repository a scopo dimostrativo.

## Licenza
Questo progetto è open-source ed è disponibile sotto la Licenza MIT. Sentiti libero di utilizzare e modificare il codice a tuo piacimento.
