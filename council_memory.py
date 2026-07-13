import ollama
import os

contexto_projeto = """
[CONTEXTO TÉCNICO PERMANENTE]
Projeto: Futsal Tracker (Python, OpenCV, YOLOv8).
Hardware: GTX 1660 Super (6GB VRAM). Prioridade: FPS e otimização.
Estado atual: Câmara móvel (não estática), a extrair ROI pelos pés dos jogadores.
"""

ficheiros_personas = {
    "Arquiteto": "arquiteto.txt",
    "Hardware Checker": "hardware.txt",
    "Visao Computacional": "visao.txt",
    "Product Owner": "po.txt",
    "Cetico": "cetico.txt"
}

historico = {}

for nome, ficheiro in ficheiros_personas.items():
    try:
        with open(ficheiro, 'r', encoding='utf-8') as f:
            prompt = f.read()
        historico[nome] = [{'role': 'system', 'content': prompt}]
    except FileNotFoundError:
        print(f"Erro: O ficheiro '{ficheiro}' não foi encontrado. Verifica se o nome está correto.")
        exit()

print("Conselho de Elite reunido. (Escreve 'sair' para fechar as portas)")

while True:
    pergunta = input("\nQual é a questão para o conselho? ")
    
    if pergunta.lower() == 'sair':
        print("A encerrar a sessão...")
        break

    pergunta_com_contexto = f"{contexto_projeto}\n\nPERGUNTA DO UTILIZADOR:\n{pergunta}"
    print("\n" + "="*60)
    
    for nome in ficheiros_personas.keys():
        historico[nome].append({'role': 'user', 'content': pergunta_com_contexto})
        print(f"A aguardar análise de {nome}...")
        
        resposta = ollama.chat(model='llama3', messages=historico[nome])
        texto_resposta = resposta['message']['content']
        
        historico[nome].append({'role': 'assistant', 'content': texto_resposta})
        
        print(f"\n[{nome.upper()}]:\n{texto_resposta}\n")
        print("-" * 60)