
import random
from collections import deque


# ---------------- Problem Data ----------------
# Each job has 3 operations: (machine_id, processing_time)

JOBS = [
    [(0,3),(1,2),(2,2)],
    [(1,2),(0,1),(2,4)],
    [(2,3),(0,2),(1,1)],
    [(0,4),(2,1),(1,3)],
    [(1,3),(2,2),(0,2)]
]

NUM_JOBS = len(JOBS)
NUM_MACHINES = 3
NUM_OPS = 3


def initial_schedule():
    # round-robin: all op0 then op1 then op2
    return [(j,o) for o in range(NUM_OPS) for j in range(NUM_JOBS)]


#  Feasibility Check 
def is_feasible(schedule):
    last = {j:-1 for j in range(NUM_JOBS)}

    for (job,op) in schedule:
        if op != last[job] + 1:
            return False
        last[job] = op

    return True


# Makespan Calculation 
def makespan(schedule):

    job_end = [0]*NUM_JOBS
    mach_end = [0]*NUM_MACHINES

    for (job,op) in schedule:

        machine,time = JOBS[job][op]

        start = max(job_end[job], mach_end[machine])
        end = start + time

        job_end[job] = end
        mach_end[machine] = end

    return max(mach_end)


# Neighbour Generation 
def neighbors(schedule, n=30):

    neigh = []
    length = len(schedule)

    for _ in range(n*3):

        i = random.randint(0,length-2)

        new = list(schedule)
        new[i],new[i+1] = new[i+1],new[i]

        if is_feasible(new):
            neigh.append((new,(i,i+1)))

        if len(neigh)>=n:
            break

    return neigh


#  Tabu Search 
def tabu_search(tenure=7, iterations=300):

    current = initial_schedule()
    best = list(current)

    best_mk = makespan(current)

    tabu = deque(maxlen=tenure)

    history = [best_mk]

    for step in range(iterations):

        neigh = neighbors(current)

        best_candidate = None
        best_candidate_mk = 1e9
        best_move = None

        for (s,move) in neigh:

            mk = makespan(s)

            # aspiration: allow tabu if better than best
            if move in tabu and mk >= best_mk:
                continue

            if mk < best_candidate_mk:
                best_candidate = s
                best_candidate_mk = mk
                best_move = move

        if best_candidate is None:
            continue

        current = best_candidate
        tabu.append(best_move)

        if best_candidate_mk < best_mk:
            best = list(current)
            best_mk = best_candidate_mk

        history.append(best_mk)

    return best,best_mk,history


# Random Search
def random_search(iterations=300):

    current = initial_schedule()
    best = makespan(current)

    history = [best]

    for _ in range(iterations):

        neigh = neighbors(current,10)

        if neigh:

            s,_ = random.choice(neigh)
            mk = makespan(s)

            if mk < best:
                best = mk
                current = s

        history.append(best)

    return best,history


def run():

    tenures = [3,7,15]

    results = {}

    for t in tenures:

        sched,mk,hist = tabu_search(t)

        results[t] = (sched,mk,hist)

        print("Tabu tenure",t,"best makespan =",mk)

    best_t = min(results,key=lambda x:results[x][1])
    best_sched,best_mk,_ = results[best_t]

    rand_mk,rand_hist = random_search()

    print("\nRandom search best =",rand_mk)
    print("Best tabu result =",best_mk,"with tenure",best_t)


if __name__ == "__main__":
    run()