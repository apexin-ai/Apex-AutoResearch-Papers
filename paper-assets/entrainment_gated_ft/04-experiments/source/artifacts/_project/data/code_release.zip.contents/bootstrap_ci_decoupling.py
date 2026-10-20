import json
import numpy as np
from itertools import combinations
import time

SEED = 42
N_BOOTSTRAP = 10000
N_EXAMPLES = 5153
ARCHS = ["GDN", "RetNet", "HGRN2"]
RATIOS = ["pure", "h24_1", "h12_1", "h6_1", "h3_1"]

BASE = "/root/entrainment_gated_ft/lm_eval_clean"
FILES = {
    ("GDN", "pure"): f"{BASE}/exp007/1.3b/GDN-pure/samples/lambada_openai.jsonl",
    ("GDN", "h24_1"): f"{BASE}/1.3b/GDN-h24-1-logsamples/samples/lambada_openai.jsonl",
    ("GDN", "h12_1"): f"{BASE}/exp007/1.3b/GDN-h12-1/samples/lambada_openai.jsonl",
    ("GDN", "h6_1"): f"{BASE}/1.3b/GDN-h6-1-logsamples/samples/lambada_openai.jsonl",
    ("GDN", "h3_1"): f"{BASE}/1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl",
    ("RetNet", "pure"): f"{BASE}/exp007/1.3b/RetNet-pure/samples/lambada_openai.jsonl",
    ("RetNet", "h24_1"): f"{BASE}/exp007/1.3b/RetNet-h24-1/samples/lambada_openai.jsonl",
    ("RetNet", "h12_1"): f"{BASE}/exp007/1.3b/RetNet-h12-1/samples/lambada_openai.jsonl",
    ("RetNet", "h6_1"): f"{BASE}/exp007/1.3b/RetNet-h6-1/samples/lambada_openai.jsonl",
    ("RetNet", "h3_1"): f"{BASE}/exp007/1.3b/RetNet-h3-1/samples/lambada_openai.jsonl",
    ("HGRN2", "pure"): f"{BASE}/exp007/1.3b/HGRN2-pure/samples/lambada_openai.jsonl",
    ("HGRN2", "h24_1"): f"{BASE}/exp007/1.3b/HGRN2-h24-1/samples/lambada_openai.jsonl",
    ("HGRN2", "h12_1"): f"{BASE}/exp007/1.3b/HGRN2-h12-1/samples/lambada_openai.jsonl",
    ("HGRN2", "h6_1"): f"{BASE}/exp007/1.3b/HGRN2-h6-1/samples/lambada_openai.jsonl",
    ("HGRN2", "h3_1"): f"{BASE}/exp007/1.3b/HGRN2-h3-1/samples/lambada_openai.jsonl",
}


def load_acc(path):
    acc = np.zeros(N_EXAMPLES, dtype=np.int8)
    with open(path) as f:
        for line in f:
            row = json.loads(line)
            acc[row["doc_id"]] = int(row["acc"])
    return acc


def main():
    t0 = time.time()
    rng = np.random.default_rng(SEED)

    print("Loading data...")
    acc_data = {}
    for arch in ARCHS:
        acc_data[arch] = {}
        for ratio in RATIOS:
            acc_data[arch][ratio] = load_acc(FILES[(arch, ratio)])
            print(f"  {arch}-{ratio}: acc={acc_data[arch][ratio].mean():.5f}")

    print("\n--- Point estimates ---")
    sigma_point = {}
    for ratio in RATIOS:
        accs = [acc_data[arch][ratio].mean() for arch in ARCHS]
        sigma_point[ratio] = float(np.std(accs, ddof=0))
        print(f"sigma({ratio}) = {sigma_point[ratio]:.5f}  accs={[round(a,5) for a in accs]}")

    j_helped_point = {}
    j_hurt_point = {}
    for ratio in RATIOS[1:]:
        helped = {}
        hurt = {}
        for arch in ARCHS:
            helped[arch] = (acc_data[arch][ratio] == 1) & (acc_data[arch]["pure"] == 0)
            hurt[arch] = (acc_data[arch][ratio] == 0) & (acc_data[arch]["pure"] == 1)
        j_h, j_r = [], []
        for a1, a2 in combinations(ARCHS, 2):
            ih = np.sum(helped[a1] & helped[a2])
            uh = np.sum(helped[a1] | helped[a2])
            j_h.append(ih / uh if uh > 0 else 0.0)
            ir = np.sum(hurt[a1] & hurt[a2])
            ur = np.sum(hurt[a1] | hurt[a2])
            j_r.append(ir / ur if ur > 0 else 0.0)
        j_helped_point[ratio] = float(np.mean(j_h))
        j_hurt_point[ratio] = float(np.mean(j_r))
        print(f"J_helped({ratio}) = {j_helped_point[ratio]:.4f}, J_hurt({ratio}) = {j_hurt_point[ratio]:.4f}")

    print(f"\nBootstrapping {N_BOOTSTRAP} resamples...")
    boot_indices = rng.integers(0, N_EXAMPLES, size=(N_BOOTSTRAP, N_EXAMPLES))

    # sigma bootstrap (vectorized)
    sigma_boot = {}
    for ratio in RATIOS:
        mat = np.stack([acc_data[arch][ratio] for arch in ARCHS])  # (3, 5153)
        boot_samples = mat[:, boot_indices]  # (3, 10000, 5153)
        boot_means = boot_samples.mean(axis=2)  # (3, 10000)
        sigma_boot[ratio] = boot_means.std(axis=0, ddof=0)  # (10000,)
    print("  sigma bootstrap done.")

    # Jaccard bootstrap (vectorized)
    j_helped_boot = {}
    j_hurt_boot = {}
    for ratio in RATIOS[1:]:
        helped_boot = {}
        hurt_boot = {}
        for arch in ARCHS:
            r_b = acc_data[arch][ratio][boot_indices]  # (10000, 5153)
            p_b = acc_data[arch]["pure"][boot_indices]  # (10000, 5153)
            helped_boot[arch] = (r_b == 1) & (p_b == 0)
            hurt_boot[arch] = (r_b == 0) & (p_b == 1)

        jh_pairs, jr_pairs = [], []
        for a1, a2 in combinations(ARCHS, 2):
            ih = (helped_boot[a1] & helped_boot[a2]).sum(axis=1).astype(np.float64)
            uh = (helped_boot[a1] | helped_boot[a2]).sum(axis=1).astype(np.float64)
            jh_pairs.append(np.where(uh > 0, ih / uh, 0.0))
            ir = (hurt_boot[a1] & hurt_boot[a2]).sum(axis=1).astype(np.float64)
            ur = (hurt_boot[a1] | hurt_boot[a2]).sum(axis=1).astype(np.float64)
            jr_pairs.append(np.where(ur > 0, ir / ur, 0.0))

        j_helped_boot[ratio] = np.mean(jh_pairs, axis=0)
        j_hurt_boot[ratio] = np.mean(jr_pairs, axis=0)
        print(f"  Jaccard bootstrap for {ratio} done.")

    # Compute CIs
    results = {"sigma": {}, "J_helped": {}, "J_hurt": {}}

    print("\n=== 95% Bootstrap CIs ===\n")
    print("sigma (architecture std):")
    for ratio in RATIOS:
        lo, hi = np.percentile(sigma_boot[ratio], [2.5, 97.5])
        results["sigma"][ratio] = {
            "point": round(sigma_point[ratio], 5),
            "ci_lower": round(float(lo), 5),
            "ci_upper": round(float(hi), 5),
        }
        print(f"  {ratio:8s}: {sigma_point[ratio]:.5f}  [{lo:.5f}, {hi:.5f}]")

    print("\nJ_helped (mean pairwise Jaccard):")
    for ratio in RATIOS[1:]:
        lo, hi = np.percentile(j_helped_boot[ratio], [2.5, 97.5])
        results["J_helped"][ratio] = {
            "point": round(j_helped_point[ratio], 4),
            "ci_lower": round(float(lo), 4),
            "ci_upper": round(float(hi), 4),
        }
        print(f"  {ratio:8s}: {j_helped_point[ratio]:.4f}  [{lo:.4f}, {hi:.4f}]")

    print("\nJ_hurt (mean pairwise Jaccard):")
    for ratio in RATIOS[1:]:
        lo, hi = np.percentile(j_hurt_boot[ratio], [2.5, 97.5])
        results["J_hurt"][ratio] = {
            "point": round(j_hurt_point[ratio], 4),
            "ci_lower": round(float(lo), 4),
            "ci_upper": round(float(hi), 4),
        }
        print(f"  {ratio:8s}: {j_hurt_point[ratio]:.4f}  [{lo:.4f}, {hi:.4f}]")

    # Key finding
    s_pure = results["sigma"]["pure"]
    s_h3 = results["sigma"]["h3_1"]
    sigma_nonoverlap = s_pure["ci_lower"] > s_h3["ci_upper"] or s_h3["ci_lower"] > s_pure["ci_upper"]

    j_ranges = [(results["J_helped"][r]["ci_lower"], results["J_helped"][r]["ci_upper"]) for r in RATIOS[1:]]
    j_all_overlap = all(
        not (j_ranges[i][0] > j_ranges[j][1] or j_ranges[j][0] > j_ranges[i][1])
        for i in range(len(j_ranges)) for j in range(i + 1, len(j_ranges))
    )

    if sigma_nonoverlap and j_all_overlap:
        finding = "sigma CIs non-overlapping between pure and h3-1 (true signal) vs J CIs overlapping across ratios (flat) -> supports decoupling"
    elif sigma_nonoverlap:
        finding = "sigma CIs non-overlapping between pure and h3-1; J CIs partially non-overlapping"
    else:
        finding = "sigma CIs overlapping between pure and h3-1 -- weaker decoupling evidence"

    results["key_finding"] = finding
    print(f"\nKey finding: {finding}")
    print(f"Elapsed: {time.time() - t0:.1f}s")

    with open("/root/entrainment_gated_ft/bootstrap_ci_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print("Saved to bootstrap_ci_results.json")


if __name__ == "__main__":
    main()
