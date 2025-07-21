import os

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import mannwhitneyu

FUNCOES = ['ackley', 'rastrigin', 'schwefel', 'rosenbrock']

print("==== Teste de Mann-Whitney U ====\n")

medias_ga = []
medias_es = []
p_values = []

# Garante que a pasta existe antes de salvar gráficos
os.makedirs("resultados", exist_ok=True)

for func in FUNCOES:
    ga_path = f"resultados/ga_{func}_melhores_fitness.txt"
    es_path = f"resultados/es_{func}_melhores_fitness.txt"

    ga_results = np.loadtxt(ga_path)
    es_results = np.loadtxt(es_path)

    stat, p_val = mannwhitneyu(ga_results, es_results, alternative='two-sided')

    media_ga = np.mean(ga_results)
    media_es = np.mean(es_results)

    medias_ga.append(media_ga)
    medias_es.append(media_es)
    p_values.append(p_val)

    print(f"Função: {func.capitalize()}")
    print(f"  Média GA: {media_ga:.4f} | Média ES: {media_es:.4f}")
    print(f"  Valor-p: {p_val:.5f}")
    if p_val < 0.05:
        print("  ✅ Diferença estatisticamente significativa")
    else:
        print("  ❌ Diferença não significativa")
    print()

# Agora plotar médias com barras e p-values

x = np.arange(len(FUNCOES))
width = 0.35
significancia = [p < 0.05 for p in p_values]

fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar(x - width/2, medias_ga, width, label='GA', color='#1f77b4')
bars2 = ax.bar(x + width/2, medias_es, width, label='ES', color='#ff7f0e')

for i in range(len(FUNCOES)):
    y = max(medias_ga[i], medias_es[i])
    cor = 'green' if significancia[i] else 'gray'
    ax.text(x[i], y + y*0.03, f'p={p_values[i]:.3g}', ha='center', color=cor, fontsize=10, fontweight='bold')

ax.set_ylabel('Média do Melhor Fitness')
ax.set_title('Comparação de Desempenho entre GA e ES com Teste de Mann-Whitney U')
ax.set_xticks(x)
ax.set_xticklabels([f.capitalize() for f in FUNCOES])
ax.legend()
ax.grid(axis='y')

plt.tight_layout()
plt.savefig("resultados/teste_estatistico_mannwhitney.png")
plt.close()
