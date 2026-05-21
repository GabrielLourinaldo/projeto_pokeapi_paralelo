import os
import time
import requests
import concurrent.futures

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

def run_futures(limit, num_workers):
    start_time = time.time()
    
<<<<<<< HEAD
    # Cria um pool de workers e envia as tarefas de ID de 1 até o limite
=======
>>>>>>> c02cab9 (chore: Correções no README e Requirements e adiciona script resultados e suas exportações)
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
        executor.map(download_pokemon_image, range(1, limit + 1))
        
    return time.time() - start_time

if __name__ == "__main__":
    print("--- INICIANDO TESTE CONCURRENT.FUTURES ---")
    limites = [100, 500, 1000]
    config_workers = [2, 4, 8]
    num_execucoes = 5
    
    for limite in limites:
        for num_workers in config_workers:
            tempos = []
            print(f"\nBaixando {limite} imagens com {num_workers} Workers (Futures) ({num_execucoes} rodadas)...")
            for execucao in range(1, num_execucoes + 1):
                tempo = run_futures(limite, num_workers)
                tempos.append(tempo)
                print(f"  Rodada {execucao}: {tempo:.2f}s")
                
            tempo_medio = sum(tempos) / len(tempos)
            print(f">>> Tempo médio Futures ({num_workers} workers) para {limite} imagens: {tempo_medio:.2f}s")