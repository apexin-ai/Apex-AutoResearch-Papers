"""
eval_lz.py — Evaluate a fine-tuned Llama adapter on full MMLU and compute lz* person-fit statistic.

Usage: python eval_lz.py --condition clean --gpu 0
"""

import argparse
import csv
import json
import os

import numpy as np
import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

BASE_DIR = "/path/to/project/llama"
MODEL_DIR = "/path/to/models"
PARAMS_PATH = os.path.join(BASE_DIR, "mmlu_params.csv")

CHOICES = ["A", "B", "C", "D"]

FEW_SHOT_EXAMPLES = [
    {
        "question": "What is the capital of France?",
        "choices": ["London", "Paris", "Berlin", "Madrid"],
        "answer": 1,
    },
    {
        "question": "Which planet is closest to the Sun?",
        "choices": ["Venus", "Mercury", "Mars", "Earth"],
        "answer": 1,
    },
    {
        "question": "What is 2 + 2?",
        "choices": ["3", "4", "5", "6"],
        "answer": 1,
    },
]


def format_question(question, choices):
    lines = [f"Question: {question}"]
    for i, c in enumerate(choices):
        lines.append(f"{CHOICES[i]}. {c}")
    lines.append("Answer:")
    return "\n".join(lines)


def build_few_shot_prompt(question, choices):
    parts = []
    for ex in FEW_SHOT_EXAMPLES:
        parts.append(format_question(ex["question"], ex["choices"]) + f" {CHOICES[ex['answer']]}")
    parts.append(format_question(question, choices))
    return "\n\n".join(parts)


def find_model_path():
    patterns = [
        os.path.join(MODEL_DIR, "LLM-Research", "Meta-Llama-3___1-8B-Instruct"),
        os.path.join(MODEL_DIR, "LLM-Research", "Meta-Llama-3.1-8B-Instruct"),
        os.path.join(MODEL_DIR, "Llama-3.1-8B-Instruct"),
        os.path.join(MODEL_DIR, "Meta-Llama-3.1-8B-Instruct"),
    ]
    for p in patterns:
        if os.path.isdir(p):
            snapshot_dir = os.path.join(p, "snapshots")
            if os.path.isdir(snapshot_dir):
                snapshots = os.listdir(snapshot_dir)
                if snapshots:
                    return os.path.join(snapshot_dir, snapshots[0])
            if os.path.isfile(os.path.join(p, "config.json")):
                return p
    for root, dirs, files in os.walk(MODEL_DIR):
        if "config.json" in files and "Llama" in root and "8B" in root:
            return root
    raise FileNotFoundError(f"Cannot find Llama-3.1-8B-Instruct in {MODEL_DIR}")


def load_irt_params(path):
    params = {}
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            idx = int(row["item_idx"])
            params[idx] = {
                "a": float(row["a_discrimination"]),
                "b": float(row["b_difficulty"]),
                "c": float(row["c_guessing"]),
                "d": float(row["d_feasibility"]),
            }
    return params


def irf_4pl(theta, a, b, c, d):
    return c + (d - c) / (1.0 + np.exp(-a * (theta - b)))


def estimate_theta_mle(responses, irt_params, item_indices, max_iter=100, tol=1e-6):
    theta = 0.0
    for _ in range(max_iter):
        grad = 0.0
        hess = 0.0
        for i, idx in enumerate(item_indices):
            p = irt_params[idx]
            a, b, c, d = p["a"], p["b"], p["c"], p["d"]
            P = irf_4pl(theta, a, b, c, d)
            P = np.clip(P, 1e-10, 1.0 - 1e-10)
            x = responses[i]
            exp_term = np.exp(-a * (theta - b))
            dP = a * (d - c) * exp_term / (1.0 + exp_term) ** 2
            grad += (x - P) * dP / (P * (1.0 - P))
            hess += -(dP ** 2) * (1.0 / (P * (1.0 - P)))
        if abs(hess) < 1e-15:
            break
        delta = -grad / hess
        theta += delta
        if abs(delta) < tol:
            break
    return np.clip(theta, -4.0, 4.0)


def compute_lz_star(responses, irt_params, item_indices, theta):
    """Compute lz* statistic (Snijders, 2001) with variance correction for estimated theta."""
    l0 = 0.0
    E_l0 = 0.0
    Var_l0 = 0.0
    I_theta = 0.0
    C_theta = 0.0
    for i, idx in enumerate(item_indices):
        p = irt_params[idx]
        a, b, c, d = p["a"], p["b"], p["c"], p["d"]
        P = irf_4pl(theta, a, b, c, d)
        P = np.clip(P, 1e-10, 1.0 - 1e-10)
        Q = 1.0 - P
        x = responses[i]
        log_P = np.log(P)
        log_Q = np.log(Q)
        l0 += x * log_P + (1 - x) * log_Q
        E_l0 += P * log_P + Q * log_Q
        g = log_P - log_Q
        Var_l0 += P * Q * g ** 2
        # Snijders (2001) correction: dP/dtheta for 4PL
        z = a * (theta - b)
        sigma = 1.0 / (1.0 + np.exp(-np.clip(z, -30, 30)))
        dP = a * (d - c) * sigma * (1.0 - sigma)
        h = dP / (P * Q)
        I_theta += P * Q * h ** 2
        C_theta += P * Q * h * g
    if Var_l0 < 1e-15:
        return 0.0
    Var_star = Var_l0 - C_theta ** 2 / I_theta if I_theta > 1e-15 else Var_l0
    if Var_star <= 0:
        Var_star = Var_l0
    return (l0 - E_l0) / np.sqrt(Var_star)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--condition", required=True)
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--max_items", type=int, default=-1)
    args = parser.parse_args()

    os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)

    with open(os.path.join(BASE_DIR, "data", "mmlu_items.json")) as f:
        mmlu_items = json.load(f)

    seen_15_path = os.path.join(BASE_DIR, "data", "seen_items_15pct.json")
    seen_25_path = os.path.join(BASE_DIR, "data", "seen_items_25pct.json")
    seen_50_path = os.path.join(BASE_DIR, "data", "seen_items_50pct.json")
    seen_15 = set(json.load(open(seen_15_path))) if os.path.exists(seen_15_path) else set()
    seen_25 = set(json.load(open(seen_25_path))) if os.path.exists(seen_25_path) else set()
    seen_50 = set(json.load(open(seen_50_path))) if os.path.exists(seen_50_path) else set()

    if "contam_15" in args.condition:
        seen_set = seen_15
    elif "contam_25" in args.condition:
        seen_set = seen_25
    elif "contam_50" in args.condition:
        seen_set = seen_50
    else:
        seen_set = set()

    irt_params = load_irt_params(PARAMS_PATH)

    model_path = find_model_path()
    adapter_path = os.path.join(BASE_DIR, "checkpoints", args.condition)
    print(f"Base model: {model_path}")
    print(f"Adapter: {adapter_path}")

    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16,
    )

    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        quantization_config=bnb_config,
        device_map={"": 0},
        trust_remote_code=True,
    )
    model = PeftModel.from_pretrained(model, adapter_path)
    model.eval()

    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    choice_token_ids = [tokenizer.encode(c, add_special_tokens=False)[0] for c in CHOICES]
    print(f"Choice token IDs: {dict(zip(CHOICES, choice_token_ids))}")

    n_items = len(mmlu_items)
    if args.max_items > 0:
        n_items = min(n_items, args.max_items)

    responses = []
    correct_count = 0
    seen_correct = 0
    seen_total = 0
    unseen_correct = 0
    unseen_total = 0

    print(f"Evaluating {n_items} items...")
    for i in range(n_items):
        item = mmlu_items[i]
        prompt = build_few_shot_prompt(item["question"], item["choices"])
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits[0, -1, :]

        choice_logits = torch.tensor([logits[tid].item() for tid in choice_token_ids])
        pred = choice_logits.argmax().item()
        correct = int(pred == item["answer"])
        responses.append(correct)
        correct_count += correct

        is_seen = item["item_idx"] in seen_set
        if is_seen:
            seen_correct += correct
            seen_total += 1
        else:
            unseen_correct += correct
            unseen_total += 1

        if (i + 1) % 500 == 0:
            print(f"  [{i+1}/{n_items}] acc={correct_count/(i+1):.4f}")

    item_indices = [mmlu_items[i]["item_idx"] for i in range(n_items)]

    theta = estimate_theta_mle(responses, irt_params, item_indices)
    lz_star = compute_lz_star(responses, irt_params, item_indices, theta)

    seen_responses = []
    seen_indices = []
    unseen_responses = []
    unseen_indices = []
    for i in range(n_items):
        idx = mmlu_items[i]["item_idx"]
        if idx in seen_set:
            seen_responses.append(responses[i])
            seen_indices.append(idx)
        else:
            unseen_responses.append(responses[i])
            unseen_indices.append(idx)

    lz_star_seen = None
    lz_star_unseen = None
    if seen_indices:
        theta_seen = estimate_theta_mle(seen_responses, irt_params, seen_indices)
        lz_star_seen = compute_lz_star(seen_responses, irt_params, seen_indices, theta_seen)
    if unseen_indices:
        theta_unseen = estimate_theta_mle(unseen_responses, irt_params, unseen_indices)
        lz_star_unseen = compute_lz_star(unseen_responses, irt_params, unseen_indices, theta_unseen)

    acc_overall = correct_count / n_items if n_items > 0 else 0
    acc_seen = seen_correct / seen_total if seen_total > 0 else None
    acc_unseen = unseen_correct / unseen_total if unseen_total > 0 else None

    results = {
        "condition": args.condition,
        "theta_mle": float(theta),
        "lz_star": float(lz_star),
        "accuracy_overall": acc_overall,
        "accuracy_seen": acc_seen,
        "accuracy_unseen": acc_unseen,
        "lz_star_seen": float(lz_star_seen) if lz_star_seen is not None else None,
        "lz_star_unseen": float(lz_star_unseen) if lz_star_unseen is not None else None,
        "response_vector": responses,
        "n_items": n_items,
        "n_seen": seen_total,
        "n_unseen": unseen_total,
    }

    out_path = os.path.join(BASE_DIR, "results", f"{args.condition}_results.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {out_path}")
    print(f"  theta={theta:.4f}, lz*={lz_star:.4f}")
    print(f"  acc_overall={acc_overall:.4f}, acc_seen={acc_seen}, acc_unseen={acc_unseen}")
    print(f"  lz*_seen={lz_star_seen}, lz*_unseen={lz_star_unseen}")


if __name__ == "__main__":
    main()
