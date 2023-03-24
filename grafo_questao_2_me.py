import matplotlib.pyplot as plt
import networkx as nx


# Instanciando o objeto Grafo
G2 = nx.Graph()

# Adicionando os Vértices
G2.add_nodes_from(["A1","A2","A3","A4","A5"])

# Adicionando as Arestas
G2.add_edge("A1","A2", impacto=15)
G2.add_edge("A1","A3", impacto=12)
G2.add_edge("A2","A3", impacto=6)
G2.add_edge("A2","A4", impacto=13)
G2.add_edge("A2","A5", impacto=5)
G2.add_edge("A3","A4", impacto=6)

# nx.minimum_spanning_tree é uma bilioteca do networkx que podemos usar parar encontrar a arvore minima do grafo, usando como pradrão o impacto que é o peso da aresta
# essa função é considerada a implementação do algoritomo de kruskal
T = nx.minimum_spanning_tree(G2, weight='impacto')

# Exibindo a árvore geradora mínima
nx.draw(T, with_labels=True)