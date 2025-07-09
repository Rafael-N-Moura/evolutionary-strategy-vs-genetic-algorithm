# Análise dos Resultados Experimentais — GA vs ES

## 1. Introdução
Esta análise compara o desempenho do Algoritmo Genético (GA) e da Estratégia Evolutiva (ES) na otimização das funções Ackley, Rastrigin, Schwefel e Rosenbrock, todas com dimensão 30. Os experimentos foram realizados com 30 execuções independentes para cada função e algoritmo.

---

## 2. Tabela Estatística dos Melhores Fitness Encontrados

| Função     | GA: Média ± DP   | ES: Média ± DP   |
| ---------- | ---------------- | ---------------- |
| Ackley     | 8.69 ± 0.97      | 8.24 ± 1.03      |
| Rastrigin  | 13.37 ± 4.02     | 51.79 ± 6.06     |
| Schwefel   | 9580.41 ± 379.71 | 9098.40 ± 657.43 |
| Rosenbrock | 5.90 ± 17.42     | 64.90 ± 18.25    |

*Valores obtidos a partir de 30 execuções para cada função e algoritmo.*

---

## 3. Análise de Convergência e Robustez
- **Ackley:** Ambos os métodos apresentaram médias próximas, com leve vantagem para a ES. A variabilidade (DP) é semelhante.
- **Rastrigin:** O GA superou a ES com folga, apresentando menor média e menor desvio padrão, indicando maior robustez e eficiência para esta função.
- **Schwefel:** A ES obteve melhor média, mas com maior variabilidade. O GA apresentou resultados mais consistentes, porém piores em média.
- **Rosenbrock:** O GA apresentou média muito inferior à ES, mas com alto desvio padrão, indicando que em algumas execuções encontrou soluções muito boas, mas em outras ficou preso em mínimos locais. A ES foi mais estável, porém menos eficiente.

Os gráficos de convergência média e boxplots (arquivos PNG em `resultados/`) ilustram a distribuição dos resultados e a evolução do melhor fitness ao longo das gerações.

---

## 4. Conclusão
- **GA** é mais robusto e eficiente para funções como Rastrigin e, em algumas execuções, pode superar a ES em Rosenbrock.
- **ES** apresenta melhor desempenho médio em Ackley e Schwefel, mas com maior variabilidade.
- A escolha do algoritmo ideal depende das características da função e da necessidade de robustez ou busca por ótimos globais.

---

## 5. Recomendações
- Para aplicações práticas, recomenda-se rodar múltiplas execuções e analisar estatísticas (média, DP, boxplot).
- Ajustar parâmetros (população, mutação, recombinação) pode melhorar o desempenho em funções específicas.
- Explorar variantes híbridas ou adaptativas pode ser interessante para problemas mais complexos.

---

## 6. Próximos Passos Sugeridos
- Realizar múltiplas execuções para obter médias e desvios padrão dos resultados.
- Testar diferentes parâmetros (população, mutação, recombinação) para cada algoritmo.
- Explorar variantes híbridas ou adaptativas para problemas mais complexos. 