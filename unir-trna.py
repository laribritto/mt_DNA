from Bio import SeqIO
import os

def unir_contigs(arquivo_entrada):
    """
    Une contigs de um arquivo FASTA em um único contig.

    Args:
        arquivo_entrada (str): Caminho para o arquivo FASTA de entrada.

    Returns:
        str: Contig combinado.
    """

    contig_combinado = ""
    for seq_record in SeqIO.parse(arquivo_entrada, "fasta"):
        contig_combinado += str(seq_record.seq)
    return contig_combinado

def unir_contigs_pasta(pasta_entrada, pasta_saida):
    """
    Une contigs de todos os arquivos FASTA em uma pasta em um único contig por arquivo.

    Args:
        pasta_entrada (str): Caminho para a pasta de entrada com arquivos FASTA.
        pasta_saida (str): Caminho para a pasta de saída para arquivos FASTA unidos.
    """

    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    for arquivo_entrada in os.listdir(pasta_entrada):
        if arquivo_entrada.endswith(".fa"):
            caminho_arquivo_entrada = os.path.join(pasta_entrada, arquivo_entrada)
            nome_arquivo, extensao = os.path.splitext(arquivo_entrada)
            arquivo_saida = os.path.join(pasta_saida, nome_arquivo + ".fasta")

            contig_combinado = unir_contigs(caminho_arquivo_entrada)

            with open(arquivo_saida, "w") as f_out:
                f_out.write(">Contig_comprimido\n")
                f_out.write(contig_combinado)

# Exemplo de uso
pasta_entrada = "/home/larissabritobiologia/Desktop/ciclideos-novoplasty-anotados/tRNA"
pasta_saida = "/home/larissabritobiologia/Desktop/ciclideos-novoplasty-anotados/tRNA_unicos"

unir_contigs_pasta(pasta_entrada, pasta_saida)

