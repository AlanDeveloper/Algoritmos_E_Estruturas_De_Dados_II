def getNumberOfVertices():
	while True:
		try:

			nVertices = int(input("Digite o número de vertices(max 20): "))

			if nVertices <= 20 and nVertices > 0: break
		except ValueError:
			print("Ooops! Digite um número\n")
	return nVertices

def readVertices(nVertices):
	vertices = []

	for i in range(0, nVertices):
		while True:
			try:
				vertices.append(int(input("Digite o valor do vertice " + str(len(vertices)) + " (número positivo): ")))

				if vertices[i] < 0: vertices.pop()
				else: break
			except ValueError:
				print("Ooops! Digite um número\n")
			
	return vertices

def readEdge(vertice, vertices):
	while True:

		response = input("Digite os vertices que se ligam ao vertice " + str(vertice) + ": ")
		edge = response.split(" ")

		if edge[0] == '': edge = []
		if verifyVertices(vertices, edge): return edge

def verifyVertices(vertices, edge):
	for e in edge:
		validate = False

		for v in vertices:
			if int(e) == v: 
				validate = True

		if validate == False: 
			print("Vertice não existe!")
			return False

	return True

def getWeight(vertices, edge, index, combinations):
	weight = []

	for e in edge:
		skip = False

		for c in combinations:
			if c[0] == (str(vertices[index]) + '-' + str(e)):
				weight.append(c[1])
				skip = True
		if skip: continue

		while True:
			try:
				w = int(input("Digite o peso da aresta " + str(vertices[index]) + '-' + str(e) + ": "))
				weight.append(w)
				combinations.append([str(e) + '-' + str(vertices[index]), w])
				break
			except ValueError:
				print("Ooops! Digite um número\n")
	return weight

def transformEdgeInBoolean(vertices, edge, weight):
	edgeBoolean = []

	for i in range(0, len(vertices)):
		append = False

		for j in range(0, len(edge)):
			if int(vertices[i]) == int(edge[j]): 
				index = j
				append = True

		if append: 
			edgeBoolean.append(weight[index])
		else:
			edgeBoolean.append(0)
		
	return edgeBoolean

def listGrafo(vertices, edges, weights):
	for i in range(0, len(edges)): 
		edges[i] = transformEdgeInBoolean(vertices, edges[i], weights[i])

	print("\nResultado final: \n")
	print(" |" + "|".join(str(v) for v in vertices))

	for i in range(0, len(vertices)):
		print(str(vertices[i]) + "|" + "|".join(str(e) for e in edges[i]))


print("-------------------- Bem Vindo --------------------")
print("Aqui você poderá transformar seus grafos em matriz!")
print("Alerta: Para ler a matriz, leia em sentido linha -> coluna")
print("Mais um recado: Você pode construir as matrizes com grafos direcionados ou não!\n")

nVertices = getNumberOfVertices()
vertices = readVertices(nVertices)

edges = []

print("\nAtenção! Digite os valores dos vertices em uma única linha além de separar por espaços")
print('Caso não haja ligação no vertice, apenas tecle "Enter"')
for v in vertices:
	edges.append(readEdge(v, vertices)) 

weights = []
combinations = []

print("\nAgora preencha os pesos das arestas")
for i in range(0, len(edges)):
	weights.append(getWeight(vertices, edges[i], i, combinations))

listGrafo(vertices, edges, weights)