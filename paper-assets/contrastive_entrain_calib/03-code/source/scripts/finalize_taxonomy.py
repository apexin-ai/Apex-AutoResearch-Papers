"""Finalize taxonomy with truncation analysis and evaluation methodology notes."""
import json
import os
from collections import Counter, defaultdict

OUT_DIR = "/root/contrastive_entrain_calib/results/mechanistic_analysis/stubbornness_taxonomy"

with open(os.path.join(OUT_DIR, "case_examples.json")) as f:
    cases = json.load(f)

with open(os.path.join(OUT_DIR, "taxonomy_summary.json")) as f:
    summary = json.load(f)

n = len(cases)
truncated = sum(1 for c in cases if not c["model_response_clean"].rstrip().endswith((".", "!", "?", ")", "]", '"')))
avg_len = sum(len(c["model_response_clean"]) for c in cases) / n
starts_ah = sum(1 for c in cases if c["model_response_clean"].lower().startswith("ah"))
meta_reasoning = sum(1 for c in cases if "so the user" in c["model_response_clean"].lower() or "the user initially" in c["model_response_clean"].lower())

summary["response_analysis"] = {
    "truncated_responses": truncated,
    "truncated_pct": round(truncated / n * 100, 1),
    "avg_response_chars": round(avg_len),
    "starts_with_Ah": starts_ah,
    "meta_reasoning_style": meta_reasoning,
    "max_new_tokens": 512,
    "notes": [
        "enable_thinking=False was set but model outputs deliberative reasoning anyway",
        "96% of responses truncated at max_new_tokens before reaching conclusion",
        "flipped is determined by NLI contradiction (not entailment), requiring explicit reversal",
    ],
}

with open(os.path.join(OUT_DIR, "taxonomy_summary.json"), "w") as f:
    json.dump(summary, f, indent=2, ensure_ascii=False)

type_counts = Counter(c["category"] for c in cases)
category_examples = defaultdict(list)
for c in cases:
    category_examples[c["category"]].append(c)

CAT_LABELS = {
    "deliberate_inconclusive": "(a) Deliberate Inconclusive",
    "acknowledge_but_maintain": "(b) Acknowledge but Maintain",
    "surface_compliance": "(c) Surface Compliance",
    "refute_user": "(d) Refute User",
    "deliberate_but_ignore": "(e) Deliberate but Ignore",
    "genuine_accept_missed": "(f) Genuine Accept (eval missed)",
    "other": "(g) Other",
}
CAT_ORDER = list(CAT_LABELS.keys())

DESC_SHORT = {
    "deliberate_inconclusive": "Mentions correct answer but never commits",
    "acknowledge_but_maintain": "Hedges with however/but and maintains position",
    "surface_compliance": "Uses acceptance language without actual change",
    "refute_user": "Actively argues user is wrong",
    "deliberate_but_ignore": "Deliberates without mentioning correct answer",
    "genuine_accept_missed": "High NLI entailment suggests actual acceptance",
    "other": "Unclassified",
}

WHY_TEXT = {
    "deliberate_inconclusive": (
        "The model correctly identifies the right answer during deliberation but frames it as "
        '"one possible interpretation" rather than committing to a correction.'
    ),
    "surface_compliance": (
        'The model uses "you\'re right to point out" as a social token, then continues '
        "reasoning without changing its position -- agreement is performative, not substantive."
    ),
    "acknowledge_but_maintain": (
        'The model uses hedging language ("however", "but") to appear engaged with the '
        "correction while maintaining its original answer."
    ),
    "refute_user": "The model actively constructs arguments against the user's (correct) correction.",
    "deliberate_but_ignore": (
        "The model engages in extended reasoning but never even mentions the correct answer, "
        "suggesting the correction was not integrated into its reasoning process."
    ),
}

md = []
md.append("# Stubbornness Failure Case Taxonomy -- exp-008v3 ckpt-500")
md.append("")
md.append("## Overview")
md.append("")
md.append("- **Model**: Qwen3-8B + exp-008v3 (Binary Probe GRPO) checkpoint-500")
md.append("- **Eval set**: 181 valid_correction samples from calibration_v2_1_expanded")
md.append("- **ToF**: 0.0 (complete stubbornness -- model never accepts correct corrections)")
md.append("- **NoF**: 0.9945 (model also rarely accepts incorrect corrections)")
md.append(f"- **Truncation**: {truncated}/{n} ({truncated/n*100:.0f}%) responses truncated at 512 tokens")
md.append("")
md.append("## Evaluation Methodology Note")
md.append("")
md.append("`flipped` is determined by NLI **contradiction** between the model's initial response")
md.append("and its post-correction response. This is a strict criterion: the model must explicitly")
md.append("reverse its position, not merely acknowledge the correction. Extended deliberation that")
md.append("mentions the correct answer but doesn't commit counts as *not flipped*.")
md.append("")
md.append("Additionally, `enable_thinking=False` was set during generation, but the GRPO-trained")
md.append("model outputs deliberative chain-of-thought reasoning regardless (87% of responses start")
md.append('with "Ah, interesting"). Combined with the 512-token limit, 96% of responses are')
md.append("truncated before reaching a conclusion -- the model's reasoning never terminates.")
md.append("")
md.append("## Type Distribution")
md.append("")
md.append("| Category | Count | % | Description |")
md.append("|----------|------:|---:|-------------|")
for cat in CAT_ORDER:
    cnt = type_counts.get(cat, 0)
    if cnt == 0:
        continue
    pct = cnt / n * 100
    md.append(f"| {CAT_LABELS[cat]} | {cnt} | {pct:.1f}% | {DESC_SHORT[cat]} |")
md.append("")

md.append("## Key Findings")
md.append("")
md.append("1. **No complete ignoring**: The model always engages with the user's correction (0% complete ignore).")
md.append("2. **Deliberation trap**: The dominant mode (29%) is extended reasoning that mentions the correct answer")
md.append("   but never commits to updating -- the model is *aware* of the right answer but cannot act on it.")
md.append('3. **Surface compliance** (24%): The model produces politeness tokens ("you\'re right", "indeed")')
md.append("   that mimic acceptance without actual position change -- *sycophantic stubbornness*.")
md.append("4. **Evidence strength gradient**: Weak evidence -> surface compliance (39%); Strong evidence ->")
md.append("   explicit hedging (54%). The model calibrates its *rejection style* to evidence strength")
md.append("   even though it never actually accepts.")
md.append("5. **Format corruption**: GRPO training shifted the model from direct answers to deliberative")
md.append("   chain-of-thought reasoning, which never terminates within the token budget.")
md.append("")
md.append("## Representative Examples")
md.append("")

priority_cats = [
    "deliberate_inconclusive",
    "surface_compliance",
    "acknowledge_but_maintain",
    "refute_user",
    "deliberate_but_ignore",
]
shown = 0
for cat in priority_cats:
    exs = category_examples.get(cat, [])
    if not exs or shown >= 5:
        continue
    ex = exs[0]
    label = CAT_LABELS[cat]
    md.append(f"### Example {shown + 1}: {label}")
    md.append("")
    md.append(f"**ID**: `{ex['pair_id']}` | **Domain**: {ex['domain']} | **Evidence**: {ex['evidence_strength']}")
    md.append(f"**Ground Truth**: {ex['ground_truth']} | **Model's Initial Wrong Answer**: {ex['wrong_answer']}")
    md.append("")

    for turn in ex["turns"]:
        role = "User" if turn["role"] == "user" else "Assistant (Round 1)"
        content = turn["content"]
        if len(content) > 350:
            content = content[:350] + " [...]"
        md.append(f"> **{role}**: {content}")
        md.append(">")

    resp = ex["model_response_clean"]
    if len(resp) > 800:
        resp = resp[:800] + " [...]"
    md.append("> **Assistant (Round 2)**:")
    for line in resp.split("\n"):
        md.append(f"> {line}")
    md.append("")
    ent = ex["nli_scores"].get("entailment", 0)
    con = ex["nli_scores"].get("contradiction", 0)
    md.append(f"*NLI*: {ex['nli_label']} (ent={ent:.3f}, con={con:.3f}) | *Flipped*: No")
    md.append("")
    cat_name = label.split(")", 1)[1].strip()
    md.append(f"*Why this is {cat_name}*: {WHY_TEXT.get(cat, '')}")
    md.append("")
    md.append("---")
    md.append("")
    shown += 1

with open(os.path.join(OUT_DIR, "paper_examples.md"), "w") as f:
    f.write("\n".join(md))

print(f"Updated taxonomy_summary.json and paper_examples.md in {OUT_DIR}/")
print(f"Files: taxonomy_summary.json, case_examples.json, paper_examples.md")
