"""Analyze whether CWM unparseable outputs are systematically biased toward easy/hard instances."""

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
from scipy import stats

CWM_8B = "/root/autodl-tmp/eval_results/cwm_8b_ckpt400_test_merged/results_merged.jsonl"
CWM_DS = "/root/autodl-tmp/eval_results/deepseek_cwm_repo_s42_test/eval_deepseek_cwm_repo_s42_predictions.jsonl"
CLS_8B = "/root/autodl-tmp/eval_results/cls8b_s42_resume_ckpt3600_test_v2/eval_repo_cls_predictions.jsonl"
TEST_DATA = "/home/sonny/exec-sim-repair-verifier/data/swebench_full/test.jsonl"
OUT_JSON = "/home/sonny/exec-sim-repair-verifier/artifacts/cwm_parseable_bias.json"


def load_jsonl(path):
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def extract_repo(problem_id):
    parts = problem_id.split("__")
    if len(parts) == 2:
        return parts[0] + "/" + parts[1].rsplit("-", 1)[0]
    return problem_id


def chi2_or_fisher(table):
    """Run chi-squared; fall back to Fisher's exact for small cells."""
    table = np.array(table)
    if table.min() < 5:
        odds, p = stats.fisher_exact(table)
        return {"test": "fisher_exact", "odds_ratio": round(odds, 4), "p_value": p}
    chi2, p, dof, _ = stats.chi2_contingency(table)
    return {"test": "chi2", "statistic": round(chi2, 4), "dof": dof, "p_value": p}


def analyze_model(cwm_records, cls_lookup, test_lookup, model_name):
    n = len(cwm_records)
    parseable = [r for r in cwm_records if not r["unparseable"]]
    unparseable = [r for r in cwm_records if r["unparseable"]]
    n_p, n_u = len(parseable), len(unparseable)

    result = {
        "model": model_name,
        "total": n,
        "parseable": n_p,
        "unparseable": n_u,
        "unparseable_rate": round(n_u / n * 100, 2),
    }

    # --- 1. Ground truth label distribution ---
    p_pass = sum(1 for r in parseable if r["label"] == 1)
    p_fail = n_p - p_pass
    u_pass = sum(1 for r in unparseable if r["label"] == 1)
    u_fail = n_u - u_pass

    table_label = [[p_pass, p_fail], [u_pass, u_fail]]
    test_label = chi2_or_fisher(table_label)

    result["label_distribution"] = {
        "parseable_pass_rate": round(p_pass / n_p * 100, 2) if n_p else None,
        "unparseable_pass_rate": round(u_pass / n_u * 100, 2) if n_u else None,
        "overall_pass_rate": round((p_pass + u_pass) / n * 100, 2),
        "contingency_table": {"parseable": {"pass": p_pass, "fail": p_fail}, "unparseable": {"pass": u_pass, "fail": u_fail}},
        "statistical_test": test_label,
    }

    # --- 2. CLS accuracy as difficulty proxy ---
    p_cls_correct = sum(1 for r in parseable if cls_lookup.get(r["index"], {}).get("correct", 0) == 1)
    p_cls_wrong = n_p - p_cls_correct
    u_cls_correct = sum(1 for r in unparseable if cls_lookup.get(r["index"], {}).get("correct", 0) == 1)
    u_cls_wrong = n_u - u_cls_correct

    table_cls = [[p_cls_correct, p_cls_wrong], [u_cls_correct, u_cls_wrong]]
    test_cls = chi2_or_fisher(table_cls)

    result["cls_difficulty_proxy"] = {
        "parseable_cls_acc": round(p_cls_correct / n_p * 100, 2) if n_p else None,
        "unparseable_cls_acc": round(u_cls_correct / n_u * 100, 2) if n_u else None,
        "contingency_table": {"parseable": {"cls_correct": p_cls_correct, "cls_wrong": p_cls_wrong}, "unparseable": {"cls_correct": u_cls_correct, "cls_wrong": u_cls_wrong}},
        "statistical_test": test_cls,
    }

    # --- 3. Per-repo unparseable rate ---
    repo_stats = defaultdict(lambda: {"total": 0, "unparseable": 0, "pass_label": 0})
    for r in cwm_records:
        repo = extract_repo(r["problem_id"])
        repo_stats[repo]["total"] += 1
        if r["unparseable"]:
            repo_stats[repo]["unparseable"] += 1
        if r["label"] == 1:
            repo_stats[repo]["pass_label"] += 1

    repo_table = []
    for repo, s in sorted(repo_stats.items(), key=lambda x: -x[1]["total"]):
        repo_table.append({
            "repo": repo,
            "total": s["total"],
            "unparseable": s["unparseable"],
            "unparseable_rate": round(s["unparseable"] / s["total"] * 100, 2),
            "pass_rate": round(s["pass_label"] / s["total"] * 100, 2),
        })
    result["per_repo"] = repo_table

    # --- 4. Per-mutation-type unparseable rate ---
    mut_stats = defaultdict(lambda: {"total": 0, "unparseable": 0})
    for r in cwm_records:
        mt = r.get("mutation_type") or test_lookup.get(r["index"], {}).get("mutation_type", "unknown")
        mut_stats[mt]["total"] += 1
        if r["unparseable"]:
            mut_stats[mt]["unparseable"] += 1

    mut_table = {}
    for mt, s in sorted(mut_stats.items()):
        mut_table[mt] = {
            "total": s["total"],
            "unparseable": s["unparseable"],
            "unparseable_rate": round(s["unparseable"] / s["total"] * 100, 2),
        }
    result["per_mutation_type"] = mut_table

    # --- 5. Parseable-only accuracy vs overall accuracy ---
    parseable_correct = sum(1 for r in parseable if r["correct"] == 1)
    overall_correct = sum(1 for r in cwm_records if r["correct"] == 1)
    result["accuracy"] = {
        "parseable_only": round(parseable_correct / n_p * 100, 2) if n_p else None,
        "overall": round(overall_correct / n * 100, 2),
    }

    return result


def print_summary(res):
    print(f"\n{'='*60}")
    print(f"Model: {res['model']}")
    print(f"Total: {res['total']}, Parseable: {res['parseable']}, Unparseable: {res['unparseable']} ({res['unparseable_rate']}%)")
    print(f"Accuracy: overall={res['accuracy']['overall']}%, parseable-only={res['accuracy']['parseable_only']}%")

    ld = res["label_distribution"]
    print(f"\n--- Label distribution (pass rate) ---")
    print(f"  Parseable:   {ld['parseable_pass_rate']}%")
    print(f"  Unparseable: {ld['unparseable_pass_rate']}%")
    t = ld["statistical_test"]
    print(f"  Test: {t['test']}, p={t['p_value']:.2e}")
    if t["p_value"] < 0.05:
        print(f"  ** SIGNIFICANT bias: unparseable outputs have {'higher' if ld['unparseable_pass_rate'] > ld['parseable_pass_rate'] else 'lower'} pass rate")
    else:
        print(f"  No significant bias (p >= 0.05)")

    cd = res["cls_difficulty_proxy"]
    print(f"\n--- CLS difficulty proxy (CLS accuracy) ---")
    print(f"  Parseable:   {cd['parseable_cls_acc']}%")
    print(f"  Unparseable: {cd['unparseable_cls_acc']}%")
    t = cd["statistical_test"]
    print(f"  Test: {t['test']}, p={t['p_value']:.2e}")
    if t["p_value"] < 0.05:
        print(f"  ** SIGNIFICANT: unparseable instances are {'easier' if cd['unparseable_cls_acc'] > cd['parseable_cls_acc'] else 'harder'} (by CLS proxy)")
    else:
        print(f"  No significant difficulty bias (p >= 0.05)")

    print(f"\n--- Per-repo unparseable rate (top 10 by count) ---")
    for row in res["per_repo"][:10]:
        print(f"  {row['repo']:40s}  n={row['total']:5d}  unparse={row['unparseable_rate']:5.1f}%  pass_rate={row['pass_rate']:5.1f}%")

    print(f"\n--- Per-mutation-type unparseable rate ---")
    for mt, s in res["per_mutation_type"].items():
        print(f"  {mt:35s}  n={s['total']:5d}  unparse={s['unparseable_rate']:5.1f}%")


def main():
    print("Loading data...")
    cwm_8b = load_jsonl(CWM_8B)
    cwm_ds = load_jsonl(CWM_DS)
    cls_8b = load_jsonl(CLS_8B)
    test_data = load_jsonl(TEST_DATA)

    cls_lookup = {r["index"]: r for r in cls_8b}
    test_lookup = {i: r for i, r in enumerate(test_data)}

    results = {}

    print("Analyzing Qwen3-8B CWM...")
    results["qwen3_8b"] = analyze_model(cwm_8b, cls_lookup, test_lookup, "Qwen3-8B CWM repo-level")
    print_summary(results["qwen3_8b"])

    print("\nAnalyzing DeepSeek CWM...")
    results["deepseek"] = analyze_model(cwm_ds, cls_lookup, test_lookup, "DeepSeek CWM repo-level")
    print_summary(results["deepseek"])

    # --- Cross-model: instances unparseable in both ---
    both_unparse = sum(1 for a, b in zip(cwm_8b, cwm_ds) if a["unparseable"] and b["unparseable"])
    either_unparse = sum(1 for a, b in zip(cwm_8b, cwm_ds) if a["unparseable"] or b["unparseable"])
    q8b_only = sum(1 for a, b in zip(cwm_8b, cwm_ds) if a["unparseable"] and not b["unparseable"])
    ds_only = sum(1 for a, b in zip(cwm_8b, cwm_ds) if not a["unparseable"] and b["unparseable"])
    neither = sum(1 for a, b in zip(cwm_8b, cwm_ds) if not a["unparseable"] and not b["unparseable"])

    results["cross_model"] = {
        "both_unparseable": both_unparse,
        "qwen3_8b_only_unparseable": q8b_only,
        "deepseek_only_unparseable": ds_only,
        "neither_unparseable": neither,
        "jaccard_overlap": round(both_unparse / either_unparse, 4) if either_unparse else 0,
    }

    print(f"\n{'='*60}")
    print("Cross-model unparseable overlap:")
    cm = results["cross_model"]
    print(f"  Both unparseable:   {cm['both_unparseable']}")
    print(f"  Qwen3-8B only:     {cm['qwen3_8b_only_unparseable']}")
    print(f"  DeepSeek only:     {cm['deepseek_only_unparseable']}")
    print(f"  Neither:           {cm['neither_unparseable']}")
    print(f"  Jaccard overlap:   {cm['jaccard_overlap']}")

    with open(OUT_JSON, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nResults saved to {OUT_JSON}")


if __name__ == "__main__":
    main()
