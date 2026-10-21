#!/usr/bin/env python3
"""Compute unified (degen%, LP_delta) for all experiments at N=8."""
import json
import sys
import os
sys.path.insert(0, "/root/autodl-tmp/struct_self_consist_ie/code")
from unified_metrics import compute_entity_f1, compute_degeneracy

BASE = "/root/autodl-tmp/struct_self_consist_ie/output"

EXPERIMENTS = [
    # Cross-dataset canonical (Qwen3-8B, T=1.0, seed=42)
    {"dir": "exp_012_rerun_1024", "label": "SciERC", "category": "cross-dataset", "model": "Qwen3-8B", "dataset": "SciERC", "T": 1.0, "seed": 42},
    {"dir": "exp_002_conll_n16_r1024", "label": "CoNLL", "category": "cross-dataset", "model": "Qwen3-8B", "dataset": "CoNLL", "T": 1.0, "seed": 42},
    {"dir": "exp_027_fewnerd_n16", "label": "FewNERD", "category": "cross-dataset", "model": "Qwen3-8B", "dataset": "FewNERD", "T": 1.0, "seed": 42},
    # Multi-seed Qwen SciERC
    {"dir": "exp_018_qwen_scierc_seed123", "label": "SciERC s123", "category": "multi-seed", "model": "Qwen3-8B", "dataset": "SciERC", "T": 1.0, "seed": 123},
    {"dir": "exp_018_qwen_scierc_seed456", "label": "SciERC s456", "category": "multi-seed", "model": "Qwen3-8B", "dataset": "SciERC", "T": 1.0, "seed": 456},
    # Multi-seed Qwen CoNLL N=8
    {"dir": "exp_002_conll_n8_seed123", "label": "CoNLL s123", "category": "multi-seed", "model": "Qwen3-8B", "dataset": "CoNLL", "T": 1.0, "seed": 123},
    {"dir": "exp_002_conll_n8_seed456", "label": "CoNLL s456", "category": "multi-seed", "model": "Qwen3-8B", "dataset": "CoNLL", "T": 1.0, "seed": 456},
    # Multi-seed Qwen FewNERD (full test set)
    {"dir": "exp_021_fewnerd_n8_seed123", "label": "FewNERD s123", "category": "multi-seed", "model": "Qwen3-8B", "dataset": "FewNERD", "T": 1.0, "seed": 123},
    {"dir": "exp_021_fewnerd_n8_seed456", "label": "FewNERD s456", "category": "multi-seed", "model": "Qwen3-8B", "dataset": "FewNERD", "T": 1.0, "seed": 456},
    # LLaMA SciERC
    {"dir": "exp_018_llama_scierc_seed42_r1024", "label": "LLaMA SciERC s42", "category": "LLaMA3.1-8B", "model": "LLaMA3.1-8B", "dataset": "SciERC", "T": 1.0, "seed": 42},
    {"dir": "exp_018_llama_scierc_seed123", "label": "LLaMA SciERC s123", "category": "LLaMA3.1-8B", "model": "LLaMA3.1-8B", "dataset": "SciERC", "T": 1.0, "seed": 123},
    {"dir": "exp_018_llama_scierc_seed456_r1024", "label": "LLaMA SciERC s456", "category": "LLaMA3.1-8B", "model": "LLaMA3.1-8B", "dataset": "SciERC", "T": 1.0, "seed": 456},
    # LLaMA CoNLL (N=16, use first 8)
    {"dir": "exp_017_llama_conll_n16_r1024", "label": "LLaMA CoNLL s42", "category": "LLaMA3.1-8B", "model": "LLaMA3.1-8B", "dataset": "CoNLL", "T": 1.0, "seed": 42},
    {"dir": "exp_017_llama_conll_n16_s123_r1024", "label": "LLaMA CoNLL s123", "category": "LLaMA3.1-8B", "model": "LLaMA3.1-8B", "dataset": "CoNLL", "T": 1.0, "seed": 123},
    {"dir": "exp_017_llama_conll_n16_s456_r1024", "label": "LLaMA CoNLL s456", "category": "LLaMA3.1-8B", "model": "LLaMA3.1-8B", "dataset": "CoNLL", "T": 1.0, "seed": 456},
    # Epoch ablation (Qwen3-8B SciERC)
    {"dir": "exp_029a_scierc_3epoch", "label": "3-epoch", "category": "epoch", "model": "Qwen3-8B", "dataset": "SciERC", "T": 1.0, "seed": 42, "note": "3ep"},
    {"dir": "exp_029b_scierc_10epoch", "label": "10-epoch", "category": "epoch", "model": "Qwen3-8B", "dataset": "SciERC", "T": 1.0, "seed": 42, "note": "10ep"},
    # Rank ablation
    {"dir": "exp_023_rank8_inference", "label": "rank=8", "category": "rank", "model": "Qwen3-8B", "dataset": "SciERC", "T": 1.0, "seed": 42, "note": "rank8"},
    # Temperature ablation (Qwen3-8B SciERC seed=42)
    {"dir": "exp_026_t05", "label": "T=0.5", "category": "temperature", "model": "Qwen3-8B", "dataset": "SciERC", "T": 0.5, "seed": 42},
    {"dir": "exp_026_t08", "label": "T=0.8", "category": "temperature", "model": "Qwen3-8B", "dataset": "SciERC", "T": 0.8, "seed": 42},
    {"dir": "exp_026_t12", "label": "T=1.2", "category": "temperature", "model": "Qwen3-8B", "dataset": "SciERC", "T": 1.2, "seed": 42},
    # Scale ablation (Qwen3-4B)
    {"dir": "exp_qwen3_4b_scierc_scs_inference", "label": "4B SciERC", "category": "Qwen3-4B", "model": "Qwen3-4B", "dataset": "SciERC", "T": 1.0, "seed": 42},
    {"dir": "exp_qwen3_4b_conll_scs_inference_v2", "label": "4B CoNLL", "category": "Qwen3-4B", "model": "Qwen3-4B", "dataset": "CoNLL", "T": 1.0, "seed": 42},
]

def analyze(path, n_samples=8):
    """Return (degen_pct, greedy_f1, lp_f1, lp_delta_pp, n_used, n_degen)."""
    greedy_f1s = []
    lp_f1s = []
    n_degen = 0
    n_used = 0
    
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            inst = json.loads(line)
            gold_ents = inst["gold"].get("entities", [])
            if not gold_ents:
                continue
            
            samples = inst["samples"][:n_samples]
            if len(samples) < n_samples:
                continue
            
            greedy = inst.get("greedy", samples[0])
            
            sample_f1s = [compute_entity_f1(s.get("entities", []), gold_ents) for s in samples]
            g_f1 = compute_entity_f1(greedy.get("entities", []), gold_ents)
            
            lp_idx = max(range(len(samples)), key=lambda i: samples[i].get("mean_logprob", 0))
            lp_f1 = sample_f1s[lp_idx]
            
            is_degen = compute_degeneracy(sample_f1s)
            if is_degen:
                n_degen += 1
            
            greedy_f1s.append(g_f1)
            lp_f1s.append(lp_f1)
            n_used += 1
    
    if n_used == 0:
        return None
    
    degen_pct = n_degen / n_used * 100
    mean_greedy = sum(greedy_f1s) / len(greedy_f1s)
    mean_lp = sum(lp_f1s) / len(lp_f1s)
    lp_delta_pp = (mean_lp - mean_greedy) * 100
    
    return {
        "degen_pct": round(degen_pct, 2),
        "greedy_f1": round(mean_greedy, 4),
        "lp_f1": round(mean_lp, 4),
        "lp_delta_pp": round(lp_delta_pp, 2),
        "n_used": n_used,
        "n_degen": n_degen,
    }

results = []
for exp in EXPERIMENTS:
    path = os.path.join(BASE, exp["dir"], "samples.jsonl")
    if not os.path.exists(path):
        print(f"SKIP: {exp['dir']} - no samples.jsonl", file=sys.stderr)
        continue
    
    metrics = analyze(path, n_samples=8)
    if metrics is None:
        print(f"SKIP: {exp['dir']} - no valid instances", file=sys.stderr)
        continue
    
    entry = {**exp, **metrics}
    del entry["dir"]
    results.append(entry)
    print(f"{exp['label']:25s}  degen={metrics['degen_pct']:5.1f}%  LP_delta={metrics['lp_delta_pp']:+.2f}pp  (n={metrics['n_used']}, greedy={metrics['greedy_f1']:.4f}, lp={metrics['lp_f1']:.4f})")

out_path = os.path.join(BASE, "scatter_v2_data.json")
with open(out_path, "w") as f:
    json.dump(results, f, indent=2)
print(f"\nSaved {len(results)} data points to {out_path}")
