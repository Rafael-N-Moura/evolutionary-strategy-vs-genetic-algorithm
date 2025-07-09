import numpy as np

def ackley(x, a=20, b=0.2, c=2*np.pi):
    d = len(x)
    sum1 = np.sum(x**2)
    sum2 = np.sum(np.cos(c * x))
    term1 = -a * np.exp(-b * np.sqrt(sum1 / d))
    term2 = -np.exp(sum2 / d)
    return term1 + term2 + a + np.exp(1)

def rastrigin(x):
    d = len(x)
    return 10 * d + np.sum(x**2 - 10 * np.cos(2 * np.pi * x))

def schwefel(x):
    d = len(x)
    return 418.9829 * d - np.sum(x * np.sin(np.sqrt(np.abs(x))))

def rosenbrock(x):
    return np.sum(100.0 * (x[1:] - x[:-1]**2)**2 + (x[:-1] - 1)**2)

# Exemplo de uso:
if __name__ == "__main__":
    d = 30
    x = np.zeros(d)
    print("Ackley:", ackley(x))
    print("Rastrigin:", rastrigin(x))
    print("Schwefel:", schwefel(x))
    print("Rosenbrock:", rosenbrock(x)) 