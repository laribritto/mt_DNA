import os
from Bio import SeqIO

nova_pasta = '/home/larissabritobiologia/Desktop/ciclideos-novoplasty-anotados/genes'
pasta_rRNA = '/home/larissabritobiologia/Desktop/ciclideos-novoplasty-anotados/rRNA'

def extrair_rRNA(input_file, output_file):
    with open(output_file, 'w') as out_file:
        for record in SeqIO.parse(input_file, 'fasta'):
            if 'RNA' in record.description and not record.description.startswith('tRNA'):
                SeqIO.write(record, out_file, 'fasta')

# Cria a pasta de destino se não existir
if not os.path.exists(pasta_rRNA):
    os.makedirs(pasta_rRNA)

# Itera sobre os arquivos "genes.fa" na nova pasta
for arquivo in os.listdir(nova_pasta):
    if arquivo.endswith('genes.fa'):
        caminho_arquivo = os.path.join(nova_pasta, arquivo)

        # Executa a função extrair_rRNA para cada arquivo
        caminho_saida = os.path.join(pasta_rRNA, arquivo)

        extrair_rRNA(caminho_arquivo, caminho_saida)
        print(f"Função extrair_rRNA executada para {caminho_arquivo}. Resultado em {caminho_saida}")
