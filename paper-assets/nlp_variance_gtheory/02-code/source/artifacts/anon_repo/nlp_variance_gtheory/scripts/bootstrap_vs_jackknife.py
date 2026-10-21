import json
import numpy as np
import pandas as pd
from itertools import combinations
from pathlib import Path
import time

df = pd.read_csv("./results/analysis/llama_full.csv")
print(f"Loaded {len(df)} records, {df['item_id'].nunique()} items", flush=True)

facets = ["precision", "temperature", "prompt_template", "seed", "ordering", "item_id"]
N = len(df)
items = sorted(df["item_id"].unique())
n_items = len(items)

def compute_variance_pct(subset_df, metric="correct"):
    grand_mean = subset_df[metric].mean()
    SS_total = ((subset_df[metric] - grand_mean) ** 2).sum()
    if SS_total == 0:
        return {}
    N_sub = len(subset_df)
    components = {}
    for f in facets:
        if f not in subset_df.columns:
            continue
        n_f = subset_df[f].nunique()
        if n_f <= 1:
            continue
        means = subset_df.groupby(f)[metric].mean()
        n_per = N_sub // n_f
        ss = n_per * ((means - grand_mean) ** 2).sum()
        components[f] = ss
    for f1, f2 in combinations(facets, 2):
        if f1 not in subset_df.columns or f2 not in subset_df.columns:
            continue
        n1 = subset_df[f1].nunique()
        n2 = subset_df[f2].nunique()
        if n1 <= 1 or n2 <= 1:
            continue
        cell_means = subset_df.groupby([f1, f2])[metric].mean()
        n_per = N_sub // (n1 * n2)
        ss = 0
        f1_means = subset_df.groupby(f1)[metric].mean()
        f2_means = subset_df.groupby(f2)[metric].mean()
        for (l1, l2), cell_mean in cell_means.items():
            ss += n_per * (cell_mean - f1_means[l1] - f2_means[l2] + grand_mean) ** 2
        components[f"{f1}:{f2}"] = ss
    ss_explained = sum(components.values())
    components["residual"] = max(0, SS_total - ss_explained)
    total = sum(components.values())
    return {k: v/total * 100 for k, v in components.items()}

# === BOOTSTRAP (1000 resamples) ===
t0 = time.time()
print("Running bootstrap (1000 resamples)...", flush=True)
np.random.seed(42)
track_comps = ["item_id", "residual", "precision", "temperature",
               "prompt_template", "seed", "ordering",
               "precision:item_id", "temperature:item_id",
               "prompt_template:item_id", "seed:item_id"]
boot_results = {comp: [] for comp in track_comps}
n_boot = 1000
for b in range(n_boot):
    if b % 100 == 0:
        print(f"  Bootstrap {b}/{n_boot}", flush=True)
    sampled_items = np.random.choice(items, size=n_items, replace=True)
    frames = []
    for i, item in enumerate(sampled_items):
        sub = df[df["item_id"] == item].copy()
        sub["item_id"] = f"item_{i}"
        frames.append(sub)
    boot_df = pd.concat(frames, ignore_index=True)
    pct = compute_variance_pct(boot_df, "correct")
    for comp in boot_results:
        boot_results[comp].append(pct.get(comp, 0))

boot_ci = {}
for comp, vals in boot_results.items():
    vals = np.array(vals)
    boot_ci[comp] = {
        "mean": round(float(np.mean(vals)), 4),
        "ci_lower": round(float(np.percentile(vals, 2.5)), 4),
        "ci_upper": round(float(np.percentile(vals, 97.5)), 4),
        "ci_width": round(float(np.percentile(vals, 97.5) - np.percentile(vals, 2.5)), 4),
    }

t1 = time.time()
print(f"Bootstrap done in {t1-t0:.1f}s", flush=True)

print("\nBootstrap CIs (binary_correct):", flush=True)
for comp, ci in sorted(boot_ci.items(), key=lambda x: -x[1]["mean"]):
    if ci["mean"] >= 0.1:
        print(f"  {comp:30s}: {ci['mean']:7.2f}% [{ci['ci_lower']:.2f}, {ci['ci_upper']:.2f}] width={ci['ci_width']:.2f}", flush=True)

# === JACKKNIFE (delete-1) ===
print(f"\nRunning jackknife (delete-1, {n_items} iterations)...", flush=True)
jack_results = {comp: [] for comp in track_comps}
for i, item_to_remove in enumerate(items):
    if i % 20 == 0:
        print(f"  Jackknife {i}/{n_items}", flush=True)
    jack_df = df[df["item_id"] != item_to_remove]
    pct = compute_variance_pct(jack_df, "correct")
    for comp in jack_results:
        jack_results[comp].append(pct.get(comp, 0))

full_pct = compute_variance_pct(df, "correct")

jack_ci = {}
for comp, vals in jack_results.items():
    vals = np.array(vals)
    theta_hat = full_pct.get(comp, 0)
    n_j = len(vals)
    pseudo_vals = n_j * theta_hat - (n_j - 1) * vals
    jack_se = np.sqrt(np.var(pseudo_vals, ddof=1) / n_j)
    jack_ci[comp] = {
        "mean": round(float(theta_hat), 4),
        "ci_lower": round(float(theta_hat - 1.96 * jack_se), 4),
        "ci_upper": round(float(theta_hat + 1.96 * jack_se), 4),
        "ci_width": round(float(2 * 1.96 * jack_se), 4),
        "se": round(float(jack_se), 4),
    }

t2 = time.time()
print(f"Jackknife done in {t2-t1:.1f}s", flush=True)

print("\nJackknife CIs (binary_correct):", flush=True)
for comp, ci in sorted(jack_ci.items(), key=lambda x: -x[1]["mean"]):
    if ci["mean"] >= 0.1:
        print(f"  {comp:30s}: {ci['mean']:7.2f}% [{ci['ci_lower']:.2f}, {ci['ci_upper']:.2f}] width={ci['ci_width']:.2f}", flush=True)

# === COMPARISON ===
print("\n" + "="*70, flush=True)
print("COMPARISON: Bootstrap vs Jackknife CI widths", flush=True)
print("="*70, flush=True)
print(f"{'Component':<30s} {'Boot Width':>10s} {'Jack Width':>10s} {'Ratio':>8s}", flush=True)
print("-"*70, flush=True)
for comp in sorted(boot_ci.keys(), key=lambda c: -boot_ci[c]["mean"]):
    bw = boot_ci[comp]["ci_width"]
    jw = jack_ci[comp]["ci_width"]
    ratio = bw / jw if jw > 0 else float('inf')
    if boot_ci[comp]["mean"] >= 0.1:
        print(f"{comp:<30s} {bw:>10.2f} {jw:>10.2f} {ratio:>8.2f}", flush=True)

# Save
output = {
    "bootstrap": {"n_resamples": n_boot, "seed": 42, "components": boot_ci},
    "jackknife": {"n_items": n_items, "components": jack_ci},
}
Path("./results/analysis").mkdir(parents=True, exist_ok=True)
with open("./results/analysis/bootstrap_vs_jackknife.json", "w") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)
print(f"\nSaved results/analysis/bootstrap_vs_jackknife.json", flush=True)
print(f"Total time: {time.time()-t0:.1f}s", flush=True)
print("DONE", flush=True)
