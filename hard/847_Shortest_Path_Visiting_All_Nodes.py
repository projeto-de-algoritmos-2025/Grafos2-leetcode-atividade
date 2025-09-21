from collections import deque
from typing import List

class Solution:
    def shortestPathLength(self, grafo: List[List[int]]) -> int:
        #caso apenas 1 nó , o menor caminho é 0
        n = len(grafo)
        if n == 1:
            return 0
        #inicialização das variaveis
        todos_nos_bits = (1 << n) - 1  
        visitados_estado = set()       
        fila = deque()

       #BFS para cada nó, assim encontrando o menor caminho
        for inicio in range(n):
            nos_visitados_bits = 1 << inicio
            fila.append((inicio, nos_visitados_bits, 0))
            visitados_estado.add((inicio, nos_visitados_bits))
        #Processa a fila até encontrar o menor caminho que visite todos os nós
        while fila:
            no, nos_visitados_bits, distancia = fila.popleft()
        #Se todos os nós já foram visitados, retorna a distância percorrida
            if nos_visitados_bits == todos_nos_bits:
                return distancia
         #Atualiza a bitmask incluindo o vizinho visitado
            for vizinho in grafo[no]:
                novos_nos_visitados_bits = nos_visitados_bits | (1 << vizinho)
                estado = (vizinho, novos_nos_visitados_bits)
                 #Se esse estado ainda não foi visitado, adiciona à fila
                if estado not in visitados_estado:
                    visitados_estado.add(estado)
                    fila.append((vizinho, novos_nos_visitados_bits, distancia + 1))
