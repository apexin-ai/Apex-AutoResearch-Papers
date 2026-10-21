"""Representation steering via linear probe weights.

Uses the linear probe's weight vector as a steering direction to causally
intervene in the residual stream during knowledge-conflict processing.
Measures whether the intervention flips model output between parametric
and contextual answers.

Input:
  - Model (causal LM)
  - Activation files (en_activations.pt from collect_activations.py)
  - Test data (en_conflict_test_verified.jsonl)

Output:
  - steering_results.json: flip rates, Fisher exact test per alpha
"""

import argparse
import json
import re
import string
from pathlib import Path

import numpy as np
import torch
from scipy import stats
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from transformers import AutoModelForCausalLM, AutoTokenizer


def load_steering_direction(activation_path: str, layer: int, seed: int = None):
    """Train a probe on the given layer and extract the steering direction."""
    data = torch.load(activation_path, map_location="cpu", weights_only=True)
    acts = data["activations"]
    if acts.dtype == torch.bfloat16:
        acts = acts.float()

    if seed is not None:
        n_train_orig = data["split_sizes"]["train"]
        n_total = acts.shape[0]
        test_ratio = (n_total - n_train_orig) / n_total
        indices = np.arange(n_total)
        y_np = data["labels"].numpy()
        tr_idx, te_idx = train_test_split(
            indices, test_size=test_ratio, random_state=seed, stratify=y_np)
        train_X = acts[tr_idx, layer, :].numpy()
        train_y = data["labels"][tr_idx].numpy()
        test_X = acts[te_idx, layer, :].numpy()
        test_y = data["labels"][te_idx].numpy()
    else:
        n_train = data["split_sizes"]["train"]
        train_X = acts[:n_train, layer, :].numpy()
        train_y = data["labels"][:n_train].numpy()
        test_X = acts[n_train:, layer, :].numpy()
        test_y = data["labels"][n_train:].numpy()

    scaler = StandardScaler()
    train_X_scaled = scaler.fit_transform(train_X)
    test_X_scaled = scaler.transform(test_X)

    probe = LogisticRegression(
        class_weight="balanced", max_iter=1000, solver="lbfgs",
        random_state=seed if seed is not None else 42
    )
    probe.fit(train_X_scaled, train_y)

    acc = float(np.mean(probe.predict(test_X_scaled) == test_y))
    print(f"Probe accuracy at layer {layer}: {acc:.4f}")

    w_scaled = probe.coef_[0]
    w_orig = w_scaled / scaler.scale_
    d = w_orig / np.linalg.norm(w_orig)
    return d.astype(np.float32), acc


def random_orthogonal_direction(d: np.ndarray, seed: int = 42) -> np.ndarray:
    rng = np.random.RandomState(seed)
    v = rng.randn(len(d)).astype(np.float32)
    v -= np.dot(v, d) * d
    v /= np.linalg.norm(v)
    return v


def get_peak_layer(probe_results_path: str, direction: str = "EN→EN") -> int:
    with open(probe_results_path) as f:
        data = json.load(f)
    if direction in data and "peak_layer" in data[direction]:
        return data[direction]["peak_layer"]
    if "summary" in data and direction in data["summary"]:
        entry = data["summary"][direction]
        if "best_layer" in entry:
            return entry["best_layer"]
        if "peak_layers" in entry:
            from collections import Counter
            return Counter(entry["peak_layers"]).most_common(1)[0][0]
    if "per_seed" in data:
        for seed_data in data["per_seed"].values():
            if direction in seed_data and "peak_layer" in seed_data[direction]:
                return seed_data[direction]["peak_layer"]
    raise ValueError(f"Could not find peak layer for {direction}")


def normalize_answer(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"\b(a|an|the)\b", " ", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\s+", " ", text).strip()
    return text


def classify_answer(generated: str, parametric: str, contextual: str) -> str:
    gen_norm = normalize_answer(generated)
    param_norm = normalize_answer(parametric)
    ctx_norm = normalize_answer(contextual)
    if not gen_norm:
        return "other"
    param_match = param_norm in gen_norm or gen_norm in param_norm
    ctx_match = ctx_norm in gen_norm or gen_norm in ctx_norm
    if param_match and ctx_match:
        return "both"
    if ctx_match:
        return "contextual"
    if param_match:
        return "parametric"
    return "other"


def build_conflict_prompt(sample: dict) -> str:
    return (
        f"Context: {sample['context']}\n"
        f"Question: {sample['question']}\n"
        f"Based on the context above, answer the question with a short factual answer.\n"
        f"Answer:"
    )


def generate_with_steering(
    model, tokenizer, prompt, layer_module, direction, alpha,
    max_new_tokens=100, position="last",
):
    hook_handle = None

    def steering_hook(module, input, output):
        hidden = output[0] if isinstance(output, tuple) else output
        d_tensor = torch.tensor(direction, device=hidden.device, dtype=hidden.dtype)
        if position == "last":
            seq_len = hidden.shape[1]
            hidden[:, seq_len - 1, :] += alpha * d_tensor
        elif position == "all":
            hidden += alpha * d_tensor.unsqueeze(0).unsqueeze(0)
        if isinstance(output, tuple):
            return (hidden,) + output[1:]
        return hidden

    hook_handle = layer_module.register_forward_hook(steering_hook)
    try:
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
        with torch.no_grad():
            outputs = model.generate(
                **inputs, max_new_tokens=max_new_tokens,
                do_sample=False, temperature=1.0,
            )
        new_tokens = outputs[0][inputs["input_ids"].shape[1]:]
        text = tokenizer.decode(new_tokens, skip_special_tokens=True).strip()
        text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()
        return text
    finally:
        if hook_handle:
            hook_handle.remove()


def run_steering_experiment(
    model, tokenizer, layer_module, test_data,
    steering_dir, control_dir, alphas,
    use_chat_template=True, position="last",
):
    baseline_results = []
    for sample in test_data:
        prompt = build_conflict_prompt(sample)
        if use_chat_template and hasattr(tokenizer, "apply_chat_template"):
            messages = [{"role": "user", "content": prompt}]
            try:
                prompt = tokenizer.apply_chat_template(
                    messages, tokenize=False, add_generation_prompt=True,
                    enable_thinking=False,
                )
            except TypeError:
                prompt = tokenizer.apply_chat_template(
                    messages, tokenize=False, add_generation_prompt=True,
                )
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
        with torch.no_grad():
            outputs = model.generate(
                **inputs, max_new_tokens=100, do_sample=False, temperature=1.0,
            )
        new_tokens = outputs[0][inputs["input_ids"].shape[1]:]
        text = tokenizer.decode(new_tokens, skip_special_tokens=True).strip()
        text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()
        answer_type = classify_answer(text, sample["parametric_answer"], sample["contextual_answer"])
        baseline_results.append({
            "question": sample["question"],
            "generated": text,
            "answer_type": answer_type,
        })

    all_alpha_results = {}
    for alpha in alphas:
        for condition, direction in [("probe", steering_dir), ("control", control_dir)]:
            key = f"alpha_{alpha}_{condition}"
            results_list = []
            flips = 0
            for i, sample in enumerate(test_data):
                prompt = build_conflict_prompt(sample)
                if use_chat_template and hasattr(tokenizer, "apply_chat_template"):
                    messages = [{"role": "user", "content": prompt}]
                    try:
                        prompt = tokenizer.apply_chat_template(
                            messages, tokenize=False, add_generation_prompt=True,
                            enable_thinking=False,
                        )
                    except TypeError:
                        prompt = tokenizer.apply_chat_template(
                            messages, tokenize=False, add_generation_prompt=True,
                        )

                steered_text = generate_with_steering(
                    model, tokenizer, prompt, layer_module, direction, alpha,
                    position=position,
                )
                steered_type = classify_answer(
                    steered_text, sample["parametric_answer"], sample["contextual_answer"]
                )
                baseline_type = baseline_results[i]["answer_type"]
                did_flip = baseline_type != steered_type and steered_type in ("parametric", "contextual")
                if did_flip:
                    flips += 1
                results_list.append({
                    "baseline_type": baseline_type,
                    "steered_type": steered_type,
                    "flipped": did_flip,
                })

            n = len(test_data)
            flip_rate = flips / n

            if condition == "probe":
                probe_flips = flips
            else:
                control_flips = flips

            all_alpha_results[key] = {
                "alpha": alpha,
                "condition": condition,
                "flip_rate": round(flip_rate, 4),
                "n_flips": flips,
                "n_total": n,
                "position": position,
                "details": results_list[:5],
            }

        table = np.array([
            [probe_flips, len(test_data) - probe_flips],
            [control_flips, len(test_data) - control_flips],
        ])
        odds_ratio, fisher_p = stats.fisher_exact(table)
        all_alpha_results[f"alpha_{alpha}_fisher"] = {
            "odds_ratio": round(float(odds_ratio), 4) if not np.isinf(odds_ratio) else "inf",
            "p_value": round(float(fisher_p), 6),
            "probe_flips": probe_flips,
            "control_flips": control_flips,
        }
        print(f"  alpha={alpha}: probe_flips={probe_flips}, control_flips={control_flips}, "
              f"Fisher p={fisher_p:.4f}")

    return all_alpha_results, baseline_results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, required=True)
    parser.add_argument("--data_dir", type=str, required=True)
    parser.add_argument("--output_dir", type=str, default=None)
    parser.add_argument("--peak_layer", type=int, default=None)
    parser.add_argument("--alphas", type=float, nargs="+", default=[5, 10, 15, 20])
    parser.add_argument("--position", choices=["last", "all"], default="last")
    parser.add_argument("--output_suffix", type=str, default="")
    parser.add_argument("--no_chat_template", action="store_true")
    parser.add_argument("--max_new_tokens", type=int, default=100)
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--dry_run", action="store_true")
    args = parser.parse_args()

    data_dir = Path(args.data_dir)
    output_dir = Path(args.output_dir) if args.output_dir else data_dir

    if args.peak_layer is not None:
        peak_layer = args.peak_layer
    else:
        probe_path = data_dir / "probe_results.json"
        peak_layer = get_peak_layer(str(probe_path))
    print(f"Steering layer: {peak_layer}")

    act_path = data_dir / "en_activations.pt"
    steering_dir, probe_acc = load_steering_direction(str(act_path), peak_layer, seed=args.seed)
    control_dir = random_orthogonal_direction(steering_dir, seed=args.seed if args.seed is not None else 42)
    print(f"Steering direction dim: {len(steering_dir)}")
    print(f"Orthogonality check: dot={np.dot(steering_dir, control_dir):.6f}")

    test_path = data_dir / "en_conflict_test_verified.jsonl"
    with open(test_path) as f:
        all_data = [json.loads(line) for line in f]
    test_data = [d for d in all_data if d["label"] == "conflict"]
    print(f"Test samples: {len(test_data)} conflict / {len(all_data)} total")

    if args.dry_run:
        print("\n=== DRY RUN: setup validated ===")
        return

    print(f"\nLoading model: {args.model}")
    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        args.model, torch_dtype=torch.bfloat16,
        device_map="auto", trust_remote_code=True,
    )
    model.eval()
    layer_module = model.model.layers[peak_layer]

    use_chat = not args.no_chat_template
    results, baseline = run_steering_experiment(
        model, tokenizer, layer_module, test_data,
        steering_dir, control_dir, args.alphas,
        use_chat_template=use_chat, position=args.position,
    )

    output_dir.mkdir(parents=True, exist_ok=True)
    suffix = args.output_suffix
    out_path = output_dir / f"steering_results{suffix}.json"
    output = {
        "config": {
            "model": args.model,
            "peak_layer": peak_layer,
            "probe_accuracy": probe_acc,
            "position": args.position,
            "alphas": args.alphas,
            "n_test": len(test_data),
            "use_chat_template": use_chat,
            "seed": args.seed,
        },
        "baseline": {
            "distribution": {},
            "samples": baseline[:5],
        },
        "results": results,
    }

    for b in baseline:
        t = b["answer_type"]
        output["baseline"]["distribution"][t] = output["baseline"]["distribution"].get(t, 0) + 1

    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
