from PIL import Image

# Abre a imagem
objImage = Image.open("Image of a Bird.jpg")

# Obtém largura e altura
width, height = objImage.size

# Define a área de corte (tirando 1/5 da borda de cada lado)
crop_area = (
    int(width / 5),        # esquerda
    int(height / 5),       # topo
    int(4 * width / 5),    # direita
    int(4 * height / 5)    # baixo
)

# Faz o corte
cropped_image = objImage.crop(crop_area)

# Salva a nova imagem
cropped_image.save("Cropped Image of a Bird.jpg")

# Mostra para confirmar
print("Corte realizado! Área da nova imagem:", cropped_image.size)
