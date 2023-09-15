import os
from cryptography.fernet import Fernet

# Lista para armazenar os nomes dos arquivos a serem descriptografados
files = []

# Ler a chave de criptografia do arquivo "chave.key" no modo binário
with open("chave.key", "rb") as chave_file:
    secretkey = chave_file.read()

# Iterar pelos arquivos no diretório atual
for file in os.listdir():
    # Ignorar o próprio script, o arquivo de chave e qualquer outro arquivo que não deseja descriptografar
    if file == "dec.py" or file == "chave.key" or file == "enc.py":
        continue
    # Verificar se o item é um arquivo
    if os.path.isfile(file):
        # Adicionar o nome do arquivo à lista
        files.append(file)

# Iterar pelos arquivos a serem descriptografados
for file in files:
    # Abrir o arquivo em modo binário para leitura
    with open(file, "rb") as arquivo:
        # Ler o conteúdo do arquivo
        conteudo = arquivo.read()
        try:
            # Descriptografar o conteúdo usando a chave
            conteudo_decrypt = Fernet(secretkey).decrypt(conteudo)
            # Abrir o arquivo em modo binário para escrita
            with open(file, "wb") as arquivo_saida:
                # Escrever o conteúdo descriptografado de volta no arquivo
                arquivo_saida.write(conteudo_decrypt)
            print(f"Arquivo {file} descriptografado com sucesso.")
        except Exception as e:
            print(f"Erro ao descriptografar {file}: {str(e)}")
