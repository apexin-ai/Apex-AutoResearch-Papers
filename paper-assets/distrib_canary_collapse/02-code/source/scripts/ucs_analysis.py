#!/usr/bin/env python3
"""
Universal Cascade Signature (UCS) Analysis

Tests whether the Entropy→Diversity→Calibration cascade ordering
observed in synthetic-data collapse extends to other domains:

Domain 1 (RLHF): OLMo-2-0425-1B alignment pipeline (Base→SFT→DPO→RLVR)
Domain 2 (Continual Learning): Pythia-70m pre-training checkpoints

For each domain, loads model checkpoints sequentially, evaluates on a
fixed held-out text, and computes 4 cascade metrics:
  - token_entropy: mean per-token entropy from logits
  - distinct_n: unigram/bigram/trigram diversity of generated text
  - ece: Expected Calibration Error
  - perplexity: exp(cross-entropy loss)

Onset ordering is determined by 2σ deviation from baseline (step 0 / base model).
"""

import argparse
import gc
import json
import os
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

HF_CACHE = os.environ.get("HF_HOME", "/root/autodl-tmp/.hf_cache")
os.environ["HF_HOME"] = HF_CACHE

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# --- Pythia-70m checkpoint steps (log-spaced early, linear late) ---
PYTHIA_STEPS = [
    "step0", "step1", "step2", "step4", "step8", "step16", "step32",
    "step64", "step128", "step256", "step512",
    "step1000", "step3000", "step6000", "step10000", "step20000",
    "step40000", "step70000", "step100000", "step143000",
]

# --- OLMo-2 alignment pipeline ---
OLMO_STAGES = [
    ("base", "allenai/OLMo-2-0425-1B"),
    ("sft", "allenai/OLMo-2-0425-1B-SFT"),
    ("dpo", "allenai/OLMo-2-0425-1B-DPO"),
    ("rlvr", "allenai/OLMo-2-0425-1B-RLVR1"),
]

# Fixed prompts for text generation (diversity measurement)
GEN_PROMPTS = [
    "The meaning of life is",
    "In the beginning, there was",
    "Scientists have discovered that",
    "The president announced today",
    "According to recent studies,",
    "The future of artificial intelligence",
    "Once upon a time in a land",
    "Breaking news: researchers found",
    "The economy is expected to",
    "In a surprising turn of events,",
    "The research team concluded that",
    "New evidence suggests that",
    "Experts warn that the current",
    "A new study published in",
    "The committee recommended that",
    "Historical records indicate that",
    "The experiment demonstrated that",
    "Climate scientists predict that",
    "The technology allows users to",
    "Researchers at the university found",
]

# Fixed eval texts for entropy/ECE/perplexity
EVAL_TEXTS = [
    "The tower is 324 metres tall, about the same height as an 81-storey building, "
    "and the tallest structure in Paris. Its base is square, measuring 125 metres on each side.",
    "Machine learning is a subset of artificial intelligence that provides systems the ability "
    "to automatically learn and improve from experience without being explicitly programmed.",
    "The Amazon rainforest produces more than 20 percent of the world's oxygen supply. "
    "The Amazon River pushes so much water into the Atlantic Ocean that the salinity is reduced.",
    "In quantum computing, a qubit is a quantum bit, the basic unit of quantum information. "
    "Unlike classical bits which can only be 0 or 1, qubits can exist in superposition.",
    "The human brain contains approximately 86 billion neurons, each connected to thousands "
    "of other neurons through synapses, forming an incredibly complex neural network.",
]


def compute_metrics_on_text(model, tokenizer, texts, device):
    """Compute token_entropy, ECE, and perplexity on fixed eval texts."""
    all_entropies = []
    all_confidences = []
    all_correct = []
    total_loss = 0.0
    total_tokens = 0

    for text in texts:
        inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
        inputs = {k: v.to(device) for k, v in inputs.items()}

        with torch.no_grad():
            outputs = model(**inputs, labels=inputs["input_ids"])

        logits = outputs.logits[:, :-1, :]
        labels = inputs["input_ids"][:, 1:]
        n_tokens = labels.numel()

        # Token entropy
        log_probs = torch.log_softmax(logits, dim=-1)
        probs = torch.exp(log_probs)
        entropy = -(probs * log_probs).sum(dim=-1)
        all_entropies.extend(entropy.squeeze().cpu().tolist())

        # Confidence and accuracy (for ECE)
        max_probs, preds = probs.max(dim=-1)
        correct = (preds == labels).float()
        all_confidences.extend(max_probs.squeeze().cpu().tolist())
        all_correct.extend(correct.squeeze().cpu().tolist())

        # Loss
        total_loss += outputs.loss.item() * n_tokens
        total_tokens += n_tokens

    # Aggregate
    mean_entropy = float(np.mean(all_entropies))
    mean_ppl = float(np.exp(total_loss / total_tokens)) if total_tokens > 0 else float("inf")

    # ECE (10 bins)
    confs = np.array(all_confidences)
    accs = np.array(all_correct)
    ece = 0.0
    n_bins = 10
    bin_edges = np.linspace(0, 1, n_bins + 1)
    for i in range(n_bins):
        mask = (confs > bin_edges[i]) & (confs <= bin_edges[i + 1])
        if mask.sum() > 0:
            bin_conf = confs[mask].mean()
            bin_acc = accs[mask].mean()
            ece += mask.sum() / len(confs) * abs(bin_conf - bin_acc)
    ece = float(ece)

    return {"token_entropy": mean_entropy, "ece": ece, "perplexity": mean_ppl}


def generate_texts(model, tokenizer, prompts, device, max_new_tokens=80, n_per_prompt=3):
    """Generate text samples from fixed prompts."""
    generated = []
    for prompt in prompts:
        inputs = tokenizer(prompt, return_tensors="pt")
        inputs = {k: v.to(device) for k, v in inputs.items()}

        for _ in range(n_per_prompt):
            with torch.no_grad():
                out = model.generate(
                    **inputs,
                    max_new_tokens=max_new_tokens,
                    do_sample=True,
                    temperature=0.8,
                    top_p=0.95,
                    pad_token_id=tokenizer.eos_token_id,
                )
            text = tokenizer.decode(out[0], skip_special_tokens=True)
            generated.append(text)
    return generated


def compute_distinct_n(texts, n):
    """Compute distinct-n ratio across generated texts."""
    all_ngrams = []
    for text in texts:
        tokens = text.split()
        ngrams = [tuple(tokens[i : i + n]) for i in range(len(tokens) - n + 1)]
        all_ngrams.extend(ngrams)
    if len(all_ngrams) == 0:
        return 0.0
    return len(set(all_ngrams)) / len(all_ngrams)


def process_checkpoint(model_name, revision=None, label="", device=DEVICE):
    """Load a checkpoint, compute all metrics, free memory."""
    t0 = time.time()
    print(f"  Loading {label} ({model_name}, rev={revision})...", flush=True)

    kwargs = {"trust_remote_code": True, "torch_dtype": torch.float16}
    if revision:
        kwargs["revision"] = revision

    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True,
                                               revision=revision if revision else None)
    model = AutoModelForCausalLM.from_pretrained(model_name, **kwargs)
    model = model.to(device).eval()

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # Eval metrics
    eval_metrics = compute_metrics_on_text(model, tokenizer, EVAL_TEXTS, device)

    # Generation for diversity
    texts = generate_texts(model, tokenizer, GEN_PROMPTS, device, max_new_tokens=80, n_per_prompt=3)
    eval_metrics["distinct_1"] = compute_distinct_n(texts, 1)
    eval_metrics["distinct_2"] = compute_distinct_n(texts, 2)
    eval_metrics["distinct_3"] = compute_distinct_n(texts, 3)
    eval_metrics["n_generated"] = len(texts)

    # Cleanup
    del model, tokenizer
    gc.collect()
    torch.cuda.empty_cache()

    elapsed = time.time() - t0
    print(f"    Done in {elapsed:.1f}s: entropy={eval_metrics['token_entropy']:.4f}, "
          f"ppl={eval_metrics['perplexity']:.2f}, ece={eval_metrics['ece']:.4f}, "
          f"d1={eval_metrics['distinct_1']:.4f}", flush=True)

    return eval_metrics


def compute_onset(series, baseline_val, direction, threshold_sigma=2.0):
    """Find first index where metric deviates beyond 2σ from baseline noise."""
    if len(series) < 3:
        return None, None

    early = np.array(series[:3])
    early_std = np.std(early)
    if early_std < 1e-10:
        early_std = abs(baseline_val) * 0.01 if abs(baseline_val) > 1e-10 else 1e-10

    sign = -1.0 if direction == "decrease" else 1.0
    for i in range(1, len(series)):
        deviation = sign * (series[i] - baseline_val)
        z = deviation / early_std
        if z >= threshold_sigma:
            return i, float(z)
    return None, None


def analyze_cascade(results, labels, domain_name):
    """Determine cascade ordering from per-checkpoint metrics."""
    metrics_config = {
        "token_entropy": "decrease",
        "distinct_1": "decrease",
        "distinct_2": "decrease",
        "distinct_3": "decrease",
        "ece": "increase",
        "perplexity": "increase",
    }

    onset_table = {}
    for metric, direction in metrics_config.items():
        series = [r[metric] for r in results]
        baseline = series[0]

        # For pretraining (Pythia), metrics IMPROVE: entropy decreases, ppl decreases.
        # We still detect "first significant change from baseline" regardless of direction.
        # Use absolute deviation instead of directional for pretraining dynamics.
        if domain_name == "pythia_pretraining":
            abs_series = [abs(v - baseline) for v in series]
            early_std = np.std(abs_series[:3]) if len(abs_series) >= 3 else 1e-10
            if early_std < 1e-10:
                early_std = abs(baseline) * 0.01 if abs(baseline) > 1e-10 else 1e-10
            onset_idx = None
            onset_z = None
            for i in range(1, len(abs_series)):
                z = abs_series[i] / early_std
                if z >= 2.0:
                    onset_idx = i
                    onset_z = float(z)
                    break
        else:
            onset_idx, onset_z = compute_onset(series, baseline, direction)

        onset_table[metric] = {
            "onset_idx": onset_idx,
            "onset_label": labels[onset_idx] if onset_idx is not None else None,
            "z_score": onset_z,
            "baseline": baseline,
            "final": series[-1],
            "pct_change": (series[-1] - baseline) / abs(baseline) * 100 if abs(baseline) > 1e-10 else None,
        }

    detected = {k: v for k, v in onset_table.items() if v["onset_idx"] is not None}
    cascade_order = sorted(
        detected.keys(),
        key=lambda k: (detected[k]["onset_idx"], -(detected[k]["z_score"] or 0)),
    )

    # Kendall tau with hypothesized ordering
    hypothesis = ["token_entropy", "ece", "distinct_1", "perplexity"]
    observed_ranks = {}
    for rank, m in enumerate(cascade_order):
        observed_ranks[m] = rank

    common = [m for m in hypothesis if m in observed_ranks]
    if len(common) >= 2:
        from scipy.stats import kendalltau
        hyp_ranks = [hypothesis.index(m) for m in common]
        obs_ranks = [observed_ranks[m] for m in common]
        tau, p_value = kendalltau(hyp_ranks, obs_ranks)
    else:
        tau, p_value = None, None

    return {
        "domain": domain_name,
        "n_checkpoints": len(results),
        "labels": labels,
        "onset_table": onset_table,
        "cascade_order": cascade_order,
        "kendall_tau": tau,
        "kendall_p": p_value,
        "metrics_per_checkpoint": [
            {"label": labels[i], **results[i]} for i in range(len(results))
        ],
    }


def run_pythia(output_dir):
    """Domain 2: Pythia-70m pre-training checkpoints."""
    print("\n=== Domain 2: Pythia-70m Pre-training Dynamics ===\n", flush=True)
    model_name = "EleutherAI/pythia-70m"

    results = []
    labels = []
    checkpoint_file = Path(output_dir) / "pythia_checkpoints_raw.json"

    # Resume from partial results
    existing = {}
    if checkpoint_file.exists():
        with open(checkpoint_file) as f:
            existing = {r["label"]: r for r in json.load(f)}
        print(f"  Resuming: {len(existing)} checkpoints already computed", flush=True)

    for step in PYTHIA_STEPS:
        if step in existing:
            results.append(existing[step])
            labels.append(step)
            print(f"  [cached] {step}", flush=True)
            continue

        metrics = process_checkpoint(model_name, revision=step, label=step)
        metrics["label"] = step
        results.append(metrics)
        labels.append(step)

        # Save incrementally
        with open(checkpoint_file, "w") as f:
            json.dump(results, f, indent=2)

    analysis = analyze_cascade(results, labels, "pythia_pretraining")

    out_path = Path(output_dir) / "continual_cascade.json"
    with open(out_path, "w") as f:
        json.dump(analysis, f, indent=2)
    print(f"\nSaved: {out_path}", flush=True)
    return analysis


def run_olmo_rlhf(output_dir):
    """Domain 1: OLMo-2-0425-1B alignment pipeline."""
    print("\n=== Domain 1: OLMo-2-1B RLHF Pipeline ===\n", flush=True)

    results = []
    labels = []
    checkpoint_file = Path(output_dir) / "olmo_checkpoints_raw.json"

    existing = {}
    if checkpoint_file.exists():
        with open(checkpoint_file) as f:
            existing = {r["label"]: r for r in json.load(f)}
        print(f"  Resuming: {len(existing)} checkpoints already computed", flush=True)

    for stage_name, model_id in OLMO_STAGES:
        if stage_name in existing:
            results.append(existing[stage_name])
            labels.append(stage_name)
            print(f"  [cached] {stage_name}", flush=True)
            continue

        metrics = process_checkpoint(model_id, label=stage_name)
        metrics["label"] = stage_name
        results.append(metrics)
        labels.append(stage_name)

        with open(checkpoint_file, "w") as f:
            json.dump(results, f, indent=2)

    analysis = analyze_cascade(results, labels, "olmo_rlhf")

    out_path = Path(output_dir) / "rlhf_cascade.json"
    with open(out_path, "w") as f:
        json.dump(analysis, f, indent=2)
    print(f"\nSaved: {out_path}", flush=True)
    return analysis


def generate_comparison_report(pythia_analysis, olmo_analysis, output_dir):
    """Generate cross-domain comparison report."""
    lines = [
        "# Universal Cascade Signature (UCS) — Cross-Domain Comparison",
        "",
        "## Hypothesis",
        "The Entropy→Diversity→Calibration cascade observed in synthetic-data collapse",
        "extends to other domains where model distributions shift.",
        "",
        "Hypothesized ordering: token_entropy → ece → distinct_n → perplexity",
        "",
    ]

    for analysis in [olmo_analysis, pythia_analysis]:
        if analysis is None:
            continue
        domain = analysis["domain"]
        lines.append(f"## Domain: {domain}")
        lines.append(f"Checkpoints: {analysis['n_checkpoints']}")
        lines.append("")

        lines.append("### Onset Table")
        lines.append("| Metric | Onset Index | Onset Label | z-score | Baseline | Final | % Change |")
        lines.append("|--------|-------------|-------------|---------|----------|-------|----------|")
        for m in ["token_entropy", "ece", "distinct_1", "distinct_2", "distinct_3", "perplexity"]:
            info = analysis["onset_table"].get(m, {})
            onset_idx = info.get("onset_idx", "-")
            onset_label = info.get("onset_label", "-")
            z = f"{info['z_score']:.2f}" if info.get("z_score") else "-"
            base = f"{info['baseline']:.4f}" if info.get("baseline") is not None else "-"
            final = f"{info['final']:.4f}" if info.get("final") is not None else "-"
            pct = f"{info['pct_change']:.1f}%" if info.get("pct_change") is not None else "-"
            lines.append(f"| {m} | {onset_idx} | {onset_label} | {z} | {base} | {final} | {pct} |")
        lines.append("")

        lines.append(f"### Cascade Order: {' → '.join(analysis['cascade_order'])}")
        if analysis.get("kendall_tau") is not None:
            lines.append(f"Kendall τ vs hypothesis: {analysis['kendall_tau']:.3f} (p={analysis['kendall_p']:.3f})")
        lines.append("")

    # Cross-domain comparison
    lines.append("## Cross-Domain Summary")
    lines.append("")

    domains_with_data = [a for a in [olmo_analysis, pythia_analysis] if a is not None]
    n_match = 0
    for a in domains_with_data:
        order = a["cascade_order"]
        if len(order) >= 2 and order[0] == "token_entropy":
            n_match += 1

    lines.append(f"Domains tested: {len(domains_with_data)}")
    lines.append(f"Domains with entropy-first onset: {n_match}/{len(domains_with_data)}")
    lines.append("")

    if n_match >= 1:
        lines.append("**Conclusion**: Cascade extends beyond synthetic-data collapse.")
    else:
        lines.append("**Conclusion**: Cascade appears specific to synthetic-data collapse (honest negative).")

    report = "\n".join(lines)
    out_path = Path(output_dir) / "ucs_comparison.md"
    with open(out_path, "w") as f:
        f.write(report)
    print(f"\nReport saved: {out_path}", flush=True)
    return report


def main():
    parser = argparse.ArgumentParser(description="Universal Cascade Signature Analysis")
    parser.add_argument("--domain", choices=["pythia", "olmo", "both"], default="both")
    parser.add_argument("--output_dir", default="/root/autodl-tmp/distrib_canary_collapse/artifacts/universal_cascade")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    pythia_result = None
    olmo_result = None

    if args.domain in ("pythia", "both"):
        pythia_result = run_pythia(args.output_dir)

    if args.domain in ("olmo", "both"):
        olmo_result = run_olmo_rlhf(args.output_dir)

    generate_comparison_report(pythia_result, olmo_result, args.output_dir)
    print("\n=== UCS Analysis Complete ===", flush=True)


if __name__ == "__main__":
    main()
