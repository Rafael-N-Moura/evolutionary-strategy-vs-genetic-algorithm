# Roteiro de Apresentação: GA vs ES - Análise Comparativa

## Estrutura Geral da Apresentação
**Duração Estimada:** 20-25 minutos  
**Público:** Acadêmico/Profissional  
**Formato:** Slides + Demonstração Visual

---

## SLIDE 1: Título e Introdução (2 minutos)

### Conteúdo do Slide:
- Título: "Comparação entre Algoritmo Genético e Estratégia Evolutiva"
- Subtítulo: "Análise Experimental em Funções de Benchmark"
- Nome do apresentador
- Data

### Pontos de Fala:
1. **Boas-vindas e introdução pessoal**
2. **Contexto do trabalho:** "Hoje vou apresentar uma análise comparativa detalhada entre dois algoritmos evolutivos..."
3. **Motivação:** "A escolha entre GA e ES é frequente em problemas de otimização, mas faltam estudos comparativos robustos"

### Transição:
"Vamos começar entendendo o que motivou este estudo..."

---

## SLIDE 2: Objetivos e Motivação (2 minutos)

### Conteúdo do Slide:
- Objetivo principal
- 4 objetivos específicos
- Justificativa da metodologia

### Pontos de Fala:
1. **Objetivo principal:** "Comparar GA e ES em problemas de otimização contínua de alta dimensão"
2. **Metodologia robusta:** "30 execuções independentes para cada teste, garantindo confiabilidade estatística"
3. **Escopo:** "4 funções de benchmark clássicas, dimensão 30"

### Transição:
"Antes de mostrar os resultados, preciso explicar como implementamos cada algoritmo..."

---

## SLIDE 3: Funções de Benchmark (1.5 minutos)

### Conteúdo do Slide:
- Tabela com as 4 funções
- Características de cada uma
- Limites de busca

### Pontos de Fala:
1. **Ackley:** "Muitos mínimos locais, mas ótimo global relativamente fácil"
2. **Rastrigin:** "Altamente multimodal, muitos mínimos locais rasos"
3. **Schwefel:** "Muitos mínimos locais, ótimo global distante"
4. **Rosenbrock:** "Vale estreito e longo, ótimo global em (1,1,...,1)"

### Transição:
"Agora vou explicar como implementamos cada algoritmo..."

---

## SLIDE 4: Implementação do GA (2 minutos)

### Conteúdo do Slide:
- Estrutura: população, representação
- Operadores: seleção, crossover, mutação, elitismo
- Parâmetros principais

### Pontos de Fala:
1. **Representação:** "Vetores reais de dimensão 30, população de 100 indivíduos"
2. **Seleção:** "Torneio binário - mantém pressão seletiva adequada"
3. **Crossover:** "Aritmético - preserva continuidade do espaço de busca"
4. **Mutação:** "Gaussiana com probabilidade 1/d"
5. **Elitismo:** "Garante que boas soluções não sejam perdidas"

### Transição:
"Agora a Estratégia Evolutiva, que tem uma abordagem diferente..."

---

## SLIDE 5: Implementação da ES (2 minutos)

### Conteúdo do Slide:
- Tipo: (μ, λ)-ES
- Operadores: recombinação, mutação, seleção
- Diferenças em relação ao GA

### Pontos de Fala:
1. **Estrutura:** "(30, 200)-ES - 30 pais geram 200 filhos"
2. **Recombinação:** "Intermediária - mais conservadora que o GA"
3. **Mutação:** "Aplicada a todos os descendentes"
4. **Seleção:** "Apenas os 30 melhores filhos sobrevivem"
5. **Pressão seletiva:** "Maior que o GA, favorece exploração"

### Transição:
"Agora vamos ver como esses algoritmos performaram nos experimentos..."

---

## SLIDE 6: Configuração Experimental (1 minuto)

### Conteúdo do Slide:
- Parâmetros dos experimentos
- Número de execuções
- Metodologia estatística

### Pontos de Fala:
1. **Escala:** "240 execuções no total - 30 por função/algoritmo"
2. **Robustez:** "Análise estatística completa: média, desvio padrão, boxplots"
3. **Gerações:** "1000 gerações por execução"

### Transição:
"Vamos aos resultados principais..."

---

## SLIDE 7: Resultados Principais (3 minutos)

### Conteúdo do Slide:
- Tabela comparativa com médias e desvios padrão
- Destaque para o melhor algoritmo em cada função

### Pontos de Fala:
1. **Ackley:** "ES ligeiramente melhor, ambos performaram bem"
2. **Rastrigin:** "GA muito superior - 74% melhor que ES"
3. **Schwefel:** "ES melhor, mas com maior variabilidade"
4. **Rosenbrock:** "GA muito superior, mas com alta variabilidade"

### **USAR IMAGEM:** `boxplot_comparativo_geral.png`
- Mostrar o gráfico e explicar: "Os boxplots mostram a distribuição completa dos resultados"
- Destacar outliers e variabilidade

### Transição:
"Esses resultados nos levaram a investigar melhorias específicas..."

---

## SLIDE 8: Análise por Função - Ackley (1.5 minutos)

### Conteúdo do Slide:
- Resultados específicos para Ackley
- Comparação GA vs ES
- Interpretação

### Pontos de Fala:
1. **Resultados:** "ES: 8.24 ± 1.03 vs GA: 8.69 ± 0.97"
2. **Interpretação:** "Ambos performaram bem, ES tem pequena vantagem"
3. **Características:** "Função com muitos mínimos locais, mas ótimo global acessível"

### **USAR IMAGEM:** `boxplot_comparativo_ackley.png`
- Mostrar distribuição dos resultados
- Destacar similaridade entre os algoritmos

### Transição:
"Agora Rastrigin, onde vimos a maior diferença..."

---

## SLIDE 9: Análise por Função - Rastrigin (2 minutos)

### Conteúdo do Slide:
- Resultados específicos para Rastrigin
- Análise da diferença significativa
- Justificativa

### Pontos de Fala:
1. **Resultados:** "GA: 13.37 ± 4.02 vs ES: 51.79 ± 6.06"
2. **Diferença:** "GA 74% melhor que ES"
3. **Justificativa:** "Função com mínimos locais rasos - elitismo do GA ajuda"
4. **Robustez:** "GA também mais consistente (menor desvio padrão)"

### **USAR IMAGEM:** `boxplot_comparativo_rastrigin.png`
- Mostrar a clara separação entre GA e ES
- Destacar a menor variabilidade do GA

### Transição:
"Schwefel mostra um padrão diferente..."

---

## SLIDE 10: Análise por Função - Schwefel (1.5 minutos)

### Conteúdo do Slide:
- Resultados específicos para Schwefel
- Análise da variabilidade

### Pontos de Fala:
1. **Resultados:** "ES: 9098 ± 657 vs GA: 9580 ± 380"
2. **ES melhor:** "5% melhor em média"
3. **Variabilidade:** "ES mais variável, GA mais consistente"
4. **Interpretação:** "Função altamente multimodal - pressão seletiva da ES ajuda"

### **USAR IMAGEM:** `boxplot_comparativo_schwefel.png`
- Mostrar sobreposição dos boxes
- Destacar maior variabilidade da ES

### Transição:
"Rosenbrock apresenta um caso interessante..."

---

## SLIDE 11: Análise por Função - Rosenbrock (2 minutos)

### Conteúdo do Slide:
- Resultados específicos para Rosenbrock
- Análise da alta variabilidade do GA

### Pontos de Fala:
1. **Resultados:** "GA: 5.90 ± 17.42 vs ES: 64.90 ± 18.25"
2. **GA superior:** "91% melhor em média"
3. **Variabilidade:** "GA muito variável - algumas execuções excelentes, outras ruins"
4. **Interpretação:** "Vale estreito - GA pode encontrar soluções muito boas, mas é instável"

### **USAR IMAGEM:** `boxplot_comparativo_rosenbrock.png`
- Mostrar os outliers do GA
- Explicar que alguns resultados são muito bons, outros ruins

### Transição:
"Esses resultados nos motivaram a investigar melhorias..."

---

## SLIDE 12: Experimentos de Melhoria - Motivação (1.5 minutos)

### Conteúdo do Slide:
- Problemas identificados
- Oportunidades de melhoria
- Abordagem dos experimentos

### Pontos de Fala:
1. **GA Rosenbrock:** "Excelente média, mas alta variabilidade"
2. **ES Rastrigin:** "Desempenho muito inferior ao GA"
3. **Abordagem:** "Melhorias específicas baseadas nos resultados"
4. **Metodologia:** "Mantivemos 30 execuções para análise estatística"

### Transição:
"Vamos ver as melhorias implementadas no GA..."

---

## SLIDE 13: GA V2 - Melhorias Implementadas (2 minutos)

### Conteúdo do Slide:
- Lista das melhorias
- Justificativa de cada uma
- Parâmetros alterados

### Pontos de Fala:
1. **População:** "100 → 200 indivíduos - maior diversidade"
2. **Mutação:** "1/d → 2/d - mais exploração"
3. **Adaptativa:** "Ajuste dinâmico baseado no progresso"
4. **Elitismo:** "1 indivíduo → 20% da população"

### Transição:
"Vamos ver como essas melhorias impactaram os resultados..."

---

## SLIDE 14: GA V2 - Resultados (2 minutos)

### Conteúdo do Slide:
- Tabela comparativa GA Original vs GA V2
- Análise das melhorias

### Pontos de Fala:
1. **Ackley:** "38% de melhoria - mutação adaptativa funcionou"
2. **Rastrigin:** "Piorou 22% - overfitting para outros problemas"
3. **Schwefel:** "23% de melhoria - população maior ajudou"
4. **Rosenbrock:** "64% de melhoria, redução significativa da variabilidade"

### **USAR IMAGEM:** `ga_rosenbrock_boxplot.png` e `ga_rosenbrock_convergencia_media.png`
- Mostrar a variabilidade do GA original em Rosenbrock
- Explicar que o GA V2 melhorou significativamente a consistência

### Transição:
"Agora vamos ver as tentativas de melhorar a ES..."

---

## SLIDE 15: ES V2 e V3 - Abordagens (2 minutos)

### Conteúdo do Slide:
- ES V2: mudanças agressivas
- ES V3: ajustes conservadores
- Comparação das abordagens

### Pontos de Fala:
1. **ES V2:** "Mudanças agressivas - piorou 40%"
2. **Lição aprendida:** "Ajustes muito drásticos podem ser prejudiciais"
3. **ES V3:** "Ajustes incrementais - melhorou 41%"
4. **Princípio:** "Melhorias graduais são mais seguras"

### **USAR IMAGEM:** `comparacao_es_rastrigin.png`
- Mostrar a evolução das versões ES
- Destacar que V3 foi mais eficaz que V2

### Transição:
"Vamos analisar os insights estatísticos..."

---

## SLIDE 16: Análise Estatística - Boxplots (2 minutos)

### Conteúdo do Slide:
- Interpretação dos boxplots
- Insights sobre variabilidade
- Comparações visuais

### Pontos de Fala:
1. **Boxplots:** "Mostram distribuição completa dos resultados"
2. **Mediana vs Média:** "Tendência central vs valores atípicos"
3. **Outliers:** "Execuções excepcionalmente boas ou ruins"
4. **Sobreposição:** "Indica se diferenças são significativas"

### **USAR IMAGEM:** `boxplot_comparativo_geral.png`
- Explicar cada subplot
- Destacar padrões visuais importantes

### Transição:
"Com base em toda essa análise, chegamos a conclusões importantes..."

---

## SLIDE 17: Principais Descobertas (2 minutos)

### Conteúdo do Slide:
- 4 descobertas principais
- Implicações práticas

### Pontos de Fala:
1. **Não existe algoritmo universal:** "Cada problema requer abordagem específica"
2. **GA para mínimos locais rasos:** "Rastrigin, Rosenbrock"
3. **ES para problemas multimodais:** "Schwefel"
4. **Melhorias específicas:** "Mais eficazes que generalistas"

### Transição:
"Essas descobertas nos levam a recomendações práticas..."

---

## SLIDE 18: Recomendações Práticas (2 minutos)

### Conteúdo do Slide:
- Quando usar cada algoritmo
- Dicas para aplicações práticas
- Metodologia recomendada

### Pontos de Fala:
1. **Escolha do algoritmo:** "Baseada nas características do problema"
2. **Execuções múltiplas:** "Sempre necessárias para algoritmos estocásticos"
3. **Análise estatística:** "Fundamental para conclusões confiáveis"
4. **Testes práticos:** "Melhor forma de decidir"

### Transição:
"Vamos finalizar com as conclusões..."

---

## SLIDE 19: Conclusões (1.5 minutos)

### Conteúdo do Slide:
- Resumo das principais conclusões
- Impacto do estudo
- Trabalhos futuros

### Pontos de Fala:
1. **Contribuição:** "Análise estatística robusta de GA vs ES"
2. **Descobertas:** "Padrões claros de comportamento"
3. **Aplicabilidade:** "Orientações práticas para escolha de algoritmos"
4. **Futuro:** "Base para trabalhos mais avançados"

### Transição:
"Agora estou aberto a perguntas e discussão..."

---

## SLIDE 20: Perguntas e Discussão (2-3 minutos)

### Conteúdo do Slide:
- Agradecimentos
- Informações de contato
- Referências

### Pontos de Fala:
1. **Agradecimentos:** "Obrigado pela atenção"
2. **Disponibilidade:** "Código e dados disponíveis"
3. **Contato:** "Disponível para discussões adicionais"
4. **Convite:** "Perguntas e comentários são bem-vindos"

---

## Dicas para a Apresentação

### Preparação:
- **Praticar transições** entre slides
- **Preparar respostas** para perguntas comuns
- **Testar projeção** das imagens
- **Cronometrar** cada seção

### Durante a Apresentação:
- **Manter contato visual** com a audiência
- **Usar as imagens** para ilustrar pontos
- **Pausar** para perguntas intermediárias
- **Adaptar ritmo** baseado no interesse da audiência

### Imagens Disponíveis e Seu Uso:

#### Boxplots Comparativos (Principais):
1. **`boxplot_comparativo_geral.png`** - Slide 7 e 16 (visão geral completa)
2. **`boxplot_comparativo_rastrigin.png`** - Slide 9 (maior diferença entre GA e ES)
3. **`boxplot_comparativo_rosenbrock.png`** - Slide 11 (alta variabilidade do GA)
4. **`boxplot_comparativo_schwefel.png`** - Slide 10 (sobreposição entre algoritmos)
5. **`boxplot_comparativo_ackley.png`** - Slide 8 (similaridade entre algoritmos)

#### Boxplots Individuais (Suporte):
6. **`ga_rosenbrock_boxplot.png`** - Slide 14 (variabilidade do GA original)
7. **`es_rosenbrock_boxplot.png`** - Comparação com GA em Rosenbrock
8. **`ga_schwefel_boxplot.png`** - Análise detalhada do GA em Schwefel
9. **`es_schwefel_boxplot.png`** - Análise detalhada da ES em Schwefel
10. **`ga_rastrigin_boxplot.png`** - Análise detalhada do GA em Rastrigin
11. **`es_rastrigin_boxplot.png`** - Análise detalhada da ES em Rastrigin
12. **`ga_ackley_boxplot.png`** - Análise detalhada do GA em Ackley
13. **`es_ackley_boxplot.png`** - Análise detalhada da ES em Ackley

#### Gráficos de Convergência (Suporte):
14. **`ga_*_convergencia_media.png`** - Mostrar evolução temporal
15. **`es_*_convergencia_media.png`** - Comparar velocidade de convergência

#### Comparações Específicas:
16. **`comparacao_es_rastrigin.png`** - Slide 15 (evolução das versões ES)
17. **`comparacao_melhorias.png`** - Resumo das melhorias implementadas

### Perguntas Antecipadas:
- "Por que 30 execuções?"
- "Como escolher entre GA e ES?"
- "As melhorias são aplicáveis a outros problemas?"
- "Qual o custo computacional de cada algoritmo?"
- "Por que não testaram outras dimensões?"

### Notas Importantes:
- **Todas as imagens referenciadas existem** na pasta ``
- **Os boxplots comparativos** são os mais importantes para a apresentação
- **Os gráficos de convergência** podem ser usados como material de suporte
- **As comparações específicas** mostram a evolução dos experimentos
