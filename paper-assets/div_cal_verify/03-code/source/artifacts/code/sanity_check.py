# Sanity check: verify greedy selection picks diverse points across clusters, not concentrated at center.
# Usage: python sanity_check.py

import numpy as np
from diversity_selection import greedy_disf_selection

def main():
    np.random.seed(42)

    # 4 well-separated clusters in 2D
    clusters = [
        np.random.randn(25, 2) + np.array([5, 5]),
        np.random.randn(25, 2) + np.array([-5, 5]),
        np.random.randn(25, 2) + np.array([5, -5]),
        np.random.randn(25, 2) + np.array([-5, -5]),
    ]
    data = np.vstack(clusters)  # 100 points
    labels = np.repeat([0, 1, 2, 3], 25)

    # Select 20 points
    selected = greedy_disf_selection(data, budget=20)

    selected_labels = labels[selected]
    cluster_counts = {i: int(np.sum(selected_labels == i)) for i in range(4)}

    print("=== Sanity Check: Greedy Diversity Selection ===")
    print(f"Total points: {len(data)}, Selected: {len(selected)}")
    print(f"Cluster distribution of selected points: {cluster_counts}")

    # Check: all 4 clusters should be represented
    all_covered = all(c > 0 for c in cluster_counts.values())
    # Check: no cluster should dominate (max/min ratio < 3)
    counts = list(cluster_counts.values())
    balance_ok = max(counts) / max(min(counts), 1) < 3.0

    print(f"All clusters covered: {all_covered}")
    print(f"Balance ratio (max/min): {max(counts) / max(min(counts), 1):.1f} (want < 3.0)")

    # Compute centroid distance: selected points should be farther from global mean than random
    global_mean = data.mean(axis=0)
    selected_mean_dist = np.mean(np.linalg.norm(data[selected] - global_mean, axis=1))
    random_indices = np.random.choice(len(data), size=20, replace=False)
    random_mean_dist = np.mean(np.linalg.norm(data[random_indices] - global_mean, axis=1))

    print(f"Mean dist to centroid — selected: {selected_mean_dist:.2f}, random: {random_mean_dist:.2f}")
    spread_ok = selected_mean_dist >= random_mean_dist * 0.8

    if all_covered and balance_ok:
        print("\n✅ PASS: Selection covers all clusters with reasonable balance")
    else:
        print("\n❌ FAIL: Selection is concentrated — bug not fixed")
        if not all_covered:
            print(f"  Missing clusters: {[i for i, c in cluster_counts.items() if c == 0]}")

    return all_covered and balance_ok


if __name__ == "__main__":
    ok = main()
    exit(0 if ok else 1)
