"""W9: Compounding scaling — quantify super-additivity of per-head distortion."""
import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
os.environ["HF_DATASETS_OFFLINE"] = "1"
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

import json
import math
import time
import torch
import torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig
from eval_ppl import patch_attention, restore_attention


def load_calibration_data(tokenizer, path, num_samples, seq_len, device):
    with open(path) as f:
        samples = json.load(f)
    all_ids = []
    for s in samples:
        tokens = tokenizer.encode(s["text"], add_special_tokens=False)
        if len(tokens) >= seq_len:
            all_ids.append(tokens[:seq_len])
        if len(all_ids) >= num_samples:
            break
    if not all_ids:
        raise RuntimeError(f"No calibration seqs with >= {seq_len} tokens")
    return torch.tensor(all_ids, dtype=torch.long, device=device)


def compute_ppl_batched(model, input_ids, seq_len, batch_size, device):
    total_loss = 0.0
    total_tokens = 0
    n = input_ids.shape[0]
    with torch.no_grad():
        for start in range(0, n, batch_size):
            end = min(start + batch_size, n)
            batch = input_ids[start:end]
            outputs = model(
                batch, use_cache=False,
                cache_position=torch.arange(seq_len, device=device)
            )
            shift_logits = outputs.logits[:, :-1].contiguous()
            shift_labels = batch[:, 1:].contiguous()
            loss = F.cross_entropy(
                shift_logits.float().view(-1, shift_logits.shape[-1]),
                shift_labels.view(-1),
                reduction="sum"
            )
            total_loss += loss.item()
            total_tokens += shift_labels.numel()
    return math.exp(total_loss / total_tokens)


def main():
    device = "cuda:0"
    model_name = "/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B"
    profiles_path = "hires_profiles.json"
    calib_path = "calibration_hires.json"
    output_json = "w9_compounding_scaling_results.json"
    output_pdf = "figures/fig_compounding_scaling.pdf"
    output_png = "figures/fig_compounding_scaling.png"
    num_samples = 64
    seq_len = 2048
    batch_size = 4
    n_values = [1, 2, 4, 8, 16, 32, 64]

    t0 = time.time()

    print("Loading profiles...")
    with open(profiles_path) as f:
        raw = json.load(f)
    profiles = raw["profiles"] if "profiles" in raw else raw

    head_deltas = []
    for l_str in sorted(profiles.keys(), key=int):
        for h_str in sorted(profiles[l_str].keys(), key=int):
            d2 = profiles[l_str][h_str]["quantization"].get("2", 0.0)
            head_deltas.append({
                "layer": int(l_str),
                "head": int(h_str),
                "key": f"{l_str},{h_str}",
                "delta_2bit": d2,
            })
    head_deltas.sort(key=lambda x: x["delta_2bit"], reverse=True)

    print(f"Total KV heads: {len(head_deltas)}")
    print(f"Top-5: {[(h['key'], round(h['delta_2bit'], 4)) for h in head_deltas[:5]]}")

    print(f"\nLoading {model_name} in bf16...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name, torch_dtype=torch.bfloat16, attn_implementation="eager"
    )
    model = model.to(device)
    model.eval()
    print(f"GPU mem: {torch.cuda.memory_allocated(device) / 1e9:.1f}GB")

    print(f"Loading calibration data ({num_samples} x {seq_len})...")
    input_ids = load_calibration_data(tokenizer, calib_path, num_samples, seq_len, device)
    print(f"Loaded {input_ids.shape[0]} sequences")

    print("\nMeasuring baseline PPL...")
    measured_baseline = compute_ppl_batched(model, input_ids, seq_len, batch_size, device)
    print(f"Baseline PPL: {measured_baseline:.4f}")

    results = []
    for n in n_values:
        print(f"\n--- n={n} ---")
        top_n = head_deltas[:n]

        allocation = {}
        for h in top_n:
            allocation[h["key"]] = ["quant", 2]

        sum_individual = sum(h["delta_2bit"] for h in top_n)

        orig_fwds = patch_attention(model, allocation)
        joint_ppl = compute_ppl_batched(model, input_ids, seq_len, batch_size, device)
        restore_attention(model, orig_fwds)

        joint_delta = joint_ppl - measured_baseline
        predicted_ppl = measured_baseline + sum_individual
        ratio = joint_delta / sum_individual if sum_individual > 0 else float('nan')

        print(f"  sum_indiv={sum_individual:.4f}  joint={joint_ppl:.4f}  pred={predicted_ppl:.4f}  ratio={ratio:.4f}")

        results.append({
            "n": n,
            "heads": [h["key"] for h in top_n],
            "sum_individual_delta": round(sum_individual, 6),
            "joint_ppl": round(joint_ppl, 4),
            "joint_delta": round(joint_delta, 6),
            "predicted_ppl": round(predicted_ppl, 4),
            "super_additive_ratio": round(ratio, 4),
        })

    total_time = time.time() - t0

    output = {
        "experiment": "w9_compounding_scaling",
        "model": model_name,
        "baseline_ppl_measured": round(measured_baseline, 4),
        "calibration": {"path": calib_path, "num_samples": num_samples, "seq_len": seq_len},
        "total_kv_heads": len(head_deltas),
        "results": results,
        "top_heads": [{"key": h["key"], "delta_2bit": round(h["delta_2bit"], 6)} for h in head_deltas[:10]],
        "timing_seconds": round(total_time, 1),
    }
    with open(output_json, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nJSON saved to {output_json}")

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    os.makedirs("figures", exist_ok=True)

    ns = [r["n"] for r in results]
    ratios = [r["super_additive_ratio"] for r in results]
    joint_ppls = [r["joint_ppl"] for r in results]
    predicted_ppls = [r["predicted_ppl"] for r in results]

    fig, ax1 = plt.subplots(figsize=(7, 4.5))

    color1 = "#d62728"
    ax1.set_xlabel("Number of heads quantized to 2-bit ($n$)", fontsize=12)
    ax1.set_ylabel("Super-additive ratio", fontsize=12, color=color1)
    ax1.plot(ns, ratios, "o-", color=color1, linewidth=2, markersize=7, label="Super-additive ratio")
    ax1.axhline(y=1.0, color="gray", linestyle="--", alpha=0.5, label="Additive (ratio=1)")
    ax1.tick_params(axis="y", labelcolor=color1)
    ax1.set_xscale("log", base=2)
    ax1.set_xticks(ns)
    ax1.set_xticklabels([str(x) for x in ns])

    ax2 = ax1.twinx()
    color2 = "#1f77b4"
    color3 = "#2ca02c"
    ax2.set_ylabel("Perplexity", fontsize=12, color=color2)
    ax2.plot(ns, joint_ppls, "s-", color=color2, linewidth=2, markersize=6, label="Joint PPL (measured)")
    ax2.plot(ns, predicted_ppls, "^--", color=color3, linewidth=1.5, markersize=6, label="Predicted PPL (additive)")
    ax2.tick_params(axis="y", labelcolor=color2)

    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left", fontsize=9)

    plt.title("Compounding Effect of Per-Head KV Cache Quantization\n(Qwen2.5-7B)", fontsize=11)
    fig.tight_layout()
    fig.savefig(output_pdf, bbox_inches="tight")
    fig.savefig(output_png, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Plot saved to {output_pdf} and {output_png}")

    print(f"\n{'='*60}")
    print("COMPOUNDING SCALING RESULTS — Qwen2.5-7B")
    print(f"{'='*60}")
    print(f"{'n':>4}  {'sum_indiv':>10}  {'joint_ppl':>10}  {'pred_ppl':>10}  {'ratio':>8}")
    print("-" * 60)
    for r in results:
        print(f"{r['n']:>4}  {r['sum_individual_delta']:>10.4f}  {r['joint_ppl']:>10.4f}  {r['predicted_ppl']:>10.4f}  {r['super_additive_ratio']:>8.4f}")
    print(f"\nTotal time: {total_time/60:.1f}min")


if __name__ == "__main__":
    main()
