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
channel.send("show fan\n")
time.sleep(5)  # Aguarde tempo suficiente para receber a saída
output = channel.recv(9999).decode('utf-8')  # Capturar a saída

# Fechar o canal e a conexão
channel.close()
client.close()

# Encontrar o valor da temperatura da ventoinha na saída
fan_temperature = None
for line in output.split('\n'):
    if "current temperature:" in line:
        parts = line.split(":")
        if len(parts) == 2:
            fan_temperature = parts[1].strip()
            break

if fan_temperature is not None:
    print({fan_temperature})
else:
    print("Temperatura da Ventoinha não encontrada na saída.")
