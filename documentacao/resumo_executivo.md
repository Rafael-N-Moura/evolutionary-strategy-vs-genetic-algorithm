# Resumo Executivo — Comparação: Algoritmo Genético vs Estratégia Evolutiva

## Objetivo
Avaliar e comparar o desempenho do Algoritmo Genético (GA) e da Estratégia Evolutiva (ES) na otimização de funções complexas (Ackley, Rastrigin, Schwefel, Rosenbrock) em alta dimensão (d=30).

---

## Principais Resultados
- **Robustez Estatística:** Ambos os métodos foram avaliados em 30 execuções independentes para cada função, garantindo confiabilidade estatística dos resultados.
- **Eficiência em Diferentes Funções:**
  - **GA** foi mais eficiente e robusto na função Rastrigin, apresentando menor média e menor variabilidade dos melhores resultados.
  - **ES** obteve melhor desempenho médio nas funções Ackley e Schwefel, embora com maior variabilidade.
  - Para Rosenbrock, o GA apresentou resultados muito bons em algumas execuções, mas com alta variabilidade; a ES foi mais estável, porém menos eficiente.
- **Variabilidade:** O desvio padrão dos resultados indica que ambos os métodos podem apresentar variações significativas entre execuções, especialmente em funções mais difíceis.

---

## Recomendações Práticas
- **Escolha do Algoritmo:**
  - Prefira o **GA** para funções com muitos mínimos locais rasos (ex: Rastrigin) ou quando a robustez for prioridade.
  - Considere a **ES** para funções altamente multimodais ou com vales estreitos (ex: Schwefel, Ackley), especialmente se a diversidade de soluções for desejada.
- **Execuções Múltiplas:** Sempre realize múltiplas execuções e utilize estatísticas (média, desvio padrão, boxplot) para avaliar o desempenho real dos algoritmos.
- **Ajuste de Parâmetros:** Parâmetros como tamanho da população, intensidade da mutação e pressão seletiva podem ser ajustados para melhorar o desempenho em problemas específicos.

---

## Implicações para Projetos de Otimização
- Não existe um algoritmo universalmente superior: a escolha deve considerar as características do problema e a necessidade de robustez ou exploração.
- A análise estatística é fundamental para evitar conclusões precipitadas baseadas em execuções isoladas.
- Métodos híbridos ou adaptativos podem ser explorados para problemas de maior complexidade.

---

## Conclusão
Tanto o Algoritmo Genético quanto a Estratégia Evolutiva são ferramentas poderosas para otimização global. A escolha entre eles deve ser guiada por testes práticos, análise estatística e conhecimento das características do problema a ser resolvido. 