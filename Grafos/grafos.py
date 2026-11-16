grafo = {
    "POA": ["SAO LEO", "CANOAS"],
    "SAO LEO": ["POA"],
    "CANOAS": ["POA"],
}

for vizinho in grafo['POA']:
    print(vizinho)

print(15 * "-")
