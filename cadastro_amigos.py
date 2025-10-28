import json
import os

ARQUIVO = "amigos.json"

# Carregar lista de amigos do arquivo
def carregar_amigos():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return []

# Salvar lista de amigos no arquivo
def salvar_amigos(amigos):
    with open(ARQUIVO, "w") as f:
        json.dump(amigos, f, indent=4)

# Adicionar novo amigo
def adicionar_amigo(amigos):
    nome = input("Digite o nome do amigo: ").strip()
    telefone = input("Digite o telefone: ").strip()
    cidade = input("Digite a cidade: ").strip()

    amigo = {
        "nome": nome,
        "telefone": telefone,
        "cidade": cidade
    }

    amigos.append(amigo)
    salvar_amigos(amigos)
    print("Amigo cadastrado com sucesso!")

# Listar todos os amigos
def listar_amigos(amigos):
    if not amigos:
        print("Nenhum amigo cadastrado.")
        return

    print("\n--- LISTA DE AMIGOS ---")
    for i, amigo in enumerate(amigos, start=1):
        print(f"{i}. Nome: {amigo['nome']} | Telefone: {amigo['telefone']} | Cidade: {amigo['cidade']}")

# Remover um amigo
def remover_amigo(amigos):
    listar_amigos(amigos)
    nome = input("\nDigite o nome do amigo que deseja remover: ").strip()

    encontrado = False
    for amigo in amigos:
        if amigo["nome"].lower() == nome.lower():
            amigos.remove(amigo)
            salvar_amigos(amigos)
            print("Amigo removido com sucesso!")
            encontrado = True
            break

    if not encontrado:
        print("Amigo não encontrado.")

# ------------------ PROGRAMA PRINCIPAL ------------------
amigos = carregar_amigos()

while True:
    print("\n--- MENU ---")
    print("1. Adicionar amigo")
    print("2. Listar amigos")
    print("3. Remover amigo")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_amigo(amigos)
    elif opcao == "2":
        listar_amigos(amigos)
    elif opcao == "3":
        remover_amigo(amigos)
    elif opcao == "4":
        print("Saindo... até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
