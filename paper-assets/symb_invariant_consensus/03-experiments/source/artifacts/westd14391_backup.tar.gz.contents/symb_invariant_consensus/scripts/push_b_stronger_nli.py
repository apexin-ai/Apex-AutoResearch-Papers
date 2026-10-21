#!/usr/bin/env python3
"""Push B: DeBERTa-v3-large NLI Verifier on ProofWriter 600
Model: MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli
Standalone NLI accuracy + combo with Mistral-7B SC and Qwen3-14B SC.
"""

import json
import os
import time
from collections import Counter
from scipy.stats import binomtest
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

NLI_MODEL = "/root/autodl-tmp/models/deberta-v3-large-mnli-fever-anli-ling-wanli"
PW_DATA = "/root/symb_invariant_consensus/data/proofwriter_full.json"
QWEN3_TRACE_DIR = "/root/symb_invariant_consensus/results/exp033_qwen3_14b_pw600_nonthinking/intermediates"
MISTRAL_VOTES_PATH = "/root/symb_invariant_consensus/data/mistral_pw600_sc_votes.json"
OUTPUT_DIR = "/root/symb_invariant_consensus/results/push_b_stronger_nli_verifier"
DEVICE = "cuda:0"
CLASSES = ["True", "False", "Unknown"]
WEIGHTS = [1, 3, 5]


def split_problem(problem_text):
    marker = "Determine whether the following statement is true, false, or unknown:"
    idx = problem_text.find(marker)
    if idx == -1:
        marker2 = "Determine whether the following statement is True, False, or Unknown:"
        idx = problem_text.find(marker2)
        if idx == -1:
            return problem_text, ""
        marker = marker2
    premise = problem_text[:idx].strip()
    hypothesis = problem_text[idx + len(marker):].strip()
    return premise, hypothesis


def mcnemar_test(correct_a, correct_b):
    b = sum(1 for a, bb in zip(correct_a, correct_b) if not a and bb)
    c = sum(1 for a, bb in zip(correct_a, correct_b) if a and not bb)
    n = b + c
    if n == 0:
        return 1.0, b, c
    result = binomtest(min(b, c), n, 0.5)
    return result.pvalue, b, c


def load_mistral_votes():
    with open(MISTRAL_VOTES_PATH) as f:
        raw = json.load(f)
    return {pid: {"True": v[0], "False": v[1], "Unknown": v[2]} for pid, v in raw.items()}


def load_qwen3_votes():
    files = sorted([f for f in os.listdir(QWEN3_TRACE_DIR) if f.endswith(".json")])
    votes = {}
    for f in files:
        pid = f.replace(".json", "")
        with open(os.path.join(QWEN3_TRACE_DIR, f)) as fh:
            d = json.load(fh)
        ac = d["sica_result"]["answer_counts"]
        clean = {k: v for k, v in ac.items() if k in CLASSES}
        votes[pid] = clean
    return votes


def sc_answer(votes):
    if not votes:
        return None
    return max(CLASSES, key=lambda x: votes.get(x, 0))


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Load ProofWriter data
    pw = json.load(open(PW_DATA))
    gt = {p["id"]: p["answer"] for p in pw}
    problems = {p["id"]: p["problem"] for p in pw}
    print(f"Loaded {len(pw)} ProofWriter problems")

    # Load SC votes
    print("Loading SC votes...")
    mistral_votes = load_mistral_votes()
    qwen3_votes = load_qwen3_votes()
    print(f"  Mistral: {len(mistral_votes)} problems")
    print(f"  Qwen3:   {len(qwen3_votes)} problems")

    # Verify SC baselines
    mistral_sc = {pid: sc_answer(mistral_votes.get(pid, {})) for pid in gt}
    qwen3_sc = {pid: sc_answer(qwen3_votes.get(pid, {})) for pid in gt}
    mistral_sc_correct = [mistral_sc[pid] == gt[pid] for pid in gt]
    qwen3_sc_correct = [qwen3_sc[pid] == gt[pid] for pid in gt]
    mistral_sc_acc = sum(mistral_sc_correct) / len(gt)
    qwen3_sc_acc = sum(qwen3_sc_correct) / len(gt)
    print(f"  Mistral SC: {sum(mistral_sc_correct)}/{len(gt)} = {mistral_sc_acc:.4f}")
    print(f"  Qwen3 SC:   {sum(qwen3_sc_correct)}/{len(gt)} = {qwen3_sc_acc:.4f}")

    # Load NLI model
    print(f"\nLoading NLI model: {NLI_MODEL}")
    tokenizer = AutoTokenizer.from_pretrained(NLI_MODEL)
    model = AutoModelForSequenceClassification.from_pretrained(NLI_MODEL)
    model.eval()
    model.to(DEVICE)
    print(f"Model on {DEVICE}")
    print(f"Label mapping: {model.config.id2label}")

    # Verify label mapping
    id2label = model.config.id2label
    actual_map = {}
    for idx, label in id2label.items():
        label_upper = label.upper()
        if "ENTAIL" in label_upper:
            actual_map[int(idx)] = "True"
        elif "CONTRA" in label_upper:
            actual_map[int(idx)] = "False"
        else:
            actual_map[int(idx)] = "Unknown"
    print(f"Resolved mapping: {actual_map}")

    # Run NLI inference
    print("\nRunning NLI inference...")
    nli_preds = {}
    nli_probs = {}
    pids = sorted(gt.keys())
    t0 = time.time()

    batch_size = 16
    for i in range(0, len(pids), batch_size):
        batch_pids = pids[i:i + batch_size]
        premises = []
        hypotheses = []
        for pid in batch_pids:
            p, h = split_problem(problems[pid])
            premises.append(p)
            hypotheses.append(h)

        inputs = tokenizer(
            premises, hypotheses,
            return_tensors="pt", truncation=True, max_length=512, padding=True
        ).to(DEVICE)

        with torch.no_grad():
            logits = model(**inputs).logits
        probs = torch.softmax(logits, dim=-1).cpu().numpy()

        for j, pid in enumerate(batch_pids):
            prob_dict = {actual_map[k]: float(probs[j, k]) for k in actual_map}
            nli_probs[pid] = {c: round(prob_dict.get(c, 0), 6) for c in CLASSES}
            nli_preds[pid] = max(CLASSES, key=lambda x: prob_dict.get(x, 0))

        if (i + batch_size) % 100 < batch_size:
            print(f"  {min(i + batch_size, len(pids))}/{len(pids)} ({time.time() - t0:.1f}s)")

    elapsed = time.time() - t0
    print(f"NLI done in {elapsed:.1f}s")

    # Standalone NLI accuracy
    nli_correct = [nli_preds[pid] == gt[pid] for pid in pids]
    nli_acc = sum(nli_correct) / len(pids)

    # Per-class breakdown
    gt_dist = Counter(gt[pid] for pid in pids)
    pred_dist = Counter(nli_preds[pid] for pid in pids)
    per_class = {}
    for cls in CLASSES:
        cls_pids = [pid for pid in pids if gt[pid] == cls]
        cls_correct = sum(1 for pid in cls_pids if nli_preds[pid] == cls)
        cls_pred = sum(1 for pid in pids if nli_preds[pid] == cls)
        per_class[cls] = {
            "n": len(cls_pids),
            "correct": cls_correct,
            "accuracy": round(cls_correct / len(cls_pids), 4) if cls_pids else 0,
            "precision": round(cls_correct / cls_pred, 4) if cls_pred > 0 else 0,
            "recall": round(cls_correct / len(cls_pids), 4) if cls_pids else 0,
        }

    print(f"\nStandalone NLI: {sum(nli_correct)}/{len(pids)} = {nli_acc:.4f}")
    for cls in CLASSES:
        pc = per_class[cls]
        print(f"  {cls}: {pc['correct']}/{pc['n']} = {pc['accuracy']:.4f} (P={pc['precision']:.4f} R={pc['recall']:.4f})")
    print(f"  Pred distribution: {dict(pred_dist)}")

    # Combo computation
    def compute_combo(sc_votes_dict, sc_correct_list, sc_acc, generator_name):
        print(f"\n=== Combo: {generator_name} ===")
        print(f"  SC baseline: {sc_acc:.4f}")
        results = {}
        for w in WEIGHTS:
            combo_answers = []
            for pid in pids:
                sv = sc_votes_dict.get(pid, {})
                np_ = nli_probs[pid]
                combined = {c: sv.get(c, 0) + w * np_.get(c, 0) for c in CLASSES}
                combo_answers.append(max(CLASSES, key=lambda x: combined[x]))

            combo_correct = [ca == gt[pid] for ca, pid in zip(combo_answers, pids)]
            combo_acc = sum(combo_correct) / len(pids)
            delta = combo_acc - sc_acc
            p, b, c = mcnemar_test(sc_correct_list, combo_correct)

            results[f"w{w}"] = {
                "accuracy": round(combo_acc, 4),
                "correct": sum(combo_correct),
                "delta_pp": round(delta * 100, 2),
                "mcnemar_p": round(p, 6),
                "discordant": [b, c],
            }
            print(f"  w={w}: {combo_acc:.4f} ({sum(combo_correct)}/{len(pids)}), "
                  f"delta={delta * 100:+.2f}pp, p={p:.4f}, disc=({b},{c})")
        return results

    mistral_combo = compute_combo(mistral_votes, mistral_sc_correct, mistral_sc_acc, "Mistral-7B")
    qwen3_combo = compute_combo(qwen3_votes, qwen3_sc_correct, qwen3_sc_acc, "Qwen3-14B")

    # Save results
    output = {
        "experiment": "Push B: Stronger NLI Verifier (DeBERTa-v3-large) on ProofWriter",
        "verifier_model": "MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli",
        "verifier_model_local": NLI_MODEL,
        "dataset": "ProofWriter-D5-OWA (600 questions)",
        "device": DEVICE,
        "inference_time_s": round(elapsed, 1),
        "standalone_accuracy": round(nli_acc, 4),
        "standalone_correct": sum(nli_correct),
        "standalone_per_class": per_class,
        "gt_distribution": dict(gt_dist),
        "pred_distribution": dict(pred_dist),
        "comparison_with_deberta_base": {
            "deberta_base_mnli_accuracy": 0.3617,
            "deberta_v3_large_mnli_accuracy": round(nli_acc, 4),
            "note": "deberta-base-mnli standalone was 36.17% (Dir-K result)"
        },
        "mistral_combo": {
            "generator": "Mistral-7B-Instruct-v0.3",
            "sc_baseline": round(mistral_sc_acc, 4),
            "sc_correct": sum(mistral_sc_correct),
            **mistral_combo,
        },
        "qwen3_combo": {
            "generator": "Qwen3-14B (non-thinking)",
            "sc_baseline": round(qwen3_sc_acc, 4),
            "sc_correct": sum(qwen3_sc_correct),
            **qwen3_combo,
        },
        "per_problem": {
            pid: {
                "gold": gt[pid],
                "nli_pred": nli_preds[pid],
                "nli_probs": nli_probs[pid],
                "nli_correct": nli_preds[pid] == gt[pid],
                "mistral_sc": mistral_sc[pid],
                "mistral_sc_correct": mistral_sc[pid] == gt[pid],
                "qwen3_sc": qwen3_sc[pid],
                "qwen3_sc_correct": qwen3_sc[pid] == gt[pid],
            }
            for pid in pids
        },
    }

    out_path = os.path.join(OUTPUT_DIR, "results.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
