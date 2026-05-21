import os
import time
import requests
import threading

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

def worker(start_id, end_id):
    """Função alvo da thread para baixar um lote de imagens."""
    for poke_id in range(start_id, end_id + 1):
        download_pokemon_image(poke_id)

def run_threading(limit, num_threads):
    start_time = time.time()
    threads = []
    
    chunk_size = limit // num_threads
    remainder = limit % num_threads
    
    current_start = 1
    for i in range(num_threads):
        current_end = current_start + chunk_size - 1
        if i < remainder:
            current_end += 1
            
        t = threading.Thread(target=worker, args=(current_start, current_end))
        threads.append(t)
        t.start()
        
        current_start = current_end + 1
        
    for t in threads:
        t.join()
        
    return time.time() - start_time

if __name__ == "__main__":
    print("--- INICIANDO TESTE THREADING ---")
<<<<<<< HEAD
    limites = [1000]
    config_threads = [4]
=======
    limites = [100, 500, 1000]
    config_threads = [2, 4, 8]
>>>>>>> c02cab9 (chore: Correções no README e Requirements e adiciona script resultados e suas exportações)
    num_execucoes = 5
    
    for limite in limites:
        for num_threads in config_threads:
            tempos = []
            print(f"\nBaixando {limite} imagens com {num_threads} Threads ({num_execucoes} rodadas)...")
            for execucao in range(1, num_execucoes + 1):
                tempo = run_threading(limite, num_threads)
                tempos.append(tempo)
                print(f"  Rodada {execucao}: {tempo:.2f}s")
                
            tempo_medio = sum(tempos) / len(tempos)
            print(f">>> Tempo médio Threading ({num_threads} threads) para {limite} imagens: {tempo_medio:.2f}s")