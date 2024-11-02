from services.banco_conectado import criar_conexao
import os

def pesquisa_com_k():
    conn = criar_conexao()
   
    try:
        cursor = conn.cursor()
        query ="select * from jogos j where j.titulo ilike '%k%' or j.subtitulo ilike '%k%';"
        cursor.execute(query)
        resultado = cursor.fetchall()
        os.system("cls")
        for nomes in resultado:
            print(f"{nomes[0]} - {nomes[1]} {nomes[2]}")
        print("\n")

    except Exception as e:
        print(f"Erro: {e}")
    finally:
        cursor.close()
        conn.close()
