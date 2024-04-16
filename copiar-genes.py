import os
import shutil

diretorio_raiz = "/home/larissabritobiologia/Desktop/ciclideos-novoplasty-anotados"  # Substitua pelo caminho do seu diretório raiz
pasta_destino = "/home/larissabritobiologia/Desktop/ciclideos-novoplasty-anotados/genes"  # Nome da pasta de destino onde os arquivos serão copiados

def copiar_arquivos_genes(diretorio_raiz, pasta_destino):
    # Cria a pasta de destino se não existir
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    # Mantém uma lista das pastas que não contêm arquivos _genes.fa ou _genes.fasta
    pastas_sem_genes = []

    # Percorre todos os arquivos nos diretórios e subdiretórios
    for root, _, files in os.walk(diretorio_raiz):
        if not any(file.endswith("_genes.fa") or file.endswith("_genes.fasta") for file in files):
            pastas_sem_genes.append(root)

        for file in files:
            if file.endswith("_genes.fa") or file.endswith("_genes.fasta"):
                arquivo_origem = os.path.join(root, file)
                arquivo_destino = os.path.join(pasta_destino, file)
                if not os.path.exists(arquivo_destino):  # Verifica se o arquivo de destino já existe
                    shutil.copy(arquivo_origem, arquivo_destino)

    return pastas_sem_genes

if __name__ == "__main__":
    pastas_sem_genes = copiar_arquivos_genes(diretorio_raiz, pasta_destino)
    if pastas_sem_genes:
        print("As seguintes pastas não continham arquivos _genes.fa ou _genes.fasta:")
        for pasta in pastas_sem_genes:
            print(pasta)
    else:
        print("Todos os arquivos _genes.fa ou _genes.fasta foram copiados com sucesso!")
