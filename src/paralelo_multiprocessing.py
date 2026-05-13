import os
import time
import requests
import multiprocessing

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
SAVE_DIR = os.path.join("data", "raw")
os.makedirs(SAVE_DIR, exist_ok=True)

def download_pokemon_image(poke_id):
    try:
        response = requests.get(f"{BASE_URL}{poke_id}", timeout=10)
        if response.status_code == 200:
            data = response.json()
            image_url = data.get("sprites", {}).get("front_default")
            if image_url:
                img_response = requests.get(image_url, timeout=10)
                if img_response.status_code == 200:
                    file_path = os.path.join(SAVE_DIR, f"{poke_id}.png")
                    with open(file_path, "wb") as f:
                        f.write(img_response.content)
    except Exception:
        pass

def worker_process(start_id, end_id):
    """Função alvo do processo para baixar um lote de imagens."""
    for poke_id in range(start_id, end_id + 1):
        download_pokemon_image(poke_id)

def run_multiprocessing(limit, num_processes):
    start_time = time.time()
    processes = []
    
    chunk_size = limit // num_processes
    remainder = limit % num_processes
    
    current_start = 1
    for i in range(num_processes):
        current_end = current_start + chunk_size - 1
        if i < remainder:
            current_end += 1
            
        p = multiprocessing.Process(target=worker_process, args=(current_start, current_end))
        processes.append(p)
        p.start()
        
        current_start = current_end + 1
        
    for p in processes:
        p.join()
        
    return time.time() - start_time

if __name__ == "__main__":
    # Importante no Windows para o multiprocessing funcionar corretamente
    multiprocessing.freeze_support() 
    
    print("--- INICIANDO TESTE MULTIPROCESSING ---")
    limites = [100, 500, 1000]
    config_processos = [2, 4, 8]
    num_execucoes = 5
    
    for limite in limites:
        for num_processes in config_processos:
            tempos = []
            print(f"\nBaixando {limite} imagens com {num_processes} Processos ({num_execucoes} rodadas)...")
            for execucao in range(1, num_execucoes + 1):
                tempo = run_multiprocessing(limite, num_processes)
                tempos.append(tempo)
                print(f"  Rodada {execucao}: {tempo:.2f}s")
                
            tempo_medio = sum(tempos) / len(tempos)
            print(f">>> Tempo médio Multiprocessing ({num_processes} processos) para {limite} imagens: {tempo_medio:.2f}s")