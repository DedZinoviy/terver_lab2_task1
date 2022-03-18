from probablity import Probability

def electicScheme3var(elementProbabilityList):
    return elementProbabilityList[0] + Probability.negativeProbability(elementProbabilityList[0]) *((elementProbabilityList[1] + Probability.negativeProbability(elementProbabilityList[1]) * elementProbabilityList[2] * elementProbabilityList[3]) * (elementProbabilityList[4] + Probability.negativeProbability(elementProbabilityList[4]) * elementProbabilityList[5]))

float_list = []
for element in input().split():
    float_list.append(float(element))
print(electicScheme3var(float_list))
