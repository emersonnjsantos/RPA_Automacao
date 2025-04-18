import time
import pandas as pd
import datetime
import pywhatkit
from email.message import EmailMessage
import ssl
import smtplib
import os
from pathlib import Path

# Configurações
SENDER_EMAIL = 'emer7681@gmail.com'  # Substitua pelo seu e-mail
SENDER_PASSWORD = os.getenv('EMAIL_PASSWORD')  # Lê a senha do arquivo .env
EXCEL_PATH = r'C:\Users\emer7\OneDrive\Área de Trabalho\Data.xlsx'  # Corrija conforme o caminho está para o arquivo
SUBJECT = 'Happy Birthday!'
BODY_TEMPLATE = "Dear {name},\n\nWish you a very happy birthday!\nBest regards,\nYour Team"

# Função para enviar e-mail
def send_email(sender, password, receiver, subject, body):
    try:
        email_msg = EmailMessage()
        email_msg['From'] = sender
        email_msg['To'] = receiver
        email_msg['Subject'] = subject
        email_msg.set_content(body)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(sender, password)
            smtp.sendmail(sender, receiver, email_msg.as_string())
        print(f"E-mail enviado para {receiver}")
    except Exception as e:
        print(f"Erro ao enviar e-mail para {receiver}: {e}")

# Função para enviar mensagem WhatsApp
def send_whatsapp(number, name):
    try:
        message = f"Hello {name}, This is a test message sent using Python."
        pywhatkit.sendwhatmsg_instantly(f"+{number}", message)
        time.sleep(10)  # Ajuste conforme necessário
        print(f"Mensagem WhatsApp enviada para {number}")
    except Exception as e:
        print(f"Erro ao enviar mensagem WhatsApp para {number}: {e}")

# Leitura do arquivo Excel
try:
    df = pd.read_excel(EXCEL_PATH)
except FileNotFoundError:
    print(f"Arquivo {EXCEL_PATH} não encontrado.")
    exit(1)
except Exception as e:
    print(f"Erro ao ler o arquivo Excel: {e}")
    exit(1)

# Verifica se as colunas necessárias existem
required_columns = ['Birthday', 'Name', 'WhatsApp No', 'Email ID']
if not all(col in df.columns for col in required_columns):
    print(f"O arquivo Excel deve conter as colunas: {required_columns}")
    exit(1)

# Data atual no formato MM-DD
today = datetime.datetime.now().strftime("%m-%d")

# Loop pelas linhas do DataFrame
for index, row in df.iterrows():
    birthday = pd.to_datetime(row['Birthday']).strftime("%m-%d")
    
    # Verifica se é o aniversário
    if birthday == today:
        name = row['Name']
        whatsapp_no = str(row['WhatsApp No']).replace("+", "")  # Remove "+" se presente
        email = row['Email ID']
        
        # Envia mensagem WhatsApp
        send_whatsapp(whatsapp_no, name)
        
        # Envia e-mail
        body = BODY_TEMPLATE.format(name=name)
        send_email(SENDER_EMAIL, SENDER_PASSWORD, email, SUBJECT, body)

print("Processo concluído.")