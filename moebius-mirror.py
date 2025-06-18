import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, MultiPolygon
from shapely.ops import unary_union
import cmath

# Clip box in (xmin, ymin, xmax, ymax)
CLIP_BOX = (-10, 0, 10, 10)

# Helper: apply Möbius transformation
def mobius_apply(mat, z):
    a, b, c, d = mat
    return (a*z + b) / (c*z + d)

# Hyperbolic distance in upper half-plane model
def h_dist(z, w):
    u = (abs(z-w)**2)/(4*z.imag * w.imag)
    return np.arccosh(1 + 2*u)

# True hyperbolic bisector: region closer to z0 than z1 in hyperbolic distance
def bisector_half_plane(z0, z1, box=CLIP_BOX, nx=400, ny=400):
    xs = np.linspace(box[0], box[2], nx)
    ys = np.linspace(box[1] + 1e-6, box[3], ny)
    dx = (box[2] - box[0]) / nx
    dy = (box[3] - box[1]) / ny

    regions = []
    for i, x in enumerate(xs[:-1]):
        for j, y in enumerate(ys[:-1]):
            z = complex(x + dx/2, y + dy/2)
            if h_dist(z, z0) < h_dist(z, z1):
                square = [
                    (x, y), (x + dx, y),
                    (x + dx, y + dy), (x, y + dy)
                ]
                regions.append(Polygon(square))

    if not regions:
        return None
    return unary_union(regions)

# Parse generator input
def parse_matrix_input():
    print("Enter Möbius generators (a b c d), one per line. Empty line to finish:")
    generators = []
    while True:
        line = input(" > ")
        if not line.strip():
            break
        try:
            a, b, c, d = map(float, line.strip().split())
            if abs(a*d - b*c - 1) > 1e-6:
                print(" Not SL(2,R): det ≠ 1")
                continue
            generators.append((a, b, c, d))
        except:
            print(" Invalid format.")
    return generators

def invert_matrix(g):
    a, b, c, d = g
    return (d, -b, -c, a)

def main():
    print("Enter base point z0 (e.g. 0+1j):")
    z0 = complex(input(" > "))
    generators = parse_matrix_input()
    generators += [invert_matrix(g) for g in generators]
    region = Polygon([
        (CLIP_BOX[0], CLIP_BOX[1]),
        (CLIP_BOX[2], CLIP_BOX[1]),
        (CLIP_BOX[2], CLIP_BOX[3]),
        (CLIP_BOX[0], CLIP_BOX[3])
    ])

    for mat in generators:
        z1 = mobius_apply(mat, z0)
        half = bisector_half_plane(z0, z1)
        if half:
            region = region.intersection(half)

    plt.figure(figsize=(8, 6))

    if region.is_empty:
        print("Empty region: no valid Dirichlet domain")
    elif isinstance(region, Polygon):
        x, y = region.exterior.xy
        plt.fill(x, y, color='lightblue', alpha=0.6, edgecolor='blue')
    elif isinstance(region, MultiPolygon):
        for geom in region.geoms:
            x, y = geom.exterior.xy
            plt.fill(x, y, color='lightblue', alpha=0.6, edgecolor='blue')

    plt.plot(z0.real, z0.imag, 'ro', label="$z_0$")
    plt.title("Dirichlet Domain (Upper Half-Plane Model)")
    plt.xlabel("Re")
    plt.ylabel("Im")
    plt.grid(True)
    plt.legend()
    plt.axis("equal")
    plt.ylim(0, CLIP_BOX[3])
    plt.xlim(CLIP_BOX[0], CLIP_BOX[2])
    plt.show()

if __name__ == "__main__":
    main()
