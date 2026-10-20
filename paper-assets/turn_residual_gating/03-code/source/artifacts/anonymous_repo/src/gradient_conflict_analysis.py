"""NTP vs GAR gradient conflict analysis on gate parameters.

Measures cosine similarity and magnitude ratio of NTP and GAR gradients
on gate parameters across all layers. Used to motivate PCGrad training.
"""

import argparse
import json
import os
import sys
import random

import torch
import torch.nn.functional as F
import numpy as np
from datasets import load_from_disk
from transformers import AutoTokenizer
from peft import PeftModel

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from threadgate import ThreadGatedModel
from gar import GARMeasurer, compute_gar_loss
from turn_utils import detect_turn_boundaries, build_turn_features
from config import MODEL_NAME


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def collect_gate_grads(model):
    grads = {}
    for layer_idx, gate in enumerate(model.gates):
        layer_grads = []
        for p in gate.parameters():
            if p.grad is not None:
                layer_grads.append(p.grad.detach().float().flatten())
            else:
                layer_grads.append(torch.zeros(p.numel(), dtype=torch.float32, device=p.device))
        if layer_grads:
            grads[layer_idx] = torch.cat(layer_grads)
    if hasattr(model, "turn_embedding"):
        te_grads = []
        for p in model.turn_embedding.parameters():
            if p.grad is not None:
                te_grads.append(p.grad.detach().float().flatten())
            else:
                te_grads.append(torch.zeros(p.numel(), dtype=torch.float32, device=p.device))
        if te_grads:
            grads["turn_embedding"] = torch.cat(te_grads)
    return grads


def compute_conflict_metrics(grads_ntp, grads_gar):
    metrics = {}
    all_keys = sorted(k for k in grads_ntp if k in grads_gar and isinstance(k, int))

    for layer_idx in all_keys:
        g_ntp = grads_ntp[layer_idx]
        g_gar = grads_gar[layer_idx]

        norm_ntp = g_ntp.norm().item()
        norm_gar = g_gar.norm().item()

        if norm_ntp > 0 and norm_gar > 0:
            cos_sim = F.cosine_similarity(g_ntp.unsqueeze(0), g_gar.unsqueeze(0)).item()
        else:
            cos_sim = 0.0

        ratio = norm_ntp / norm_gar if norm_gar > 1e-12 else float("inf")

        metrics[layer_idx] = {
            "cosine_similarity": cos_sim,
            "norm_ntp": norm_ntp,
            "norm_gar": norm_gar,
            "magnitude_ratio": ratio,
        }

    return metrics


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--checkpoint-dir", required=True)
    parser.add_argument("--data-dir", default="./data/ultrachat_8k")
    parser.add_argument("--output", default="results/gradient_conflict.json")
    parser.add_argument("--model", default=MODEL_NAME)
    parser.add_argument("--num-samples", type=int, default=100)
    parser.add_argument("--max-seq-len", type=int, default=2048)
    parser.add_argument("--gar-loss-mode", default="mse_target")
    parser.add_argument("--gar-target", type=float, default=0.5)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    set_seed(args.seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = ThreadGatedModel(args.model, gate_type="threadgate", init_bias=2.0, device_map="auto")

    lora_path = os.path.join(args.checkpoint_dir, "lora")
    if os.path.isdir(lora_path):
        from peft import LoraConfig, get_peft_model
        from peft import PeftModel
        model.base_model = PeftModel.from_pretrained(model.base_model, lora_path)

    gate_path = os.path.join(args.checkpoint_dir, "gate_params.pt")
    if os.path.exists(gate_path):
        gate_state = torch.load(gate_path, map_location="cpu", weights_only=True)
        model.gates.load_state_dict(gate_state["gates"])
        if "turn_embedding" in gate_state:
            model.turn_embedding.load_state_dict(gate_state["turn_embedding"])

    original_model = model.base_model.base_model.model if hasattr(model.base_model, "base_model") else model.base_model
    if hasattr(original_model, "config"):
        original_model.config._attn_implementation = "eager"
        original_model.config.attn_implementation = "eager"
        if hasattr(original_model, "model") and hasattr(original_model.model, "layers"):
            for layer in original_model.model.layers:
                layer.self_attn._attn_implementation = "eager"

    hf_model = original_model
    if hasattr(hf_model, "model") and hasattr(hf_model.model, "layers"):
        measurer = GARMeasurer(hf_model, measure_only=False)
    else:
        raise ValueError("Cannot find model layers for GAR measurement")

    tokenizer = AutoTokenizer.from_pretrained(args.model)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    ds = load_from_disk(args.data_dir)
    num_layers = model.num_layers

    all_metrics = []
    all_ntp_losses = []
    all_gar_losses = []

    indices = list(range(len(ds)))
    random.shuffle(indices)

    print(f"Analyzing gradient conflict on {args.num_samples} samples...")

    for sample_idx in range(min(args.num_samples, len(ds))):
        idx = indices[sample_idx]
        messages = ds[idx]["messages"]
        text = tokenizer.apply_chat_template(messages, tokenize=False)
        encoding = tokenizer(text, truncation=True, max_length=args.max_seq_len, return_tensors="pt")
        input_ids = encoding.input_ids.squeeze(0)

        boundaries = detect_turn_boundaries(input_ids, tokenizer)
        turn_feats = build_turn_features(input_ids, tokenizer)

        labels = input_ids.clone()
        labels[:] = -100
        for turn in boundaries["turns"]:
            if turn["role"] == "assistant":
                labels[turn["content_start"]:turn["content_end"]] = input_ids[turn["content_start"]:turn["content_end"]]

        goal_pos = boundaries["goal_token_positions"]
        assistant_pos = boundaries["assistant_last_token_positions"]

        if len(assistant_pos) < 2 or len(goal_pos) == 0:
            continue

        input_batch = input_ids.unsqueeze(0).to(device)
        labels_batch = labels.unsqueeze(0).to(device)
        tf = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in turn_feats.items()}

        # NTP gradient
        model.zero_grad()
        with measurer.measure():
            outputs = model(input_batch, labels=labels_batch, turn_features=tf, output_attentions=True)
        l_ntp = outputs.loss
        l_ntp.backward(retain_graph=True)
        grads_ntp = collect_gate_grads(model)

        # GAR gradient
        model.zero_grad()
        with measurer.measure():
            outputs = model(input_batch, labels=labels_batch, turn_features=tf, output_attentions=True)
        gar_per_turn = []
        for pos in assistant_pos:
            gar_val = measurer.compute_gar_differentiable(goal_pos, [pos])
            gar_per_turn.append(gar_val)
        l_gar = compute_gar_loss(gar_per_turn, mode=args.gar_loss_mode, target=args.gar_target)
        l_gar.backward()
        grads_gar = collect_gate_grads(model)

        metrics = compute_conflict_metrics(grads_ntp, grads_gar)
        all_metrics.append(metrics)
        all_ntp_losses.append(l_ntp.item())
        all_gar_losses.append(l_gar.item())

        if sample_idx % 20 == 0:
            avg_cos = np.mean([m[k]["cosine_similarity"] for m in [metrics] for k in m if isinstance(k, int)])
            print(f"  Sample {sample_idx}: NTP={l_ntp.item():.4f} GAR={l_gar.item():.6f} avg_cos={avg_cos:.4f}")

    # Aggregate
    per_layer_results = {}
    for i in range(num_layers):
        cos_vals = [m[i]["cosine_similarity"] for m in all_metrics if i in m]
        ratio_vals = [m[i]["magnitude_ratio"] for m in all_metrics if i in m]
        norm_ntp_vals = [m[i]["norm_ntp"] for m in all_metrics if i in m]
        norm_gar_vals = [m[i]["norm_gar"] for m in all_metrics if i in m]

        per_layer_results[f"layer_{i}"] = {
            "cosine_similarity_mean": float(np.mean(cos_vals)),
            "cosine_similarity_std": float(np.std(cos_vals)),
            "magnitude_ratio_median": float(np.median(ratio_vals)),
            "norm_ntp_mean": float(np.mean(norm_ntp_vals)),
            "norm_gar_mean": float(np.mean(norm_gar_vals)),
        }

    all_cos = [per_layer_results[f"layer_{i}"]["cosine_similarity_mean"] for i in range(num_layers)]
    negative_layers = sum(1 for c in all_cos if c < 0)
    strong_negative = sum(1 for c in all_cos if c < -0.3)

    summary = {
        "num_samples": len(all_metrics),
        "avg_ntp_loss": float(np.mean(all_ntp_losses)),
        "avg_gar_loss": float(np.mean(all_gar_losses)),
        "overall_cos_sim_mean": float(np.mean(all_cos)),
        "negative_cos_layers": negative_layers,
        "strong_negative_cos_layers": strong_negative,
        "total_layers": num_layers,
        "conflict_fraction": negative_layers / num_layers,
    }

    results = {
        "config": vars(args),
        "summary": summary,
        "per_layer": per_layer_results,
    }

    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {args.output}")

    # Summary
    print(f"\n{'='*70}")
    print(f"Gradient Conflict Analysis: NTP vs GAR on Gate Parameters")
    print(f"{'='*70}")
    print(f"Samples: {len(all_metrics)}")
    print(f"Layers with negative cos_sim: {negative_layers}/{num_layers} ({summary['conflict_fraction']*100:.1f}%)")
    print(f"Strong conflict (cos < -0.3): {strong_negative}/{num_layers}")

    if summary["conflict_fraction"] > 0.5:
        print(f"\nCONCLUSION: Widespread gradient conflict detected.")
    elif summary["conflict_fraction"] > 0.2:
        print(f"\nCONCLUSION: Partial gradient conflict in {negative_layers} layers.")
    else:
        print(f"\nCONCLUSION: Minimal gradient conflict between NTP and GAR.")


if __name__ == "__main__":
    main()
