

def registrar_treino(treinos):
    nome = input("Qual treino você fez? ")
    if nome == "":
        print("Digite um nome para registrar o treino.")
        return
    treinos.append(nome)
    print(f"Treino registrado: {nome}")



def listar_treinos(treinos):
    if len(treinos) == 0:
        print("Nenhum treino registrado.")
    else:
        for nome in treinos:
            print("-" , nome)


def calcular_faltantes(meta, realizados):
    if realizados >= meta:
        return 0
    return meta - realizados


def mostrar_progresso(treinos, meta):
    realizados = len(treinos)   
    faltam = calcular_faltantes(meta, realizados) 
    print(f"Treinos realizados: {realizados} | Meta: {meta}")
    if faltam == 0:
        print("Meta atingida!")
    else:
        print("Treinos que faltam:" , faltam)


treinos_da_semana = []
meta_semanal = 5

while True:
    print("\n1 - Registrar treino")
    print("2 - Listar treinos")
    print("3 - Consultar progresso")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        registrar_treino(treinos_da_semana)
    elif opcao == "2":
        listar_treinos(treinos_da_semana)
    elif opcao == "3":
        mostrar_progresso(treinos_da_semana, meta_semanal)
    elif opcao == "0":
        print("Até o próximo treino!")
        break
    else:
        print("Opção inválida.")
