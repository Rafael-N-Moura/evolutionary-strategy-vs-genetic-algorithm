import numpy as np
import matplotlib.pyplot as plt
from genetic_algorithm import GeneticAlgorithm
from genetic_algorithm_v2 import GeneticAlgorithmV2
from evolution_strategy import EvolutionStrategy
from evolution_strategy_v2 import EvolutionStrategyV2
from benchmarks import ackley, rastrigin, schwefel, rosenbrock
import os

# Parâmetros gerais
FUNCOES = {
    'ackley': ackley,
    'rastrigin': rastrigin,
    'schwefel': schwefel,
    'rosenbrock': rosenbrock
}
D = 30
GENERATIONS = 10000
BOUNDS = {
    'ackley': (-32.768, 32.768),
    'rastrigin': (-5.12, 5.12),
    'schwefel': (-500, 500),
    'rosenbrock': (-5, 10)
}
NUM_EXECUCOES = 30

os.makedirs('resultados', exist_ok=True)

print("=== EXPERIMENTOS DE MELHORIA ===")
print("Testando ES V2 em Rastrigin (melhorar consistência)")
print("Testando GA V2 em Rosenbrock (melhorar robustez)")
print()

# Experimento 1: ES V2 em Rastrigin
print("Executando ES V2 para Rastrigin...")
melhores_fitness_es_v2_rastrigin = []
historicos_es_v2_rastrigin = []

for execucao in range(NUM_EXECUCOES):
    es_v2 = EvolutionStrategyV2(
        func=rastrigin,
        d=D,
        mu=50,  # Aumentado de 30 para 50
        lamb=150,  # Reduzido de 200 para 150
        generations=GENERATIONS,
        bounds=BOUNDS['rastrigin']
    )
    melhor_ind, melhor_fit, hist = es_v2.run()
    melhores_fitness_es_v2_rastrigin.append(melhor_fit)
    historicos_es_v2_rastrigin.append(hist)

melhores_fitness_es_v2_rastrigin = np.array(melhores_fitness_es_v2_rastrigin)
historicos_es_v2_rastrigin = np.array(historicos_es_v2_rastrigin)

# Salvar resultados ES V2 Rastrigin
np.savetxt('resultados/es_v2_rastrigin_melhores_fitness.txt', melhores_fitness_es_v2_rastrigin)
media_hist_es_v2 = np.mean(historicos_es_v2_rastrigin, axis=0)
std_hist_es_v2 = np.std(historicos_es_v2_rastrigin, axis=0)
np.savetxt('resultados/es_v2_rastrigin_convergencia_media.txt', media_hist_es_v2)
np.savetxt('resultados/es_v2_rastrigin_convergencia_std.txt', std_hist_es_v2)

with open('resultados/es_v2_rastrigin_estatisticas.txt', 'w') as f:
    f.write(f'Média do melhor fitness: {np.mean(melhores_fitness_es_v2_rastrigin)}\n')
    f.write(f'Desvio padrão do melhor fitness: {np.std(melhores_fitness_es_v2_rastrigin)}\n')
    f.write(f'Mínimo: {np.min(melhores_fitness_es_v2_rastrigin)}\n')
    f.write(f'Máximo: {np.max(melhores_fitness_es_v2_rastrigin)}\n')

print(f'ES V2 Rastrigin - Média: {np.mean(melhores_fitness_es_v2_rastrigin):.4f} ± {np.std(melhores_fitness_es_v2_rastrigin):.4f}')
print(f'ES Original Rastrigin - Média: 51.79 ± 6.06')
print(f'Melhoria: {((51.79 - np.mean(melhores_fitness_es_v2_rastrigin)) / 51.79 * 100):.1f}%')
print()

# Experimento 2: GA V2 em Rosenbrock
print("Executando GA V2 para Rosenbrock...")
melhores_fitness_ga_v2_rosenbrock = []
historicos_ga_v2_rosenbrock = []

for execucao in range(NUM_EXECUCOES):
    ga_v2 = GeneticAlgorithmV2(
        func=rosenbrock,
        d=D,
        pop_size=200,  # Aumentado de 100 para 200
        generations=GENERATIONS,
        bounds=BOUNDS['rosenbrock']
    )
    melhor_ind, melhor_fit, hist = ga_v2.run()
    melhores_fitness_ga_v2_rosenbrock.append(melhor_fit)
    historicos_ga_v2_rosenbrock.append(hist)

melhores_fitness_ga_v2_rosenbrock = np.array(melhores_fitness_ga_v2_rosenbrock)
historicos_ga_v2_rosenbrock = np.array(historicos_ga_v2_rosenbrock)

# Salvar resultados GA V2 Rosenbrock
np.savetxt('resultados/ga_v2_rosenbrock_melhores_fitness.txt', melhores_fitness_ga_v2_rosenbrock)
media_hist_ga_v2 = np.mean(historicos_ga_v2_rosenbrock, axis=0)
std_hist_ga_v2 = np.std(historicos_ga_v2_rosenbrock, axis=0)
np.savetxt('resultados/ga_v2_rosenbrock_convergencia_media.txt', media_hist_ga_v2)
np.savetxt('resultados/ga_v2_rosenbrock_convergencia_std.txt', std_hist_ga_v2)

with open('resultados/ga_v2_rosenbrock_estatisticas.txt', 'w') as f:
    f.write(f'Média do melhor fitness: {np.mean(melhores_fitness_ga_v2_rosenbrock)}\n')
    f.write(f'Desvio padrão do melhor fitness: {np.std(melhores_fitness_ga_v2_rosenbrock)}\n')
    f.write(f'Mínimo: {np.min(melhores_fitness_ga_v2_rosenbrock)}\n')
    f.write(f'Máximo: {np.max(melhores_fitness_ga_v2_rosenbrock)}\n')

print(f'GA V2 Rosenbrock - Média: {np.mean(melhores_fitness_ga_v2_rosenbrock):.4f} ± {np.std(melhores_fitness_ga_v2_rosenbrock):.4f}')
print(f'GA Original Rosenbrock - Média: 5.90 ± 17.42')
print(f'Melhoria na média: {((5.90 - np.mean(melhores_fitness_ga_v2_rosenbrock)) / 5.90 * 100):.1f}%')
print(f'Melhoria na consistência: {((17.42 - np.std(melhores_fitness_ga_v2_rosenbrock)) / 17.42 * 100):.1f}%')
print()

# Gerar gráficos comparativos
plt.figure(figsize=(12, 5))

# Gráfico ES V2 vs Original em Rastrigin
plt.subplot(1, 2, 1)
plt.plot(media_hist_es_v2, label='ES V2 (Melhorada)', color='red')
plt.fill_between(range(GENERATIONS), media_hist_es_v2-std_hist_es_v2, media_hist_es_v2+std_hist_es_v2, alpha=0.3, color='red')
plt.xlabel('Geração')
plt.ylabel('Melhor Fitness')
plt.title('ES V2 vs Original - Rastrigin')
plt.legend()
plt.grid()

# Gráfico GA V2 vs Original em Rosenbrock
plt.subplot(1, 2, 2)
plt.plot(media_hist_ga_v2, label='GA V2 (Melhorado)', color='blue')
plt.fill_between(range(GENERATIONS), media_hist_ga_v2-std_hist_ga_v2, media_hist_ga_v2+std_hist_ga_v2, alpha=0.3, color='blue')
plt.xlabel('Geração')
plt.ylabel('Melhor Fitness')
plt.title('GA V2 vs Original - Rosenbrock')
plt.legend()
plt.grid()

plt.tight_layout()
plt.savefig('resultados/comparacao_melhorias.png', dpi=300, bbox_inches='tight')
plt.close()

print("=== RESUMO DOS RESULTADOS ===")
print("ES V2 em Rastrigin:")
print(f"  - Média: {np.mean(melhores_fitness_es_v2_rastrigin):.4f} ± {np.std(melhores_fitness_es_v2_rastrigin):.4f}")
print(f"  - Melhoria: {((51.79 - np.mean(melhores_fitness_es_v2_rastrigin)) / 51.79 * 100):.1f}%")
print()
print("GA V2 em Rosenbrock:")
print(f"  - Média: {np.mean(melhores_fitness_ga_v2_rosenbrock):.4f} ± {np.std(melhores_fitness_ga_v2_rosenbrock):.4f}")
print(f"  - Melhoria na média: {((5.90 - np.mean(melhores_fitness_ga_v2_rosenbrock)) / 5.90 * 100):.1f}%")
print(f"  - Melhoria na consistência: {((17.42 - np.std(melhores_fitness_ga_v2_rosenbrock)) / 17.42 * 100):.1f}%") 