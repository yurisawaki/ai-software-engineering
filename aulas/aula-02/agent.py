from datetime import datetime
from ollama import chat

def consultar_horario():
    """Retorna o horário atual do sistema."""
    return datetime.now().strftime("%H:%M:%S")

def buscar_usuario(nome: str):
    """Busca informações sobre um usuário pelo nome."""
    usuarios = {
        "Breno": "Estudante de Computação",
        "Yuri": "Desenvolvedor de software"
    }
    return usuarios.get(nome, "Usuário não encontrado")

MAX_PASSOS = 10

tools = [
    {
        "type": "function",
        "function": {
            "name": "consultar_horario",
            "description": "Retorna o horário atual do sistema.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "buscar_usuario",
            "description": "Faz uma consulta.",
            "parameters": {
                "type": "object",
                "properties": {
                    "nome": {
                        "type": "string",
                        "description": "Nome do usuário"
                    }
                },
                "required": ["nome"]
            }
        }
    }
]

funcoes = {
    "consultar_horario": consultar_horario,
    "buscar_usuario": buscar_usuario
}

def agente(pergunta):
    mensagens = [
        {
            "role": "user",
            "content": pergunta
        }
    ]

    for passo in range(MAX_PASSOS):
        resposta = chat(
            model="llama3.1",
            messages=mensagens,
            tools=tools
        )

        mensagens.append(resposta.message)

        if not resposta.message.tool_calls:
            print(f"Finalizado em {passo + 1} passos")
            return resposta.message.content

        for chamada in resposta.message.tool_calls:
            nome = chamada.function.name
            argumentos = chamada.function.arguments

            print(f"Passo {passo + 1}: usando {nome}")

            resultado = funcoes[nome](**argumentos)

            mensagens.append({
                "role": "tool",
                "tool_name": nome,
                "content": str(resultado)
            })

    return "Limite de passos atingido."

print(agente("Qual é a profissão do Breno?"))
