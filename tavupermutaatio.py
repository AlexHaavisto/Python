import itertools
#print (list(itertools.permutations(["Au","sa","Koi","ra"], 2)))
# tulos = (list(itertools.combinations(["gan","da","mel","zap","cra"], 3)))
# print(tulos)

tulos = (list(itertools.product(["Au","sa","Koi","ra"], ["nen","la","ras","muu"], ["si","la","ka","na"])))

for sana in tulos:
    print(sana[0] + sana[1] + sana[2])
