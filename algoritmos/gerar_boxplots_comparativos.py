import numpy as np
import matplotlib.pyplot as plt
import os

# Configurações para melhor visualização
plt.rcParams['figure.figsize'] = (15, 10)
plt.rcParams['font.size'] = 12

# Funções para análise
FUNCOES = ['ackley', 'rastrigin', 'schwefel', 'rosenbrock']

def carregar_resultados(funcao, algoritmo, versao=''):
    """Carrega os resultados de um algoritmo específico"""
    arquivo = f'resultados/{algoritmo}{versao}_{funcao}_melhores_fitness.txt'
    if os.path.exists(arquivo):
        return np.loadtxt(arquivo)
    else:
        return None

def criar_boxplot_comparativo(funcao):
    """Cria boxplot comparativo para uma função específica"""
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    
    # 1. Comparação Original: GA vs ES
    ga_orig = carregar_resultados(funcao, 'ga', '')
    es_orig = carregar_resultados(funcao, 'es', '')
    
    if ga_orig is not None and es_orig is not None:
        ax1.boxplot([ga_orig, es_orig], tick_labels=['GA Original', 'ES Original'])
        ax1.set_title(f'{funcao.capitalize()} - Comparação Original')
        ax1.set_ylabel('Melhor Fitness')
        ax1.grid(True, alpha=0.3)
    
    # 2. Comparação GA: Original vs V2
    ga_v2 = carregar_resultados(funcao, 'ga', '_v2')
    
    if ga_orig is not None and ga_v2 is not None:
        ax2.boxplot([ga_orig, ga_v2], tick_labels=['GA Original', 'GA V2'])
        ax2.set_title(f'{funcao.capitalize()} - GA Original vs V2')
        ax2.set_ylabel('Melhor Fitness')
        ax2.grid(True, alpha=0.3)
    
    # 3. Comparação ES: Original vs V2 vs V3 (apenas para Rastrigin)
    if funcao == 'rastrigin':
        es_v2 = carregar_resultados(funcao, 'es', '_v2')
        es_v3 = carregar_resultados(funcao, 'es', '_v3')
        
        if es_orig is not None and es_v2 is not None and es_v3 is not None:
            ax3.boxplot([es_orig, es_v2, es_v3], tick_labels=['ES Original', 'ES V2', 'ES V3'])
            ax3.set_title(f'{funcao.capitalize()} - ES Original vs V2 vs V3')
            ax3.set_ylabel('Melhor Fitness')
            ax3.grid(True, alpha=0.3)
        elif es_orig is not None and es_v3 is not None:
            ax3.boxplot([es_orig, es_v3], tick_labels=['ES Original', 'ES V3'])
            ax3.set_title(f'{funcao.capitalize()} - ES Original vs V3')
            ax3.set_ylabel('Melhor Fitness')
            ax3.grid(True, alpha=0.3)
    else:
        # Para outras funções, mostrar apenas ES Original
        if es_orig is not None:
            ax3.boxplot([es_orig], tick_labels=['ES Original'])
            ax3.set_title(f'{funcao.capitalize()} - ES Original')
            ax3.set_ylabel('Melhor Fitness')
            ax3.grid(True, alpha=0.3)
    
    # 4. Comparação Melhorada: GA V2 vs ES V3 (apenas para Rastrigin)
    if funcao == 'rastrigin' and ga_v2 is not None and es_v3 is not None:
        ax4.boxplot([ga_v2, es_v3], tick_labels=['GA V2', 'ES V3'])
        ax4.set_title(f'{funcao.capitalize()} - Melhorado: GA V2 vs ES V3')
        ax4.set_ylabel('Melhor Fitness')
        ax4.grid(True, alpha=0.3)
    else:
        # Para outras funções, mostrar GA V2 vs ES Original
        if ga_v2 is not None and es_orig is not None:
            ax4.boxplot([ga_v2, es_orig], tick_labels=['GA V2', 'ES Original'])
            ax4.set_title(f'{funcao.capitalize()} - GA V2 vs ES Original')
            ax4.set_ylabel('Melhor Fitness')
            ax4.grid(True, alpha=0.3)
        elif ga_v2 is not None:
            ax4.boxplot([ga_v2], tick_labels=['GA V2'])
            ax4.set_title(f'{funcao.capitalize()} - GA V2')
            ax4.set_ylabel('Melhor Fitness')
            ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f'resultados/boxplot_comparativo_{funcao}.png', dpi=300, bbox_inches='tight')
    plt.close()

def criar_boxplot_geral():
    """Cria boxplot geral comparando todos os algoritmos em todas as funções"""
    fig, axes = plt.subplots(2, 2, figsize=(20, 15))
    axes = axes.flatten()
    
    for i, funcao in enumerate(FUNCOES):
        ax = axes[i]
        
        # Carregar todos os dados disponíveis
        dados = []
        labels = []
        
        # GA Original
        ga_orig = carregar_resultados(funcao, 'ga', '')
        if ga_orig is not None:
            dados.append(ga_orig)
            labels.append('GA Original')
        
        # ES Original
        es_orig = carregar_resultados(funcao, 'es', '')
        if es_orig is not None:
            dados.append(es_orig)
            labels.append('ES Original')
        
        # GA V2
        ga_v2 = carregar_resultados(funcao, 'ga', '_v2')
        if ga_v2 is not None:
            dados.append(ga_v2)
            labels.append('GA V2')
        
        # ES V2 e V3 (apenas para Rastrigin)
        if funcao == 'rastrigin':
            es_v2 = carregar_resultados(funcao, 'es', '_v2')
            if es_v2 is not None:
                dados.append(es_v2)
                labels.append('ES V2')
            
            es_v3 = carregar_resultados(funcao, 'es', '_v3')
            if es_v3 is not None:
                dados.append(es_v3)
                labels.append('ES V3')
        
        if dados:
            bp = ax.boxplot(dados, tick_labels=labels)
            ax.set_title(f'{funcao.capitalize()}', fontsize=14, fontweight='bold')
            ax.set_ylabel('Melhor Fitness')
            ax.grid(True, alpha=0.3)
            
            # Rotacionar labels se necessário
            if len(labels) > 3:
                ax.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig('resultados/boxplot_comparativo_geral.png', dpi=300, bbox_inches='tight')
    plt.close()

def gerar_estatisticas_comparativas():
    """Gera arquivo com estatísticas comparativas detalhadas"""
    with open('resultados/estatisticas_comparativas.txt', 'w') as f:
        f.write("=== ESTATÍSTICAS COMPARATIVAS DETALHADAS ===\n\n")
        
        for funcao in FUNCOES:
            f.write(f"--- {funcao.upper()} ---\n")
            
            # Carregar dados
            ga_orig = carregar_resultados(funcao, 'ga', '')
            es_orig = carregar_resultados(funcao, 'es', '')
            ga_v2 = carregar_resultados(funcao, 'ga', '_v2')
            
            # ES V2 e V3 apenas para Rastrigin
            es_v2 = None
            es_v3 = None
            if funcao == 'rastrigin':
                es_v2 = carregar_resultados(funcao, 'es', '_v2')
                es_v3 = carregar_resultados(funcao, 'es', '_v3')
            
            # Estatísticas GA Original
            if ga_orig is not None:
                f.write(f"GA Original: {np.mean(ga_orig):.4f} ± {np.std(ga_orig):.4f}\n")
                f.write(f"  - Mínimo: {np.min(ga_orig):.4f}\n")
                f.write(f"  - Máximo: {np.max(ga_orig):.4f}\n")
                f.write(f"  - Mediana: {np.median(ga_orig):.4f}\n")
            
            # Estatísticas ES Original
            if es_orig is not None:
                f.write(f"ES Original: {np.mean(es_orig):.4f} ± {np.std(es_orig):.4f}\n")
                f.write(f"  - Mínimo: {np.min(es_orig):.4f}\n")
                f.write(f"  - Máximo: {np.max(es_orig):.4f}\n")
                f.write(f"  - Mediana: {np.median(es_orig):.4f}\n")
            
            # Comparação GA vs ES Original
            if ga_orig is not None and es_orig is not None:
                if np.mean(ga_orig) < np.mean(es_orig):
                    melhor = "GA"
                    pct_melhoria = ((np.mean(es_orig) - np.mean(ga_orig)) / np.mean(es_orig)) * 100
                else:
                    melhor = "ES"
                    pct_melhoria = ((np.mean(ga_orig) - np.mean(es_orig)) / np.mean(ga_orig)) * 100
                f.write(f"Melhor Original: {melhor} ({pct_melhoria:.1f}% melhor)\n")
            
            # Estatísticas GA V2
            if ga_v2 is not None:
                f.write(f"GA V2: {np.mean(ga_v2):.4f} ± {np.std(ga_v2):.4f}\n")
                if ga_orig is not None:
                    melhoria = ((np.mean(ga_orig) - np.mean(ga_v2)) / np.mean(ga_orig)) * 100
                    f.write(f"  - Melhoria vs GA Original: {melhoria:.1f}%\n")
            
            # Estatísticas ES V2 e V3 (apenas para Rastrigin)
            if funcao == 'rastrigin':
                if es_v2 is not None:
                    f.write(f"ES V2: {np.mean(es_v2):.4f} ± {np.std(es_v2):.4f}\n")
                    if es_orig is not None:
                        melhoria = ((np.mean(es_orig) - np.mean(es_v2)) / np.mean(es_orig)) * 100
                        f.write(f"  - Melhoria vs ES Original: {melhoria:.1f}%\n")
                
                if es_v3 is not None:
                    f.write(f"ES V3: {np.mean(es_v3):.4f} ± {np.std(es_v3):.4f}\n")
                    if es_orig is not None:
                        melhoria = ((np.mean(es_orig) - np.mean(es_v3)) / np.mean(es_orig)) * 100
                        f.write(f"  - Melhoria vs ES Original: {melhoria:.1f}%\n")
            
            f.write("\n")

# Executar análise
print("=== GERANDO BOXPLOTS COMPARATIVOS (VERSÃO CORRIGIDA) ===")

# Criar boxplots individuais para cada função
for funcao in FUNCOES:
    print(f"Gerando boxplot para {funcao}...")
    criar_boxplot_comparativo(funcao)

# Criar boxplot geral
print("Gerando boxplot geral...")
criar_boxplot_geral()

# Gerar estatísticas comparativas
print("Gerando estatísticas comparativas...")
gerar_estatisticas_comparativas()

print("=== ANÁLISE COMPLETA FINALIZADA ===")
print("Arquivos gerados:")
print("- resultados/boxplot_comparativo_[funcao].png")
print("- resultados/boxplot_comparativo_geral.png")
print("- resultados/estatisticas_comparativas.txt") 