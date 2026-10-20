"""Re-extract GSM8K answers with stop-sequence truncation.

Checks whether the original answer extraction differs from a corrected version
that first truncates generated_text at common stop sequences (e.g. "\n\n",
"Question:", "Q:") before extracting the numeric answer. If discrepancies
exist, outputs a corrected JSONL.

Input:  exp-002 GSM8K JSONL records
Output: results/analysis/gsm8k_answer_reextract.json  (report)
        results/analysis/gsm8k_corrected.jsonl         (optional, if diffs found)

Usage:
  python scripts/exp002_analysis/gsm8k_answer_reextract.py --data-dir results/exp002
"""

import argparse
import json
import re
import sys
import time
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from src.config.model_paths import normalize_model_name

STOP_SEQUENCES = ["\n\n", "\nQuestion:", "\nQ:", "\nProblem:", "####"]

GSM8K_ANSWER_PATTERN = re.compile(r"(?:####\s*|(?:the answer is|= |equals )\s*)(-?[\d,]+(?:\.\d+)?)")
NUMERIC_PATTERN = re.compile(r"(-?[\d,]+(?:\.\d+)?)")


def truncate_at_stop(text: str) -> str:
    """Truncate generated text at the earliest stop sequence."""
    earliest_pos = len(text)
    for stop in STOP_SEQUENCES:
        pos = text.find(stop)
        if pos != -1 and pos < earliest_pos:
            earliest_pos = pos
    return text[:earliest_pos].strip()


def extract_gsm8k_answer_original(text: str) -> str | None:
    """Original extraction: take first number-like token from generated text."""
    if text is None:
        return None
    text = text.strip()
    m = GSM8K_ANSWER_PATTERN.search(text)
    if m:
        return m.group(1).replace(",", "")
    m = NUMERIC_PATTERN.search(text)
    if m:
        return m.group(1).replace(",", "")
    return None


def extract_gsm8k_answer_fixed(text: str) -> str | None:
    """Fixed extraction: truncate at stop sequences first, then extract."""
    if text is None:
        return None
    truncated = truncate_at_stop(text)
    return extract_gsm8k_answer_original(truncated)


def normalize_numeric(answer: str | None) -> str | None:
    """Normalize numeric answer: remove leading zeros, trailing .0, etc."""
    if pd.isna(answer):
        return None
    if answer is None:
        return None
    try:
        val = float(answer)
        if val == int(val):
            return str(int(val))
        return str(val)
    except ValueError:
        return answer


def main():
    parser = argparse.ArgumentParser(description="GSM8K answer re-extraction with stop-sequence truncation")
    parser.add_argument("--data-dir", default="results/exp002")
    parser.add_argument("--output", default="results/analysis/gsm8k_answer_reextract.json")
    parser.add_argument("--corrected-output", default="results/analysis/gsm8k_corrected.jsonl")
    args = parser.parse_args()

    t0 = time.time()

    data_path = Path(args.data_dir)
    jsonl_files = sorted(data_path.glob("*.jsonl"))
    if not jsonl_files:
        raise FileNotFoundError(f"No JSONL files in {args.data_dir}")

    frames = [pd.read_json(f, lines=True) for f in jsonl_files]
    df = pd.concat(frames, ignore_index=True)
    df = df[df["benchmark"] == "gsm8k"].reset_index(drop=True)

    if len(df) == 0:
        print("No GSM8K records found.", flush=True)
        return

    print(f"GSM8K records: {len(df)} ({time.time()-t0:.1f}s)", flush=True)

    df["original_predicted"] = df["predicted_answer"].copy()
    df["reextracted_answer"] = df["generated_text"].apply(extract_gsm8k_answer_fixed)

    df["original_norm"] = df["original_predicted"].apply(normalize_numeric)
    df["reextracted_norm"] = df["reextracted_answer"].apply(normalize_numeric)
    df["gold_norm"] = df["gold_answer"].apply(normalize_numeric)

    df["original_correct"] = (df["original_norm"] == df["gold_norm"]).astype(int)
    df["reextracted_correct"] = (df["reextracted_norm"] == df["gold_norm"]).astype(int)

    differs = df["original_norm"] != df["reextracted_norm"]
    n_diff = differs.sum()
    n_total = len(df)
    pct_diff = n_diff / n_total * 100

    orig_acc = df["original_correct"].mean()
    reext_acc = df["reextracted_correct"].mean()

    print(f"\nDifferences: {n_diff}/{n_total} ({pct_diff:.2f}%)", flush=True)
    print(f"Original accuracy:     {orig_acc:.6f}", flush=True)
    print(f"Re-extracted accuracy: {reext_acc:.6f}", flush=True)
    print(f"Delta:                 {reext_acc - orig_acc:+.6f}", flush=True)

    diff_details = []
    if n_diff > 0:
        diff_df = df[differs].head(20)
        for _, row in diff_df.iterrows():
            diff_details.append({
                "item_id": row["item_id"],
                "condition_id": int(row["condition_id"]),
                "gold": row["gold_norm"],
                "original": row["original_norm"],
                "reextracted": row["reextracted_norm"],
                "generated_text_preview": row["generated_text"][:200],
                "original_correct": int(row["original_correct"]),
                "reextracted_correct": int(row["reextracted_correct"]),
            })

    flipped_to_correct = ((df["original_correct"] == 0) & (df["reextracted_correct"] == 1)).sum()
    flipped_to_wrong = ((df["original_correct"] == 1) & (df["reextracted_correct"] == 0)).sum()

    report = {
        "experiment": "exp-002",
        "analysis": "gsm8k_answer_reextract",
        "n_total": n_total,
        "n_differences": int(n_diff),
        "pct_differences": round(pct_diff, 4),
        "original_accuracy": round(float(orig_acc), 6),
        "reextracted_accuracy": round(float(reext_acc), 6),
        "accuracy_delta": round(float(reext_acc - orig_acc), 6),
        "flipped_to_correct": int(flipped_to_correct),
        "flipped_to_wrong": int(flipped_to_wrong),
        "stop_sequences_used": STOP_SEQUENCES,
        "sample_differences": diff_details,
        "corrected_file": args.corrected_output if n_diff > 0 else None,
    }

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    if n_diff > 0:
        df["predicted_answer"] = df["reextracted_norm"]
        df["correct"] = df["reextracted_correct"]
        cols_to_drop = ["original_predicted", "reextracted_answer", "original_norm",
                        "reextracted_norm", "gold_norm", "original_correct", "reextracted_correct"]
        df_out = df.drop(columns=[c for c in cols_to_drop if c in df.columns])
        with open(args.corrected_output, "w") as f:
            for _, row in df_out.iterrows():
                f.write(json.dumps(row.to_dict(), ensure_ascii=False, default=str) + "\n")
        print(f"Corrected JSONL -> {args.corrected_output}", flush=True)

    print(f"\nRuntime: {time.time()-t0:.1f}s", flush=True)
    print(f"-> {args.output}", flush=True)


if __name__ == "__main__":
    main()
