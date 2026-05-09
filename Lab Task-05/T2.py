import random
import math

# Create random cities

NUM_CITIES = 20
CITIES = [(random.uniform(0,100), random.uniform(0,100)) for _ in range(NUM_CITIES)]


# Tour distance

def tour_distance(tour):
    dist = 0
    n = len(tour)

    for i in range(n):
        x1,y1 = CITIES[tour[i]]
        x2,y2 = CITIES[tour[(i+1)%n]]
        dist += math.hypot(x1-x2, y1-y2)

    return dist

# 2-opt swap neighbour

def two_opt(tour):

    i = random.randint(0, len(tour)-2)
    j = random.randint(i+1, len(tour)-1)

    new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]

    return new_tour


# Simulated Annealing

def simulated_annealing(schedule="geometric",
                        T0=1000,
                        alpha=0.995,
                        max_iter=50000):

    # random starting tour
    current = list(range(NUM_CITIES))
    random.shuffle(current)

    curr_dist = tour_distance(current)

    best = list(current)
    best_dist = curr_dist

    history = [curr_dist]

    for t in range(1, max_iter+1):

        # temperature update
        if schedule == "geometric":
            T = T0 * (alpha**t)

        elif schedule == "linear":
            T = max(0.001, T0 - alpha*t)

        elif schedule == "logarithmic":
            T = T0 / math.log(t+2)

        if T < 0.001:
            break

        neighbour = two_opt(current)
        nb_dist = tour_distance(neighbour)

        delta = nb_dist - curr_dist

        # acceptance rule
        if delta < 0 or random.random() < math.exp(-delta/T):
            current = neighbour
            curr_dist = nb_dist

        if curr_dist < best_dist:
            best = list(current)
            best_dist = curr_dist

        if t % 500 == 0:
            history.append(best_dist)

    return best, best_dist, history


# Draw a tour

def draw_tour(ax, tour, title):

    xs = [CITIES[i][0] for i in tour] + [CITIES[tour[0]][0]]
    ys = [CITIES[i][1] for i in tour] + [CITIES[tour[0]][1]]

    ax.plot(xs, ys)
    ax.scatter([c[0] for c in CITIES], [c[1] for c in CITIES])

    ax.set_title(title)

# Run experiment

def run():

    schedules = {
        "geometric": {"T0":1000, "alpha":0.995},
        "linear": {"T0":1000, "alpha":0.02},
        "logarithmic": {"T0":300, "alpha":0.995}
    }

    results = {}
    histories = {}

    # initial random tour
    init = list(range(NUM_CITIES))
    random.shuffle(init)
    init_dist = tour_distance(init)

    print("Initial distance:", init_dist)

    # run SA for each schedule
    for name,params in schedules.items():

        best,dist,hist = simulated_annealing(
            schedule=name,
            T0=params["T0"],
            alpha=params["alpha"]
        )

        results[name] = (best,dist)
        histories[name] = hist

        print(name,"best distance:",dist)

    # best schedule
    best_sched = min(results, key=lambda x: results[x][1])
    print("Best schedule:", best_sched)


if __name__ == "__main__":
    run()