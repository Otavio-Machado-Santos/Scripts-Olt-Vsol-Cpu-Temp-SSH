Programa de Monitoramento de Temperatura da Ventoinha via SSH
Este é um programa Python que permite monitorar a temperatura da ventoinha de um equipamento via SSH. Ele se conecta ao equipamento, executa um comando para obter as informações da temperatura da ventoinha e extrai o valor correspondente. O programa é configurado para lidar com situações em que o equipamento pode solicitar um segundo login e senha.

Requisitos
Python 3.x
Módulo paramiko (para conexão SSH)

Você pode instalar o módulo paramiko com o seguinte comando: pip install paramiko

Como usar:

Certifique-se de ter os requisitos instalados.
Abra o arquivo VsoltempFan.py em um editor de código ou ambiente de desenvolvimento Python.
Edite as variáveis host, login, password, second_login, e second_password com as informações de conexão do seu equipamento.
Execute o programa:

python3 VsoltempFan.py

O programa se conectará ao equipamento, executará o comando show fan e imprimirá o valor da temperatura da ventoinha.