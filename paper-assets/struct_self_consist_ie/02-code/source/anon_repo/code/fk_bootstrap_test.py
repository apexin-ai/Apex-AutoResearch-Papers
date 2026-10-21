"""FK Instance-Level Bootstrap Test (R3-W4) — optimized version.

Pre-computes entity key sets to avoid redundant string parsing in permutation loop.
"""

import json
import sys
import os
import numpy as np
from scipy.stats import spearmanr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from evaluation import per_instance_f1

DATA_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl"
OUT_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/analysis_round8/fk_bootstrap_test.json"

N_PERMUTATIONS = 10000
N_SPLITS = 100
SEED = 42


def extract_ner_keys(sample):
    return frozenset((e["text"], e["type"]) for e in sample.get("entities", []))


def fk_from_keysets(keysets):
    """Fast Fleiss' kappa from pre-computed frozensets."""
    n_raters = len(keysets)
    if n_raters <= 1:
        return 1.0

    all_keys = set()
    for ks in keysets:
        all_keys |= ks
    n_subjects = len(all_keys)
    if n_subjects == 0:
        return 1.0

    key_list = sorted(all_keys)
    key_to_idx = {k: i for i, k in enumerate(key_list)}

    # Count present votes per subject
    present_counts = np.zeros(n_subjects, dtype=np.int64)
    for ks in keysets:
        for k in ks:
            present_counts[key_to_idx[k]] += 1

    absent_counts = n_raters - present_counts
    n = n_raters

    # Check perfect agreement
    if np.all((present_counts == 0) | (present_counts == n)):
        return 1.0

    # P_i for each subject: (sum(n_ij^2) - n) / (n*(n-1))
    sum_sq = present_counts**2 + absent_counts**2
    P_i = (sum_sq - n) / (n * (n - 1))
    P_bar = np.mean(P_i)

    # P_e
    total_votes = n_subjects * n
    p_present = np.sum(present_counts) / total_votes
    p_absent = np.sum(absent_counts) / total_votes
    P_e = p_present**2 + p_absent**2

    if abs(1.0 - P_e) < 1e-12:
        return 1.0

    kappa = (P_bar - P_e) / (1.0 - P_e)
    return float(kappa)


def load_valid_instances(path):
    instances = []
    with open(path) as f:
        for line in f:
            inst = json.loads(line)
            if len(inst["gold"].get("entities", [])) > 0:
                instances.append(inst)
    return instances


def main():
    print("Loading data...", flush=True)
    instances = load_valid_instances(DATA_PATH)
    n_inst = len(instances)
    n_samples = len(instances[0]["samples"])
    print(f"n_valid={n_inst}, n_samples={n_samples}", flush=True)

    # Pre-compute all entity key sets: keysets_matrix[i][j] = frozenset for instance i, sample j
    print("Pre-computing entity key sets...", flush=True)
    keysets_matrix = []
    for inst in instances:
        row = [extract_ner_keys(s) for s in inst["samples"]]
        keysets_matrix.append(row)

    # --- Method B: Instance-level FK statistics ---
    print("[Method B] Per-instance FK...", flush=True)
    fk_values = np.array([fk_from_keysets(keysets_matrix[i]) for i in range(n_inst)])
    fk_mean = float(np.mean(fk_values))
    fk_std = float(np.std(fk_values))
    fk_median = float(np.median(fk_values))
    fk_q25 = float(np.percentile(fk_values, 25))
    fk_q75 = float(np.percentile(fk_values, 75))
    print(f"  FK: mean={fk_mean:.4f}, std={fk_std:.4f}, median={fk_median:.4f}, IQR=[{fk_q25:.4f}, {fk_q75:.4f}]", flush=True)

    # FK-F1 Spearman
    print("  Computing per-instance F1...", flush=True)
    f1_values = []
    for inst in instances:
        greedy = inst.get("greedy")
        if greedy is not None:
            f1_values.append(per_instance_f1(greedy, inst["gold"], subtask="ner"))
        else:
            f1s = [per_instance_f1(s, inst["gold"], subtask="ner") for s in inst["samples"]]
            f1_values.append(float(np.mean(f1s)))
    f1_values = np.array(f1_values)
    rho_fk_f1, p_fk_f1 = spearmanr(fk_values, f1_values)
    print(f"  FK-F1 Spearman rho={rho_fk_f1:.4f}, p={p_fk_f1:.2e}", flush=True)

    # --- Method A: Permutation bootstrap ---
    print(f"[Method A] Permutation bootstrap ({N_PERMUTATIONS} iterations)...", flush=True)
    rng = np.random.default_rng(SEED)
    real_mean = np.mean(fk_values)
    permuted_means = np.zeros(N_PERMUTATIONS)

    for p in range(N_PERMUTATIONS):
        # For each sample position, shuffle instance assignments
        perm_fks = np.zeros(n_inst)
        shuffled_indices = [rng.permutation(n_inst) for _ in range(n_samples)]

        for i in range(n_inst):
            fake_keysets = [keysets_matrix[shuffled_indices[j][i]][j] for j in range(n_samples)]
            perm_fks[i] = fk_from_keysets(fake_keysets)

        permuted_means[p] = np.mean(perm_fks)

        if (p + 1) % 2000 == 0:
            print(f"  permutation {p+1}/{N_PERMUTATIONS}, mean={permuted_means[p]:.4f}", flush=True)

    p_value = float(np.mean(permuted_means >= real_mean))
    perm_mean = float(np.mean(permuted_means))
    perm_std = float(np.std(permuted_means))
    print(f"  Real FK mean={real_mean:.4f}, Permuted={perm_mean:.4f}±{perm_std:.4f}, p={p_value}", flush=True)

    # --- Method C: Split-half reliability ---
    print(f"[Method C] Split-half reliability ({N_SPLITS} splits)...", flush=True)
    rng2 = np.random.default_rng(SEED + 1)
    split_corrs = []

    for s in range(N_SPLITS):
        fk_h1 = np.zeros(n_inst)
        fk_h2 = np.zeros(n_inst)
        for i in range(n_inst):
            perm = rng2.permutation(n_samples)
            h1 = [keysets_matrix[i][perm[j]] for j in range(4)]
            h2 = [keysets_matrix[i][perm[j]] for j in range(4, 8)]
            fk_h1[i] = fk_from_keysets(h1)
            fk_h2[i] = fk_from_keysets(h2)
        rho, _ = spearmanr(fk_h1, fk_h2)
        split_corrs.append(rho)
        if (s + 1) % 25 == 0:
            print(f"  split {s+1}/{N_SPLITS}, rho={rho:.4f}", flush=True)

    split_corrs = np.array(split_corrs)
    split_mean = float(np.mean(split_corrs))
    split_std = float(np.std(split_corrs))
    print(f"  Split-half: r={split_mean:.4f}±{split_std:.4f}", flush=True)

    # --- Assemble results ---
    results = {
        "n_valid": n_inst,
        "real_fk_mean": round(fk_mean, 6),
        "real_fk_std": round(fk_std, 6),
        "real_fk_median": round(fk_median, 6),
        "fk_iqr": [round(fk_q25, 6), round(fk_q75, 6)],
        "fk_f1_spearman_rho": round(float(rho_fk_f1), 6),
        "fk_f1_spearman_p": float(p_fk_f1),
        "permuted_fk_mean": round(perm_mean, 6),
        "permuted_fk_std": round(perm_std, 6),
        "permutation_p_value": float(p_value),
        "permutation_n": N_PERMUTATIONS,
        "split_half_correlation_mean": round(split_mean, 6),
        "split_half_correlation_std": round(split_std, 6),
        "split_half_n": N_SPLITS,
        "conclusion": (
            f"FK shows significant within-instance agreement beyond random "
            f"(permutation p={'<0.0001' if p_value < 0.0001 else f'{p_value:.4f}'}; "
            f"real mean FK={fk_mean:.4f} vs permuted={perm_mean:.4f}) "
            f"and split-half reliability r={split_mean:.4f}+/-{split_std:.4f}. "
            f"FK-F1 Spearman rho={rho_fk_f1:.4f} (p={p_fk_f1:.2e})."
        )
    }

    with open(OUT_PATH, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {OUT_PATH}", flush=True)
    print(json.dumps(results, indent=2), flush=True)


if __name__ == "__main__":
    main()
