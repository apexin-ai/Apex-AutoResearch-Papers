import os
os.environ["CUDA_VISIBLE_DEVICES"] = "1"

"""StructFuse Factual Recall (Country Capitals) pipeline — GPT-2 Small.

Task: "The capital of {country} is" → correct capital vs wrong capital.
Circuit tests MLP-based factual knowledge retrieval (Meng et al. 2022).
All three methods use identical top-100 binarization for fair comparison.
Evaluation includes both zero and mean ablation.
"""

import json
import random
import gc
import re
from pathlib import Path
from functools import partial
from collections import Counter

import torch
from torch.utils.data import DataLoader, Dataset

from config import MVPConfig
from circuit_discovery import run_eap_ig, run_edge_pruning, run_acdc
from circus import run_circus, get_tier_sets
from cross_tabulate import (
    cross_tabulate, compute_off_diagonal, print_cross_table,
    pairwise_jaccard, three_way_jaccard, print_pairwise_jaccard,
)


_LOCAL_GPT2 = "/root/autodl-tmp/gpt2-small"
_GPT2_ALIASES = ("gpt2", "gpt2-small", "openai-community/gpt2")

def _patch_hf_from_pretrained():
    from transformers import AutoConfig, AutoTokenizer, AutoModelForCausalLM
    def _make_patched(orig_fn):
        def patched(pretrained_model_name_or_path, *args, **kwargs):
            if pretrained_model_name_or_path in _GPT2_ALIASES:
                pretrained_model_name_or_path = _LOCAL_GPT2
            return orig_fn(pretrained_model_name_or_path, *args, **kwargs)
        return patched
    AutoConfig.from_pretrained = staticmethod(_make_patched(AutoConfig.from_pretrained))
    AutoTokenizer.from_pretrained = staticmethod(_make_patched(AutoTokenizer.from_pretrained))
    AutoModelForCausalLM.from_pretrained = staticmethod(_make_patched(AutoModelForCausalLM.from_pretrained))

_patch_hf_from_pretrained()


# ---------------------------------------------------------------------------
# Factual Recall Dataset
# ---------------------------------------------------------------------------

COUNTRY_CAPITAL_PAIRS = [
    ("France", "Paris"), ("Germany", "Berlin"), ("Japan", "Tokyo"),
    ("Italy", "Rome"), ("Spain", "Madrid"), ("Russia", "Moscow"),
    ("China", "Beijing"), ("England", "London"), ("Poland", "Warsaw"),
    ("Greece", "Athens"), ("Ireland", "Dublin"), ("Sweden", "Stockholm"),
    ("Norway", "Oslo"), ("Portugal", "Lisbon"), ("Austria", "Vienna"),
    ("Egypt", "Cairo"), ("Korea", "Seoul"), ("Denmark", "Copenhagen"),
    ("Belgium", "Brussels"), ("Netherlands", "Amsterdam"),
    ("Ukraine", "Kiev"), ("Turkey", "Istanbul"),
]


def generate_factual_recall_prompts(num_samples=500, seed=42):
    rng = random.Random(seed)
    n = len(COUNTRY_CAPITAL_PAIRS)
    prompts = []
    seen = set()
    attempts = 0
    while len(prompts) < num_samples and attempts < num_samples * 20:
        attempts += 1
        i = rng.randint(0, n - 1)
        j = rng.randint(0, n - 2)
        if j >= i:
            j += 1
        sig = (i, j)
        if sig in seen:
            continue
        seen.add(sig)
        country, capital = COUNTRY_CAPITAL_PAIRS[i]
        wrong_country, wrong_capital = COUNTRY_CAPITAL_PAIRS[j]
        clean = f"The capital of {country} is"
        corrupt = f"The capital of {wrong_country} is"
        prompts.append({
            "clean": clean,
            "corrupt": corrupt,
            "answer": capital,
            "wrong_answer": wrong_capital,
        })
    return prompts


FR_DATASET_PATH = "/root/miniconda3/lib/python3.12/site-packages/datasets/factual_recall_gpt2-small_prompts.json"


def ensure_fr_dataset():
    if not os.path.exists(FR_DATASET_PATH):
        prompts = generate_factual_recall_prompts(num_samples=500, seed=42)
        with open(FR_DATASET_PATH, "w") as f:
            json.dump({"prompts": prompts}, f, indent=2)
        print(f"FR dataset created: {len(prompts)} prompts -> {FR_DATASET_PATH}")
    else:
        with open(FR_DATASET_PATH) as f:
            n = len(json.load(f)["prompts"])
        print(f"FR dataset exists: {n} prompts at {FR_DATASET_PATH}")


class FactualRecallDataset(Dataset):
    def __init__(self, tokenizer, num_samples=100, seed=42):
        ensure_fr_dataset()
        with open(FR_DATASET_PATH) as f:
            all_prompts = json.load(f)["prompts"]
        random.seed(seed)
        if len(all_prompts) > num_samples:
            all_prompts = random.sample(all_prompts, num_samples)
        self.prompts = []
        self.corrupted = []
        self.labels = []
        for p in all_prompts:
            self.prompts.append(p["clean"])
            self.corrupted.append(p["corrupt"])
            ans_id = tokenizer.encode(" " + p["answer"])[0]
            wrong_id = tokenizer.encode(" " + p["wrong_answer"])[0]
            self.labels.append((ans_id, wrong_id))

    def __len__(self):
        return len(self.prompts)

    def __getitem__(self, idx):
        return self.prompts[idx], self.corrupted[idx], self.labels[idx]


def fr_collate_fn(batch):
    return [b[0] for b in batch], [b[1] for b in batch], [b[2] for b in batch]


def factual_recall_metric(logits, clean_logits, input_lengths, labels):
    batch_size = logits.shape[0]
    diffs = []
    for i in range(batch_size):
        last_pos = input_lengths[i] - 1
        correct_id, incorrect_id = labels[i]
        diff = logits[i, last_pos, correct_id] - logits[i, last_pos, incorrect_id]
        diffs.append(diff)
    return torch.stack(diffs).mean()


# ---------------------------------------------------------------------------
# Binarization: ALL top-100 (including ACDC)
# ---------------------------------------------------------------------------

def binarize_top100(scores, top_n=100):
    sorted_edges = sorted(scores.items(), key=lambda x: abs(x[1]), reverse=True)
    return {e for e, _ in sorted_edges[:top_n]}


# ---------------------------------------------------------------------------
# CSS helpers
# ---------------------------------------------------------------------------

def compute_css(method_circuits, K=3):
    all_edges = set()
    for edges in method_circuits.values():
        all_edges |= edges
    scores = {}
    for edge in all_edges:
        count = sum(1 for c in method_circuits.values() if edge in c)
        scores[edge] = count / K
    return scores


def threshold_css(css_scores, threshold):
    return {e for e, s in css_scores.items() if s >= threshold - 1e-2}


def css_summary(css_scores, K=3):
    dist = Counter()
    for s in css_scores.values():
        dist[round(s, 4)] += 1
    result = {}
    for v in sorted(dist.keys()):
        label = f"{v:.2f}"
        result[label] = dist[v]
        print(f"  CSS={label}: {dist[v]} edges")
    return result


# ---------------------------------------------------------------------------
# Evaluation (zero + mean ablation)
# ---------------------------------------------------------------------------

def _extract_circuit_nodes(circuit_edges):
    nodes = set()
    for edge in circuit_edges:
        parts = edge.split("->")
        if len(parts) != 2:
            continue
        nodes.add(parts[0].strip())
        dst_base = re.sub(r"\.[qkv]$", "", parts[1].strip())
        nodes.add(dst_base)
    nodes.discard("input")
    nodes.discard("logits")
    return nodes


def evaluate_circuit_fr(model, circuit_edges, clean_tokens, ans_id, wrong_id, ablation="zero"):
    if len(circuit_edges) == 0:
        return {"name": "", "num_edges": 0, "cpr": 0.0, "cmd": 0.0}

    circuit_nodes = _extract_circuit_nodes(circuit_edges)
    n_layers, n_heads = model.cfg.n_layers, model.cfg.n_heads

    ablate_heads = {}
    ablate_mlps = []
    for layer in range(n_layers):
        heads = [h for h in range(n_heads) if f"a{layer}.h{h}" not in circuit_nodes]
        if heads:
            ablate_heads[layer] = heads
        if f"m{layer}" not in circuit_nodes:
            ablate_mlps.append(layer)

    mean_cache = {}
    if ablation == "mean":
        with torch.no_grad():
            _, cache = model.run_with_cache(clean_tokens)
            for layer in ablate_heads:
                hook_name = f"blocks.{layer}.attn.hook_result"
                mean_cache[hook_name] = cache[hook_name].mean(dim=0, keepdim=True)
            for layer in ablate_mlps:
                hook_name = f"blocks.{layer}.hook_mlp_out"
                mean_cache[hook_name] = cache[hook_name].mean(dim=0, keepdim=True)
            del cache
            torch.cuda.empty_cache()

    def _head_hook_zero(value, hook, heads_to_ablate):
        for h in heads_to_ablate:
            value[:, :, h, :] = 0
        return value

    def _head_hook_mean(value, hook, heads_to_ablate, mean_val):
        for h in heads_to_ablate:
            value[:, :, h, :] = mean_val[:, :, h, :]
        return value

    def _mlp_hook_zero(value, hook):
        return torch.zeros_like(value)

    def _mlp_hook_mean(value, hook, mean_val):
        return mean_val.expand_as(value)

    with torch.no_grad():
        baseline_logits = model(clean_tokens)
        bl_diffs = []
        for i in range(len(clean_tokens)):
            a_id, w_id = ans_id[i], wrong_id[i]
            bl_diffs.append(baseline_logits[i, -1, a_id] - baseline_logits[i, -1, w_id])
        baseline_diff = torch.stack(bl_diffs).mean().item()

        hooks = []
        for layer, heads in ablate_heads.items():
            hook_name = f"blocks.{layer}.attn.hook_result"
            if ablation == "zero":
                hooks.append((hook_name, partial(_head_hook_zero, heads_to_ablate=heads)))
            else:
                hooks.append((hook_name, partial(_head_hook_mean, heads_to_ablate=heads,
                                                  mean_val=mean_cache[hook_name])))
        for layer in ablate_mlps:
            hook_name = f"blocks.{layer}.hook_mlp_out"
            if ablation == "zero":
                hooks.append((hook_name, _mlp_hook_zero))
            else:
                hooks.append((hook_name, partial(_mlp_hook_mean, mean_val=mean_cache[hook_name])))

        circuit_logits = model.run_with_hooks(clean_tokens, fwd_hooks=hooks)
        c_diffs = []
        for i in range(len(clean_tokens)):
            a_id, w_id = ans_id[i], wrong_id[i]
            c_diffs.append(circuit_logits[i, -1, a_id] - circuit_logits[i, -1, w_id])
        circuit_diff = torch.stack(c_diffs).mean().item()

    cpr = circuit_diff / baseline_diff if abs(baseline_diff) > 1e-6 else 0.0
    cmd = abs(baseline_diff - circuit_diff)
    return {"name": "", "num_edges": len(circuit_edges), "cpr": round(cpr, 4), "cmd": round(cmd, 4)}


def evaluate_all_fr(model, circuits, clean_tokens, ans_id, wrong_id, ablation="zero"):
    results = []
    for name, edges in circuits.items():
        print(f"  {name} ({len(edges)} edges, {ablation})")
        r = evaluate_circuit_fr(model, edges, clean_tokens, ans_id, wrong_id, ablation=ablation)
        r["name"] = name
        r["ablation"] = ablation
        results.append(r)
    return results


# ---------------------------------------------------------------------------
# Model loading
# ---------------------------------------------------------------------------

def load_tl_model(device="cuda"):
    from transformer_lens import HookedTransformer
    local_path = "/root/autodl-tmp/gpt2-small"
    if os.path.exists(os.path.join(local_path, "model.safetensors")):
        print(f"Loading GPT-2 from local: {local_path}")
        from transformers import AutoModelForCausalLM
        hf_model = AutoModelForCausalLM.from_pretrained(local_path)
        model = HookedTransformer.from_pretrained("gpt2-small", hf_model=hf_model, device=device)
    else:
        print("Loading GPT-2 from HuggingFace...")
        model = HookedTransformer.from_pretrained("gpt2-small", device=device)
    model.set_use_attn_result(True)
    model.set_use_split_qkv_input(True)
    model.set_use_hook_mlp_in(True)
    return model


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def main():
    device = torch.device("cuda")
    config = MVPConfig(
        model_name="gpt2-small",
        task="factual_recall",
        num_samples=100,
        methods=["eap_ig", "edge_pruning", "acdc"],
        K=3,
        eap_ig_steps=5,
        eap_ig_topn=100,
    )
    print(f"StructFuse Factual Recall: model={config.model_name}, task={config.task}, K={config.K}")
    print(f"Methods: {config.methods}")
    print(f"Binarization: all top-{config.eap_ig_topn}")
    print()

    all_scores = {}
    cache_dir = Path(__file__).parent

    # === Phase A: EAP-IG ===
    eap_cache = cache_dir / "cache_eap_ig_fr.json"
    if eap_cache.exists():
        print("=== Phase A: EAP-IG (loading from cache) ===")
        with open(eap_cache) as f:
            all_scores["eap_ig"] = json.load(f)
        print(f"  eap_ig: {len(all_scores['eap_ig'])} edges (cached)")
        model = load_tl_model(device=device)
        fr_dataset = FactualRecallDataset(model.tokenizer, num_samples=config.num_samples)
        eval_prompts = fr_dataset.prompts[:50]
        eval_labels = fr_dataset.labels[:50]
        del model
        gc.collect()
        torch.cuda.empty_cache()
    else:
        print("=== Phase A: EAP-IG ===")
        model = load_tl_model(device=device)
        print(f"Model loaded: {model.cfg.n_layers} layers, {model.cfg.n_heads} heads")
        fr_dataset = FactualRecallDataset(model.tokenizer, num_samples=config.num_samples)
        eap_dataloader = DataLoader(fr_dataset, batch_size=25, collate_fn=fr_collate_fn)
        print("Running eap_ig...")
        all_scores["eap_ig"] = run_eap_ig(model, eap_dataloader, factual_recall_metric, config.eap_ig_steps, config)
        print(f"  eap_ig: {len(all_scores['eap_ig'])} edges scored")
        with open(eap_cache, "w") as f:
            json.dump(all_scores["eap_ig"], f)
        print(f"  Cached to {eap_cache}")
        eval_prompts = fr_dataset.prompts[:50]
        eval_labels = fr_dataset.labels[:50]
        del model
        gc.collect()
        torch.cuda.empty_cache()
        print("EAP model freed from GPU")

    # === Phase A: Edge Pruning + ACDC ===
    ep_cache = cache_dir / "cache_ep_fr.json"
    acdc_cache = cache_dir / "cache_acdc_fr.json"
    need_ep = not ep_cache.exists()
    need_acdc = not acdc_cache.exists()

    if ep_cache.exists():
        print("\n=== Edge Pruning (loading from cache) ===")
        with open(ep_cache) as f:
            all_scores["edge_pruning"] = json.load(f)
        print(f"  edge_pruning: {len(all_scores['edge_pruning'])} edges (cached)")
    if acdc_cache.exists():
        print("\n=== ACDC (loading from cache) ===")
        with open(acdc_cache) as f:
            all_scores["acdc"] = json.load(f)
        print(f"  acdc: {len(all_scores['acdc'])} edges (cached)")

    if need_ep or need_acdc:
        model2 = load_tl_model(device=device)
        fr_dataset2 = FactualRecallDataset(model2.tokenizer, num_samples=config.num_samples)
        dl2 = DataLoader(fr_dataset2, batch_size=25, collate_fn=fr_collate_fn)

        if need_ep:
            print("\n=== Phase A: Edge Pruning ===")
            all_scores["edge_pruning"] = run_edge_pruning(model2, dl2, factual_recall_metric, config)
            print(f"  edge_pruning: {len(all_scores['edge_pruning'])} edges scored")
            with open(ep_cache, "w") as f:
                json.dump(all_scores["edge_pruning"], f)

        if need_acdc:
            print("\n=== Phase A: ACDC ===")
            all_scores["acdc"] = run_acdc(model2, dl2, factual_recall_metric, config)
            print(f"  acdc: {len(all_scores['acdc'])} edges scored")
            with open(acdc_cache, "w") as f:
                json.dump(all_scores["acdc"], f)

        del model2
        gc.collect()
        torch.cuda.empty_cache()

    # === Phase B: Binarization (all top-100) ===
    print("\n=== Phase B: Binarization (all top-100) ===")
    method_circuits = {}
    for method in config.methods:
        method_circuits[method] = binarize_top100(all_scores[method], top_n=config.eap_ig_topn)
        print(f"  {method}: {len(method_circuits[method])} edges")

    # === Phase B: CSS ===
    print("\n=== Phase B: CSS ===")
    css_scores = compute_css(method_circuits, K=config.K)
    css_dist = css_summary(css_scores, K=config.K)

    # === Phase B: CIRCUS ===
    print("\n=== Phase B: CIRCUS ===")
    union_scores = {}
    for method in config.methods:
        for edge, score in all_scores[method].items():
            if edge not in union_scores:
                union_scores[edge] = 0.0
            union_scores[edge] = max(union_scores[edge], abs(score))
    circus_stability, circus_tiers = run_circus(union_scores, config)

    # === Phase C: Cross-tabulation ===
    print("\n=== Phase C: Cross-tabulation ===")
    table = cross_tabulate(circus_tiers, css_scores, config.css_default_threshold)
    print_cross_table(table)
    off_diag = compute_off_diagonal(table)

    from scipy.stats import beta as beta_dist
    n = table.core_total
    k = len(table.method_specific)
    alpha = 0.05
    if n > 0:
        ci_low = beta_dist.ppf(alpha / 2, max(k, 0.5), n - k + 1) if k > 0 else 0.0
        ci_high = beta_dist.ppf(1 - alpha / 2, k + 1, max(n - k, 0.5)) if k < n else 1.0
    else:
        ci_low, ci_high = 0.0, 0.0
    print(f"Off-diagonal %: {off_diag*100:.1f}%  95% CI: [{ci_low*100:.1f}%, {ci_high*100:.1f}%]")

    print("\n--- Pairwise Jaccard Decomposition ---")
    pw_jaccard = pairwise_jaccard(method_circuits)
    tw_jaccard = three_way_jaccard(method_circuits)
    print_pairwise_jaccard(pw_jaccard, tw_jaccard)

    # === Phase D: Evaluation (zero + mean ablation) ===
    print("\n=== Phase D: Evaluation (zero + mean ablation) ===")
    eval_model = load_tl_model(device=device)
    eval_tokens = eval_model.to_tokens(eval_prompts, prepend_bos=True)
    eval_ans_ids = [lab[0] for lab in eval_labels]
    eval_wrong_ids = [lab[1] for lab in eval_labels]

    circuits_to_eval = {}
    for method, edges in method_circuits.items():
        circuits_to_eval[f"method_{method}"] = edges
    for thr in config.css_thresholds:
        if thr > 0:
            circuits_to_eval[f"css_{thr:.2f}"] = threshold_css(css_scores, thr)
    tier_sets = get_tier_sets(circus_tiers)
    circuits_to_eval["circus_core"] = tier_sets["core"]
    circuits_to_eval["stable_core"] = table.stable_core

    print("\n--- Zero Ablation ---")
    eval_zero = evaluate_all_fr(eval_model, circuits_to_eval, eval_tokens, eval_ans_ids, eval_wrong_ids, ablation="zero")
    hdr = f"{'Circuit':<30} {'Edges':>6} {'CPR':>8} {'CMD':>8}"
    print(f"\n{hdr}")
    print("-" * 54)
    for r in sorted(eval_zero, key=lambda x: x["cpr"], reverse=True):
        print(f"{r['name']:<30} {r['num_edges']:>6} {r['cpr']:>8.4f} {r['cmd']:>8.4f}")

    print("\n--- Mean Ablation ---")
    eval_mean = evaluate_all_fr(eval_model, circuits_to_eval, eval_tokens, eval_ans_ids, eval_wrong_ids, ablation="mean")
    print(f"\n{hdr}")
    print("-" * 54)
    for r in sorted(eval_mean, key=lambda x: x["cpr"], reverse=True):
        print(f"{r['name']:<30} {r['num_edges']:>6} {r['cpr']:>8.4f} {r['cmd']:>8.4f}")

    del eval_model
    gc.collect()
    torch.cuda.empty_cache()

    # === Gate Assessment ===
    print("\n" + "=" * 50)
    print("FACTUAL RECALL GATE ASSESSMENT")
    print("=" * 50)
    pct = off_diag * 100
    if pct >= 10:
        gate_verdict = "PASS_MAIN"
        gate_msg = f"Off-diagonal {pct:.1f}% >= 10% -> Main track"
    elif pct >= 5:
        gate_verdict = "PASS_FINDINGS"
        gate_msg = f"Off-diagonal {pct:.1f}% in [5-10%) -> Findings default"
    elif pct >= 2:
        gate_verdict = "MARGINAL"
        gate_msg = f"Off-diagonal {pct:.1f}% in [2-5%) -> Marginal"
    else:
        gate_verdict = "KILL"
        gate_msg = f"Off-diagonal {pct:.1f}% < 2% -> Kill project"
    print(f"Off-diagonal %: {pct:.1f}%  95% CI: [{ci_low*100:.1f}%, {ci_high*100:.1f}%]")
    print(f"Verdict: {gate_verdict}")
    print(f"Action: {gate_msg}")
    if n > 0 and n < 30:
        print(f"WARNING: CIRCUS-core has only {n} edges (< 30).")

    # D032 condition④: check css_1.00 CPR
    css_100_edges = threshold_css(css_scores, 1.0)
    css_100_zero = [r for r in eval_zero if r["name"] == "css_1.00"]
    css_100_mean = [r for r in eval_mean if r["name"] == "css_1.00"]
    if css_100_zero:
        print(f"\nD032 condition④: css_1.00 CPR(zero)={css_100_zero[0]['cpr']:.4f} edges={css_100_zero[0]['num_edges']}")
    if css_100_mean:
        print(f"D032 condition④: css_1.00 CPR(mean)={css_100_mean[0]['cpr']:.4f} edges={css_100_mean[0]['num_edges']}")

    # Save results
    output = {
        "config": {"model": config.model_name, "task": "factual_recall", "K": config.K, "methods": config.methods},
        "binarization": {m: f"top-{config.eap_ig_topn}" for m in config.methods},
        "method_edge_counts": {m: len(edges) for m, edges in method_circuits.items()},
        "cross_table": table.summary(),
        "core_off_diagonal_pct": off_diag,
        "binomial_ci_95": {"low": round(ci_low, 4), "high": round(ci_high, 4)},
        "css_distribution": css_dist,
        "circus_tier_counts": {t: sum(1 for v in circus_tiers.values() if v == t) for t in ["core", "contingent", "noise"]},
        "evaluation_zero": eval_zero,
        "evaluation_mean": eval_mean,
        "gate_verdict": gate_verdict,
        "pairwise_jaccard": {f"{m1}_x_{m2}": {"jaccard": round(j, 4), "intersection": i, "union": u} for m1, m2, j, i, u in pw_jaccard},
        "three_way_jaccard": {"jaccard": round(tw_jaccard[0], 4), "intersection": tw_jaccard[1], "union": tw_jaccard[2]},
    }

    output_path = Path(__file__).parent / "factual_recall_results.json"
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {output_path}")


if __name__ == "__main__":
    main()
