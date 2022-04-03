from itertools import combinations
import grafo

print("\nAnalizando grafo ...")

def startVertice(vertices):
	while True:
		start = input("Digite o vertice inicial: ")

		if grafo.verifyVertices(vertices, [start]): break
	return start

def endVertice(vertices):
	while True:
		end = input("Digite o vertice final: ")

		if grafo.verifyVertices(vertices, [end]): break
	return end

def getCombinations(currentVertice, combinations):
	c = []

	for i in range(0, len(combinations)):
		if combinations[i][0].find("-" + str(currentVertice)) != -1:
			c.append(combinations[i])
	return c

def getValue(vertice, analyzed):
	for i in range(0, len(analyzed)):
		if vertice == analyzed[i][1]: return analyzed[i][0]
	return 0

def analyzedGraph(vertices, combinations, start, end):
	analyze = []

	currentVertice = start
	currentValue = 0
	analyze.append([currentValue, currentVertice, None])
	for k in range(0, len(vertices)):

		currentVertice = vertices[k]
		currentValue = getValue(vertices[k], analyze)
		if start != vertices[k]:

			c = getCombinations(currentVertice, combinations)

			for i in range(0, len(c)):
				save = -1

				for j in range(0, len(analyze)):
					if c[i][0][0] == analyze[j][1]: save = j

				if save == -1:
					analyze.append([currentValue + c[i][1], c[i][0][0], currentVertice])
				elif analyze[save][0] > c[i][1] :
					analyze[save] = [currentValue + c[i][1], c[i][0][0], currentVertice]

	return analyze

def deleteRoad(analyze, vertice):
	for i in range(0, len(analyze)):
		if int(analyze[i][1]) == vertice:
			analyze = analyze[:i] + analyze[i+1 :]
			break
	return analyze

def readAnalyze(analyze, end):
	road = []

	currentVertice = None
	lastVertice = None
	value = 0
	while True:

		for i in range(0, len(analyze)):
			if currentVertice == analyze[i][2]:
				currentVertice = int(analyze[i][1])
				value += analyze[i][0]
				road.append(currentVertice)

		if currentVertice == int(end): break
		if len(analyze) == 1: 
			currentVertice = None
			break
		if currentVertice == lastVertice:
			analyze = deleteRoad(analyze, currentVertice)
			road = []

			currentVertice = None
			lastVertice = None
			value = 0
		lastVertice = currentVertice

	print("\n---------------------Caminho final---------------------")
	if currentVertice == None:
		print("Nenhum caminho disponível.")
		return
	print(" -> ".join(str(r) for r in road))
	print("Peso: " + str(value))


start = startVertice(grafo.vertices)
end = endVertice(grafo.vertices)

analyze = analyzedGraph(grafo.vertices, grafo.combinations, start, end)
readAnalyze(analyze, end)