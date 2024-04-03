import sys

def read_polygons(file_path):
    """
    Fonction pour lire les polygones à partir d'un fichier .poly.
    """
    polygons = []
    with open(file_path, 'r') as file:
        current_polygon = []
        for line in file:
            parts = line.split()
            if len(parts) == 3:
                polygon_index = int(parts[0])
                if polygon_index == len(polygons):
                    if current_polygon:
                        polygons.append(current_polygon)
                    current_polygon = []
                x, y = map(float, parts[1:])
                current_polygon.append([x, y])
        if current_polygon:
            polygons.append(current_polygon)
    return polygons

def ray_tracing_method(x, y, poly):
    """
    Méthode de traçage de rayons pour tester l'inclusion d'un point dans un polygone.
    Adaptée à partir de l'algorithme fourni.
    """
    n = len(poly)
    inside = False

    p1x, p1y = poly[0]
    for i in range(n + 1):
        p2x, p2y = poly[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xints = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xints:
                        inside = not inside
        p1x, p1y = p2x, p2y

    return inside

def trouve_inclusions(polygons):
    """
    Trouve les inclusions des polygones les uns dans les autres.
    """
    num_polygons = len(polygons)
    inclusions = [-1] * num_polygons  # Initialiser à -1 signifie qu'aucun polygone n'est inclus dans un autre

    for i, poly1 in enumerate(polygons):
        for j, poly2 in enumerate(polygons):
            if i != j:  # Ne pas tester un polygone contre lui-même
                # Sélectionner un point du premier polygone pour tester l'inclusion dans le deuxième polygone
                print(poly1)
                test_point = poly1[0]
                x, y = test_point[0], test_point[1]
                if ray_tracing_method(x, y, poly2):  # Si le point est à l'intérieur du deuxième polygone
                    inclusions[i] = j  # Le premier polygone est inclus dans le deuxième polygone
                    break  # Passer au polygone suivant

    return inclusions

def main():
    """
    charge chaque fichier .poly donne
    trouve les inclusions
    affiche l'arbre en format texte
    """
    for fichier in sys.argv[1:]:
        polygons = read_polygons(fichier)
        inclusions = trouve_inclusions(polygons)
        print(inclusions)

if __name__ == "__main__":
    main()
