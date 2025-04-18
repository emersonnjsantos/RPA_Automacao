import os

# Caminho exato da sua área de trabalho via OneDrive
desktop_path = r"C:\Users\emer7\OneDrive\Área de Trabalho"

# Nome e caminho da pasta
folder_name = "Test Folder"
folder_path = os.path.join(desktop_path, folder_name)

# Criação da pasta
if not os.path.exists(folder_path):
    os.mkdir(folder_path)
    print(f"Pasta '{folder_name}' criada com sucesso na área de trabalho!")
else:
    print(f"A pasta '{folder_name}' já existe na área de trabalho.")
