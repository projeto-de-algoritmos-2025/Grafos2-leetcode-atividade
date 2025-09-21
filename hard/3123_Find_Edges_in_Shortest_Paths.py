import heapq
from collections import defaultdict

class Solution(object):
    def findAnswer(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[bool]
        """
        
# Dijkstra com heap para calcular distâncias mínimas do início e do fim
# O heap serve para processarmos sempre o nó com menor distância 
# Marca as arestas que participam de algum caminho mínimo entre 0 e n-1.

        
        # grafo da lista de adjacência 
        grafo = defaultdict(list)
        for origem, destino, peso in edges:
            grafo[origem].append((destino, peso))
            grafo[destino].append((origem, peso))

        # lisa de distâncias minimas do inicio
        def dijkstra(inicio):
            INF = float("inf")
            dist = [INF] * n
            dist[inicio] = 0
            fila = [(0, inicio)]  
            while fila:
                d_atual, no = heapq.heappop(fila)
                if d_atual > dist[no]:
                    continue
                for vizinho, peso in grafo[no]:
                    novo = d_atual + peso
                    if novo < dist[vizinho]:
                        dist[vizinho] = novo
                        heapq.heappush(fila, (novo, vizinho))
            return dist

        dist_inicio = dijkstra(0)
        dist_fim = dijkstra(n - 1)
        menor_caminho = dist_inicio[n - 1]

        # não entra no menor caminho se não tem caminho entre 0 e n-1
        if menor_caminho == float("inf"):
            return [False] * len(edges)

        resposta = []
        for origem, destino, peso in edges:
            if (dist_inicio[origem] + peso + dist_fim[destino] == menor_caminho or
                dist_inicio[destino] + peso + dist_fim[origem] == menor_caminho):
                resposta.append(True)
            else:
                resposta.append(False)

        return resposta