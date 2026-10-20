#!/usr/bin/env python3
"""
Unified Fleiss' kappa computation for all SICA experiments.
Non-standard answers mapped to Unknown (FOLIO/ProofWriter) or excluded (LogiQA).
Output: Table 3 data for the paper.

Usage:
    python compute_fleiss_kappa_unified.py --results-dir results/ --output fleiss_kappa_unified.json
    python compute_fleiss_kappa_unified.py --results-dir results/ --exp exp033_mistral_7b_folio204
"""
import json, os, glob, sys, argparse
import numpy as np
from collections import Counter

FOLIO_PW_CATEGORIES = ['True', 'False', 'Unknown']
LOGIQA_CATEGORIES = ['A', 'B', 'C', 'D']

K_NOMINAL = 12


def detect_dataset(intermediates_dir):
    """Detect dataset type from the first JSON file's 'dataset' field."""
    files = sorted(glob.glob(os.path.join(intermediates_dir, "*.json")))
    if not files:
        return None
    with open(files[0]) as f:
        data = json.load(f)
    return data.get("problem", {}).get("dataset", "unknown")


def get_categories(dataset):
    if dataset in ("folio", "proofwriter"):
        return FOLIO_PW_CATEGORIES
    elif dataset == "logiqa":
        return LOGIQA_CATEGORIES
    else:
        return FOLIO_PW_CATEGORIES


def normalize_answer(ans, categories, raw=False):
    """Map answer to one of the valid categories.
    None/empty -> None (excluded from vote count).
    Non-standard -> Unknown for FOLIO/PW, None for LogiQA.
    """
    if ans is None:
        return None
    ans_str = str(ans).strip()
    if not ans_str:
        return None

    lower_map = {c.lower(): c for c in categories}
    if ans_str.lower() in lower_map:
        return lower_map[ans_str.lower()]

    if not raw and categories == FOLIO_PW_CATEGORIES:
        return 'Unknown'

    return None


def fleiss_kappa_variable_n(M):
    """Fleiss' kappa allowing variable n_i (raters per subject).

    M: (n_subjects, n_categories) matrix.
    Rows with < 2 raters are excluded.
    """
    n_i = M.sum(axis=1)
    valid = n_i >= 2
    M = M[valid]
    n_i = n_i[valid]
    n = M.shape[0]

    if n == 0:
        return float('nan'), 0

    P_i = (np.sum(M ** 2, axis=1) - n_i) / (n_i * (n_i - 1))
    P_bar = np.mean(P_i)

    p_j = M.sum(axis=0) / n_i.sum()
    P_e = np.sum(p_j ** 2)

    if (1 - P_e) == 0:
        return 1.0, int(n)

    kappa = (P_bar - P_e) / (1 - P_e)
    return float(kappa), int(n)


def eff_k(kappa, K=K_NOMINAL):
    """Eff-K = K / (1 + (K-1) * kappa), K=12 fixed."""
    denom = 1 + (K - 1) * kappa
    if denom == 0:
        return float('inf')
    return K / denom


def process_experiment(intermediates_dir, exp_name, raw=False, K_used=K_NOMINAL):
    dataset = detect_dataset(intermediates_dir)
    if dataset is None:
        print(f"  SKIP {exp_name}: no files in {intermediates_dir}", file=sys.stderr)
        return None

    categories = get_categories(dataset)
    cat_idx = {c: i for i, c in enumerate(categories)}
    n_cat = len(categories)

    files = sorted(glob.glob(os.path.join(intermediates_dir, "*.json")))
    ratings = []
    n_valid_votes = 0
    n_total_traces = 0
    n_excluded = 0
    n_nonstandard = 0
    correct_sica = 0
    correct_sc = 0
    ground_truths = []
    sica_answers = []

    for fpath in files:
        with open(fpath) as f:
            data = json.load(f)

        gt = data.get("problem", {}).get("answer", None)
        sr = data.get("sica_result", {})
        traces = sr.get("traces", [])
        sica_answer = sr.get("answer", None)

        row = [0] * n_cat
        n_total_traces += len(traces)

        for t in traces:
            ans_raw = t.get("answer", None)
            ans_norm = normalize_answer(ans_raw, categories, raw=raw)
            if ans_norm is None:
                n_excluded += 1
                continue
            if ans_raw is not None and str(ans_raw).strip() != "" and ans_norm != str(ans_raw).strip():
                if not any(str(ans_raw).strip().lower() == c.lower() for c in categories):
                    n_nonstandard += 1
            row[cat_idx[ans_norm]] += 1

        row_total = sum(row)
        n_valid_votes += row_total
        ratings.append(row)

        if gt is not None and row_total > 0:
            majority_idx = int(np.argmax(row))
            sc_pred = categories[majority_idx]
            gt_norm = normalize_answer(gt, categories)
            if gt_norm is not None:
                ground_truths.append(gt_norm)
                sica_answers.append(sica_answer)
                if sc_pred == gt_norm:
                    correct_sc += 1
                sica_norm = normalize_answer(sica_answer, categories)
                if sica_norm == gt_norm:
                    correct_sica += 1

    M = np.array(ratings, dtype=float)
    n_problems = len(M)
    n_per_q = M.sum(axis=1)
    n_total_votes = n_problems * K_used

    kappa, n_valid_problems = fleiss_kappa_variable_n(M)
    ek = eff_k(kappa, K=K_used)

    sc_acc = correct_sc / len(ground_truths) * 100 if ground_truths else float('nan')
    sica_acc = correct_sica / len(ground_truths) * 100 if ground_truths else float('nan')
    delta_pp = sica_acc - sc_acc if ground_truths else float('nan')

    total_v = M.sum()
    cat_dist = {}
    for i, c in enumerate(categories):
        cat_dist[c] = float(M[:, i].sum() / total_v * 100) if total_v > 0 else 0.0

    unanimous = float(np.sum(M.max(axis=1) == n_per_q) / n_problems * 100) if n_problems > 0 else 0.0

    model_label = ""
    dataset_label = ""
    if "mistral" in exp_name.lower():
        model_label = "Mistral-7B-Instruct-v0.3"
    elif "qwen3_14b" in exp_name.lower() or "qwen3-14b" in exp_name.lower():
        model_label = "Qwen3-14B"
    elif "qwen25_14b" in exp_name.lower() or "qwen2.5-14b" in exp_name.lower():
        model_label = "Qwen2.5-14B-Instruct"
    elif "qwen25_7b" in exp_name.lower() or "qwen2.5-7b" in exp_name.lower():
        model_label = "Qwen2.5-7B-Instruct"
    elif "llama" in exp_name.lower():
        model_label = "Llama-3.1-8B-Instruct"

    if dataset == "folio":
        dataset_label = f"FOLIO-{n_problems}"
    elif dataset == "proofwriter":
        dataset_label = f"PW-{n_problems}"
    elif dataset == "logiqa":
        dataset_label = f"LogiQA-{n_problems}"

    result = {
        "exp_id": exp_name.split("_")[0] if "_" in exp_name else exp_name,
        "exp_dir": exp_name,
        "model": model_label,
        "dataset": dataset_label,
        "dataset_type": dataset,
        "kappa": round(kappa, 4),
        "eff_k": round(ek, 2),
        "K_used": K_used,
        "sc_accuracy": round(sc_acc, 2),
        "sica_accuracy": round(sica_acc, 2),
        "delta_pp": round(delta_pp, 2),
        "n_problems": n_problems,
        "n_valid_problems_kappa": n_valid_problems,
        "n_valid_votes": int(n_valid_votes),
        "n_total_votes": int(n_total_votes),
        "valid_vote_rate": round(n_valid_votes / n_total_votes, 4) if n_total_votes > 0 else 0,
        "n_excluded_empty": int(n_excluded),
        "n_nonstandard_mapped": int(n_nonstandard),
        "unanimous_rate_pct": round(unanimous, 1),
        "category_distribution_pct": cat_dist,
        "mean_valid_votes_per_q": round(float(n_per_q.mean()), 2) if n_problems > 0 else 0,
        "min_valid_votes": int(n_per_q.min()) if n_problems > 0 else 0,
        "max_valid_votes": int(n_per_q.max()) if n_problems > 0 else 0,
    }

    print(f"\n{'=' * 60}")
    print(f"  {exp_name}  ({dataset})")
    print(f"{'=' * 60}")
    print(f"  n_problems:          {n_problems}")
    print(f"  Mean valid votes/q:  {result['mean_valid_votes_per_q']}")
    print(f"  Valid vote rate:     {result['valid_vote_rate']}")
    print(f"  Non-standard->Unk:  {n_nonstandard}")
    print(f"  Excluded (empty):   {n_excluded}")
    print(f"  ---")
    print(f"  Fleiss' kappa:       {kappa:.4f}")
    print(f"  Eff-K (K={K_used}):       {ek:.2f}")
    print(f"  SC accuracy:        {sc_acc:.2f}%")
    print(f"  SICA accuracy:      {sica_acc:.2f}%")
    print(f"  Delta (pp):         {delta_pp:+.2f}")
    print(f"  Unanimous rate:     {unanimous:.1f}%")
    print(f"  Category dist:      {cat_dist}")

    return result


def main():
    parser = argparse.ArgumentParser(description="Unified Fleiss' kappa for SICA experiments")
    parser.add_argument("--results-dir", required=True, help="Path to results/ directory")
    parser.add_argument("--output", default="fleiss_kappa_unified.json", help="Output JSON path")
    parser.add_argument("--exp", nargs="*", help="Specific experiment dir names (default: all with intermediates/)")
    parser.add_argument("--raw", action="store_true", help="Skip T/F/U normalization (non-standard answers excluded, not mapped to Unknown)")
    parser.add_argument("--K", type=int, default=None, help="Override K for Eff-K computation (default: 12)")
    args = parser.parse_args()

    results_dir = args.results_dir

    if args.exp:
        exp_dirs = []
        for e in args.exp:
            d = os.path.join(results_dir, e, "intermediates")
            if os.path.isdir(d):
                exp_dirs.append((e, d))
            else:
                print(f"  WARN: {d} not found, skipping", file=sys.stderr)
    else:
        exp_dirs = []
        for entry in sorted(os.listdir(results_dir)):
            inter = os.path.join(results_dir, entry, "intermediates")
            if os.path.isdir(inter):
                exp_dirs.append((entry, inter))

    all_results = []
    for exp_name, inter_dir in exp_dirs:
        K_val = args.K if args.K else K_NOMINAL
        r = process_experiment(inter_dir, exp_name, raw=args.raw, K_used=K_val)
        if r is not None:
            all_results.append(r)

    output = {
        "formula": "Eff-K = K / (1 + (K-1) * kappa), K=12",
        "answer_normalization": "raw (non-standard excluded, not mapped)" if args.raw else "non-standard answers mapped to Unknown (FOLIO/PW) or excluded (LogiQA), None/empty excluded",
        "raw_mode": args.raw,
        "experiments": all_results,
    }

    out_path = args.output
    if not os.path.isabs(out_path):
        out_path = os.path.join(results_dir, out_path)

    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\n{'=' * 60}")
    print(f"Results saved to {out_path}")
    print(f"Total experiments processed: {len(all_results)}")


if __name__ == "__main__":
    main()
