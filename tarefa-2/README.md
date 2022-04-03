# Trabalho de Grafos

Para utilizar o programa é necessário ter o python 3 instalado, após cole o comando no terminal:

````
> py dijkstra.py
```


## Casos de teste

````
	N° vertices: 3
	Nome dos vertice 0: 1
	Nome dos vertice 1: 2
	Nome dos vertice 2: 3
	Aresta(s): 
		1 -> 2 3
		2 -> 3
		3 ->
	Peso(s):
		1-2 -> 3
		1-3 -> 7
		2-3 -> 2
	Vertice inicial: 1
	Vertice final: 3
	Saída: 1 -> 2 -> 3 Peso: 5
```

````
	N° vertices: 4
	Nome dos vertice 0: 1 
	Nome dos vertice 1: 2
	Nome dos vertice 2: 3
	Nome dos vertice 3: 4
	Aresta(s): 
		1 -> 4
		2 ->
		3 ->
		4 -> 2 3
	Peso(s):
		1-4 -> 2
		4-2 -> 3
		4-3 -> 4
	Vertice inicial: 1
	Vertice final: 3
	Saída: 1 -> 4 -> 3 Peso: 6
```

````
	N° vertices: 3
	Nome dos vertice 0: 1
	Nome dos vertice 1: 2
	Nome dos vertice 2: 3
	Aresta(s): 
		1 -> 2 3
		2 -> 3
		3 -> 
	Peso(s):
		1-2 -> 2
		1-3 -> 1
		2-3 -> 5
	Vertice inicial: 3
	Vertice final: 1
	Saída: Nenhum caminho disponível
```