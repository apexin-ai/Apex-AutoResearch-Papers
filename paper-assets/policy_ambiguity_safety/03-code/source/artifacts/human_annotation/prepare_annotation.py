"""Prepare stratified sample of 100 violation traces for human annotation.

Outputs:
  - annotation_sheet.csv
  - annotation_sheet.json
  - sample_summary.json
"""

import csv
import json
import random
from collections import defaultdict
from pathlib import Path

random.seed(42)

ARTIFACTS_DIR = Path(__file__).resolve().parent.parent
JUDGMENTS_DIR = ARTIFACTS_DIR / "full_study" / "judgments"
EPISODES_DIR = ARTIFACTS_DIR / "full_study" / "episodes"
CLAUSES_FILE = ARTIFACTS_DIR / "clause_templates_full.json"
OUTPUT_DIR = Path(__file__).resolve().parent

MODELS = ["claude-sonnet-4-6", "deepseek-v3", "gpt-4.1", "gpt-5.4", "qwen3-235b"]
TARGET_TOTAL = 100


def load_clauses():
    with open(CLAUSES_FILE) as f:
        clauses = json.load(f)
    return {c["clause_id"]: c for c in clauses}


def format_trajectory(trajectory):
    parts = []
    for msg in trajectory:
        role = msg.get("role", "unknown")
        content = msg.get("content", "")

        if role == "user":
            prefix = "[User]"
        elif role == "assistant":
            prefix = "[Agent]"
        elif role == "tool":
            prefix = "[Tool Result]"
        else:
            prefix = f"[{role}]"

        if content:
            parts.append(f"{prefix} {content}")

        tool_calls = msg.get("tool_calls")
        if tool_calls:
            for tc in tool_calls:
                fn = tc.get("function", {})
                name = fn.get("name", "unknown")
                args = fn.get("arguments", "")
                parts.append(f"[Tool Call] {name}({args})")

    return "\n\n".join(parts)


def load_all_violations():
    clauses = load_clauses()
    all_violations = []

    for model in MODELS:
        # Load episodes
        ep_file = EPISODES_DIR / model / "episodes.jsonl"
        episodes = {}
        with open(ep_file) as f:
            for line in f:
                ep = json.loads(line)
                episodes[ep["episode_id"]] = ep

        # Load judgments, filter violations
        jdg_file = JUDGMENTS_DIR / model / "judgments.jsonl"
        with open(jdg_file) as f:
            for line in f:
                j = json.loads(line)
                if (j["condition"] == "ambiguous"
                        and j["judgment"]["violation_level"] in ("moderate", "critical")):
                    eid = j["episode_id"]
                    if eid not in episodes:
                        continue
                    ep = episodes[eid]
                    clause = clauses.get(j["clause_id"], {})

                    all_violations.append({
                        "episode_id": eid,
                        "clause_id": j["clause_id"],
                        "ambiguity_type": j["ambiguity_type"],
                        "model": model,
                        "violation_level": j["judgment"]["violation_level"],
                        "violation_description": j["judgment"]["violation_description"],
                        "policy_clause_ambiguous": clause.get("ambiguous_clause", ep.get("system_prompt", "")),
                        "policy_clause_unambiguous": clause.get("unambiguous_clause", ""),
                        "trajectory": ep["trajectory"],
                        "system_prompt": ep.get("system_prompt", ""),
                    })

    return all_violations


def stratified_sample(violations, target=TARGET_TOTAL):
    by_type = defaultdict(list)
    for v in violations:
        by_type[v["ambiguity_type"]].append(v)

    n_types = len(by_type)
    per_type = target // n_types  # ~16-17
    remainder = target - per_type * n_types

    sampled = []
    type_counts = {}

    for i, (atype, items) in enumerate(sorted(by_type.items())):
        quota = per_type + (1 if i < remainder else 0)

        if len(items) <= quota:
            chosen = items
        else:
            # Within each type, ensure model diversity
            by_model = defaultdict(list)
            for item in items:
                by_model[item["model"]].append(item)

            chosen = []
            per_model = quota // len(by_model)
            model_remainder = quota - per_model * len(by_model)

            for j, (model, model_items) in enumerate(sorted(by_model.items())):
                model_quota = per_model + (1 if j < model_remainder else 0)
                random.shuffle(model_items)
                chosen.extend(model_items[:model_quota])

            # If we still need more (some models had fewer than quota)
            if len(chosen) < quota:
                chosen_ids = {c["episode_id"] for c in chosen}
                remaining = [x for x in items if x["episode_id"] not in chosen_ids]
                random.shuffle(remaining)
                chosen.extend(remaining[:quota - len(chosen)])

            chosen = chosen[:quota]

        sampled.extend(chosen)
        type_counts[atype] = len(chosen)

    return sampled, type_counts


def build_annotation_records(sampled):
    records = []
    for i, v in enumerate(sampled, 1):
        traj_text = format_trajectory(v["trajectory"])
        records.append({
            "sample_id": i,
            "episode_id": v["episode_id"],
            "clause_id": v["clause_id"],
            "ambiguity_type": v["ambiguity_type"],
            "model": v["model"],
            "violation_level": v["violation_level"],
            "policy_clause_ambiguous": v["policy_clause_ambiguous"],
            "policy_clause_unambiguous": v["policy_clause_unambiguous"],
            "trajectory": traj_text,
            "judge_violation_description": v["violation_description"],
            "failure_mode": "",  # to be filled by annotator
            "annotator_notes": "",  # to be filled by annotator
        })
    return records


def write_csv(records, path):
    fieldnames = [
        "sample_id", "episode_id", "clause_id", "ambiguity_type", "model",
        "violation_level", "policy_clause_ambiguous", "policy_clause_unambiguous",
        "trajectory", "judge_violation_description", "failure_mode", "annotator_notes",
    ]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(records)


def write_json(records, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)


def write_summary(sampled, type_counts, path):
    model_counts = defaultdict(int)
    type_model = defaultdict(lambda: defaultdict(int))
    for v in sampled:
        model_counts[v["model"]] += 1
        type_model[v["ambiguity_type"]][v["model"]] += 1

    summary = {
        "total_sampled": len(sampled),
        "by_ambiguity_type": dict(type_counts),
        "by_model": dict(model_counts),
        "by_type_and_model": {t: dict(m) for t, m in type_model.items()},
    }
    with open(path, "w") as f:
        json.dump(summary, f, indent=2)
    return summary


def main():
    print("Loading violations...")
    violations = load_all_violations()
    print(f"  Total violations: {len(violations)}")

    print("Stratified sampling...")
    sampled, type_counts = stratified_sample(violations)
    print(f"  Sampled: {len(sampled)}")
    for t, c in sorted(type_counts.items()):
        print(f"    {t}: {c}")

    print("Building annotation records...")
    records = build_annotation_records(sampled)

    print("Writing outputs...")
    write_csv(records, OUTPUT_DIR / "annotation_sheet.csv")
    write_json(records, OUTPUT_DIR / "annotation_sheet.json")
    summary = write_summary(sampled, type_counts, OUTPUT_DIR / "sample_summary.json")

    print("\nSummary:")
    print(json.dumps(summary, indent=2))
    print("\nDone.")


if __name__ == "__main__":
    main()
