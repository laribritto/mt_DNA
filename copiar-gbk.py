# Script com o objetivo de realizar uma cópia de todos os arquivos que terminam com .gbk para uma pasta chamda gbk
# bibliotecas necessárias
import os
import shutil

# diretórios

pasta_raiz = "/home/larissabritobiologia/Desktop/ciclideos-novoplasty-anotados"
pasta_destino = "/home/larissabritobiologia/Desktop/gbk"

# função para copiar os arquivos .gbk
def copiar_arquivos_gbk(pasta_raiz, pasta_destino):
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    for pasta_atual, subpastas, arquivos in os.walk(pasta_raiz):
        arquivos_gbk_presentes = [arquivo for arquivo in arquivos if arquivo.endswith(".gbk")]
        if not arquivos_gbk_presentes:
            print(f"Não há arquivos .gbk em: {pasta_atual}")
        else:
            for arquivo in arquivos_gbk_presentes:
                caminho_completo_raiz = os.path.join(pasta_atual, arquivo)
                shutil.copy(caminho_completo_raiz, pasta_destino)



# chamando a função 
copiar_arquivos_gbk(pasta_raiz, pasta_destino)













