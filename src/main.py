from services.pesquisa_por_nome import pesquisa_nome
from services.listar_ordem_crescente import listar_ordem_crescente
from services.listar_com_K import pesquisa_com_k

while(True):
    print("1 - Pesquisa por Nome")
    print("2 - Lista em Ordem Crescente")
    print("3 - Listar os que contenham K")
    print("0 - Fechar")
    opc = int(input("Digite sua escolha: "))

    if opc >= 0 and opc <= 3:
        if opc == 0:
            break
        elif opc == 1:
            pesquisa = input("Digite o nome do jogo: ")
            pesquisa_nome(pesquisa)
        elif opc == 2:
            listar_ordem_crescente()
        elif opc == 3:
            pesquisa_com_k()
