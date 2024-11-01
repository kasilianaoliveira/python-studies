from typing import Dict, List, Union


numbers = []


def adicionar_contato(
    contatos: List[Dict[str, Union[str, bool]]],
    nome: str,
    telefone: int,
    email: str,
    favorito: str,
):
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": True if favorito == "Sim" else False,
    }
    contatos.append(contato)
    print(f"{nome} adicionado com sucesso aos contatos")
    return


def mostrar_contato(contatos: List[Dict[str, Union[str, bool]]]):
    print("\n================================")
    for indice, contato in enumerate(contatos):
        status = "Sim" if contato["favorito"] else "Não"
        name = contato["nome"]
        print(f"{indice + 1}. Nome do contato:{name} \n")
        print(f"Número: {contato["telefone"]} \n")
        print(f"Email: {contato["email"]} \n")
        print(f"Adicionado aos favoritos? {status} \n")

    print("\n================================")


def atualizar_telefone(contatos: List[Dict[str, Union[str, bool]]], telefone: int):
    for contato in contatos:
        if telefone == contato["telefone"]:
            novo_telefone = input("Digite o novo numero para seu contato \n")
            contato["telefone"] = novo_telefone
            print(f"O contato {contato["nome"]} foi atualizado com sucesso!")
            return


def adicionar_favoritos(
    contatos: List[Dict[str, Union[str, bool]]], telefone: int, isFavorite: str
):
    for contato in contatos:
        if telefone == contato["telefone"]:
            if isFavorite == "Adicionar":
                contato["favorito"] = True
                print(numbers)
                print(f"O {telefone} foi adicionado aos favoritos com sucesso!")
            else:
                contato["favorito"] = False
                print(numbers)
                print(f"O {telefone} foi removido dos favoritos com sucesso!")
            return


def mostrar_contato_favoritos(contatos: List[Dict[str, Union[str, bool]]]):
    print("\n================================")
    for indice, contato in enumerate(contatos):
        status = "Sim" if contato["favorito"] else "Não"
        if contato["favorito"]:
            name = contato["nome"]
            print(f"{indice + 1}. Nome do contato:{name} \n")
            print(f"Número: {contato["telefone"]} \n")
            print(f"Email: {contato["email"]} \n")
            print(f"Favorito: {status} \n")

    print("\n================================")


def remover_telefone(contatos: List[Dict[str, bool]], telefone: int, nome: str):
    try:
        for contato in contatos:
            if telefone == contato["telefone"] and nome == contato["nome"]:
                contatos.remove(contato)
                print(f"O número {telefone} foi removido com sucesso")
                return
    except ValueError as e:
        print(f"Nenhum contato encontrado com o telefone {telefone} e nome {nome}.")


print(numbers)

while True:
    print("\n--- Menu ---")
    print("1. Adicionar um contato")
    print("2. Ver lista de contato")
    print("3. Atualizar um contato")
    print("4. Adicionar/Remover dos favoritos")
    print("5. Ver lista de favoritos")
    print("6. Deletar um contato")
    print("7. Sair")

    option = input("Digite a sua escolha \n")
    match option:
        case "1":
            nome = input("Digite o nome do contato \n")
            telefone = int(input("Digite o telefone do contato \n"))
            email = input("Digite o email do contato \n")
            favorito = input("Digite se o contato é favorito (Sim/Não) \n")

            adicionar_contato(
                numbers, nome=nome, telefone=telefone, email=email, favorito=favorito
            )
        case "2":
            mostrar_contato(numbers)
        case "3":
            telefone = int(
                input("Digite o telefone do contato que você quer atualizar \n")
            )
            atualizar_telefone(numbers, telefone)
        case "4":
            telefone = int(
                input(
                    "Digite o telefone do contato que você quer adicionar/remover dos favoritos \n"
                )
            )

            favorito = input(
                "Digite se você quer remover ou adicionar (Adicionar/Remover) \n"
            )

            adicionar_favoritos(numbers, telefone=telefone, isFavorite=favorito)
        case "5":
            mostrar_contato_favoritos(numbers)
        case "6":
            telefone = int(input("Digite o numero que você deseja remover \n"))
            nome = input("Digite o nome do contato \n")
            remover_telefone(numbers, nome=nome, telefone=telefone)
        case "7":
            break
