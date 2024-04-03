import matplotlib.pyplot as plt
import matplotlib.patches as patches
import colorsys

# Parse les données
data = [line.split() for line in open("randomly_generated.poly").read().split("\n") if line]
polygons = {}
points = {}
colors = {}
for line in data:
    poly_id, x, y = line
    poly_id = int(poly_id)
    x, y = float(x), float(y)
    point_id = f"{poly_id}.{len(polygons.get(poly_id, []))}"
    points[point_id] = (x, y)
    polygons.setdefault(poly_id, []).append(point_id)
    colors.setdefault(poly_id, None)

# Génère des couleurs uniques pour chaque polygone
for poly_id in colors:
    hue = poly_id / len(colors)
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    colors[poly_id] = color

# Crée la figure et l'axe
fig, ax = plt.subplots()

# Dessine les polygones et les points
for poly_id, point_ids in polygons.items():
    color = colors[poly_id]
    x, y = zip(*[points[point_id] for point_id in point_ids])
    poly = patches.Polygon([(x[i], y[i]) for i in range(len(x))], closed=True, facecolor=color, edgecolor=color, alpha=0.5)
    ax.add_patch(poly)
    ax.text(x[0], y[0]+ 0.5, f"Polygone {poly_id}", ha="center", va="center", color=color)
    for point_id in point_ids:
        x, y = points[point_id]
        ax.scatter(x, y, color=color)
        ax.text(x, y + 0.05, point_id, ha="center", va="bottom", color=color)  # Ajoute un décalage de 0.05 à la coordonnée y de l'étiquette

# Ajuste les limites et affiche la figure
plt.axis("scaled")
plt.show()
