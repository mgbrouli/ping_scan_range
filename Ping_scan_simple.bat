REM (script criado para .bat simples range scan)


@echo off
@echo ========================================================
@echo Criado por MGBrouli
@echo ========================================================

for /l %%i (0,1,254) do (
  ping 192.168.0.%%i -n 1 -w 100 | find "TTL"

REM Para ter uma saida em um documento diferente use >> após o final do comando. "To output in external file use >> in the final line"
REM EX: ping 192.168.0.%%i -n 1 | find "TTL" >> resultado.txt 
REM Quando feito desta maneira não é mostrado no CMD, precisa copiar a linha de comando para funcionar "When done this way does not appear on the CMD screen, you need to copy the comand line"
  ping 192.168.0.%%i -n 1 -w 100 | find "TTL" >> result.txt
  

)

