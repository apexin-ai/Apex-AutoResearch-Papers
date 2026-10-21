#!/usr/bin/env python3
"""Cross-dataset OOD signal analysis for structured self-consistency IE."""
import json
import sys
import numpy as np
from collections import Counter
from scipy.stats import spearmanr
from sklearn.metrics import roc_auc_score

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import structural_consistency_soft_jaccard, fleiss_kappa_surface
from evaluation import per_instance_f1


def load_data(path):
    records = []
    with open(path) as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    return records


def compute_exact_match_rate(samples, subtask):
    if subtask == "ner":
        keys = [frozenset((e["text"], e["type"]) for e in s.get("entities", [])) for s in samples]
    else:
        keys = [frozenset((r["head"], r["tail"], r["type"]) for r in s.get("relations", [])) for s in samples]
    if not keys:
        return 0.0
    counter = Counter(keys)
    return counter.most_common(1)[0][1] / len(samples)


def compute_voting_confidence(samples, subtask):
    N = len(samples)
    if N == 0:
        return 0.0
    counter = Counter()
    if subtask == "ner":
        for s in samples:
            for e in s.get("entities", []):
                counter[(e["text"], e["type"])] += 1
    else:
        for s in samples:
            for r in s.get("relations", []):
                counter[(r["head"], r["tail"], r["type"])] += 1
    if not counter:
        return 0.0
    majority = [v / N for v in counter.values() if v > N / 2]
    if not majority:
        return 0.0
    return float(np.mean(majority))


def compute_mean_logprob(samples):
    logprobs = [s.get("mean_logprob") for s in samples if s.get("mean_logprob") is not None]
    logprobs = [lp for lp in logprobs if np.isfinite(lp)]
    if not logprobs:
        return float("nan")
    return float(np.mean(logprobs))


def analyze_experiment(data_path, subtask_signal, subtask_eval_ner, subtask_eval_re=None):
    records = load_data(data_path)
    total = len(records)

    parsed = [r for r in records if len(r.get("samples", [])) > 0]
    parse_rate = len(parsed) / total * 100 if total > 0 else 0

    valid_ner = [r for r in parsed if len(r["gold"].get("entities", [])) > 0]

    sj_vals, fk_vals, vc_vals, em_vals, lp_vals, f1_ner_vals = [], [], [], [], [], []
    f1_re_vals = []

    for inst in valid_ner:
        samples = inst["samples"]
        gold = inst["gold"]
        greedy = inst.get("greedy", samples[0])

        sj_vals.append(structural_consistency_soft_jaccard(samples, subtask=subtask_signal))
        fk_vals.append(fleiss_kappa_surface(samples, subtask=subtask_signal))
        vc_vals.append(compute_voting_confidence(samples, subtask_signal))
        em_vals.append(compute_exact_match_rate(samples, subtask_signal))
        lp_vals.append(compute_mean_logprob(samples))
        f1_ner_vals.append(per_instance_f1(greedy, gold, subtask="ner"))

        if subtask_eval_re:
            f1_re_vals.append(per_instance_f1(greedy, gold, subtask="re"))

    greedy_ner_f1 = float(np.mean(f1_ner_vals)) if f1_ner_vals else 0.0
    greedy_re_f1 = float(np.mean(f1_re_vals)) if f1_re_vals else None

    signals = {
        "SJ": np.array(sj_vals),
        "FK": np.array(fk_vals),
        "VC": np.array(vc_vals),
        "EM": np.array(em_vals),
        "LP": np.array(lp_vals),
    }
    f1_arr = np.array(f1_ner_vals)

    results = {
        "total_instances": total,
        "parsed_instances": len(parsed),
        "parse_rate": parse_rate,
        "valid_ner_instances": len(valid_ner),
        "greedy_ner_f1": greedy_ner_f1,
        "greedy_re_f1": greedy_re_f1,
        "signals": {},
    }

    median_f1 = np.median(f1_arr)
    binary_labels = (f1_arr >= median_f1).astype(int)

    for name, vals in signals.items():
        mask = np.isfinite(vals) & np.isfinite(f1_arr)
        v, f = vals[mask], f1_arr[mask]
        bl = binary_labels[mask]

        rho, pval = spearmanr(v, f)

        try:
            if len(np.unique(bl)) > 1:
                auroc = roc_auc_score(bl, v)
            else:
                auroc = float("nan")
        except Exception:
            auroc = float("nan")

        results["signals"][name] = {
            "rho": round(float(rho), 4),
            "p_value": float(pval),
            "auroc": round(float(auroc), 4) if np.isfinite(auroc) else "N/A",
            "n": int(mask.sum()),
        }

    return results


IN_DOMAIN_RHO = {
    "VC": 0.386, "SJ": 0.364, "EM": 0.307, "FK": 0.254, "LP": 0.217,
}


def format_report(exp1_results, exp2_results):
    lines = ["# Cross-dataset OOD Signal Analysis", ""]

    for label, res, has_re in [
        ("Exp 1: SciERC model → CoNLL (NER only)", exp1_results, False),
        ("Exp 2: CoNLL model → SciERC (NER+RE)", exp2_results, True),
    ]:
        lines.append(f"## {label}")
        lines.append(f"- Instances: {res['total_instances']}, Parsed: {res['parsed_instances']}, Valid NER: {res['valid_ner_instances']}")
        lines.append(f"- Parse rate: {res['parse_rate']:.1f}%")
        lines.append(f"- Greedy NER F1: {res['greedy_ner_f1']:.4f}")
        if has_re and res.get("greedy_re_f1") is not None:
            lines.append(f"- Greedy RE F1: {res['greedy_re_f1']:.4f}")
        lines.append("")
        lines.append("| Signal | ρ | p-value | AUROC | In-domain ρ | Δρ |")
        lines.append("|--------|---|---------|-------|-------------|-----|")
        for sig_name in ["SJ", "FK", "VC", "LP", "EM"]:
            s = res["signals"][sig_name]
            in_d = IN_DOMAIN_RHO.get(sig_name, "N/A")
            if isinstance(in_d, (int, float)):
                delta = f"{s['rho'] - in_d:+.4f}"
            else:
                delta = "N/A"
            p_str = f"{s['p_value']:.2e}" if s['p_value'] < 0.001 else f"{s['p_value']:.4f}"
            sig_marker = " ***" if s['p_value'] < 0.001 else (" **" if s['p_value'] < 0.01 else (" *" if s['p_value'] < 0.05 else ""))
            auroc_str = f"{s['auroc']:.4f}" if isinstance(s['auroc'], float) else s['auroc']
            lines.append(f"| {sig_name} | {s['rho']:+.4f}{sig_marker} | {p_str} | {auroc_str} | {in_d} | {delta} |")
        lines.append("")

    lines.append("## Key Findings")
    lines.append("")

    for label, res in [("SciERC→CoNLL", exp1_results), ("CoNLL→SciERC", exp2_results)]:
        sigs = res["signals"]
        structural = [(n, sigs[n]["rho"]) for n in ["SJ", "FK", "VC"]]
        lp_rho = sigs["LP"]["rho"]
        best_struct = max(structural, key=lambda x: x[1])
        struct_sig = all(sigs[n]["p_value"] < 0.05 for n in ["SJ", "FK", "VC"])
        lp_sig = sigs["LP"]["p_value"] < 0.05

        lines.append(f"### {label}")
        lines.append(f"- Best structural signal: {best_struct[0]} (ρ={best_struct[1]:+.4f})")
        lines.append(f"- LogProb (LP): ρ={lp_rho:+.4f}")
        if best_struct[1] > lp_rho:
            lines.append(f"- Structural > LP by Δρ={best_struct[1]-lp_rho:+.4f}")
        else:
            lines.append(f"- LP > best structural by Δρ={lp_rho-best_struct[1]:+.4f}")
        lines.append(f"- Structural signals {'ALL significant (p<0.05)' if struct_sig else 'NOT all significant'}")
        lines.append(f"- LP {'significant' if lp_sig else 'NOT significant'} (p={sigs['LP']['p_value']:.2e})")
        lines.append("")

    lines.append("### Overall: Do structural signals remain effective under OOD?")
    lines.append("")

    for label, res in [("SciERC→CoNLL", exp1_results), ("CoNLL→SciERC", exp2_results)]:
        sigs = res["signals"]
        struct_rhos = [sigs[n]["rho"] for n in ["SJ", "FK", "VC"]]
        lp_rho = sigs["LP"]["rho"]
        avg_struct = np.mean(struct_rhos)
        in_domain_avg = np.mean([IN_DOMAIN_RHO[n] for n in ["SJ", "FK", "VC"]])
        lines.append(f"- **{label}**: avg structural ρ = {avg_struct:.4f} (in-domain avg = {in_domain_avg:.4f}, Δ = {avg_struct-in_domain_avg:+.4f}), LP ρ = {lp_rho:+.4f} (in-domain = {IN_DOMAIN_RHO['LP']}, Δ = {lp_rho-IN_DOMAIN_RHO['LP']:+.4f})")

    return "\n".join(lines)


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--exp1_path", required=True)
    p.add_argument("--exp2_path", required=True)
    p.add_argument("--output", required=True)
    args = p.parse_args()

    print("Analyzing Exp 1: SciERC model -> CoNLL ...")
    exp1 = analyze_experiment(args.exp1_path, subtask_signal="ner", subtask_eval_ner="ner")

    print("Analyzing Exp 2: CoNLL model -> SciERC ...")
    exp2 = analyze_experiment(args.exp2_path, subtask_signal="ner", subtask_eval_ner="ner", subtask_eval_re="re")

    report = format_report(exp1, exp2)
    print(report)

    with open(args.output, "w") as f:
        f.write(report + "\n")
    print(f"\nReport saved to {args.output}")

    json_out = args.output.replace(".md", ".json")
    with open(json_out, "w") as f:
        json.dump({"exp1_scierc_to_conll": exp1, "exp2_conll_to_scierc": exp2}, f, indent=2, default=str)
    print(f"JSON saved to {json_out}")
