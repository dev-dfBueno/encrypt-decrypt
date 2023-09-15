```markdown
# Projeto de Criptografia e Descriptografia em Python

Este é um projeto simples de criptografia e descriptografia em Python que utiliza a biblioteca `cryptography.fernet` para proteger arquivos com uma chave secreta. O programa permite encriptar arquivos sensíveis para proteger seu conteúdo e, posteriormente, descriptografá-los quando necessário.

## Funcionalidades

- Gere uma chave secreta para a criptografia.
- Encripte arquivos com a chave secreta gerada.
- Descriptografe arquivos previamente encriptados usando a mesma chave secreta.

## Como Usar

1. Clone este repositório para o seu sistema local.
2. Instale as dependências necessárias executando `pip install cryptography`.
3. Execute o script `encript.py` para encriptar os arquivos desejados.
4. Para descriptografar os arquivos encriptados, execute o script `decript.py`.

**Importante:** Mantenha a chave secreta (`chave.key`) em segurança, pois ela é necessária para a descriptografia dos arquivos.

## Exemplo de Uso

```bash
# Gerar chave secreta
python encript.py

# Encriptar arquivos
python encript.py

# Descriptografar arquivos
python decript.py
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) e enviar pull requests com melhorias.

## Licença

Este projeto é licenciado sob a [Licença MIT](LICENSE).
