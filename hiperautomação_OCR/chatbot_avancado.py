import nltk
from nltk.chat.util import Chat
import random

# Reflexões em português — versão avançada
reflexoes_avancadas = {
    "eu sou": "você é",
    "eu estou": "você está",
    "eu estava": "você estava",
    "eu tenho": "você tem",
    "eu": "você",
    "meu": "seu",
    "minha": "sua",
    "meus": "seus",
    "minhas": "suas",
    "você é": "eu sou",
    "você está": "eu estou",
    "você tem": "eu tenho",
    "você": "eu",
    "seu": "meu",
    "sua": "minha",
    "seus": "meus",
    "suas": "minhas",
    "estou": "está",
    "sou": "é",
    "era": "era"
}

# Respostas dinâmicas
boas_vindas = [
    "Olá! Bem-vindo ao suporte virtual inteligente.",
    "Oi! Sou seu assistente virtual de TI.",
    "Seja bem-vindo! Como posso te ajudar hoje?"
]

# Regras do chatbot (em português)
pares = [
    [
        r"(.*)(olá|oi|boa tarde|bom dia)(.*)",
        [random.choice(boas_vindas)]
    ],
    [
        r"meu nome é (.*)",
        ["Prazer em te conhecer, %1! Como posso te ajudar?"]
    ],
    [
        r"(estou bem|tudo certo|tudo bem|beleza|de boa)",
        ["Fico feliz em saber disso! 😄 No que posso te ajudar hoje?",
         "Ótimo! Vamos resolver o que você precisar."]
    ],
    [
        r"(.*)instalar(.*)",
        ["Claro, posso te ajudar com isso. Qual software deseja instalar? Use o formato: Software: nome"]
    ],
    [
        r"(.*)problema(.*)|(.*)erro(.*)|(.*)falha(.*)",
        ["Entendo. Poderia descrever o problema? Ou escolha uma opção:\n1) Atualizar versão\n2) Desinstalar"]
    ],
    [
        r"software:(.*)",
        ["Entendido! Criando um chamado para instalação do software: %1.\nVocê será contatado em breve."]
    ],
    [
        r"(.*)(atualizar|versão)(.*)",
        ["Certo, vamos providenciar a atualização. Um técnico será designado para isso."]
    ],
    [
        r"(.*)(desinstalar|remover)(.*)",
        ["A desinstalação será registrada. Um membro da equipe de TI irá cuidar disso pra você."]
    ],
    [
        r"(obrigado|valeu|agradecido)",
        ["De nada! 😄 Posso ajudar com mais alguma coisa?"]
    ],
    [
        r"(não|nao|nada mais|encerrar)",
        ["Tudo certo então. Tenha um excelente dia! 👋"]
    ],
    [
        r"(.*)",
        ["Desculpe, não entendi muito bem. Poderia reformular ou tentar de outra forma?"]
    ],
]

# Início da conversa
print("🧠 SUPORTE VIRTUAL INTELIGENTE")
print("Digite 'encerrar' a qualquer momento para sair.\n")

# Inicia o chatbot
chat = Chat(pares, reflexoes_avancadas)
chat.converse(quit="encerrar")
