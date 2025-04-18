from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import urllib.parse
import random

# Lista de números de telefone e mensagens
contacts = [
    ("+554598235723", "Hello"),
    ("+14155238886", "Hello"),
    ("+554599204507", "Hello"),
    ("+554599448481", "Hello")
]

# ID do grupo
group_id = "Bs6g7BpUYwB4nbB3wOQcgl"

# Configurar o navegador com WebDriver Manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 5)  # Espera explícita de até 20 segundos

driver.get("https://web.whatsapp.com")
print("✅ Escaneie o QR code do WhatsApp Web e pressione Enter quando estiver pronto...")
input()

# Função para enviar mensagem a um número
def send_message_to_number(number, message):
    encoded_message = urllib.parse.quote(message)
    driver.get(f"https://web.whatsapp.com/send?phone={number}&text={encoded_message}")
    try:
        # Espera até que o campo de mensagem esteja disponível
        input_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@title="Digite uma mensagem"]')))
        input_box.send_keys(message)
        input_box.send_keys(Keys.ENTER)
        time.sleep(random.randint(2, 4))  # Pequena pausa aleatória
        print(f"✅ Mensagem enviada para {number}")
    except Exception as e:
        print(f"❌ Erro ao enviar para {number}: {e}")

# Função para enviar mensagem a um grupo
def send_message_to_group(group_id, message):
    driver.get(f"https://web.whatsapp.com/group?invite_code={group_id}")
    try:
        input_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@title="Digite uma mensagem"]')))
        input_box.send_keys(message)
        input_box.send_keys(Keys.ENTER)
        time.sleep(2)
        print(f"✅ Mensagem enviada para o grupo {group_id}")
    except Exception as e:
        print(f"❌ Erro ao enviar para o grupo {group_id}: {e}")

# Enviar mensagens para os contatos
for number, message in contacts:
    send_message_to_number(number, message)

# Enviar mensagem para o grupo
send_message_to_group(group_id, "Hello!")

# Fechar o navegador
driver.quit()








"""
import pywhatkit

# Enviando mensagem para o número original
pywhatkit.sendwhatmsg_instantly("+554598031634", "Hello")

# Enviando mensagem para os quatro novos números de contato
pywhatkit.sendwhatmsg_instantly("+554598235723", "Hello")
pywhatkit.sendwhatmsg_instantly("+14155238886", "Hello")
pywhatkit.sendwhatmsg_instantly("+554599204507", "Hello")
pywhatkit.sendwhatmsg_instantly("+554599448481", "Hello")

# Enviando mensagem para o grupo
pywhatkit.sendwhatmsg_to_group_instantly("Bs6g7BpUYwB4nbB3wOQcgl", "Hello!")
"""