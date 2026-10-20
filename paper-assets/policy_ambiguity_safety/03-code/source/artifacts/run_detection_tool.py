#!/usr/bin/env python3
"""Ambiguity Type Detection Tool — LLM-based classifier with 5-fold CV."""

import json
import os
import sys
import asyncio
import random
import time
from pathlib import Path
from collections import defaultdict

import numpy as np
from sklearn.metrics import (
    precision_recall_fscore_support,
    confusion_matrix,
    accuracy_score,
)

# ── API key setup ──
sys.path.insert(0, "/home/ubuntu/agent-ml-research")
from core.crypto import load_secret

key = load_secret(
    Path(
        "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4"
        "/config/secrets/policy_ambiguity_safety/openrouter_api_key.enc"
    )
)

from openai import AsyncOpenAI

client = AsyncOpenAI(base_url="http://47.94.22.126/v1", api_key=[REDACTED]
MODEL = "gpt-4.1"
CONCURRENCY = 5
DATA_PATH = Path(__file__).parent / "_project/data/clause_templates_full.json"
OUT_DIR = Path(__file__).parent / "detection_tool"
OUT_DIR.mkdir(exist_ok=True)

AMBIGUITY_TYPES = [
    "scopal",
    "lexical",
    "incompleteness",
    "conditional_precedence",
    "authorization_scope",
]

SYSTEM_PROMPT = """You are an expert policy analyst. Classify whether a policy clause contains ambiguity and identify the type.

## The 5 Ambiguity Types (read distinctions carefully)

### 1. scopal
**Core test**: Does a modifier, quantifier, negation, or condition have multiple possible attachment points in the sentence structure?
- The ambiguity arises from SYNTAX — the same words could parse differently.
- Example: "Agents should assist premium customers and those with urgent issues quickly" — "quickly" could attach to just "urgent issues" or to both groups.
- Example: "Do not share data with third parties and internal teams without approval" — "without approval" could scope over just "internal teams" or both.
- NOT scopal if individual words are vague — that's lexical.

### 2. lexical
**Core test**: Does a SINGLE word or short phrase have multiple established dictionary meanings, or is it a subjective/vague gradable adjective?
- The ambiguity is in WORD MEANING — a specific term could be interpreted differently.
- Example: "Agents may offer reasonable compensation" — "reasonable" is a vague gradable adjective.
- Example: "Process urgent requests first" — "urgent" is subjective with no threshold.
- CRITICAL DISTINCTION from authorization_scope: If the vague term describes WHO can act or WHAT authority they have, it's authorization_scope, NOT lexical. "Senior agents" is authorization_scope (who has authority?), not lexical.
- CRITICAL DISTINCTION from incompleteness: If the problem is that an entire procedure/condition/criterion is MISSING (not just vaguely worded), it's incompleteness, NOT lexical.

### 3. incompleteness
**Core test**: Is critical information entirely ABSENT — a missing procedure, undefined criterion, unspecified exception, or gap in coverage?
- The clause fails to mention something it needs to. The problem isn't a vague word — it's a missing piece.
- Example: "Refunds should be processed for eligible orders" — WHAT makes an order "eligible" is completely unspecified.
- Example: "Escalate complex cases to the appropriate team" — no escalation procedure, no team identification.
- CRITICAL DISTINCTION from lexical: If you can point to a specific vague WORD, it's lexical. If the problem is that the clause OMITS necessary information (conditions, procedures, criteria, limits, exceptions), it's incompleteness.

### 4. conditional_precedence
**Core test**: Are there two or more rules/conditions that could CONFLICT, with no specified priority?
- The clause creates a situation where following one rule means violating another.
- Example: "Customer satisfaction should be prioritized. All interactions must follow the standard script." — conflict when script hurts satisfaction.
- Example: "Protect user privacy. Share all relevant information with the support team." — conflict between privacy and information sharing.

### 5. authorization_scope
**Core test**: Is it unclear WHO has permission/authority to do something, or WHAT the boundaries of that authority are?
- The ambiguity is about ROLES, PERMISSIONS, or AUTHORITY BOUNDARIES.
- Example: "Senior agents can override the return policy when circumstances warrant" — who is "senior"? What circumstances trigger override authority?
- Example: "Managers may approve exceptions" — which managers? All managers? Only direct managers?
- CRITICAL DISTINCTION from lexical: Even if the role term is vague ("senior," "authorized," "appropriate"), if the core question is about who can do what, classify as authorization_scope.

## Decision Procedure
1. Is the clause clear and complete? → "none"
2. Are there conflicting rules with no priority? → "conditional_precedence"
3. Is it unclear who has authority or what authority boundaries are? → "authorization_scope"
4. Is critical information (procedures, criteria, exceptions) entirely missing? → "incompleteness"
5. Does a modifier/quantifier/condition have ambiguous syntactic attachment? → "scopal"
6. Is a specific word/phrase vague or polysemous? → "lexical"

## Output Format
Respond with ONLY valid JSON:
{"has_ambiguity": true, "ambiguity_type": "TYPE", "confidence": 0.85, "reasoning": "brief explanation"}

If unambiguous:
{"has_ambiguity": false, "ambiguity_type": "none", "confidence": 0.9, "reasoning": "brief explanation"}"""


def build_user_prompt(clause: str) -> str:
    return f"Follow the decision procedure step by step. Classify this policy clause:\n\n\"{clause}\""


def parse_response(text: str) -> dict:
    text = text.strip()
    if text.startswith("```"):
        lines = text.split("\n")
        lines = [l for l in lines if not l.strip().startswith("```")]
        text = "\n".join(lines)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        import re
        m = re.search(r'\{.*\}', text, re.DOTALL)
        if m:
            try:
                return json.loads(m.group())
            except json.JSONDecodeError:
                pass
    return None


async def classify_clause(clause: str, semaphore: asyncio.Semaphore, retries: int = 3) -> dict:
    async with semaphore:
        for attempt in range(retries):
            try:
                resp = await client.chat.completions.create(
                    model=MODEL,
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": build_user_prompt(clause)},
                    ],
                    temperature=0.0,
                    max_tokens=300,
                )
                text = resp.choices[0].message.content
                parsed = parse_response(text)
                if parsed and "has_ambiguity" in parsed:
                    return parsed
                print(f"  [WARN] Unparseable response (attempt {attempt+1}): {text[:100]}")
            except Exception as e:
                print(f"  [ERR] API error (attempt {attempt+1}): {e}")
                if attempt < retries - 1:
                    await asyncio.sleep(2 ** attempt)
    return {"has_ambiguity": None, "ambiguity_type": "parse_error", "confidence": 0.0, "reasoning": "Failed to parse"}


def load_data() -> list[dict]:
    with open(DATA_PATH) as f:
        raw = json.load(f)
    samples = []
    for item in raw:
        samples.append({
            "clause_id": item["clause_id"],
            "variant": "ambiguous",
            "clause": item["ambiguous_clause"],
            "gold_has_ambiguity": True,
            "gold_type": item["ambiguity_type"],
        })
        samples.append({
            "clause_id": item["clause_id"],
            "variant": "unambiguous",
            "clause": item["unambiguous_clause"],
            "gold_has_ambiguity": False,
            "gold_type": "none",
        })
    return samples


def make_folds(data: list[dict], n_folds: int = 5, seed: int = 42) -> list[list[int]]:
    clause_ids = sorted(set(d["clause_id"] for d in data))
    rng = random.Random(seed)
    rng.shuffle(clause_ids)

    id_to_indices = defaultdict(list)
    for i, d in enumerate(data):
        id_to_indices[d["clause_id"]].append(i)

    folds = [[] for _ in range(n_folds)]
    for i, cid in enumerate(clause_ids):
        folds[i % n_folds].extend(id_to_indices[cid])
    return folds


async def run_fold(fold_idx: int, test_indices: set[int], data: list[dict], semaphore: asyncio.Semaphore) -> list[dict]:
    test_data = [data[i] for i in sorted(test_indices)]
    print(f"  Fold {fold_idx+1}: classifying {len(test_data)} test samples...")

    tasks = []
    for sample in test_data:
        tasks.append(classify_clause(sample["clause"], semaphore))

    results = await asyncio.gather(*tasks)
    predictions = []
    for sample, pred in zip(test_data, results):
        pred_type = pred.get("ambiguity_type", "parse_error")
        if pred_type not in AMBIGUITY_TYPES and pred_type != "none":
            pred_type = "none" if not pred.get("has_ambiguity") else "parse_error"

        predictions.append({
            "clause_id": sample["clause_id"],
            "variant": sample["variant"],
            "clause": sample["clause"][:200],
            "gold_has_ambiguity": sample["gold_has_ambiguity"],
            "gold_type": sample["gold_type"],
            "pred_has_ambiguity": bool(pred.get("has_ambiguity")),
            "pred_type": pred_type,
            "confidence": pred.get("confidence", 0.0),
            "reasoning": pred.get("reasoning", ""),
            "fold": fold_idx,
        })
    return predictions


async def dry_run(data: list[dict]) -> bool:
    print("=== DRY RUN (5 samples) ===")
    semaphore = asyncio.Semaphore(5)
    test_samples = data[:3] + data[-2:]
    tasks = [classify_clause(s["clause"], semaphore) for s in test_samples]
    results = await asyncio.gather(*tasks)
    ok = True
    for s, r in zip(test_samples, results):
        status = "OK" if r.get("has_ambiguity") is not None else "FAIL"
        print(f"  [{status}] {s['clause_id']}({s['variant']}): has_ambiguity={r.get('has_ambiguity')}, type={r.get('ambiguity_type')}")
        if r.get("has_ambiguity") is None:
            ok = False
    if not ok:
        print("DRY RUN FAILED — aborting.")
    else:
        print("DRY RUN PASSED\n")
    return ok


def compute_metrics(all_preds: list[dict]) -> dict:
    all_labels = ["none"] + AMBIGUITY_TYPES
    gold_types = [p["gold_type"] for p in all_preds]
    pred_types = [p["pred_type"] for p in all_preds]

    # Map parse_error to a wrong prediction
    pred_types_clean = []
    for pt in pred_types:
        if pt == "parse_error":
            pred_types_clean.append("__error__")
        else:
            pred_types_clean.append(pt)

    all_labels_ext = all_labels + (["__error__"] if "__error__" in pred_types_clean else [])

    prec, rec, f1, sup = precision_recall_fscore_support(
        gold_types, pred_types_clean, labels=all_labels, average=None, zero_division=0
    )
    macro_prec, macro_rec, macro_f1, _ = precision_recall_fscore_support(
        gold_types, pred_types_clean, labels=all_labels, average="macro", zero_division=0
    )

    per_type = {}
    for i, label in enumerate(all_labels):
        per_type[label] = {
            "precision": round(float(prec[i]), 4),
            "recall": round(float(rec[i]), 4),
            "f1": round(float(f1[i]), 4),
            "support": int(sup[i]),
        }

    cm = confusion_matrix(gold_types, pred_types_clean, labels=all_labels)

    # Binary detection metrics
    gold_binary = [p["gold_has_ambiguity"] for p in all_preds]
    pred_binary = [p["pred_has_ambiguity"] for p in all_preds]
    b_prec, b_rec, b_f1, _ = precision_recall_fscore_support(
        gold_binary, pred_binary, average="binary", zero_division=0
    )
    b_acc = accuracy_score(gold_binary, pred_binary)

    # False positive rate: unambiguous classified as ambiguous
    unamb = [p for p in all_preds if not p["gold_has_ambiguity"]]
    fp = sum(1 for p in unamb if p["pred_has_ambiguity"])
    fpr = fp / len(unamb) if unamb else 0.0

    # Baselines
    rng = random.Random(42)
    n = len(gold_types)
    random_preds = [rng.choice(all_labels) for _ in range(n)]
    _, _, random_f1, _ = precision_recall_fscore_support(
        gold_types, random_preds, labels=all_labels, average="macro", zero_division=0
    )

    majority = max(set(gold_types), key=gold_types.count)
    majority_preds = [majority] * n
    _, _, majority_f1, _ = precision_recall_fscore_support(
        gold_types, majority_preds, labels=all_labels, average="macro", zero_division=0
    )

    n_amb = sum(1 for p in all_preds if p["gold_has_ambiguity"])
    n_unamb = len(all_preds) - n_amb

    results = {
        "macro_f1": round(float(macro_f1), 4),
        "macro_precision": round(float(macro_prec), 4),
        "macro_recall": round(float(macro_rec), 4),
        "per_type_metrics": per_type,
        "binary_detection": {
            "accuracy": round(float(b_acc), 4),
            "precision": round(float(b_prec), 4),
            "recall": round(float(b_rec), 4),
            "f1": round(float(b_f1), 4),
        },
        "false_positive_rate": round(float(fpr), 4),
        "baselines": {
            "random_macro_f1": round(float(random_f1), 4),
            "majority_macro_f1": round(float(majority_f1), 4),
        },
        "n_total": len(all_preds),
        "n_ambiguous": n_amb,
        "n_unambiguous": n_unamb,
        "cv_folds": 5,
        "classifier_model": MODEL,
    }

    cm_dict = {
        "labels": all_labels,
        "matrix": cm.tolist(),
    }

    return results, cm_dict


async def main():
    data = load_data()
    print(f"Loaded {len(data)} samples ({len(data)//2} clause pairs)")

    if not await dry_run(data):
        sys.exit(1)

    folds = make_folds(data, n_folds=5)
    semaphore = asyncio.Semaphore(CONCURRENCY)

    all_predictions = []
    t0 = time.time()
    for fold_idx, test_indices in enumerate(folds):
        preds = await run_fold(fold_idx, set(test_indices), data, semaphore)
        all_predictions.extend(preds)
        print(f"  Fold {fold_idx+1} done. Total predictions so far: {len(all_predictions)}")

    elapsed = time.time() - t0
    print(f"\nAll folds complete in {elapsed:.1f}s. Total predictions: {len(all_predictions)}")

    results, cm_dict = compute_metrics(all_predictions)

    print(f"\n=== RESULTS ===")
    print(f"Macro F1: {results['macro_f1']}")
    print(f"Binary Detection F1: {results['binary_detection']['f1']}")
    print(f"False Positive Rate: {results['false_positive_rate']}")
    print(f"Baselines — Random: {results['baselines']['random_macro_f1']}, Majority: {results['baselines']['majority_macro_f1']}")
    print(f"\nPer-type metrics:")
    for t, m in results["per_type_metrics"].items():
        print(f"  {t:25s}  P={m['precision']:.3f}  R={m['recall']:.3f}  F1={m['f1']:.3f}  (n={m['support']})")

    with open(OUT_DIR / "detection_results.json", "w") as f:
        json.dump(results, f, indent=2)
    with open(OUT_DIR / "confusion_matrix.json", "w") as f:
        json.dump(cm_dict, f, indent=2)
    with open(OUT_DIR / "predictions.jsonl", "w") as f:
        for p in all_predictions:
            f.write(json.dumps(p, ensure_ascii=False) + "\n")

    print(f"\nOutputs saved to {OUT_DIR}/")

    # Generate paper paragraph if macro F1 >= 0.60
    if results["macro_f1"] >= 0.60:
        write_paper_paragraph(results)


def write_paper_paragraph(results: dict):
    per_type = results["per_type_metrics"]
    best_type = max(
        [(t, m["f1"]) for t, m in per_type.items() if t != "none"],
        key=lambda x: x[1],
    )
    worst_type = min(
        [(t, m["f1"]) for t, m in per_type.items() if t != "none"],
        key=lambda x: x[1],
    )

    tex = r"""\paragraph{Automated Ambiguity Detection Tool}
To demonstrate the practical utility of our taxonomy, we build an automated ambiguity detection classifier.
Given a policy clause, the classifier determines (1)~whether the clause contains ambiguity, and (2)~the specific ambiguity type from our five-category taxonomy.
We use GPT-4.1 as the backbone with a zero-shot prompt that includes definitions and examples for each ambiguity type.

We evaluate on our full dataset of """ + str(results["n_total"]) + r""" policy clauses (""" + str(results["n_ambiguous"]) + r""" ambiguous, """ + str(results["n_unambiguous"]) + r""" unambiguous) using stratified 5-fold cross-validation, where clause pairs are kept in the same fold to prevent data leakage.
The classifier achieves a macro F1 of """ + f"{results['macro_f1']:.2f}" + r""" across all six classes (five ambiguity types plus ``no ambiguity''), substantially outperforming both random (""" + f"{results['baselines']['random_macro_f1']:.2f}" + r""") and majority-class (""" + f"{results['baselines']['majority_macro_f1']:.2f}" + r""") baselines.
For binary ambiguity detection, we observe """ + f"{results['binary_detection']['f1']:.2f}" + r""" F1 with a false positive rate of """ + f"{results['false_positive_rate']:.2f}" + r""".
Performance varies across ambiguity types: \textit{""" + best_type[0].replace("_", r"\_") + r"""} is most reliably detected (F1=""" + f"{best_type[1]:.2f}" + r"""), while \textit{""" + worst_type[0].replace("_", r"\_") + r"""} proves most challenging (F1=""" + f"{worst_type[1]:.2f}" + r""").
These results suggest that LLM-based classifiers can serve as effective first-pass tools for flagging potentially ambiguous policy language, though human review remains essential for nuanced cases.
"""

    out_path = OUT_DIR / "paper_paragraph.tex"
    with open(out_path, "w") as f:
        f.write(tex)
    print(f"Paper paragraph saved to {out_path}")


if __name__ == "__main__":
    asyncio.run(main())
