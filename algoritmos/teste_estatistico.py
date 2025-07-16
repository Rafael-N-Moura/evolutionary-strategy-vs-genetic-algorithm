import numpy as np
from scipy.stats import mannwhitneyu

FUNCOES = ['ackley', 'rastrigin', 'schwefel', 'rosenbrock']

print("==== Teste de Mann-Whitney U ====\n")

for func in FUNCOES:
    ga_path = f"resultados/ga_{func}_melhores_fitness.txt"
    es_path = f"resultados/es_{func}_melhores_fitness.txt"

    ga_results = np.loadtxt(ga_path)
    es_results = np.loadtxt(es_path)

    stat, p = mannwhitneyu(ga_results, es_results, alternative='two-sided')

    print(f"Função: {func.capitalize()}")
    print(f"  Média GA: {np.mean(ga_results):.4f} | Média ES: {np.mean(es_results):.4f}")
    print(f"  Valor-p: {p:.5f}")
    if p < 0.05:
        print("  ✅ Diferença estatisticamente significativa")
    else:
        print("  ❌ Diferença não significativa")
    print()
