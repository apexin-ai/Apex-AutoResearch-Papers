#!/usr/bin/env python3
"""Generate tab_math500.tex and summary.json from registry or local JSON files."""

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

REGISTRY_PATH = Path(__file__).resolve().parent.parent / "registry.yaml"
TABLE_OUTPUT = Path(__file__).resolve().parent.parent / "paper" / "tables" / "tab_math500.tex"
SUMMARY_OUTPUT = Path(__file__).resolve().parent / "summary_math500.json"

# ── Experiment definitions ──────────────────────────────────────────────

METHOD_COMPARISON_20 = {
    "Dense (unpruned)": {
        "sft": "eval_math500_dense_unpruned",
        "grpo": "eval_math500_grpo_unpruned",
    },
    "Standard": {
        "sft": "eval_math500_sft_standard_20_fixed_v4",
        "grpo": "eval_math500_grpo_standard_20_fixed",
    },
    "Random": {
        "sft": "eval_math500_sft_random_20_fixed_v3",
        "grpo": "eval_math500_grpo_random_20_fixed",
    },
    "CKA-only": {
        "sft": "eval_math500_sft_cka_only_20_fixed_v2",
        "grpo": "eval_math500_grpo_cka_only_20_fixed",
    },
    r"RASP ($\alpha\!=\!1.0$)": {
        "sft": "eval_math500_sft_rasp_alpha1p0_20_fixed",
        "grpo": "eval_math500_grpo_rasp_alpha1p0_20_fixed",
    },
}

ALPHA_SWEEP = {
    "0.5": {
        "sft": "eval_math500_sft_rasp_alpha0p5_20_fixed",
        "grpo": "eval_math500_grpo_rasp_alpha0p5_20_fixed",
    },
    "1.0": {
        "sft": "eval_math500_sft_rasp_alpha1p0_20_fixed",
        "grpo": "eval_math500_grpo_rasp_alpha1p0_20_fixed",
    },
    "2.0": {
        "sft": "eval_math500_sft_rasp_alpha2p0_20_fixed",
        "grpo": "eval_math500_grpo_rasp_alpha2p0_20_fixed",
    },
    "3.0": {
        "sft": "eval_math500_sft_rasp_alpha3p0_20_fixed",
        "grpo": "eval_math500_grpo_alpha3p0_20_fixed",
    },
    "4.0": {
        "sft": "eval_math500_sft_rasp_alpha4p0_20_fixed",
        "grpo": "eval_math500_grpo_rasp_alpha4p0_20_fixed",
    },
}

SPARSITY_25 = {
    "Standard (25\\%)": {
        "sft": "eval_math500_sft_standard_25_fixed_v2",
        "grpo": None,
    },
    "CKA-only (25\\%)": {
        "sft": "eval_math500_sft_cka_only_25_fixed",
        "grpo": "eval_math500_grpo_cka_only_25_fixed",
    },
}


def all_exp_ids():
    ids = set()
    for group in [METHOD_COMPARISON_20, ALPHA_SWEEP, SPARSITY_25]:
        for row in group.values():
            for v in row.values():
                if v:
                    ids.add(v)
    return ids


# ── Data loading ────────────────────────────────────────────────────────

def load_registry():
    with open(REGISTRY_PATH) as f:
        reg = yaml.safe_load(f)
    return reg.get("experiments", {})


def extract_from_registry(experiments, exp_id):
    exp = experiments.get(exp_id)
    if not exp:
        return None
    metrics = exp.get("metrics", {})
    status = exp.get("status", "UNKNOWN")
    if status != "DONE" or not metrics:
        return {"status": status, "accuracy": None, "truncation_rate": None}

    accuracy = metrics.get("accuracy") or metrics.get("math500_acc")
    trunc = metrics.get("truncated_pct")
    if trunc is None:
        n_total = metrics.get("num_total") or metrics.get("n_total") or metrics.get("N")
        truncated = metrics.get("truncated")
        if truncated is not None and n_total:
            trunc = truncated / n_total
        else:
            natural_eos = metrics.get("natural_eos_pct")
            if natural_eos is not None:
                trunc = 1.0 - natural_eos

    return {"status": "done", "accuracy": accuracy, "truncation_rate": trunc}


def load_json_results(json_dir):
    results = {}
    json_dir = Path(json_dir)
    for f in json_dir.glob("eval_math500_*.json"):
        exp_id = f.stem
        with open(f) as fh:
            data = json.load(fh)
        accuracy = data.get("accuracy")
        trunc = data.get("truncated_pct") or data.get("truncation_rate")
        if trunc is None:
            n_total = data.get("num_total") or data.get("n_total") or data.get("N")
            truncated = data.get("truncated")
            if truncated is not None and n_total:
                trunc = truncated / n_total
        results[exp_id] = {"status": "done", "accuracy": accuracy, "truncation_rate": trunc}
    return results


def cross_validate(registry_data, json_data, exp_id):
    reg = registry_data.get(exp_id)
    js = json_data.get(exp_id)
    if not reg or not js:
        return True
    if reg.get("accuracy") is None or js.get("accuracy") is None:
        return True
    return abs(reg["accuracy"] - js["accuracy"]) < 0.001


# ── LaTeX generation ────────────────────────────────────────────────────

def fmt_acc(val):
    if val is None:
        return "--"
    return f"{val*100:.1f}"


def fmt_trunc(val):
    if val is None:
        return "--"
    return f"{val*100:.1f}"


def make_row(label, data, sft_id, grpo_id, best_sft_acc=None, best_grpo_acc=None):
    sft = data.get(sft_id) if sft_id else None
    grpo = data.get(grpo_id) if grpo_id else None

    sft_acc = sft["accuracy"] if sft and sft.get("accuracy") is not None else None
    sft_trunc = sft["truncation_rate"] if sft and sft.get("truncation_rate") is not None else None
    grpo_acc = grpo["accuracy"] if grpo and grpo.get("accuracy") is not None else None
    grpo_trunc = grpo["truncation_rate"] if grpo and grpo.get("truncation_rate") is not None else None

    sft_acc_str = fmt_acc(sft_acc)
    grpo_acc_str = fmt_acc(grpo_acc)

    if best_sft_acc is not None and sft_acc is not None and abs(sft_acc - best_sft_acc) < 1e-6:
        sft_acc_str = r"\textbf{" + sft_acc_str + "}"
    if best_grpo_acc is not None and grpo_acc is not None and abs(grpo_acc - best_grpo_acc) < 1e-6:
        grpo_acc_str = r"\textbf{" + grpo_acc_str + "}"

    if grpo_id is None:
        grpo_acc_str = "--"
        grpo_trunc_str = "--"
    else:
        grpo_trunc_str = fmt_trunc(grpo_trunc)

    return f"    {label} & {sft_acc_str} & {fmt_trunc(sft_trunc)} & {grpo_acc_str} & {grpo_trunc_str} \\\\"


def find_best(data, group, col):
    best = None
    for row in group.values():
        eid = row.get(col)
        if not eid:
            continue
        entry = data.get(eid)
        if entry and entry.get("accuracy") is not None:
            if best is None or entry["accuracy"] > best:
                best = entry["accuracy"]
    return best


def generate_latex(data):
    lines = []
    lines.append(r"\begin{table}[t]")
    lines.append(r"\centering")
    lines.append(r"\small")
    lines.append(r"\caption{MATH-500 accuracy (\%) and truncation rate (\%) under different pruning methods and recovery strategies. Sparsity = 20\% unless noted. Best pruned-model accuracy per column in \textbf{bold}.}")
    lines.append(r"\label{tab:math500}")
    lines.append(r"\begin{tabular}{l cc cc}")
    lines.append(r"\toprule")
    lines.append(r"& \multicolumn{2}{c}{\textbf{Post-SFT}} & \multicolumn{2}{c}{\textbf{Post-GRPO}} \\")
    lines.append(r"\cmidrule(lr){2-3} \cmidrule(lr){4-5}")
    lines.append(r"Method & Acc & Trunc & Acc & Trunc \\")
    lines.append(r"\midrule")

    # Dense baseline (no bold competition)
    dense_row = METHOD_COMPARISON_20["Dense (unpruned)"]
    lines.append(make_row(
        r"Dense (unpruned)",
        data, dense_row["sft"], dense_row["grpo"]
    ))
    lines.append(r"\midrule")

    # Method comparison (20%) - find best among pruned methods only
    pruned_methods = {k: v for k, v in METHOD_COMPARISON_20.items() if k != "Dense (unpruned)"}
    best_sft = find_best(data, pruned_methods, "sft")
    best_grpo = find_best(data, pruned_methods, "grpo")

    for label, ids in pruned_methods.items():
        lines.append(make_row(label, data, ids["sft"], ids["grpo"], best_sft, best_grpo))

    lines.append(r"\midrule")
    lines.append(r"\multicolumn{5}{l}{\textit{Dose-response ($\alpha$ sweep, 20\% sparsity)}} \\")

    best_sft_alpha = find_best(data, ALPHA_SWEEP, "sft")
    best_grpo_alpha = find_best(data, ALPHA_SWEEP, "grpo")

    for alpha, ids in ALPHA_SWEEP.items():
        label = rf"$\alpha = {alpha}$"
        lines.append(make_row(label, data, ids["sft"], ids["grpo"], best_sft_alpha, best_grpo_alpha))

    lines.append(r"\midrule")
    lines.append(r"\multicolumn{5}{l}{\textit{25\% sparsity}} \\")

    best_sft_25 = find_best(data, SPARSITY_25, "sft")
    best_grpo_25 = find_best(data, SPARSITY_25, "grpo")

    for label, ids in SPARSITY_25.items():
        lines.append(make_row(label, data, ids["sft"], ids["grpo"], best_sft_25, best_grpo_25))

    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")

    return "\n".join(lines) + "\n"


# ── Summary JSON ────────────────────────────────────────────────────────

def generate_summary(data, source):
    expected = all_exp_ids()
    experiments = {}
    missing = []

    for eid in sorted(expected):
        entry = data.get(eid)
        if entry and entry.get("accuracy") is not None:
            experiments[eid] = {
                "accuracy": entry["accuracy"],
                "truncation_rate": entry.get("truncation_rate"),
                "registry_match": True,
                "status": "done",
            }
        else:
            status = entry["status"] if entry else "not_found"
            missing.append(eid)
            experiments[eid] = {
                "accuracy": None,
                "truncation_rate": None,
                "registry_match": None,
                "status": status,
            }

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": source,
        "experiments": experiments,
        "missing": missing,
        "total_done": len(expected) - len(missing),
        "total_expected": len(expected),
    }


# ── Main ────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Generate MATH-500 LaTeX table")
    parser.add_argument("--source", choices=["registry", "json"], default="registry")
    parser.add_argument("--json-dir", type=str, help="Directory with eval_math500_*.json files")
    parser.add_argument("--cross-validate", action="store_true",
                        help="Cross-validate registry vs JSON (requires both --source registry and --json-dir)")
    parser.add_argument("--output-tex", type=str, default=str(TABLE_OUTPUT))
    parser.add_argument("--output-summary", type=str, default=str(SUMMARY_OUTPUT))
    args = parser.parse_args()

    if args.source == "json" and not args.json_dir:
        print("ERROR: --json-dir required when --source json", file=sys.stderr)
        sys.exit(1)

    # Load data
    registry_experiments = load_registry()
    data = {}

    if args.source == "registry":
        for eid in all_exp_ids():
            result = extract_from_registry(registry_experiments, eid)
            if result:
                data[eid] = result
    else:
        data = load_json_results(args.json_dir)

    # Cross-validation
    if args.cross_validate and args.json_dir:
        json_data = load_json_results(args.json_dir) if args.source == "registry" else data
        reg_data = {}
        for eid in all_exp_ids():
            result = extract_from_registry(registry_experiments, eid)
            if result:
                reg_data[eid] = result

        errors = []
        for eid in all_exp_ids():
            if not cross_validate(reg_data, json_data, eid):
                r_acc = reg_data.get(eid, {}).get("accuracy")
                j_acc = json_data.get(eid, {}).get("accuracy")
                errors.append(f"  {eid}: registry={r_acc}, json={j_acc}")
        if errors:
            print("CROSS-VALIDATION FAILED:", file=sys.stderr)
            for e in errors:
                print(e, file=sys.stderr)
            sys.exit(1)
        print(f"Cross-validation passed for {len(all_exp_ids())} experiments.")

    # Generate outputs
    tex = generate_latex(data)
    os.makedirs(os.path.dirname(args.output_tex), exist_ok=True)
    with open(args.output_tex, "w") as f:
        f.write(tex)
    print(f"Wrote {args.output_tex}")

    summary = generate_summary(data, args.source)
    os.makedirs(os.path.dirname(args.output_summary) if os.path.dirname(args.output_summary) else ".", exist_ok=True)
    with open(args.output_summary, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"Wrote {args.output_summary}")

    print(f"\nDone: {summary['total_done']}/{summary['total_expected']} experiments have results.")
    if summary["missing"]:
        print("Missing:")
        for m in summary["missing"]:
            print(f"  - {m}")


if __name__ == "__main__":
    main()
