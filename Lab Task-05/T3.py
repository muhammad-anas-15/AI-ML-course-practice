
import random
import math
import numpy as np


# Ackley function (global min = 0 at x=0,y=0)

def ackley(x, y):
    a = 20
    b = 0.2
    c = 2 * math.pi

    term1 = -a * math.exp(-b * math.sqrt(0.5 * (x*x + y*y)))
    term2 = -math.exp(0.5 * (math.cos(c*x) + math.cos(c*y)))

    return term1 + term2 + a + math.e

# Generate random neighbours

def neighbors(point, count=6, step=0.3):
    x, y = point
    pts = []

    for _ in range(count):
        nx = max(-5, min(5, x + random.uniform(-step, step)))
        ny = max(-5, min(5, y + random.uniform(-step, step)))
        pts.append((nx, ny))

    return pts


# Deterministic Local Beam Search

def beam_search(k=5, iterations=300):

    # random starting points
    beam = [(random.uniform(-5,5), random.uniform(-5,5)) for _ in range(k)]

    diversity = []
    snapshots = []

    for t in range(iterations):

        if t in [0, iterations//2, iterations-1]:
            snapshots.append(list(beam))

        candidates = list(beam)

        # generate neighbors of all beam states
        for p in beam:
            candidates.extend(neighbors(p))

        # select best k states
        candidates.sort(key=lambda p: ackley(p[0],p[1]))
        beam = candidates[:k]

        xs = [p[0] for p in beam]
        ys = [p[1] for p in beam]

        div = math.sqrt(np.std(xs)**2 + np.std(ys)**2)
        diversity.append(div)

    best = min(beam, key=lambda p: ackley(p[0],p[1]))

    return best, ackley(best[0],best[1]), snapshots, diversity


# Stochastic Beam Search

def stochastic_beam(k=5, iterations=300):

    beam = [(random.uniform(-5,5), random.uniform(-5,5)) for _ in range(k)]
    diversity = []

    for _ in range(iterations):

        candidates = list(beam)

        for p in beam:
            candidates.extend(neighbors(p))

        vals = [ackley(p[0],p[1]) for p in candidates]
        m = min(vals)

        weights = [math.exp(-(v-m)) for v in vals]

        # probabilistic selection
        beam = random.choices(candidates, weights=weights, k=k)

        xs = [p[0] for p in beam]
        ys = [p[1] for p in beam]

        div = math.sqrt(np.std(xs)**2 + np.std(ys)**2)
        diversity.append(div)

    best = min(beam, key=lambda p: ackley(p[0],p[1]))

    return best, ackley(best[0],best[1]), diversity


# Create heatmap grid

def create_grid():

    xs = np.linspace(-5,5,200)
    ys = np.linspace(-5,5,200)

    Z = [[ackley(x,y) for x in xs] for y in ys]

    return xs, ys, Z


def run():

    k_values = [3,5,10,20]

    results = {}
    diversity = {}

    print("Deterministic Beam Search Results")

    for k in k_values:

        pt,val,snaps,div = beam_search(k)

        results[k] = (pt,val,snaps)
        diversity[k] = div

        print("k =",k," best value =",val)

    print("\nStochastic Beam Search")

    for k in [5,10]:

        pt,val,div = stochastic_beam(k)

        print("k =",k," best value =",val)
        

if __name__ == "__main__":
    run()