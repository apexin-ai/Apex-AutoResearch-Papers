"""exp32: Strategy Prediction Analysis — linking persuasion head predictions to detection correctness.

Analyses:
1. Detection correctness vs strategy prediction accuracy (correct detections vs misses)
2. Per-strategy confusion matrix (GT vs predicted, per-class P/R/F1)
3. Per-strategy detection rate (which strategies are easier/harder to detect)
"""

import os
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

import sys
import json
import numpy as np
import torch
from pathlib import Path
from collections import defaultdict, Counter

sys.path.insert(0, "/root/persuasion_turn_jailbreak_detect")
from src.models.deberta_multitask import DeBERTaMultiTask
from src.models.gru_classifier import GRUClassifier
from transformers import AutoTokenizer

PROJ = Path("/root/persuasion_turn_jailbreak_detect")
DEVICE = torch.device("cuda:0")
MODEL_NAME = "microsoft/deberta-v3-base"
MAX_LENGTH = 256

STRATEGY_NAMES = {
    0: "none", 1: "rapport_building", 2: "authority_appeal",
    3: "emotional_manipulation", 4: "logical_reframing", 5: "role_assignment",
    6: "gradual_escalation", 7: "obfuscation", 8: "direct_request",
}

SEEDS = [42, 123, 456]
CKPT_PATHS = {
    seed: {
        "deberta": PROJ / f"checkpoints/exp16/9class_seed{seed}/best/model.pt",
        "gru": PROJ / f"checkpoints/exp16/9class_gru_seed{seed}/treatment/best.pt",
        "tokenizer": PROJ / f"checkpoints/exp16/9class_seed{seed}/best/",
    }
    for seed in SEEDS
}


def load_jsonl(path):
    with open(path) as f:
        return [json.loads(l) for l in f if l.strip()]


def get_gt_strategy_labels(conv):
    """Extract ground truth strategy labels for user turns in model class space (0-8).
    DD data: intended_strategy + 1.  AA data: persuasion_strategy.  Benign: 0."""
    labels = []
    is_jailbreak = conv["label"] == "jailbreak"
    for turn in conv["turns"]:
        if turn["role"] != "user":
            continue
        if not is_jailbreak:
            labels.append(0)
        elif "persuasion_strategy" in turn and turn["persuasion_strategy"] is not None:
            labels.append(turn["persuasion_strategy"])
        elif "intended_strategy" in turn:
            labels.append(turn["intended_strategy"] + 1)
        else:
            labels.append(0)
    return labels


def get_conv_label(conv):
    return 1 if conv["label"] == "jailbreak" else 0


def extract_user_turns(conv):
    return [t["content"] for t in conv["turns"] if t["role"] == "user"]


def load_models(seed):
    paths = CKPT_PATHS[seed]
    tokenizer = AutoTokenizer.from_pretrained(str(paths["tokenizer"]))

    deberta = DeBERTaMultiTask(model_name=MODEL_NAME, num_persuasion_classes=9)
    sd = torch.load(paths["deberta"], map_location="cpu")
    deberta.load_state_dict(sd)
    deberta.to(DEVICE).eval()

    gru = GRUClassifier(input_dim=768, hidden_dim=256, num_layers=2, dropout=0.3)
    gru.load_state_dict(torch.load(paths["gru"], map_location="cpu"))
    gru.to(DEVICE).eval()

    return tokenizer, deberta, gru


@torch.no_grad()
def inference_conversation(tokenizer, deberta, gru, conv):
    """Run full inference on one conversation. Returns per-turn and conv-level predictions."""
    user_turns = extract_user_turns(conv)
    if not user_turns:
        return 0, 0.0, [], [], [], []

    enc = tokenizer(
        user_turns, max_length=MAX_LENGTH, padding=True, truncation=True, return_tensors="pt"
    ).to(DEVICE)

    outputs = deberta(input_ids=enc["input_ids"], attention_mask=enc["attention_mask"])
    cls_embs = outputs["cls_embedding"]
    persuasion_logits = outputs["persuasion_logits"]
    intent_logits = outputs["intent_logits"]

    strategy_probs = torch.softmax(persuasion_logits, dim=-1)
    strategy_preds = persuasion_logits.argmax(dim=-1).cpu().tolist()

    intent_probs = torch.softmax(intent_logits, dim=-1)
    intent_preds = intent_logits.argmax(dim=-1).cpu().tolist()

    embs_batch = cls_embs.unsqueeze(0)
    lengths = torch.tensor([cls_embs.size(0)], dtype=torch.long).to(DEVICE)
    gru_logits = gru(embs_batch, lengths)
    conv_pred = gru_logits.argmax(dim=1).item()
    conv_prob = torch.softmax(gru_logits, dim=-1)[0, 1].item()

    return (
        conv_pred, conv_prob,
        strategy_preds, strategy_probs.cpu().tolist(),
        intent_preds, intent_probs[:, 1].cpu().tolist(),
    )


def run_inference(tokenizer, deberta, gru, convs):
    results = []
    for conv in convs:
        gt_label = get_conv_label(conv)
        gt_strategies = get_gt_strategy_labels(conv)
        conv_pred, conv_prob, strat_preds, strat_probs, intent_preds, intent_probs = \
            inference_conversation(tokenizer, deberta, gru, conv)
        results.append({
            "conv_id": conv["conversation_id"],
            "gt_label": gt_label,
            "pred_label": conv_pred,
            "pred_prob": conv_prob,
            "correct_detection": int(gt_label == conv_pred),
            "gt_strategies": gt_strategies,
            "pred_strategies": strat_preds,
            "strategy_probs": strat_probs,
            "intent_preds": intent_preds,
            "intent_probs": intent_probs,
            "attack_type": conv.get("attack_type", "benign"),
        })
    return results


def compute_analysis(results):
    """Compute all three analyses from inference results."""
    analysis = {}
    jailbreak_results = [r for r in results if r["gt_label"] == 1]
    benign_results = [r for r in results if r["gt_label"] == 0]
    correct_detected = [r for r in jailbreak_results if r["correct_detection"] == 1]
    missed = [r for r in jailbreak_results if r["correct_detection"] == 0]

    # ---- helpers ----
    def strategy_accuracy(result_list):
        correct = total = 0
        for r in result_list:
            for gt, pred in zip(r["gt_strategies"], r["pred_strategies"]):
                correct += int(gt == pred)
                total += 1
        return correct / total if total > 0 else 0.0

    def avg_max_confidence(result_list):
        vals = [max(p) for r in result_list for p in r["strategy_probs"]]
        return float(np.mean(vals)) if vals else 0.0

    def avg_gt_confidence(result_list):
        vals = [p[gt] for r in result_list for gt, p in zip(r["gt_strategies"], r["strategy_probs"])]
        return float(np.mean(vals)) if vals else 0.0

    # ---- Analysis 1: Detection correctness vs strategy prediction accuracy ----
    a1 = {
        "n_jailbreak": len(jailbreak_results),
        "n_correct_detected": len(correct_detected),
        "n_missed": len(missed),
        "correct_detected_strategy_acc": round(strategy_accuracy(correct_detected), 4),
        "missed_strategy_acc": round(strategy_accuracy(missed), 4) if missed else None,
        "correct_detected_max_conf": round(avg_max_confidence(correct_detected), 4),
        "missed_max_conf": round(avg_max_confidence(missed), 4) if missed else None,
        "correct_detected_gt_conf": round(avg_gt_confidence(correct_detected), 4),
        "missed_gt_conf": round(avg_gt_confidence(missed), 4) if missed else None,
    }

    # Correlation: jailbreak detection probability vs per-conv strategy accuracy
    if len(jailbreak_results) > 2:
        from scipy.stats import pearsonr
        probs = []
        accs = []
        for r in jailbreak_results:
            probs.append(r["pred_prob"])
            n = len(r["gt_strategies"])
            if n > 0:
                acc = sum(1 for g, p in zip(r["gt_strategies"], r["pred_strategies"]) if g == p) / n
            else:
                acc = 0.0
            accs.append(acc)
        corr, pval = pearsonr(probs, accs)
        a1["correlation_detection_prob_vs_strategy_acc"] = {
            "pearson_r": round(float(corr), 4),
            "p_value": round(float(pval), 6),
        }

    analysis["detection_vs_strategy"] = a1

    # ---- Analysis 2: Per-strategy confusion matrix ----
    all_gt = []
    all_pred = []
    for r in results:
        all_gt.extend(r["gt_strategies"])
        all_pred.extend(r["pred_strategies"])

    gt_arr = np.array(all_gt)
    pred_arr = np.array(all_pred)
    cm = np.zeros((9, 9), dtype=int)
    for g, p in zip(all_gt, all_pred):
        cm[g][p] += 1

    per_class = {}
    for cid in range(9):
        gt_mask = gt_arr == cid
        pred_mask = pred_arr == cid
        tp = int((gt_mask & pred_mask).sum())
        fp = int((~gt_mask & pred_mask).sum())
        fn = int((gt_mask & ~pred_mask).sum())
        prec = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        rec = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0
        per_class[STRATEGY_NAMES[cid]] = {
            "precision": round(prec, 4), "recall": round(rec, 4),
            "f1": round(f1, 4), "support": int(gt_mask.sum()),
        }

    overall_acc = int((gt_arr == pred_arr).sum()) / len(gt_arr) if len(gt_arr) > 0 else 0.0

    # Macro F1 (excluding "none" if desired, but include all for completeness)
    macro_f1 = np.mean([v["f1"] for v in per_class.values()])

    # Jailbreak-only strategy accuracy (exclude benign turns)
    jb_gt = []
    jb_pred = []
    for r in jailbreak_results:
        jb_gt.extend(r["gt_strategies"])
        jb_pred.extend(r["pred_strategies"])
    jb_acc = sum(1 for g, p in zip(jb_gt, jb_pred) if g == p) / len(jb_gt) if jb_gt else 0.0

    analysis["strategy_prediction"] = {
        "overall_accuracy": round(float(overall_acc), 4),
        "jailbreak_only_accuracy": round(float(jb_acc), 4),
        "macro_f1": round(float(macro_f1), 4),
        "per_class": per_class,
        "confusion_matrix": cm.tolist(),
        "confusion_matrix_labels": [STRATEGY_NAMES[i] for i in range(9)],
    }

    # ---- Analysis 3: Per-strategy detection rate ----
    # By dominant strategy
    dominant_detection = defaultdict(lambda: {"detected": 0, "total": 0})
    for r in jailbreak_results:
        non_zero = [s for s in r["gt_strategies"] if s > 0]
        dominant = Counter(non_zero).most_common(1)[0][0] if non_zero else 0
        sname = STRATEGY_NAMES[dominant]
        dominant_detection[sname]["total"] += 1
        if r["correct_detection"] == 1:
            dominant_detection[sname]["detected"] += 1

    per_dominant = {}
    for sname in sorted(dominant_detection):
        c = dominant_detection[sname]
        per_dominant[sname] = {
            "detection_rate": round(c["detected"] / c["total"], 4) if c["total"] > 0 else 0.0,
            "detected": c["detected"], "total": c["total"],
        }
    analysis["per_dominant_strategy_detection"] = per_dominant

    # By any strategy present
    any_detection = defaultdict(lambda: {"detected": 0, "total": 0})
    for r in jailbreak_results:
        present = set(s for s in r["gt_strategies"] if s > 0)
        for s in present:
            sname = STRATEGY_NAMES[s]
            any_detection[sname]["total"] += 1
            if r["correct_detection"] == 1:
                any_detection[sname]["detected"] += 1

    per_any = {}
    for sname in sorted(any_detection):
        c = any_detection[sname]
        per_any[sname] = {
            "detection_rate": round(c["detected"] / c["total"], 4) if c["total"] > 0 else 0.0,
            "detected": c["detected"], "total": c["total"],
        }
    analysis["per_any_strategy_detection"] = per_any

    # Benign FPR
    if benign_results:
        fp = sum(1 for r in benign_results if r["pred_label"] == 1)
        analysis["benign_fpr"] = round(fp / len(benign_results), 4)

    # Missed conversation details
    if missed:
        analysis["missed_details"] = []
        for r in missed:
            gt_names = [STRATEGY_NAMES[s] for s in r["gt_strategies"]]
            pred_names = [STRATEGY_NAMES[s] for s in r["pred_strategies"]]
            analysis["missed_details"].append({
                "conv_id": r["conv_id"],
                "attack_type": r["attack_type"],
                "pred_prob": round(r["pred_prob"], 4),
                "gt_strategies": gt_names,
                "pred_strategies": pred_names,
                "strategy_match": [int(g == p) for g, p in zip(r["gt_strategies"], r["pred_strategies"])],
            })

    return analysis


def print_summary(ds_name, analysis):
    d = analysis["detection_vs_strategy"]
    print(f"\n  [{ds_name}] Detection: {d['n_correct_detected']}/{d['n_jailbreak']} "
          f"(missed={d['n_missed']})")
    print(f"    Strategy acc (detected): {d['correct_detected_strategy_acc']}")
    print(f"    Strategy acc (missed):   {d['missed_strategy_acc']}")
    print(f"    GT conf (detected): {d['correct_detected_gt_conf']}")
    print(f"    GT conf (missed):   {d['missed_gt_conf']}")
    if "correlation_detection_prob_vs_strategy_acc" in d:
        c = d["correlation_detection_prob_vs_strategy_acc"]
        print(f"    Correlation(det_prob, strat_acc): r={c['pearson_r']}, p={c['p_value']}")

    sp = analysis["strategy_prediction"]
    print(f"    Strategy overall acc: {sp['overall_accuracy']}, "
          f"jailbreak-only: {sp['jailbreak_only_accuracy']}, macro_f1: {sp['macro_f1']}")

    print(f"    Per-class:")
    for cls_name, m in sp["per_class"].items():
        if m["support"] > 0:
            print(f"      {cls_name:25s} P={m['precision']:.3f} R={m['recall']:.3f} "
                  f"F1={m['f1']:.3f} n={m['support']}")

    print(f"    Per-dominant-strategy detection rate:")
    for sname, v in analysis["per_dominant_strategy_detection"].items():
        print(f"      {sname:25s} {v['detected']}/{v['total']} = {v['detection_rate']:.3f}")


def main():
    print("=== exp32: Strategy Prediction Analysis ===")

    dd_convs = load_jsonl(PROJ / "data/generated/deceptive_delight_all.jsonl")
    aa_convs = load_jsonl(PROJ / "data/generated/actorattack_all.jsonl")
    test_data = load_jsonl(PROJ / "data/plan_002_splits/test.jsonl")
    test_benign = [c for c in test_data if c["label"] == "benign"]

    dd_test = dd_convs + test_benign
    aa_test = aa_convs + test_benign

    print(f"DD OOD: {len(dd_convs)} jailbreak + {len(test_benign)} benign = {len(dd_test)}")
    print(f"AA OOD: {len(aa_convs)} jailbreak + {len(test_benign)} benign = {len(aa_test)}")

    all_seed_results = {}

    for seed in SEEDS:
        print(f"\n{'='*50}")
        print(f"Seed {seed}")
        print(f"{'='*50}")
        tokenizer, deberta, gru = load_models(seed)

        print("  DD OOD inference...")
        dd_results = run_inference(tokenizer, deberta, gru, dd_test)
        dd_analysis = compute_analysis(dd_results)
        print_summary("DD OOD", dd_analysis)

        print("  AA OOD inference...")
        aa_results = run_inference(tokenizer, deberta, gru, aa_test)
        aa_analysis = compute_analysis(aa_results)
        print_summary("AA OOD", aa_analysis)

        all_seed_results[f"seed_{seed}"] = {
            "dd_ood": dd_analysis,
            "aa_ood": aa_analysis,
        }

        del deberta, gru
        torch.cuda.empty_cache()

    # ---- Aggregate across seeds ----
    print(f"\n{'='*60}")
    print("AGGREGATED ACROSS SEEDS")
    print(f"{'='*60}")

    aggregated = {}
    for ds_name in ["dd_ood", "aa_ood"]:
        vals = {
            "strategy_acc": [],
            "jb_strategy_acc": [],
            "strategy_acc_detected": [],
            "strategy_acc_missed": [],
            "gt_conf_detected": [],
            "gt_conf_missed": [],
            "n_missed": [],
            "macro_f1": [],
        }
        per_class_f1s = defaultdict(list)
        per_dominant_rates = defaultdict(list)

        for seed in SEEDS:
            r = all_seed_results[f"seed_{seed}"][ds_name]
            vals["strategy_acc"].append(r["strategy_prediction"]["overall_accuracy"])
            vals["jb_strategy_acc"].append(r["strategy_prediction"]["jailbreak_only_accuracy"])
            vals["macro_f1"].append(r["strategy_prediction"]["macro_f1"])
            vals["strategy_acc_detected"].append(r["detection_vs_strategy"]["correct_detected_strategy_acc"])
            vals["n_missed"].append(r["detection_vs_strategy"]["n_missed"])
            if r["detection_vs_strategy"]["missed_strategy_acc"] is not None:
                vals["strategy_acc_missed"].append(r["detection_vs_strategy"]["missed_strategy_acc"])
            if r["detection_vs_strategy"]["correct_detected_gt_conf"] is not None:
                vals["gt_conf_detected"].append(r["detection_vs_strategy"]["correct_detected_gt_conf"])
            if r["detection_vs_strategy"]["missed_gt_conf"] is not None:
                vals["gt_conf_missed"].append(r["detection_vs_strategy"]["missed_gt_conf"])
            for cls_name, m in r["strategy_prediction"]["per_class"].items():
                per_class_f1s[cls_name].append(m["f1"])
            for sname, v in r["per_dominant_strategy_detection"].items():
                per_dominant_rates[sname].append(v["detection_rate"])

        def fmt(vs):
            return f"{np.mean(vs):.4f}±{np.std(vs):.4f}" if vs else "N/A"

        agg = {
            "strategy_acc": f"{np.mean(vals['strategy_acc']):.4f}±{np.std(vals['strategy_acc']):.4f}",
            "jb_strategy_acc": f"{np.mean(vals['jb_strategy_acc']):.4f}±{np.std(vals['jb_strategy_acc']):.4f}",
            "macro_f1": f"{np.mean(vals['macro_f1']):.4f}±{np.std(vals['macro_f1']):.4f}",
            "strategy_acc_detected": fmt(vals["strategy_acc_detected"]),
            "strategy_acc_missed": fmt(vals["strategy_acc_missed"]),
            "gt_conf_detected": fmt(vals["gt_conf_detected"]),
            "gt_conf_missed": fmt(vals["gt_conf_missed"]),
            "n_missed_per_seed": vals["n_missed"],
            "per_class_f1_mean": {k: round(np.mean(v), 4) for k, v in per_class_f1s.items()},
            "per_dominant_detection_mean": {k: round(np.mean(v), 4) for k, v in per_dominant_rates.items()},
        }
        aggregated[ds_name] = agg

        print(f"\n  [{ds_name.upper()}]")
        print(f"    Strategy acc: {agg['strategy_acc']}")
        print(f"    JB-only strategy acc: {agg['jb_strategy_acc']}")
        print(f"    Macro F1: {agg['macro_f1']}")
        print(f"    Strategy acc (detected): {agg['strategy_acc_detected']}")
        print(f"    Strategy acc (missed): {agg['strategy_acc_missed']}")
        print(f"    GT conf (detected): {agg['gt_conf_detected']}")
        print(f"    GT conf (missed): {agg['gt_conf_missed']}")
        print(f"    Missed per seed: {agg['n_missed_per_seed']}")
        print(f"    Per-class F1 (mean):")
        for cls_name, f1 in sorted(agg["per_class_f1_mean"].items()):
            print(f"      {cls_name:25s} {f1:.4f}")
        print(f"    Per-dominant detection rate (mean):")
        for sname, rate in sorted(agg["per_dominant_detection_mean"].items()):
            print(f"      {sname:25s} {rate:.4f}")

    # ---- Save ----
    output = {
        "experiment": "exp32_strategy_prediction",
        "model": "exp16_9class_deberta+bigru",
        "seeds": SEEDS,
        "datasets": {
            "dd_ood": f"{len(dd_convs)} jailbreak + {len(test_benign)} benign",
            "aa_ood": f"{len(aa_convs)} jailbreak + {len(test_benign)} benign",
        },
        "per_seed_results": all_seed_results,
        "aggregated": aggregated,
    }

    out_path = PROJ / "results/exp32_strategy_prediction.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
