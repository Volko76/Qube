import random

def generate_test_file(name, polygons):
    """
    Generate a test file with polygons in .poly
    """
    test_file = name + ".poly"
    with open(test_file, 'w') as f:
        to_write = ""
        for i, polygon in enumerate(polygons):
            for point in polygon:
                to_write += f"{i} {point[0]} {point[1]} \n"
        f.write(to_write)


def generate_random_polygons(n, m, min_coord, max_coord):
    """
    Generate n random polygons, each with m random points within the specified coordinate range.
    """
    polygons = []
    for _ in range(n):
        polygon = []
        for _ in range(m):
            x = random.randint(min_coord, max_coord)
            y = random.randint(min_coord, max_coord)
            point = [x, y]
            polygon.append(point)
        polygons.append(polygon)
    return polygons


# Test Case 1: Single polygon
polygons_1 = [[[0, 0], [0, 5], [5, 5], [5, 0]]]
generate_test_file("single_poly",polygons_1)

# Test Case 2: Multiple polygons
polygons_2 = [[[0, 0], [0, 5], [5, 5], [5, 0]], [[1, 1], [1, 4], [4, 4], [4, 1]]]
generate_test_file("mutliple_poly", polygons_2)

# Test Case 3: Empty polygon
polygons_3 = [[]]
generate_test_file("empty_poly",polygons_3)

# Test Case 4: Complex polygons
polygons_4 = [
    [[0, 0], [0, 5], [5, 5], [5, 0]],
    [[1, 1], [1, 4], [4, 4], [4, 1]],
    [[2, 2], [2, 3], [3, 3], [3, 2]]
]
generate_test_file("complex_poly",polygons_4)

# Test Case 5: Large number of polygons
polygons_5 = [[[i, i], [i, i + 1], [i + 1, i + 1], [i + 1, i]] for i in range(1000)]
generate_test_file("large_poly",polygons_5)


# Générer n polygones de m points de manière aléatoire
n = 4000
m = 50
min_coord = -100000000
max_coord = 100000000
polygons = generate_random_polygons(n, m, min_coord, max_coord)

generate_test_file("randomly_generated", polygons)