import json
import os

FILES = {
    "Transformer": "/root/entrainment_gated_ft/results_v5/transformer/__root__autodl-tmp__models_1.3b__transformer_1.3B_baseline/samples_lambada_openai_2026-05-18T19-46-52.474119.jsonl",
    "GDN-pure": "/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/GDN-pure/samples/lambada_openai.jsonl",
    "GDN-h3-1": "/root/entrainment_gated_ft/lm_eval_clean/1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl",
    "RetNet-pure": "/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/RetNet-pure/samples/lambada_openai.jsonl",
    "RetNet-h3-1": "/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/RetNet-h3-1/samples/lambada_openai.jsonl",
    "HGRN2-pure": "/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/HGRN2-pure/samples/lambada_openai.jsonl",
    "HGRN2-h3-1": "/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/HGRN2-h3-1/samples/lambada_openai.jsonl",
}

def load_acc_by_docid(path):
    acc_map = {}
    with open(path) as f:
        for line in f:
            obj = json.loads(line)
            doc_id = obj["doc_id"]
            acc = int(obj["acc"]) if isinstance(obj["acc"], (int, float)) else int(float(obj["acc"]))
            acc_map[doc_id] = acc
    return acc_map

def jaccard(set_a, set_b):
    if len(set_a) == 0 and len(set_b) == 0:
        return 1.0
    intersection = len(set_a & set_b)
    union = len(set_a | set_b)
    return intersection / union if union > 0 else 0.0

# Load all
data = {}
for name, path in FILES.items():
    data[name] = load_acc_by_docid(path)
    print(f"{name}: {sum(data[name].values())}/{len(data[name])} correct ({sum(data[name].values())/len(data[name])*100:.2f}%)")

# Correct sets
correct_sets = {}
for name, acc_map in data.items():
    correct_sets[name] = set(doc_id for doc_id, acc in acc_map.items() if acc == 1)

n_total = len(data["Transformer"])
trans_correct = correct_sets["Transformer"]

# Agreement rates and Jaccard with Transformer
models = ["GDN-pure", "GDN-h3-1", "RetNet-pure", "RetNet-h3-1", "HGRN2-pure", "HGRN2-h3-1"]

print("\n=== Agreement with Transformer ===")
agreement_rates = {}
correct_set_jaccard = {}
for m in models:
    both_correct = len(trans_correct & correct_sets[m])
    both_wrong = n_total - len(trans_correct | correct_sets[m])
    agreement = (both_correct + both_wrong) / n_total
    j = jaccard(trans_correct, correct_sets[m])
    agreement_rates[f"{m}_vs_Transformer"] = round(agreement, 4)
    correct_set_jaccard[f"{m}_vs_Transformer"] = round(j, 4)
    print(f"{m} vs Transformer: agreement={agreement:.4f}, J(correct)={j:.4f}, both_correct={both_correct}, both_wrong={both_wrong}")

# Pairwise Jaccard among hybrids and pures
print("\n=== Pairwise Jaccard (correct sets) ===")
pairwise_jaccard = {}
for i, m1 in enumerate(models):
    for m2 in models[i+1:]:
        j = jaccard(correct_sets[m1], correct_sets[m2])
        key = f"{m1}_vs_{m2}"
        pairwise_jaccard[key] = round(j, 4)
        print(f"  {key}: {j:.4f}")

# Key comparison: does h3-1 move closer to Transformer than pure?
print("\n=== Key Comparison: Does h3-1 move closer to Transformer? ===")
for arch in ["GDN", "RetNet", "HGRN2"]:
    pure_j = correct_set_jaccard[f"{arch}-pure_vs_Transformer"]
    h3_j = correct_set_jaccard[f"{arch}-h3-1_vs_Transformer"]
    delta = h3_j - pure_j
    direction = "CLOSER" if delta > 0 else "FARTHER" if delta < 0 else "SAME"
    print(f"  {arch}: pure J={pure_j:.4f}, h3-1 J={h3_j:.4f}, delta={delta:+.4f} ({direction})")

# Additional: unique correct analysis
print("\n=== Unique correct analysis ===")
for m in models:
    only_m = correct_sets[m] - trans_correct
    only_trans = trans_correct - correct_sets[m]
    shared = trans_correct & correct_sets[m]
    print(f"  {m}: shared_with_trans={len(shared)}, only_{m}={len(only_m)}, only_trans={len(only_trans)}")

# Build conclusion
conclusions = []
for arch in ["GDN", "RetNet", "HGRN2"]:
    pure_j = correct_set_jaccard[f"{arch}-pure_vs_Transformer"]
    h3_j = correct_set_jaccard[f"{arch}-h3-1_vs_Transformer"]
    delta = h3_j - pure_j
    if delta > 0.01:
        conclusions.append(f"{arch}-h3-1 moves toward Transformer (J delta={delta:+.4f})")
    elif delta < -0.01:
        conclusions.append(f"{arch}-h3-1 moves away from Transformer (J delta={delta:+.4f})")
    else:
        conclusions.append(f"{arch}-h3-1 shows minimal change vs Transformer (J delta={delta:+.4f})")

conclusion_text = "; ".join(conclusions)

# Save results
result = {
    "transformer_acc": round(sum(data["Transformer"].values()) / len(data["Transformer"]), 4),
    "model_accuracies": {name: round(sum(acc_map.values()) / len(acc_map), 4) for name, acc_map in data.items()},
    "agreement_rates": agreement_rates,
    "correct_set_jaccard": correct_set_jaccard,
    "pairwise_jaccard": pairwise_jaccard,
    "unique_correct": {
        m: {
            "shared_with_transformer": len(correct_sets[m] & trans_correct),
            f"only_{m}": len(correct_sets[m] - trans_correct),
            "only_transformer": len(trans_correct - correct_sets[m]),
        } for m in models
    },
    "key_comparison": {
        arch: {
            "pure_J_vs_transformer": correct_set_jaccard[f"{arch}-pure_vs_Transformer"],
            "h3_1_J_vs_transformer": correct_set_jaccard[f"{arch}-h3-1_vs_Transformer"],
            "delta": round(correct_set_jaccard[f"{arch}-h3-1_vs_Transformer"] - correct_set_jaccard[f"{arch}-pure_vs_Transformer"], 4),
        } for arch in ["GDN", "RetNet", "HGRN2"]
    },
    "conclusion": conclusion_text,
}

out_path = "/root/entrainment_gated_ft/transformer_baseline_analysis.json"
with open(out_path, "w") as f:
    json.dump(result, f, indent=2)
print(f"\nSaved to {out_path}")
