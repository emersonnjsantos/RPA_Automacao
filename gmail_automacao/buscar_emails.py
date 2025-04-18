import os
import base64
import pandas as pd
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Escopo de leitura dos e-mails
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def autenticar_gmail():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

def buscar_emails(service, max_results=100):
    resultado = service.users().messages().list(userId='me', maxResults=max_results).execute()
    mensagens = resultado.get('messages', [])
    dados = []

    for msg in mensagens:
        mensagem = service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
        headers = mensagem['payload'].get('headers', [])
        assunto = remetente = data = ''

        for header in headers:
            if header['name'] == 'Subject':
                assunto = header['value']
            elif header['name'] == 'From':
                remetente = header['value']
            elif header['name'] == 'Date':
                data = header['value']

        dados.append({
            'Remetente': remetente,
            'Assunto': assunto,
            'Data': data
        })

    return dados

def salvar_csv(dados, nome_arquivo='emails.csv'):
    df = pd.DataFrame(dados)
    df.to_csv(nome_arquivo, index=False, encoding='utf-8')
    print(f'\n✅ Arquivo CSV "{nome_arquivo}" criado com sucesso!')

if __name__ == '__main__':
    print("🔐 Autenticando com o Gmail...")
    service = autenticar_gmail()
    print("📥 Buscando e-mails...")
    dados_emails = buscar_emails(service, max_results=100)  # Pode mudar para 500, 1000...
    print("💾 Salvando em CSV...")
    salvar_csv(dados_emails)
