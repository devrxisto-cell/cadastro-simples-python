cadastros = []

def menu():
    print("=" * 40)
    print("   SISTEMA DE CADASTRO SIMPLES")
    print("=" * 40)
    print("[1] Cadastrar pessoa")
    print("[2] Listar cadastros")
    print("[0] Sair")


while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Encerrando o sistema...")
        break

    elif opcao == "1":
        nome = input("Nome: ").strip()
        idade = input("Idade: ").strip()

        if not idade.isdigit():
            print("❌ Idade inválida.")
            continue

        pessoa = {
            "nome": nome,
            "idade": int(idade)
        }

        cadastros.append(pessoa)
        print("✅ Cadastro realizado com sucesso!")

    elif opcao == "2":
        if not cadastros:
            print("📭 Nenhum cadastro encontrado.")
        else:
            print("\n📋 LISTA DE CADASTROS")
            for i, pessoa in enumerate(cadastros, start=1):
                print(f"{i}. Nome: {pessoa['nome']} | Idade: {pessoa['idade']}")

    else:
        print("❌ Opção inválida.")
