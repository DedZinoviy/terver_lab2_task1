def negativeProbability(probability):
    return 1 - probability

def electicScheme4var(elementProbabilityList):
    return elementProbabilityList[0] + negativeProbability(elementProbabilityList[0]) *((elementProbabilityList[1] + negativeProbability(elementProbabilityList[1]) * elementProbabilityList[2] * elementProbabilityList[3]) * (elementProbabilityList[4] + negativeProbability(elementProbabilityList[4]) * elementProbabilityList[5]))

float_list = []
for element in input().split():
    float_list.append(float(element))
print(electicScheme4var(float_list))
