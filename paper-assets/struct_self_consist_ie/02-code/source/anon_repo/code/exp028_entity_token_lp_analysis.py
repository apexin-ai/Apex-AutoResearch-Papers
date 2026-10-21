"""exp-028: Entity-Token LP Analysis

Compare entity-only LP vs full-sequence LP to test whether
LP compression is caused by format token dilution or is model-intrinsic.

Uses token-level logprob data from exp_entity_token_lp/scierc/.
"""

import json
import sys
import numpy as np
from pathlib import Path
from collections import OrderedDict
from scipy.stats import spearmanr

sys.path.insert(0, str(Path(__file__).resolve().parent))
from entity_token_lp_full_analysis import classify_tokens, mean_lp_for_labels
from evaluation import per_instance_f1


def load_data(path):
    with open(path) as f:
        return [json.loads(l) for l in f if l.strip()]


def compute_span_f1(pred_ents, gold_ents):
    pred_set = {(e["text"], e["type"], e["start"], e["end"]) for e in pred_ents}
    gold_set = {(e["text"], e["type"], e["start"], e["end"]) for e in gold_ents}
    tp = len(pred_set & gold_set)
    p = tp / max(len(pred_set), 1)
    r = tp / max(len(gold_set), 1)
    return 2 * p * r / max(p + r, 1e-10)


def analyze(data_path, output_dir):
    data = load_data(data_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    LP_VARIANTS = {
        "full": None,
        "entity_text": {"entity_text"},
        "entity_type": {"entity_type"},
        "entity_text_type": {"entity_text", "entity_type"},
        "entity_all": {"entity_text", "entity_type", "entity_span"},
        "schema_only": {"schema"},
        "nonentity": {"entity_text", "entity_type", "entity_span", "relation"},
    }

    instance_records = []
    sample_records = []
    skipped_no_gold = 0
    skipped_no_tokens = 0

    for inst in data:
        gold_ents = inst["gold"].get("entities", [])
        if not gold_ents:
            skipped_no_gold += 1
            continue

        samples = inst["samples"]
        if len(samples) < 2:
            continue

        has_tokens = all(s.get("token_logprobs") and s.get("token_texts") for s in samples)
        if not has_tokens:
            skipped_no_tokens += 1
            continue

        sample_lps = {k: [] for k in LP_VARIANTS}
        sample_f1s = []

        for si, s in enumerate(samples):
            tt = s["token_texts"]
            tl = s["token_logprobs"]
            labels = classify_tokens(tt)
            f1 = compute_span_f1(s.get("entities", []), gold_ents)
            sample_f1s.append(f1)

            sample_lps["full"].append(s["mean_logprob"])
            for key, label_set in LP_VARIANTS.items():
                if key == "full":
                    continue
                lp = mean_lp_for_labels(tl, labels, label_set)
                sample_lps[key].append(lp if lp is not None else s["mean_logprob"])

            sample_records.append({
                "instance_id": inst["id"],
                "sample_idx": si,
                "f1": f1,
                **{f"{k}_lp": sample_lps[k][-1] for k in LP_VARIANTS},
            })

        greedy_f1 = compute_span_f1(
            inst["greedy"].get("entities", []), gold_ents
        )

        inst_rec = {
            "id": inst["id"],
            "n_samples": len(samples),
            "greedy_f1": greedy_f1,
            "oracle_f1": max(sample_f1s),
            "mean_sample_f1": float(np.mean(sample_f1s)),
        }

        for key in LP_VARIANTS:
            lps = np.array(sample_lps[key])
            inst_rec[f"{key}_lp_range"] = float(np.max(lps) - np.min(lps))
            inst_rec[f"{key}_lp_std"] = float(np.std(lps))
            if len(set(lps)) > 1 and len(set(sample_f1s)) > 1:
                rho, _ = spearmanr(lps, sample_f1s)
                inst_rec[f"{key}_within_rho"] = float(rho) if not np.isnan(rho) else 0.0
            else:
                inst_rec[f"{key}_within_rho"] = 0.0

        instance_records.append(inst_rec)

    n_valid = len(instance_records)
    print(f"Valid instances: {n_valid} (skipped {skipped_no_gold} no-gold, {skipped_no_tokens} no-tokens)")

    greedy_f1 = float(np.mean([r["greedy_f1"] for r in instance_records]))
    oracle_f1 = float(np.mean([r["oracle_f1"] for r in instance_records]))

    results = {
        "experiment": "exp_028_entity_token_lp",
        "dataset": "scierc",
        "data_source": "exp_entity_token_lp/scierc/samples.jsonl",
        "n_valid": n_valid,
        "n_skipped_no_gold": skipped_no_gold,
        "n_skipped_no_tokens": skipped_no_tokens,
        "greedy_f1": greedy_f1,
        "oracle_f1": oracle_f1,
        "variants": {},
    }

    print(f"\nGreedy F1: {greedy_f1:.4f}  |  Oracle F1: {oracle_f1:.4f}")
    print(f"\n{'LP Variant':<20} {'W-Range':>8} {'W-Rho':>8} {'G-Rho':>8} {'Sel.F1':>8} {'D.Greedy':>9}")
    print("-" * 75)

    all_f1 = np.array([r["f1"] for r in sample_records])

    for key in LP_VARIANTS:
        ranges = [r[f"{key}_lp_range"] for r in instance_records]
        within_rhos = [r[f"{key}_within_rho"] for r in instance_records]

        all_lps = np.array([r[f"{key}_lp"] for r in sample_records])
        g_rho, g_p = spearmanr(all_lps, all_f1)

        inst_groups = OrderedDict()
        for r in sample_records:
            iid = r["instance_id"]
            if iid not in inst_groups:
                inst_groups[iid] = []
            inst_groups[iid].append(r)

        sel_f1s = []
        for iid, group in inst_groups.items():
            best_idx = max(range(len(group)), key=lambda j: group[j][f"{key}_lp"])
            sel_f1s.append(group[best_idx]["f1"])
        sel_f1 = float(np.mean(sel_f1s))

        variant_result = {
            "within_range_median": float(np.median(ranges)),
            "within_range_mean": float(np.mean(ranges)),
            "within_rho_median": float(np.median(within_rhos)),
            "within_rho_mean": float(np.mean(within_rhos)),
            "within_rho_n_positive": int(sum(1 for r in within_rhos if r > 0)),
            "global_rho": float(g_rho),
            "global_rho_p": float(g_p),
            "selection_f1": sel_f1,
            "sel_delta_greedy": sel_f1 - greedy_f1,
        }
        results["variants"][key] = variant_result

        print(f"{key:<20} {variant_result['within_range_median']:>8.4f} "
              f"{variant_result['within_rho_median']:>8.4f} "
              f"{variant_result['global_rho']:>8.4f} "
              f"{variant_result['selection_f1']:>8.4f} "
              f"{variant_result['sel_delta_greedy']:>+9.4f}")

    print()

    # Key comparison: full vs entity_text_type
    full = results["variants"]["full"]
    ett = results["variants"]["entity_text_type"]
    et = results["variants"]["entity_text"]
    schema = results["variants"]["schema_only"]

    print("=" * 75)
    print("KEY FINDING: Format token dilution analysis")
    print("=" * 75)
    print(f"  Global rho improvement (entity_text_type vs full): "
          f"{ett['global_rho']:.4f} vs {full['global_rho']:.4f} "
          f"(+{ett['global_rho'] - full['global_rho']:.4f})")
    print(f"  Within-instance range (entity_text_type vs full): "
          f"{ett['within_range_median']:.4f} vs {full['within_range_median']:.4f}")
    print(f"  Selection F1 (entity_text_type vs full): "
          f"{ett['selection_f1']:.4f} vs {full['selection_f1']:.4f} "
          f"({ett['sel_delta_greedy'] - full['sel_delta_greedy']:+.4f})")
    print(f"  Schema-only tokens global rho: {schema['global_rho']:.4f}")
    print()

    dilution_ratio = 1 - full['global_rho'] / ett['global_rho'] if ett['global_rho'] != 0 else 0
    results["dilution_analysis"] = {
        "dilution_ratio": dilution_ratio,
        "entity_text_type_global_rho": ett["global_rho"],
        "full_global_rho": full["global_rho"],
        "rho_improvement": ett["global_rho"] - full["global_rho"],
        "schema_only_global_rho": schema["global_rho"],
        "within_range_ratio_entity_vs_full": (
            ett["within_range_median"] / full["within_range_median"]
            if full["within_range_median"] > 0 else float("nan")
        ),
        "selection_f1_gap": ett["selection_f1"] - full["selection_f1"],
    }

    if dilution_ratio > 0.2:
        verdict = "FORMAT_DILUTION_SIGNIFICANT"
        note = (f"Removing format tokens improves global rho by {results['dilution_analysis']['rho_improvement']:.3f} "
                f"({dilution_ratio:.0%} dilution). But selection F1 gap is only "
                f"{abs(results['dilution_analysis']['selection_f1_gap']):.4f}, suggesting within-instance "
                f"ranking is less affected because format tokens have low within-instance variance.")
    else:
        verdict = "DILUTION_MINIMAL"
        note = "Format tokens do not significantly dilute entity LP signal."

    results["verdict"] = verdict
    results["verdict_note"] = note
    print(f"  Verdict: {verdict}")
    print(f"  {note}")
    print()

    out_path = output_dir / "analysis_results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Results saved to {out_path}")

    return results


if __name__ == "__main__":
    results = analyze(
        data_path="/root/autodl-tmp/struct_self_consist_ie/output/exp_entity_token_lp/scierc/samples.jsonl",
        output_dir="/root/autodl-tmp/struct_self_consist_ie/output/exp_028_entity_token_lp",
    )
