#!/usr/bin/env python3
"""Compile dose_response CSV from post-fix 5method_leadlag.json files.

Usage: python3 compile_dose_response.py <server_name> <output_csv>

Reads all results/*/analysis/5method_leadlag.json files,
filters for post-D105 (true_3sigma_d105 threshold),
extracts forward/reverse significance counts using:
  - diff_xcorr, perm_granger: significant_fdr
  - naive_xcorr, threshold_onset, ty_granger: significant
"""
import json
import csv
import os
import re
import sys
from pathlib import Path

SERVER = sys.argv[1] if len(sys.argv) > 1 else "unknown"
OUT_CSV = sys.argv[2] if len(sys.argv) > 2 else "/tmp/dose_response_partial.csv"
RESULTS_DIR = Path("/root/autodl-tmp/distrib_canary_collapse/results")

FIELDS = [
    "category", "experiment", "alpha", "seed", "T", "domain", "precision", "model",
    "n_pairs",
    "naive_fwd", "naive_rev",
    "diffxcorr_fwd_fdr", "diffxcorr_rev_fdr",
    "threshold_fwd", "threshold_rev",
    "permg_fwd_fdr", "permg_rev_fdr",
    "ty_fwd", "ty_rev",
    "naive_rate", "diff_rate", "threshold_rate", "permg_rate", "ty_rate",
    "consensus_ge3", "consensus_ge4", "consensus_ge5",
    "server",
]


def find_jsons():
    results = []
    for jp in RESULTS_DIR.rglob("analysis/5method_leadlag.json"):
        if "analysis_mauve" in str(jp):
            continue
        results.append(jp)
    return sorted(results)


def extract_model(exp_name):
    patterns = [
        (r"(?:^|/)gen_wiki_(gpt2m)", 1),
        (r"(?:^|/)gen_(opt13b)", 1),
        (r"(smollm3_\d+b)", 1),
        (r"(pythia\d+[bm])", 1),
        (r"(qwen\d+_\d+b)", 1),
        (r"(gpt2m)", 1),
        (r"(opt\d+b)", 1),
        (r"^(\d+b)_", 1),
    ]
    for pat, grp in patterns:
        m = re.search(pat, exp_name)
        if m:
            name = m.group(grp)
            if name == "opt13b":
                return "opt1.3b"
            return name
    return "gpt2"


def infer_metadata(json_path, meta):
    rel = json_path.relative_to(RESULTS_DIR)
    parts = rel.parts

    if len(parts) == 3:
        exp_name = parts[0]
        if exp_name.startswith("gen_"):
            category = "generalize"
        else:
            category = "unknown"
    elif len(parts) >= 4:
        category = parts[0]
        exp_name = parts[1]
    else:
        category = "unknown"
        exp_name = parts[0] if parts else "unknown"

    domain = "c4" if re.search(r"(?:^|_)c4(?:_|$)", exp_name) else "wikitext"

    if "_bf16" in exp_name:
        precision = "bf16"
    else:
        precision = "fp32"

    if category in ("generalize", "scale_check", "scale"):
        model = extract_model(exp_name)
    elif category == "unknown" and exp_name.startswith("gen_"):
        category = "generalize"
        model = extract_model(exp_name)
    else:
        model = "gpt2"

    return category, exp_name, domain, model, precision


def extract_row(json_path, server):
    with open(json_path) as f:
        data = json.load(f)

    meta = data["meta"]
    pairs = data["pairs"]

    tc = meta.get("threshold_criterion", "")
    if tc != "true_3sigma_d105":
        return None

    alpha = meta["alpha"]
    seed = meta["seed"]
    n_gens = meta["n_gens"]
    T = n_gens - 1

    category, exp_name, domain, model, precision = infer_metadata(json_path, meta)
    n_pairs = len(pairs)

    naive_fwd = naive_rev = 0
    diff_fwd = diff_rev = 0
    thr_fwd = thr_rev = 0
    pg_fwd = pg_rev = 0
    ty_fwd_c = ty_rev_c = 0
    K_values = []

    for p in pairs:
        fwd, rev = p["forward"], p["reverse"]

        # D111: xcorr methods require peak_lag < 0 for forward causation
        fwd_naive = fwd.get("naive_xcorr", {})
        nf = bool(fwd_naive.get("significant", False)) and fwd_naive.get("peak_lag", 0) < 0
        fwd_diff = fwd.get("diff_xcorr", {})
        df = bool(fwd_diff.get("significant_fdr", False)) and fwd_diff.get("peak_lag", 0) < 0
        tf = bool(fwd.get("threshold_onset", {}).get("significant", False))
        pf = bool(fwd.get("perm_granger", {}).get("significant_fdr", False))
        yf = bool(fwd.get("ty_granger", {}).get("significant", False))

        naive_fwd += nf
        diff_fwd += df
        thr_fwd += tf
        pg_fwd += pf
        ty_fwd_c += yf

        rev_naive = rev.get("naive_xcorr", {})
        naive_rev += bool(rev_naive.get("significant", False)) and rev_naive.get("peak_lag", 0) < 0
        rev_diff = rev.get("diff_xcorr", {})
        diff_rev += bool(rev_diff.get("significant_fdr", False)) and rev_diff.get("peak_lag", 0) < 0
        thr_rev += bool(rev.get("threshold_onset", {}).get("significant", False))
        pg_rev += bool(rev.get("perm_granger", {}).get("significant_fdr", False))
        ty_rev_c += bool(rev.get("ty_granger", {}).get("significant", False))

        K_values.append(sum([nf, df, tf, pf, yf]))

    def rate(count):
        return round(count / n_pairs, 4) if n_pairs > 0 else 0

    return {
        "category": category,
        "experiment": exp_name,
        "alpha": alpha,
        "seed": seed,
        "T": T,
        "domain": domain,
        "precision": precision,
        "model": model,
        "n_pairs": n_pairs,
        "naive_fwd": naive_fwd,
        "naive_rev": naive_rev,
        "diffxcorr_fwd_fdr": diff_fwd,
        "diffxcorr_rev_fdr": diff_rev,
        "threshold_fwd": thr_fwd,
        "threshold_rev": thr_rev,
        "permg_fwd_fdr": pg_fwd,
        "permg_rev_fdr": pg_rev,
        "ty_fwd": ty_fwd_c,
        "ty_rev": ty_rev_c,
        "naive_rate": rate(naive_fwd),
        "diff_rate": rate(diff_fwd),
        "threshold_rate": rate(thr_fwd),
        "permg_rate": rate(pg_fwd),
        "ty_rate": rate(ty_fwd_c),
        "consensus_ge3": sum(1 for k in K_values if k >= 3),
        "consensus_ge4": sum(1 for k in K_values if k >= 4),
        "consensus_ge5": sum(1 for k in K_values if k >= 5),
        "server": server,
    }


def main():
    jsons = find_jsons()
    print(f"Found {len(jsons)} JSON files", file=sys.stderr)

    rows = []
    skipped = []
    for jp in jsons:
        try:
            row = extract_row(jp, SERVER)
        except Exception as e:
            print(f"ERROR processing {jp}: {e}", file=sys.stderr)
            skipped.append(str(jp))
            continue
        if row is None:
            skipped.append(str(jp))
            continue
        rows.append(row)

    if skipped:
        print(f"Skipped {len(skipped)} files (pre-D105 or error):", file=sys.stderr)
        for s in skipped:
            print(f"  {s}", file=sys.stderr)

    rows.sort(key=lambda r: (r["category"], r["alpha"], r["seed"], r["experiment"]))

    with open(OUT_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {OUT_CSV}", file=sys.stderr)


if __name__ == "__main__":
    main()
