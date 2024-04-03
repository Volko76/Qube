import sys
from math import sqrt
import time

def read_polygons(file_path):
    """
    Function to read polygons from a .poly file.
    """
    polygons = []
    with open(file_path, 'r') as file:
        current_polygon = []
        for line in file:
            parts = line.split()
            if len(parts) == 3:
                polygon_index = int(parts[0])
                if polygon_index == len(polygons):
                    polygons.append(current_polygon)
                    current_polygon = []
                x, y = map(float, parts[1:])
                current_polygon.append([x, y])
        if current_polygon:
            polygons.append(current_polygon)
    return polygons

def ray_tracing_method(x, y, poly):
    """
    Ray tracing method to test point inclusion in a polygon.
    Adapted from the provided algorithm.
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

def winding_number_method(x, y, poly):
    """
    Check if a point is inside a polygon using the Winding Number algorithm.
    """
    wn = 0
    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        if y1 <= y:
            if y2 > y and (x2 - x1) * (y - y1) - (x - x1) * (y2 - y1) > 0:
                wn += 1
        else:
            if y2 <= y and (x2 - x1) * (y - y1) - (x - x1) * (y2 - y1) < 0:
                wn -= 1
    return wn != 0

def point_line_distance(point, start, end):
    """
    Calculate the distance between a point and a line segment.
    """
    if start == end:
        return sqrt((point[0] - start[0]) ** 2 + (point[1] - start[1]) ** 2) # Trivial case: Euclidean distance

    segment_dx = end[0] - start[0]
    segment_dy = end[1] - start[1]

    segment_length = sqrt(segment_dx ** 2 + segment_dy ** 2)

    dot_product = ((point[0] - start[0]) * segment_dx + (point[1] - start[1]) * segment_dy) / segment_length ** 2

    if dot_product < 0:
        return sqrt((point[0] - start[0]) ** 2 + (point[1] - start[1]) ** 2)
    elif dot_product > 1:
        return sqrt((point[0] - end[0]) ** 2 + (point[1] - end[1]) ** 2)
    else:
        closest_point_x = start[0] + dot_product * segment_dx
        closest_point_y = start[1] + dot_product * segment_dy
        return sqrt((point[0] - closest_point_x) ** 2 + (point[1] - closest_point_y) ** 2)

def peucker_reduce(polygon, tolerance):
    """
    Reduce the number of points in a polygon using the Peucker algorithm.
    """
    dmax = 0
    index = 0
    for i in range(1, len(polygon) - 1):
        d = point_line_distance(polygon[i], polygon[0], polygon[-1])
        if d > dmax:
            index = i
            dmax = d

    if dmax >= tolerance:
        peucker1 = peucker_reduce(polygon[:index+1], tolerance)
        peucker2 = peucker_reduce(polygon[index:], tolerance)
        reduced_polygon = peucker1[:-1] + peucker2
    else:
        reduced_polygon = [polygon[0], polygon[-1]]

    return reduced_polygon

def cross_product_method(x, y, poly):
    """
    Check if a point is inside a polygon using the cross product algorithm.
    """
    n = len(poly)
    inside = False

    for i in range(n):
        p1x, p1y = poly[i]
        p2x, p2y = poly[(i + 1) % n]

        # Trivial Case | Check if the point is on one of the polygon's edges
        if (x, y) == (p1x, p1y) or (x, y) == (p2x, p2y):
            return True

        # Check if the point is inside the polygon using the cross product
        if (p1y > y) != (p2y > y) and x < p1x + (p2x - p1x) * (y - p1y) / (p2y - p1y):
            inside = not inside

    return inside

def trouve_inclusions(polygons):
    """
    Find the inclusions of polygons within each other.
    """
    num_polygons = len(polygons)
    inclusions = [-1] * num_polygons  # Initialize to -1 means no polygon is included in another

    for i, poly1 in enumerate(polygons):
        for j, poly2 in enumerate(polygons):
            if i != j:  # Don't test a polygon against itself
                # Select a point from the first polygon to test inclusion in the second polygon
                test_point = poly1[0]
                x, y = test_point[0], test_point[1]
                if cross_product_method(x, y, poly2):  # TO EDIT TO TEST DIFFERENT METHODS If the point is inside the second polygon
                    inclusions[i] = j  # The first polygon is included in the second polygon
                    break  # Move to the next polygon

    return inclusions

def main():
    """
    charge chaque fichier .poly donne
    trouve les inclusions
    affiche l'arbre en format texte
    """
    for fichier in sys.argv[1:]:
        polygons = read_polygons(fichier)
        polygons = polygons[1:] # To remove the "ghost" first polygone
        reduced_polygons = [peucker_reduce(poly, 0.01) for poly in polygons] # Optimize polygons to improve performances in highly detailled ones (MIGHT LOOSE PRECISION). 0.01 is the tolerance
        inclusions = trouve_inclusions(reduced_polygons)
        print(inclusions)

def benchmark(polygons):
    """
    Benchmark the speed of each method on the input polygons.
    """
    methods = {
        "Ray Tracing Method": ray_tracing_method,
        "Winding Number Method": winding_number_method,
        "Cross Product Method": cross_product_method
    }

    results = {}

    for method_name, method_func in methods.items():
        start_time = time.time()
        for poly in polygons:
            for point in poly:
                x, y = point
                method_func(x, y, poly)
        end_time = time.time()
        execution_time = end_time - start_time
        results[method_name] = execution_time

    return results

def run_benchmark():
    for fichier in sys.argv[1:]:
        polygons = read_polygons(fichier)
        polygons = polygons[1:]  # To remove the "ghost" first polygon
        reduced_polygons = [peucker_reduce(poly, 90000000) for poly in polygons]  # Optimize polygons to improve performances in highly detailed ones (MIGHT LOSE PRECISION). 0.01 is the tolerance
        
        # Benchmark the methods
        benchmark_results = benchmark(reduced_polygons)
        
        # Print the benchmark results
        print("Benchmark results for file:", fichier)
        for method_name, execution_time in benchmark_results.items():
            print(f"{method_name}: {execution_time} seconds")

if __name__ == "__main__":
    main()
    #run_benchmark()
