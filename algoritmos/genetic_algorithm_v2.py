import numpy as np
from benchmarks import ackley, rastrigin, schwefel, rosenbrock

class GeneticAlgorithmV2:
    def __init__(self, func, d=30, pop_size=200, generations=10000, bounds=(-5, 5)):
        self.func = func
        self.d = d
        self.pop_size = pop_size
        self.generations = generations
        self.bounds = bounds
        self.population = None
        self.fitness = None
        self.best_fitness_history = []
        self.mutation_rate = 2.0 / d  # Taxa de mutação aumentada

    def initialize_population(self):
        low, high = self.bounds
        self.population = np.random.uniform(low, high, (self.pop_size, self.d))

    def evaluate_fitness(self):
        self.fitness = np.apply_along_axis(self.func, 1, self.population)

    def select_parents(self):
        # Seleção por torneio binário
        parents_idx = []
        for _ in range(self.pop_size):
            i, j = np.random.randint(0, self.pop_size, 2)
            if self.fitness[i] < self.fitness[j]:
                parents_idx.append(i)
            else:
                parents_idx.append(j)
        return np.array(parents_idx)

    def crossover(self, parents):
        # Crossover aritmético
        offspring = np.empty_like(self.population)
        np.random.shuffle(parents)
        for i in range(0, self.pop_size, 2):
            p1 = self.population[parents[i]]
            p2 = self.population[parents[i+1]]
            alpha = np.random.rand()
            offspring[i] = alpha * p1 + (1 - alpha) * p2
            offspring[i+1] = alpha * p2 + (1 - alpha) * p1
        return offspring

    def adaptive_mutation(self, offspring):
        low, high = self.bounds
        
        # Mutação adaptativa baseada no progresso
        if len(self.best_fitness_history) > 10:
            recent_improvement = self.best_fitness_history[-1] - self.best_fitness_history[-10]
            if recent_improvement < 0.01:  # Pouca melhoria recente
                mutation_rate = self.mutation_rate * 1.5  # Aumentar mutação
            else:
                mutation_rate = self.mutation_rate
        else:
            mutation_rate = self.mutation_rate
        
        for i in range(self.pop_size):
            for j in range(self.d):
                if np.random.rand() < mutation_rate:
                    # Mutação gaussiana com desvio padrão adaptativo
                    std_dev = 0.1
                    if len(self.best_fitness_history) > 5:
                        if self.best_fitness_history[-1] - self.best_fitness_history[-5] < 0.01:
                            std_dev = 0.2  # Aumentar desvio padrão se estagnado
                    
                    offspring[i, j] += np.random.normal(0, std_dev)
                    offspring[i, j] = np.clip(offspring[i, j], low, high)
        return offspring

    def survivor_selection(self, offspring):
        # Elitismo: manter os 20% melhores da geração anterior
        elite_size = int(0.2 * self.pop_size)
        elite_idx = np.argsort(self.fitness)[:elite_size]
        elite = self.population[elite_idx].copy()
        elite_fitness = self.fitness[elite_idx]
        
        # Avaliar fitness dos filhos
        offspring_fitness = np.apply_along_axis(self.func, 1, offspring)
        
        # Selecionar os melhores filhos para preencher o restante
        best_offspring_idx = np.argsort(offspring_fitness)[:self.pop_size-elite_size]
        
        self.population = np.vstack([elite, offspring[best_offspring_idx]])
        self.fitness = np.concatenate([elite_fitness, offspring_fitness[best_offspring_idx]])

    def run(self):
        self.initialize_population()
        for gen in range(self.generations):
            self.evaluate_fitness()
            current_best = np.min(self.fitness)
            self.best_fitness_history.append(current_best)
            
            parents = self.select_parents()
            offspring = self.crossover(parents)
            offspring = self.adaptive_mutation(offspring)
            self.survivor_selection(offspring)
        
        # Avalia fitness final
        self.evaluate_fitness()
        best_idx = np.argmin(self.fitness)
        best_individual = self.population[best_idx]
        best_fitness = self.fitness[best_idx]
        return best_individual, best_fitness, self.best_fitness_history 