#!/usr/bin/env python3
"""Evaluate fine-tuned DeBERTa on ProofWriter depth-5 test set.
Standalone accuracy + combo with LLM SC votes.

Usage:
    python scripts/eval_finetuned_nli.py \
        --model-path checkpoints/deberta-large-pw-finetuned/best
    python scripts/eval_finetuned_nli.py \
        --model-path /root/autodl-tmp/models/deberta-large-mnli \
        --sc-sources llama8b qwen14b mistral
"""

# Environment setup for westd-16639:
#   export CUDA_VISIBLE_DEVICES=<free_gpu_id>
#   export LD_LIBRARY_PATH=/root/miniconda3/lib/python3.12/site-packages/nvidia/cu13/lib:$LD_LIBRARY_PATH


import argparse
import json
import os
import time
from collections import Counter
import numpy as np
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.stats import binomtest

PW_DATA_PATH = "/root/symb_invariant_consensus/data/proofwriter_full.json"
RESULTS_DIR = "/root/symb_invariant_consensus/results"
CLASSES = sorted(["True", "False", "Unknown"])
WEIGHTS = [1, 3, 5]

SC_SOURCES = {
    "llama8b": {
        "path": os.path.join(RESULTS_DIR, "exp048_llama8b_pw600/exp048_results.json"),
        "name": "LLaMA-3.1-8B-Instruct",
        "format": "results_list",
    },
    "qwen14b": {
        "path": os.path.join(RESULTS_DIR, "exp032_qwen25_14b_pw600/results.json"),
        "name": "Qwen2.5-14B-Instruct",
        "format": "results_list",
    },
    "mistral": {
        "path": "/root/symb_invariant_consensus/data/mistral_pw600_sc_votes.json",
        "name": "Mistral-7B-Instruct-v0.3",
        "format": "vote_dict",
    },
}


def parse_pw_problem(text):
    for m in [
        "Determine whether the following statement is true, false, or unknown:\n",
        "Determine whether the following statement is True, False, or Unknown:\n",
    ]:
        i = text.find(m)
        if i != -1:
            return text[:i].strip(), text[i + len(m):].strip()
    return text, ""


def sc_answer(votes):
    if not votes:
        return None
    return max(CLASSES, key=lambda x: votes.get(x, 0))


def mcnemar_exact(correct_a, correct_b):
    b = sum(1 for a, bb in zip(correct_a, correct_b) if not a and bb)
    c = sum(1 for a, bb in zip(correct_a, correct_b) if a and not bb)
    n = b + c
    if n == 0:
        return 1.0, b, c
    return binomtest(min(b, c), n, 0.5).pvalue, b, c


def load_sc_votes(source_key):
    src = SC_SOURCES[source_key]
    with open(src["path"]) as f:
        raw = json.load(f)

    votes = {}
    if src["format"] == "results_list":
        for r in raw["results"]:
            pid = r["problem_id"]
            votes[pid] = r["sc_vote_distribution"]
    elif src["format"] == "vote_dict":
        for pid, counts in raw.items():
            votes[pid] = {"True": counts[0], "False": counts[1], "Unknown": counts[2]}

    return votes, src["name"]


def main():
    parser = argparse.ArgumentParser(description="Evaluate fine-tuned DeBERTa on ProofWriter")
    parser.add_argument("--model-path", required=True, help="Path to fine-tuned checkpoint")
    parser.add_argument("--sc-sources", nargs="+", default=["llama8b", "qwen14b"],
                        choices=list(SC_SOURCES.keys()))
    parser.add_argument("--weights", nargs="+", type=int, default=WEIGHTS)
    parser.add_argument("--max-length", type=int, default=512)
    parser.add_argument("--batch-size", type=int, default=32)
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--output-dir", default=None)
    args = parser.parse_args()

    if args.output_dir is None:
        model_name = os.path.basename(args.model_path.rstrip("/"))
        if model_name == "best":
            model_name = os.path.basename(os.path.dirname(args.model_path.rstrip("/")))
        args.output_dir = os.path.join(RESULTS_DIR, f"eval_finetuned_{model_name}")
    os.makedirs(args.output_dir, exist_ok=True)

    print(f"Loading model: {args.model_path}")
    tokenizer = AutoTokenizer.from_pretrained(args.model_path)
    model = AutoModelForSequenceClassification.from_pretrained(args.model_path)
    model.eval()
    device = args.device if torch.cuda.is_available() else "cpu"
    model.to(device)
    print(f"Device: {device}, id2label: {model.config.id2label}")

    nli_to_pw = {}
    for idx, label in model.config.id2label.items():
        lu = label.upper()
        if "ENTAIL" in lu:
            nli_to_pw[int(idx)] = "True"
        elif "CONTRA" in lu:
            nli_to_pw[int(idx)] = "False"
        else:
            nli_to_pw[int(idx)] = "Unknown"
    print(f"NLI->PW: {nli_to_pw}")

    with open(PW_DATA_PATH) as f:
        pw_data = json.load(f)
    gt = {p["id"]: p["answer"] for p in pw_data}
    problems = {p["id"]: p["problem"] for p in pw_data}
    pids = list(gt.keys())
    total = len(pids)
    print(f"Loaded {total} problems")

    # NLI inference (batched)
    print("\nRunning NLI inference...")
    nli_preds = {}
    nli_probs = {}
    t0 = time.time()

    for i in range(0, total, args.batch_size):
        batch_pids = pids[i:i + args.batch_size]
        premises, hypotheses = [], []
        for pid in batch_pids:
            p, h = parse_pw_problem(problems[pid])
            premises.append(p)
            hypotheses.append(h)

        inputs = tokenizer(premises, hypotheses, return_tensors="pt", truncation=True,
                           max_length=args.max_length, padding=True).to(device)
        with torch.no_grad():
            outputs = model(**inputs)

        probs = torch.softmax(outputs.logits, dim=-1).cpu().numpy()
        for j, pid in enumerate(batch_pids):
            pred_idx = int(probs[j].argmax())
            nli_preds[pid] = nli_to_pw[pred_idx]
            nli_probs[pid] = {nli_to_pw[k]: round(float(probs[j][k]), 4) for k in nli_to_pw}

        done = min(i + args.batch_size, total)
        if done % 200 == 0 or done == total:
            print(f"  {done}/{total}")

    elapsed = time.time() - t0
    print(f"Inference: {elapsed:.1f}s ({total/elapsed:.1f} samples/s)")

    # Standalone metrics
    nli_correct_list = [nli_preds[pid] == gt[pid] for pid in pids]
    nli_acc = sum(nli_correct_list) / total

    gt_dist = Counter(gt[pid] for pid in pids)
    pred_dist = Counter(nli_preds[pid] for pid in pids)
    per_class = {}
    for cls in CLASSES:
        cls_pids = [pid for pid in pids if gt[pid] == cls]
        if not cls_pids:
            continue
        cls_correct = sum(1 for pid in cls_pids if nli_preds[pid] == cls)
        cls_pred = sum(1 for pid in pids if nli_preds[pid] == cls)
        prec = cls_correct / cls_pred if cls_pred > 0 else 0
        rec = cls_correct / len(cls_pids)
        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0
        per_class[cls] = {
            "n": len(cls_pids), "correct": cls_correct,
            "accuracy": round(rec, 4), "precision": round(prec, 4),
            "recall": round(rec, 4), "f1": round(f1, 4),
        }

    print(f"\n=== Standalone: {nli_acc:.4f} ({sum(nli_correct_list)}/{total}) ===")
    for cls in CLASSES:
        if cls in per_class:
            pc = per_class[cls]
            print(f"  {cls}: {pc['correct']}/{pc['n']} = {pc['accuracy']:.4f} "
                  f"(P={pc['precision']:.4f} R={pc['recall']:.4f} F1={pc['f1']:.4f})")
    print(f"  Pred dist: {dict(pred_dist)}")

    # Combo with each SC source
    combo_all = {}
    for src_key in args.sc_sources:
        if not os.path.exists(SC_SOURCES[src_key]["path"]):
            print(f"\nSkipping {src_key}: file not found at {SC_SOURCES[src_key]['path']}")
            continue

        sc_votes, gen_name = load_sc_votes(src_key)
        sc_answers_dict = {pid: sc_answer(sc_votes.get(pid, {})) for pid in pids}
        sc_correct_list = [sc_answers_dict[pid] == gt[pid] for pid in pids]
        sc_acc = sum(sc_correct_list) / total

        nli_right_sc_wrong = sum(
            1 for pid in pids
            if nli_preds[pid] == gt[pid] and sc_answers_dict[pid] != gt[pid]
        )
        sc_right_nli_wrong = sum(
            1 for pid in pids
            if sc_answers_dict[pid] == gt[pid] and nli_preds[pid] != gt[pid]
        )
        both_right = sum(
            1 for pid in pids
            if nli_preds[pid] == gt[pid] and sc_answers_dict[pid] == gt[pid]
        )
        both_wrong = sum(
            1 for pid in pids
            if nli_preds[pid] != gt[pid] and sc_answers_dict[pid] != gt[pid]
        )

        print(f"\n=== Combo: {gen_name} (SC={sc_acc:.4f}) ===")
        print(f"  NLI↑SC↓={nli_right_sc_wrong}, SC↑NLI↓={sc_right_nli_wrong}, "
              f"both↑={both_right}, both↓={both_wrong}")

        combo_results = {}
        for w in args.weights:
            combo_answers = []
            for pid in pids:
                sv = sc_votes.get(pid, {})
                combo_v = {c: sv.get(c, 0) for c in CLASSES}
                combo_v[nli_preds[pid]] = combo_v.get(nli_preds[pid], 0) + w
                combo_answers.append(max(CLASSES, key=lambda x: combo_v.get(x, 0)))

            combo_correct_list = [ca == gt[pid] for ca, pid in zip(combo_answers, pids)]
            combo_acc = sum(combo_correct_list) / total
            delta = combo_acc - sc_acc
            p_val, b, c = mcnemar_exact(sc_correct_list, combo_correct_list)

            combo_results[f"w{w}"] = {
                "accuracy": round(combo_acc, 4),
                "correct": sum(combo_correct_list),
                "delta_pp": round(delta * 100, 2),
                "mcnemar_p": round(p_val, 6),
                "discordant": [b, c],
            }
            sig = "***" if p_val < 0.001 else "**" if p_val < 0.01 else "*" if p_val < 0.05 else ""
            print(f"  w={w}: {combo_acc:.4f} ({sum(combo_correct_list)}/{total}), "
                  f"delta={delta*100:+.2f}pp, p={p_val:.4f} {sig}")

        # Agreement analysis
        agree = sum(1 for pid in pids if nli_preds[pid] == sc_answers_dict[pid])
        disagree = total - agree
        agree_correct = sum(
            1 for pid in pids
            if nli_preds[pid] == sc_answers_dict[pid] == gt[pid]
        )
        print(f"  Agree: {agree}/{total} ({agree/total:.4f}), "
              f"acc when agree={agree_correct/agree:.4f}" if agree > 0 else "")
        print(f"  Disagree: {disagree}, NLI right={nli_right_sc_wrong}, SC right={sc_right_nli_wrong}")

        combo_all[src_key] = {
            "generator": gen_name,
            "sc_baseline": round(sc_acc, 4),
            "sc_correct": sum(sc_correct_list),
            "complementarity": {
                "nli_right_sc_wrong": nli_right_sc_wrong,
                "sc_right_nli_wrong": sc_right_nli_wrong,
                "both_right": both_right,
                "both_wrong": both_wrong,
            },
            "agreement": {
                "agree": agree,
                "disagree": disagree,
                "agreement_rate": round(agree / total, 4),
                "agree_accuracy": round(agree_correct / agree, 4) if agree > 0 else 0,
            },
            **combo_results,
        }

    # Save results
    output = {
        "model_path": args.model_path,
        "dataset": "ProofWriter-D5-600",
        "n_questions": total,
        "inference_time_s": round(elapsed, 1),
        "standalone": {
            "accuracy": round(nli_acc, 4),
            "correct": sum(nli_correct_list),
            "per_class": per_class,
            "gt_distribution": dict(gt_dist),
            "pred_distribution": dict(pred_dist),
        },
        "combo": combo_all,
        "per_question": {
            pid: {
                "gold": gt[pid],
                "nli_pred": nli_preds[pid],
                "nli_probs": nli_probs[pid],
                "nli_correct": nli_preds[pid] == gt[pid],
            }
            for pid in pids
        },
    }

    out_path = os.path.join(args.output_dir, "results.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()
