# Analisador de sequências de DNA

import matplotlib.pyplot as plt

def contar_nucleotidos(sequencia):
    nucleotideos = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for nuc in sequencia:
        if nuc in nucleotideos:
            nucleotideos[nuc] += 1  # Corrigido para usar 'nucleotideos'
    return nucleotideos

def calcular_gc_content(sequencia):
    g_count = sequencia.count('G')
    c_count = sequencia.count('C')
    gc_content = (g_count + c_count) / len(sequencia) * 100
    return gc_content

def buscar_padrao(sequencia, padrao):
    return sequencia.count(padrao)

def visualizar_frequencia(nucleotideos):
    cores = {'A': 'blue', 'T': 'orange', 'C': 'green', 'G': 'red'}
    plt.figure(figsize=(8, 5))
    bars = plt.bar(nucleotideos.keys(), nucleotideos.values(), 
                  color=[cores[nuc] for nuc in nucleotideos.keys()])
    
    # Adiciona os valores nas barras
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{height}',
                ha='center', va='bottom')
    
    plt.xlabel('Nucleotídeos')
    plt.ylabel('Quantidade')
    plt.title('Frequência de Nucleotídeos na Sequência de DNA')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def analisar_dna():
    # Entrada da sequência
    while True:
        sequencia = input("Digite a sequência de DNA (somente A, T, C, G): ").upper()
        if all(nuc in 'ATCG' for nuc in sequencia):
            break
        print("Sequência inválida! Use apenas A, T, C ou G.")
    
    # Entrada do padrão
    while True:
        padrao = input("Digite o padrão a ser buscado: ").upper()
        if all(nuc in 'ATCG' for nuc in padrao):
            break
        print("Padrão inválido! Use apenas A, T, C ou G.")
    
    # Realiza as análises
    nucleotideos = contar_nucleotidos(sequencia)
    gc_content = calcular_gc_content(sequencia)
    padrao_count = buscar_padrao(sequencia, padrao)
    
    # Exibe os resultados
    print("\nResultados da Análise:")
    print(f"Tamanho da sequência: {len(sequencia)} nucleotídeos")
    print(f"A: {nucleotideos['A']} | T: {nucleotideos['T']} | C: {nucleotideos['C']} | G: {nucleotideos['G']}")
    print(f"GC Content: {gc_content:.2f}%")
    print(f"O padrão '{padrao}' aparece {padrao_count} vezes")
    
    # Visualização gráfica
    visualizar_frequencia(nucleotideos)

# Executa a função principal
if __name__ == "__main__":
    analisar_dna()
