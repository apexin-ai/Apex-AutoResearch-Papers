"""
Cohen's kappa pairwise agreement + Fleiss' kappa for 8 models x 5 benchmarks.
Baseline condition: temperature=0.0, prompt_template=1, seed=42, ordering=1.
"""
import json
import os
import sys
from itertools import combinations
from collections import defaultdict

DATA_DIR = "./results/exp002"
OUTPUT_PATH = "./results/exp004_8model_analysis/cohens_kappa_pairwise.json"

MODEL_SHORTS = ["llama", "gemma", "mistral", "qwen", "olmo", "yi", "internlm", "deepseek"]
BENCHMARKS = ["mmlu", "arc", "gsm8k", "hellaswag", "math"]

BASELINE = {"temperature": 0.0, "prompt_template": 1, "seed": 42, "ordering": 1}


def load_baseline(model_short, benchmark):
    path = os.path.join(DATA_DIR, f"{model_short}_{benchmark}.jsonl")
    if not os.path.exists(path):
        return None
    items = {}
    with open(path) as f:
        for line in f:
            r = json.loads(line)
            if (r["temperature"] == BASELINE["temperature"]
                    and r["prompt_template"] == BASELINE["prompt_template"]
                    and r["seed"] == BASELINE["seed"]
                    and r["ordering"] == BASELINE["ordering"]):
                items[r["item_id"]] = r["correct"]
    return items


def cohens_kappa(labels_a, labels_b):
    n = len(labels_a)
    assert n == len(labels_b) and n > 0
    agree = sum(a == b for a, b in zip(labels_a, labels_b))
    po = agree / n
    p1_a = sum(labels_a) / n
    p1_b = sum(labels_b) / n
    p0_a = 1 - p1_a
    p0_b = 1 - p1_b
    pe = p1_a * p1_b + p0_a * p0_b
    if pe == 1.0:
        return 1.0, po, pe
    kappa = (po - pe) / (1 - pe)
    return kappa, po, pe


def fleiss_kappa(ratings_matrix):
    n_items = len(ratings_matrix)
    n_raters = len(ratings_matrix[0])
    if n_items == 0 or n_raters < 2:
        return None
    P_bar = 0.0
    p_cat = [0.0, 0.0]
    for row in ratings_matrix:
        n1 = sum(row)
        n0 = n_raters - n1
        P_bar += (n0 * (n0 - 1) + n1 * (n1 - 1)) / (n_raters * (n_raters - 1))
        p_cat[0] += n0
        p_cat[1] += n1
    P_bar /= n_items
    total_ratings = n_items * n_raters
    p_cat[0] /= total_ratings
    p_cat[1] /= total_ratings
    Pe = p_cat[0] ** 2 + p_cat[1] ** 2
    if Pe == 1.0:
        return 1.0
    return (P_bar - Pe) / (1 - Pe)


def get_model_display_name(short):
    names = {
        "llama": "Llama-3.1-8B",
        "gemma": "Gemma-2-9B",
        "mistral": "Mistral-7B",
        "qwen": "Qwen3-8B",
        "olmo": "OLMo-2-7B",
        "yi": "Yi-1.5-9B",
        "internlm": "InternLM2.5-7B",
        "deepseek": "DeepSeek-7B",
    }
    return names.get(short, short)


def main():
    results = {
        "method": "Cohen's kappa",
        "condition": "baseline (T=0, P=1, S=42, O=1)",
        "benchmarks": {}
    }
    summary_rows = []

    for bm in BENCHMARKS:
        model_data = {}
        for ms in MODEL_SHORTS:
            data = load_baseline(ms, bm)
            if data and len(data) > 0:
                model_data[ms] = data

        available_models = sorted(model_data.keys())
        n_models = len(available_models)
        print(f"\n{'='*60}")
        print(f"Benchmark: {bm.upper()} -- {n_models} models: {', '.join(get_model_display_name(m) for m in available_models)}")

        common_items = set(model_data[available_models[0]].keys())
        for ms in available_models[1:]:
            common_items &= set(model_data[ms].keys())
        common_items = sorted(common_items)
        print(f"Common items: {len(common_items)}")

        pairs = []
        for ma, mb in combinations(available_models, 2):
            labels_a = [model_data[ma][item] for item in common_items]
            labels_b = [model_data[mb][item] for item in common_items]
            kappa, po, pe = cohens_kappa(labels_a, labels_b)
            pairs.append({
                "model_a": get_model_display_name(ma),
                "model_b": get_model_display_name(mb),
                "kappa": round(kappa, 4),
                "po": round(po, 4),
                "pe": round(pe, 4),
            })

        kappas = [p["kappa"] for p in pairs]
        mean_k = sum(kappas) / len(kappas)
        min_k = min(kappas)
        max_k = max(kappas)

        ratings_matrix = []
        for item in common_items:
            row = [model_data[ms][item] for ms in available_models]
            ratings_matrix.append(row)
        fk = fleiss_kappa(ratings_matrix)

        results["benchmarks"][bm] = {
            "n_models": n_models,
            "n_pairs": len(pairs),
            "n_items": len(common_items),
            "mean_kappa": round(mean_k, 4),
            "min_kappa": round(min_k, 4),
            "max_kappa": round(max_k, 4),
            "fleiss_kappa": round(fk, 4) if fk is not None else None,
            "pairs": sorted(pairs, key=lambda x: x["kappa"]),
        }
        summary_rows.append((bm, n_models, len(common_items), len(pairs),
                             mean_k, min_k, max_k, fk))

        sorted_pairs = sorted(pairs, key=lambda x: x["kappa"])
        print(f"  Mean k={mean_k:.4f}, Min k={min_k:.4f}, Max k={max_k:.4f}, Fleiss k={fk:.4f}")
        print(f"  Lowest 3:")
        for p in sorted_pairs[:3]:
            print(f"    {p['model_a']:>16s} x {p['model_b']:<16s}  k={p['kappa']:.4f}  po={p['po']:.4f}")
        print(f"  Highest 3:")
        for p in sorted_pairs[-3:]:
            print(f"    {p['model_a']:>16s} x {p['model_b']:<16s}  k={p['kappa']:.4f}  po={p['po']:.4f}")

    print(f"\n{'='*60}")
    print(f"{'Benchmark':>12s} {'Models':>6s} {'Items':>6s} {'Pairs':>6s} {'Mean_k':>8s} {'Min_k':>8s} {'Max_k':>8s} {'Fleiss_k':>9s}")
    print("-" * 70)
    for row in summary_rows:
        bm, nm, ni, np_, mk, mink, maxk, fk = row
        print(f"{bm:>12s} {nm:>6d} {ni:>6d} {np_:>6d} {mk:>8.4f} {mink:>8.4f} {maxk:>8.4f} {fk:>9.4f}")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
