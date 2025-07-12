import numpy as np
import matplotlib.pyplot as plt
from genetic_algorithm import GeneticAlgorithm
from genetic_algorithm_v2 import GeneticAlgorithmV2
from evolution_strategy import EvolutionStrategy
from evolution_strategy_v2 import EvolutionStrategyV2
from evolution_strategy_v3 import EvolutionStrategyV3
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
GENERATIONS = 1000
BOUNDS = {
    'ackley': (-32.768, 32.768),
    'rastrigin': (-5.12, 5.12),
    'schwefel': (-500, 500),
    'rosenbrock': (-5, 10)
}
NUM_EXECUCOES = 30

os.makedirs('resultados', exist_ok=True)

print("=== EXPERIMENTOS DE MELHORIA EXTENDIDOS ===")
print("1. Testando GA V2 em todas as funções")
print("2. Testando ES V3 em Rastrigin (ajuste conservador)")
print("3. Comparando todas as versões")
print()

# Resultados originais (para comparação)
RESULTADOS_ORIGINAIS = {
    'ga': {
        'ackley': (8.69, 0.97),
        'rastrigin': (13.37, 4.02),
        'schwefel': (9580.41, 379.71),
        'rosenbrock': (5.90, 17.42)
    },
    'es': {
        'ackley': (8.24, 1.03),
        'rastrigin': (51.79, 6.06),
        'schwefel': (9098.40, 657.43),
        'rosenbrock': (64.90, 18.25)
    }
}

# Experimento 1: GA V2 em todas as funções
print("=== TESTANDO GA V2 EM TODAS AS FUNÇÕES ===")
resultados_ga_v2 = {}

for nome, func in FUNCOES.items():
    print(f"Executando GA V2 para {nome}...")
    melhores_fitness = []
    historicos = []
    
    for execucao in range(NUM_EXECUCOES):
        ga_v2 = GeneticAlgorithmV2(
            func=func,
            d=D,
            pop_size=200,
            generations=GENERATIONS,
            bounds=BOUNDS[nome]
        )
        melhor_ind, melhor_fit, hist = ga_v2.run()
        melhores_fitness.append(melhor_fit)
        historicos.append(hist)
    
    melhores_fitness = np.array(melhores_fitness)
    historicos = np.array(historicos)
    
    # Salvar resultados
    np.savetxt(f'resultados/ga_v2_{nome}_melhores_fitness.txt', melhores_fitness)
    media_hist = np.mean(historicos, axis=0)
    std_hist = np.std(historicos, axis=0)
    np.savetxt(f'resultados/ga_v2_{nome}_convergencia_media.txt', media_hist)
    np.savetxt(f'resultados/ga_v2_{nome}_convergencia_std.txt', std_hist)
    
    with open(f'resultados/ga_v2_{nome}_estatisticas.txt', 'w') as f:
        f.write(f'Média do melhor fitness: {np.mean(melhores_fitness)}\n')
        f.write(f'Desvio padrão do melhor fitness: {np.std(melhores_fitness)}\n')
        f.write(f'Mínimo: {np.min(melhores_fitness)}\n')
        f.write(f'Máximo: {np.max(melhores_fitness)}\n')
    
    resultados_ga_v2[nome] = (np.mean(melhores_fitness), np.std(melhores_fitness))
    
    # Comparar com original
    media_orig, std_orig = RESULTADOS_ORIGINAIS['ga'][nome]
    melhoria_media = ((media_orig - np.mean(melhores_fitness)) / media_orig * 100)
    melhoria_std = ((std_orig - np.std(melhores_fitness)) / std_orig * 100)
    
    print(f'  GA V2 {nome}: {np.mean(melhores_fitness):.4f} ± {np.std(melhores_fitness):.4f}')
    print(f'  GA Original {nome}: {media_orig:.4f} ± {std_orig:.4f}')
    print(f'  Melhoria média: {melhoria_media:.1f}%')
    print(f'  Melhoria consistência: {melhoria_std:.1f}%')
    print()

# Experimento 2: ES V3 em Rastrigin
print("=== TESTANDO ES V3 EM RASTRIGIN ===")
print("Executando ES V3 para Rastrigin...")
melhores_fitness_es_v3_rastrigin = []
historicos_es_v3_rastrigin = []

for execucao in range(NUM_EXECUCOES):
    es_v3 = EvolutionStrategyV3(
        func=rastrigin,
        d=D,
        mu=40,  # Reduzido de 50 para 40
        lamb=180,  # Aumentado de 150 para 180
        generations=GENERATIONS,
        bounds=BOUNDS['rastrigin']
    )
    melhor_ind, melhor_fit, hist = es_v3.run()
    melhores_fitness_es_v3_rastrigin.append(melhor_fit)
    historicos_es_v3_rastrigin.append(hist)

melhores_fitness_es_v3_rastrigin = np.array(melhores_fitness_es_v3_rastrigin)
historicos_es_v3_rastrigin = np.array(historicos_es_v3_rastrigin)

# Salvar resultados ES V3 Rastrigin
np.savetxt('resultados/es_v3_rastrigin_melhores_fitness.txt', melhores_fitness_es_v3_rastrigin)
media_hist_es_v3 = np.mean(historicos_es_v3_rastrigin, axis=0)
std_hist_es_v3 = np.std(historicos_es_v3_rastrigin, axis=0)
np.savetxt('resultados/es_v3_rastrigin_convergencia_media.txt', media_hist_es_v3)
np.savetxt('resultados/es_v3_rastrigin_convergencia_std.txt', std_hist_es_v3)

with open('resultados/es_v3_rastrigin_estatisticas.txt', 'w') as f:
    f.write(f'Média do melhor fitness: {np.mean(melhores_fitness_es_v3_rastrigin)}\n')
    f.write(f'Desvio padrão do melhor fitness: {np.std(melhores_fitness_es_v3_rastrigin)}\n')
    f.write(f'Mínimo: {np.min(melhores_fitness_es_v3_rastrigin)}\n')
    f.write(f'Máximo: {np.max(melhores_fitness_es_v3_rastrigin)}\n')

# Comparar todas as versões ES em Rastrigin
media_orig_es, std_orig_es = RESULTADOS_ORIGINAIS['es']['rastrigin']
print(f'ES V3 Rastrigin: {np.mean(melhores_fitness_es_v3_rastrigin):.4f} ± {np.std(melhores_fitness_es_v3_rastrigin):.4f}')
print(f'ES V2 Rastrigin: 72.5365 ± 6.8815')
print(f'ES Original Rastrigin: {media_orig_es:.4f} ± {std_orig_es:.4f}')
print(f'Melhoria V3 vs Original: {((media_orig_es - np.mean(melhores_fitness_es_v3_rastrigin)) / media_orig_es * 100):.1f}%')
print()

# Gerar gráfico comparativo das versões ES em Rastrigin
plt.figure(figsize=(10, 6))
plt.plot(media_hist_es_v3, label='ES V3 (Conservadora)', color='green', linewidth=2)
plt.fill_between(range(GENERATIONS), media_hist_es_v3-std_hist_es_v3, media_hist_es_v3+std_hist_es_v3, alpha=0.3, color='green')

# Carregar dados ES V2 para comparação
if os.path.exists('resultados/es_v2_rastrigin_convergencia_media.txt'):
    media_hist_es_v2 = np.loadtxt('resultados/es_v2_rastrigin_convergencia_media.txt')
    std_hist_es_v2 = np.loadtxt('resultados/es_v2_rastrigin_convergencia_std.txt')
    plt.plot(media_hist_es_v2, label='ES V2 (Agressiva)', color='red', linewidth=2)
    plt.fill_between(range(GENERATIONS), media_hist_es_v2-std_hist_es_v2, media_hist_es_v2+std_hist_es_v2, alpha=0.3, color='red')

plt.xlabel('Geração')
plt.ylabel('Melhor Fitness')
plt.title('Comparação das Versões ES - Rastrigin')
plt.legend()
plt.grid()
plt.savefig('resultados/comparacao_es_rastrigin.png', dpi=300, bbox_inches='tight')
plt.close()

print("=== RESUMO FINAL DOS EXPERIMENTOS ===")
print("GA V2 em todas as funções:")
for nome in FUNCOES.keys():
    media_v2, std_v2 = resultados_ga_v2[nome]
    media_orig, std_orig = RESULTADOS_ORIGINAIS['ga'][nome]
    melhoria_media = ((media_orig - media_v2) / media_orig * 100)
    melhoria_std = ((std_orig - std_v2) / std_orig * 100)
    print(f"  {nome}: {media_v2:.4f} ± {std_v2:.4f} (melhoria: {melhoria_media:.1f}% média, {melhoria_std:.1f}% consistência)")

print()
print("ES V3 em Rastrigin:")
print(f"  Rastrigin: {np.mean(melhores_fitness_es_v3_rastrigin):.4f} ± {np.std(melhores_fitness_es_v3_rastrigin):.4f}")
print(f"  Melhoria vs Original: {((media_orig_es - np.mean(melhores_fitness_es_v3_rastrigin)) / media_orig_es * 100):.1f}%")
print(f"  Melhoria vs V2: {((72.5365 - np.mean(melhores_fitness_es_v3_rastrigin)) / 72.5365 * 100):.1f}%") 