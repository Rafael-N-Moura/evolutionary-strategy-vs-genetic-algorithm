# Estratégia Evolutiva (ES) — Documentação Detalhada

## 1. Descrição Esquemática do Algoritmo
A Estratégia Evolutiva (ES) é um método de otimização inspirado na evolução biológica, especialmente adaptado para problemas contínuos. Utiliza uma população de soluções (indivíduos) que evoluem por recombinação, mutação e seleção dos melhores descendentes.

Fluxo básico ((μ, λ)-ES):
1. Inicializar uma população de μ indivíduos aleatórios.
2. Avaliar o fitness de cada indivíduo.
3. Repetir por várias gerações:
   - Gerar λ descendentes por recombinação dos pais.
   - Aplicar mutação nos descendentes.
   - Selecionar os μ melhores descendentes para formar a nova população.
4. Retornar o melhor indivíduo encontrado.

---

## 2. Descrição dos Processos

### a. Representação das Soluções (Indivíduos)
Cada indivíduo é um vetor de números reais de dimensão `d = 30`, representando uma possível solução para o problema.

### b. Função de Fitness
A função de fitness é a própria função objetivo (Ackley, Rastrigin, Schwefel ou Rosenbrock). O objetivo é minimizar esse valor.

### c. População
- **Tamanho (μ):** 30 indivíduos.
- **Inicialização:** Cada gene do vetor é inicializado aleatoriamente dentro dos limites definidos para cada função.

### d. Recombinação
- **Método:** Recombinação intermediária. Para cada descendente, dois pais são escolhidos aleatoriamente e o filho é a média dos dois.
- **Número de descendentes (λ):** 200 por geração.

### e. Mutação
- Cada gene de cada descendente recebe um ruído gaussiano (média 0, desvio padrão 0.1).
- Após a mutação, os valores são limitados aos intervalos válidos da função.

### f. Processo de Seleção por Sobrevivência
- **(μ, λ)-ES:** Apenas os μ melhores entre os λ descendentes formam a nova população.
- Não há elitismo explícito: apenas os melhores descendentes sobrevivem.

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
- O código está em `algoritmos/evolution_strategy.py`.
- Para rodar experimentos, execute `algoritmos/experimentos_es.py`.
- Os parâmetros principais (μ, λ, número de gerações, limites) podem ser ajustados no script de experimentos.
- Para usar a ES em outra função, basta passar a função objetivo desejada ao instanciar `EvolutionStrategy`.

---

## 5. Observações
- A ES é estocástica: resultados podem variar entre execuções.
- Recomenda-se rodar múltiplas execuções para análise estatística.
- O valor de λ deve ser significativamente maior que μ para garantir pressão seletiva e diversidade. 