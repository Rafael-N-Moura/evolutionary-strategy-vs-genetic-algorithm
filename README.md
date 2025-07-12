# Relatório Completo: Comparação entre Algoritmo Genético e Estratégia Evolutiva

## 1. Introdução

### 1.1 Objetivo do Estudo
Este relatório apresenta uma análise comparativa detalhada entre o Algoritmo Genético (GA) e a Estratégia Evolutiva (ES) na otimização de funções de benchmark complexas. O objetivo principal é entender como diferentes abordagens evolutivas se comportam em problemas de otimização contínua de alta dimensão (d=30).

### 1.2 Funções de Benchmark Utilizadas
Foram utilizadas quatro funções de benchmark clássicas, cada uma com características específicas que desafiam os algoritmos de diferentes formas:

- **Função de Ackley**: Muitos mínimos locais, ótimo global em (0,0,...,0)
- **Função de Rastrigin**: Altamente multimodal, muitos mínimos locais rasos
- **Função de Schwefel**: Muitos mínimos locais, ótimo global distante da origem
- **Função de Rosenbrock**: Vale estreito e longo, ótimo global em (1,1,...,1)

### 1.3 Justificativa da Metodologia
A escolha de 30 execuções independentes para cada teste foi baseada na necessidade de obter resultados estatisticamente confiáveis, considerando a natureza estocástica dos algoritmos evolutivos. Esta abordagem permite identificar padrões de comportamento e avaliar a robustez dos métodos.

---

## 2. Implementação dos Algoritmos

### 2.1 Algoritmo Genético (GA)

#### 2.1.1 Estrutura e Representação
- **Representação**: Vetores de números reais de dimensão 30
- **População**: 100 indivíduos
- **Inicialização**: Valores aleatórios uniformemente distribuídos dentro dos limites de cada função

#### 2.1.2 Operadores Genéticos

**Seleção de Pais (Torneio Binário)**
```python
# Para cada novo pai, dois indivíduos são sorteados aleatoriamente
# O de melhor fitness (menor valor) é escolhido
```

**Justificativa**: O torneio binário mantém pressão seletiva adequada sem ser excessivamente elitista, permitindo que indivíduos com fitness intermediário também tenham chance de reproduzir.

**Recombinação (Crossover Aritmético)**
```python
# Para cada par de pais, dois filhos são gerados como:
filho1 = α × pai1 + (1-α) × pai2
filho2 = α × pai2 + (1-α) × pai1
# onde α é um valor aleatório entre 0 e 1
```

**Justificativa**: O crossover aritmético é adequado para problemas contínuos, pois preserva a continuidade do espaço de busca e permite combinações suaves entre soluções parentais.

**Mutação (Gaussiana)**
```python
# Cada gene tem probabilidade 1/d de sofrer mutação
# Mutação = valor_atual + N(0, 0.1)
# Valores são limitados aos intervalos válidos
```

**Justificativa**: A mutação gaussiana introduz variação contínua, adequada para problemas de otimização contínua. A probabilidade 1/d garante que, em média, um gene por indivíduo seja mutado.

**Seleção de Sobreviventes (Elitismo)**
```python
# O melhor indivíduo da geração anterior é sempre mantido
# O restante da população é preenchido pelos melhores descendentes
```

**Justificativa**: O elitismo garante que boas soluções não sejam perdidas, mas pode reduzir a diversidade se usado excessivamente.

### 2.2 Estratégia Evolutiva (ES)

#### 2.2.1 Estrutura e Representação
- **Tipo**: (μ, λ)-ES
- **μ (pais)**: 30 indivíduos
- **λ (filhos)**: 200 indivíduos
- **Representação**: Vetores de números reais de dimensão 30

#### 2.2.2 Operadores Evolutivos

**Recombinação (Intermediária)**
```python
# Para cada descendente, dois pais são escolhidos aleatoriamente
# O filho é a média dos dois pais
filho = (pai1 + pai2) / 2
```

**Justificativa**: A recombinação intermediária é conservadora e estável, adequada para problemas contínuos onde a exploração gradual é desejada.

**Mutação (Gaussiana)**
```python
# Cada gene de cada descendente recebe ruído gaussiano
# Mutação = valor_atual + N(0, 0.1)
# Valores são limitados aos intervalos válidos
```

**Justificativa**: Similar ao GA, mas aplicada a todos os descendentes, garantindo exploração adequada do espaço de busca.

**Seleção de Sobreviventes ((μ, λ)-ES)**
```python
# Apenas os μ melhores entre os λ descendentes formam a nova população
# Não há elitismo explícito
```

**Justificativa**: A pressão seletiva (λ ≫ μ) favorece a exploração e diversidade, mas pode dificultar a convergência em problemas com ótimos globais estreitos.

---

## 3. Resultados Experimentais Iniciais

### 3.1 Configuração dos Experimentos
- **Número de execuções**: 30 independentes por função/algoritmo
- **Total de execuções**: 240 (4 funções × 2 algoritmos × 30 execuções)
- **Número de gerações**: 1000
- **Dimensão**: 30

### 3.2 Resultados Estatísticos

| Função     | GA: Média ± DP   | ES: Média ± DP   | Melhor Algoritmo  |
| ---------- | ---------------- | ---------------- | ----------------- |
| Ackley     | 8.69 ± 0.97      | 8.24 ± 1.03      | ES (5.2% melhor)  |
| Rastrigin  | 13.37 ± 4.02     | 51.79 ± 6.06     | GA (74.2% melhor) |
| Schwefel   | 9580.41 ± 379.71 | 9098.40 ± 657.43 | ES (5.0% melhor)  |
| Rosenbrock | 5.90 ± 17.42     | 64.90 ± 18.25    | GA (90.9% melhor) |

### 3.3 Análise dos Resultados

**Ackley**: Ambos os algoritmos performaram bem, com leve vantagem para a ES. A função tem muitos mínimos locais, mas o ótimo global é relativamente fácil de encontrar.

**Rastrigin**: O GA superou significativamente a ES. Esta função tem muitos mínimos locais rasos, onde o elitismo do GA ajuda a manter boas soluções.

**Schwefel**: A ES obteve melhor média, mas com maior variabilidade. A função é altamente multimodal, beneficiando da maior pressão seletiva da ES.

**Rosenbrock**: O GA apresentou média muito superior, mas com alta variabilidade. O vale estreito da função é mais adequado ao crossover aritmético do GA.

---

## 4. Experimentos de Melhoria

### 4.1 Motivação dos Experimentos
Baseado nos resultados iniciais, identificamos oportunidades de melhoria específicas para cada algoritmo:

1. **GA em Rosenbrock**: Excelente média mas alta variabilidade
2. **ES em Rastrigin**: Desempenho muito inferior ao GA
3. **GA em outras funções**: Potencial para melhorias gerais

### 4.2 Algoritmo Genético V2 (GA V2)

#### 4.2.1 Melhorias Implementadas

**População Aumentada (100 → 200)**
- **Justificativa**: Maior diversidade genética, especialmente importante para funções com vales estreitos como Rosenbrock

**Taxa de Mutação Aumentada (1/d → 2/d)**
- **Justificativa**: Maior exploração do espaço de busca

**Mutação Adaptativa**
```python
# Se pouca melhoria nas últimas 10 gerações:
mutation_rate = mutation_rate * 1.5
# Se estagnação nas últimas 5 gerações:
std_dev = 0.2  # Aumentar desvio padrão
```

**Justificativa**: Ajuste dinâmico da mutação baseado no progresso, evitando convergência prematura

**Elitismo Reduzido (1 indivíduo → 20% da população)**
- **Justificativa**: Manter diversidade enquanto preserva boas soluções

#### 4.2.2 Resultados do GA V2

| Função     | GA Original      | GA V2            | Melhoria |
| ---------- | ---------------- | ---------------- | -------- |
| Ackley     | 8.69 ± 0.97      | 5.37 ± 0.86      | 38.3%    |
| Rastrigin  | 13.37 ± 4.02     | 16.35 ± 8.43     | -22.3%   |
| Schwefel   | 9580.41 ± 379.71 | 7388.04 ± 478.98 | 22.9%    |
| Rosenbrock | 5.90 ± 17.42     | 2.12 ± 0.59      | 64.0%    |

**Análise**: O GA V2 foi muito eficaz em Ackley, Schwefel e Rosenbrock, mas piorou em Rastrigin. Isso sugere que as melhorias são específicas para certos tipos de problemas.

### 4.3 Estratégia Evolutiva V2 (ES V2)

#### 4.3.1 Melhorias Implementadas

**Pressão Seletiva Reduzida (λ=200 → λ=150)**
- **Justificativa**: Menor pressão seletiva para permitir mais exploração

**População Aumentada (μ=30 → μ=50)**
- **Justificativa**: Maior diversidade na população parental

**Recombinação Uniforme**
```python
# Para cada gene, escolher aleatoriamente entre os dois pais
filho[i] = pai1[i] se random() < 0.5 else pai2[i]
```

**Justificativa**: Maior diversidade genética na recombinação

**Elitismo Adicionado**
- **Justificativa**: Preservar o melhor indivíduo entre gerações

#### 4.3.2 Resultados do ES V2

**Rastrigin**: 72.54 ± 6.88 (piorou 40.1% vs original)

**Análise**: As mudanças agressivas pioraram o desempenho, indicando que a abordagem original era mais adequada para Rastrigin.

### 4.4 Estratégia Evolutiva V3 (ES V3)

#### 4.4.1 Ajustes Conservadores

**Parâmetros Intermediários**
- μ=40 (entre original 30 e V2 50)
- λ=180 (entre original 200 e V2 150)
- Recombinação intermediária (voltar ao original)
- Manter elitismo

**Justificativa**: Ajustes incrementais baseados nos resultados da V2

#### 4.4.2 Resultados do ES V3

**Rastrigin**: 30.66 ± 3.64 (melhorou 40.8% vs original)

**Análise**: A abordagem conservadora funcionou melhor, confirmando que ajustes incrementais são mais seguros.

---

## 5. Análise Estatística Detalhada

### 5.1 Boxplots Comparativos

Os boxplots gerados fornecem insights visuais importantes:

**Distribuição dos Resultados**
- Mostram a variabilidade entre execuções
- Identificam outliers (execuções excepcionalmente boas ou ruins)
- Permitem comparação direta entre algoritmos

**Interpretação dos Boxplots**
- **Mediana**: Tendência central dos resultados
- **Quartis**: Dispersão dos dados
- **Outliers**: Execuções atípicas que podem indicar convergência para ótimos locais diferentes

### 5.2 Análise de Robustez

**GA Original**
- Mais robusto em Rastrigin e Rosenbrock
- Menor variabilidade em funções com mínimos locais rasos

**ES Original**
- Mais robusto em Schwefel
- Maior variabilidade, mas melhor média em funções altamente multimodais

**GA V2**
- Melhorou significativamente a robustez em Rosenbrock
- Manteve boa performance em Ackley e Schwefel
- Piorou em Rastrigin (overfitting para outros tipos de problemas)

**ES V3**
- Melhorou a robustez em Rastrigin
- Demonstrou que ajustes incrementais são mais seguros

---

## 6. Conclusões e Recomendações

### 6.1 Principais Descobertas

1. **Não existe algoritmo universalmente superior**
   - Cada função requer abordagens específicas
   - As características do problema determinam o melhor método

2. **GA é mais eficaz para problemas com mínimos locais rasos**
   - Excelente em Rastrigin e Rosenbrock
   - Beneficia do elitismo e crossover aritmético

3. **ES é mais eficaz para problemas altamente multimodais**
   - Melhor em Schwefel
   - Beneficia da maior pressão seletiva

4. **Melhorias específicas são mais eficazes que generalistas**
   - GA V2 funcionou bem em 3 de 4 funções
   - ES V3 foi mais eficaz que ES V2

### 6.2 Recomendações Práticas

**Para Problemas com Mínimos Locais Rasos (ex: Rastrigin)**
- Use GA com elitismo
- Considere população maior e mutação adaptativa

**Para Problemas Altamente Multimodais (ex: Schwefel)**
- Use ES com pressão seletiva adequada
- Evite ajustes muito agressivos

**Para Problemas com Vales Estreitos (ex: Rosenbrock)**
- Use GA com população maior
- Implemente mutação adaptativa

**Para Aplicações Práticas**
- Sempre realize múltiplas execuções
- Use análise estatística robusta
- Teste diferentes configurações
- Considere características específicas do problema

### 6.3 Limitações e Trabalhos Futuros

**Limitações do Estudo**
- Testado apenas em funções de benchmark
- Parâmetros fixos para cada algoritmo
- Dimensão fixa (d=30)

**Trabalhos Futuros Sugeridos**
- Testar em problemas reais de otimização
- Implementar parâmetros adaptativos
- Explorar dimensões variadas
- Desenvolver métodos híbridos
- Implementar testes estatísticos formais (teste t, ANOVA)

---

## 7. Referências e Arquivos Gerados

### 7.1 Arquivos de Resultados
- `resultados/ga_*_melhores_fitness.txt`: Melhores fitness do GA
- `resultados/es_*_melhores_fitness.txt`: Melhores fitness da ES
- `resultados/*_convergencia_media.txt`: Histórico médio de convergência
- `resultados/*_estatisticas.txt`: Estatísticas detalhadas

### 7.2 Gráficos Gerados
- `resultados/boxplot_comparativo_*.png`: Boxplots comparativos
- `resultados/*_convergencia_media.png`: Gráficos de convergência
- `resultados/comparacao_*.png`: Comparações visuais

### 7.3 Código Fonte
- `algoritmos/genetic_algorithm.py`: GA original
- `algoritmos/genetic_algorithm_v2.py`: GA melhorado
- `algoritmos/evolution_strategy.py`: ES original
- `algoritmos/evolution_strategy_v2.py`: ES agressivo
- `algoritmos/evolution_strategy_v3.py`: ES conservador

---

## 8. Apêndice: Análise Técnica Detalhada

### 8.1 Complexidade Computacional
- **GA**: O(n × g × p) onde n=dimensão, g=gerações, p=tamanho população
- **ES**: O(n × g × λ) onde λ=número de descendentes

### 8.2 Análise de Convergência
Os gráficos de convergência mostram:
- Velocidade de convergência inicial
- Estagnação em ótimos locais
- Eficácia das estratégias de escape

### 8.3 Impacto dos Parâmetros
- **População**: Maior população = mais diversidade, mas mais custo computacional
- **Mutação**: Maior mutação = mais exploração, mas pode prejudicar convergência
- **Pressão Seletiva**: Maior pressão = convergência mais rápida, mas risco de ótimos locais

 
