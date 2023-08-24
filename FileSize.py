import math


def formata_tamanho(tamanho_em_bytes: int, base: int = 1024) -> str:
    if tamanho_em_bytes <= 0:
        return "0B"

    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"

    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))

    potencia = base ** indice_abreviacao_tamanhos

    tamanho_final = round(tamanho_em_bytes / potencia, 2)

    abreviacao_tamanhos = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final} {abreviacao_tamanhos}'


# B
print(formata_tamanho(1000))
# MB
print(formata_tamanho(1_000_000))
#  GB
print(formata_tamanho(1_000_000_000))
