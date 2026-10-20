"""Batch recalculate degeneracy using unified_metrics (constant-F1 gold-filtered)."""

import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from unified_metrics import (
    load_and_filter, compute_sample_f1s, compute_degeneracy, compute_greedy_f1
)

BASE = "/root/autodl-tmp/struct_self_consist_ie/output"

EXPERIMENTS = [
    # Qwen3-8B SciERC T=1.0
    {"label": "Qwen3-8B / SciERC / T=1.0 / seed=42",
     "dir": "exp_012_rerun_1024", "dataset": "scierc", "model": "Qwen3-8B",
     "T": 1.0, "seed": 42},
    {"label": "Qwen3-8B / SciERC / T=1.0 / seed=123",
     "dir": "exp_018_qwen_scierc_seed123", "dataset": "scierc", "model": "Qwen3-8B",
     "T": 1.0, "seed": 123},
    {"label": "Qwen3-8B / SciERC / T=1.0 / seed=456",
     "dir": "exp_018_qwen_scierc_seed456", "dataset": "scierc", "model": "Qwen3-8B",
     "T": 1.0, "seed": 456},

    # Qwen3-8B CoNLL T=1.0 N=16
    {"label": "Qwen3-8B / CoNLL / T=1.0 N=16 / seed=42",
     "dir": "exp_002_conll_n16", "dataset": "conll2003", "model": "Qwen3-8B",
     "T": 1.0, "seed": 42, "N": 16},
    {"label": "Qwen3-8B / CoNLL / T=1.0 N=16 / seed=123",
     "dir": "exp_002_conll_n16_seed123", "dataset": "conll2003", "model": "Qwen3-8B",
     "T": 1.0, "seed": 123, "N": 16},
    {"label": "Qwen3-8B / CoNLL / T=1.0 N=16 / seed=456",
     "dir": "exp_002_conll_n16_seed456", "dataset": "conll2003", "model": "Qwen3-8B",
     "T": 1.0, "seed": 456, "N": 16},

    # Qwen3-8B FewNERD T=1.0
    {"label": "Qwen3-8B / FewNERD / T=1.0 / seed=42",
     "dir": "exp_027_fewnerd_n16", "dataset": "fewnerd", "model": "Qwen3-8B",
     "T": 1.0, "seed": 42},
    {"label": "Qwen3-8B / FewNERD / T=1.0 / seed=123",
     "dir": "exp_021_fewnerd_n8_seed123", "dataset": "fewnerd", "model": "Qwen3-8B",
     "T": 1.0, "seed": 123},
    {"label": "Qwen3-8B / FewNERD / T=1.0 / seed=456",
     "dir": "exp_021_fewnerd_n8_seed456", "dataset": "fewnerd", "model": "Qwen3-8B",
     "T": 1.0, "seed": 456},

    # LLaMA3.1-8B SciERC
    {"label": "LLaMA3.1-8B / SciERC / T=1.0 / seed=42",
     "dir": "exp_018_llama_scierc_seed42_r1024", "dataset": "scierc", "model": "LLaMA3.1-8B",
     "T": 1.0, "seed": 42},
    {"label": "LLaMA3.1-8B / SciERC / T=1.0 / seed=123",
     "dir": "exp_018_llama_scierc_seed123", "dataset": "scierc", "model": "LLaMA3.1-8B",
     "T": 1.0, "seed": 123},
    {"label": "LLaMA3.1-8B / SciERC / T=1.0 / seed=456",
     "dir": "exp_018_llama_scierc_seed456_r1024", "dataset": "scierc", "model": "LLaMA3.1-8B",
     "T": 1.0, "seed": 456},

    # LLaMA3.1-8B CoNLL
    {"label": "LLaMA3.1-8B / CoNLL / T=1.0 N=16 / seed=42",
     "dir": "exp_017_llama_conll_n16_r1024", "dataset": "conll2003", "model": "LLaMA3.1-8B",
     "T": 1.0, "seed": 42, "N": 16},
    {"label": "LLaMA3.1-8B / CoNLL / T=1.0 N=16 / seed=123",
     "dir": "exp_017_llama_conll_n16_s123_r1024", "dataset": "conll2003", "model": "LLaMA3.1-8B",
     "T": 1.0, "seed": 123, "N": 16},
    {"label": "LLaMA3.1-8B / CoNLL / T=1.0 N=16 / seed=456",
     "dir": "exp_017_llama_conll_n16_s456_r1024", "dataset": "conll2003", "model": "LLaMA3.1-8B",
     "T": 1.0, "seed": 456, "N": 16},

    # T ablation (SciERC, Qwen3-8B, seed=42)
    {"label": "Qwen3-8B / SciERC / T=0.5 / seed=42 (ablation)",
     "dir": "exp_026_t05", "dataset": "scierc", "model": "Qwen3-8B",
     "T": 0.5, "seed": 42},
    {"label": "Qwen3-8B / SciERC / T=0.8 / seed=42 (ablation)",
     "dir": "exp_026_t08", "dataset": "scierc", "model": "Qwen3-8B",
     "T": 0.8, "seed": 42},
    {"label": "Qwen3-8B / SciERC / T=1.2 / seed=42 (ablation)",
     "dir": "exp_026_t12", "dataset": "scierc", "model": "Qwen3-8B",
     "T": 1.2, "seed": 42},

    # 4B model experiments
    {"label": "Qwen3-4B / SciERC / T=1.0 / seed=42",
     "dir": "exp_qwen3_4b_scierc_scs_inference", "dataset": "scierc", "model": "Qwen3-4B",
     "T": 1.0, "seed": 42},
    {"label": "Qwen3-4B / CoNLL / T=1.0 / seed=42",
     "dir": "exp_qwen3_4b_conll_scs_inference_v2", "dataset": "conll2003", "model": "Qwen3-4B",
     "T": 1.0, "seed": 42},
]


def get_old_report_value(exp_dir):
    """Try to extract old sample_f1_pct_zero from report.json."""
    report_path = os.path.join(exp_dir, "report.json")
    if not os.path.exists(report_path):
        return None
    try:
        with open(report_path) as f:
            r = json.load(f)
        # Check NER-specific or flat key
        for key in ["ner_sample_f1_pct_zero", "sample_f1_pct_zero"]:
            if key in r:
                return r[key]
    except Exception:
        pass
    return None


def process_experiment(exp):
    exp_dir = os.path.join(BASE, exp["dir"])
    samples_path = os.path.join(exp_dir, "samples.jsonl")

    if not os.path.exists(samples_path):
        return {**exp, "status": "MISSING", "error": f"{samples_path} not found"}

    try:
        instances = load_and_filter(samples_path, gold_filter=True)
    except Exception as e:
        return {**exp, "status": "ERROR", "error": str(e)}

    n_total = len(instances)
    n_degen = 0
    greedy_f1s = []

    for inst in instances:
        f1s = compute_sample_f1s(inst)
        if compute_degeneracy(f1s):
            n_degen += 1
        greedy_f1s.append(compute_greedy_f1(inst))

    degen_pct = 100.0 * n_degen / n_total if n_total > 0 else 0.0
    mean_greedy_f1 = sum(greedy_f1s) / len(greedy_f1s) if greedy_f1s else 0.0

    old_val = get_old_report_value(exp_dir)

    return {
        **exp,
        "status": "OK",
        "n_instances": n_total,
        "n_degenerate": n_degen,
        "degen_pct_unified": round(degen_pct, 2),
        "greedy_f1": round(mean_greedy_f1 * 100, 2),
        "old_sample_f1_pct_zero": round(old_val, 2) if old_val is not None else None,
        "delta": round(degen_pct - old_val, 2) if old_val is not None else None,
    }


if __name__ == "__main__":
    results = []
    for exp in EXPERIMENTS:
        print(f"Processing: {exp['label']} ...", flush=True)
        r = process_experiment(exp)
        results.append(r)
        if r["status"] == "OK":
            old_str = f"{r['old_sample_f1_pct_zero']:.1f}%" if r['old_sample_f1_pct_zero'] is not None else "N/A"
            print(f"  => Degen(unified)={r['degen_pct_unified']:.1f}%  "
                  f"Old_pct_zero={old_str}  "
                  f"Greedy_F1={r['greedy_f1']:.1f}%  "
                  f"N={r['n_instances']}")
        else:
            print(f"  => {r['status']}: {r.get('error', '')}")

    # Save JSON
    out_dir = os.path.join(BASE, "unified_degeneracy_audit")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "degeneracy_recalc_results.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {out_path}")

    # Print summary table
    print("\n" + "=" * 120)
    print(f"{'Label':<55} {'N':>5} {'Degen%(unified)':>16} {'OldPctZero':>11} {'Delta':>7} {'Greedy_F1':>10}")
    print("-" * 120)
    for r in results:
        if r["status"] != "OK":
            print(f"{r['label']:<55} {'MISSING/ERROR'}")
            continue
        old_str = f"{r['old_sample_f1_pct_zero']:.1f}%" if r['old_sample_f1_pct_zero'] is not None else "N/A"
        delta_str = f"{r['delta']:+.1f}" if r['delta'] is not None else "N/A"
        print(f"{r['label']:<55} {r['n_instances']:>5} {r['degen_pct_unified']:>15.1f}% {old_str:>11} {delta_str:>7} {r['greedy_f1']:>9.1f}%")
    print("=" * 120)
