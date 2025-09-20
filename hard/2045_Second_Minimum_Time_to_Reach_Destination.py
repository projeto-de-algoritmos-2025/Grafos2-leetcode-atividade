import heapq

class Solution(object):
    def secondMinimum(self, n, edges, time, change):
        """
        :type n: int
        :type edges: List[List[int]]
        :type time: int
        :type change: int
        :rtype: int
        """

# O heap  é usado para escolher sempre o próximo nó com o menor tempo acumulado.
# Assim garantimos que os caminhos são explorados em ordem crescente de tempo,
# o que é essencial para registrar corretamente o menor e o segundo menor tempo de chegada ao destino.

        grafo = {}
        for origem, destino in edges:
            if origem not in grafo:
                grafo[origem] = []
            if destino not in grafo:
                grafo[destino] = []
            grafo[origem].append(destino)
            grafo[destino].append(origem)

        # guarda os dois tempos distintos de chegada
        distancias = [[] for _ in range(n + 1)]

        # HEAP
        fila = [(0, 1)] 
        while fila:
            tempo_atual, no = heapq.heappop(fila)  # remove o menor tempo da fila

            if distancias[no] and tempo_atual == distancias[no][-1]:
                continue

            if len(distancias[no]) == 2:
                continue

            
            distancias[no].append(tempo_atual)

            # Se chegar em dois tempos diferentes, retorna o segundo tempo registrado
            if no == n and len(distancias[no]) == 2:
                return distancias[no][1]

            for vizinho in grafo[no]:
                novo_tempo = tempo_atual

                ciclo = novo_tempo // change
                if ciclo % 2 == 1:  # se o semaforo estiver vermelho, espera o proximo verde
                    novo_tempo = (ciclo + 1) * change
                    
                novo_tempo += time

                # Só enfileirar o vizinho se ele ainda pode registrar tempos
                if len(distancias[vizinho]) < 2 and (not distancias[vizinho] or novo_tempo != distancias[vizinho][-1]):
                    heapq.heappush(fila, (novo_tempo, vizinho))


