from services.banco_conectado import criar_conexao
import os

def listar_ordem_crescente():
    conn = criar_conexao()
   
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM jogos j ORDER BY titulo;"
        cursor.execute(query)
        resultado = cursor.fetchall()
        os.system("cls")
        if resultado:
            for nomes in resultado:
                print(f"{nomes[0]} - {nomes[1]} {nomes[2]}")
        else:
            print("Nenhum resultado!")
        print("\n")
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        cursor.close()
        conn.close()
