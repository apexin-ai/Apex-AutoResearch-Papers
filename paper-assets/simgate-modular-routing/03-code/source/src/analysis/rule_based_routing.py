"""Rule-based keyword routing baseline for plan-011.

Reads episodes.jsonl files from plan_c results, applies keyword-based
routing heuristic, and compares with oracle labels derived from score
comparison. Outputs terminal summary tables and per-episode CSV.

Input:  --data_dir pointing to plan_c results (subfolders = tasks, each
        containing episodes.jsonl)
        --keywords_file pointing to JSON with {"keywords": [...], "version": "..."}
Output: Terminal tables (overall + per-task) and CSV file (--output)

Dependencies: stdlib + pandas (for CSV/table output)
"""

import argparse
import csv
import json
import os
import sys
from collections import defaultdict
from pathlib import Path


DEFAULT_KEYWORDS = {
    "keywords": [
        "heat", "cool", "boil", "melt", "freeze",
        "mix", "react", "pour", "activate"
    ],
    "version": "v3"
}


def load_or_create_keywords(path: str) -> list[str]:
    """Load keywords from JSON. Creates default file if it doesn't exist."""
    p = Path(path)
    if not p.exists():
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "w") as f:
            json.dump(DEFAULT_KEYWORDS, f, indent=2)
        print(f"Created default keywords file: {path}")
    with open(p) as f:
        data = json.load(f)
    kws = data.get("keywords", [])
    version = data.get("version", "unknown")
    print(f"Keywords ({len(kws)}, {version}): {kws}")
    return kws


def extract_actions(episode: dict) -> list[str]:
    """Extract all action strings from both internal and deterministic runs."""
    actions = []
    for mode_key in ("always_internal", "always_deterministic"):
        mode_data = episode.get(mode_key, {})
        for step in mode_data.get("steps", []):
            a = step.get("action", "")
            if a:
                actions.append(a)
    return actions


def keyword_match_any(actions: list[str], keywords: list[str]) -> tuple[bool, list[str]]:
    """Check if any action contains any keyword (case-insensitive substring).

    Returns (matched, list_of_hit_keywords).
    """
    hits = set()
    for action in actions:
        action_lower = action.lower()
        for kw in keywords:
            if kw.lower() in action_lower:
                hits.add(kw)
    return len(hits) > 0, sorted(hits)


def oracle_label(int_score: float, det_score: float) -> str:
    if det_score > int_score:
        return "det-preferred"
    if int_score > det_score:
        return "internal-preferred"
    return "no-preference"


def process_episode(episode: dict, keywords: list[str]) -> dict:
    int_ep = episode["always_internal"]
    det_ep = episode["always_deterministic"]
    int_score = int_ep["final_score"]
    det_score = det_ep["final_score"]

    actions = extract_actions(episode)
    matched, hit_kws = keyword_match_any(actions, keywords)

    route_decision = "det-preferred" if matched else "internal-preferred"
    oracle = oracle_label(int_score, det_score)

    return {
        "task": int_ep.get("task_name", ""),
        "episode_idx": episode.get("episode_idx", -1),
        "variation_idx": episode.get("variation_idx", -1),
        "int_score": int_score,
        "det_score": det_score,
        "oracle": oracle,
        "keyword_matched": matched,
        "route_decision": route_decision,
        "correct": route_decision == oracle if oracle != "no-preference" else None,
        "hit_keywords": ",".join(hit_kws),
        "n_actions": len(actions),
    }


def compute_metrics(rows: list[dict]) -> dict:
    scorable = [r for r in rows if r["oracle"] != "no-preference"]
    n_scorable = len(scorable)
    n_correct = sum(1 for r in scorable if r["correct"])
    accuracy = n_correct / n_scorable if n_scorable else 0.0

    n_matched = sum(1 for r in rows if r["keyword_matched"])
    match_rate = n_matched / len(rows) if rows else 0.0

    class_metrics = {}
    for cls in ("det-preferred", "internal-preferred"):
        tp = sum(1 for r in rows if r["route_decision"] == cls and r["oracle"] == cls)
        fp = sum(1 for r in rows if r["route_decision"] == cls and r["oracle"] != cls
                 and r["oracle"] != "no-preference")
        fn = sum(1 for r in rows if r["route_decision"] != cls and r["oracle"] == cls)
        prec = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        rec = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0
        class_metrics[cls] = {"precision": prec, "recall": rec, "f1": f1,
                              "tp": tp, "fp": fp, "fn": fn}

    return {
        "n_total": len(rows),
        "n_scorable": n_scorable,
        "n_correct": n_correct,
        "accuracy": accuracy,
        "n_matched": n_matched,
        "match_rate": match_rate,
        "n_no_pref": len(rows) - n_scorable,
        "class_metrics": class_metrics,
    }


def print_overall(metrics: dict):
    m = metrics
    print(f"\n{'=' * 72}")
    print("RULE-BASED ROUTING BASELINE — OVERALL")
    print(f"{'=' * 72}")
    print(f"Total episodes:      {m['n_total']}")
    print(f"Scorable (excl tie): {m['n_scorable']}")
    print(f"No-preference:       {m['n_no_pref']}")
    print(f"Keyword match rate:  {m['match_rate']:.1%} ({m['n_matched']}/{m['n_total']})")
    print(f"Overall accuracy:    {m['accuracy']:.1%} ({m['n_correct']}/{m['n_scorable']})")
    print()
    print(f"{'Label':<20} {'Prec':>8} {'Recall':>8} {'F1':>8}   (TP/FP/FN)")
    print("-" * 65)
    for cls in ("det-preferred", "internal-preferred"):
        c = m["class_metrics"][cls]
        print(f"{cls:<20} {c['precision']:>7.1%} {c['recall']:>7.1%} "
              f"{c['f1']:>7.1%}   ({c['tp']}/{c['fp']}/{c['fn']})")


def print_per_task(task_metrics: dict):
    print(f"\n{'=' * 72}")
    print("PER-TASK BREAKDOWN")
    print(f"{'=' * 72}")
    hdr = f"{'Task':<42} {'Eps':>4} {'Match%':>7} {'Acc':>7} {'Det':>4} {'Int':>4} {'Tie':>4}"
    print(hdr)
    print("-" * 72)
    for task in sorted(task_metrics):
        m = task_metrics[task]
        rows = m["_rows"]
        n_det = sum(1 for r in rows if r["oracle"] == "det-preferred")
        n_int = sum(1 for r in rows if r["oracle"] == "internal-preferred")
        n_tie = sum(1 for r in rows if r["oracle"] == "no-preference")
        print(f"{task:<42} {m['n_total']:>4} {m['match_rate']:>6.1%} "
              f"{m['accuracy']:>6.1%} {n_det:>4} {n_int:>4} {n_tie:>4}")


def write_csv(rows: list[dict], output_path: str):
    fieldnames = [
        "task", "episode_idx", "variation_idx",
        "int_score", "det_score", "oracle",
        "keyword_matched", "route_decision", "correct",
        "hit_keywords", "n_actions",
    ]
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"\nCSV saved: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Rule-based keyword routing baseline (plan-011)")
    parser.add_argument("--data_dir", type=str, required=True,
                        help="Directory containing task subdirs with episodes.jsonl")
    parser.add_argument("--keywords_file", type=str,
                        default="src/rule_based_keywords.json",
                        help="Path to keywords JSON file")
    parser.add_argument("--output", type=str,
                        default="rule_based_comparison.csv",
                        help="Output CSV path")
    args = parser.parse_args()

    if not os.path.isdir(args.data_dir):
        print(f"ERROR: data_dir not found: {args.data_dir}", file=sys.stderr)
        sys.exit(1)

    keywords = load_or_create_keywords(args.keywords_file)
    if not keywords:
        print("ERROR: keyword list is empty", file=sys.stderr)
        sys.exit(1)

    all_rows = []
    task_groups = defaultdict(list)

    for task_name in sorted(os.listdir(args.data_dir)):
        ep_path = os.path.join(args.data_dir, task_name, "episodes.jsonl")
        if not os.path.isfile(ep_path):
            continue

        with open(ep_path) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                episode = json.loads(line)
                row = process_episode(episode, keywords)
                row["task"] = task_name
                all_rows.append(row)
                task_groups[task_name].append(row)

    if not all_rows:
        print("No episodes found.")
        sys.exit(1)

    overall = compute_metrics(all_rows)
    print_overall(overall)

    task_metrics = {}
    for task, rows in task_groups.items():
        m = compute_metrics(rows)
        m["_rows"] = rows
        task_metrics[task] = m
    print_per_task(task_metrics)

    write_csv(all_rows, args.output)


if __name__ == "__main__":
    main()
