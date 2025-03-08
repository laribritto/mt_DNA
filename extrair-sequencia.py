from Bio import SeqIO

# Caminho do arquivo de entrada
genome_file = r"C:\Users\Cliente\Documents\area de trabalho\mitogenome\mitofish-novoplasty\ERR10768340_Australoheros_barbosae\ERR10768340_Australoheros_barbosae_Contig1.fa"

# Solicitar o nome do arquivo de saída
output_file = r"C:\Users\Cliente\Documents\area de trabalho\mitogenome\ERR10768340_Australoheros_barbosae-cox.fasta"

# Abrir o arquivo de saída para escrita
with open(output_file, "w") as out_fasta:
    for registro in SeqIO.parse(genome_file, "fasta"):
        # Extrair o intervalo desejado (correção da indexação)
        sequencia_extraida = registro.seq[5474:7037]

        # Criar um novo registro FASTA
        novo_registro = f">{registro.id} intervalo\n{sequencia_extraida}\n"

        # Escrever no arquivo
        out_fasta.write(novo_registro)

print(f"Sequência salva em: {output_file}")
