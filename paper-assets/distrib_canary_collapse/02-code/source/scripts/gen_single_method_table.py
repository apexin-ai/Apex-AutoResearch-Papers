"""Generate Single-Method Error Consequence table from 5method_leadlag.json files."""
import json
import os
import glob

BASE = "/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep"

files = sorted(glob.glob(os.path.join(BASE, "a*_s*/analysis/5method_leadlag.json")))

METHOD_KEYS = ["naive_xcorr", "diff_xcorr", "threshold_onset", "perm_granger", "ty_granger"]
METHOD_LABELS = {
    "naive_xcorr": "Naive XCorr",
    "diff_xcorr": "Diff XCorr (FDR)",
    "threshold_onset": "Threshold Onset",
    "perm_granger": "Perm Granger (FDR)",
    "ty_granger": "TY Granger",
}

def get_sig(method_data, method_key):
    if method_key in ("diff_xcorr", "perm_granger"):
        return method_data.get("significant_fdr", method_data.get("significant", False))
    return method_data.get("significant", False)

results = {}
data_sources = {}

for f in files:
    with open(f) as fh:
        d = json.load(fh)
    if "meta" in d:
        alpha = d["meta"]["alpha"]
        seed = d["meta"]["seed"]
    else:
        alpha = d["alpha"]
        seed = d["seed"]
    alpha_str = f"a{int(alpha*100):03d}"
    key = (alpha_str, seed)
    data_sources[key] = f

    method_sig = {m: 0 for m in METHOD_KEYS}
    n_pairs = len(d["pairs"])

    for pair in d["pairs"]:
        fwd = pair["forward"]
        for m in METHOD_KEYS:
            if m in fwd and isinstance(fwd[m], dict) and get_sig(fwd[m], m):
                method_sig[m] += 1

    results[key] = {"method_sig": method_sig, "n_pairs": n_pairs}

ALPHAS = ["a000", "a025", "a050", "a075", "a100"]
ALPHA_LABELS = {"a000": "0.00", "a025": "0.25", "a050": "0.50", "a075": "0.75", "a100": "1.00"}

print("=" * 80)
print("Per-seed, per-method forward significant pair counts (out of 8)")
print("=" * 80)

for alpha in ALPHAS:
    seeds = sorted([k[1] for k in results if k[0] == alpha])
    if not seeds:
        print(f"\n{alpha} (alpha={ALPHA_LABELS[alpha]}): NO DATA")
        continue
    print(f"\n{alpha} (alpha={ALPHA_LABELS[alpha]}): seeds {seeds}")
    header = f"  {'Method':<25} " + " ".join(f"s{s:<5}" for s in seeds) + "  majority"
    print(header)
    for m in METHOD_KEYS:
        vals = [results[(alpha, s)]["method_sig"][m] for s in seeds]
        n_seeds_sig = sum(1 for v in vals if v >= 4)
        if len(seeds) >= 3:
            majority = "SIG" if n_seeds_sig >= 2 else "non"
        else:
            majority = "SIG" if n_seeds_sig >= 2 else "non"
        print(f"  {METHOD_LABELS[m]:<25} " + " ".join(f"{v}/8  " for v in vals) + f"  {majority}")

GROUND_TRUTH = {
    "a000": "NO",
    "a025": "NO",
    "a050": "AMB",
    "a075": "YES",
    "a100": "YES",
}

print("\n" + "=" * 80)
print("Classification table")
print("=" * 80)

def classify(gt, is_sig):
    if gt == "NO":
        return "FP" if is_sig else "OK"
    elif gt == "YES":
        return "OK" if is_sig else "FN"
    else:
        return "O"

method_verdicts = {}
for alpha in ALPHAS:
    seeds = sorted([k[1] for k in results if k[0] == alpha])
    if not seeds:
        method_verdicts[alpha] = {m: None for m in METHOD_KEYS}
        continue
    for m in METHOD_KEYS:
        vals = [results[(alpha, s)]["method_sig"][m] for s in seeds]
        n_seeds_sig = sum(1 for v in vals if v >= 4)
        if len(seeds) >= 3:
            is_sig = n_seeds_sig >= 2
        else:
            is_sig = n_seeds_sig >= 2
        method_verdicts.setdefault(alpha, {})[m] = is_sig

consensus_verdicts = {}
for alpha in ALPHAS:
    if alpha not in method_verdicts or all(v is None for v in method_verdicts[alpha].values()):
        consensus_verdicts[alpha] = None
        continue
    n_sig_methods = sum(1 for v in method_verdicts[alpha].values() if v)
    consensus_verdicts[alpha] = n_sig_methods >= 3

print(f"\n{'Method':<25} " + " ".join(f"a={ALPHA_LABELS[a]:>4}" for a in ALPHAS))
for m in METHOD_KEYS:
    row = []
    for alpha in ALPHAS:
        v = method_verdicts.get(alpha, {}).get(m)
        if v is None:
            row.append("N/A ")
        else:
            gt = GROUND_TRUTH[alpha]
            c = classify(gt, v)
            label = {"OK": " OK ", "FP": " FP ", "FN": " FN ", "O": " O  "}[c]
            row.append(label)
    print(f"  {METHOD_LABELS[m]:<25} " + " ".join(row))

row = []
for alpha in ALPHAS:
    v = consensus_verdicts.get(alpha)
    if v is None:
        row.append("N/A ")
    else:
        gt = GROUND_TRUTH[alpha]
        c = classify(gt, v)
        label = {"OK": " OK ", "FP": " FP ", "FN": " FN ", "O": " O  "}[c]
        row.append(label)
print(f"  {'Consensus (K>=3)':<25} " + " ".join(row))

print("\n" + "=" * 80)
print("Raw data: per-seed sig counts")
print("=" * 80)
for alpha in ALPHAS:
    seeds = sorted([k[1] for k in results if k[0] == alpha])
    if not seeds:
        print(f"  {alpha}: no data")
        continue
    print(f"  {alpha}:")
    for m in METHOD_KEYS:
        vals = [results[(alpha, s)]["method_sig"][m] for s in seeds]
        print(f"    {METHOD_LABELS[m]:<25}: {vals}")

print("\n" + "=" * 80)
print("Data sources")
print("=" * 80)
for k in sorted(data_sources.keys()):
    print(f"  {k[0]}_s{k[1]}: {data_sources[k]}")

# Print method verdicts summary for LaTeX generation
print("\n" + "=" * 80)
print("Method verdicts (True=sig, False=non-sig)")
print("=" * 80)
for alpha in ALPHAS:
    print(f"  {alpha}:")
    for m in METHOD_KEYS:
        v = method_verdicts.get(alpha, {}).get(m)
        print(f"    {METHOD_LABELS[m]:<25}: {v}")
    print(f"    {'Consensus (K>=3)':<25}: {consensus_verdicts.get(alpha)}")
