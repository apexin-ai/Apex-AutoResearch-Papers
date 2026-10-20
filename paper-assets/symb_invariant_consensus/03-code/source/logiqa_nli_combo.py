#!/usr/bin/env python3
"""LogiQA NLI Combo: NLI verifier × 4 generators × 3 weights.

For each LogiQA problem:
  - NLI(premise=context, hypothesis=choice_text) → entailment prob per choice
  - Combined score = SC_votes[choice] + w * NLI_entailment_prob[choice]
  - Alphabetical tiebreaking: sorted(tied_candidates)[0]
  - McNemar exact test + BH correction
"""

import argparse, json, time, re, os
import numpy as np
from pathlib import Path
from collections import Counter
from scipy.stats import binomtest
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

CANONICAL = ["A", "B", "C", "D"]
WEIGHTS = [1, 3, 5]

GENERATORS = {
    "Mistral-7B": "/root/symb_invariant_consensus/results/exp049b_mistral_logiqa200/intermediates",
    "LLaMA-3.1-8B": "/root/symb_invariant_consensus/results/exp072b_llama8b_logiqa200/intermediates",
    "Qwen2.5-14B": "/root/symb_invariant_consensus/results/exp038_qwen25_14b_logiqa200/intermediates",
    "Qwen3-14B": "/root/symb_invariant_consensus/results/exp068_qwen3_logiqa200/intermediates",
}

VERIFIER_PATHS = {
    "deberta-large-mnli": "/root/autodl-tmp/models/deberta-large-mnli",
    "bart-large-mnli": "/root/autodl-tmp/models/bart-large-mnli",
    "roberta-large-mnli": "/root/autodl-tmp/models/roberta-large-mnli",
}


def normalize_answer(raw, choices):
    if not raw:
        return None
    raw = raw.strip()
    if raw in CANONICAL:
        return raw
    m = re.match(r'^([A-D])\b', raw)
    if m:
        return m.group(1)
    for i, ch in enumerate(choices):
        ch_text = re.sub(r'^[A-D]\.\s*', '', ch).strip()
        if raw.lower() == ch_text.lower() or raw.lower() == ch.lower():
            return CANONICAL[i]
    return None


def alpha_winner(score_dict):
    mx = max(score_dict.values())
    tied = sorted(c for c in CANONICAL if score_dict.get(c, 0) == mx)
    return tied[0]


def mcnemar_test(b, c):
    n = b + c
    if n == 0:
        return 1.0
    return binomtest(min(b, c), n, 0.5).pvalue


def bh_correct(tests):
    m = len(tests)
    if m == 0:
        return []
    sorted_tests = sorted(enumerate(tests), key=lambda x: x[1][1])
    adjusted = [0.0] * m
    prev = 1.0
    for rank_minus_1 in range(m - 1, -1, -1):
        orig_idx, (label, raw_p) = sorted_tests[rank_minus_1]
        rank = rank_minus_1 + 1
        adj = min(prev, raw_p * m / rank)
        adjusted[orig_idx] = adj
        prev = adj
    results = []
    for i, (label, raw_p) in enumerate(tests):
        results.append({
            "label": label,
            "raw_p": float(raw_p),
            "bh_adjusted_p": round(float(adjusted[i]), 6),
            "significant": bool(adjusted[i] < 0.05),
        })
    return results


def load_traces(trace_dir, max_problems=None):
    trace_dir = Path(trace_dir)
    files = sorted(trace_dir.glob("logiqa_*.json"))
    if max_problems:
        files = files[:max_problems]
    problems = []
    for tf in files:
        with open(tf) as f:
            problems.append(json.load(f))
    return problems


def run_nli_for_problems(model, tokenizer, problems, device):
    id2label = model.config.id2label
    ent_idx = None
    for idx, lbl in id2label.items():
        if "entail" in lbl.lower():
            ent_idx = int(idx)
            break
    if ent_idx is None:
        raise ValueError(f"Cannot find entailment label in {id2label}")
    print(f"  id2label: {id2label}, entailment_idx: {ent_idx}")

    nli_probs = {}
    for i, prob_data in enumerate(problems):
        pid = prob_data["problem"]["id"]
        ctx = prob_data["problem"]["context"]
        choices = prob_data["problem"]["choices"]
        choice_texts = [re.sub(r'^[A-D]\.\s*', '', ch).strip() for ch in choices]

        inputs = tokenizer(
            [ctx] * len(choice_texts), choice_texts,
            return_tensors="pt", truncation=True, max_length=512, padding=True
        ).to(device)
        with torch.no_grad():
            logits = model(**inputs).logits
        probs = torch.softmax(logits, dim=-1)
        ent = probs[:, ent_idx].cpu().numpy().tolist()

        nli_probs[pid] = {CANONICAL[j]: round(ent[j], 6) for j in range(len(choice_texts))}

        if (i + 1) % 50 == 0:
            print(f"  NLI progress: {i+1}/{len(problems)}")

    return nli_probs


def run_one_verifier(verifier_name, device, max_problems=None):
    model_path = VERIFIER_PATHS[verifier_name]
    print(f"\n{'='*60}")
    print(f"Verifier: {verifier_name}")
    print(f"Model: {model_path}")
    print(f"Device: {device}")

    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path).to(device).eval()

    ref_gen = list(GENERATORS.keys())[0]
    ref_traces = load_traces(GENERATORS[ref_gen], max_problems)
    n = len(ref_traces)
    print(f"Problems: {n}")

    t0 = time.time()
    nli_probs = run_nli_for_problems(model, tokenizer, ref_traces, device)
    nli_elapsed = time.time() - t0
    print(f"NLI inference: {nli_elapsed:.1f}s")

    gt = {p["problem"]["id"]: p["problem"]["answer"] for p in ref_traces}
    nli_correct_count = sum(1 for pid in nli_probs if alpha_winner(nli_probs[pid]) == gt[pid])
    nli_standalone_acc = nli_correct_count / n * 100

    del model
    torch.cuda.empty_cache()

    all_results = []
    all_tests_for_bh = []

    for gen_name, trace_dir in GENERATORS.items():
        gen_traces = load_traces(trace_dir, max_problems)

        sc_correct_list = []
        combo_results_by_w = {w: [] for w in WEIGHTS}

        for prob_data in gen_traces:
            pid = prob_data["problem"]["id"]
            choices = prob_data["problem"]["choices"]
            gold = gt[pid]
            traces = prob_data["sica_result"]["traces"]

            sc_votes = dict(Counter(
                a for t in traces
                if (a := normalize_answer(t["answer"], choices)) is not None
            ))
            sc_ans = alpha_winner({c: sc_votes.get(c, 0) for c in CANONICAL})
            sc_correct_list.append(sc_ans == gold)

            for w in WEIGHTS:
                combined = {c: sc_votes.get(c, 0) + w * nli_probs[pid].get(c, 0.0) for c in CANONICAL}
                combo_ans = alpha_winner(combined)
                combo_results_by_w[w].append(combo_ans == gold)

        sc_acc = sum(sc_correct_list) / n * 100
        sc_n = sum(sc_correct_list)

        gen_result = {
            "generator": gen_name,
            "verifier": verifier_name,
            "n": n,
            "sc_accuracy": round(sc_acc, 2),
            "sc_correct": sc_n,
            "nli_standalone_accuracy": round(nli_standalone_acc, 2),
            "nli_standalone_correct": nli_correct_count,
            "capability_gap_pp": round(nli_standalone_acc - sc_acc, 2),
            "combo": {},
        }

        for w in WEIGHTS:
            combo_correct = combo_results_by_w[w]
            combo_acc = sum(combo_correct) / n * 100
            combo_n = sum(combo_correct)
            delta = combo_acc - sc_acc
            b = sum(1 for s, c in zip(sc_correct_list, combo_correct) if not s and c)
            c_disc = sum(1 for s, c in zip(sc_correct_list, combo_correct) if s and not c)
            p_val = mcnemar_test(b, c_disc)

            gen_result["combo"][f"w{w}"] = {
                "accuracy": round(combo_acc, 2),
                "correct": combo_n,
                "delta_pp": round(delta, 2),
                "mcnemar_b": b,
                "mcnemar_c": c_disc,
                "mcnemar_p": round(p_val, 6),
            }
            all_tests_for_bh.append((f"{gen_name}_w{w}", p_val))

        all_results.append(gen_result)
        print(f"\n{gen_name}: SC={sc_acc:.2f}%, NLI={nli_standalone_acc:.2f}%, gap={nli_standalone_acc - sc_acc:+.2f}pp")
        for w in WEIGHTS:
            c = gen_result["combo"][f"w{w}"]
            print(f"  w={w}: {c['accuracy']:.2f}% (Δ={c['delta_pp']:+.2f}pp, p={c['mcnemar_p']:.6f})")

    bh_results = bh_correct(all_tests_for_bh)
    n_sig = sum(1 for r in bh_results if r["significant"])
    print(f"\n=== BH Correction ({len(bh_results)} tests) ===")
    for r in bh_results:
        star = "*" if r["significant"] else ""
        print(f"  {r['label']}: raw={r['raw_p']:.6f}, adj={r['bh_adjusted_p']:.6f} {star}")
    print(f"  {n_sig}/{len(bh_results)} significant (alpha=0.05)")

    return {
        "experiment": f"LogiQA NLI Combo - {verifier_name}",
        "verifier": verifier_name,
        "verifier_local_path": model_path,
        "dataset": "LogiQA-200",
        "n": n,
        "tiebreaking": "alphabetical (sorted(tied_candidates)[0])",
        "nli_inference_time_s": round(nli_elapsed, 1),
        "generators": all_results,
        "bh_correction": {
            "n_tests": len(bh_results),
            "alpha": 0.05,
            "n_significant": n_sig,
            "tests": bh_results,
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--verifier", required=True,
                        help="Verifier name or 'all' to run all three")
    parser.add_argument("--device", default="cuda:1")
    parser.add_argument("--output-dir", default="/root/symb_invariant_consensus/results")
    parser.add_argument("--max-problems", type=int, default=None)
    args = parser.parse_args()

    if args.verifier == "all":
        verifiers = list(VERIFIER_PATHS.keys())
    else:
        verifiers = [args.verifier]

    for v in verifiers:
        if v not in VERIFIER_PATHS:
            print(f"Unknown verifier: {v}. Available: {list(VERIFIER_PATHS.keys())}")
            return

    for v in verifiers:
        result = run_one_verifier(v, args.device, args.max_problems)
        short_name = v.replace("-mnli", "").replace("-large", "")
        out_path = os.path.join(args.output_dir, f"logiqa_nli_combo_{short_name}.json")
        os.makedirs(args.output_dir, exist_ok=True)
        with open(out_path, "w") as f:
            json.dump(result, f, indent=2)
        print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()
