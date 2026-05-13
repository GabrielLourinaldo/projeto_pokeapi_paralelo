import os
import time
import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
SAVE_DIR = os.path.join("data", "raw")
os.makedirs(SAVE_DIR, exist_ok=True)

def download_pokemon_image(poke_id):
    """Baixa a imagem principal de um Pokémon específico."""
    try:
        response = requests.get(f"{BASE_URL}{poke_id}", timeout=10)
        if response.status_code != 200:
            return False
        
        data = response.json()
        image_url = data.get("sprites", {}).get("front_default")
        
        if image_url:
            img_response = requests.get(image_url, timeout=10)
            if img_response.status_code == 200:
                file_path = os.path.join(SAVE_DIR, f"{poke_id}.png")
                with open(file_path, "wb") as f:
                    f.write(img_response.content)
                return True
    except Exception:
        pass
    return False

def run_sequential(limit):
    """Executa o download sequencial."""
    start_time = time.time()
    for i in range(1, limit + 1):
        download_pokemon_image(i)
    return time.time() - start_time

if __name__ == "__main__":
    print("--- INICIANDO TESTE SEQUENCIAL ---")
    limites = [1000]
    num_execucoes = 5
    
    for limite in limites:
        tempos = []
        print(f"\nBaixando {limite} imagens ({num_execucoes} rodadas)...")
        for execucao in range(1, num_execucoes + 1):
            tempo = run_sequential(limite)
            tempos.append(tempo)
            print(f"  Rodada {execucao}: {tempo:.2f}s")
            
        tempo_medio = sum(tempos) / len(tempos)
        print(f">>> Tempo médio Sequencial para {limite} imagens: {tempo_medio:.2f}s")