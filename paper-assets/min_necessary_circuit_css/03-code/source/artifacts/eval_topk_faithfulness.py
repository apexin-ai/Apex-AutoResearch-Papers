import os
os.environ["CUDA_VISIBLE_DEVICES"] = "5"

import json, math, random, re, sys
from pathlib import Path
from functools import partial

import torch
import numpy as np

sys.path.insert(0, "/root/structfuse-context")

_LOCAL_GPT2 = "/root/autodl-tmp/gpt2-small"
_GPT2_ALIASES = ("gpt2", "gpt2-small", "openai-community/gpt2")

def _patch_hf():
    from transformers import AutoConfig, AutoTokenizer, AutoModelForCausalLM
    def _make_patched(orig_fn):
        def patched(name_or_path, *args, **kwargs):
            if name_or_path in _GPT2_ALIASES:
                name_or_path = _LOCAL_GPT2
            return orig_fn(name_or_path, *args, **kwargs)
        return patched
    AutoConfig.from_pretrained = staticmethod(_make_patched(AutoConfig.from_pretrained))
    AutoTokenizer.from_pretrained = staticmethod(_make_patched(AutoTokenizer.from_pretrained))
    AutoModelForCausalLM.from_pretrained = staticmethod(_make_patched(AutoModelForCausalLM.from_pretrained))

_patch_hf()

GT_DATASET_PATH = "/root/miniconda3/lib/python3.12/site-packages/datasets/greaterthan_gpt2-small_prompts.json"

NAMES = ["John", "Mary", "Alice", "Bob", "Charlie", "David", "Emma", "Frank",
         "Grace", "Henry", "Jack", "Kate", "Leo", "Mia", "Noah", "Tom"]
TEMPLATES = [
    "When {io} and {s} went to the {place}, {s} gave a {obj} to",
    "After {io} and {s} arrived at the {place}, {s} handed a {obj} to",
    "{io} and {s} were at the {place}. {s} gave a {obj} to",
    "Then, {io} and {s} had a meeting at the {place}, {s} passed a {obj} to",
]
PLACES = ["store", "park", "library", "school", "hospital", "restaurant", "office"]
OBJECTS = ["bottle", "book", "letter", "ball", "gift", "toy", "bag"]

# ── Data ──

def _precompute_year_tokens(tokenizer):
    tokens = {}
    for yr in range(100):
        s = f"{yr:02d}"
        ids = tokenizer.encode(s)
        tokens[s] = ids[0]
    return tokens

def load_gt_data(tokenizer, num_samples=100, seed=42):
    with open(GT_DATASET_PATH) as f:
        all_prompts = json.load(f)["prompts"]
    random.seed(seed)
    if len(all_prompts) > num_samples:
        all_prompts = random.sample(all_prompts, num_samples)
    yr_tok = _precompute_year_tokens(tokenizer)
    prompts, ans_list, wrong_list = [], [], []
    for p in all_prompts:
        prompts.append(p["clean"])
        ans_ids = torch.tensor([yr_tok[a] for a in p["answers"] if a in yr_tok])
        wrong_ids = torch.tensor([yr_tok[a] for a in p["wrong_answers"] if a in yr_tok])
        ans_list.append(ans_ids)
        wrong_list.append(wrong_ids)
    return prompts, ans_list, wrong_list

def generate_ioi_data(tokenizer, num_samples=100, seed=42):
    random.seed(seed)
    prompts, labels = [], []
    for _ in range(num_samples):
        io_name, s_name = random.sample(NAMES, 2)
        template = random.choice(TEMPLATES)
        place = random.choice(PLACES)
        obj = random.choice(OBJECTS)
        prompts.append(template.format(io=io_name, s=s_name, place=place, obj=obj))
        io_tokens = tokenizer.encode(" " + io_name)
        s_tokens = tokenizer.encode(" " + s_name)
        labels.append((io_tokens[0], s_tokens[0]))
    return prompts, labels

# ── Model ──

def load_model(device="cuda"):
    from transformer_lens import HookedTransformer
    from transformers import AutoModelForCausalLM
    hf_model = AutoModelForCausalLM.from_pretrained(_LOCAL_GPT2)
    model = HookedTransformer.from_pretrained("gpt2-small", hf_model=hf_model, device=device)
    model.set_use_attn_result(True)
    model.set_use_split_qkv_input(True)
    model.set_use_hook_mlp_in(True)
    return model

# ── Evaluation core ──

def extract_circuit_nodes(circuit_edges):
    nodes = set()
    for edge in circuit_edges:
        parts = edge.split('->')
        if len(parts) != 2:
            continue
        nodes.add(parts[0].strip())
        dst_base = re.sub(r'\.[qkv]$', '', parts[1].strip())
        nodes.add(dst_base)
    nodes.discard('input')
    nodes.discard('logits')
    return nodes

def collect_mean_activations(model, tokens):
    n_layers = model.cfg.n_layers
    accumulators = {}

    def make_accumulator(key):
        def hook_fn(value, hook):
            if key not in accumulators:
                accumulators[key] = value.detach().mean(dim=0, keepdim=True).clone()
            else:
                accumulators[key] += value.detach().mean(dim=0, keepdim=True)
            return value
        return hook_fn

    hooks = []
    for layer in range(n_layers):
        hooks.append((f"blocks.{layer}.attn.hook_result", make_accumulator(f"attn_{layer}")))
        hooks.append((f"blocks.{layer}.hook_mlp_out", make_accumulator(f"mlp_{layer}")))

    batch_size = 25
    n_batches = 0
    with torch.no_grad():
        for start in range(0, len(tokens), batch_size):
            batch = tokens[start:start + batch_size]
            model.run_with_hooks(batch, fwd_hooks=hooks)
            n_batches += 1

    attn_means, mlp_means = {}, {}
    for layer in range(n_layers):
        attn_means[layer] = accumulators[f"attn_{layer}"] / n_batches
        mlp_means[layer] = accumulators[f"mlp_{layer}"] / n_batches
    return attn_means, mlp_means

def evaluate_circuit(model, circuit_edges, tokens, metric_fn,
                     ablation_mode="zero", attn_means=None, mlp_means=None):
    if len(circuit_edges) == 0:
        return {"num_edges": 0, "cpr": 0.0, "cmd": 0.0}

    circuit_nodes = extract_circuit_nodes(circuit_edges)
    n_layers, n_heads = model.cfg.n_layers, model.cfg.n_heads

    ablate_heads = {}
    ablate_mlps = []
    for layer in range(n_layers):
        heads = [h for h in range(n_heads) if f'a{layer}.h{h}' not in circuit_nodes]
        if heads:
            ablate_heads[layer] = heads
        if f'm{layer}' not in circuit_nodes:
            ablate_mlps.append(layer)

    if ablation_mode == "zero":
        def _head_hook(value, hook, heads_to_ablate):
            for h in heads_to_ablate:
                value[:, :, h, :] = 0
            return value
        def _mlp_hook(value, hook):
            return torch.zeros_like(value)
    else:
        def _head_hook(value, hook, heads_to_ablate, layer_idx=None):
            mean_val = attn_means[layer_idx]
            seq_len = value.shape[1]
            mean_seq = mean_val.shape[1]
            if mean_seq >= seq_len:
                m = mean_val[:, -seq_len:, :, :]
            else:
                m = torch.nn.functional.pad(mean_val, (0,0,0,0,0,seq_len-mean_seq), mode='replicate')
            for h in heads_to_ablate:
                value[:, :, h, :] = m[:, :seq_len, h, :].expand(value.shape[0], -1, -1)
            return value
        def _mlp_hook(value, hook, layer_idx=None):
            mean_val = mlp_means[layer_idx]
            seq_len = value.shape[1]
            mean_seq = mean_val.shape[1]
            if mean_seq >= seq_len:
                m = mean_val[:, -seq_len:, :]
            else:
                m = torch.nn.functional.pad(mean_val, (0,0,0,seq_len-mean_seq), mode='replicate')
            return m[:, :seq_len, :].expand(value.shape[0], -1, -1)

    with torch.no_grad():
        baseline_logits = model(tokens)
        baseline_diff = metric_fn(baseline_logits, tokens)

        hooks = []
        for layer, heads in ablate_heads.items():
            if ablation_mode == "zero":
                hooks.append((f"blocks.{layer}.attn.hook_result",
                              partial(_head_hook, heads_to_ablate=heads)))
            else:
                hooks.append((f"blocks.{layer}.attn.hook_result",
                              partial(_head_hook, heads_to_ablate=heads, layer_idx=layer)))
        for layer in ablate_mlps:
            if ablation_mode == "zero":
                hooks.append((f"blocks.{layer}.hook_mlp_out", _mlp_hook))
            else:
                hooks.append((f"blocks.{layer}.hook_mlp_out", partial(_mlp_hook, layer_idx=layer)))

        circ_logits = model.run_with_hooks(tokens, fwd_hooks=hooks)
        circuit_diff = metric_fn(circ_logits, tokens)

    cpr = circuit_diff / baseline_diff if abs(baseline_diff) > 1e-6 else 0.0
    cmd = abs(baseline_diff - circuit_diff)
    return {"num_edges": len(circuit_edges), "cpr": round(cpr, 4), "cmd": round(cmd, 4)}

# ── Circuit construction ──

def topk_edges(scores, k):
    sorted_edges = sorted(
        scores.items(),
        key=lambda x: abs(x[1]) if not math.isinf(x[1]) else float('inf'),
        reverse=True
    )
    return set(e for e, _ in sorted_edges[:k])

def isinf_edges(scores):
    return set(e for e, v in scores.items() if math.isinf(v))

def compute_css(methods_edges):
    K = len(methods_edges)
    union = set()
    for edges in methods_edges.values():
        union |= edges
    return {e: sum(1 for es in methods_edges.values() if e in es) / K for e in union}

def threshold_css(css_scores, threshold):
    return {e for e, s in css_scores.items() if s >= threshold - 1e-2}

def css_distribution(css_scores):
    dist = {"1/3": 0, "2/3": 0, "3/3": 0}
    for s in css_scores.values():
        if s >= 1.0 - 1e-2:
            dist["3/3"] += 1
        elif s >= 0.67 - 1e-2:
            dist["2/3"] += 1
        else:
            dist["1/3"] += 1
    return dist

# ── Evaluation runner ──

def run_task_evaluation(model, tokens, metric_fn, attn_means, mlp_means,
                        acdc_scores, eapig_scores, ep_scores,
                        k_values, task_name):
    results = {}

    for k in k_values:
        print(f"\n--- k={k} ---")
        # CSS: ACDC-topK, EAP-IG-top100, EP-top100 (matches sweep convention)
        acdc_circ = topk_edges(acdc_scores, k)
        eapig_100 = topk_edges(eapig_scores, 100)
        ep_100 = topk_edges(ep_scores, 100)
        css_scores = compute_css({"acdc": acdc_circ, "eap_ig": eapig_100, "ep": ep_100})
        css_10 = threshold_css(css_scores, 1.0)
        css_067 = threshold_css(css_scores, 0.67)
        dist = css_distribution(css_scores)

        # Individual method circuits at same k (for fair per-edge comparison)
        eapig_k = topk_edges(eapig_scores, k)
        ep_k = topk_edges(ep_scores, k)

        circuits = {
            "CSS=1.0": css_10,
            "CSS>=2/3": css_067,
            "ACDC": acdc_circ,
            "EAP-IG": eapig_k,
            "EP": ep_k,
        }

        print(f"  CSS dist: {dist}")
        for name, edges in circuits.items():
            print(f"  {name}: {len(edges)} edges")

        k_results = {"css_distribution": dist}

        for mode in ["zero", "mean"]:
            print(f"  [{mode} ablation]")
            mode_results = {}
            for name, edges in circuits.items():
                r = evaluate_circuit(
                    model, edges, tokens, metric_fn,
                    ablation_mode=mode,
                    attn_means=attn_means if mode == "mean" else None,
                    mlp_means=mlp_means if mode == "mean" else None,
                )
                r["name"] = name
                mode_results[name] = r
                print(f"    {name} ({len(edges)} edges): CPR={r['cpr']:.4f}, CMD={r['cmd']:.4f}")
            k_results[mode] = mode_results
        results[f"k={k}"] = k_results

    # Also EAP-IG-top100 and EP-top100 as reference
    print("\n--- Reference: top-100 / isinf ---")
    acdc_inf = isinf_edges(acdc_scores)
    eapig_100 = topk_edges(eapig_scores, 100)
    ep_100 = topk_edges(ep_scores, 100)

    css_inf = compute_css({"acdc": acdc_inf, "eap_ig": eapig_100, "ep": ep_100})
    css_inf_10 = threshold_css(css_inf, 1.0)
    css_inf_067 = threshold_css(css_inf, 0.67)

    ref_circuits = {
        "ACDC-isinf": acdc_inf,
        "EAP-IG-100": eapig_100,
        "EP-100": ep_100,
        "CSS=1.0-isinf": css_inf_10,
        "CSS>=2/3-isinf": css_inf_067,
    }

    ref_results = {}
    for mode in ["zero", "mean"]:
        print(f"  [{mode} ablation - ref]")
        mode_results = {}
        for name, edges in ref_circuits.items():
            r = evaluate_circuit(
                model, edges, tokens, metric_fn,
                ablation_mode=mode,
                attn_means=attn_means if mode == "mean" else None,
                mlp_means=mlp_means if mode == "mean" else None,
            )
            r["name"] = name
            mode_results[name] = r
            print(f"    {name} ({len(edges)} edges): CPR={r['cpr']:.4f}, CMD={r['cmd']:.4f}")
        ref_results[mode] = mode_results
    results["isinf_ref"] = ref_results

    return results

def print_summary_table(task_name, results, k_values):
    print(f"\n=== {task_name} Top-K Faithfulness ===\n")
    print(f"{'Circuit':<20} {'k':>5} {'Edges':>6} {'Zero CPR':>9} {'Zero CMD':>9} {'Mean CPR':>9} {'Mean CMD':>9}")
    print("-" * 72)

    for k in k_values:
        key = f"k={k}"
        data = results[key]
        for name in ["CSS=1.0", "CSS>=2/3", "ACDC", "EAP-IG", "EP"]:
            z = data["zero"][name]
            m = data["mean"][name]
            print(f"{name:<20} {k:>5} {z['num_edges']:>6} {z['cpr']:>9.4f} {z['cmd']:>9.4f} {m['cpr']:>9.4f} {m['cmd']:>9.4f}")
        print()

    # isinf reference
    ref = results["isinf_ref"]
    for name in ["CSS=1.0-isinf", "CSS>=2/3-isinf", "ACDC-isinf", "EAP-IG-100", "EP-100"]:
        z = ref["zero"][name]
        m = ref["mean"][name]
        print(f"{name:<20} {'ref':>5} {z['num_edges']:>6} {z['cpr']:>9.4f} {z['cmd']:>9.4f} {m['cpr']:>9.4f} {m['cmd']:>9.4f}")

def check_condition_4(task_name, results, k_values):
    print(f"\n--- {task_name}: D025 Condition ④ ---")
    for k in k_values:
        key = f"k={k}"
        data = results[key]
        for mode in ["zero", "mean"]:
            css_cpr = data[mode]["CSS=1.0"]["cpr"]
            css_edges = data[mode]["CSS=1.0"]["num_edges"]
            methods = ["ACDC", "EAP-IG", "EP"]
            best_name = max(methods, key=lambda n: data[mode][n]["cpr"])
            best_cpr = data[mode][best_name]["cpr"]
            best_edges = data[mode][best_name]["num_edges"]
            passed = css_cpr > best_cpr
            print(f"  k={k} [{mode}]: CSS=1.0 CPR={css_cpr:.4f} ({css_edges}e) "
                  f"vs {best_name} CPR={best_cpr:.4f} ({best_edges}e) "
                  f"→ {'PASS ✓' if passed else 'FAIL ✗'}")


def main():
    device = torch.device("cuda")
    cache_dir = Path("/root/structfuse-context")

    print(f"CUDA_VISIBLE_DEVICES={os.environ.get('CUDA_VISIBLE_DEVICES')}")
    print("Loading model...")
    model = load_model(device)

    # ═══════════════ Arithmetic ═══════════════
    print("\n" + "=" * 70)
    print("  ARITHMETIC (Greaterthan)")
    print("=" * 70)

    prompts_a, ans_list, wrong_list = load_gt_data(model.tokenizer, num_samples=100, seed=42)
    tokens_a = model.to_tokens(prompts_a, prepend_bos=True)
    print(f"Data: {len(prompts_a)} prompts, tokens {tokens_a.shape}")

    def metric_arith(logits, tokens):
        diffs = []
        for i in range(len(tokens)):
            diffs.append(logits[i, -1, ans_list[i]].mean() - logits[i, -1, wrong_list[i]].mean())
        return torch.stack(diffs).mean().item()

    print("Collecting mean activations...")
    attn_m_a, mlp_m_a = collect_mean_activations(model, tokens_a)

    with open(cache_dir / "cache_acdc_arith.json") as f: acdc_a = json.load(f)
    with open(cache_dir / "cache_eap_ig_arith.json") as f: eapig_a = json.load(f)
    with open(cache_dir / "cache_ep_arith.json") as f: ep_a = json.load(f)

    arith_results = run_task_evaluation(
        model, tokens_a, metric_arith, attn_m_a, mlp_m_a,
        acdc_a, eapig_a, ep_a,
        k_values=[50, 75, 100],
        task_name="Arithmetic"
    )

    with open(cache_dir / "faithfulness_arithmetic_topk.json", "w") as f:
        json.dump(arith_results, f, indent=2)
    print(f"\nSaved: faithfulness_arithmetic_topk.json")

    # ═══════════════ IOI ═══════════════
    print("\n" + "=" * 70)
    print("  IOI")
    print("=" * 70)

    prompts_i, labels_i = generate_ioi_data(model.tokenizer, num_samples=100, seed=42)
    tokens_i = model.to_tokens(prompts_i, prepend_bos=True)
    io_ids = torch.tensor([l[0] for l in labels_i])
    s_ids = torch.tensor([l[1] for l in labels_i])
    print(f"Data: {len(prompts_i)} prompts, tokens {tokens_i.shape}")

    def metric_ioi(logits, tokens):
        return (logits[range(len(tokens)), -1, io_ids] -
                logits[range(len(tokens)), -1, s_ids]).mean().item()

    print("Collecting mean activations...")
    attn_m_i, mlp_m_i = collect_mean_activations(model, tokens_i)

    with open(cache_dir / "cache_acdc.json") as f: acdc_i = json.load(f)
    with open(cache_dir / "cache_eap_ig.json") as f: eapig_i = json.load(f)
    with open(cache_dir / "cache_edge_pruning.json") as f: ep_i = json.load(f)

    ioi_results = run_task_evaluation(
        model, tokens_i, metric_ioi, attn_m_i, mlp_m_i,
        acdc_i, eapig_i, ep_i,
        k_values=[50, 100],
        task_name="IOI"
    )

    with open(cache_dir / "faithfulness_ioi_topk.json", "w") as f:
        json.dump(ioi_results, f, indent=2)
    print(f"\nSaved: faithfulness_ioi_topk.json")

    # ═══════════════ Summary ═══════════════
    print("\n" + "=" * 70)
    print("  FULL SUMMARY")
    print("=" * 70)

    print_summary_table("Arithmetic", arith_results, [50, 75, 100])
    print_summary_table("IOI", ioi_results, [50, 100])

    check_condition_4("Arithmetic", arith_results, [50, 75])
    check_condition_4("IOI", ioi_results, [50, 100])

    # CPR inconsistency analysis
    print("\n=== IOI CPR Inconsistency Analysis ===")
    print("phase_d_results.json: IOI task, node-level zero ablation (evaluation.py)")
    print("mean_ablation_results.json: ARITHMETIC task, not IOI (eval_mean_ablation.py)")
    print("Conclusion: The files evaluate DIFFERENT TASKS.")
    print("  - evaluation.py uses io_ids/s_ids (IOI logit difference)")
    print("  - eval_mean_ablation.py uses ans_list/wrong_list (Greaterthan year tokens)")
    print("  - Numbers are incomparable. Both implementations are correct for their task.")
    print("  - The isinf issue (CSS=1.0 = ACDC) affects both tasks, now resolved with topk.")

    print("\nDone.")


if __name__ == "__main__":
    main()
