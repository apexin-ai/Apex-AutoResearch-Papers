#!/usr/bin/env python3
"""B3: Prompted Diversity — multi-template vs single-template entity construction.

Hypothesis: Structurally different prompt templates generate more diverse N=8
samples than identical template, improving entity construction F1.

Conditions:
  single_template: Template A × N=8
  multi_template:  A×2 + B×2 + C×2 + D×2 = 8 total

Usage:
  CUDA_VISIBLE_DEVICES=2 python exp_b3_prompted_diversity.py --phase both --num_instances 3000
"""

import argparse
import json
import os
import sys
import time
import numpy as np
from collections import defaultdict

sys.path.insert(0, "/root/autodl-tmp/struct_self_consist_ie/code")

# ============================================================
# Template Definitions
# ============================================================

FEWNERD_TYPES = "person, organization, location, building, art, product, event, other"

TEMPLATES = {
    "A_standard": {
        "description": "Train-aligned baseline template (same as FT training format)",
        "system": None,
        "user": (
            "Extract all structured information (entities and relations) from the following text. "
            "Output a JSON object.\n\n"
            "Text: {text}\n"
            "Schema: Entity types: " + FEWNERD_TYPES + "\n\n"
            "Output format: "
            '{{"entities": [{{"text": "...", "type": "...", "start": <int>, "end": <int>}}], '
            '"relations": [{{"head": "...", "tail": "...", "type": "...", '
            '"head_start": <int>, "head_end": <int>, "tail_start": <int>, "tail_end": <int>}}], '
            '"events": []}}'
        ),
    },
    "B_expert": {
        "description": "Expert persona via system message — emphasizes precision and offset correctness",
        "system": (
            "You are an expert named entity recognition system. "
            "You identify every named entity in the input text with high precision. "
            "Output character-level offsets using Python slice convention: text[start:end] == entity_text."
        ),
        "user": (
            "Extract all named entities from the following text.\n\n"
            "Text: {text}\n\n"
            "Entity types: " + FEWNERD_TYPES + "\n\n"
            "Output a JSON object:\n"
            '{{"entities": [{{"text": "...", "type": "...", "start": <int>, "end": <int>}}], '
            '"relations": [], "events": []}}'
        ),
    },
    "C_descriptive": {
        "description": "Rich type descriptions — provides definitions for each entity type",
        "system": None,
        "user": (
            "Extract named entities from the following text. "
            "Classify each entity using the type definitions below.\n\n"
            "Entity type definitions:\n"
            "- person: Person names (politicians, athletes, authors, scientists)\n"
            "- organization: Organizations, companies, teams, institutions, agencies\n"
            "- location: Geographic locations, countries, cities, regions\n"
            "- building: Buildings, facilities, landmarks, airports, stadiums\n"
            "- art: Artworks, songs, films, books, creative works, albums\n"
            "- product: Commercial products, software, vehicles, technologies\n"
            "- event: Events, competitions, wars, festivals, ceremonies\n"
            "- other: Other named entities not fitting the above categories\n\n"
            "Text: {text}\n\n"
            "Output format:\n"
            '{{"entities": [{{"text": "exact span from text", "type": "TYPE", '
            '"start": <char_offset>, "end": <char_offset>}}], '
            '"relations": [], "events": []}}'
        ),
    },
    "D_recall": {
        "description": "Recall-focused — emphasizes exhaustive extraction of borderline entities",
        "system": None,
        "user": (
            "Carefully read the text below and extract ALL named entities. "
            "Be thorough: include every entity that matches any of the given types, "
            "even if borderline.\n\n"
            "Text: {text}\n"
            "Entity types: " + FEWNERD_TYPES + "\n\n"
            "For each entity, provide the exact text span, type, and character offsets "
            "(start = first char index, end = index after last char).\n"
            "Output:\n"
            '{{"entities": [{{"text": "...", "type": "...", "start": <int>, "end": <int>}}], '
            '"relations": [], "events": []}}'
        ),
    },
}

TEMPLATE_ORDER = ["A_standard", "B_expert", "C_descriptive", "D_recall"]
SAMPLES_PER_TEMPLATE = 2


def build_chat_prompt(tokenizer, template_name, text):
    tmpl = TEMPLATES[template_name]
    messages = []
    if tmpl["system"]:
        messages.append({"role": "system", "content": tmpl["system"]})
    messages.append({"role": "user", "content": tmpl["user"].format(text=text)})
    return tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True, enable_thinking=False,
    )


def save_template_definitions(output_dir):
    defs = {}
    for name, tmpl in TEMPLATES.items():
        defs[name] = {
            "description": tmpl["description"],
            "system": tmpl["system"],
            "user_template": tmpl["user"],
        }
    path = os.path.join(output_dir, "template_definitions.json")
    with open(path, "w") as f:
        json.dump(defs, f, indent=2, ensure_ascii=False)
    print(f"Template definitions saved to {path}", flush=True)


# ============================================================
# Sampling Phase
# ============================================================

def run_sampling(args):
    from vllm import LLM, SamplingParams
    from vllm.sampling_params import StructuredOutputsParams
    from transformers import AutoTokenizer
    from sampling import UIE_JSON_SCHEMA, parse_extraction_output, realign_spans

    # Load data
    data_path = os.path.join(args.data_dir, "test.json")
    instances = []
    with open(data_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            if obj.get("entities"):
                instances.append(obj)
    if args.num_instances > 0:
        instances = instances[:args.num_instances]
    print(f"Loaded {len(instances)} instances (with gold entities)", flush=True)

    # Init vLLM
    print(f"Loading model: {args.model_path}", flush=True)
    llm = LLM(
        model=args.model_path,
        tensor_parallel_size=1,
        max_model_len=2048,
        gpu_memory_utilization=0.88,
        enforce_eager=True,
        seed=args.seed,
    )
    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
    guided = StructuredOutputsParams(json=UIE_JSON_SCHEMA)
    print("Model ready.", flush=True)

    os.makedirs(args.output_dir, exist_ok=True)
    save_template_definitions(args.output_dir)

    def do_sample(template_name, n_samples, temperature, seed_val):
        prompts = [build_chat_prompt(tokenizer, template_name, inst["text"])
                   for inst in instances]
        params = SamplingParams(
            n=n_samples,
            temperature=temperature,
            max_tokens=512,
            structured_outputs=guided,
            seed=seed_val if temperature > 0 else None,
            logprobs=1,
        )
        t0 = time.time()
        outputs = llm.generate(prompts, params)
        dt = time.time() - t0
        print(f"  {template_name} n={n_samples} T={temperature} → {dt:.1f}s "
              f"({len(instances)*n_samples} samples)", flush=True)

        all_samples = []
        for i, out in enumerate(outputs):
            src = instances[i]["text"]
            samps = []
            for comp in out.outputs:
                p = parse_extraction_output(comp.text)
                p = realign_spans(p, src)
                n_toks = len(comp.token_ids)
                clp = comp.cumulative_logprob if comp.cumulative_logprob is not None else 0.0
                p["cumulative_logprob"] = clp
                p["n_tokens"] = n_toks
                p["mean_logprob"] = clp / max(n_toks, 1)
                if comp.logprobs:
                    tok_lps, tok_txts = [], []
                    for j, tok_lp in enumerate(comp.logprobs):
                        tid = comp.token_ids[j]
                        if tid in tok_lp:
                            tok_lps.append(tok_lp[tid].logprob)
                            tok_txts.append(tok_lp[tid].decoded_token)
                        else:
                            best = min(tok_lp.values(), key=lambda x: x.rank)
                            tok_lps.append(best.logprob)
                            tok_txts.append(best.decoded_token)
                    p["token_logprobs"] = tok_lps
                    p["token_texts"] = tok_txts
                samps.append(p)
            all_samples.append(samps)
        return all_samples

    def write_instances(samples_list, greedy_list, path, extra_fn=None):
        with open(path, "w") as f:
            for i, inst in enumerate(instances):
                gold = {"entities": inst.get("entities", []),
                        "relations": inst.get("relations", []),
                        "events": inst.get("events", [])}
                rec = {
                    "id": inst.get("id", str(i)),
                    "text": inst["text"],
                    "gold": gold,
                    "samples": samples_list[i],
                    "greedy": greedy_list[i][0],
                    "logprobs": [s.get("mean_logprob", 0.0) for s in samples_list[i]],
                }
                if extra_fn:
                    rec.update(extra_fn(i))
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    # --- Greedy ---
    print("\n--- Greedy (A_standard, T=0) ---", flush=True)
    greedy = do_sample("A_standard", 1, 0.0, None)

    # --- Single template baseline: A × 8 ---
    print("\n--- Single Template Baseline (A×8, T=1.0) ---", flush=True)
    single = do_sample("A_standard", 8, 1.0, args.seed)
    write_instances(single, greedy,
                    os.path.join(args.output_dir, "single_template_samples.jsonl"))
    print("Saved single_template_samples.jsonl", flush=True)

    # --- Multi template: 4 × 2 ---
    print("\n--- Multi Template (4×2, T=1.0) ---", flush=True)
    per_tmpl = {}
    for tn in TEMPLATE_ORDER:
        per_tmpl[tn] = do_sample(tn, SAMPLES_PER_TEMPLATE, 1.0, args.seed)

    # Save per-template files
    for tn in TEMPLATE_ORDER:
        tp = os.path.join(args.output_dir, f"template_{tn}_samples.jsonl")
        with open(tp, "w") as f:
            for i, inst in enumerate(instances):
                gold = {"entities": inst.get("entities", []),
                        "relations": inst.get("relations", []),
                        "events": inst.get("events", [])}
                f.write(json.dumps({
                    "id": inst.get("id", str(i)),
                    "text": inst["text"],
                    "gold": gold,
                    "samples": per_tmpl[tn][i],
                    "template": tn,
                }, ensure_ascii=False) + "\n")
        print(f"Saved template_{tn}_samples.jsonl", flush=True)

    # Merge multi-template samples
    labels = [tn for tn in TEMPLATE_ORDER for _ in range(SAMPLES_PER_TEMPLATE)]
    merged = []
    for i in range(len(instances)):
        m = []
        for tn in TEMPLATE_ORDER:
            m.extend(per_tmpl[tn][i])
        merged.append(m)

    write_instances(merged, greedy,
                    os.path.join(args.output_dir, "multi_template_samples.jsonl"),
                    extra_fn=lambda i: {"template_labels": labels})
    print("Saved multi_template_samples.jsonl", flush=True)
    print(f"\nSampling complete! Output: {args.output_dir}", flush=True)


# ============================================================
# Analysis Phase
# ============================================================

def entity_set(sample):
    return {(e["start"], e["end"], e["type"]) for e in sample.get("entities", [])}


def compute_f1(pred_set, gold_set):
    if not gold_set and not pred_set:
        return 1.0
    if not pred_set or not gold_set:
        return 0.0
    tp = len(pred_set & gold_set)
    p = tp / len(pred_set)
    r = tp / len(gold_set)
    return 2 * p * r / (p + r) if (p + r) > 0 else 0.0


def compute_pr(pred_set, gold_set):
    if not gold_set and not pred_set:
        return 1.0, 1.0
    if not pred_set:
        return 0.0, 0.0
    if not gold_set:
        return 0.0, 0.0
    tp = len(pred_set & gold_set)
    return tp / len(pred_set), tp / len(gold_set)


def weighted_construction(samples, threshold, weights=None):
    entity_counts = defaultdict(float)
    N = len(samples)
    for i, s in enumerate(samples):
        w = weights[i] if weights is not None else 1.0
        seen = set()
        for e in s.get("entities", []):
            key = (e["start"], e["end"], e["type"])
            if key not in seen:
                entity_counts[key] += w
                seen.add(key)
    total_weight = sum(weights) if weights is not None else N
    return {k for k, c in entity_counts.items() if c / total_weight >= threshold}


def get_lp_weights(samples):
    lps = [s.get("mean_logprob", -1.0) for s in samples]
    mx = max(lps) if lps else 0.0
    return [np.exp(lp - mx) for lp in lps]


def get_vc_weights(samples):
    ec = defaultdict(int)
    for s in samples:
        for e in s.get("entities", []):
            ec[(e["start"], e["end"], e["type"])] += 1
    ws = []
    for s in samples:
        ents = [(e["start"], e["end"], e["type"]) for e in s.get("entities", [])]
        ws.append(float(np.mean([ec[k] for k in ents])) if ents else 0.0)
    return ws


def compute_construction_metrics(instances, method):
    f1s, ps, rs = [], [], []
    for inst in instances:
        samples = inst["samples"]
        N = len(samples)
        gold = entity_set(inst["gold"])
        if method == "greedy":
            pred = entity_set(inst["greedy"])
        elif method == "majority_vote":
            pred = weighted_construction(samples, 0.5)
        elif method == "theta2n":
            pred = weighted_construction(samples, 2 / N)
        elif method == "lp_weighted":
            pred = weighted_construction(samples, 2 / N, get_lp_weights(samples))
        elif method == "vc_weighted":
            pred = weighted_construction(samples, 2 / N, get_vc_weights(samples))
        else:
            raise ValueError(method)
        f1s.append(compute_f1(pred, gold))
        p, r = compute_pr(pred, gold)
        ps.append(p)
        rs.append(r)
    return {
        "f1": float(np.mean(f1s)),
        "precision": float(np.mean(ps)),
        "recall": float(np.mean(rs)),
        "f1_list": f1s,
    }


def jaccard(a, b):
    if not a and not b:
        return 1.0
    u = a | b
    return len(a & b) / len(u) if u else 1.0


def compute_diversity(instances, template_labels=None):
    d = {"unique_entities": [], "pairwise_jaccard": [],
         "cross_template_jaccard": [], "within_template_jaccard": []}
    for inst in instances:
        samples = inst["samples"]
        N = len(samples)
        all_e = set()
        for s in samples:
            all_e |= entity_set(s)
        d["unique_entities"].append(len(all_e))
        jvals = []
        for i in range(N):
            for j in range(i + 1, N):
                jvals.append(jaccard(entity_set(samples[i]), entity_set(samples[j])))
        d["pairwise_jaccard"].append(np.mean(jvals) if jvals else 1.0)
        if template_labels:
            labels = inst.get("template_labels", template_labels)
            cross, within = [], []
            for i in range(N):
                for j in range(i + 1, N):
                    jv = jaccard(entity_set(samples[i]), entity_set(samples[j]))
                    (within if labels[i] == labels[j] else cross).append(jv)
            if cross:
                d["cross_template_jaccard"].append(np.mean(cross))
            if within:
                d["within_template_jaccard"].append(np.mean(within))
    return {k: float(np.mean(v)) if v else None for k, v in d.items()}


def bootstrap_test(f1a, f1b, n_boot=10000, seed=42):
    rng = np.random.RandomState(seed)
    n = len(f1a)
    a, b = np.array(f1a), np.array(f1b)
    obs = float(np.mean(b) - np.mean(a))
    count = 0
    for _ in range(n_boot):
        idx = rng.randint(0, n, n)
        if np.mean(b[idx]) - np.mean(a[idx]) <= 0:
            count += 1
    return obs, count / n_boot


def run_analysis(args):
    sp = os.path.join(args.output_dir, "single_template_samples.jsonl")
    mp = os.path.join(args.output_dir, "multi_template_samples.jsonl")
    single = [json.loads(l) for l in open(sp) if l.strip()]
    multi = [json.loads(l) for l in open(mp) if l.strip()]
    print(f"Loaded — Single: {len(single)}, Multi: {len(multi)} instances", flush=True)

    methods = ["greedy", "majority_vote", "theta2n", "lp_weighted", "vc_weighted"]
    report = {"n_instances": len(single), "construction_f1": {}, "diversity": {},
              "bootstrap": {}, "per_template": {}}

    # --- Construction F1 ---
    print(f"\n{'Method':<18} {'Single':>8} {'Multi':>8} {'Δ':>8} {'p':>8}", flush=True)
    print("-" * 54, flush=True)
    for m in methods:
        sm = compute_construction_metrics(single, m)
        mm = compute_construction_metrics(multi, m)
        delta = mm["f1"] - sm["f1"]
        if m != "greedy":
            _, p = bootstrap_test(sm["f1_list"], mm["f1_list"])
            ps = f"{p:.4f}"
            report["bootstrap"][m] = {"diff": delta, "p": p}
        else:
            ps = "—"
        print(f"{m:<18} {sm['f1']:>8.4f} {mm['f1']:>8.4f} {delta:>+8.4f} {ps:>8}", flush=True)
        report["construction_f1"][m] = {
            "single": {"f1": sm["f1"], "P": sm["precision"], "R": sm["recall"]},
            "multi":  {"f1": mm["f1"], "P": mm["precision"], "R": mm["recall"]},
            "delta": delta,
        }

    # --- Diversity ---
    labels = [tn for tn in TEMPLATE_ORDER for _ in range(SAMPLES_PER_TEMPLATE)]
    sd = compute_diversity(single)
    md = compute_diversity(multi, labels)
    report["diversity"] = {"single": sd, "multi": md}

    print(f"\n{'Diversity Metric':<30} {'Single':>8} {'Multi':>8}", flush=True)
    print("-" * 48, flush=True)
    for k in ["unique_entities", "pairwise_jaccard"]:
        sv, mv = sd.get(k), md.get(k)
        if sv is not None and mv is not None:
            print(f"{k:<30} {sv:>8.4f} {mv:>8.4f}", flush=True)
    for k in ["cross_template_jaccard", "within_template_jaccard"]:
        mv = md.get(k)
        if mv is not None:
            print(f"{k:<30} {'—':>8} {mv:>8.4f}", flush=True)

    # --- Per-template quality ---
    print("\nPer-template quality (best-sample F1 / mean-sample F1):", flush=True)
    for tn in TEMPLATE_ORDER:
        tp = os.path.join(args.output_dir, f"template_{tn}_samples.jsonl")
        if not os.path.exists(tp):
            continue
        ti = [json.loads(l) for l in open(tp) if l.strip()]
        best_f1s, mean_f1s = [], []
        for inst in ti:
            gold = entity_set(inst["gold"])
            sample_f1s = [compute_f1(entity_set(s), gold) for s in inst["samples"]]
            best_f1s.append(max(sample_f1s))
            mean_f1s.append(np.mean(sample_f1s))
        report["per_template"][tn] = {
            "best_sample_f1": float(np.mean(best_f1s)),
            "mean_sample_f1": float(np.mean(mean_f1s)),
        }
        print(f"  {tn}: best={np.mean(best_f1s):.4f}  mean={np.mean(mean_f1s):.4f}", flush=True)

    # --- Cross-template agreement rate ---
    print("\nCross-template agreement rate:", flush=True)
    agree_rates = {}
    for i, tn_i in enumerate(TEMPLATE_ORDER):
        for j, tn_j in enumerate(TEMPLATE_ORDER):
            if j <= i:
                continue
            agreements = []
            for inst in multi:
                si = inst["samples"][i * SAMPLES_PER_TEMPLATE:(i + 1) * SAMPLES_PER_TEMPLATE]
                sj = inst["samples"][j * SAMPLES_PER_TEMPLATE:(j + 1) * SAMPLES_PER_TEMPLATE]
                ents_i = set()
                for s in si:
                    ents_i |= entity_set(s)
                ents_j = set()
                for s in sj:
                    ents_j |= entity_set(s)
                agreements.append(jaccard(ents_i, ents_j))
            rate = float(np.mean(agreements))
            agree_rates[f"{tn_i}_vs_{tn_j}"] = rate
            print(f"  {tn_i} vs {tn_j}: {rate:.4f}", flush=True)
    report["cross_template_agreement"] = agree_rates

    # Save report
    rp = os.path.join(args.output_dir, "b3_report.json")
    with open(rp, "w") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"\nFull report: {rp}", flush=True)

    # --- Conclusion ---
    mv_d = report["construction_f1"]["majority_vote"]["delta"]
    mv_p = report["bootstrap"].get("majority_vote", {}).get("p", 1.0)
    t2n_d = report["construction_f1"]["theta2n"]["delta"]
    t2n_p = report["bootstrap"].get("theta2n", {}).get("p", 1.0)
    sj = sd.get("pairwise_jaccard", 0)
    mj = md.get("pairwise_jaccard", 0)

    print("\n" + "=" * 54, flush=True)
    print("CONCLUSION", flush=True)
    print("=" * 54, flush=True)
    print(f"Diversity: pairwise Jaccard  single={sj:.4f}  multi={mj:.4f}", flush=True)
    if mj < sj:
        print(f"  Multi-template is MORE diverse (lower Jaccard by {sj-mj:.4f})", flush=True)
    else:
        print(f"  Multi-template is NOT more diverse", flush=True)
    print(f"majority_vote F1: delta={mv_d:+.4f}  p={mv_p:.4f}", flush=True)
    print(f"theta2n F1:       delta={t2n_d:+.4f}  p={t2n_p:.4f}", flush=True)
    if mv_d > 0 and mv_p < 0.05:
        print("Verdict: Multi-template SIGNIFICANTLY improves construction F1", flush=True)
    elif mv_d > 0:
        print("Verdict: Positive trend but NOT statistically significant", flush=True)
    else:
        print("Verdict: Multi-template does NOT improve construction F1", flush=True)
    print("=" * 54, flush=True)


# ============================================================
# Main
# ============================================================

def main():
    p = argparse.ArgumentParser(description="B3: Prompted Diversity Experiment")
    p.add_argument("--phase", choices=["sample", "analyze", "both"], default="both")
    p.add_argument("--model_path",
                   default="/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-exp021-merged")
    p.add_argument("--data_dir",
                   default="/root/autodl-tmp/struct_self_consist_ie/data/fewnerd")
    p.add_argument("--output_dir",
                   default="/root/autodl-tmp/struct_self_consist_ie/output/exp_b3_prompted_diversity")
    p.add_argument("--num_instances", type=int, default=3000,
                   help="Number of test instances (0 = all)")
    p.add_argument("--seed", type=int, default=123)
    args = p.parse_args()

    print(f"B3 Prompted Diversity | phase={args.phase} | n={args.num_instances} | seed={args.seed}",
          flush=True)

    if args.phase in ("sample", "both"):
        run_sampling(args)
    if args.phase in ("analyze", "both"):
        run_analysis(args)


if __name__ == "__main__":
    main()
