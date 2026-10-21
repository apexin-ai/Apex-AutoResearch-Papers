"""exp-002: 5-signal analysis for CoNLL-2003 NER (cross-dataset validation).

Computes: soft_jaccard, fleiss_kappa, mean_logprob, exact_match_rate, entity_voting_conf
Metrics: Spearman rho, Kendall tau, AUROC, bootstrap 95% CI
"""

import json
import os
import sys
from collections import Counter

import numpy as np
from scipy.stats import spearmanr, kendalltau

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import compute_all_consistency_scores
from evaluation import per_instance_f1

DATA_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/exp002_conll2003/samples.jsonl"
OUTPUT_DIR = "/root/autodl-tmp/struct_self_consist_ie/output/exp002_conll2003"
SUBTASK = "ner"


def load_data(path):
    instances = []
    with open(path) as f:
        for line in f:
            if line.strip():
                instances.append(json.loads(line))
    return instances


def auroc_simple(scores, labels):
    scores = np.array(scores, dtype=float)
    labels = np.array(labels, dtype=int)
    if len(set(labels)) < 2:
        return float('nan')
    pos = scores[labels == 1]
    neg = scores[labels == 0]
    if len(pos) == 0 or len(neg) == 0:
        return float('nan')
    count = sum(np.sum(p > neg) + 0.5 * np.sum(p == neg) for p in pos)
    return count / (len(pos) * len(neg))


def compute_exact_match_rate(samples, subtask):
    keys = [frozenset((e["text"], e["type"]) for e in s.get("entities", [])) for s in samples]
    counter = Counter(keys)
    return counter.most_common(1)[0][1] / len(samples)


def compute_entity_voting_conf(samples, subtask):
    N = len(samples)
    counter = Counter()
    for s in samples:
        for e in s.get("entities", []):
            counter[(e["text"], e["type"])] += 1
    if not counter:
        return 0.0
    return float(np.mean([v / N for v in counter.values()]))


def compute_mean_logprob(samples):
    logprobs = [s.get("mean_logprob") for s in samples if s.get("mean_logprob") is not None]
    logprobs = [lp for lp in logprobs if np.isfinite(lp)]
    if not logprobs:
        return float("nan")
    return float(np.mean(logprobs))


def compute_instance_mean_logprob(inst):
    if "logprobs" in inst and inst["logprobs"]:
        lps = [lp for lp in inst["logprobs"] if np.isfinite(lp)]
        return float(np.mean(lps)) if lps else float("nan")
    samples = inst["samples"]
    lps = [compute_mean_logprob([s]) for s in samples]
    lps = [lp for lp in lps if np.isfinite(lp)]
    return float(np.mean(lps)) if lps else float("nan")


def compute_all_signals(instances, subtask):
    consistency = compute_all_consistency_scores(instances, subtask=subtask)
    signals = {
        "soft_jaccard": consistency["soft_jaccard"],
        "fleiss_kappa": consistency["fleiss_kappa"],
        "mean_logprob": [],
        "exact_match": [],
        "entity_voting": [],
    }
    f1_scores = []
    for inst in instances:
        samples = inst["samples"]
        gold = inst["gold"]
        greedy = inst.get("greedy")
        if greedy is not None:
            f1 = per_instance_f1(greedy, gold, subtask=subtask)
        else:
            f1 = per_instance_f1(samples[0], gold, subtask=subtask)
        f1_scores.append(f1)
        signals["mean_logprob"].append(compute_instance_mean_logprob(inst))
        signals["exact_match"].append(compute_exact_match_rate(samples, subtask))
        signals["entity_voting"].append(compute_entity_voting_conf(samples, subtask))
    return signals, f1_scores


def compute_metrics(signal_values, f1_values, median_f1):
    x = np.array(signal_values, dtype=float)
    y = np.array(f1_values, dtype=float)
    mask = np.isfinite(x) & np.isfinite(y)
    x, y = x[mask], y[mask]
    if len(x) < 3:
        return {"rho": float("nan"), "p_rho": float("nan"),
                "tau": float("nan"), "p_tau": float("nan"),
                "auroc": float("nan"), "n": int(mask.sum())}
    rho, p_rho = spearmanr(x, y)
    tau, p_tau = kendalltau(x, y)
    labels = (y >= median_f1).astype(int)
    auc = auroc_simple(x, labels) if len(set(labels)) >= 2 else float("nan")
    return {"rho": float(rho), "p_rho": float(p_rho),
            "tau": float(tau), "p_tau": float(p_tau),
            "auroc": float(auc), "n": int(mask.sum())}


def bootstrap_rho_diff(sig_a, sig_b, f1_values, n_boot=2000, seed=42):
    rng = np.random.RandomState(seed)
    a = np.array(sig_a, dtype=float)
    b = np.array(sig_b, dtype=float)
    y = np.array(f1_values, dtype=float)
    mask = np.isfinite(a) & np.isfinite(b) & np.isfinite(y)
    a, b, y = a[mask], b[mask], y[mask]
    n = len(y)
    if n < 10:
        return {"mean_diff": float("nan"), "ci_95_low": float("nan"),
                "ci_95_high": float("nan"), "significant": False}
    diffs = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, n)
        rho_a = spearmanr(a[idx], y[idx])[0]
        rho_b = spearmanr(b[idx], y[idx])[0]
        diffs.append(rho_a - rho_b)
    diffs = np.array(diffs)
    return {
        "mean_diff": float(np.mean(diffs)),
        "ci_95_low": float(np.percentile(diffs, 2.5)),
        "ci_95_high": float(np.percentile(diffs, 97.5)),
        "significant": bool(np.percentile(diffs, 2.5) > 0 or np.percentile(diffs, 97.5) < 0),
    }


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    instances = load_data(DATA_PATH)
    print(f"Loaded {len(instances)} instances")

    field = "entities"
    valid = [inst for inst in instances if len(inst["gold"].get(field, [])) > 0]
    print(f"Valid (gold non-empty): {len(valid)}")

    signals, f1_scores = compute_all_signals(valid, SUBTASK)

    # Conditional: exclude all-samples-F1=0
    cond_mask = []
    for i, inst in enumerate(valid):
        has_nonzero = any(
            per_instance_f1(s, inst["gold"], subtask=SUBTASK) > 0
            for s in inst["samples"]
        )
        cond_mask.append(has_nonzero)
    cond_idx = [i for i, m in enumerate(cond_mask) if m]
    print(f"Conditional: {len(cond_idx)}")

    median_full = float(np.median(f1_scores))
    cond_f1 = [f1_scores[i] for i in cond_idx]
    median_cond = float(np.median(cond_f1)) if cond_f1 else 0.0

    signal_order = ["soft_jaccard", "fleiss_kappa", "mean_logprob", "exact_match", "entity_voting"]
    signal_labels = {
        "soft_jaccard": "SJ (Soft Jaccard)",
        "fleiss_kappa": "FK (Fleiss Kappa)",
        "mean_logprob": "LogProb (Mean)",
        "exact_match": "EM (Exact Match Rate)",
        "entity_voting": "EV (Entity Voting Conf)",
    }

    results = {
        "dataset": "conll2003",
        "subtask": "ner",
        "n_total": len(instances),
        "n_valid": len(valid),
        "n_conditional": len(cond_idx),
        "median_f1_full": median_full,
        "median_f1_cond": median_cond,
        "signals": {},
    }

    print(f"\n{'='*70}")
    print(f"{'Signal':<20} {'ρ (full)':>10} {'τ (full)':>10} {'AUROC':>10} {'ρ (cond)':>10}")
    print(f"{'-'*70}")

    for sname in signal_order:
        svals = signals[sname]
        full_m = compute_metrics(svals, f1_scores, median_full)
        cond_svals = [svals[i] for i in cond_idx]
        cond_m = compute_metrics(cond_svals, cond_f1, median_cond)
        results["signals"][sname] = {"full": full_m, "cond": cond_m}
        print(f"{signal_labels[sname]:<20} {full_m['rho']:>+10.4f} {full_m['tau']:>+10.4f} {full_m['auroc']:>10.4f} {cond_m['rho']:>+10.4f}")

    # Bootstrap CI: SJ vs each other signal
    print(f"\n{'='*70}")
    print("Bootstrap CI (SJ vs others, n_boot=2000)")
    sj = signals["soft_jaccard"]
    bootstrap = {}
    for other in ["fleiss_kappa", "mean_logprob", "exact_match", "entity_voting"]:
        boot = bootstrap_rho_diff(sj, signals[other], f1_scores)
        bootstrap[f"sj_vs_{other}"] = boot
        sig_str = "***" if boot["significant"] else ""
        print(f"  SJ vs {signal_labels[other]:<20}: Δρ={boot['mean_diff']:+.4f}  CI=[{boot['ci_95_low']:+.4f}, {boot['ci_95_high']:+.4f}] {sig_str}")
    results["bootstrap_ci"] = bootstrap

    # Key comparison: SJ vs logprob
    sj_rho = results["signals"]["soft_jaccard"]["full"]["rho"]
    lp_rho = results["signals"]["mean_logprob"]["full"]["rho"]
    sj_wins = sj_rho > lp_rho
    boot_sj_lp = bootstrap.get("sj_vs_mean_logprob", {})

    results["key_comparison"] = {
        "sj_rho": sj_rho,
        "logprob_rho": lp_rho,
        "sj_wins": sj_wins,
        "delta_rho": sj_rho - lp_rho,
        "bootstrap_significant": boot_sj_lp.get("significant", False),
    }

    # Voting-based F1
    from evaluation import compute_ner_f1
    greedy_preds = [inst.get("greedy", inst["samples"][0]) for inst in valid]
    golds = [inst["gold"] for inst in valid]
    greedy_f1 = compute_ner_f1(greedy_preds, golds)["f1"]
    oracle_preds = [max(inst["samples"], key=lambda s: per_instance_f1(s, inst["gold"], SUBTASK)) for inst in valid]
    oracle_f1 = compute_ner_f1(oracle_preds, golds)["f1"]

    # Majority voting
    voting_preds = []
    for inst in valid:
        entity_counter = Counter()
        for s in inst["samples"]:
            for e in s.get("entities", []):
                entity_counter[(e["text"], e["type"], e.get("start", 0), e.get("end", 0))] += 1
        N = len(inst["samples"])
        voted_entities = [{"text": k[0], "type": k[1], "start": k[2], "end": k[3]} for k, v in entity_counter.items() if v > N / 2]
        voting_preds.append({"entities": voted_entities})
    voting_f1 = compute_ner_f1(voting_preds, golds)["f1"]

    results["f1_summary"] = {
        "greedy_f1": greedy_f1,
        "oracle_f1": oracle_f1,
        "voting_f1": voting_f1,
        "oracle_headroom": oracle_f1 - greedy_f1,
    }

    print(f"\n{'='*70}")
    print(f"F1 Summary: greedy={greedy_f1:.4f}  voting={voting_f1:.4f}  oracle={oracle_f1:.4f}  headroom={oracle_f1-greedy_f1:.4f}")

    conclusion = "success" if sj_wins else "negative"
    print(f"\n*** Conclusion: {conclusion.upper()} (SJ ρ={sj_rho:.4f} vs LogProb ρ={lp_rho:.4f}, delta={sj_rho-lp_rho:+.4f})")
    if boot_sj_lp.get("significant"):
        print(f"    Bootstrap significant: CI=[{boot_sj_lp['ci_95_low']:+.4f}, {boot_sj_lp['ci_95_high']:+.4f}]")
    else:
        print(f"    Bootstrap NOT significant: CI=[{boot_sj_lp.get('ci_95_low',0):+.4f}, {boot_sj_lp.get('ci_95_high',0):+.4f}]")
    results["conclusion"] = conclusion

    json_path = os.path.join(OUTPUT_DIR, "exp002_5signal_report.json")
    with open(json_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nSaved: {json_path}")


if __name__ == "__main__":
    main()
