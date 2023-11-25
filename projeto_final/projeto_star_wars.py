
"""
Cadastro sobre filmes de Star Wars com um quiz sobre os filmes I II III IV V VI
"""
# Sistema de Cadastro de Planetas
from galaxia_2d import Galaxia2DApp


# dicionario base
cadastro_planetas = {
    "Tatooine": {
        "personagens": "Anakin Skywalker, Luke Skywalker",
        "eventos": "Pod race, Duelo com Darth Vader",
        "perguntas": [
            {
                "pergunta": "Qual é o planeta natal de Anakin Skywalker?",
                "respostas": ["a) Tatooine", "b) Coruscant", "c) Naboo"],
                "resposta_correta": "a",
                "explicacao": "Anakin Skywalker nasceu em Tatooine."
            }
        ]
    },
    "Endor": {
        "personagens": "Leia Organa",
        "eventos": "Batalha de Endor",
        "perguntas": [
            {
                "pergunta": "Onde os Ewoks vivem?",
                "respostas": ["a) Alderaan", "b) Coruscant", "c) Endor"],
                "resposta_correta": "c",
                "explicacao": "Os Ewoks vivem no planeta Endor."
            }
        ]
    }
}

# dicionário separado para as pontuações
pontuacoes = {}


# tratamento de erro, verifica e entrada nao esta vazia
def entrada_nao_vazia(mensagem):
    while True:
        entrada = input(mensagem).strip()
        if entrada:
            return entrada
        else:
            print("Por favor, insira uma entrada valida")

def cadastrar_planeta():
    nome_planeta = entrada_nao_vazia("Digite o nome do planeta: ")
    personagens = entrada_nao_vazia("Digite os personagens que nasceram neste planeta: ")
    eventos = entrada_nao_vazia("Digite os eventos relacionados a este planeta: ")

    # adiciona no dicionario
    cadastro_planetas[nome_planeta] = {
        "personagens": personagens,
        "eventos": eventos,
        "perguntas": []
    }

def cadastrar_pergunta_planeta():
    nome_planeta = entrada_nao_vazia("Digite o nome do planeta para cadastrar a pergunta: ")

    # verificar se planeta existe no cadastro
    if nome_planeta in cadastro_planetas:
        pergunta = entrada_nao_vazia("Digite a pergunta: ")
        respostas = [input("Digite a alternativa (a): "), input("Digite a alternativa (b): "), input("Digite a alternativa (c): ")]
        resposta_correta = entrada_nao_vazia("Digite a resposta correta (a, b, c): ")
        explicacao = entrada_nao_vazia("Digite uma explicação da resposta: ")

        # adiciona no dicionario
        cadastro_planetas[nome_planeta]["perguntas"].append({
            "pergunta": pergunta,
            "respostas": respostas,
            "resposta_correta": resposta_correta,
            "explicacao": explicacao
        })
    else:
        print(f"O planeta {nome_planeta} não está cadastrado. Cadastre primeiro.")

# Funcao para mostrar lista de planetas que estao no dicionario de cadastro
def lista_planetas():
    print("\nLista de Planetas:")
    for planeta in cadastro_planetas.keys():
        print(f"\n- {planeta}")

# retorna perguntas sobre um planeta especifico
def get_pergunta(nome_planeta):
    return cadastro_planetas.get(nome_planeta, {}).get("perguntas", [])

def executar_quiz():
    nome_planeta = input("Digite o nome do planeta para o quiz: ")

    # verifica se o planeta existe no cadastro
    if nome_planeta in cadastro_planetas:
        jogador = input("Digite o nome do jogador: ")

        # usando as perguntas cadastradas para cada planeta específico
        pontuacao = 0
        perguntas = cadastro_planetas.get(nome_planeta, {}).get("perguntas", [])

        if not perguntas:
            print(f"Não há perguntas cadastradas para o planeta {nome_planeta}.")
            return

        print(f"Quiz sobre o planeta {nome_planeta} para {jogador}:\n")

        # dicinario sobre uma pergunta especifica relacionada a um planeta
        for pergunta_data in perguntas:
            print(pergunta_data["pergunta"])
            for resposta in pergunta_data["respostas"]:
                print(resposta)

            resposta = input("Sua resposta (a, b ou c): ")

            if resposta == pergunta_data["resposta_correta"]:
                print("Correto! Você ganhou um ponto.")
                pontuacao += 1
            else:
                print("Errado. A resposta correta é:", pergunta_data["resposta_correta"])
                print(pergunta_data["explicacao"])

        if jogador not in pontuacoes:
            pontuacoes[jogador] = {}

        pontuacoes[jogador][nome_planeta] = pontuacao
    else:
        print(f"O planeta {nome_planeta} não está cadastrado. Cadastre-o primeiro.")

def executa_estrela_da_morte():
    print("  .          __---__")
    print(".     .   .-'...:...'-.               .          .")
    print("         / .  . : .__ .\                                         .")
    print("  .     /........./  \ .\  .   .                            .")
    print("       / :  :   :| () | :\                  .        .")
    print("      :...........\__/....:         .")
    print("      |___________________|              .                     .")
    print("      |...................|               .")
    print(".     :  :  :   :   :   : :                          .            .")
    print("    .  \................./      .            .")
    print("        \  .  . : .  .  /   .                                .")
    print("     .   \._........._./  .        .                   .")
    print("            -..___..-                .         .")
    print("")

def main():
    while True:
        print("\n")
        print("                    8888888888  888    88888")
        print("                   88     88   88 88   88  88")
        print("                    8888  88  88   88  88888")
        print("                       88 88 888888888 88   88")
        print("                88888888  88 88     88 88    888888")
        print(" ")
        print("                88  88  88   888    88888    888888")
        print("                88  88  88  88 88   88  88  88")
        print("                88 8888 88 88   88  88888    8888")
        print("                 888  888 888888888 88   88     88")
        print("                  88  88  88     88 88    8888888")
        print("\nMenu:")
        print("1. Cadastrar Planeta")
        print("2. Cadastrar Pergunta")
        print("3. Lista de Planetas")
        print("4. Iniciar Quiz")
        print("5. Mostrar Galaxia 2D")
        print("6. Encerrar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_planeta()

        elif opcao == "2":
            cadastrar_pergunta_planeta()
        
        elif opcao == "3":
            lista_planetas()

        elif opcao == "4":
            executar_quiz()
            
        elif opcao == "5":
            galaxia_app = Galaxia2DApp()
            galaxia_app.run()

        elif opcao == "6":
            break
        
        else:
            print("Opção inválida")


    print("Pontuações finais:")
    for jogador, dados in pontuacoes.items():
        for planeta, pontuacao in dados.items():
            print(f"{jogador} - Planeta {planeta}: Pontuação: {pontuacao}")

    
    print(executa_estrela_da_morte())


if __name__ == "__main__":
    main()
