import os
import csv

def calcular_tamanho(sequencia):
    return len(sequencia.replace('\n', ''))

def calcular_porcentagem_AT(sequencia):
    total = len(sequencia.replace('\n', ''))
    count_AT = sequencia.count('A') + sequencia.count('T')
    return (count_AT / total) * 100

def calcular_AT_skew(sequencia):
    total = len(sequencia.replace('\n', ''))
    count_A = sequencia.count('A')
    count_T = sequencia.count('T')
    return (count_A - count_T) / (count_A + count_T)

def ler_arquivo_FASTA(caminho_arquivo):
    nome_especie = os.path.basename(caminho_arquivo).split('.')[0]  # Obtém o nome do arquivo sem a extensão como o nome da espécie
    with open(caminho_arquivo, 'r') as f:
        sequencia = ''.join(line.strip() for line in f)
        tamanho = calcular_tamanho(sequencia)
        percentual_AT = calcular_porcentagem_AT(sequencia)
        AT_skew = calcular_AT_skew(sequencia)
        return nome_especie, tamanho, percentual_AT, AT_skew

def calcular_estatisticas_diretorio(diretorio):
    estatisticas = []
    for arquivo in os.listdir(diretorio):
        if arquivo.endswith('.fasta'):
            caminho_arquivo = os.path.join(diretorio, arquivo)
            nome_especie, tamanho, percentual_AT, AT_skew = ler_arquivo_FASTA(caminho_arquivo)
            estatisticas.append((nome_especie, tamanho, percentual_AT, AT_skew))
    return estatisticas

def salvar_tabela_csv(estatisticas, nome_arquivo):
    with open(nome_arquivo, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Espécie", "Tamanho (pb)", "%AT", "AT-skew"])
        writer.writerows(estatisticas)

if __name__ == "__main__":
    diretorio = '/home/larissabritobiologia/Desktop/ciclideos-novoplasty-anotados/rRNA_unicos'  # Substitua pelo caminho do seu diretório
    nome_arquivo_csv = '/home/larissabritobiologia/Desktop/rRNA.csv'  # Nome do arquivo CSV de saída
    estatisticas = calcular_estatisticas_diretorio(diretorio)
    salvar_tabela_csv(estatisticas, nome_arquivo_csv)
