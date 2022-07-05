import psutil
import time
import psutil


def MostrarUso(usoCpu,usoMemoria,barras=20):
  porcentagem_cpu = (usoCpu/100.0)
  porcentagem_memoria = (usoMemoria/100.0)
  barraCpu = '█' * int(porcentagem_cpu * barras) + '-' * int(barras - int(porcentagem_cpu * barras))
  barraMemoria = '█' * int(porcentagem_memoria * barras) + '-' * int(barras - int(porcentagem_memoria * barras))

  print(f"\rCPU Uso:|{barraCpu}| {usoCpu:.2f}%  ",end="")
  print(f"MEM Uso:|{barraMemoria}| {usoMemoria:.2f}%  ",end="\r")


if __name__=='__main__':

  while True:
    MostrarUso(psutil.cpu_percent(),psutil.virtual_memory().percent)
    time.sleep(1)