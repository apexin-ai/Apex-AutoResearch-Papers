"""Compute within-instance Spearman rho(LP, F1) for LLaMA CoNLL N=8."""
import json
import numpy as np
from scipy.stats import spearmanr

DATA = "/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/samples.jsonl"

def entity_set(entities):
    return {(e["text"], e["type"]) for e in entities}

def f1_score(pred_set, gold_set):
    if not pred_set and not gold_set:
        return 1.0
    if not pred_set or not gold_set:
        return 0.0
    tp = len(pred_set & gold_set)
    p = tp / len(pred_set) if pred_set else 0
    r = tp / len(gold_set) if gold_set else 0
    return 2*p*r/(p+r) if (p+r) > 0 else 0.0

records = []
with open(DATA) as f:
    for line in f:
        if line.strip():
            records.append(json.loads(line))

rhos = []
n_constant_lp = 0
n_constant_f1 = 0
n_too_few = 0
n_gold_empty = 0

for rec in records:
    gold_ents = rec.get("gold", {}).get("entities", [])
    if not gold_ents:
        n_gold_empty += 1
        continue

    gold_set = entity_set(gold_ents)
    samples = rec.get("samples", [])
    if len(samples) < 3:
        n_too_few += 1
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
        n_too_few += 1
        continue

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
result = {
    "metric": "within_instance_rho_LP_F1",
    "dataset": "llama_conll_n8",
    "n_total": len(records),
    "n_gold_empty": n_gold_empty,
    "n_constant_f1_excluded": n_constant_f1,
    "n_constant_lp_excluded": n_constant_lp,
    "n_valid_rho": len(rhos),
    "median": round(float(np.median(rhos)), 4) if len(rhos) > 0 else None,
    "mean": round(float(np.mean(rhos)), 4) if len(rhos) > 0 else None,
    "std": round(float(np.std(rhos)), 4) if len(rhos) > 0 else None,
    "pct_positive": round(float((rhos > 0).mean() * 100), 1) if len(rhos) > 0 else None,
    "pct_gt_0.3": round(float((rhos > 0.3).mean() * 100), 1) if len(rhos) > 0 else None,
    "q25": round(float(np.percentile(rhos, 25)), 4) if len(rhos) > 0 else None,
    "q75": round(float(np.percentile(rhos, 75)), 4) if len(rhos) > 0 else None,
}

print(json.dumps(result, indent=2))

out_path = "/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/within_lp_f1_rho.json"
with open(out_path, "w") as f:
    json.dump(result, f, indent=2)
print(f"\nSaved to {out_path}")
