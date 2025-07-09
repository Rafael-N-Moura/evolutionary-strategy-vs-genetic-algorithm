import numpy as np
from benchmarks import ackley, rastrigin, schwefel, rosenbrock

class GeneticAlgorithm:
    def __init__(self, func, d=30, pop_size=100, generations=1000, bounds=(-5, 5)):
        self.func = func
        self.d = d
        self.pop_size = pop_size
        self.generations = generations
        self.bounds = bounds
        self.population = None
        self.fitness = None

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

    def mutate(self, offspring):
        mutation_rate = 1.0 / self.d
        low, high = self.bounds
        for i in range(self.pop_size):
            for j in range(self.d):
                if np.random.rand() < mutation_rate:
                    offspring[i, j] += np.random.normal(0, 0.1)
                    # Garantir que o gene fique dentro dos limites
                    offspring[i, j] = np.clip(offspring[i, j], low, high)
        return offspring

    def survivor_selection(self, offspring):
        # Elitismo: mantém o melhor da geração anterior
        elite_idx = np.argmin(self.fitness)
        elite = self.population[elite_idx].copy()
        # Avalia fitness dos filhos
        offspring_fitness = np.apply_along_axis(self.func, 1, offspring)
        # Seleciona os melhores filhos (pop_size - 1)
        best_offspring_idx = np.argsort(offspring_fitness)[:self.pop_size-1]
        self.population = np.vstack([elite, offspring[best_offspring_idx]])
        self.fitness = np.concatenate([[self.fitness[elite_idx]], offspring_fitness[best_offspring_idx]])

    def run(self):
        self.initialize_population()
        best_fitness_history = []
        for gen in range(self.generations):
            self.evaluate_fitness()
            best_fitness_history.append(np.min(self.fitness))
            parents = self.select_parents()
            offspring = self.crossover(parents)
            offspring = self.mutate(offspring)
            self.survivor_selection(offspring)
        # Avalia fitness final
        self.evaluate_fitness()
        best_idx = np.argmin(self.fitness)
        best_individual = self.population[best_idx]
        best_fitness = self.fitness[best_idx]
        return best_individual, best_fitness, best_fitness_history 