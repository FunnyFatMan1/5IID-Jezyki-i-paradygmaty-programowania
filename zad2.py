from collections import deque

def sciezka_bfs(graf, start, koniec):
    kolejka = deque([[start]])
    odwiedzone = set()

    while kolejka:
        sciezka = kolejka.popleft()
        biezacy_wierzcholek = sciezka[-1]

        if biezacy_wierzcholek == koniec:
            return sciezka

        if biezacy_wierzcholek not in odwiedzone:
            for sasiad in graf.get(biezacy_wierzcholek, []):
                kolejka.append(sciezka + [sasiad])
            odwiedzone.add(biezacy_wierzcholek)

    return None

graf = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

print(sciezka_bfs(graf, 'A', 'F'))
