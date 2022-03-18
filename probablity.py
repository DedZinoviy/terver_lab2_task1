from combinatoric import Combinatoric
from main import negativeProbability

class Probability:
    def __init__(self):
        pass


    def negativeProbability(probability):
        return 1 - probability

    def bernoulli(p, n, m):
        return Combinatoric.combinations_without_repeats(n, m) * p**m * negativeProbability(p)**(n-m)