import argparse
from netaddr import iter_iprange
import scan as side

argument = argparse.ArgumentParser(prog='rede_scan.py', description='Meu programa pessoal para escanear Redes Pivot lateral.')
argument.add_argument('-p', type=str, metavar='[Ping]', nargs=2, help='Ip de host, digite o endereço IPV4 do Gatway padrão')
argument.add_argument('-m', type=str, metavar='[Mascara Subrede]', nargs=1, help='Digite a mascara de subre rede. Por padrão sera 255.255.255.0')
argument.add_argument('-o', type=str, metavar='Resultado.txt', nargs=1, help="Digite esta função para output, salvar sua pesquisa em um arquivo externo. \n Caso não escolha o nome do arquivo sera automatizado um nome. \n Somente se for utilizado a opção.")


result = argument.parse_args()
print(result.p)



f1 = side.verifica_sistema()


if result.p == None:
    result.p = ['192.168.0.1', '192.168.0.255']

if result.m == None:
    result.m = '255.255.255.0'
print(result.m)
last = str(result.p)
print(last)

generate = iter_iprange( result.p[0], result.p[1], step=1 )
paraPing =''
for ip in generate:
    if result.o != None:
        side.resultado(str(result.o[0]), side.ping(str(ip), f1) )
    else:
        side.ping(str(ip), f1)
    if result.o == None:
        result.o = 'resultado.txt'
    


        
