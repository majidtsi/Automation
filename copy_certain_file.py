'''Escursione nell'albero delle cartelle e ricerca di file con una certa estensione di file ('.jpg','.pdf')
  e copiando da qualunque posizione siano presenti in una nuova cartella'''

import shutil
import os

# Walking through a folder tree
os.makedirs('newfolder', exist_ok=True)
for folders, subfoldes, filenames in os.walk('.'):
    for filename in filenames:
        if filename.endswith('.jpg') or filename.endswith('.pdf'):
            shutil.copy(filename, 'newfolder')