#!/usr/bin/env python3
"""Patch libero_object_full_pipeline.py to add RSA analysis module."""

import sys

SCRIPT_PATH = "/root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py"

with open(SCRIPT_PATH, "r") as f:
    code = f.read()

# 1. RSA function to insert before main()
RSA_FUNC = '''

def run_rsa(reps, actions, task_labels, n_sample=20, bootstrap_n=1000, seed=42):
    log("Phase 5: RSA analysis")
    from scipy.spatial.distance import pdist
    from scipy.stats import spearmanr

    rng = np.random.RandomState(seed)
    n_tasks = int(task_labels.max()) + 1
    layers_to_check = [0, 4, 8, 12, 16, 20, 24, 28, 31]

    results = {
        "method": {
            "pairing": "within-task",
            "rep_distance": "cosine",
            "act_distance": "euclidean",
            "n_sample": n_sample,
            "bootstrap_n": bootstrap_n,
            "seed": seed,
            "n_tasks": n_tasks,
            "layers": layers_to_check,
        },
        "per_layer": {},
    }

    for l in layers_to_check:
        for pos in ("image_mean", "last_preaction"):
            task_rhos = []
            for ti in range(n_tasks):
                mask = task_labels == ti
                X = reps[l][pos][mask]
                A = actions[mask]
                n = len(X)
                if n < n_sample:
                    continue

                idx = rng.choice(n, size=n_sample, replace=False)
                Xs, As = X[idx], A[idx]

                rep_d = pdist(Xs.astype(np.float64), metric="cosine")
                act_d = pdist(As.astype(np.float64), metric="euclidean")

                if rep_d.std() < 1e-10 or act_d.std() < 1e-10:
                    continue
                rho, _ = spearmanr(rep_d, act_d)
                task_rhos.append(float(rho))

            if not task_rhos:
                continue
            arr = np.array(task_rhos)
            boot_means = [float(np.mean(rng.choice(arr, size=len(arr), replace=True)))
                          for _ in range(bootstrap_n)]
            boot_means.sort()
            ci_lo = boot_means[int(0.025 * bootstrap_n)]
            ci_hi = boot_means[int(0.975 * bootstrap_n)]

            key = f"L{l}_{pos}"
            results["per_layer"][key] = {
                "mean_rsa": round(float(arr.mean()), 6),
                "std": round(float(arr.std()), 6),
                "ci_95": [round(ci_lo, 6), round(ci_hi, 6)],
                "per_task": [round(v, 6) for v in task_rhos],
                "n_tasks": len(task_rhos),
            }
        if l % 8 == 0:
            im_key = f"L{l}_image_mean"
            lp_key = f"L{l}_last_preaction"
            im_v = results["per_layer"].get(im_key, {}).get("mean_rsa", "N/A")
            lp_v = results["per_layer"].get(lp_key, {}).get("mean_rsa", "N/A")
            log(f"  L{l}: img_mean RSA={im_v}  last_pre RSA={lp_v}")

    if results["per_layer"]:
        best_key = max(results["per_layer"], key=lambda k: results["per_layer"][k]["mean_rsa"])
        results["best"] = {"key": best_key, **results["per_layer"][best_key]}
        log(f"  Best RSA: {best_key} = {results['per_layer'][best_key]['mean_rsa']:.4f}")
    return results

'''

# 2. RSA call block to insert in main()
RSA_CALL = '''
    if not args.skip_rsa:
        t_rsa = time.time()
        rsa_res = run_rsa(reps, actions, labels)
        with open(os.path.join(RESULTS_DIR, "rsa_analysis.json"), "w") as f:
            json.dump(rsa_res, f, indent=2)
        log(f"Phase 5: {time.time()-t_rsa:.1f}s -> rsa_analysis.json")

'''

# --- Apply patches ---

# Insert RSA function before def main():
assert "\ndef main():" in code, "Cannot find 'def main():'"
code = code.replace("\ndef main():", RSA_FUNC + "\ndef main():")

# Insert RSA call before "del reps, actions, labels"
assert "    del reps, actions, labels" in code, "Cannot find 'del reps, actions, labels'"
code = code.replace("    del reps, actions, labels",
                     RSA_CALL + "    del reps, actions, labels")

# Rename counterfactual phase 5 -> 6
code = code.replace('log("Phase 5: counterfactual analysis")',
                     'log("Phase 6: counterfactual analysis")')
code = code.replace("Phase 5: {time.time()-t5:.1f}s -> counterfactual_combined.json",
                     "Phase 6: {time.time()-t5:.1f}s -> counterfactual_combined.json")

# Update docstring
code = code.replace(
    "  5. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d",
    "  5. RSA: representational similarity across conditions\n  6. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d"
)

# Add --skip-rsa flag
code = code.replace(
    '    p.add_argument("--skip-counterfactual", action="store_true")',
    '    p.add_argument("--skip-counterfactual", action="store_true")\n'
    '    p.add_argument("--skip-rsa", action="store_true")'
)

with open(SCRIPT_PATH, "w") as f:
    f.write(code)

# Verify syntax
import ast
ast.parse(code)
print("PATCH_OK")
