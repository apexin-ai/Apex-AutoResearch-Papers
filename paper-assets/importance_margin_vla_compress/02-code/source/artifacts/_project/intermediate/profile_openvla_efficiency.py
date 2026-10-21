"""
OpenVLA inference efficiency profiling: latency / peak memory / token count
across pruning modes and keep ratios.

Usage:
    python profile_openvla_efficiency.py --mode l2norm_prune
    python profile_openvla_efficiency.py --mode random_prune --output res.csv
    python profile_openvla_efficiency.py --mode attention_prune \
        --k_ratios 1.0 0.9 0.7 0.5 0.3

Notes:
    - Single forward pass, batch=1, dummy 224x224 image, fixed prompt.
    - 3 warmup + 10 timed runs per k_ratio; reports median latency.
    - k_ratio == 1.0 disables the pruning hook (true baseline).
    - Uses torch.cuda.synchronize() around timing.
    - Observation hook runs BEFORE the prune hook so we capture the
      original token count cleanly (forward hooks chain in registration
      order; later hooks see earlier hooks' modified output).
"""
import argparse
import csv
import json
import math
import os
import sys
import time

os.environ.setdefault("CUDA_VISIBLE_DEVICES", "0")
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
DEFAULT_CHECKPOINT = "/root/autodl-tmp/openvla-libero-object"
DEFAULT_UNNORM_KEY = "libero_object"


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument(
        "--mode",
        choices=["l2norm_prune", "random_prune", "attention_prune"],
        default="l2norm_prune",
    )
    p.add_argument(
        "--k_ratios", type=float, nargs="+",
        default=[1.0, 0.9, 0.7, 0.5, 0.3],
        help="Keep ratios to profile. 1.0 = no pruning (baseline).",
    )
    p.add_argument("--warmup", type=int, default=3)
    p.add_argument("--repeats", type=int, default=10)
    p.add_argument("--gpu", type=int, default=0)
    p.add_argument("--model_path", type=str, default=DEFAULT_CHECKPOINT)
    p.add_argument("--unnorm_key", type=str, default=DEFAULT_UNNORM_KEY)
    p.add_argument(
        "--output",
        type=str,
        default="/root/autodl-tmp/importance_margin_vla_compress/artifacts/openvla_efficiency.csv",
    )
    p.add_argument(
        "--prompt_task",
        type=str,
        default="pick up the black bowl and place it on the plate",
        help="Task description used in the dummy prompt.",
    )
    return p.parse_args()


# --- Pruning hooks (copied from eval_openvla_l2norm_libero.py) ---

class RandomPruningHook:
    def __init__(self, k_ratio):
        self.k_ratio = k_ratio

    def __call__(self, module, input, output):
        B, N, D = output.shape
        keep = max(1, int(N * self.k_ratio))
        indices = torch.randperm(N)[:keep].sort().values.to(output.device)
        return output[:, indices, :]


class L2NormPruningHook:
    def __init__(self, k_ratio):
        self.k_ratio = k_ratio

    def __call__(self, module, input, output):
        B, N, D = output.shape
        keep = max(1, int(N * self.k_ratio))
        norms = torch.norm(output.float(), dim=-1)
        _, indices = torch.topk(norms, keep, dim=-1)
        indices = indices.sort(dim=-1).values
        return torch.gather(output, 1, indices.unsqueeze(-1).expand(-1, -1, D))


class AttentionPruningHook:
    def __init__(self, k_ratio, vla):
        self.k_ratio = k_ratio
        self.vla = vla

    def __call__(self, module, input, output):
        import torch.nn.functional as F

        B, N, D = output.shape
        keep = max(1, int(N * self.k_ratio))
        if keep >= N:
            return output

        lm = self.vla.language_model.model
        position_ids = torch.arange(N, device=output.device).unsqueeze(0).expand(B, -1)

        hidden = output
        all_attn = []

        with torch.no_grad():
            for layer_idx in range(min(2, len(lm.layers))):
                layer = lm.layers[layer_idx]
                normed = layer.input_layernorm(hidden)

                head_dim = layer.self_attn.head_dim
                n_q_heads = layer.self_attn.num_heads
                n_kv_heads = layer.self_attn.num_key_value_heads

                q = layer.self_attn.q_proj(normed)
                k = layer.self_attn.k_proj(normed)
                v = layer.self_attn.v_proj(normed)

                q = q.view(B, N, n_q_heads, head_dim).transpose(1, 2)
                k = k.view(B, N, n_kv_heads, head_dim).transpose(1, 2)
                v = v.view(B, N, n_kv_heads, head_dim).transpose(1, 2)

                cos, sin = lm.rotary_emb(v, position_ids)
                from transformers.models.llama.modeling_llama import rotate_half
                q_embed = (q * cos) + (rotate_half(q) * sin)
                k_embed = (k * cos) + (rotate_half(k) * sin)

                if n_kv_heads != n_q_heads:
                    n_rep = n_q_heads // n_kv_heads
                    k_embed = k_embed.repeat_interleave(n_rep, dim=1)
                    v = v.repeat_interleave(n_rep, dim=1)

                attn_weights = torch.matmul(q_embed, k_embed.transpose(-2, -1)) / math.sqrt(head_dim)
                attn_weights = F.softmax(attn_weights, dim=-1, dtype=torch.float32)
                all_attn.append(attn_weights)

                attn_out = torch.matmul(attn_weights.to(v.dtype), v)
                attn_out = attn_out.transpose(1, 2).reshape(B, N, n_q_heads * head_dim)
                attn_out = layer.self_attn.o_proj(attn_out)
                hidden = hidden + attn_out

                normed2 = layer.post_attention_layernorm(hidden)
                mlp_out = layer.mlp(normed2)
                hidden = hidden + mlp_out

        avg_attn = torch.stack(all_attn).mean(dim=0).mean(dim=1)
        importance = avg_attn.sum(dim=1)

        _, indices = torch.topk(importance, keep, dim=-1)
        indices = indices.sort(dim=-1).values
        return torch.gather(output, 1, indices.unsqueeze(-1).expand(-1, -1, D))


HOOK_FACTORIES = {
    "random_prune": lambda k, vla: RandomPruningHook(k),
    "l2norm_prune": lambda k, vla: L2NormPruningHook(k),
    "attention_prune": lambda k, vla: AttentionPruningHook(k, vla),
}


def load_model(model_path):
    print(f"[*] Loading OpenVLA from: {model_path}", flush=True)
    config = OpenVLAConfig.from_pretrained(model_path)
    vla = OpenVLAForActionPrediction.from_pretrained(
        model_path,
        config=config,
        torch_dtype=torch.bfloat16,
        low_cpu_mem_usage=True,
    ).to(DEVICE)
    with open(os.path.join(model_path, "dataset_statistics.json")) as f:
        vla.norm_stats = json.load(f)
    vla.eval()

    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    image_processor = PrismaticImageProcessor.from_pretrained(model_path)
    processor = PrismaticProcessor(image_processor=image_processor, tokenizer=tokenizer)
    print(
        f"[*] Model loaded, GPU alloc: "
        f"{torch.cuda.max_memory_allocated()/1e9:.2f} GB",
        flush=True,
    )
    return vla, processor


def make_inputs(processor, task_label):
    img = Image.new("RGB", (224, 224), (128, 128, 128))
    prompt = f"In: What action should the robot take to {task_label.lower()}?\nOut:"
    return processor(prompt, img).to(DEVICE, dtype=torch.bfloat16)


def profile_one_k(vla, inputs, mode, k_ratio, warmup, repeats):
    """Install (obs + optional prune) hooks, run warmup + timed forwards.

    Hook order on vla.projector:
        1. obs_hook  - records original projector output token count
        2. prune_hook (if k<1.0) - prunes and records kept count
    """
    counts = {"n_original": -1, "n_kept": -1}

    def obs_hook(m, i, o):
        counts["n_original"] = o.shape[1]
        return o

    handles = [vla.projector.register_forward_hook(obs_hook)]

    if k_ratio < 1.0:
        prune = HOOK_FACTORIES[mode](k_ratio, vla)

        def prune_and_count(m, i, o):
            pruned = prune(m, i, o)
            counts["n_kept"] = pruned.shape[1]
            return pruned

        handles.append(vla.projector.register_forward_hook(prune_and_count))
    else:
        def kept_eq_orig(m, i, o):
            counts["n_kept"] = o.shape[1]
            return o

        handles.append(vla.projector.register_forward_hook(kept_eq_orig))

    try:
        with torch.no_grad():
            for _ in range(warmup):
                vla.predict_action(
                    **inputs, unnorm_key=DEFAULT_UNNORM_KEY, do_sample=False
                )
        torch.cuda.synchronize()

        torch.cuda.reset_peak_memory_stats()
        latencies_ms = []
        with torch.no_grad():
            for _ in range(repeats):
                torch.cuda.synchronize()
                t0 = time.perf_counter()
                vla.predict_action(
                    **inputs, unnorm_key=DEFAULT_UNNORM_KEY, do_sample=False
                )
                torch.cuda.synchronize()
                latencies_ms.append((time.perf_counter() - t0) * 1000.0)
        peak_mb = torch.cuda.max_memory_allocated() / (1024**2)
    finally:
        for h in handles:
            h.remove()

    return latencies_ms, peak_mb, counts["n_original"], counts["n_kept"]


def main():
    args = parse_args()
    global DEVICE, DEFAULT_UNNORM_KEY
    DEVICE = torch.device(f"cuda:{args.gpu}")
    DEFAULT_UNNORM_KEY = args.unnorm_key

    torch.manual_seed(0)
    np.random.seed(0)

    vla, processor = load_model(args.model_path)
    inputs = make_inputs(processor, args.prompt_task)

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    print(
        f"[*] Profiling mode={args.mode} | k_ratios={args.k_ratios} | "
        f"warmup={args.warmup} | repeats={args.repeats}",
        flush=True,
    )

    rows = []
    for k in args.k_ratios:
        latencies, peak_mb, n_orig, n_kept = profile_one_k(
            vla, inputs, args.mode, k, args.warmup, args.repeats
        )
        med = float(np.median(latencies))
        p10 = float(np.percentile(latencies, 10))
        p90 = float(np.percentile(latencies, 90))
        row = {
            "mode": args.mode,
            "k_ratio": k,
            "latency_ms_median": round(med, 3),
            "latency_ms_p10": round(p10, 3),
            "latency_ms_p90": round(p90, 3),
            "peak_mem_mb": round(peak_mb, 2),
            "tokens_original": n_orig,
            "tokens_kept": n_kept,
        }
        rows.append(row)
        print(
            f"  k={k:.2f}  latency={med:.2f}ms (p10/p90={p10:.1f}/{p90:.1f}) "
            f"peak={peak_mb:.0f}MB tokens={n_orig}->{n_kept}",
            flush=True,
        )

    with open(args.output, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"[*] Saved CSV: {args.output}", flush=True)


if __name__ == "__main__":
    main()
