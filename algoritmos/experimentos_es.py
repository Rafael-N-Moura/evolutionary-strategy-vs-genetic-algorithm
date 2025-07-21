import numpy as np
import matplotlib.pyplot as plt
from evolution_strategy import EvolutionStrategy
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
MU = 30
LAMB = 200
GENERATIONS = 10000
BOUNDS = {
    'ackley': (-32.768, 32.768),
    'rastrigin': (-5.12, 5.12),
    'schwefel': (-500, 500),
    'rosenbrock': (-5, 10)
}
NUM_EXECUCOES = 30

os.makedirs('resultados', exist_ok=True)

for nome, func in FUNCOES.items():
    print(f'Executando ES para {nome}...')
    melhores_fitness = []
    historicos = []
    for execucao in range(NUM_EXECUCOES):
        es = EvolutionStrategy(
            func=func,
            d=D,
            mu=MU,
            lamb=LAMB,
            generations=GENERATIONS,
            bounds=BOUNDS[nome]
        )
        melhor_ind, melhor_fit, hist = es.run()
        melhores_fitness.append(melhor_fit)
        historicos.append(hist)
    melhores_fitness = np.array(melhores_fitness)
    historicos = np.array(historicos)
    # Salvar melhores fitness de cada execução
    np.savetxt(f'resultados/es_{nome}_melhores_fitness.txt', melhores_fitness)
    # Salvar histórico médio e desvio padrão
    media_hist = np.mean(historicos, axis=0)
    std_hist = np.std(historicos, axis=0)
    np.savetxt(f'resultados/es_{nome}_convergencia_media.txt', media_hist)
    np.savetxt(f'resultados/es_{nome}_convergencia_std.txt', std_hist)
    # Salvar estatísticas
    with open(f'resultados/es_{nome}_estatisticas.txt', 'w') as f:
        f.write(f'Média do melhor fitness: {np.mean(melhores_fitness)}\n')
        f.write(f'Desvio padrão do melhor fitness: {np.std(melhores_fitness)}\n')
        f.write(f'Mínimo: {np.min(melhores_fitness)}\n')
        f.write(f'Máximo: {np.max(melhores_fitness)}\n')
    # Gerar gráfico de convergência médio
    plt.figure()
    plt.plot(media_hist, label='Média')
    plt.fill_between(range(GENERATIONS), media_hist-std_hist, media_hist+std_hist, alpha=0.3, label='±1 DP')
    plt.xlabel('Geração')
    plt.ylabel('Melhor Fitness')
    plt.title(f'Convergência Média ES - {nome.capitalize()}')
    plt.legend()
    plt.grid()
    plt.savefig(f'resultados/es_{nome}_convergencia_media.png')
    plt.close()
    # Gerar boxplot dos melhores fitness
    plt.figure()
    plt.boxplot(melhores_fitness)
    plt.ylabel('Melhor Fitness')
    plt.title(f'Boxplot dos Melhores Fitness - ES - {nome.capitalize()}')
    plt.grid()
    plt.savefig(f'resultados/es_{nome}_boxplot.png')
    plt.close()
    print(f'Finalizado {nome}. Média do melhor fitness: {np.mean(melhores_fitness):.4f} ± {np.std(melhores_fitness):.4f}\n') 