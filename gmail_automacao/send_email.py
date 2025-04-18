"""
import os
from email.message import EmailMessage
import ssl
import smtplib
from dotenv import load_dotenv

# Carregar variáveis de ambiente de um arquivo .env
load_dotenv()

# Configurações do e-mail
strSender = 'emer7681@gmail.com'  # Substitua pelo seu Gmail
strReceiver = 'santson7681@gmail.com'  # Substitua pelo destinatário
strPassword = os.getenv('EMAIL_PASSWORD')  # Senha de aplicativo (armazenada no .env)
strSubject = 'Learning Email Sending with Python'

# Corpo do e-mail (texto simples ou HTML)
strBody = 
#Learning how to send emails using Python.
 """
"""""
# Criar o e-mail
objEmail = EmailMessage()
objEmail['From'] = strSender
objEmail['To'] = strReceiver
objEmail['Subject'] = strSubject
objEmail.set_content(strBody)
# Para corpo em HTML, descomente abaixo:
# objEmail.add_alternative("<h1>Learning Python Email</h1><p>This is a test.</p>", subtype='html')

# Configurar conexão segura
objContext = ssl.create_default_context()

try:
    # Conectar ao servidor SMTP do Gmail
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=objContext) as objSMTP:
        objSMTP.login(strSender, strPassword)
        objSMTP.sendmail(strSender, strReceiver, objEmail.as_string())
    print("E-mail enviado com sucesso!")
except Exception as e:
    print(f"Erro ao enviar e-mail: {e}")

    """


import os
import time
import pandas as pd
from email.message import EmailMessage
import ssl
import smtplib
from dotenv import load_dotenv

# Carregar variáveis de ambiente Senhas
load_dotenv()

# Configurações do e-mail
strSender = 'emer7681@gmail.com'  # Substitua pelo seu Gmail
strPassword = os.getenv('EMAIL_PASSWORD')  # Senha de aplicativo no .env
strSubject = 'Learning Email Sending with Python'

# Ler lista de e-mails do CSV
try:
    df = pd.read_csv('emails.csv')
except FileNotFoundError:
    print("Erro: Arquivo 'emails.csv' não encontrado.")
    exit()

# Configurar conexão segura
objContext = ssl.create_default_context()

def send_email_batch(recipients, batch_number):
    """Enviar e-mails para um lote de destinatários."""
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=objContext) as objSMTP:
            objSMTP.login(strSender, strPassword)
            for index, row in recipients.iterrows():
                email = row['email']
                # Personalizar o corpo do e-mail (se houver nome)
                nome = row.get('nome', 'Destinatário')
                strBody = f"Olá, {nome},\n\nLearning how to send emails using Python."
                
                # Criar o e-mail
                objEmail = EmailMessage()
                objEmail['From'] = strSender
                objEmail['To'] = email
                objEmail['Subject'] = strSubject
                objEmail.set_content(strBody)
                
                # Enviar
                objSMTP.sendmail(strSender, email, objEmail.as_string())
                print(f"E-mail enviado para {email} (Lote {batch_number})")
    except Exception as e:
        print(f"Erro no lote {batch_number}: {e}")

# Enviar e-mails em lotes de 50
batch_size = 50
for i in range(0, len(df), batch_size):
    batch = df[i:i + batch_size]
    print(f"Enviando lote {i//batch_size + 1} ({len(batch)} e-mails)...")
    send_email_batch(batch, i//batch_size + 1)
    if i + batch_size < len(df):  # Não esperar após o último lote
        print("Aguardando 30 segundos antes do próximo lote...")
        time.sleep(30)


