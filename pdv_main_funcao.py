#IMPORTANDO O MODULO PARA LER AS DLL'S
# import windll from ctypes 
#
# IMPLEMENTAÇÃO DA FUNÇÃO DA CHAMADA DE CARTÃO
#def TransacaoCartoa():
#	print("chamada de cartão")
# IMPLEMENTAÇÃO DA FUNÇÃO DA CHAMADA DE CARTÃO
import os

#arq = open('%TEMP%\IntPos.001')
arq = open('C:\IntPos.001','w')
dados = """000-000 = CRT
001-000 = 1111
002-000 = 1111
003-000 = 010
004-000 = 00
999-999 = 00
"""


arq.write(dados)
arq.close()

os.system("move C:\IntPos.001 C:\TEF_DIAL\REQ\ ")
os.system("echo Conculido transferencia de arquivo")
os.system("pause")

