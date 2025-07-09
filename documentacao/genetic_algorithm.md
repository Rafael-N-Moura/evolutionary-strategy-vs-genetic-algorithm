# Algoritmo Genético (GA) — Documentação Detalhada

## 1. Descrição Esquemática do Algoritmo
O Algoritmo Genético (GA) é um método de otimização inspirado na evolução natural. Ele utiliza uma população de soluções candidatas (indivíduos), que evoluem ao longo de gerações por meio de seleção, recombinação (crossover) e mutação, buscando encontrar o mínimo global de uma função objetivo.

Fluxo básico:
1. Inicializar uma população de indivíduos aleatórios.
2. Avaliar o fitness de cada indivíduo.
3. Repetir por várias gerações:
   - Selecionar pais com base no fitness.
   - Gerar descendentes por recombinação (crossover).
   - Aplicar mutação nos descendentes.
   - Selecionar sobreviventes para a próxima geração (com elitismo).
4. Retornar o melhor indivíduo encontrado.

---

## 2. Descrição dos Processos

### a. Representação das Soluções (Indivíduos)
Cada indivíduo é um vetor de números reais de dimensão `d = 30`, representando uma possível solução para o problema.

### b. Função de Fitness
A função de fitness é a própria função objetivo (Ackley, Rastrigin, Schwefel ou Rosenbrock). O objetivo é minimizar esse valor.

### c. População
- **Tamanho:** 100 indivíduos.
- **Inicialização:** Cada gene do vetor é inicializado aleatoriamente dentro dos limites definidos para cada função.

### d. Processo de Seleção
- **Método:** Torneio binário. Para cada novo pai, dois indivíduos são sorteados aleatoriamente e o de melhor fitness é escolhido.

### e. Operadores Genéticos
- **Recombinação (Crossover):**
  - Crossover aritmético: para cada par de pais, dois filhos são gerados como combinações lineares dos pais.
- **Mutação:**
  - Cada gene tem probabilidade `1/d` de sofrer mutação, recebendo um ruído gaussiano (média 0, desvio padrão 0.1). O valor é limitado aos intervalos válidos.

### f. Processo de Seleção por Sobrevivência
- **Elitismo:** O melhor indivíduo da geração anterior é sempre mantido. O restante da nova população é preenchido pelos melhores descendentes.

### g. Condições de Término
- O algoritmo executa por um número fixo de gerações (1000).

---

## 3. Descrição dos Resultados Experimentais
- Para cada função, são salvos:
  - O melhor fitness encontrado
  - O vetor do melhor indivíduo
  - O histórico de convergência (melhor fitness por geração)
  - Gráfico de convergência (PNG)
- Os arquivos ficam na pasta `resultados/`.
- O gráfico mostra a evolução do melhor fitness ao longo das gerações, permitindo analisar a convergência do algoritmo.

---

## 4. Guia de Implementação e Uso
- O código está em `algoritmos/genetic_algorithm.py`.
- Para rodar experimentos, execute `algoritmos/experimentos_ga.py`.
- Os parâmetros principais (tamanho da população, número de gerações, limites) podem ser ajustados no script de experimentos.
- Para usar o GA em outra função, basta passar a função objetivo desejada ao instanciar `GeneticAlgorithm`.

---

## 5. Observações
- O GA é estocástico: resultados podem variar entre execuções.
- Recomenda-se rodar múltiplas execuções para análise estatística.
- O elitismo ajuda a evitar a perda de boas soluções, mas pode reduzir a diversidade se usado em excesso. 