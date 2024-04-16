from Bio import SeqIO
import os

def extrair_dloop(registro_genoma):
    """Função para extrair a região D-loop de um registro de genoma."""
    for feature in registro_genoma.features:
        if feature.type == "D_loop":
            return feature.extract(registro_genoma.seq)
    return None

def principal(caminho_pasta):
    # Lista todos os arquivos na pasta especificada
    for nome_arquivo in os.listdir(caminho_pasta):
        # Verifica se é um arquivo GenBank
        if nome_arquivo.endswith(".gbk"):
            print("Processando", nome_arquivo)
            try:
                # Lê o arquivo GenBank
                registro_genoma = SeqIO.read(os.path.join(caminho_pasta, nome_arquivo), "genbank")
                # Extrai o D-loop
                sequencia_dloop = extrair_dloop(registro_genoma)
                if sequencia_dloop:
                    # Salva o D-loop em um arquivo FASTA
                    nome_saida = os.path.splitext(nome_arquivo)[0] + "_dloop.fasta"
                    with open(os.path.join(caminho_pasta, nome_saida), "w") as saida_dloop:
                        saida_dloop.write(">{}_D-loop\n{}\n".format(registro_genoma.id, sequencia_dloop))
                    print("D-loop extraído e salvo para", nome_arquivo)
                else:
                    print("Característica D-loop não encontrada em", nome_arquivo)
            except Exception as e:
                print("Erro ao processar", nome_arquivo, ":", str(e))
    print("Concluído")

if __name__ == "__main__":
    caminho_pasta = "/home/larissabritobiologia/Desktop/gbk"
    principal(caminho_pasta)
