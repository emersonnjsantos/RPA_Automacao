"""

import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
imagetext = pytesseract.image_to_string(Image.open('Van-Cropped.jpeg'))
print(imagetext)

"""


""" 
tudo em um codigo 
"""


from PIL import Image
import pytesseract
import os
import cv2

# Caminho do executável do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

# Nome da imagem original (sem extensão)
base_filename = "Van"

# Tenta encontrar a imagem com extensão válida
valid_extensions = ['.jpeg', '.jpg', '.png']
image_path = None

for ext in valid_extensions:
    tentative_path = base_filename + ext
    if os.path.exists(tentative_path):
        image_path = tentative_path
        break

if not image_path:
    print("Imagem não encontrada com extensões .jpeg, .jpg ou .png.")
else:
    # Abrir a imagem com PIL
    objImage = Image.open(image_path)
    fltWidth, fltHeight = objImage.size

    # Calcular a área de crop com base nas proporções e margens
    X1 = fltWidth / 3 - 100
    X2 = 2 * fltWidth / 3 + 100
    Y1 = fltHeight / 6
    Y2 = fltHeight / 3
    fltArea = (X1, Y1, X2, Y2)

    # Cortar a imagem
    croppedImage = objImage.crop(fltArea)

    # Salvar a imagem cortada
    cropped_filename = base_filename + "-Cropped.jpeg"
    croppedImage.save(cropped_filename)

    # Ler o texto da imagem cortada com pytesseract
    imagetext = pytesseract.image_to_string(croppedImage)
    print("Texto detectado:")
    print(imagetext)

    # Mostrar a imagem original com OpenCV (modo colorido ou cinza, como quiser)
    #img_cv2 = cv2.imread(image_path  , cv2.IMREAD_COLOR,)
    img_cv2 = cv2.imread(image_path, 0)  # Ou: cv2.IMREAD_GRAYSCALE
    #img_crop_cv2 = cv2.imread(cropped_filename, cv2.IMREAD_COLOR) #se quiser também mostrar o recorte em preto e branco, troque esta:



    cv2.imshow('Imagem Original', img_cv2)
    
    # Também pode mostrar a imagem cortada com OpenCV
    img_crop_cv2 = cv2.imread(cropped_filename, cv2.IMREAD_COLOR)
    cv2.imshow('Imagem Cortada', img_crop_cv2)

    # Espera até pressionar qualquer tecla
    cv2.waitKey(0)
    cv2.destroyAllWindows()


