# AI Council (Sistema Multi-Agente)

Um script em Python que usa o Ollama (Llama 3) para simular um painel de especialistas locais. Criei esta ferramenta para me ajudar a validar as decisões técnicas do meu projeto principal: um sistema de análise e tracking de jogos de futsal.

Como roda 100% localmente na GPU, permite-me testar ideias de arquitetura e código à vontade, sem custos com APIs na cloud.

## O Conselho

O script lê prompts específicos para criar 4 perfis focados em resolver os problemas do sistema de futsal:
* Arquiteto de Software: Avalia a estrutura do código, escalabilidade e se a solução é fácil de manter a longo prazo.
* Especialista em Visão Computacional: Foca-se em FPS, viabilidade do YOLO, OpenCV e otimização do processamento de vídeo.
* Product Owner: Garante que a ferramenta final vai ser realmente útil e simples para um treinador de futsal amador usar.
* Cético: Procura as falhas e as assunções erradas que me possam ter escapado no planeamento.

## Stack
* Python 3
* Ollama (Motor LLM local)
* Llama 3 (Modelo 8B)

## Como executar

1. Garantir que o Ollama está instalado e transferir o modelo:
`ollama pull llama3`

2. Preparar o ambiente local:
`git clone https://github.com/HHH2431/ai-council.git`
`cd ai-council`
`python -m venv venv`
`venv\Scripts\activate`
`pip install ollama`

4. Iniciar o painel:
`python council.py`

## Exemplo Prático
O script serve para debater questões do tipo: "Compensa usar o modelo YOLO pré-treinado a correr no telemóvel do treinador, ou é melhor treinar um modelo custom e processar tudo na cloud para não rebentar com a bateria do utilizador?"
