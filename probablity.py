<<<<<<< HEAD
from combinatoric import Combinatoric

class Probability:
    def __init__(self):
        pass


    def negativeProbability(probability):
        return 1 - probability

    def bernoulli(p, n, m):
=======
from combinatoric import Combinatoric

class Probability:
    def __init__(self):
        pass


    def negativeProbability(probability):
        return 1 - probability

    def bernoulli(p, n, m):
>>>>>>> 18294e9de50f832036c408dfa4b24bea2a46a6bf
        return Combinatoric.combinations_without_repeats(n, m) * p**m * Probability.negativeProbability(p)**(n-m)