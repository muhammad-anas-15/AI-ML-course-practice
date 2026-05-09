import random

# probabilities
outcomes = [0,1,2,3,4,6,'W']
prob = [30,25,15,5,12,8,5]

# function to simulate innings
def play_innings(team):

    print(f"\n--- {team} Batting ---")

 # runs & balls faced by each player as there are 11 players.
    batsman_runs = [0]*11
    batsman_balls = [0]*11

 # set initial game variables , striker -> current batsman , next_batsman
    striker = 0
    next_batsman = 1

    total_runs = 0
    wickets = 0
    ball = 0

    runs_per_over = []
    fall_wickets = []

    over_runs = 0

    while ball < 120 and wickets < 10:

        result = random.choices(outcomes, weights=prob)[0]

        batsman_balls[striker] += 1

        if result == 'W':
            wickets += 1
            fall_wickets.append((total_runs, wickets))
            print(f"Ball {ball+1}: Wicket!")

            striker = next_batsman
            next_batsman += 1

        else:
            total_runs += result
            batsman_runs[striker] += result
            over_runs += result
            print(f"Ball {ball+1}: {result} run(s)")

        ball += 1

    # End of Over --> every 6 balls = 1 over
        if ball % 6 == 0: 
            runs_per_over.append(over_runs)
          # reset to 0  
            over_runs = 0

# Overs played: 60 balls = 10 overs
    overs = ball/6

    if overs > 0:
        run_rate = total_runs / overs

    else:
        run_rate = 0

# function retturn a dictionary
    return {
        "runs": total_runs,
        "wickets": wickets,
        "overs": overs,
        "run_rate": run_rate,
        "batsman_runs": batsman_runs,
        "batsman_balls": batsman_balls,
        "runs_per_over": runs_per_over,
        "fall": fall_wickets
    }


# function to print scorecard
def print_scorecard(team, data):

    print(f"\n===== {team} Scorecard =====")

    print("\nBatsman  Runs  Balls")

    for i in range(11):
        print(f"Batsman {i+1},  {data['batsman_runs'][i]},  {data['batsman_balls'][i]}")

    print("\nRuns per Over:")

    i = 1
    for r in data["runs_per_over"]:
        print("Over", i, ":", r)
        i = i + 1

    print("\nFall of Wickets:")
    
    for item in data["fall"]:
        r = item[0]
        w = item[1]
        print(w, "-", r)

    print(f"\nTotal: {data['runs']}/{data['wickets']}")
    print(f"Overs: {data['overs']:.1f}")
    print(f"Run Rate: {data['run_rate']:.2f}")


# simulate match
team1 = "Peshawar Zalmi"
team2 = "Islamabad United"

innings1 = play_innings(team1)
innings2 = play_innings(team2)

# print scorecards
print_scorecard(team1, innings1)
print_scorecard(team2, innings2)

# result
print("\n===== Match Result =====")

if innings1["runs"] > innings2["runs"]:
    margin = innings1["runs"] - innings2["runs"]
    print(team1, "won by", margin, "runs")

elif innings2["runs"] > innings1["runs"]:
    margin = innings2["runs"] - innings1["runs"]
    print(team2, "won by", margin, "runs")

else:
    print("Match Tied!")