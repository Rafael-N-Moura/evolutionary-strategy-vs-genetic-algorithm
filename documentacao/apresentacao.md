# Apresentação: Algoritmo Genético vs Estratégia Evolutiva

---

## Slide 1: Título
# Comparação de Algoritmos Evolutivos
### GA vs ES para Otimização de Funções de Benchmark

**Aluno:** [Seu Nome]  
**Disciplina:** Computação Bioinspirada  
**Data:** [Data da Apresentação]

---

## Slide 2: Objetivos
### Objetivo Principal
- Comparar o desempenho do **Algoritmo Genético (GA)** e da **Estratégia Evolutiva (ES)** na otimização de funções complexas

### Objetivos Específicos
- Implementar GA e ES em Python
- Testar em 4 funções de benchmark (d=30)
- Realizar análise estatística robusta (30 execuções)
- Identificar pontos fortes de cada método

---

## Slide 3: Funções de Benchmark
### Funções Testadas (d = 30)

| Função         | Características       | Limites           |
| -------------- | --------------------- | ----------------- |
| **Ackley**     | Muitos mínimos locais | [-32.768, 32.768] |
| **Rastrigin**  | Altamente multimodal  | [-5.12, 5.12]     |
| **Schwefel**   | Muitos mínimos locais | [-500, 500]       |
| **Rosenbrock** | Vale estreito         | [-5, 10]          |

---

## Slide 4: Metodologia - GA
### Algoritmo Genético Implementado

**Representação:** Vetores reais (30 dimensões)  
**População:** 100 indivíduos  
**Seleção:** Torneio binário  
**Crossover:** Aritmético (média dos pais)  
**Mutação:** Gaussiana (prob. 1/d)  
**Elitismo:** Sim (melhor sobrevive)  
**Gerações:** 1000

---

## Slide 5: Metodologia - ES
### Estratégia Evolutiva Implementada

**Tipo:** (μ, λ)-ES  
**μ (pais):** 30 indivíduos  
**λ (filhos):** 200 indivíduos  
**Recombinação:** Intermediária  
**Mutação:** Gaussiana  
**Seleção:** μ melhores filhos  
**Gerações:** 1000

---

## Slide 6: Configuração Experimental
### Parâmetros dos Experimentos

- **Execuções:** 30 independentes por função/algoritmo
- **Total:** 240 execuções (4 funções × 2 algoritmos × 30 execuções)
- **Análise:** Média, desvio padrão, boxplots
- **Gráficos:** Convergência média com faixa de confiança

---

## Slide 7: Resultados - Tabela Comparativa
### Melhores Fitness (Média ± Desvio Padrão)

| Função         | GA               | ES                   |
| -------------- | ---------------- | -------------------- |
| **Ackley**     | 8.69 ± 0.97      | **8.24 ± 1.03**      |
| **Rastrigin**  | **13.37 ± 4.02** | 51.79 ± 6.06         |
| **Schwefel**   | 9580.41 ± 379.71 | **9098.40 ± 657.43** |
| **Rosenbrock** | 5.90 ± 17.42     | 64.90 ± 18.25        |

*Melhor resultado em **negrito***

---

## Slide 8: Análise por Função - Ackley
### Resultados Ackley
- **ES:** Ligeiramente melhor (8.24 vs 8.69)
- **Variabilidade:** Similar entre os métodos
- **Conclusão:** Ambos performam bem, ES tem pequena vantagem

---

## Slide 9: Análise por Função - Rastrigin
### Resultados Rastrigin
- **GA:** Muito superior (13.37 vs 51.79)
- **Robustez:** GA mais consistente (menor DP)
- **Conclusão:** GA é claramente melhor para esta função

---

## Slide 10: Análise por Função - Schwefel
### Resultados Schwefel
- **ES:** Melhor média (9098 vs 9580)
- **Variabilidade:** ES mais variável (maior DP)
- **Conclusão:** ES encontra melhores soluções, mas menos consistente

---

## Slide 11: Análise por Função - Rosenbrock
### Resultados Rosenbrock
- **GA:** Média melhor (5.90 vs 64.90)
- **Variabilidade:** GA muito variável (DP alto)
- **Conclusão:** GA pode encontrar soluções excelentes, mas é instável

---

## Slide 12: Principais Achados
### Descobertas Importantes

✅ **GA é mais robusto** para funções com mínimos locais rasos  
✅ **ES é mais eficiente** para funções altamente multimodais  
✅ **Variabilidade significativa** entre execuções  
✅ **Não existe algoritmo universalmente superior**

---

## Slide 13: Recomendações Práticas
### Quando Usar Cada Algoritmo

**Use GA quando:**
- Função tem muitos mínimos locais rasos
- Robustez é prioridade
- Consistência é importante

**Use ES quando:**
- Função é altamente multimodal
- Exploração é necessária
- Diversidade de soluções é desejada

---

## Slide 14: Lições Aprendidas
### Insights Importantes

🔍 **Análise estatística é fundamental**  
🔍 **Múltiplas execuções são essenciais**  
🔍 **Características da função determinam o melhor método**  
🔍 **Parâmetros podem ser ajustados para melhorar performance**

---

## Slide 15: Conclusões
### Resumo Final

- **GA e ES** são ambos ferramentas poderosas
- **Escolha depende** das características do problema
- **Testes práticos** são necessários para decisão
- **Análise estatística** evita conclusões precipitadas

---

## Slide 16: Obrigado!
### Perguntas e Discussão

**Contato:** [Seu Email]  
**Código:** Disponível no repositório  
**Documentação:** Completa na pasta `documentacao/`

**Obrigado pela atenção!** 