import os, platform, subprocess

def resultado(arquivo = "resultado.txt", escrever = ''):
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as res:
            res.write('Resultado de ping scan. \n Criado por: Welligton \n')
            print(f"Arquivo '{res}' criado com sucesso.")
    else:
        with open(arquivo, 'a') as add:
            add.write(str(f"\n {escrever}"))

def verifica_sistema():
    sistema = platform.system()
    if sistema == "Windows":
        flag = '-n'
    else:
        flag = '-c'
    return flag


def ping(host, f1):
    try:
        output = subprocess.run(['ping', f1 ,'1', host ], capture_output=True, text=True)

        if output.returncode == 0:
            print(f"Ping bem-sucedido em {host}")
            print(output.stderr)
            resultado = f"Ping bem-sucedido em {host}"

        
        else:
            print(f"Falha ao pingar {host}")
            return resultado
    except Exception as e:
        print(f"Erro ao tentar pingar {host}:{e}")

    
    
