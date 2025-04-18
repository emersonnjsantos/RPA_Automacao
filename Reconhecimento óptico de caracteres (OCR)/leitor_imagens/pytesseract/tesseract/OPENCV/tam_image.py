


""""
#aqui ele calcula o tamanho da imagem
from PIL import Image
objImage = Image.open("Van.jpeg")
fltWidth,fltHeight = objImage.size
print(fltWidth,fltHeight)

(venv) PS D:\rpa_app> python tam_image.py
1274 880
(venv) PS D:\rpa_app> 

"""



"""

 sua imagem Van.jpg tem as dimensões:

Largura (width): 1274 pixels

Altura (height): 880 pixels

Agora, com base nas proporções descritas no trecho do livro, podemos calcular as coordenadas para fazer o crop da parte da imagem que contém o texto "SCHOOL BUS", adaptando para o seu tamanho real.

Passos:
X1 = 1/3 da largura - 100

X2 = 2/3 da largura + 100

Y1 = 1/6 da altura

Y2 = 1/3 da altura

Vamos fazer as contas com base em 1274x880:

"""

from PIL import Image

objImage = Image.open("Van.jpeg")
fltWidth, fltHeight = objImage.size

X1 = fltWidth / 3 - 100        # 1274 / 3 ≈ 424.67 - 100 ≈ 324.67
X2 = 2 * fltWidth / 3 + 100    # 2*424.67 ≈ 849.33 + 100 ≈ 949.33
Y1 = fltHeight / 6            # 880 / 6 ≈ 146.67
Y2 = fltHeight / 3            # 880 / 3 ≈ 293.33

fltArea = (X1, Y1, X2, Y2)
objImage = objImage.crop(fltArea)
objImage.save("Van-Cropped.jpeg")


