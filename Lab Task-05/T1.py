
import random

N = 8


# Generate random board
def random_state():
    return [random.randint(0, N-1) for _ in range(N)]


# Cost function: number of attacking queen pairs
def attacking_pairs(state):
    attacks = 0
    for i in range(N):
        for j in range(i+1, N):
            if state[i] == state[j] or abs(state[i]-state[j]) == abs(i-j):
                attacks += 1
    return attacks

# a) Steepest-Ascent Hill Climbing

def steepest_ascent():
    state = random_state()
    cost = attacking_pairs(state)
    steps = 0

    while True:
        best_state = state
        best_cost = cost

        for r in range(N):
            for c in range(N):
                if c == state[r]:
                    continue

                new = state.copy()
                new[r] = c
                new_cost = attacking_pairs(new)

                if new_cost < best_cost:
                    best_state = new
                    best_cost = new_cost

        if best_cost >= cost:
            break

        state = best_state
        cost = best_cost
        steps += 1

    return state, cost, steps, cost == 0


# b) Random-Restart Hill Climbing

def random_restart(max_restarts=1000):

    for r in range(1, max_restarts+1):

        state, cost, steps, success = steepest_ascent()

        if success:
            return state, cost, r, steps

    return state, cost, max_restarts, steps


# c) First-Choice Hill Climbing

def first_choice(max_attempts=500):

    state = random_state()
    cost = attacking_pairs(state)
    steps = 0

    while True:

        improved = False

        for _ in range(max_attempts):

            r = random.randint(0, N-1)
            c = random.randint(0, N-1)

            if c == state[r]:
                continue

            new = state.copy()
            new[r] = c

            new_cost = attacking_pairs(new)

            if new_cost < cost:
                state = new
                cost = new_cost
                steps += 1
                improved = True
                break

        if not improved:
            break

    return state, cost, steps, cost == 0


# Run Experiments

def run():

    steepest_success = 0
    first_success = 0
    restarts_list = []

    # run experiment 100 times
    for i in range(100):

        # Steepest Ascent
        state, cost, steps, success = steepest_ascent()
        if success:
            steepest_success += 1

        # First Choice
        state, cost, steps, success = first_choice()
        if success:
            first_success += 1

        # Random Restart
        state, cost, restarts, steps = random_restart()
        restarts_list.append(restarts)

    # calculate average restarts
    avg_restart = sum(restarts_list) / len(restarts_list)

    print("Results after 100 runs")
    print("Steepest success Ascent:", steepest_success)
    print("First-choice success:", first_success)
    print("Average random restarts:", avg_restart)


run()