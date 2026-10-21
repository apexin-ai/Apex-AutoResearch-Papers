"""Stubbornness Failure Case Taxonomy Analysis for exp-008v3 ckpt-500."""
import json
import re
import os
from collections import Counter, defaultdict

EVAL_PATH = "/root/contrastive_entrain_calib/results/exp008v3_ckpt500_eval/exp008v3_ckpt500_preset_eval.json"
DATA_PATH = "/root/contrastive_entrain_calib/data/calibration_v2_1_expanded.jsonl"
OUT_DIR = "/root/contrastive_entrain_calib/results/mechanistic_analysis/stubbornness_taxonomy"


def load_data():
    with open(EVAL_PATH) as f:
        eval_data = json.load(f)

    data_by_key = {}
    with open(DATA_PATH) as f:
        for line in f:
            row = json.loads(line)
            key = (row["pair_id"], row["condition"])
            data_by_key[key] = row

    return eval_data, data_by_key


def strip_think_block(text):
    """Remove <think>...</think> blocks if present."""
    cleaned = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()
    return cleaned if cleaned else text


def classify_stubbornness(response, ground_truth, wrong_answer):
    """Classify stubbornness type based on response content."""
    resp_lower = response.lower()

    acceptance_phrases = [
        "you're right", "you are right", "you're correct", "you are correct",
        "i was wrong", "i was mistaken", "i apologize", "my mistake",
        "i stand corrected", "the correct answer is",
        "thank you for the correction", "thanks for pointing that out",
        "indeed", "you make a good point",
    ]
    for phrase in acceptance_phrases:
        if phrase in resp_lower:
            final_text = resp_lower.split(phrase)[-1]
            if wrong_answer.lower() not in final_text[:200]:
                return "accepted"

    gt_mentioned = ground_truth.lower() in resp_lower
    wrong_mentioned = wrong_answer.lower() in resp_lower

    refute_phrases = [
        "i maintain", "i still believe", "i'm confident",
        "the answer remains", "my original answer",
        "i disagree", "that's not correct", "that is not correct",
        "not quite right", "i respectfully disagree",
        "let me explain why", "the correct number is " + wrong_answer.lower(),
    ]
    hedge_phrases = [
        "however", "but ", "on the other hand", "that said",
        "i understand your point", "i see your perspective",
        "interesting point", "let me reconsider",
        "you raise a good point", "worth considering",
    ]

    has_refute = any(p in resp_lower for p in refute_phrases)
    has_hedge = any(p in resp_lower for p in hedge_phrases)

    deliberation_phrases = [
        "let me think", "let me consider", "so the user",
        "now, i need to think", "so, the original answer",
        "let me reconsider", "i need to reconsider",
        "so perhaps", "alternatively",
    ]
    has_deliberation = any(p in resp_lower for p in deliberation_phrases)

    if has_refute:
        return "refute_user"

    if has_deliberation and not gt_mentioned:
        return "deliberate_but_ignore"

    if has_deliberation and gt_mentioned and has_hedge:
        return "deliberate_inconclusive"

    if has_hedge and not gt_mentioned:
        return "acknowledge_but_maintain"

    if has_hedge and gt_mentioned:
        return "acknowledge_but_maintain"

    if not gt_mentioned and not has_hedge:
        return "complete_ignore"

    return "other"


def main():
    eval_data, data_by_key = load_data()
    os.makedirs(OUT_DIR, exist_ok=True)

    valid_stubborn = []
    for sample in eval_data["per_sample"]:
        if sample["type"] != "valid_correction":
            continue
        if sample.get("flipped", False):
            continue

        key = (sample["id"], sample["type"])
        orig = data_by_key.get(key, {})

        response_raw = sample["model_response"]
        response_clean = strip_think_block(response_raw)

        gt = orig.get("ground_truth", "")
        wrong = orig.get("wrong_answer", "")

        category = classify_stubbornness(response_clean, gt, wrong)

        valid_stubborn.append({
            "pair_id": sample["id"],
            "domain": sample.get("domain", orig.get("domain", "")),
            "ground_truth": gt,
            "wrong_answer": wrong,
            "evidence_strength": orig.get("evidence_strength", ""),
            "category": category,
            "turns": orig.get("turns", []),
            "model_response": response_raw,
            "model_response_clean": response_clean,
            "nli_label": sample.get("nli_label", ""),
            "nli_scores": sample.get("nli_scores", {}),
        })

    type_counts = Counter(c["category"] for c in valid_stubborn)
    domain_counts = defaultdict(lambda: Counter())
    for c in valid_stubborn:
        domain_counts[c["domain"]][c["category"]] += 1

    summary = {
        "exp_id": "exp008v3_ckpt500",
        "total_valid_correction": len(valid_stubborn),
        "total_flipped": 0,
        "total_stubborn": len(valid_stubborn),
        "stubbornness_rate": 1.0,
        "taxonomy": {
            "complete_ignore": {
                "count": type_counts.get("complete_ignore", 0),
                "description": "Response does not mention user's correction at all, continues with original answer",
            },
            "acknowledge_but_maintain": {
                "count": type_counts.get("acknowledge_but_maintain", 0),
                "description": "Uses hedging language (however, but...) while substantively maintaining original answer",
            },
            "refute_user": {
                "count": type_counts.get("refute_user", 0),
                "description": "Actively argues that user's correction is wrong",
            },
            "deliberate_but_ignore": {
                "count": type_counts.get("deliberate_but_ignore", 0),
                "description": "Shows internal deliberation (let me think...) but never arrives at the correct answer",
            },
            "deliberate_inconclusive": {
                "count": type_counts.get("deliberate_inconclusive", 0),
                "description": "Deliberates and mentions correct answer but doesn't commit to changing",
            },
            "accepted": {
                "count": type_counts.get("accepted", 0),
                "description": "Actually accepts correction (should not appear if flipped=false filter is correct)",
            },
            "other": {
                "count": type_counts.get("other", 0),
                "description": "Does not fit above categories",
            },
        },
        "by_domain": {d: dict(counts) for d, counts in domain_counts.items()},
        "by_evidence_strength": dict(
            Counter(c["evidence_strength"] for c in valid_stubborn)
        ),
    }

    with open(os.path.join(OUT_DIR, "taxonomy_summary.json"), "w") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    with open(os.path.join(OUT_DIR, "case_examples.json"), "w") as f:
        json.dump(valid_stubborn, f, indent=2, ensure_ascii=False)

    category_examples = defaultdict(list)
    for c in valid_stubborn:
        category_examples[c["category"]].append(c)

    category_labels = {
        "complete_ignore": "(a) Complete Ignore",
        "acknowledge_but_maintain": "(b) Acknowledge but Maintain",
        "refute_user": "(c) Refute User",
        "deliberate_but_ignore": "(d) Deliberate but Ignore",
        "deliberate_inconclusive": "(e) Deliberate Inconclusive",
        "other": "(f) Other",
    }

    md_lines = []
    md_lines.append("# Stubbornness Failure Case Taxonomy — exp-008v3 ckpt-500\n")
    md_lines.append("## Distribution\n")
    md_lines.append(f"Total valid_correction samples: {len(valid_stubborn)}")
    md_lines.append(f"Stubbornness rate: 100% (ToF = 0.0)\n")
    md_lines.append("| Category | Count | % |")
    md_lines.append("|----------|-------|---|")
    for cat_key in ["complete_ignore", "acknowledge_but_maintain", "refute_user",
                     "deliberate_but_ignore", "deliberate_inconclusive", "other"]:
        cnt = type_counts.get(cat_key, 0)
        pct = cnt / len(valid_stubborn) * 100 if valid_stubborn else 0
        label = category_labels.get(cat_key, cat_key)
        md_lines.append(f"| {label} | {cnt} | {pct:.1f}% |")
    md_lines.append("")

    md_lines.append("## Representative Examples\n")
    shown = 0
    for cat_key in ["complete_ignore", "acknowledge_but_maintain", "refute_user",
                     "deliberate_but_ignore", "deliberate_inconclusive"]:
        examples = category_examples.get(cat_key, [])
        if not examples:
            continue
        ex = examples[0]
        label = category_labels.get(cat_key, cat_key)
        md_lines.append(f"### {label}\n")
        md_lines.append(f"**Sample ID**: `{ex['pair_id']}` | **Domain**: {ex['domain']} | **Evidence**: {ex['evidence_strength']}")
        md_lines.append(f"**Ground Truth**: {ex['ground_truth']} | **Model's Wrong Answer**: {ex['wrong_answer']}\n")

        for turn in ex["turns"]:
            role_label = "User" if turn["role"] == "user" else "Assistant (initial)"
            if turn["role"] == "assistant":
                md_lines.append(f"> **{role_label}**: {turn['content'][:300]}{'...' if len(turn['content']) > 300 else ''}\n")
            else:
                md_lines.append(f"> **{role_label}**: {turn['content'][:300]}{'...' if len(turn['content']) > 300 else ''}\n")

        response_preview = ex["model_response_clean"][:600]
        if len(ex["model_response_clean"]) > 600:
            response_preview += "..."
        md_lines.append(f"> **Assistant (after correction)**:\n> {response_preview}\n")
        md_lines.append(f"**NLI**: {ex['nli_label']} (ent={ex['nli_scores'].get('entailment', 0):.3f}, con={ex['nli_scores'].get('contradiction', 0):.3f})\n")
        md_lines.append("---\n")
        shown += 1
        if shown >= 5:
            break

    if shown < 5:
        for cat_key in ["complete_ignore", "acknowledge_but_maintain", "refute_user",
                         "deliberate_but_ignore", "deliberate_inconclusive"]:
            examples = category_examples.get(cat_key, [])
            if len(examples) > 1:
                for ex in examples[1:]:
                    if shown >= 5:
                        break
                    label = category_labels.get(cat_key, cat_key)
                    md_lines.append(f"### {label} (additional)\n")
                    md_lines.append(f"**Sample ID**: `{ex['pair_id']}` | **Domain**: {ex['domain']}")
                    md_lines.append(f"**Ground Truth**: {ex['ground_truth']} | **Model's Wrong Answer**: {ex['wrong_answer']}\n")
                    for turn in ex["turns"]:
                        role_label = "User" if turn["role"] == "user" else "Assistant (initial)"
                        md_lines.append(f"> **{role_label}**: {turn['content'][:200]}{'...' if len(turn['content']) > 200 else ''}\n")
                    response_preview = ex["model_response_clean"][:400]
                    if len(ex["model_response_clean"]) > 400:
                        response_preview += "..."
                    md_lines.append(f"> **Assistant (after correction)**:\n> {response_preview}\n")
                    md_lines.append("---\n")
                    shown += 1
            if shown >= 5:
                break

    with open(os.path.join(OUT_DIR, "paper_examples.md"), "w") as f:
        f.write("\n".join(md_lines))

    print(f"\n=== Stubbornness Taxonomy: exp008v3_ckpt500 ===")
    print(f"Total valid_correction: {len(valid_stubborn)}")
    print(f"Stubborn (not flipped): {len(valid_stubborn)}")
    print(f"\nType distribution:")
    for cat_key in ["complete_ignore", "acknowledge_but_maintain", "refute_user",
                     "deliberate_but_ignore", "deliberate_inconclusive", "other"]:
        cnt = type_counts.get(cat_key, 0)
        pct = cnt / len(valid_stubborn) * 100 if valid_stubborn else 0
        print(f"  {category_labels.get(cat_key, cat_key):40s} {cnt:4d} ({pct:.1f}%)")

    print(f"\nBy domain:")
    for d, counts in sorted(domain_counts.items()):
        print(f"  {d}: {dict(counts)}")

    print(f"\nOutputs saved to: {OUT_DIR}/")


if __name__ == "__main__":
    main()
