"""Generate EDCR cross-method diagnostic table from all eval results.

Usage (from ./outputs
  python -m freige.eval.cross_method_table
"""
import json
import statistics
from pathlib import Path

EVAL_CONFIGS = [
    {"name": "SFT baseline (quant)", "path": "./outputs"},
    {"name": "SFT baseline (noquant)", "path": "./outputs/eval_results"},
    {"name": "SFT no-evidence", "path": "./outputs/eval_results"},
    {"name": "RSFT-CED (s42, 3ep)", "path": "./outputs/eval_results"},
    {"name": "RSFT-CED (s43, 3ep)", "path": "./outputs/eval_results"},
    {"name": "RSFT-CED (s44, 3ep)", "path": "./outputs/eval_results"},
    {"name": "RSFT-CED (r2a, 1ep)", "path": "./outputs/eval_results"},
    {"name": "RSFT-CED (r2b, a=32)", "path": "./outputs/eval_results"},
    {"name": "RSFT-flatNLI (s42)", "path": "./outputs/eval_results"},
    {"name": "CED-reranker (N=8)", "path": "./outputs/eval_results",
     "key": "ced_reranker"},
    {"name": "GRPO bf16 (G=8, ckpt100)", "path": "./outputs/eval_results"},
    {"name": "DPO-CED (ckpt501)", "path": "./outputs/eval_results"},
]


def load_metrics(cfg):
    path = Path(cfg["path"])
    if not path.exists():
        return None
    with open(path) as f:
        data = json.load(f)
    if "key" in cfg:
        data = data[cfg["key"]]
    return data


def get_val(m, *keys):
    for k in keys:
        if k in m:
            return m[k]
    return 0


def main():
    results = []
    for cfg in EVAL_CONFIGS:
        m = load_metrics(cfg)
        if m is None:
            print(f"MISSING: {cfg['name']} -> {cfg['path']}")
            continue
        results.append((cfg["name"], m))

    if not results:
        print("No results found!")
        return

    sft_f1 = get_val(results[0][1], "f1", "rel_f1")
    sft_edcr = get_val(results[0][1], "edcr")

    header = (f"{'Method':<28} {'rel_f1':>7} {'Δf1':>8} {'evi_f1':>7} "
              f"{'EDCR':>7} {'ΔEDCR':>8} {'evi_j':>7} {'preds':>6} {'trunc':>6}")
    print(header)
    print("-" * len(header))

    table_data = []
    for name, m in results:
        f1 = get_val(m, "f1", "rel_f1")
        evi_f1 = get_val(m, "evi_f1")
        edcr = get_val(m, "edcr")
        evi_joint = get_val(m, "evi_f1_joint")
        delta_f1 = (f1 - sft_f1) * 100
        delta_edcr = (edcr - sft_edcr) * 100
        preds = get_val(m, "n_predictions", "pred_count")
        trunc = m.get("n_truncated")
        trunc_str = str(trunc) if trunc is not None else "-"

        print(f"{name:<28} {f1:>7.4f} {delta_f1:>+7.2f}p {evi_f1:>7.4f} "
              f"{edcr:>7.4f} {delta_edcr:>+7.2f}p {evi_joint:>7.4f} {preds:>6} {trunc_str:>6}")

        table_data.append({
            "method": name,
            "rel_f1": round(f1, 4),
            "evi_f1": round(evi_f1, 4),
            "edcr": round(edcr, 4),
            "evi_f1_joint": round(evi_joint, 4),
            "delta_rel_f1_pp": round(delta_f1, 2),
            "delta_edcr_pp": round(delta_edcr, 2),
            "precision": round(get_val(m, "precision"), 4),
            "recall": round(get_val(m, "recall"), 4),
            "n_predictions": preds,
            "n_truncated": trunc,
        })

    # 3-seed aggregate
    seed_names = {"RSFT-CED (s42, 3ep)", "RSFT-CED (s43, 3ep)", "RSFT-CED (s44, 3ep)"}
    rsft_seeds = [(n, m) for n, m in results if n in seed_names]
    if len(rsft_seeds) == 3:
        print()
        print("--- RSFT-CED 3-seed (s42/s43/s44) ---")
        for k, label in [("f1", "rel_f1"), ("evi_f1", "evi_f1"), ("edcr", "EDCR"), ("evi_f1_joint", "evi_j")]:
            vals = [get_val(m, k) for _, m in rsft_seeds]
            if all(v > 0 for v in vals):
                mean_v = statistics.mean(vals)
                std_v = statistics.stdev(vals)
                print(f"  {label:>7} = {mean_v:.4f} ± {std_v:.4f}")

        table_data.append({
            "method": "RSFT-CED 3-seed mean",
            "rel_f1": round(statistics.mean([get_val(m, "f1") for _, m in rsft_seeds]), 4),
            "rel_f1_std": round(statistics.stdev([get_val(m, "f1") for _, m in rsft_seeds]), 4),
            "evi_f1": round(statistics.mean([get_val(m, "evi_f1") for _, m in rsft_seeds]), 4),
            "evi_f1_std": round(statistics.stdev([get_val(m, "evi_f1") for _, m in rsft_seeds]), 4),
            "edcr": round(statistics.mean([get_val(m, "edcr") for _, m in rsft_seeds]), 4),
            "edcr_std": round(statistics.stdev([get_val(m, "edcr") for _, m in rsft_seeds]), 4),
        })

    output_path = Path("./outputs/eval_results")
    with open(output_path, "w") as f:
        json.dump(table_data, f, indent=2, ensure_ascii=False)
    print(f"\nExported -> {output_path}")


if __name__ == "__main__":
    main()
