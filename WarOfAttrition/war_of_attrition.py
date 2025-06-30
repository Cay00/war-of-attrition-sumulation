import random
import matplotlib.pyplot as plt
import seaborn as sns


def war_of_attrition():
    v = 100

    t1 = random.randint(0, 100)
    t2 = random.randint(0, 100)

    # print(f"Player 1 chooses to wait {t1} units")
    # print(f"Player 2 chooses to wait {t2} units")

    if t1 < t2:
        p1 = -t1
        p2 = v - t2
    elif t1 > t2:
        p1 = v - t1
        p2 = -t2
    else:
        p1 = p2 = v / 2 - t1

    return p1, p2, t1, t2


def plot_payoff_difference_distribution(num_samples):
    results = [war_of_attrition() for _ in range(num_samples)]
    diffs = [p1 - p2 for p1, p2, _, _ in results]

    plt.hist(diffs, bins=30)
    plt.title("Distribution of payoff differences (P1 - P2)")
    plt.xlabel("Payoff difference")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()


def plot_payoffs_scatter(num_samples):
    results = [war_of_attrition() for _ in range(num_samples)]
    p1s = [r[0] for r in results]
    p2s = [r[1] for r in results]

    plt.figure(figsize=(8, 6))
    plt.scatter(p1s, p2s, alpha=0.6, color="red", edgecolors="k")
    plt.title("Player 1 vs Player 2 Payoffs")
    plt.xlabel("Player 1 payoff")
    plt.ylabel("Player 2 payoff")
    plt.axhline(0, color='gray', linewidth=0.8)
    plt.axvline(0, color='gray', linewidth=0.8)
    plt.grid(True)
    plt.show()


def plot_cumulative_combined(num_games):
    cumulative_p1 = []
    cumulative_p2 = []
    cumulative_diff = []

    total_p1 = 0
    total_p2 = 0

    for _ in range(num_games):
        p1, p2, _, _ = war_of_attrition()
        total_p1 += p1
        total_p2 += p2
        cumulative_p1.append(total_p1)
        cumulative_p2.append(total_p2)
        cumulative_diff.append(total_p1 - total_p2)

    plt.figure(figsize=(12, 6))
    plt.plot(cumulative_p1, label="Player 1 Payoff", color="blue")
    plt.plot(cumulative_p2, label="Player 2 Payoff", color="red")
    plt.plot(cumulative_diff, label="P1 - P2 Advantage", color="purple", linestyle="--")

    plt.title("Cumulative Payoffs and Advantage")
    plt.xlabel("Game Number")
    plt.ylabel("Cumulative Value")
    plt.axhline(0, color="gray", linestyle="--", linewidth=0.8)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_wait_times_kde(num_samples):
    results = [war_of_attrition() for _ in range(num_samples)]
    t1s = [t1 for _, _, t1, _ in results]
    t2s = [t2 for _, _, _, t2 in results]

    plt.figure(figsize=(7, 6))
    sns.kdeplot(x=t1s, y=t2s, cmap="viridis", fill=True, bw_adjust=0.5)
    plt.xlabel("Player 1 wait time (t1)")
    plt.ylabel("Player 2 wait time (t2)")
    plt.title("KDE Heatmap of Wait Times")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def simulate_game(num_games):
    total_p1 = 0
    total_p2 = 0

    for _ in range(num_games):
        p1, p2, _, _ = war_of_attrition()
        total_p1 += p1
        total_p2 += p2

    print(f"After {num_games} games:")
    print(f"  Player 1 total payoff: {total_p1}")
    print(f"  Player 2 total payoff: {total_p2}")

    plot_payoff_difference_distribution(num_games)
    plot_payoffs_scatter(num_games)
    plot_cumulative_combined(num_games)
    plot_wait_times_kde(num_games)


if __name__ == "__main__":
    simulate_game(1000)
