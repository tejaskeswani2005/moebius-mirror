# moebius-mirror

**moebius-mirror** is a Python tool for visualizing Dirichlet domains of Fuchsian groups acting on the hyperbolic upper half-plane. It computes and renders the region of points closer (in hyperbolic distance) to a fixed base point than to any of its images under Möbius transformations from a user-defined group.

## 📐 What it Does
- Accepts Möbius transformations in SL(2, ℝ) as input.
- Computes true hyperbolic bisectors (via distance comparison).
- Approximates the Dirichlet domain using alpha shapes.
- Supports non-convex, curved, and even disconnected domains.
- Visualizes the domain using matplotlib.

## 📦 Requirements
- Python 3.7+
- numpy
- matplotlib
- shapely
- alphashape
- scipy

Install all dependencies:
```bash
pip install numpy matplotlib shapely alphashape scipy
```

## ▶️ Usage
Run the script from terminal:
```bash
python dirichlet_scope.py
```

You will be prompted to enter:
- A base point (e.g., `0+1j`)
- One or more Möbius transformations as 4 real numbers: `a b c d`
  - Ensure they satisfy `ad - bc = 1`
  - Press Enter on a blank line to finish input

### Example Input
```
Enter base point z0 (e.g. 0+1j):
 > 0+1j
Enter Möbius generators (a b c d), one per line. Empty line to finish:
 > 1 1 0 1
 > 1 0 -1 1
 >
```

## 📚 Background
A Dirichlet domain for a group $\Gamma \subset SL(2, \mathbb{R})$ centered at $z_0 \in \mathbb{H}$ is defined as:

$
D(z_0) = \{ z \in \mathbb{H} : d(z, z_0) < d(z, \gamma z_0), \forall \gamma \in \Gamma \setminus \{1\} \}
$

This script constructs these domains numerically by discretizing the upper half-plane, evaluating hyperbolic distances, and intersecting the corresponding half-planes.

## 🧪 Tips
- Try standard modular group generators: `1 1 0 1` and `1 0 -1 1`
- To observe disconnected domains, try `100 1 0 0.01` and its inverse

## 📸 Example Output
_(Include screenshots or animated gifs here)_

## 🙋 Contributing
Pull requests and suggestions are welcome!

---
Created for exploration, learning, and fun with hyperbolic geometry ✨

