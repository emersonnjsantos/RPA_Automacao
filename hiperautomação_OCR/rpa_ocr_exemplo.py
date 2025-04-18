import rpa as r
import pytesseract
from PIL import Image, ImageEnhance

# Ative o Tesseract (coloque o caminho da sua instalação aqui)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

# --- Etapa RPA ---
r.init()
r.url('https://cdn.pensador.com/img/frase/el/le/ellen_g_white_oracao_e_fe_farao_o_que_nenhum_poder_na_t_lwezn53.jpg')
r.snap('page', 'Captured_Image.png')
r.wait(10)
r.close()

# --- Etapa OCR ---
# Abrir a imagem capturada
imagem = Image.open('Captured_Image.png')

# Converter para escala de cinza
imagem = imagem.convert('L')

# Aumentar o contraste da imagem
enhancer = ImageEnhance.Contrast(imagem)
imagem = enhancer.enhance(2)  # Aumenta o contraste (ajuste conforme necessário)

# Salvar a imagem melhorada
imagem.save('Enhanced_Image.png')

# Usar o Tesseract para extrair texto da imagem melhorada
texto = pytesseract.image_to_string(imagem, lang='eng', config='--psm 6')

print("Texto extraído da imagem:\n")
print(texto)
