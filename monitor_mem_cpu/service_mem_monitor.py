from rocketry import Rocketry
from rocketry.conds import daily
import psutil
import os
import time
from datetime import datetime

# Configuração do Rocketry
app = Rocketry()

# Diretórios e arquivos de log
LOG_DIR = "/home/ubuntu/logs"
MONITOR_LOG = os.path.join(LOG_DIR, "monitor_memoria.log")
RESTART_LOG = os.path.join(LOG_DIR, "historico_reinicios.txt")

# Limites configuráveis
CPU_MIN_THRESHOLD = 1  # Percentual mínimo de utilização da CPU
MEMORY_MAX_THRESHOLD = 60  # Percentual mínimo de memória para iniciar monitoramento
CPU_CHECK_INTERVAL = 3  # Intervalo de checagem (em segundos) quando memória está alta
LOW_CPU_DURATION = 30  # Tempo acumulado (em segundos) para reiniciar o servidor

# Função para registrar mensagens no log
def write_to_log(file_path, message):
    with open(file_path, "a") as log_file:
        log_file.write(f"{message}\n")

# Função para verificar o uso de memória
def is_memory_high():
    memory_usage = psutil.virtual_memory().percent
    log_message = f"[{datetime.now()}] Utilização de Memória: {memory_usage}%"
    print(log_message)
    write_to_log(MONITOR_LOG, log_message)
    return memory_usage >= MEMORY_MAX_THRESHOLD

# Função para monitorar CPU e memória
def monitor_system():
    low_cpu_time = 0

    while True:
        # Obtém uso da CPU
        cpu_usage = psutil.cpu_percent(interval=1)
        # Obtém uso da memória
        memory_usage = psutil.virtual_memory().percent

        log_message = (
            f"[{datetime.now()}] Utilização da CPU: {cpu_usage}%, "
            f"Utilização de Memória: {memory_usage}%"
        )
        print(log_message)
        write_to_log(MONITOR_LOG, log_message)

        # Verifica se ambas as condições estão atendidas
        if cpu_usage <= CPU_MIN_THRESHOLD and memory_usage >= MEMORY_MAX_THRESHOLD:
            low_cpu_time += CPU_CHECK_INTERVAL
            log_message = (
                f"[{datetime.now()}] CPU abaixo do limite e memória acima do limite "
                f"por {low_cpu_time} segundos."
            )
            print(log_message)
            write_to_log(MONITOR_LOG, log_message)

            # Reinicia o sistema se as condições persistirem
            if low_cpu_time >= LOW_CPU_DURATION:
                log_restart(cpu_usage, memory_usage)
                restart_system()
        else:
            # Reseta o contador caso as condições não sejam atendidas
            low_cpu_time = 0

        # Pausa antes da próxima verificação
        time.sleep(CPU_CHECK_INTERVAL)

# Função para registrar informações de reinício
def log_restart(cpu_usage, memory_usage):
    restart_time = datetime.now()
    log_message = (
        f"[{restart_time}] Reiniciando o sistema.\n"
        f" - CPU: {cpu_usage}%\n"
        f" - Memória: {memory_usage}%\n"
        f" - Data/Hora: {restart_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
    )
    print(log_message)
    write_to_log(RESTART_LOG, log_message)

# Função para reiniciar o sistema
def restart_system():
    os.system('sudo reboot')

# Tarefa principal do Rocketry
@app.task(daily.at("13:00"))  # Executa todos os dias às 13h
def daily_monitor():
    print(f"[{datetime.now()}] Tarefa iniciada: Verificando memória...")
    write_to_log(MONITOR_LOG, f"[{datetime.now()}] Tarefa iniciada: Verificando memória...")
    
    if is_memory_high():
        print(f"[{datetime.now()}] Memória acima do limite. Iniciando monitoramento detalhado.")
        write_to_log(MONITOR_LOG, f"[{datetime.now()}] Memória acima do limite. Iniciando monitoramento detalhado.")
        monitor_system()
    else:
        print(f"[{datetime.now()}] Memória abaixo do limite. Monitoramento encerrado para hoje.")
        write_to_log(MONITOR_LOG, f"[{datetime.now()}] Memória abaixo do limite. Monitoramento encerrado para hoje.")

# Inicia o aplicativo Rocketry
if __name__ == "__main__":
    print("Iniciando aplicação Monitoramento de Memória Rocketry...")
    os.makedirs(LOG_DIR, exist_ok=True)  # Garante que o diretório de logs existe
    write_to_log(MONITOR_LOG, f"[{datetime.now()}] Aplicação Rocketry iniciada.")
    app.run()
