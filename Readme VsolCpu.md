Programa de Monitoramento de CPU via SSH
Este é um programa Python que permite monitorar o uso da CPU em um equipamento via SSH. Ele se conecta ao equipamento, executa um comando para obter as estatísticas de uso da CPU e extrai o valor numérico correspondente. O programa é configurado para lidar com situações em que o equipamento pode solicitar um segundo login e senha.

Requisitos
Python 3.x
Módulo paramiko (para conexão SSH)

Como usar: 

1.Certifique-se de ter os requisitos instalados.
2.Abra o arquivo monitor_cpu.py em um editor de código ou ambiente de desenvolvimento Python.
3.Edite as variáveis host, login, password, second_login, e second_password com as informações de conexão do seu equipamento.
4.Execute o programa:

python3 VsolCpu.py