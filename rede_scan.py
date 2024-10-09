import argparse
from netaddr import iter_iprange
import os, platform

argument = argparse.ArgumentParser(prog='rede_scan.py', description='Meu programa pessoal para escanear Redes Pivot lateral.')
argument.add_argument('-p', type=str, metavar='[Ping]', nargs=2, help='Ip de host, digite o endereço IPV4 do Gatway padrão')
argument.add_argument('-m', type=str, metavar='[Mascara Subrede]', nargs=1, help='Digite a mascara de subre rede. Por padrão sera 255.255.255.0')


result = argument.parse_args()
print(result.p)

if result.p == None:
    result.p = ['192.168.0.1', '192.168.0.255']

if result.m == None:
    result.m = '255.255.255.0'
print(result.m)
last = str(result.p)
print(last)

generate = iter_iprange(result.p[0], result.p[1], step=1 )
for i in generate:
    print(i) #result of ping
    
def ping(host):
    if platform.system().lower == "windows":
        ping_str = '-n 1'
    else:
        ping_str = "-c 1"

    resposta = os.system(ping + "ping_str" + generate + "" + host)
    return resposta == 0
