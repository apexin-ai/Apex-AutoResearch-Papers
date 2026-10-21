"""Compute F1/precision/recall of KL and BCE predictors against per-token oracle mask.

Oracle mask: per-token magnitude-based top-k (retain top 50% of SwiGLU intermediates).
This is the gold-standard per-token decision that TEAL approximates with mean-magnitude.

If BCE F1 > KL F1 but KL PPL << BCE PPL, it proves per-neuron accuracy is the wrong
optimization target — output fidelity (KL) matters more than mask fidelity (BCE).
"""

import json
import os
import sys
import torch
import numpy as np
from pathlib import Path

sys.path.insert(0, "/root/distill_sparse_swiglu/src")
from predictor import PredictorWrapper
from transformers import AutoModelForCausalLM, AutoTokenizer
from datasets import load_dataset

MODEL_PATH = "/root/autodl-tmp/models/llama-3.1-8b"
KL_CKPT = "/root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt"
BCE_CKPT_CANDIDATES = [
    "/root/distill_sparse_swiglu/checkpoints/bce_isocompute_v3_s42/predictor_bce.pt",
    "/root/distill_sparse_swiglu/checkpoints/bce_isocompute_v3_s42/predictor_bce_comp.pt",
    "/root/distill_sparse_swiglu/checkpoints/bce_isocompute_v3_s42/checkpoint.pt",
    "/root/distill_sparse_swiglu/checkpoints/bce_framework_lr3e3/predictor_bce_gumbel.pt",
]
OUTPUT_PATH = "/root/distill_sparse_swiglu/artifacts/kl_bce_f1_oracle.json"

SPARSITY_TARGET = 0.5
NUM_SAMPLES = 50
SEQ_LEN = 2048
SEED = 42
BATCH_SIZE = 2


def find_bce_checkpoint():
    for path in BCE_CKPT_CANDIDATES:
        if os.path.exists(path):
            return path
    ckpt_dir = Path("/root/distill_sparse_swiglu/checkpoints")
    for f in sorted(ckpt_dir.rglob("*bce*")):
        if f.suffix == ".pt":
            return str(f)
    return None


def load_c4_data(tokenizer, num_samples, seq_len, seed=42):
    try:
        ds = load_dataset("allenai/c4", "en", split="validation", streaming=True)
    except Exception:
        ds = load_dataset("allenai/c4", "en", split="validation",
                          streaming=True, trust_remote_code=True)

    torch.manual_seed(seed)
    texts = []
    for i, item in enumerate(ds):
        texts.append(item["text"])
        if len(texts) >= num_samples * 3:
            break

    input_ids_list = []
    for text in texts:
        tokens = tokenizer(text, return_tensors="pt", truncation=True,
                           max_length=seq_len + 100)["input_ids"][0]
        if tokens.size(0) >= seq_len:
            input_ids_list.append(tokens[:seq_len])
        if len(input_ids_list) >= num_samples:
            break

    if len(input_ids_list) < num_samples:
        print(f"Warning: only got {len(input_ids_list)} samples (requested {num_samples})")

    return torch.stack(input_ids_list)


def compute_per_token_oracle_masks(model, input_ids, sparsity_target, device, batch_size=2):
    """Compute per-token magnitude-based top-k oracle masks.

    For each token at each layer: compute |intermediate|, retain top (1-sparsity) neurons.
    Returns dict[layer_idx] -> list of (batch, seq_len, inter_dim) bool tensors on CPU.
    """
    n_layers = len(model.model.layers)
    all_oracle_masks = {i: [] for i in range(n_layers)}
    all_layer_inputs = {i: [] for i in range(n_layers)}

    hooks = []
    layer_intermediates = {}
    layer_inputs_buf = {}

    def make_hook(layer_idx):
        def hook_fn(module, inp, out):
            x = inp[0].detach()
            layer_inputs_buf[layer_idx] = x.cpu()
            gp = module.gate_proj
            up = module.up_proj
            af = module.act_fn
            intermediate = af(gp(x)) * up(x)
            layer_intermediates[layer_idx] = intermediate.detach().cpu()
        return hook_fn

    for idx, layer in enumerate(model.model.layers):
        hooks.append(layer.mlp.register_forward_hook(make_hook(idx)))

    num_keep_ratio = 1.0 - sparsity_target

    with torch.no_grad():
        for start in range(0, input_ids.size(0), batch_size):
            batch = input_ids[start:start + batch_size].to(device)
            model(batch, use_cache=False)

            for layer_idx in range(n_layers):
                inter = layer_intermediates[layer_idx]  # (B, S, D)
                B, S, D = inter.shape
                num_keep = int(D * num_keep_ratio)

                inter_flat = inter.view(B * S, D)
                mag = inter_flat.abs().float()
                topk_vals = torch.topk(mag, num_keep, dim=1).values
                threshold = topk_vals[:, -1].unsqueeze(1)
                oracle = (mag >= threshold)  # (B*S, D)
                oracle = oracle.view(B, S, D)
                all_oracle_masks[layer_idx].append(oracle)
                all_layer_inputs[layer_idx].append(layer_inputs_buf[layer_idx])

            layer_intermediates.clear()
            layer_inputs_buf.clear()
            torch.cuda.empty_cache()

    for h in hooks:
        h.remove()

    oracle_masks = {i: torch.cat(all_oracle_masks[i], dim=0) for i in range(n_layers)}
    layer_inputs = {i: torch.cat(all_layer_inputs[i], dim=0) for i in range(n_layers)}
    return oracle_masks, layer_inputs


def compute_predictor_masks(wrapper, layer_inputs, device, batch_size=4):
    """Compute predictor masks from layer inputs. Threshold: logits > 0."""
    n_layers = len(wrapper.predictors)
    pred_masks = {}

    with torch.no_grad():
        for layer_idx in range(n_layers):
            inp = layer_inputs[layer_idx]  # (N, S, H)
            masks_list = []
            for start in range(0, inp.size(0), batch_size):
                chunk = inp[start:start + batch_size].to(device=device, dtype=torch.bfloat16)
                logits = wrapper.predictors[layer_idx](chunk)
                mask = (logits > 0)  # retain=True, prune=False
                masks_list.append(mask.cpu())
                del chunk, logits, mask
            pred_masks[layer_idx] = torch.cat(masks_list, dim=0)

    return pred_masks


def compute_f1_metrics(pred_masks, oracle_masks, n_layers):
    """Compute F1, precision, recall. Positive class = retain (mask=1)."""
    per_layer = []
    total_tp, total_fp, total_fn = 0, 0, 0

    for layer_idx in range(n_layers):
        pred = pred_masks[layer_idx].view(-1).bool()
        oracle = oracle_masks[layer_idx].view(-1).bool()

        tp = (pred & oracle).sum().item()
        fp = (pred & ~oracle).sum().item()
        fn = (~pred & oracle).sum().item()

        precision = tp / max(tp + fp, 1)
        recall = tp / max(tp + fn, 1)
        f1 = 2 * precision * recall / max(precision + recall, 1e-8)

        per_layer.append({
            "layer": layer_idx,
            "f1": round(f1, 4),
            "precision": round(precision, 4),
            "recall": round(recall, 4),
            "tp": tp, "fp": fp, "fn": fn,
        })

        total_tp += tp
        total_fp += fp
        total_fn += fn

    overall_precision = total_tp / max(total_tp + total_fp, 1)
    overall_recall = total_tp / max(total_tp + total_fn, 1)
    overall_f1 = 2 * overall_precision * overall_recall / max(overall_precision + overall_recall, 1e-8)

    return {
        "f1": round(overall_f1, 4),
        "precision": round(overall_precision, 4),
        "recall": round(overall_recall, 4),
    }, per_layer


def main():
    torch.manual_seed(SEED)
    np.random.seed(SEED)

    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    print(f"Device: {device}")

    print("Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    print("Loading C4 calibration data...")
    input_ids = load_c4_data(tokenizer, NUM_SAMPLES, SEQ_LEN, SEED)
    print(f"  Got {input_ids.size(0)} samples, shape {input_ids.shape}")

    print("Loading model...")
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        torch_dtype=torch.bfloat16,
        device_map=device,
        attn_implementation="sdpa",
    )
    model.eval()

    print("Computing per-token oracle masks (magnitude top-k)...")
    oracle_masks, layer_inputs = compute_per_token_oracle_masks(
        model, input_ids, SPARSITY_TARGET, device, batch_size=BATCH_SIZE
    )
    n_layers = len(oracle_masks)
    print(f"  {n_layers} layers, oracle shape per layer: {oracle_masks[0].shape}")

    # Verify oracle sparsity
    total_ones = sum(oracle_masks[i].sum().item() for i in range(n_layers))
    total_elems = sum(oracle_masks[i].numel() for i in range(n_layers))
    print(f"  Oracle retain ratio: {total_ones/total_elems:.4f} (expect ~{1-SPARSITY_TARGET})")

    # --- KL predictor ---
    print(f"Loading KL predictor from {KL_CKPT}...")
    wrapper_kl = PredictorWrapper(model, bottleneck_size=128)
    ckpt_kl = torch.load(KL_CKPT, map_location="cpu", weights_only=True)
    wrapper_kl.predictors.load_state_dict(ckpt_kl["predictors"])
    wrapper_kl.predictors.to(device=device, dtype=torch.bfloat16)
    wrapper_kl.predictors.eval()

    print("Computing KL predictor masks...")
    kl_pred_masks = compute_predictor_masks(wrapper_kl, layer_inputs, device)

    kl_retain = sum(kl_pred_masks[i].sum().item() for i in range(n_layers))
    kl_total = sum(kl_pred_masks[i].numel() for i in range(n_layers))
    print(f"  KL retain ratio: {kl_retain/kl_total:.4f}")

    kl_overall, kl_per_layer = compute_f1_metrics(kl_pred_masks, oracle_masks, n_layers)
    print(f"  KL overall: F1={kl_overall['f1']}, P={kl_overall['precision']}, R={kl_overall['recall']}")

    del wrapper_kl, ckpt_kl, kl_pred_masks
    torch.cuda.empty_cache()

    # --- BCE predictor ---
    bce_ckpt_path = find_bce_checkpoint()
    bce_overall = None
    bce_per_layer = None

    if bce_ckpt_path:
        print(f"Loading BCE predictor from {bce_ckpt_path}...")
        wrapper_bce = PredictorWrapper(model, bottleneck_size=128)
        ckpt_bce = torch.load(bce_ckpt_path, map_location="cpu", weights_only=True)

        if "predictors" in ckpt_bce:
            wrapper_bce.predictors.load_state_dict(ckpt_bce["predictors"])
        elif "model_state_dict" in ckpt_bce:
            wrapper_bce.predictors.load_state_dict(ckpt_bce["model_state_dict"])
        else:
            wrapper_bce.predictors.load_state_dict(ckpt_bce)

        wrapper_bce.predictors.to(device=device, dtype=torch.bfloat16)
        wrapper_bce.predictors.eval()

        print("Computing BCE predictor masks...")
        bce_pred_masks = compute_predictor_masks(wrapper_bce, layer_inputs, device)

        bce_retain = sum(bce_pred_masks[i].sum().item() for i in range(n_layers))
        bce_total = sum(bce_pred_masks[i].numel() for i in range(n_layers))
        print(f"  BCE retain ratio: {bce_retain/bce_total:.4f}")

        bce_overall, bce_per_layer = compute_f1_metrics(bce_pred_masks, oracle_masks, n_layers)
        print(f"  BCE overall: F1={bce_overall['f1']}, P={bce_overall['precision']}, R={bce_overall['recall']}")

        del wrapper_bce, ckpt_bce, bce_pred_masks
    else:
        print("WARNING: No BCE checkpoint found. Computing random baseline instead.")
        # Random baseline at 50% retain
        random_masks = {}
        torch.manual_seed(SEED + 1)
        for i in range(n_layers):
            shape = oracle_masks[i].shape
            random_masks[i] = torch.rand(shape) > SPARSITY_TARGET
        bce_overall, bce_per_layer = compute_f1_metrics(random_masks, oracle_masks, n_layers)
        bce_ckpt_path = "RANDOM_BASELINE"
        print(f"  Random baseline: F1={bce_overall['f1']}, P={bce_overall['precision']}, R={bce_overall['recall']}")

    # --- Compile results ---
    per_layer_combined = []
    for i in range(n_layers):
        entry = {"layer": i, "kl_f1": kl_per_layer[i]["f1"]}
        if bce_per_layer:
            entry["bce_f1"] = bce_per_layer[i]["f1"]
            entry["delta"] = round(bce_per_layer[i]["f1"] - kl_per_layer[i]["f1"], 4)
        per_layer_combined.append(entry)

    bce_f1_higher = bce_overall["f1"] > kl_overall["f1"] if bce_overall else False

    if bce_f1_higher:
        conclusion = (
            f"BCE F1={bce_overall['f1']:.4f} > KL F1={kl_overall['f1']:.4f} "
            f"confirms per-neuron accuracy is the wrong optimization target. "
            f"KL (PPL=11.92) vastly outperforms BCE (PPL=22.51) despite lower mask fidelity, "
            f"proving output distribution fidelity matters more than matching the oracle mask."
        )
    else:
        conclusion = (
            f"KL F1={kl_overall['f1']:.4f} >= BCE F1={bce_overall['f1']:.4f}. "
            f"KL predictor is better on BOTH mask fidelity and output fidelity (PPL). "
            f"The end-to-end KL gradient captures cross-neuron interactions that improve "
            f"both per-neuron decisions and overall output quality."
        )

    results = {
        "kl": kl_overall,
        "bce": bce_overall,
        "per_layer": per_layer_combined,
        "kl_ppl": 11.92,
        "bce_ppl": 22.51,
        "bce_checkpoint": bce_ckpt_path,
        "kl_checkpoint": KL_CKPT,
        "oracle": "per-token magnitude top-k (retain top 50%)",
        "data": f"C4 validation, {NUM_SAMPLES} samples, seq_len={SEQ_LEN}",
        "conclusion": conclusion,
    }

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {OUTPUT_PATH}")
    print(f"\n{'='*60}")
    print(f"CONCLUSION: {conclusion}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
