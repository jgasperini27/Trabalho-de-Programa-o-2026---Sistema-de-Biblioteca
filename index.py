livros = [
    {
        "nome": "Dom Casmurro",
        "autor": "Machado de Assis",
        "disponivel": True,
        "devolucao": "",
        "favorito": False,
        "usuario": ""
    },
    {
        "nome": "Memórias Póstumas de Brás Cubas",
        "autor": "Machado de Assis",
        "disponivel": True,
        "devolucao": "",
        "favorito": False,
        "usuario": ""
    },
    {
        "nome": "O Cortiço",
        "autor": "Aluísio Azevedo",
        "disponivel": True,
        "devolucao": "",
        "favorito": False,
        "usuario": ""
    },
    {
        "nome": "Vidas Secas",
        "autor": "Graciliano Ramos",
        "disponivel": True,
        "devolucao": "",
        "favorito": False,
        "usuario": ""
    },
    {
        "nome": "Capitães da Areia",
        "autor": "Jorge Amado",
        "disponivel": True,
        "devolucao": "",
        "favorito": False,
        "usuario": ""
    },
    {
        "nome": "A Hora da Estrela",
        "autor": "Clarice Lispector",
        "disponivel": True,
        "devolucao": "",
        "favorito": False,
        "usuario": ""
    },
    {
        "nome": "Iracema",
        "autor": "José de Alencar",
        "disponivel": True,
        "devolucao": "",
        "favorito": False,
        "usuario": ""
    },
    {
        "nome": "O Auto da Compadecida",
        "autor": "Ariano Suassuna",
        "disponivel": True,
        "devolucao": "",
        "favorito": False,
        "usuario": ""
    }
]

usuarios = []
while True:
    print("\n * BIBLIOTECA DIGITAL * ")
    print("1 - Cadastrar Usuário")
    print("2 - Ver Livros")
    print("3 - Pesquisar Livro")
    print("4 - Emprestar Livro")
    print("5 - Devolver Livro")
    print("6 - Adicionar Livro")
    print("7 - Remover Livro")
    print("8 - Ver Usuários (Cadastrados)")
    print("9 - Favoritar Livros")
    print("10 - Mais Informações")
    print("0 - Sair")

    opcao = input("Escolha: ")
    if opcao == "1":
        nome = input("Nome do usuário: ")
        if nome in usuarios:
            print("Este usuário já está cadastrado.")
        else:
            usuarios.append(nome)
            print("Usuário cadastrado")


    elif opcao == "2":
        if len(livros) == 0:
            print("Não existem livros cadastrados.")
        else:
            for livro in livros:
                print("\nLivro:", livro["nome"])
                print("Autor:", livro["autor"])
                if livro["disponivel"]:
                    print("Status: Disponível")
                else:
                    print("Status: Emprestado")
                    print("Usuário:", livro["usuario"])
                    if livro["devolucao"] != "":
                        print("Devolver até:", livro["devolucao"])
                if livro["favorito"]:
                    print("Favorito")



    elif opcao == "3":
        pesquisa = input("Digite o nome ou autor: ")
        encontrou = False
        for livro in livros:
            if pesquisa.lower() in livro["nome"].lower() or pesquisa.lower() in livro["autor"].lower():
                print("\nLivro:", livro["nome"])
                print("Autor:", livro["autor"])
                if livro["disponivel"]:
                    print("Status: Disponível")
                else:
                    print("Status: Emprestado")
                encontrou = True
        if not encontrou:
            print("Nenhum livro foi encontrado.")



    elif opcao == "4":
        nome = input("Nome do livro: ")
        encontrou = False
        for livro in livros:
            if livro["nome"].lower() == nome.lower():
                encontrou = True
                if livro["disponivel"]:
                    usuario = input("Nome do usuário: ")
                    data = input("Data de devolução: ")
                    livro["disponivel"] = False
                    livro["devolucao"] = data
                    livro["usuario"] = usuario
                    print("Livro emprestado para", usuario)
                else:
                    print("Este livro está sendo emprestado.")
                break
        if not encontrou:
            print("Livro não encontrado.")




    elif opcao == "5":
        nome = input("Nome do livro: ")
        encontrou = False
        for livro in livros:
            if livro["nome"].lower() == nome.lower():
                encontrou = True
                if livro["disponivel"]:
                    print("O livro está disponível.")
                else:
                    livro["disponivel"] = True
                    livro["devolucao"] = ""
                    livro["usuario"] = ""
                    print("Livro devolvido com sucesso!")

                break
        if not encontrou:
            print("Livro não encontrado.")




    elif opcao == "6":
        nome = input("Nome do livro: ")
        autor = input("Autor: ")
        livros.append({
            "nome": nome,
            "autor": autor,
            "disponivel": True,
            "devolucao": "",
            "favorito": False,
            "usuario": ""
        })
        print("Livro adicionado com sucesso!")




    elif opcao == "7":
        nome = input("Nome do livro: ")
        encontrou = False
        for livro in livros:
            if livro["nome"].lower() == nome.lower():
                encontrou = True
                if livro["disponivel"]:
                    livros.remove(livro)
                    print("Livro removido!")
                else:
                    print("Não é possível remover um livro emprestado.")
                break
        if not encontrou:
            print("Livro não encontrado.")




    elif opcao == "8":
        print("\n * USUÁRIOS CADASTRADOS * ")
        if len(usuarios) == 0:
            print("Nenhum usuário foi cadastrado.")
        else:
            for usuario in usuarios:
                print("-", usuario)




    elif opcao == "9":
        nome = input("Nome do livro: ")
        encontrou = False
        for livro in livros:
            if livro["nome"].lower() == nome.lower():
                encontrou = True
                if livro["favorito"]:
                    livro["favorito"] = False
                    print("Livro removido dos favoritos.")
                else:
                    livro["favorito"] = True
                    print("Livro favoritado!")

                break
        if not encontrou:
            print("Não encontrado.")




    elif opcao == "10":
        disponiveis = 0
        emprestados = 0
        favoritos = 0
        for livro in livros:
            if livro["disponivel"]:
                disponiveis += 1
            else:
                emprestados += 1
            if livro["favorito"]:
                favoritos += 1
        print("\n * DADOS GERAIS * ")
        print("Total de livros:", len(livros))
        print("Disponíveis:", disponiveis)
        print("Emprestados:", emprestados)
        print("Favoritos:", favoritos)
        print("Usuários:", len(usuarios))




    elif opcao == "0":
        print("Saindo...")

        break
    else:
        print("Opção inválida.")