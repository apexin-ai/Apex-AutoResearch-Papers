"""D195: GPT-4o vs GPT-4o-mini Cohen's kappa validation.

Samples 50 messages from existing GPT-4o annotations, re-annotates with
GPT-4o-mini using the same prompt, computes inter-model agreement (kappa).
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import random
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.gpt4o_annotation import SYSTEM_PROMPT, VALID_TYPES, annotate_single

from openai import OpenAI


def main():
    parser = argparse.ArgumentParser(description="D195: GPT-4o vs GPT-4o-mini kappa")
    parser.add_argument("--api-key", help="OpenAI API key (or set OPENAI_API_KEY)")
    parser.add_argument("--input", default="outputs/gpt4o_annotation/gpt4o_annotations.csv")
    parser.add_argument("--output-dir", default="outputs/d195_mini_kappa")
    parser.add_argument("--n-samples", type=int, default=50)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--delay", type=float, default=1.0, help="Seconds between requests")
    args = parser.parse_args()

    api_key = [REDACTED] or os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("Set OPENAI_API_KEY or pass --api-key")

    with open(args.input, newline="") as f:
        rows = list(csv.DictReader(f))

    valid_rows = [r for r in rows if r["gpt4o_label"] != "unknown"]
    print(f"Total valid GPT-4o annotations: {len(valid_rows)}")

    random.seed(args.seed)
    sampled = random.sample(valid_rows, min(args.n_samples, len(valid_rows)))
    print(f"Sampled {len(sampled)} messages (seed={args.seed})")

    # We need the original message text to re-annotate. The CSV has msg_id but
    # not full message text. Read the source annotation sheet for texts.
    anno_sheet_path = "data/human_annotation/annotation_sheet_full.csv"
    with open(anno_sheet_path, newline="") as f:
        sheet_rows = {r["msg_id"]: r for r in csv.DictReader(f)}

    client = OpenAI(api_key=[REDACTED]
    token_tracker = {"prompt_tokens": 0, "completion_tokens": 0, "api_calls": 0}
    results = []

    for i, row in enumerate(sampled):
        msg_id = row["msg_id"]
        sheet_row = sheet_rows.get(msg_id)
        if not sheet_row:
            print(f"  WARN: {msg_id} not found in annotation sheet, skipping")
            continue

        print(f"  [{i+1}/{len(sampled)}] {msg_id} ...", end=" ", flush=True)

        ann = annotate_single(
            client, "gpt-4o-mini",
            prev_text=sheet_row.get("prev_message_text", ""),
            msg_text=sheet_row["message_text"],
            sender=sheet_row["sender"],
            task_id=sheet_row["task_id"],
            token_tracker=token_tracker,
        )

        mini_label = ann.get("type", "unknown")
        print(f"gpt4o={row['gpt4o_label']} | mini={mini_label}")

        results.append({
            "msg_id": msg_id,
            "backbone": row["backbone"],
            "task_id": row["task_id"],
            "gpt4o_label": row["gpt4o_label"],
            "mini_label": mini_label,
            "mini_confidence": ann.get("confidence", 0),
            "mini_reasoning": ann.get("reasoning", ""),
        })

        if i < len(sampled) - 1:
            time.sleep(args.delay)

    # Compute Cohen's kappa
    valid_results = [r for r in results if r["mini_label"] != "unknown"]
    gpt4o_labels = [r["gpt4o_label"] for r in valid_results]
    mini_labels = [r["mini_label"] for r in valid_results]

    n = len(valid_results)
    if n == 0:
        print("ERROR: No valid results to compute kappa")
        return

    from src.gpt4o_annotation import compute_cohens_kappa, build_confusion_matrix

    kappa = compute_cohens_kappa(gpt4o_labels, mini_labels)
    agreement = sum(1 for a, b in zip(gpt4o_labels, mini_labels) if a == b) / n

    confusion = build_confusion_matrix(gpt4o_labels, mini_labels)

    # Per-category agreement
    categories = sorted(set(gpt4o_labels) | set(mini_labels))
    per_cat = {}
    for cat in categories:
        both = sum(1 for a, b in zip(gpt4o_labels, mini_labels) if a == cat and b == cat)
        either = sum(1 for a, b in zip(gpt4o_labels, mini_labels) if a == cat or b == cat)
        per_cat[cat] = {"both_agree": both, "either_labeled": either,
                        "agreement": round(both / either, 4) if either > 0 else 0}

    total_tokens = token_tracker["prompt_tokens"] + token_tracker["completion_tokens"]
    cost_in = token_tracker["prompt_tokens"] / 1_000_000 * 0.15
    cost_out = token_tracker["completion_tokens"] / 1_000_000 * 0.60
    total_cost = cost_in + cost_out

    output = {
        "task": "D195_mini_kappa",
        "comparison": "GPT-4o vs GPT-4o-mini",
        "n_sampled": len(sampled),
        "n_valid": n,
        "seed": args.seed,
        "cohens_kappa": round(kappa, 4),
        "percent_agreement": round(agreement, 4),
        "verdict": "mini_acceptable" if kappa > 0.8 else "mini_not_acceptable",
        "threshold": 0.8,
        "per_category": per_cat,
        "confusion_matrix": confusion,
        "token_usage": {
            "prompt_tokens": token_tracker["prompt_tokens"],
            "completion_tokens": token_tracker["completion_tokens"],
            "total_tokens": total_tokens,
            "api_calls": token_tracker["api_calls"],
            "cost_usd": round(total_cost, 4),
            "pricing_note": "GPT-4o-mini: $0.15/M input, $0.60/M output",
        },
        "per_message": valid_results,
    }

    os.makedirs(args.output_dir, exist_ok=True)
    out_path = os.path.join(args.output_dir, "kappa_results.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print("\n" + "=" * 60)
    print(f"  Cohen's κ (GPT-4o vs GPT-4o-mini): {kappa:.4f}")
    print(f"  Percent agreement: {agreement:.1%}")
    print(f"  N = {n}")
    print(f"  Verdict: {'PASS — mini acceptable' if kappa > 0.8 else 'FAIL — mini NOT acceptable, use Claude API'}")
    print("=" * 60)
    print(f"\n  Confusion matrix (rows=GPT-4o, cols=GPT-4o-mini):")
    header = "  {:>20s}".format("") + "".join(f"{c[:8]:>10s}" for c in categories)
    print(header)
    for cat in categories:
        row_vals = "".join(f"{confusion.get(cat, {}).get(c, 0):>10d}" for c in categories)
        print(f"  {cat:>20s}{row_vals}")
    print(f"\n  Cost: ${total_cost:.4f} ({token_tracker['api_calls']} calls, {total_tokens} tokens)")
    print(f"  Results saved to: {out_path}")


if __name__ == "__main__":
    main()
