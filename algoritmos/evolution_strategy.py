import numpy as np
from benchmarks import ackley, rastrigin, schwefel, rosenbrock

class EvolutionStrategy:
    def __init__(self, func, d=30, mu=30, lamb=200, generations=1000, bounds=(-5, 5)):
        self.func = func
        self.d = d
        self.mu = mu
        self.lamb = lamb
        self.generations = generations
        self.bounds = bounds
        self.population = None
        self.fitness = None

    def initialize_population(self):
        low, high = self.bounds
        self.population = np.random.uniform(low, high, (self.mu, self.d))
        assert self.population is not None, 'População não inicializada!'

    def evaluate_fitness(self):
        assert self.population is not None, 'População não inicializada!'
        self.fitness = np.apply_along_axis(self.func, 1, self.population)

    def recombination(self):
        assert self.population is not None, 'População não inicializada!'
        # Recombinacao intermediária: cada filho é a média de dois pais aleatórios
        offspring = np.empty((self.lamb, self.d))
        for i in range(self.lamb):
            p1, p2 = self.population[np.random.choice(self.mu, 2, replace=False)]
            offspring[i] = (p1 + p2) / 2
        return offspring

    def mutation(self, offspring):
        low, high = self.bounds
        for i in range(self.lamb):
            noise = np.random.normal(0, 0.1, self.d)
            offspring[i] += noise
            offspring[i] = np.clip(offspring[i], low, high)
        return offspring

    def survivor_selection(self, offspring):
        # Seleção dos mu melhores entre os lambda descendentes
        offspring_fitness = np.apply_along_axis(self.func, 1, offspring)
        best_idx = np.argsort(offspring_fitness)[:self.mu]
        self.population = offspring[best_idx]
        self.fitness = offspring_fitness[best_idx]

    def run(self):
        self.initialize_population()
        best_fitness_history = []
        for gen in range(self.generations):
            self.evaluate_fitness()
            best_fitness_history.append(np.min(self.fitness))
            offspring = self.recombination()
            offspring = self.mutation(offspring)
            self.survivor_selection(offspring)
        # Avalia fitness final
        self.evaluate_fitness()
        best_idx = np.argmin(self.fitness)
        best_individual = self.population[best_idx]
        best_fitness = self.fitness[best_idx]
        return best_individual, best_fitness, best_fitness_history 