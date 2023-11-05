#!/usr/bin/python3
import paramiko
import time

# Definir as variáveis de conexão SSH
host = "Ip do Equipamento"
login = "Login"
password = "Senha"
second_login = "login"
second_password = "senha"

# Iniciar a conexão SSH
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=login, password=password)

# Abrir um canal SSH
channel = client.invoke_shell()

# Aguardar o prompt de comando
time.sleep(1)
output = channel.recv(9999).decode('utf-8')

# Se o equipamento solicitar um segundo login, envie o segundo login e senha
if "Login:" in output:
    channel.send(f"{second_login}\n")
    time.sleep(1)
    channel.send(f"{second_password}\n")
    time.sleep(1)

# Aguardar o prompt de comando novamente
time.sleep(1)
output = channel.recv(9999).decode('utf-8')

# Enviar comandos e esperar pelas respostas
channel.send("enable\n")
time.sleep(1)
channel.send(f"{password}\n")
time.sleep(1)
channel.send("configure terminal\n")
time.sleep(1)
channel.send("show sys cpu-usage\n")
time.sleep(5)  # Aguarde tempo suficiente para receber a saída
output = channel.recv(9999).decode('utf-8')  # Capturar a saída

# Fechar o canal e a conexão
channel.close()
client.close()

# Analisar a saída para encontrar o primeiro valor numérico
import re
match = re.search(r'(\d+\.\d+)', output)

if match:
    # Pegar o valor correspondente
    cpu_value = match.group(1)
    print(cpu_value)
else:
    print("Valor numérico não encontrado na saída.")
