"""
OpenVLA Attention Entropy Analysis.

Computes how uniformly OpenVLA's LLM backbone (Llama-2 7B) attends to
vision tokens. Compares with SmolVLA's entropy ratio (0.98 = near-uniform).

Hypothesis: OpenVLA has more concentrated attention (lower entropy ratio)
-> tokens have differentiated importance -> can tolerate pruning.

Usage:
    CUDA_VISIBLE_DEVICES=1 python analyze_openvla_attention_entropy.py
"""

import json, math, os, sys, time

os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["HF_HUB_OFFLINE"] = "1"

sys.path.insert(0, "/root/autodl-tmp/openvla_deps")

import numpy as np
import torch
from PIL import Image

hf_dir = "/root/autodl-tmp/openvla-repo/prismatic/extern/hf"
init_path = os.path.join(hf_dir, "__init__.py")
if not os.path.exists(init_path):
    open(init_path, "w").close()
sys.path.insert(0, "/root/autodl-tmp/openvla-repo/prismatic/extern")
from hf.configuration_prismatic import OpenVLAConfig
from hf.modeling_prismatic import OpenVLAForActionPrediction
from hf.processing_prismatic import PrismaticImageProcessor, PrismaticProcessor

DEVICE = torch.device("cuda:0")
CHECKPOINT_PATH = "/root/autodl-tmp/openvla-libero-object"
N_VISION_TOKENS = 256
N_SAMPLES = 20


def load_model():
    print(f"[*] Loading OpenVLA from: {CHECKPOINT_PATH}", flush=True)
    config = OpenVLAConfig.from_pretrained(CHECKPOINT_PATH)
    vla = OpenVLAForActionPrediction.from_pretrained(
        CHECKPOINT_PATH,
        config=config,
        torch_dtype=torch.bfloat16,
        low_cpu_mem_usage=True,
        attn_implementation="eager",
    ).to(DEVICE)
    with open(os.path.join(CHECKPOINT_PATH, "dataset_statistics.json")) as f:
        vla.norm_stats = json.load(f)
    vla.eval()

    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(CHECKPOINT_PATH)
    image_processor = PrismaticImageProcessor.from_pretrained(CHECKPOINT_PATH)
    processor = PrismaticProcessor(image_processor=image_processor, tokenizer=tokenizer)
    print(f"[*] Model loaded, GPU mem: {torch.cuda.max_memory_allocated()/1e9:.1f} GB", flush=True)
    return vla, processor


def compute_entropy_bits(p, eps=1e-10):
    p = p.clamp(min=eps)
    return -(p * p.log2()).sum(dim=-1)


def main():
    print("=" * 60)
    print("OpenVLA Attention Entropy Analysis")
    print("=" * 60, flush=True)

    t0 = time.time()
    vla, processor = load_model()

    n_layers = vla.language_model.config.num_hidden_layers
    n_heads = vla.language_model.config.num_attention_heads
    print(f"[*] LLM: {n_layers} layers, {n_heads} heads", flush=True)

    prompts = [
        "In: What action should the robot take to pick up the alphabet soup?\nOut:",
        "In: What action should the robot take to put the cream cheese in the bowl?\nOut:",
        "In: What action should the robot take to pick up the butter?\nOut:",
        "In: What action should the robot take to put the chocolate pudding in the basket?\nOut:",
        "In: What action should the robot take to pick up the ketchup?\nOut:",
        "In: What action should the robot take to open the top drawer?\nOut:",
        "In: What action should the robot take to push the plate to the front?\nOut:",
        "In: What action should the robot take to stack the blocks?\nOut:",
        "In: What action should the robot take to close the microwave?\nOut:",
        "In: What action should the robot take to pick up the red mug?\nOut:",
    ]

    all_entropies = []
    all_vision_attn_frac = []

    for sample_idx in range(N_SAMPLES):
        img = Image.fromarray(np.random.randint(0, 255, (224, 224, 3), dtype=np.uint8))
        prompt = prompts[sample_idx % len(prompts)]
        inputs = processor(prompt, img).to(DEVICE, dtype=torch.bfloat16)

        with torch.no_grad():
            outputs = vla(
                **inputs,
                output_attentions=True,
                return_dict=True,
            )

        attentions = outputs.attentions

        if sample_idx == 0:
            seq_len = attentions[0].shape[-1]
            text_start = 1 + N_VISION_TOKENS
            n_text = seq_len - text_start
            print(f"[*] Seq len: {seq_len}, text starts at: {text_start}, n_text: {n_text}")
            print(f"[*] Attention shape per layer: {attentions[0].shape}")
            print(f"[*] Actual layers returned: {len(attentions)}", flush=True)

        text_start = 1 + N_VISION_TOKENS
        sample_entropies = np.zeros((n_layers, n_heads))
        sample_vis_frac = np.zeros((n_layers, n_heads))

        for layer_idx in range(len(attentions)):
            attn = attentions[layer_idx]  # (1, H, seq_len, seq_len)

            # Attention from text tokens to vision tokens
            text_to_vision = attn[0, :, text_start:, 1:1+N_VISION_TOKENS].float()  # (H, n_text, 256)

            # Fraction of total attention going to vision tokens
            text_to_all = attn[0, :, text_start:, :].float()  # (H, n_text, seq_len)
            vis_frac = text_to_vision.sum(dim=-1) / text_to_all.sum(dim=-1).clamp(min=1e-10)  # (H, n_text)
            sample_vis_frac[layer_idx] = vis_frac.mean(dim=-1).cpu().numpy()

            # Normalize to distribution over vision tokens only
            vis_sum = text_to_vision.sum(dim=-1, keepdim=True).clamp(min=1e-10)
            text_to_vision_norm = text_to_vision / vis_sum  # (H, n_text, 256)

            # Entropy per head, averaged over text token positions
            ent = compute_entropy_bits(text_to_vision_norm)  # (H, n_text)
            sample_entropies[layer_idx] = ent.mean(dim=-1).cpu().numpy()  # (H,)

        all_entropies.append(sample_entropies)
        all_vision_attn_frac.append(sample_vis_frac)

        if (sample_idx + 1) % 5 == 0:
            cur_mean = np.mean(all_entropies)
            cur_ratio = cur_mean / math.log2(N_VISION_TOKENS)
            print(f"[*] {sample_idx+1}/{N_SAMPLES} done, "
                  f"mean entropy: {cur_mean:.4f} bits, "
                  f"ratio: {cur_ratio:.4f}", flush=True)

        del outputs, attentions
        torch.cuda.empty_cache()

    all_entropies = np.array(all_entropies)       # (N_SAMPLES, n_layers, n_heads)
    all_vision_attn_frac = np.array(all_vision_attn_frac)

    max_entropy = math.log2(N_VISION_TOKENS)  # 8.0

    per_layer_mean = all_entropies.mean(axis=(0, 2))
    per_layer_std = all_entropies.std(axis=(0, 2))
    per_layer_ratio = per_layer_mean / max_entropy
    per_layer_vis_frac = all_vision_attn_frac.mean(axis=(0, 2))

    overall_mean = float(all_entropies.mean())
    overall_std = float(all_entropies.std())
    overall_ratio = overall_mean / max_entropy
    overall_vis_frac = float(all_vision_attn_frac.mean())

    min_layer = int(per_layer_mean.argmin())
    max_layer = int(per_layer_mean.argmax())

    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)
    print(f"Vision tokens: {N_VISION_TOKENS}")
    print(f"Max entropy: {max_entropy:.4f} bits")
    print(f"Samples: {N_SAMPLES}")
    print()
    print(f"Overall mean entropy:     {overall_mean:.4f} bits")
    print(f"Overall entropy RATIO:    {overall_ratio:.4f}")
    print(f"Overall vision attn frac: {overall_vis_frac:.4f}")
    print()
    print(f"SmolVLA entropy ratio:    0.98")
    print(f"OpenVLA entropy ratio:    {overall_ratio:.4f}")
    print(f"Delta:                    {0.98 - overall_ratio:+.4f}")
    print()
    print(f"Min entropy layer: {min_layer} (ratio={per_layer_ratio[min_layer]:.4f})")
    print(f"Max entropy layer: {max_layer} (ratio={per_layer_ratio[max_layer]:.4f})")
    print()
    print("Per-layer breakdown:")
    print(f"{'Layer':>5} {'Ratio':>7} {'Entropy':>9} {'VisFrac':>8}  Bar")
    for i in range(n_layers):
        bar = "#" * int(per_layer_ratio[i] * 40)
        print(f"  {i:3d}  {per_layer_ratio[i]:.4f}  {per_layer_mean[i]:.4f}    {per_layer_vis_frac[i]:.4f}  {bar}")

    results = {
        "model": "OpenVLA (Llama-2 7B)",
        "n_vision_tokens": N_VISION_TOKENS,
        "max_entropy_bits": max_entropy,
        "n_samples": N_SAMPLES,
        "n_layers": n_layers,
        "n_heads": n_heads,
        "overall_mean_entropy": overall_mean,
        "overall_std_entropy": overall_std,
        "overall_entropy_ratio": overall_ratio,
        "overall_vision_attn_fraction": overall_vis_frac,
        "smolvla_entropy_ratio": 0.98,
        "per_layer_mean_entropy": per_layer_mean.tolist(),
        "per_layer_std_entropy": per_layer_std.tolist(),
        "per_layer_entropy_ratio": per_layer_ratio.tolist(),
        "per_layer_vision_attn_fraction": per_layer_vis_frac.tolist(),
        "min_entropy_layer": {
            "layer": min_layer,
            "entropy": float(per_layer_mean[min_layer]),
            "ratio": float(per_layer_ratio[min_layer]),
        },
        "max_entropy_layer": {
            "layer": max_layer,
            "entropy": float(per_layer_mean[max_layer]),
            "ratio": float(per_layer_ratio[max_layer]),
        },
    }

    out_path = "/root/autodl-tmp/importance_margin_vla_compress/artifacts/openvla_attention_entropy.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\n[*] Results saved to {out_path}")
    print(f"[*] Total time: {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
