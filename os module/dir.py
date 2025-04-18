
"""

🎯 Aqui está um script completo que:

Pergunta ao usuário se ele quer criar ou apagar a pasta,

Trabalha com a pasta "Test Folder" no diretório atual (onde o script estiver),

Mostra mensagens claras sobre o que aconteceu.

"""
import os
import shutil

folder_name = "Test Folder"
folder_path = os.path.join(os.getcwd(), folder_name)

print("O que você deseja fazer?")
print("1 - Criar pasta")
print("2 - Apagar pasta")
opcao = input("Digite a opção (1 ou 2): ")

if opcao == "1":
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        print(f"Pasta '{folder_name}' criada com sucesso!")
    else:
        print(f"A pasta '{folder_name}' já existe.")

elif opcao == "2":
    if os.path.exists(folder_path):
        try:
            shutil.rmtree(folder_path)
            print(f"Pasta '{folder_name}' removida com sucesso!")
        except Exception as e:
            print(f"Erro ao remover a pasta: {e}")
    else:
        print(f"A pasta '{folder_name}' não existe.")

else:
    print("Opção inválida. Por favor, escolha 1 ou 2.")






"""


import os
 
if not os.path.exists('Test Folder'):
    os.mkdir('Test Folder')

    """


"""
    📌 Onde a pasta vai aparecer?
Ela será criada no diretório de trabalho atual, que no seu caso é:

makefile
Copiar código
D:\rpa_app
Se você quiser criar essa pasta na área de trabalho, precisa especificar o caminho como fizemos antes.

    """

"""
Excluir um diretório: Esta funcionalidade pode ser usada para excluir um diretório existente e todo o conteúdo dentro dele também. Copie e execute o código abaixo no editor Python:
    

    """

"""
import os

try:
    os.rmdir('Test Folder')
    print("Pasta removida com sucesso!")
except Exception as e:
    print(f"Ocorreu um erro: {e}")


   
    ⚠️ Lembrete importante:
os.rmdir() só funciona se a pasta estiver vazia.
Se a pasta tiver algum arquivo ou subpasta, ele vai lançar um erro.

Se você quiser apagar a pasta mesmo com conteúdo dentro, use isso:

   


    import shutil

try:
    shutil.rmtree('Test Folder')
    print("Pasta (e seu conteúdo) removida com sucesso!")
except Exception as e:
    print(f"Ocorreu um erro: {e}")


 """