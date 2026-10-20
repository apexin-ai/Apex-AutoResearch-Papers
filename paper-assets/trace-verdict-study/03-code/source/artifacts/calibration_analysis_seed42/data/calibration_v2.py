"""Calibration analysis for trace-verdict classification models.

v2 (2026-05-15):
- P0: Token IDs resolved dynamically from tokenizer (was hardcoded 6385/18403)
- P1: Prediction via greedy generation (matches evaluate.py); confidence from logits
- P2: MCE computation added; empty bins skipped
"""

import argparse
import json
import os
import sys

import numpy as np
import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

sys.path.insert(0, os.path.dirname(__file__))
from evaluate import load_test_data, classify_prediction

CHECKPOINT_MAP = {
    "vota": "/root/autodl-tmp/trace-verdict-study-checkpoints/vota/final/",
    "no_trace": "/root/autodl-tmp/trace-verdict-study-checkpoints/no_trace/final/",
    "full_trace": "/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace/final/",
    "label_only": "/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only/final/",
    "exception_only": "/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only/final/",
    "ae_only": "/root/autodl-tmp/trace-verdict-study-checkpoints/ae_only/final/",
    "loop_only": "/root/autodl-tmp/trace-verdict-study-checkpoints/loop_only/final/",
}

DATA_CONDITION_MAP = {
    "vota": "vota",
    "no_trace": "no_trace",
    "full_trace": "full_trace",
    "label_only": "full_trace",
    "exception_only": "exception_only",
    "ae_only": "ae_only",
    "loop_only": "loop_only",
}

MODEL_PATH = "/root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct"


def resolve_token_ids(tokenizer):
    """Resolve pass/fail token IDs from tokenizer vocabulary."""
    pass_ids = tokenizer.encode("pass", add_special_tokens=False)
    fail_ids = tokenizer.encode("fail", add_special_tokens=False)
    pass_token_id = pass_ids[-1]
    fail_token_id = fail_ids[-1]
    print(f"Token IDs: pass={pass_token_id} (encode={pass_ids}), "
          f"fail={fail_token_id} (encode={fail_ids})")
    return pass_token_id, fail_token_id


def get_pass_fail_probs(model, tokenizer, input_text, device,
                        pass_token_id, fail_token_id):
    """Greedy generation for prediction + logit-based confidence."""
    messages = [{"role": "user", "content": input_text}]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    with torch.no_grad():
        gen_out = model.generate(
            **inputs,
            max_new_tokens=1,
            do_sample=False,
            temperature=None,
            top_p=None,
            output_scores=True,
            return_dict_in_generate=True,
        )

    gen_ids = gen_out.sequences[0][inputs["input_ids"].shape[1]:]
    raw_pred = tokenizer.decode(gen_ids, skip_special_tokens=True).strip().lower()
    predicted_label = classify_prediction(raw_pred)

    logits = gen_out.scores[0][0]
    pf_logits = logits[[pass_token_id, fail_token_id]]
    pf_probs = torch.softmax(pf_logits, dim=0)

    pass_prob = pf_probs[0].item()
    fail_prob = pf_probs[1].item()
    confidence = max(pass_prob, fail_prob)

    return predicted_label, confidence, pass_prob, fail_prob


def compute_ece(confidences, accuracies, n_bins=10):
    """Expected Calibration Error with equal-width bins from 0.5 to 1.0."""
    bin_boundaries = np.linspace(0.5, 1.0, n_bins + 1)
    ece = 0.0
    n = len(confidences)
    bin_data = []

    for i in range(n_bins):
        lo, hi = bin_boundaries[i], bin_boundaries[i + 1]
        if i == n_bins - 1:
            mask = (confidences >= lo) & (confidences <= hi)
        else:
            mask = (confidences >= lo) & (confidences < hi)

        count = mask.sum()
        if count > 0:
            mean_conf = confidences[mask].mean()
            acc = accuracies[mask].mean()
            ece += (count / n) * abs(acc - mean_conf)
        else:
            mean_conf = 0.0
            acc = 0.0

        bin_data.append({
            "bin_lower": round(float(lo), 4),
            "bin_upper": round(float(hi), 4),
            "mean_confidence": round(float(mean_conf), 6),
            "accuracy": round(float(acc), 6),
            "count": int(count),
        })

    return float(ece), bin_data


def compute_mce(reliability_data):
    """Maximum Calibration Error: max |acc - conf| over non-empty bins."""
    errors = [abs(b["accuracy"] - b["mean_confidence"])
              for b in reliability_data if b["count"] > 0]
    return float(max(errors)) if errors else 0.0


def compute_brier_score(true_labels, pass_probs):
    """Brier score: MSE between predicted prob and true binary label."""
    true_binary = np.array([1.0 if l == "pass" else 0.0 for l in true_labels])
    return float(np.mean((np.array(pass_probs) - true_binary) ** 2))


def compute_confidence_distribution(confidences, n_bins=10):
    """Histogram of confidence values in equal-width bins from 0.5 to 1.0."""
    bin_boundaries = np.linspace(0.5, 1.0, n_bins + 1)
    n = len(confidences)
    dist = []

    for i in range(n_bins):
        lo, hi = bin_boundaries[i], bin_boundaries[i + 1]
        if i == n_bins - 1:
            count = int(((confidences >= lo) & (confidences <= hi)).sum())
        else:
            count = int(((confidences >= lo) & (confidences < hi)).sum())
        dist.append({
            "bin_lower": round(float(lo), 4),
            "bin_upper": round(float(hi), 4),
            "count": count,
            "fraction": round(count / n, 6) if n > 0 else 0.0,
        })

    return dist


def run_calibration(model, tokenizer, test_data, device, condition):
    """Run calibration analysis on test data, return results dict."""
    pass_token_id, fail_token_id = resolve_token_ids(tokenizer)

    true_labels = []
    pred_labels = []
    confidences = []
    pass_probs_list = []
    correct_list = []

    n = len(test_data)
    for i, item in enumerate(test_data):
        pred_label, conf, pass_prob, fail_prob = get_pass_fail_probs(
            model, tokenizer, item["input"], device,
            pass_token_id, fail_token_id
        )
        true_label = item["output"]

        true_labels.append(true_label)
        pred_labels.append(pred_label)
        confidences.append(conf)
        pass_probs_list.append(pass_prob)
        correct_list.append(1.0 if pred_label == true_label else 0.0)

        if (i + 1) % 50 == 0:
            acc = sum(correct_list) / len(correct_list)
            print(f"  [{i+1}/{n}] running accuracy: {acc:.4f}")

    confidences = np.array(confidences)
    correct = np.array(correct_list)
    accuracy = float(correct.mean())

    ece, reliability_data = compute_ece(confidences, correct)
    brier = compute_brier_score(true_labels, pass_probs_list)
    mce = compute_mce(reliability_data)
    conf_dist = compute_confidence_distribution(confidences)

    per_class = {}
    for cls in ["pass", "fail"]:
        cls_mask = np.array([l == cls for l in true_labels])
        cls_n = int(cls_mask.sum())
        if cls_n > 0:
            cls_ece, cls_rel = compute_ece(confidences[cls_mask],
                                           correct[cls_mask])
            cls_mce = compute_mce(cls_rel)
            cls_pass_probs = np.array(pass_probs_list)[cls_mask]
            cls_true = np.array(true_labels)[cls_mask]
            cls_brier = compute_brier_score(cls_true.tolist(),
                                            cls_pass_probs.tolist())
            per_class[cls] = {
                "ece": round(cls_ece, 6), "brier": round(cls_brier, 6),
                "mce": round(cls_mce, 6), "n": cls_n,
            }
        else:
            per_class[cls] = {"ece": 0.0, "brier": 0.0, "mce": 0.0, "n": 0}

    return {
        "condition": condition,
        "n_samples": n,
        "accuracy": round(accuracy, 6),
        "ece": round(ece, 6),
        "mce": round(mce, 6),
        "brier_score": round(brier, 6),
        "reliability_diagram": reliability_data,
        "confidence_distribution": conf_dist,
        "per_class": per_class,
    }


def load_model(checkpoint_dir, model_path, device):
    """Load base model + LoRA adapter."""
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        device_map={"": device},
    )
    model = PeftModel.from_pretrained(model, checkpoint_dir)
    model.eval()
    return model, tokenizer


def main():
    parser = argparse.ArgumentParser(
        description="Calibration analysis for trace-verdict models.")

    parser.add_argument("--batch", action="store_true",
                        help="Batch mode: run multiple conditions")
    parser.add_argument("--conditions", type=str, default=None,
                        help="Comma-separated conditions for batch mode")

    parser.add_argument("--condition", type=str, default=None,
                        help="Single condition name")
    parser.add_argument("--checkpoint_dir", type=str, default=None,
                        help="Path to checkpoint directory with LoRA adapter")
    parser.add_argument("--model_path", type=str, default=MODEL_PATH,
                        help="Path to base model")
    parser.add_argument("--data_dir", type=str,
                        default="/root/autodl-tmp/trace-verdict-study-data/",
                        help="Directory containing test data")
    parser.add_argument("--gpu", type=int, default=0, help="GPU device number")
    parser.add_argument("--output", type=str, default=None,
                        help="Output JSON path (single mode)")
    parser.add_argument("--output_dir", type=str, default=None,
                        help="Output directory (batch mode)")
    args = parser.parse_args()

    if args.batch:
        if args.conditions is None:
            parser.error("--conditions required in batch mode")
        conditions = [c.strip() for c in args.conditions.split(",")]
        output_dir = (args.output_dir or
                      "/root/autodl-tmp/trace-verdict-study-checkpoints/calibration/")
        os.makedirs(output_dir, exist_ok=True)

        os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)
        device = torch.device("cuda:0")

        all_results = {}
        for cond in conditions:
            checkpoint_dir = CHECKPOINT_MAP.get(cond)
            if checkpoint_dir is None:
                print(f"[SKIP] Unknown condition: {cond}")
                continue
            if not os.path.isdir(checkpoint_dir):
                print(f"[SKIP] Checkpoint not found: {checkpoint_dir}")
                continue

            data_cond = DATA_CONDITION_MAP[cond]
            print(f"\n{'='*60}")
            print(f"Condition: {cond}")
            print(f"Checkpoint: {checkpoint_dir}")
            print(f"Data condition: {data_cond}")

            test_data = load_test_data(args.data_dir, data_cond)
            print(f"Test samples: {len(test_data)}")

            model, tokenizer = load_model(checkpoint_dir, args.model_path,
                                          device)
            results = run_calibration(model, tokenizer, test_data, device, cond)
            results["checkpoint_dir"] = checkpoint_dir

            out_path = os.path.join(output_dir, f"{cond}_calibration.json")
            with open(out_path, "w") as f:
                json.dump(results, f, indent=2)
            print(f"Saved: {out_path}")
            print(f"ECE={results['ece']:.4f}  MCE={results['mce']:.4f}  "
                  f"Brier={results['brier_score']:.4f}  "
                  f"Acc={results['accuracy']:.4f}")

            all_results[cond] = {
                "ece": results["ece"],
                "mce": results["mce"],
                "brier_score": results["brier_score"],
                "accuracy": results["accuracy"],
                "n_samples": results["n_samples"],
            }

            del model
            torch.cuda.empty_cache()

        summary_path = os.path.join(output_dir, "calibration_metrics_v2.json")
        with open(summary_path, "w") as f:
            json.dump(all_results, f, indent=2)
        print(f"\nCombined metrics: {summary_path}")
        print(f"All results saved to {output_dir}")

    else:
        if args.condition is None:
            parser.error("--condition required in single mode")
        if args.checkpoint_dir is None:
            args.checkpoint_dir = CHECKPOINT_MAP.get(args.condition)
            if args.checkpoint_dir is None:
                parser.error(f"No default checkpoint for condition "
                             f"'{args.condition}', specify --checkpoint_dir")

        if args.output is None:
            args.output = os.path.join(
                os.path.dirname(args.checkpoint_dir.rstrip("/")),
                f"calibration_{args.condition}.json")

        os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)
        device = torch.device("cuda:0")

        data_cond = DATA_CONDITION_MAP.get(args.condition, args.condition)
        print(f"Condition: {args.condition}")
        print(f"Checkpoint: {args.checkpoint_dir}")

        test_data = load_test_data(args.data_dir, data_cond)
        print(f"Test samples: {len(test_data)}")

        model, tokenizer = load_model(args.checkpoint_dir, args.model_path,
                                      device)
        results = run_calibration(model, tokenizer, test_data, device,
                                  args.condition)
        results["checkpoint_dir"] = args.checkpoint_dir

        os.makedirs(os.path.dirname(os.path.abspath(args.output)),
                    exist_ok=True)
        with open(args.output, "w") as f:
            json.dump(results, f, indent=2)

        print(f"\n=== Calibration Results (condition: {args.condition}) ===")
        print(f"Accuracy:    {results['accuracy']:.4f}")
        print(f"ECE:         {results['ece']:.4f}")
        print(f"MCE:         {results['mce']:.4f}")
        print(f"Brier score: {results['brier_score']:.4f}")
        print(f"\nReliability diagram:")
        for b in results["reliability_diagram"]:
            bar = "#" * min(b["count"], 50)
            print(f"  [{b['bin_lower']:.2f}-{b['bin_upper']:.2f}] "
                  f"conf={b['mean_confidence']:.3f} "
                  f"acc={b['accuracy']:.3f} n={b['count']:4d} {bar}")
        print(f"\nPer-class:")
        for cls, v in results["per_class"].items():
            print(f"  {cls}: ECE={v['ece']:.4f} MCE={v['mce']:.4f} "
                  f"Brier={v['brier']:.4f} n={v['n']}")
        print(f"\nSaved to {args.output}")


if __name__ == "__main__":
    main()
