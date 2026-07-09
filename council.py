import ollama
from pathlib import Path

PERSONAS_DIR = Path("personas")
MODEL = "llama3"

def carregar_personas():
    personas = {}
    for ficheiro in PERSONAS_DIR.glob("*.txt"):
        nome = ficheiro.stem
        # Lê os ficheiros txt que criaste
        personas[nome] = ficheiro.read_text(encoding="utf-8").strip()
    return personas

def perguntar_persona(nome, system_prompt, pergunta):
    # O Ollama usa um formato de mensagens parecido com um chat
    response = ollama.chat(model=MODEL, messages=[
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': pergunta}
    ])
    return nome, response['message']['content']

def council(pergunta):
    personas = carregar_personas()
    print(f"\n{'='*70}\nPERGUNTA: {pergunta}\n{'='*70}\n")
    
    for nome, system_prompt in personas.items():
        print(f"\n--- {nome.upper().replace('_', ' ')} ---\n")
        _, resposta = perguntar_persona(nome, system_prompt, pergunta)
        print(resposta)

if __name__ == "__main__":
    pergunta = input("Qual é a decisão que queres discutir com o council?\n> ")
    council(pergunta)