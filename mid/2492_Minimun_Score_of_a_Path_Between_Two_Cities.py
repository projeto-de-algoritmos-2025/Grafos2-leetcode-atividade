class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        #inicialização do grafo bidirecional
        grafo = defaultdict(list)
        for orig, dest, dist in roads:
            grafo[orig].append((dest, dist))
            grafo[dest].append((orig, dist))
        #nenhum nó do grafo estávisitado e menor caminho é o infinito
        visitados = [False] * (n + 1)
        menor = float("inf")
        #A função faz uma busca em profundidade anotando e atualizando o menor caminho encontrado ate então
        #ao fim  o valor do menor caminho é retornado
        def DFS(cidade: int ):
            
            visitados[cidade] = True
            nonlocal menor
            for vizinho, distancia in grafo[cidade]:
                if distancia < menor:
                    menor = distancia          
                if not visitados[vizinho]:
                    DFS(vizinho)
        #começa a busca pela cidade 1
        DFS(1)
        return menor