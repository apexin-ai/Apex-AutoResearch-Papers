#!/usr/bin/env python3
"""Verbalized Confidence baseline for structured self-consistency IE.

For each test instance's N=8 samples, asks the model to rate its own
extraction confidence on a 1-10 scale. Evaluates as a per-sample and
per-instance signal against gold F1.
"""

import json
import os
import re
import sys
import time

import numpy as np
from collections import Counter
from scipy.stats import spearmanr, rankdata

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import (
    _ner_soft_jaccard_pair,
    _re_soft_jaccard_pair,
    _extract_surface_keys,
)
from evaluation import per_instance_f1

BASE = "/root/autodl-tmp/struct_self_consist_ie"
OUTPUT_DIR = f"{BASE}/output/review_round9_experiments/verbalized_confidence"

EXPERIMENTS = {
    "scierc_ner": {
        "samples_path": f"{BASE}/output/exp_012_rerun_1024/samples.jsonl",
        "model_path": f"{BASE}/checkpoints/qwen3-8b-scierc-merged-v2",
        "subtask": "ner",
        "dataset": "scierc",
    },
    "conll_ner": {
        "samples_path": f"{BASE}/output/exp002_conll2003/samples.jsonl",
        "model_path": f"{BASE}/checkpoints/qwen3-8b-conll2003-merged",
        "subtask": "ner",
        "dataset": "conll2003",
    },
}

# ---------------------------------------------------------------------------
# Data I/O
# ---------------------------------------------------------------------------

def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


# ---------------------------------------------------------------------------
# Prompt construction
# ---------------------------------------------------------------------------

def format_extraction(sample, subtask):
    entities = sample.get("entities", [])
    if not entities:
        return "No entities found."
    lines = []
    for e in entities:
        lines.append(f'- "{e["text"]}" ({e["type"]})')
    return "Entities found:\n" + "\n".join(lines)


def build_prompts(instances, subtask):
    prompts = []
    index_map = []
    for i, inst in enumerate(instances):
        for j, sample in enumerate(inst["samples"]):
            extraction_str = format_extraction(sample, subtask)
            prompt = (
                "Given the following text and NER extraction result, "
                "rate your confidence in the correctness of this extraction "
                "on a scale of 1-10, where 1 means very likely incorrect and "
                "10 means very likely correct. Only output the number.\n\n"
                f"Text: {inst['text']}\n"
                f"Extraction:\n{extraction_str}\n"
                "Confidence:"
            )
            prompts.append(prompt)
            index_map.append((i, j))
    return prompts, index_map


# ---------------------------------------------------------------------------
# Score parsing
# ---------------------------------------------------------------------------

def parse_score(text):
    text = text.strip()
    m = re.search(r'(\d+(?:\.\d+)?)', text)
    if m:
        val = float(m.group(1))
        return min(max(val, 1.0), 10.0)
    return None


# ---------------------------------------------------------------------------
# Existing signal computation (per-sample level for selection F1)
# ---------------------------------------------------------------------------

def compute_sample_sj_scores(instance, subtask):
    samples = instance["samples"]
    N = len(samples)
    field = "entities" if subtask == "ner" else "relations"
    pair_fn = _ner_soft_jaccard_pair if subtask == "ner" else _re_soft_jaccard_pair
    matrix = np.zeros((N, N))
    for i in range(N):
        for j in range(i + 1, N):
            s = pair_fn(samples[i].get(field, []), samples[j].get(field, []))
            matrix[i][j] = s
            matrix[j][i] = s
    np.fill_diagonal(matrix, 1.0)
    return [float(np.mean([matrix[k][j] for j in range(N) if j != k])) for k in range(N)]


def compute_sample_surface_scores(instance, subtask):
    samples = instance["samples"]
    N = len(samples)
    key_sets = [frozenset(_extract_surface_keys(s, subtask)) for s in samples]
    matrix = np.zeros((N, N))
    for i in range(N):
        for j in range(i + 1, N):
            union = len(key_sets[i] | key_sets[j])
            inter = len(key_sets[i] & key_sets[j])
            s = inter / union if union > 0 else 1.0
            matrix[i][j] = s
            matrix[j][i] = s
    np.fill_diagonal(matrix, 1.0)
    fk_scores = [float(np.mean([matrix[k][j] for j in range(N) if j != k])) for k in range(N)]
    return fk_scores, key_sets


def compute_sample_voting_conf(key_sets, N):
    all_keys_count = Counter()
    for ks in key_sets:
        for k in ks:
            all_keys_count[k] += 1
    scores = []
    for ks in key_sets:
        if not ks:
            scores.append(0.0)
        else:
            fracs = [all_keys_count[key] / N for key in ks]
            scores.append(float(np.mean(fracs)))
    return scores


def compute_sample_em_scores(key_sets):
    N = len(key_sets)
    return [float(sum(1 for j in range(N) if j != k and key_sets[k] == key_sets[j])) for k in range(N)]


def compute_sample_logprobs(instance):
    lps = []
    for s in instance["samples"]:
        lp = s.get("mean_logprob")
        if lp is None:
            lp = s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1)
        lps.append(lp)
    return lps


# ---------------------------------------------------------------------------
# Per-instance signal computation (for rho / AUROC)
# ---------------------------------------------------------------------------

def compute_instance_mean_logprob(samples):
    lps = [s.get("mean_logprob") for s in samples if s.get("mean_logprob") is not None]
    lps = [lp for lp in lps if np.isfinite(lp)]
    return float(np.mean(lps)) if lps else float("nan")


def compute_instance_em_rate(samples, subtask):
    if subtask == "ner":
        keys = [frozenset((e["text"], e["type"]) for e in s.get("entities", [])) for s in samples]
    else:
        keys = [frozenset((r["head"], r["tail"], r["type"]) for r in s.get("relations", [])) for s in samples]
    if not keys:
        return 0.0
    c = Counter(keys)
    return c.most_common(1)[0][1] / len(samples)


def compute_instance_voting_conf(samples, subtask):
    N = len(samples)
    if N == 0:
        return 0.0
    counter = Counter()
    if subtask == "ner":
        for s in samples:
            for e in s.get("entities", []):
                counter[(e["text"], e["type"])] += 1
    else:
        for s in samples:
            for r in s.get("relations", []):
                counter[(r["head"], r["tail"], r["type"])] += 1
    if not counter:
        return 0.0
    return float(np.mean([v / N for v in counter.values()]))


# ---------------------------------------------------------------------------
# Evaluation metrics
# ---------------------------------------------------------------------------

def safe_spearman(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    m = np.isfinite(x) & np.isfinite(y)
    x, y = x[m], y[m]
    if len(x) < 3:
        return float("nan"), float("nan")
    r = spearmanr(x, y)
    return float(r.statistic), float(r.pvalue)


def safe_auroc(scores, labels):
    scores, labels = np.asarray(scores, float), np.asarray(labels, int)
    m = np.isfinite(scores)
    scores, labels = scores[m], labels[m]
    if len(np.unique(labels)) < 2:
        return float("nan")
    n_pos, n_neg = (labels == 1).sum(), (labels == 0).sum()
    if n_pos == 0 or n_neg == 0:
        return float("nan")
    ranks = rankdata(scores)
    u = ranks[labels == 1].sum() - n_pos * (n_pos + 1) / 2
    return float(u / (n_pos * n_neg))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def run_experiment(exp_name, cfg):
    print(f"\n{'='*60}")
    print(f"Experiment: {exp_name} ({cfg['dataset']})")
    print(f"{'='*60}")

    subtask = cfg["subtask"]
    field = "entities" if subtask == "ner" else "relations"

    # Load samples
    print(f"Loading samples from {cfg['samples_path']}...")
    all_instances = load_data(cfg["samples_path"])
    # Filter: non-empty gold
    instances = [d for d in all_instances if len(d["gold"].get(field, [])) > 0]
    print(f"  Total: {len(all_instances)}, non-empty gold: {len(instances)}")

    N_samples = len(instances[0]["samples"]) if instances else 0
    print(f"  Samples per instance: {N_samples}")

    # Build prompts
    print("Building verbalized confidence prompts...")
    prompts, index_map = build_prompts(instances, subtask)
    print(f"  Total prompts: {len(prompts)}")

    # Load model & generate
    print(f"Loading model: {cfg['model_path']}...")
    from vllm import LLM, SamplingParams
    from transformers import AutoTokenizer

    llm = LLM(
        model=cfg["model_path"],
        tensor_parallel_size=1,
        max_model_len=4096,
        gpu_memory_utilization=0.90,
    )
    tokenizer = AutoTokenizer.from_pretrained(cfg["model_path"], trust_remote_code=True)

    # Format with chat template
    formatted_prompts = []
    for p in prompts:
        messages = [{"role": "user", "content": p}]
        try:
            fp = tokenizer.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True,
                enable_thinking=False,
            )
        except TypeError:
            fp = tokenizer.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True,
            )
        formatted_prompts.append(fp)

    params = SamplingParams(
        n=1,
        temperature=0,
        max_tokens=16,
    )

    print(f"Generating {len(formatted_prompts)} completions...")
    t0 = time.time()
    outputs = llm.generate(formatted_prompts, params)
    elapsed = time.time() - t0
    print(f"  Generation done in {elapsed:.1f}s ({len(formatted_prompts)/elapsed:.0f} prompts/s)")

    # Parse scores
    raw_texts = [out.outputs[0].text for out in outputs]
    parsed_scores = [parse_score(t) for t in raw_texts]
    n_failed = sum(1 for s in parsed_scores if s is None)
    n_total = len(parsed_scores)
    print(f"  Parse failures: {n_failed}/{n_total} ({100*n_failed/n_total:.1f}%)")

    # Assign scores back to instances
    vc_scores_per_sample = [[None] * N_samples for _ in range(len(instances))]
    for idx, (i, j) in enumerate(index_map):
        vc_scores_per_sample[i][j] = parsed_scores[idx]

    # Replace None with fallback (5.0 = neutral)
    for i in range(len(instances)):
        for j in range(N_samples):
            if vc_scores_per_sample[i][j] is None:
                vc_scores_per_sample[i][j] = 5.0

    # Free GPU memory
    del llm
    import gc, torch
    gc.collect()
    torch.cuda.empty_cache()

    # --- Compute all metrics ---
    print("Computing metrics...")

    # Per-instance aggregation: mean of sample VerbConf
    instance_verb_conf = [float(np.mean(vc_scores_per_sample[i])) for i in range(len(instances))]

    # Greedy F1
    greedy_f1s = []
    for inst in instances:
        greedy = inst.get("greedy", inst["samples"][0])
        greedy_f1s.append(per_instance_f1(greedy, inst["gold"], subtask=subtask))
    greedy_arr = np.array(greedy_f1s)

    # Per-instance existing signals
    from consistency import compute_all_consistency_scores
    cons = compute_all_consistency_scores(instances, subtask=subtask)
    inst_sj = np.array(cons["soft_jaccard"])
    inst_fk = np.array(cons["fleiss_kappa"])
    inst_lp = np.array([compute_instance_mean_logprob(inst["samples"]) for inst in instances])
    inst_em = np.array([compute_instance_em_rate(inst["samples"], subtask) for inst in instances])
    inst_vc = np.array([compute_instance_voting_conf(inst["samples"], subtask) for inst in instances])
    inst_verbconf = np.array(instance_verb_conf)

    binary = (greedy_arr >= 1.0).astype(int)

    signals = {
        "SJ": inst_sj, "FK": inst_fk, "LP": inst_lp,
        "EM": inst_em, "VC": inst_vc, "VerbConf": inst_verbconf,
    }

    rho_results = {}
    for name, vals in signals.items():
        rho, p_rho = safe_spearman(vals, greedy_arr)
        auroc = safe_auroc(vals, binary)
        rho_results[name] = {
            "rho": round(rho, 4),
            "p_rho": float(p_rho) if np.isfinite(p_rho) else None,
            "auroc": round(auroc, 4) if np.isfinite(auroc) else None,
        }

    # --- Selection F1 ---
    print("Computing selection F1...")
    signal_sel_f1s = {sig: [] for sig in ["SJ", "FK", "VC", "EM", "LP", "VerbConf"]}
    oracle_f1s = []
    random_f1s = []

    for idx, inst in enumerate(instances):
        samples = inst["samples"]
        gold = inst["gold"]
        N = len(samples)

        sample_f1s = [per_instance_f1(s, gold, subtask=subtask) for s in samples]
        oracle_f1s.append(max(sample_f1s))
        random_f1s.append(float(np.mean(sample_f1s)))

        sj_scores = compute_sample_sj_scores(inst, subtask)
        fk_scores, key_sets = compute_sample_surface_scores(inst, subtask)
        vc_scores_inst = compute_sample_voting_conf(key_sets, N)
        em_scores = compute_sample_em_scores(key_sets)
        lp_scores = compute_sample_logprobs(inst)
        verb_scores = vc_scores_per_sample[idx]

        all_sig = {
            "SJ": sj_scores, "FK": fk_scores, "VC": vc_scores_inst,
            "EM": em_scores, "LP": lp_scores, "VerbConf": verb_scores,
        }

        for sig in signal_sel_f1s:
            chosen = int(np.argmax(all_sig[sig]))
            signal_sel_f1s[sig].append(sample_f1s[chosen])

    greedy_mean = float(greedy_arr.mean())
    oracle_mean = float(np.mean(oracle_f1s))
    random_mean = float(np.mean(random_f1s))

    selection_results = {
        "greedy_f1": round(greedy_mean, 4),
        "oracle_f1": round(oracle_mean, 4),
        "random_f1": round(random_mean, 4),
    }
    for sig in signal_sel_f1s:
        sel_mean = float(np.mean(signal_sel_f1s[sig]))
        delta = sel_mean - greedy_mean
        selection_results[sig] = {
            "selection_f1": round(sel_mean, 4),
            "delta_vs_greedy": round(delta, 4),
        }

    # Verb confidence distribution
    all_verb_flat = [s for row in vc_scores_per_sample for s in row]
    verb_dist = {
        "mean": round(float(np.mean(all_verb_flat)), 2),
        "std": round(float(np.std(all_verb_flat)), 2),
        "min": round(float(np.min(all_verb_flat)), 2),
        "max": round(float(np.max(all_verb_flat)), 2),
        "median": round(float(np.median(all_verb_flat)), 2),
    }
    # Score histogram
    hist = Counter()
    for s in all_verb_flat:
        hist[int(round(s))] += 1
    verb_dist["histogram"] = {str(k): v for k, v in sorted(hist.items())}

    result = {
        "experiment": exp_name,
        "dataset": cfg["dataset"],
        "n_instances": len(instances),
        "n_samples_per_instance": N_samples,
        "parse_failure_rate": round(n_failed / n_total, 4),
        "verb_conf_distribution": verb_dist,
        "rho_auroc": rho_results,
        "selection_f1": selection_results,
    }

    # Print summary
    print(f"\n--- Results for {exp_name} ---")
    print(f"  N instances: {len(instances)}")
    print(f"  Parse failure rate: {n_failed}/{n_total} ({100*n_failed/n_total:.1f}%)")
    print(f"  VerbConf distribution: mean={verb_dist['mean']}, std={verb_dist['std']}")
    print(f"\n  Spearman ρ (signal vs greedy F1):")
    for sig, v in rho_results.items():
        print(f"    {sig:10s}: ρ={v['rho']:+.4f}  AUROC={v['auroc']}")
    print(f"\n  Selection F1:")
    print(f"    Greedy:   {greedy_mean:.4f}")
    print(f"    Oracle:   {oracle_mean:.4f}")
    print(f"    Random:   {random_mean:.4f}")
    for sig in signal_sel_f1s:
        v = selection_results[sig]
        print(f"    {sig:10s}: {v['selection_f1']:.4f} (Δ={v['delta_vs_greedy']:+.4f})")

    return result


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    all_results = {}
    for exp_name, cfg in EXPERIMENTS.items():
        result = run_experiment(exp_name, cfg)
        all_results[exp_name] = result

        # Save individual result
        out_path = os.path.join(OUTPUT_DIR, f"{cfg['dataset']}_results.json")
        with open(out_path, "w") as f:
            json.dump(result, f, indent=2, default=str)
        print(f"  Saved to {out_path}")

    # Comparison table
    comparison = {}
    for exp_name, res in all_results.items():
        row = {"dataset": res["dataset"]}
        for sig in ["SJ", "FK", "VC", "EM", "LP", "VerbConf"]:
            row[f"{sig}_rho"] = res["rho_auroc"][sig]["rho"]
            row[f"{sig}_auroc"] = res["rho_auroc"][sig]["auroc"]
            row[f"{sig}_sel_f1"] = res["selection_f1"][sig]["selection_f1"]
            row[f"{sig}_delta"] = res["selection_f1"][sig]["delta_vs_greedy"]
        row["greedy_f1"] = res["selection_f1"]["greedy_f1"]
        row["oracle_f1"] = res["selection_f1"]["oracle_f1"]
        comparison[exp_name] = row

    comp_path = os.path.join(OUTPUT_DIR, "comparison.json")
    with open(comp_path, "w") as f:
        json.dump(comparison, f, indent=2, default=str)

    # Summary
    summary = {
        "experiment_id": "exp_verbalized_confidence",
        "date": time.strftime("%Y-%m-%d %H:%M:%S"),
        "description": "Verbalized confidence baseline: model self-rates extraction confidence 1-10",
        "datasets": list(all_results.keys()),
        "findings": {},
    }
    for exp_name, res in all_results.items():
        verb_rho = res["rho_auroc"]["VerbConf"]["rho"]
        sj_rho = res["rho_auroc"]["SJ"]["rho"]
        verb_sel = res["selection_f1"]["VerbConf"]["selection_f1"]
        sj_sel = res["selection_f1"]["SJ"]["selection_f1"]
        greedy = res["selection_f1"]["greedy_f1"]

        finding = {
            "VerbConf_rho": verb_rho,
            "best_existing_rho": max(
                res["rho_auroc"][s]["rho"]
                for s in ["SJ", "FK", "VC", "EM", "LP"]
                if np.isfinite(res["rho_auroc"][s]["rho"])
            ),
            "VerbConf_selection_f1": verb_sel,
            "VerbConf_delta_vs_greedy": res["selection_f1"]["VerbConf"]["delta_vs_greedy"],
            "greedy_f1": greedy,
            "parse_failure_rate": res["parse_failure_rate"],
            "verb_conf_mean": res["verb_conf_distribution"]["mean"],
            "verb_conf_std": res["verb_conf_distribution"]["std"],
        }

        if verb_rho < 0.1:
            finding["interpretation"] = "VerbConf shows near-zero correlation — supports score compression hypothesis"
        elif verb_rho > 0.2:
            finding["interpretation"] = "VerbConf shows meaningful correlation — positive finding"
        else:
            finding["interpretation"] = "VerbConf shows weak correlation — inconclusive"

        summary["findings"][exp_name] = finding

    sum_path = os.path.join(OUTPUT_DIR, "summary.json")
    with open(sum_path, "w") as f:
        json.dump(summary, f, indent=2, default=str)

    print(f"\n{'='*60}")
    print("All results saved to:")
    print(f"  {OUTPUT_DIR}/")
    print(f"  - scierc_results.json")
    print(f"  - conll_results.json")
    print(f"  - comparison.json")
    print(f"  - summary.json")


if __name__ == "__main__":
    main()
