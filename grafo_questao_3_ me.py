import networkx as nx
from collections import deque

# função recebe um conjunto de parentes e verifica quais dos parentes estão diretamente conectados.
# a função inicia criando uma lista vazia, é adicionado na lista se o parente ( vertice ), estiver presente no grafo. 

def encontra_parentes_conectados(usuario, parentes, grafo):
    parentes_conectados = []
    distancia_para_parente = float('inf')
    parente_mais_proximo = None
    
    fila = deque([(usuario, 0)])
    visitados = set([usuario])
    
# while sendo usado para o algoritimo de busca em largura
    while fila:
        no, distancia = fila.popleft()
        
        if distancia < distancia_para_parente and no in parentes:
            parente_mais_proximo = no
            distancia_para_parente = distancia
        
        for vizinho in grafo[no]:
            if vizinho not in visitados:
                fila.append((vizinho, distancia+1))
                visitados.add(vizinho)
                
                if vizinho in parentes:
                    parentes_conectados.append(vizinho)
    
    return parentes_conectados, parente_mais_proximo, distancia_para_parente


# Instanciando o objeto Grafo
G3 = nx.Graph()

# Adicionando os Vértices
G3.add_nodes_from(["P1","P2","P3","P4","P5","P6","P7","P8","P9","P10","P11","P12","P13","P14","P15","P16","P17","P18"])

# Adicionando as Arestas
G3.add_edge("P1","P2")
G3.add_edge("P1","P4")
G3.add_edge("P2","P4")
G3.add_edge("P3","P4")
G3.add_edge("P3","P5")
G3.add_edge("P3","P6")
G3.add_edge("P4","P6")
G3.add_edge("P5","P6")
G3.add_edge("P6","P12")
G3.add_edge("P7","P8")
G3.add_edge("P7","P9")
G3.add_edge("P8","P9")
G3.add_edge("P10","P11")
G3.add_edge("P10","P12")
G3.add_edge("P11","P12")
G3.add_edge("P11","P13")
G3.add_edge("P12","P14")
G3.add_edge("P13","P14")
G3.add_edge("P15","P16")
G3.add_edge("P15","P17")
G3.add_edge("P16","P17")
G3.add_edge("P17","P18")

parentes = ["P3", "P5", "P7", "P10", "P11", "P12", "P14", "P16"]
usuario = "P1"

parentes_conectados, parente_mais_proximo, distancia_para_parente = encontra_parentes_conectados(usuario, parentes, G3)

print(f"Parentes conectados: {parentes_conectados}")
print(f"Parente mais próximo: {parente_mais_proximo}")
print(f"Distância para o parente mais próximo: {distancia_para_parente}")
