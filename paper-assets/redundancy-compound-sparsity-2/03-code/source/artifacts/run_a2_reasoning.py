"""
A2 Experiment: Attention vs EMA correlation on reasoning traces.
Compares attention-based KV importance with EMA anchor scores per layer.
"""
import argparse
import gc
import json
import os
import sys
import time
from typing import Dict, List

import numpy as np
import torch
from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer

sys.path.insert(0, '/root/carc')
from carc_utils import EMAAnchorManager
from d003_reasoning_traces import KVCapture, get_math_prompts


def compute_correlation(x: np.ndarray, y: np.ndarray):
    try:
        from scipy.stats import pearsonr, spearmanr
        pr, pp = pearsonr(x, y)
        sr, sp = spearmanr(x, y)
        return float(pr), float(pp), float(sr), float(sp)
    except ImportError:
        pr = float(np.corrcoef(x, y)[0, 1])
        rx = np.argsort(np.argsort(x)).astype(float)
        ry = np.argsort(np.argsort(y)).astype(float)
        sr = float(np.corrcoef(rx, ry)[0, 1])
        return pr, 0.0, sr, 0.0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--gpu', type=int, default=0)
    parser.add_argument('--seq-len', type=int, default=4096)
    parser.add_argument('--chunk-size', type=int, default=512)
    parser.add_argument('--num-problems', type=int, default=60)
    parser.add_argument('--model', default='/root/autodl-tmp/carc/models/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B')
    parser.add_argument('--output', default='/root/carc/results/a2_reasoning_traces.json')
    parser.add_argument('--figure-dir', default='/root/carc/figures')
    args = parser.parse_args()

    device = torch.device(f'cuda:{args.gpu}')
    t_start = time.time()

    print(f"Loading model: {args.model}")
    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        torch_dtype=torch.bfloat16,
        device_map={"": device},
        trust_remote_code=True,
        attn_implementation="eager",
    )
    model.eval()
    num_layers = len(model.model.layers)
    num_kv_heads = model.config.num_key_value_heads
    print(f"Model: {num_layers} layers, {num_kv_heads} KV heads, device={device}")

    print("Preparing reasoning traces...")
    prompts = get_math_prompts(num_problems=args.num_problems, seed=42)
    full_text = "\n\n".join(prompts)
    tokens = tokenizer.encode(full_text, add_special_tokens=True)
    seq_len = min(args.seq_len, len(tokens))
    input_ids = torch.tensor([tokens[:seq_len]], dtype=torch.long, device=device)
    print(f"Tokenized: {len(tokens)} total, using {seq_len}")

    kv_capture = KVCapture(model, num_layers)
    ema_manager = EMAAnchorManager(gamma=0.9, num_kv_heads=num_kv_heads, per_head=True)

    ema_scores_all: Dict[int, List[torch.Tensor]] = {l: [] for l in range(num_layers)}
    # Accumulated attention importance (sum of attention mass received from all subsequent queries)
    attn_accum: Dict[int, torch.Tensor] = {
        l: torch.zeros(seq_len, dtype=torch.float64) for l in range(num_layers)
    }
    # Last chunk attention importance (single snapshot)
    attn_last: Dict[int, np.ndarray] = {}

    chunk_size = args.chunk_size
    num_chunks = (seq_len + chunk_size - 1) // chunk_size
    past_kv = None

    print(f"Running {num_chunks} chunks (chunk_size={chunk_size})...")
    for ci in tqdm(range(num_chunks), desc="Chunks"):
        start = ci * chunk_size
        end = min(start + chunk_size, seq_len)
        chunk_ids = input_ids[:, start:end]
        pos_ids = torch.arange(start, end, device=device).unsqueeze(0)

        kv_capture.clear()

        with torch.no_grad():
            outputs = model(
                chunk_ids,
                position_ids=pos_ids,
                past_key_values=past_kv,
                use_cache=True,
                output_attentions=True,
            )

        past_kv = outputs.past_key_values

        # EMA scores for new positions
        for li in range(num_layers):
            if li in kv_capture.kv and kv_capture.kv[li][0] is not None:
                scores = ema_manager.compute_scores(
                    li, kv_capture.kv[li][0], kv_capture.kv[li][1]
                )
                ema_scores_all[li].append(scores[0].cpu().float())

        # Attention importance
        if outputs.attentions is not None:
            is_last = (ci == num_chunks - 1)
            for li in range(num_layers):
                attn_w = outputs.attentions[li]  # (1, heads, chunk_len, kv_len)
                # Sum over heads and queries → (kv_len,)
                imp = attn_w[0].float().sum(dim=0).sum(dim=0)
                kv_len = imp.shape[0]
                attn_accum[li][:kv_len] += imp.cpu().double()

                if is_last:
                    # Last chunk: avg over heads and queries for unbiased snapshot
                    avg_imp = attn_w[0].float().mean(dim=0).mean(dim=0)  # (kv_len,)
                    attn_last[li] = avg_imp.cpu().numpy().astype(np.float64)

        if ci == 0 and outputs.attentions is not None:
            attn_w0 = outputs.attentions[0]
            print(f"  Attention shape check: {attn_w0.shape}")

        del outputs
        kv_capture.clear()
        gc.collect()
        torch.cuda.empty_cache()

    kv_capture.remove()
    del past_kv, model
    gc.collect()
    torch.cuda.empty_cache()

    # Compute correlations
    print("\nComputing correlations...")
    # Skip first chunk positions to avoid EMA initialization artifacts
    skip = chunk_size
    layer_results = []

    for li in range(num_layers):
        if not ema_scores_all[li]:
            layer_results.append({
                'layer': li,
                'pearson_last': 0.0, 'spearman_last': 0.0,
                'pearson_accum': 0.0, 'spearman_accum': 0.0,
            })
            continue

        ema_vec = torch.cat(ema_scores_all[li]).numpy().astype(np.float64)
        n = len(ema_vec)

        # Method 1: Last chunk attention
        last_vec = attn_last.get(li, np.zeros(n))
        last_vec = last_vec[:n]
        # Pad if needed
        if len(last_vec) < n:
            last_vec = np.pad(last_vec, (0, n - len(last_vec)))

        # Method 2: Accumulated attention
        accum_vec = attn_accum[li].numpy()[:n]

        # Slice to skip initialization
        e = ema_vec[skip:]
        l1 = last_vec[skip:]
        a1 = accum_vec[skip:]

        r = {'layer': li}
        if len(e) > 10 and np.std(e) > 1e-10:
            if np.std(l1) > 1e-10:
                pr, pp, sr, sp = compute_correlation(e, l1)
                r['pearson_last'] = round(pr, 6)
                r['spearman_last'] = round(sr, 6)
                r['pearson_last_p'] = round(pp, 6)
                r['spearman_last_p'] = round(sp, 6)
            else:
                r['pearson_last'] = 0.0
                r['spearman_last'] = 0.0

            if np.std(a1) > 1e-10:
                pr, pp, sr, sp = compute_correlation(e, a1)
                r['pearson_accum'] = round(pr, 6)
                r['spearman_accum'] = round(sr, 6)
                r['pearson_accum_p'] = round(pp, 6)
                r['spearman_accum_p'] = round(sp, 6)
            else:
                r['pearson_accum'] = 0.0
                r['spearman_accum'] = 0.0
        else:
            r['pearson_last'] = 0.0
            r['spearman_last'] = 0.0
            r['pearson_accum'] = 0.0
            r['spearman_accum'] = 0.0

        layer_results.append(r)

    # Summary
    sp_last = [r['spearman_last'] for r in layer_results]
    sp_accum = [r['spearman_accum'] for r in layer_results]
    pr_last = [r['pearson_last'] for r in layer_results]
    pr_accum = [r['pearson_accum'] for r in layer_results]

    g_sp_last = float(np.mean(sp_last))
    g_sp_accum = float(np.mean(sp_accum))
    g_pr_last = float(np.mean(pr_last))
    g_pr_accum = float(np.mean(pr_accum))

    # Use last-chunk Spearman as primary verdict
    g_sp = g_sp_last
    if g_sp > 0.8:
        verdict = "redundant"
    elif g_sp > 0.5:
        verdict = "moderate"
    else:
        verdict = "complementary"

    elapsed = time.time() - t_start

    print(f"\n{'='*60}")
    print(f"A2: Attention vs EMA — Reasoning Traces")
    print(f"{'='*60}")
    print(f"[Last-chunk]  Pearson: {g_pr_last:.4f}  Spearman: {g_sp_last:.4f}")
    print(f"[Accumulated] Pearson: {g_pr_accum:.4f}  Spearman: {g_sp_accum:.4f}")
    print(f"Verdict (last-chunk ρ): {verdict}")
    print(f"Time: {elapsed:.0f}s")

    sorted_r = sorted(layer_results, key=lambda x: abs(x['spearman_last']), reverse=True)
    print(f"\nTop 5 layers (|Spearman_last|):")
    for r in sorted_r[:5]:
        print(f"  Layer {r['layer']:2d}: ρ_last={r['spearman_last']:.4f} ρ_accum={r['spearman_accum']:.4f}")
    print(f"Bottom 5:")
    for r in sorted_r[-5:]:
        print(f"  Layer {r['layer']:2d}: ρ_last={r['spearman_last']:.4f} ρ_accum={r['spearman_accum']:.4f}")

    # Save
    output = {
        'experiment': 'a2_attn_vs_ema_reasoning_traces',
        'config': {
            'model': args.model,
            'seq_len': seq_len,
            'chunk_size': chunk_size,
            'num_problems': args.num_problems,
            'ema_gamma': 0.9,
            'num_kv_heads': num_kv_heads,
            'num_layers': num_layers,
            'skip_init_tokens': skip,
        },
        'per_layer': layer_results,
        'summary': {
            'global_pearson_last': round(g_pr_last, 4),
            'global_spearman_last': round(g_sp_last, 4),
            'global_pearson_accum': round(g_pr_accum, 4),
            'global_spearman_accum': round(g_sp_accum, 4),
            'verdict': verdict,
            'elapsed_seconds': round(elapsed, 1),
        },
    }

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved: {args.output}")

    # Figures
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt

        os.makedirs(args.figure_dir, exist_ok=True)

        # 1) Bar chart: per-layer correlation
        fig, axes = plt.subplots(2, 2, figsize=(16, 10))

        for col, (label, sp_vals, pr_vals) in enumerate([
            ('Last-Chunk', sp_last, pr_last),
            ('Accumulated', sp_accum, pr_accum),
        ]):
            ax_p = axes[0, col]
            ax_s = axes[1, col]
            layers = list(range(num_layers))

            ax_p.bar(layers, pr_vals, color='steelblue', alpha=0.8)
            ax_p.set_ylabel('Pearson r')
            ax_p.set_title(f'{label} Attention: Pearson')
            ax_p.axhline(0.8, color='red', ls='--', lw=0.8, label='0.8')
            ax_p.axhline(0.5, color='orange', ls='--', lw=0.8, label='0.5')
            ax_p.axhline(0, color='gray', ls='--', lw=0.5)
            ax_p.legend(fontsize=7)

            ax_s.bar(layers, sp_vals, color='darkorange', alpha=0.8)
            ax_s.set_ylabel('Spearman ρ')
            ax_s.set_xlabel('Layer')
            ax_s.set_title(f'{label} Attention: Spearman')
            ax_s.axhline(0.8, color='red', ls='--', lw=0.8)
            ax_s.axhline(0.5, color='orange', ls='--', lw=0.8)
            ax_s.axhline(0, color='gray', ls='--', lw=0.5)

        plt.suptitle(f'A2: Attn vs EMA (Reasoning) — verdict={verdict}', fontsize=14)
        plt.tight_layout()
        p1 = os.path.join(args.figure_dir, 'a2_reasoning_correlation.png')
        plt.savefig(p1, dpi=150)
        plt.close()
        print(f"Figure: {p1}")

        # 2) Scatter for select layers (last-chunk attention)
        sample_layers = [0, 11, 23, 35, 43, 47]
        fig, axes_sc = plt.subplots(2, 3, figsize=(15, 10))
        for ax, sl in zip(axes_sc.flat, sample_layers):
            if sl >= num_layers:
                ax.set_visible(False)
                continue
            ev = torch.cat(ema_scores_all[sl]).numpy()
            lv = attn_last.get(sl, np.zeros(len(ev)))[:len(ev)]
            n = len(ev)
            idx = np.random.RandomState(42).choice(n, min(2000, n), replace=False)
            ax.scatter(ev[idx], lv[idx], alpha=0.3, s=5, c='steelblue')
            ax.set_title(f'Layer {sl} (ρ={layer_results[sl]["spearman_last"]:.3f})')
            ax.set_xlabel('EMA score')
            ax.set_ylabel('Attn importance (last chunk)')

        plt.suptitle('A2: EMA vs Last-Chunk Attention Scatter (Reasoning)', fontsize=14)
        plt.tight_layout()
        p2 = os.path.join(args.figure_dir, 'a2_reasoning_scatter.png')
        plt.savefig(p2, dpi=150)
        plt.close()
        print(f"Figure: {p2}")

    except Exception as e:
        print(f"Warning: viz failed: {e}")

    print("\nDone.")


if __name__ == '__main__':
    main()
