import os
import pyaes

### Arquivo Original
file_original = "arquivo.txt"

### Abrir o arquivo criptografado
file_name = file_original+".ransomwaretroll"
file = open(file_name, "rb")
file_data = file.read()
file.close()

### Chave de criptografia
key = b"arquivransomware"
aes = pyaes.AESModeOfOperationCTR(key)

### Descriptografar o arquivo
decrypto_data = aes.decrypt(file_data)

### Remover o arquivo
os.remove(file_name)

### Criar o arquivo descriptografado
new_file = file_original
new_file = open(f'{new_file}','wb')
new_file.write(decrypto_data)
new_file.close()
