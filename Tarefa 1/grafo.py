def getNumberOfVertices():
	while True:
		nVertices = input("Digite o número de vertices(max 20): ")
		nVertices = int(nVertices)

		if nVertices <= 20 and nVertices > 0: break
	return nVertices

def readVertices(nVertices):
	vertices = []

	for i in range(0, nVertices):
		while True:
			vertices.append(int(input("Digite o valor do vertice(número positivo): ")))

			if vertices[i] < 0: 
				vertices.pop()
			else:
				break
	return vertices

def readEdge(vertice, vertices):
	while True:

		response = input("Digite os vertices que se ligam ao vertice " + str(vertice) + ": ")
		edge = response.split(" ")

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

def transformEdgeInBoolean(vertices, edge):
	edgeBoolean = []

	for e in edge:
		for i in range(0, len(vertices)):
			if int(vertices[i]) == int(e):
				edgeBoolean.append(1)
			else:
				edgeBoolean.append(0)
		
	return edgeBoolean

def listGrafo(vertices, edges):
	for i in range(0, len(edges)): 
		edges[i] = transformEdgeInBoolean(vertices, edges[i])

	print(" |" + "|".join(str(v) for v in vertices))

	for i in range(0, len(vertices)):
		print(str(vertices[i]) + "|" + "|".join(str(e) for e in edges[i]))


nVertices = getNumberOfVertices()
vertices = readVertices(nVertices)

edges = []
for v in vertices:
	print("\nPara introduzir as arestas do vertice " + str(v) + ", digite tudo em uma única linha e separado por espaços")
	edges.append(readEdge(v, vertices)) 

listGrafo(vertices, edges)