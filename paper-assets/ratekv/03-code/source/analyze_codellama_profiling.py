"""Analyze CodeLlama-7B hires profiling results: concentration, t1/t5, classification."""
import json
import sys
import math

REFERENCE = {
    "Qwen2.5-7B":     {"gqa": "7:1", "kv_heads": 112, "conc": 0.61, "t1t5": 0.57, "shape": "Spread"},
    "Qwen2.5-14B":    {"gqa": "5:1", "kv_heads": 384, "conc": 0.33, "t1t5": 0.68, "shape": "Flat"},
    "Yi-1.5-9B":      {"gqa": "8:1", "kv_heads": 192, "conc": 0.71, "t1t5": 0.90, "shape": "Spike"},
    "Llama-3.1-8B":   {"gqa": "4:1", "kv_heads": 256, "conc": 0.57, "t1t5": 0.85, "shape": "Spike"},
    "Mistral-7B-v0.3":{"gqa": "4:1", "kv_heads": 256, "conc": 0.24, "t1t5": 0.41, "shape": "Flat"},
    "Gemma-2-9B":     {"gqa": "2:1", "kv_heads": 336, "conc": 0.23, "t1t5": 0.38, "shape": "Flat"},
    "Pythia-1.4B":    {"gqa": "1:1", "kv_heads": 384, "conc": 0.24, "t1t5": 0.28, "shape": "Flat"},
}


def classify(conc, t1t5):
    """Paper classification rule (analysis.tex §5.2)."""
    if conc >= 0.50 and t1t5 <= 0.70:
        return "Spread"
    if t1t5 > 0.70 and conc >= 0.25:
        return "Spike"
    return "Flat"


def analyze(profiles_path):
    with open(profiles_path) as f:
        profiles = json.load(f)

    all_deltas = []
    layer_deltas = {}
    for l_str in sorted(profiles.keys(), key=int):
        l = int(l_str)
        layer_deltas[l] = []
        for h_str in sorted(profiles[l_str].keys(), key=int):
            d2 = profiles[l_str][h_str]["quantization"].get("2", 0.0)
            all_deltas.append((l, int(h_str), d2))
            layer_deltas[l].append(d2)

    total_heads = len(all_deltas)
    num_layers = max(l for l, _, _ in all_deltas) + 1
    num_kv_heads = total_heads // num_layers

    sorted_desc = sorted(all_deltas, key=lambda x: -x[2])
    n_top5 = max(1, int(total_heads * 0.05))

    total_sum = sum(x[2] for x in all_deltas)
    top5_sum = sum(x[2] for x in sorted_desc[:n_top5])
    concentration = top5_sum / total_sum if total_sum > 0 else 0

    top1_delta = sorted_desc[0][2] if sorted_desc else 0
    t1t5 = top1_delta / top5_sum if top5_sum > 0 else 0

    deltas_only = [x[2] for x in all_deltas]
    mean_d = sum(deltas_only) / len(deltas_only)
    var_d = sum((d - mean_d) ** 2 for d in deltas_only) / len(deltas_only)
    std_d = math.sqrt(var_d)
    cv = std_d / mean_d if mean_d > 0 else 0

    l0_deltas = layer_deltas.get(0, [0])
    l0_mean = sum(l0_deltas) / len(l0_deltas)
    other_means = []
    for l in range(1, num_layers):
        if l in layer_deltas and layer_deltas[l]:
            other_means.append(sum(layer_deltas[l]) / len(layer_deltas[l]))
    other_avg = sum(other_means) / len(other_means) if other_means else 0
    l0_ratio = l0_mean / other_avg if other_avg > 0 else float("inf")

    n_positive = sum(1 for d in deltas_only if d > 1e-6)

    shape = classify(concentration, t1t5)

    print("=" * 70)
    print("CodeLlama-7B Profiling Analysis")
    print("=" * 70)
    print(f"Architecture: {num_layers}L x {num_kv_heads}KV heads, MHA 1:1, {total_heads} total")
    print()

    print("--- Key Metrics ---")
    print(f"  Top-5% concentration:  {concentration:.4f}  (threshold: >=0.50 for Spread)")
    print(f"  t1/t5 ratio:           {t1t5:.4f}  (threshold: <=0.70 for Spread)")
    print(f"  Classification:        {shape}")
    print()

    print("--- Supporting Metrics ---")
    print(f"  Top-5% heads:          {n_top5}")
    print(f"  Total delta sum:       {total_sum:.4f}")
    print(f"  Top-5% delta sum:      {top5_sum:.4f}")
    print(f"  Top-1 delta:           {top1_delta:.6f}")
    print(f"  L0 dominance ratio:    {l0_ratio:.2f}x")
    print(f"  CV (delta 2-bit):      {cv:.4f}")
    print(f"  Heads with delta > 0:  {n_positive}/{total_heads}")
    print(f"  Mean delta:            {mean_d:.6f}")
    print(f"  Std delta:             {std_d:.6f}")
    print()

    print("--- Top-10 Sensitive Heads ---")
    for i, (l, h, d2) in enumerate(sorted_desc[:10]):
        frac = d2 / total_sum * 100 if total_sum > 0 else 0
        print(f"  #{i+1:2d}  L{l}H{h:2d}  delta={d2:+.6f}  ({frac:.1f}% of total)")
    print()

    print("--- Layer-wise Mean Delta (top-5 layers) ---")
    layer_means = [(l, sum(ds) / len(ds)) for l, ds in sorted(layer_deltas.items()) if ds]
    layer_means.sort(key=lambda x: -x[1])
    for l, m in layer_means[:5]:
        print(f"  Layer {l:2d}: mean={m:.6f}")
    print()

    # Cross-reference table
    print("=" * 70)
    print("Cross-Architecture Reference Table")
    print("=" * 70)
    print(f"{'Model':<20s} {'GQA':>5s} {'Heads':>6s} {'Conc':>6s} {'t1/t5':>6s} {'Shape':<8s}")
    print("-" * 55)
    for name, r in REFERENCE.items():
        print(f"{name:<20s} {r['gqa']:>5s} {r['kv_heads']:>6d} {r['conc']:>6.2f} {r['t1t5']:>6.2f} {r['shape']:<8s}")
    print("-" * 55)
    print(f"{'CodeLlama-7B':<20s} {'1:1':>5s} {total_heads:>6d} {concentration:>6.2f} {t1t5:>6.2f} {shape:<8s}  <-- NEW")
    print()

    # Prediction assessment
    print("=" * 70)
    print("Assessment")
    print("=" * 70)
    if shape == "Spread":
        print("  CodeLlama-7B is SPREAD — potential second Spread model!")
        print("  Next: run constrained MCKP to confirm benefit.")
    elif shape == "Spike":
        print("  CodeLlama-7B is SPIKE — single outlier dominates.")
        print("  MCKP unlikely to help (cf. Yi-1.5, Llama).")
    else:
        print("  CodeLlama-7B is FLAT — near-uniform sensitivity.")
        print("  MCKP unlikely to help (cf. Mistral, Gemma-2, Pythia).")
        if total_heads >= 512:
            print(f"  Note: {total_heads} heads → heavy dilution effect (cf. Qwen-14B 384→Flat).")

    return {
        "concentration": round(concentration, 4),
        "t1t5": round(t1t5, 4),
        "shape": shape,
        "total_heads": total_heads,
        "n_top5": n_top5,
        "cv": round(cv, 4),
        "l0_dominance": round(l0_ratio, 2),
        "top1_head": {"layer": sorted_desc[0][0], "head": sorted_desc[0][1], "delta": round(sorted_desc[0][2], 6)},
    }


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "artifacts/codellama_profiles_hires.json"
    result = analyze(path)
    out_path = "artifacts/codellama_classification_result.json"
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)
    print(f"\nSaved: {out_path}")
