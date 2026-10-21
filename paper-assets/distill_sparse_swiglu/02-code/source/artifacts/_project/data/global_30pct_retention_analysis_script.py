"""Per-layer retention analysis for 30% global top-k allocation.

Demonstrates which layers get starved by global allocation, explaining
why MMLU=25.27% (global) << 38.61% (TEAL) / 40.61% (uniform).
"""

import importlib.util
import json
import os
import sys
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

sys.path.insert(0, "/root/distill_sparse_swiglu/src")
from data_utils import get_eval_dataset
from predictor import PredictorWrapper

MODEL_PATH = "/root/autodl-tmp/models/llama-3.1-8b"
PREDICTOR_PATH = "/root/distill_sparse_swiglu/checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt"
SPARSITY_TARGET = 0.3
NUM_CALIB = 50
SEQ_LEN = 2048
OUTPUT_PATH = "/root/distill_sparse_swiglu/artifacts/global_30pct_retention_analysis.json"
DEVICE = "cuda:0"


def best_attn_impl():
    if importlib.util.find_spec("flash_attn"):
        return "flash_attention_2"
    return "sdpa"


def global_topk_masks(layer_scores, sparsity_target):
    """Normalize per-layer scores by mean, then global top-k."""
    items = sorted(layer_scores.items())
    normalized = []
    for li, s in items:
        s_f = s.float()
        mu = s_f.mean()
        normalized.append((li, s_f / mu if mu > 1e-12 else s_f))
    all_s = torch.cat([s for _, s in normalized])
    num_keep = int(len(all_s) * (1.0 - sparsity_target))
    thr = torch.topk(all_s, num_keep).values[-1]
    return {li: (s >= thr).to(torch.bfloat16) for li, s in normalized}


@torch.no_grad()
def compute_layer_scores(wrapper, input_ids, calib_batch_size=4):
    """Compute per-layer neuron importance scores from predictor + activations."""
    accum_scores = {}
    n_batches = 0
    for start in range(0, input_ids.size(0), calib_batch_size):
        batch = input_ids[start:start + calib_batch_size]
        wrapper.forward_dense(batch, capture_intermediates=True)
        intermediates = wrapper.get_intermediates()
        layer_inputs = wrapper.get_layer_inputs()
        with torch.no_grad():
            for layer_idx in range(len(wrapper.predictors)):
                if layer_idx not in layer_inputs or layer_idx not in intermediates:
                    continue
                logits = wrapper.predictors[layer_idx](layer_inputs[layer_idx])
                hard_mask = (logits > 0).float()
                mag = intermediates[layer_idx].abs().float()
                scores = (mag * hard_mask).mean(dim=(0, 1))
                if layer_idx not in accum_scores:
                    accum_scores[layer_idx] = scores
                else:
                    accum_scores[layer_idx] = accum_scores[layer_idx] + scores
        n_batches += 1
        if start == 0:
            print(f"  Dry-run batch 0 OK, layers={len(accum_scores)}, "
                  f"score shape={accum_scores[0].shape}")
    layer_scores = {li: accum_scores[li] / n_batches for li in sorted(accum_scores)}
    return layer_scores


def analyze_retention(masks, n_layers=32, inter_dim=14336):
    """Compute per-layer retention statistics."""
    per_layer = []
    for li in range(n_layers):
        mask = masks[li]
        retained = mask.sum().item()
        ratio = retained / inter_dim
        per_layer.append({
            "layer": li,
            "retained_neurons": int(retained),
            "mean_retention": round(ratio, 4),
        })

    retentions = [p["mean_retention"] for p in per_layer]

    early = retentions[:8]
    middle = retentions[8:24]
    knowledge = retentions[12:21]
    late = retentions[24:]

    min_layer = min(per_layer, key=lambda x: x["mean_retention"])
    max_layer = max(per_layer, key=lambda x: x["mean_retention"])

    starved = [p for p in per_layer if p["mean_retention"] < 0.50]

    return {
        "per_layer_retention": per_layer,
        "starved_layers": starved,
        "knowledge_layer_avg_retention": round(sum(knowledge) / len(knowledge), 4),
        "early_layer_avg_retention": round(sum(early) / len(early), 4),
        "middle_layer_avg_retention": round(sum(middle) / len(middle), 4),
        "late_layer_avg_retention": round(sum(late) / len(late), 4),
        "min_retention_layer": {
            "layer": min_layer["layer"],
            "retention": min_layer["mean_retention"]
        },
        "max_retention_layer": {
            "layer": max_layer["layer"],
            "retention": max_layer["mean_retention"]
        },
        "uniform_baseline_retention": 0.70,
        "sparsity_target": SPARSITY_TARGET,
        "num_calib_samples": NUM_CALIB,
    }


def main():
    print(f"=== Global 30% Per-Layer Retention Analysis ===")
    print(f"Model: {MODEL_PATH}")
    print(f"Predictor: {PREDICTOR_PATH}")
    print(f"Sparsity target: {SPARSITY_TARGET}")
    print(f"Calibration: {NUM_CALIB} samples, seq_len={SEQ_LEN}")
    print()

    device = torch.device(DEVICE)

    print("Loading model...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        torch_dtype=torch.bfloat16,
        device_map={"": device},
        attn_implementation=best_attn_impl(),
    )
    model.eval()

    print("Loading predictor...")
    wrapper = PredictorWrapper(model, bottleneck_size=128)
    ckpt = torch.load(PREDICTOR_PATH, map_location=device, weights_only=True)
    wrapper.predictors.load_state_dict(ckpt["predictors"])
    wrapper.predictors.to(device=device, dtype=torch.bfloat16)
    wrapper.predictors.eval()
    wrapper.gumbel_mask.hard = True

    print("Loading calibration data (C4)...")
    calib_data = get_eval_dataset("c4", tokenizer, SEQ_LEN)
    n_calib = min(NUM_CALIB, len(calib_data))
    calib_ids = torch.stack([calib_data[i]["input_ids"] for i in range(n_calib)]).to(device)
    print(f"  Using {n_calib} sequences, shape={calib_ids.shape}")

    # --- Dry run with 2 samples ---
    print("\n--- Dry run (2 samples) ---")
    dry_ids = calib_ids[:2]
    dry_scores = compute_layer_scores(wrapper, dry_ids, calib_batch_size=2)
    dry_masks = global_topk_masks(dry_scores, SPARSITY_TARGET)
    dry_total = sum(m.numel() for m in dry_masks.values())
    dry_kept = sum(m.sum().item() for m in dry_masks.values())
    print(f"  Dry-run sparsity: {1 - dry_kept/dry_total:.4f} (target: {SPARSITY_TARGET})")
    for li in [0, 15, 16, 17, 31]:
        r = dry_masks[li].sum().item() / 14336
        print(f"  Layer {li}: retention={r:.4f}")
    print("  Dry run OK, proceeding with full calibration...\n")

    # --- Full calibration ---
    print(f"--- Full calibration ({n_calib} samples) ---")
    layer_scores = compute_layer_scores(wrapper, calib_ids, calib_batch_size=4)
    global_masks = global_topk_masks(layer_scores, SPARSITY_TARGET)

    total_n = sum(m.numel() for m in global_masks.values())
    total_kept = sum(m.sum().item() for m in global_masks.values())
    actual_sparsity = 1 - total_kept / total_n
    print(f"  Actual global sparsity: {actual_sparsity:.4f}")

    # --- Analyze ---
    result = analyze_retention(global_masks)
    result["actual_global_sparsity"] = round(actual_sparsity, 4)

    # Print summary
    print(f"\n{'='*60}")
    print("PER-LAYER RETENTION (global top-k, 30% target)")
    print(f"{'='*60}")
    print(f"{'Layer':<6} {'Retention':<10} {'Neurons Kept':<14} {'Status'}")
    print("-" * 50)
    for p in result["per_layer_retention"]:
        status = "STARVED" if p["mean_retention"] < 0.50 else ""
        if p["mean_retention"] < 0.30:
            status = "CRITICAL"
        print(f"  {p['layer']:<4} {p['mean_retention']:<10.4f} "
              f"{p['retained_neurons']:<14} {status}")

    print(f"\n--- Summary ---")
    print(f"Early layers (0-7):      avg retention = {result['early_layer_avg_retention']:.4f}")
    print(f"Middle layers (8-23):    avg retention = {result['middle_layer_avg_retention']:.4f}")
    print(f"Knowledge layers (12-20): avg retention = {result['knowledge_layer_avg_retention']:.4f}")
    print(f"Late layers (24-31):     avg retention = {result['late_layer_avg_retention']:.4f}")
    print(f"Min retention: layer {result['min_retention_layer']['layer']} "
          f"({result['min_retention_layer']['retention']:.4f})")
    print(f"Max retention: layer {result['max_retention_layer']['layer']} "
          f"({result['max_retention_layer']['retention']:.4f})")
    print(f"Starved layers (<50%): {len(result['starved_layers'])}")
    print(f"Uniform baseline: every layer = 0.70")

    # Interpretation
    knowledge_ret = result["knowledge_layer_avg_retention"]
    n_starved = len(result["starved_layers"])
    if knowledge_ret < 0.50:
        interpretation = (
            f"Knowledge layers (L12-L20) retain only {knowledge_ret:.1%} of neurons under "
            f"global allocation, far below the uniform 70%. This severe under-allocation "
            f"destroys factual knowledge stored in middle-layer FFNs, explaining the MMLU "
            f"collapse from 40.61% (uniform) to 25.27% (global). {n_starved} layers are "
            f"starved below 50% retention."
        )
    elif knowledge_ret < 0.65:
        interpretation = (
            f"Knowledge layers (L12-L20) retain {knowledge_ret:.1%}, moderately below "
            f"uniform 70%. Combined with {n_starved} starved layers, global allocation "
            f"causes uneven capacity distribution that degrades knowledge tasks."
        )
    else:
        interpretation = (
            f"Knowledge layers retain {knowledge_ret:.1%}, close to uniform. "
            f"The MMLU gap may stem from other factors (e.g., specific critical layers "
            f"being starved rather than the entire middle region)."
        )
    result["interpretation"] = interpretation
    print(f"\nInterpretation: {interpretation}")

    # Also store raw normalized scores for further analysis
    score_stats = []
    for li in sorted(layer_scores):
        s = layer_scores[li].float()
        score_stats.append({
            "layer": li,
            "mean_score": round(s.mean().item(), 6),
            "std_score": round(s.std().item(), 6),
            "max_score": round(s.max().item(), 6),
            "min_score": round(s.min().item(), 6),
        })
    result["raw_score_stats"] = score_stats

    # Save
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(result, f, indent=2)
    print(f"\nResults saved to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
