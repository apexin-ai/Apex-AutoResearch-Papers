# Verify KL-derived oracle masks: load trained KL predictor, generate binary masks on
# calibration data, report per-layer sparsity and agreement with magnitude-based masks.
# Full masks are generated on-the-fly during training (too large to pre-store on disk).

import argparse
import importlib.util
import os
import sys

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data_utils import get_calibration_loader
from predictor import PredictorWrapper


def _best_attn_impl():
    if importlib.util.find_spec("flash_attn"):
        return "flash_attention_2"
    return "sdpa"


def main():
    p = argparse.ArgumentParser(description="Generate and verify KL oracle masks")
    p.add_argument("--model_name_or_path", type=str,
                   default="/root/autodl-tmp/models/llama-3.1-8b")
    p.add_argument("--kl_checkpoint", type=str, required=True,
                   help="Path to trained KL predictor checkpoint")
    p.add_argument("--gpu", type=int, default=0)
    p.add_argument("--batch_size", type=int, default=4)
    p.add_argument("--seq_len", type=int, default=2048)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--num_verify_batches", type=int, default=5)
    p.add_argument("--sparsity_target", type=float, default=0.5,
                   help="Expected sparsity for magnitude-based comparison")
    p.add_argument("--output_path", type=str, default=None,
                   help="Save sample masks to this path (optional)")
    p.add_argument("--bottleneck_dim", type=int, default=128)
    args = p.parse_args()

    device = torch.device(f"cuda:{args.gpu}")

    print(f"Loading model from {args.model_name_or_path} ...")
    tokenizer = AutoTokenizer.from_pretrained(args.model_name_or_path)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(
        args.model_name_or_path,
        torch_dtype=torch.bfloat16,
        device_map={"": device},
        attn_implementation=_best_attn_impl(),
    )
    model.eval()

    wrapper = PredictorWrapper(model, bottleneck_size=args.bottleneck_dim)

    print(f"Loading KL predictor from {args.kl_checkpoint} ...")
    ckpt = torch.load(args.kl_checkpoint, map_location=device, weights_only=True)
    wrapper.predictors.load_state_dict(ckpt["predictors"])
    wrapper.predictors.to(device=device, dtype=torch.bfloat16)
    wrapper.predictors.eval()

    print(f"Loading calibration data (wikitext-103, seed={args.seed}) ...")
    dataloader = get_calibration_loader(tokenizer, args.batch_size, args.seq_len, args.seed)
    data_iter = iter(dataloader)

    num_layers = len(wrapper.predictors)
    layer_density_sum = [0.0] * num_layers
    layer_agreement_sum = [0.0] * num_layers
    layer_count = [0] * num_layers

    print(f"\nVerifying {args.num_verify_batches} batches ...")
    for batch_idx in range(args.num_verify_batches):
        batch = next(data_iter)
        input_ids = batch["input_ids"].to(device)

        wrapper.forward_dense(input_ids, capture_intermediates=True)
        layer_inputs = wrapper.get_layer_inputs()
        intermediates = wrapper.get_intermediates()

        for layer_idx in range(num_layers):
            if layer_idx not in layer_inputs:
                continue
            inp = layer_inputs[layer_idx]
            with torch.no_grad():
                kl_logits = wrapper.predictors[layer_idx](inp)
            kl_mask = (kl_logits > 0).float()

            density = kl_mask.mean().item()
            layer_density_sum[layer_idx] += density
            layer_count[layer_idx] += 1

            # Magnitude-based mask for comparison
            dense_act = intermediates[layer_idx]
            k = int(dense_act.shape[-1] * (1 - args.sparsity_target))
            abs_vals = dense_act.abs()
            topk_vals, _ = abs_vals.topk(k, dim=-1)
            threshold = topk_vals[..., -1:]
            mag_mask = (abs_vals >= threshold).float()

            agreement = ((kl_mask == mag_mask).float().mean().item())
            layer_agreement_sum[layer_idx] += agreement

            if batch_idx == 0 and layer_idx % 8 == 0:
                print(f"  Layer {layer_idx:2d}: KL density={density:.3f}, "
                      f"KL-vs-magnitude agreement={agreement:.3f}")

        if batch_idx == 0:
            print(f"  (showing every 8th layer for batch 0)")

    print(f"\n=== Per-layer stats (mean over {args.num_verify_batches} batches) ===")
    for layer_idx in range(num_layers):
        if layer_count[layer_idx] > 0:
            avg_density = layer_density_sum[layer_idx] / layer_count[layer_idx]
            avg_agreement = layer_agreement_sum[layer_idx] / layer_count[layer_idx]
            print(f"  Layer {layer_idx:2d}: density={avg_density:.3f} "
                  f"(sparsity={1-avg_density:.3f})  agreement={avg_agreement:.3f}")

    total_density = sum(layer_density_sum) / max(sum(layer_count), 1)
    total_agreement = sum(layer_agreement_sum) / max(sum(layer_count), 1)
    print(f"\n  Global: density={total_density:.3f} (sparsity={1-total_density:.3f})  "
          f"agreement={total_agreement:.3f}")

    if args.output_path:
        # Save one batch of masks as sample
        batch = next(data_iter)
        input_ids = batch["input_ids"].to(device)
        wrapper.forward_dense(input_ids, capture_intermediates=True)
        layer_inputs = wrapper.get_layer_inputs()
        sample = {}
        for layer_idx in range(num_layers):
            if layer_idx not in layer_inputs:
                continue
            with torch.no_grad():
                kl_logits = wrapper.predictors[layer_idx](layer_inputs[layer_idx])
            sample[layer_idx] = (kl_logits > 0).cpu()
        torch.save(sample, args.output_path)
        print(f"\nSaved sample masks ({len(sample)} layers) -> {args.output_path}")

    print("\nVerification complete.")


if __name__ == "__main__":
    main()
