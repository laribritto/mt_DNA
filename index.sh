#!/usr/bin/env bash
# Este script é um script em Bash projetado para indexar arquivos usando a ferramenta BWA.
# Ele itera sobre uma lista de arquivos contida no arquivo list.txt e indexa cada um desses arquivos usando o BWA.

for i in $(cat /data/list.txt)
do
    bwa index /data/${i}
done
