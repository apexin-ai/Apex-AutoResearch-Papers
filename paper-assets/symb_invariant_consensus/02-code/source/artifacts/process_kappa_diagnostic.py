import json, os, numpy as np
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import roc_auc_score
from scipy.stats import fisher_exact

DATA_DIR = "/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates"
OUT_DIR = "/root/symb_invariant_consensus/results/process_kappa_diagnostic"
os.makedirs(OUT_DIR, exist_ok=True)

records = []
for i in range(204):
    path = os.path.join(DATA_DIR, f"folio_{i}.json")
    with open(path) as f:
        d = json.load(f)

    gold = d["problem"]["answer"]
    traces = d["sica_result"]["traces"]
    sica_answer = d["sica_result"]["answer"]

    texts = [t["trace"] for t in traces]
    answers = [t["answer"] for t in traces]

    # SC vote = majority of non-empty answers
    valid_answers = [a for a in answers if a.strip()]
    if valid_answers:
        cnt = Counter(valid_answers)
        sc_vote = cnt.most_common(1)[0][0]
    else:
        sc_vote = ""

    # process-kappa: mean pairwise cosine similarity of TF-IDF vectors
    non_empty = [t for t in texts if t.strip()]
    if len(non_empty) >= 2:
        vect = TfidfVectorizer(max_features=5000)
        tfidf = vect.fit_transform(non_empty)
        sim_matrix = cosine_similarity(tfidf)
        n = sim_matrix.shape[0]
        upper = sim_matrix[np.triu_indices(n, k=1)]
        kappa = float(np.mean(upper))
    else:
        kappa = 1.0

    records.append({
        "id": f"folio_{i}",
        "gold": gold,
        "sc_vote": sc_vote,
        "sc_correct": int(sc_vote == gold),
        "sica_answer": sica_answer,
        "sica_correct": int(sica_answer == gold),
        "process_kappa": kappa,
        "n_traces": len(traces),
        "n_valid_answers": len(valid_answers),
    })

records.sort(key=lambda r: r["process_kappa"])

# --- Step 2: Tercile analysis ---
n = len(records)
t1, t2 = n // 3, 2 * n // 3
terciles = {
    "low": records[:t1],
    "mid": records[t1:t2],
    "high": records[t2:],
}

tercile_table = {}
for name, group in terciles.items():
    sc_acc = np.mean([r["sc_correct"] for r in group])
    sica_acc = np.mean([r["sica_correct"] for r in group])
    mean_k = np.mean([r["process_kappa"] for r in group])
    tercile_table[name] = {
        "n": len(group),
        "sc_accuracy": round(float(sc_acc), 4),
        "sica_accuracy": round(float(sica_acc), 4),
        "mean_kappa": round(float(mean_k), 4),
    }

print("=== Tercile Analysis ===")
print(f"{'Tercile':<8} {'n':>4} {'SC Acc':>8} {'SICA Acc':>9} {'Mean κ':>8}")
for name in ["low", "mid", "high"]:
    t = tercile_table[name]
    print(f"{name:<8} {t['n']:>4} {t['sc_accuracy']:>8.4f} {t['sica_accuracy']:>9.4f} {t['mean_kappa']:>8.4f}")

# --- Step 3: Abstention curve ---
records_desc = sorted(records, key=lambda r: -r["process_kappa"])
abstention_curve = {}
for pct in [10, 20, 30, 40, 50]:
    drop = int(len(records_desc) * pct / 100)
    remaining = records_desc[drop:]
    sc_acc = np.mean([r["sc_correct"] for r in remaining]) if remaining else 0
    sica_acc = np.mean([r["sica_correct"] for r in remaining]) if remaining else 0
    abstention_curve[f"drop_{pct}pct"] = {
        "coverage": round(len(remaining) / len(records_desc), 4),
        "n_remaining": len(remaining),
        "sc_accuracy": round(float(sc_acc), 4),
        "sica_accuracy": round(float(sica_acc), 4),
    }

print("\n=== Abstention Curve (drop high-κ) ===")
print(f"{'Drop%':>6} {'Coverage':>9} {'n':>4} {'SC Acc':>8} {'SICA Acc':>9}")
for pct in [10, 20, 30, 40, 50]:
    a = abstention_curve[f"drop_{pct}pct"]
    print(f"{pct:>5}% {a['coverage']:>9.4f} {a['n_remaining']:>4} {a['sc_accuracy']:>8.4f} {a['sica_accuracy']:>9.4f}")

# --- Step 4: Fisher exact test (high-κ vs low-κ SC accuracy) ---
low_g = terciles["low"]
high_g = terciles["high"]
# 2x2 table: [[low_correct, low_wrong], [high_correct, high_wrong]]
low_correct = sum(r["sc_correct"] for r in low_g)
low_wrong = len(low_g) - low_correct
high_correct = sum(r["sc_correct"] for r in high_g)
high_wrong = len(high_g) - high_correct
table = [[low_correct, low_wrong], [high_correct, high_wrong]]
odds_ratio, p_value = fisher_exact(table)
print(f"\n=== Fisher Exact Test (low-κ vs high-κ SC accuracy) ===")
print(f"Low-κ:  {low_correct}/{len(low_g)} correct")
print(f"High-κ: {high_correct}/{len(high_g)} correct")
print(f"Odds ratio: {odds_ratio:.4f}, p-value: {p_value:.6f}")

# --- Step 5: AUROC ---
kappas = [r["process_kappa"] for r in records]
sc_incorrect = [1 - r["sc_correct"] for r in records]
if len(set(sc_incorrect)) > 1:
    auroc = roc_auc_score(sc_incorrect, kappas)
else:
    auroc = float("nan")
print(f"\n=== AUROC (process-κ predicting SC error) ===")
print(f"AUROC: {auroc:.4f}")

# --- Baseline stats ---
overall_sc = np.mean([r["sc_correct"] for r in records])
overall_sica = np.mean([r["sica_correct"] for r in records])
print(f"\n=== Baselines ===")
print(f"Overall SC accuracy:   {overall_sc:.4f} ({int(overall_sc*204)}/204)")
print(f"Overall SICA accuracy: {overall_sica:.4f} ({int(overall_sica*204)}/204)")

# --- Save all results ---
results = {
    "overall": {
        "sc_accuracy": round(float(overall_sc), 4),
        "sica_accuracy": round(float(overall_sica), 4),
        "n": len(records),
    },
    "tercile_table": tercile_table,
    "abstention_curve": abstention_curve,
    "fisher_test": {
        "table_2x2": table,
        "odds_ratio": round(float(odds_ratio), 4),
        "p_value": round(float(p_value), 6),
    },
    "auroc": round(float(auroc), 4),
    "per_question": records,
}

out_path = os.path.join(OUT_DIR, "results.json")
with open(out_path, "w") as f:
    json.dump(results, f, indent=2)
print(f"\nResults saved to {out_path}")
