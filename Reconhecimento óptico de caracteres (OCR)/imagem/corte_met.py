from PIL import Image

# Abre a imagem
objImage = Image.open("Image of a Bird.jpg")

# Obtém largura e altura
width, height = objImage.size

# Define a área de corte para a metade esquerda
crop_area = (
    0,                   # esquerda (começo)
    0,                   # topo (começo)
    int(width / 2),      # direita (metade)
    height               # baixo (final)
)

# Faz o corte
cropped_image = objImage.crop(crop_area)

# Salva a nova imagem
cropped_image.save("Cropped_Left_Half_of_Image.jpg")

# Mostra para confirmar
print("Corte realizado! Área da nova imagem:", cropped_image.size)
