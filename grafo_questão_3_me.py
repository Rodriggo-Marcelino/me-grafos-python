import networkx as nx

# Instanciando o objeto Grafo
G4 = nx.Graph()

# Adicionando os Vértices
G4.add_nodes_from(["A","B","C","D","E","F","G","H","I","J"])

# Adicionando as Arestas
G4.add_edge("A","B")
G4.add_edge("A","D")
G4.add_edge("A","H")
G4.add_edge("B","C")
G4.add_edge("C","D")
G4.add_edge("D","E")
G4.add_edge("E","F")
G4.add_edge("E","G")
G4.add_edge("F","G")
G4.add_edge("G","H")
G4.add_edge("H","I")
G4.add_edge("H","J")
G4.add_edge("I","J")

def adiciona_vertices_q4(grafo, vertices):
    for v in vertices:
        if v == 'X1':
            grafo.add_edge("X1","A")
            grafo.add_edge("X1","D")

        if v == 'X2':
            grafo.add_edge("X2","D")
            grafo.add_edge("X2","E")

        if v == 'X3':
            grafo.add_edge("X3","E")
            grafo.add_edge("X3","G")

        if v == 'X4':
            grafo.add_edge("X4","H")
            grafo.add_edge("X4","J")

# Adicionando os novos vértices
adiciona_vertices_q4(G4,['X1','X2','X3','X4'])

# Verificando se o grafo é euleriano
if nx.is_eulerian(G4):
    # Encontrando o caminho euleriano
    caminho = list(nx.eulerian_circuit(G4))
    # Transformando o caminho em uma lista de vértices
    vertices = [c[0] for c in caminho]
    vertices.append(caminho[0][0])
    # Imprimindo o caminho
    print("Caminho encontrado:")
    print(" -> ".join(vertices))
else:
    print("O grafo não é euleriano.")