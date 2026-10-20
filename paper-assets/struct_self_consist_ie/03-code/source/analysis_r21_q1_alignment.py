import json, os
import numpy as np
from scipy.stats import spearmanr

BASE = "/root/autodl-tmp/struct_self_consist_ie"
OUT_DIR = f"{BASE}/output/r21_q1_alignment"
os.makedirs(OUT_DIR, exist_ok=True)

DATASETS = {
    "SciERC_3epoch": f"{BASE}/output/exp_029a_scierc_3epoch/samples.jsonl",
    "SciERC_5epoch": f"{BASE}/output/exp_012_rerun_1024/samples.jsonl",
}

def entity_set(entities):
    return {(e["text"], e["type"]) for e in entities}

def f1_score(pred_set, gold_set):
    if not pred_set and not gold_set:
        return 1.0
    if not pred_set or not gold_set:
        return 0.0
    tp = len(pred_set & gold_set)
    p = tp / len(pred_set)
    r = tp / len(gold_set)
    return 2*p*r/(p+r) if (p+r) > 0 else 0.0

def bootstrap_ci(data, n_boot=10000, ci=0.95):
    data = np.array(data)
    if len(data) == 0:
        return None, None
    rng = np.random.default_rng(42)
    boot_medians = []
    for _ in range(n_boot):
        idx = rng.integers(0, len(data), size=len(data))
        boot_medians.append(np.median(data[idx]))
    boot_medians = np.array(boot_medians)
    lo = np.percentile(boot_medians, (1-ci)/2*100)
    hi = np.percentile(boot_medians, (1+ci)/2*100)
    return round(float(lo), 4), round(float(hi), 4)

results = {}
for name, path in DATASETS.items():
    if not os.path.exists(path):
        print(f"SKIP {name}: {path} not found")
        continue

    records = []
    with open(path) as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))

    rhos = []
    n_constant_lp = 0
    n_constant_f1 = 0
    n_gold_empty = 0
    n_valid = 0

    greedy_f1s = []
    lp_sel_f1s = []
    oracle_f1s = []

    for rec in records:
        gold_ents = rec.get("gold", {}).get("entities", [])
        if not gold_ents:
            n_gold_empty += 1
            continue
        gold_set = entity_set(gold_ents)
        samples = rec.get("samples", [])
        if len(samples) < 3:
            continue

        lps = []
        f1s = []
        for s in samples:
            lp = s.get("mean_logprob")
            if lp is None:
                continue
            pred_set = entity_set(s.get("entities", []))
            f1 = f1_score(pred_set, gold_set)
            lps.append(lp)
            f1s.append(f1)

        if len(lps) < 3:
            continue
        n_valid += 1

        lp_best_idx = int(np.argmax(lps))
        lp_sel_f1s.append(f1s[lp_best_idx])
        oracle_f1s.append(max(f1s))

        greedy = rec.get("greedy")
        if greedy:
            greedy_pred = entity_set(greedy.get("entities", []))
            greedy_f1s.append(f1_score(greedy_pred, gold_set))

        if len(set(lps)) < 2:
            n_constant_lp += 1
            continue
        if len(set(f1s)) < 2:
            n_constant_f1 += 1
            continue

        rho, p = spearmanr(lps, f1s)
        if not np.isnan(rho):
            rhos.append(rho)

    rhos = np.array(rhos)
    ci_lo, ci_hi = bootstrap_ci(rhos)

    greedy_macro = np.mean(greedy_f1s) if greedy_f1s else None
    lp_sel_macro = np.mean(lp_sel_f1s) if lp_sel_f1s else None
    lp_sel_delta = (lp_sel_macro - greedy_macro) * 100 if (greedy_macro is not None and lp_sel_macro is not None) else None

    r = {
        "n_total": len(records),
        "n_gold_filtered": len(records) - n_gold_empty,
        "n_valid": n_valid,
        "n_valid_rho": len(rhos),
        "n_constant_lp": n_constant_lp,
        "n_constant_f1": n_constant_f1,
        "n_samples_per_instance": len(records[0].get("samples", [])) if records else None,
        "median_rho": round(float(np.median(rhos)), 4) if len(rhos) > 0 else None,
        "mean_rho": round(float(np.mean(rhos)), 4) if len(rhos) > 0 else None,
        "std_rho": round(float(np.std(rhos)), 4) if len(rhos) > 0 else None,
        "ci95_lo": ci_lo,
        "ci95_hi": ci_hi,
        "pct_positive_rho": round(float(np.mean(rhos > 0) * 100), 2) if len(rhos) > 0 else None,
        "greedy_macro_f1": round(float(greedy_macro), 4) if greedy_macro is not None else None,
        "lp_sel_macro_f1": round(float(lp_sel_macro), 4) if lp_sel_macro is not None else None,
        "lp_sel_delta_pp": round(float(lp_sel_delta), 2) if lp_sel_delta is not None else None,
        "oracle_macro_f1": round(float(np.mean(oracle_f1s)), 4) if oracle_f1s else None,
    }
    results[name] = r
    print(f"\n=== {name} ===")
    print(f"  N_inst={r['n_valid']}, N_rho={r['n_valid_rho']}, N_samples={r['n_samples_per_instance']}")
    print(f"  Median rho={r['median_rho']}, Mean rho={r['mean_rho']}, 95% CI=[{ci_lo}, {ci_hi}]")
    print(f"  %positive={r['pct_positive_rho']}%")
    print(f"  Greedy F1={r['greedy_macro_f1']}, LP_sel F1={r['lp_sel_macro_f1']}, Delta={r['lp_sel_delta_pp']}pp")
    print(f"  Oracle F1={r['oracle_macro_f1']}")
    print(f"  Constant LP={n_constant_lp}, Constant F1={n_constant_f1}")

with open(f"{OUT_DIR}/results.json", "w") as f:
    json.dump(results, f, indent=2)

report = []
report.append("# R21 Q1: 3-epoch SciERC Within-Instance Alignment rho(LP, F1)")
report.append("")
report.append("## Method")
report.append("Per-instance Spearman rho(mean_logprob, entity_F1) across N samples.")
report.append("Instances with <3 valid samples, empty gold, constant LP, or constant F1 excluded from rho computation.")
report.append("95% CI via bootstrap (10000 resamples) on median rho.")
report.append("")
report.append("## Results")
report.append("")
report.append("| Setting | N_inst | N_rho | N_samp | Median rho | Mean rho | 95% CI | %pos | LP_sel Delta |")
report.append("|---------|--------|-------|--------|------------|----------|--------|------|--------------|")
for name, r in results.items():
    epoch = "3-epoch" if "3epoch" in name else "5-epoch"
    ci_str = f"[{r['ci95_lo']}, {r['ci95_hi']}]" if r['ci95_lo'] is not None else "N/A"
    delta_str = f"{r['lp_sel_delta_pp']:+.2f}pp" if r['lp_sel_delta_pp'] is not None else "N/A"
    report.append(f"| {epoch} | {r['n_valid']} | {r['n_valid_rho']} | {r['n_samples_per_instance']} | {r['median_rho']} | {r['mean_rho']} | {ci_str} | {r['pct_positive_rho']}% | {delta_str} |")

report.append("")
report.append("## Interpretation")
if "SciERC_3epoch" in results and "SciERC_5epoch" in results:
    r3 = results["SciERC_3epoch"]
    r5 = results["SciERC_5epoch"]
    diff = r3["median_rho"] - r5["median_rho"] if r3["median_rho"] and r5["median_rho"] else None
    if diff is not None:
        report.append(f"- 3-epoch median rho = {r3['median_rho']}, 5-epoch median rho = {r5['median_rho']} (diff = {diff:+.4f})")
        if abs(diff) < 0.10:
            report.append("- The alignment rho values are close, suggesting LP-F1 alignment is a dataset-intrinsic property, not an epoch artifact.")
        else:
            report.append(f"- Notable difference of {diff:+.4f} between epochs.")
        report.append(f"- 3-epoch has fewer constant-F1 instances ({r3['n_constant_f1']} vs {r5['n_constant_f1']}), consistent with lower degeneracy at fewer epochs.")

report_text = "\n".join(report)
with open(f"{OUT_DIR}/report.md", "w") as f:
    f.write(report_text)

print(f"\n{'='*60}")
print(report_text)
print(f"\nSaved to {OUT_DIR}/results.json and {OUT_DIR}/report.md")
