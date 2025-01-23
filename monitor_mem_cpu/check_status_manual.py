import psutil
from datetime import datetime

def main():
    # Obtém uso da CPU
    cpu_usage = psutil.cpu_percent(interval=1)
    # Obtém uso da memória
    memory_usage = psutil.virtual_memory().percent

    # Mensagem com os dados
    log_message = f"[{datetime.now()}] CPU: {cpu_usage}%, Memória: {memory_usage}%"
    
    # Imprime no console
    print(log_message)

if __name__ == "__main__":
    main()
