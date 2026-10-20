import json, os, glob
from collections import Counter

def load_and_analyze(intermediates_dir, label):
    """Load all intermediate files, compute per-problem agreement and answers."""
    problems = []
    for fpath in sorted(glob.glob(os.path.join(intermediates_dir, "*.json"))):
        try:
            d = json.load(open(fpath))
        except:
            continue
        gt = d["problem"]["answer"]
        sica_answer = d["sica_result"]["answer"]
        answer_counts = d["sica_result"].get("answer_counts", {})
        
        # Compute from answer_counts
        if answer_counts:
            K = sum(answer_counts.values())
            max_count = max(answer_counts.values())
            agreement = max_count / K if K > 0 else 0
            # SC answer = most frequent, alphabetical tiebreak
            sc_answer = sorted(answer_counts.items(), key=lambda x: (-x[1], x[0]))[0][0]
        else:
            # Fallback: compute from traces
            traces = d["sica_result"].get("traces", [])
            answers = [t["answer"] for t in traces if t.get("answer")]
            if not answers:
                continue
            counts = Counter(answers)
            K = len(answers)
            max_count = max(counts.values())
            agreement = max_count / K
            sc_answer = sorted(counts.items(), key=lambda x: (-x[1], x[0]))[0][0]
        
        problems.append({
            "id": d["problem"]["id"],
            "gt": gt,
            "sc_answer": sc_answer,
            "sica_answer": sica_answer,
            "agreement": agreement,
            "K": K
        })
    return problems

def drc_sweep(problems, taus, verifier_key="sica_answer"):
    """Sweep τ values for DRC."""
    results = {}
    for tau in taus:
        correct = 0
        routed = 0
        for p in problems:
            if p["agreement"] >= tau:
                pred = p["sc_answer"]
            else:
                pred = p[verifier_key]
                routed += 1
            if pred == p["gt"]:
                correct += 1
        n = len(problems)
        acc = correct / n * 100 if n > 0 else 0
        route_frac = routed / n * 100 if n > 0 else 0
        sc_coverage = 100 - route_frac
        results[tau] = {
            "accuracy": round(acc, 2),
            "routed_pct": round(route_frac, 1),
            "sc_coverage_pct": round(sc_coverage, 1),
            "n": n,
            "correct": correct,
            "routed": routed
        }
    return results

def print_table(label, results, taus, sc_acc, sica_acc):
    print(f"\n{'='*70}")
    print(f"  DRC τ Sensitivity: {label}")
    print(f"  SC baseline: {sc_acc:.2f}%  |  SICA (verifier proxy): {sica_acc:.2f}%")
    print(f"{'='*70}")
    print(f"  {'τ':>5}  {'Accuracy':>10}  {'Routed→V':>10}  {'SC Cov.':>10}  {'Δ vs SC':>10}")
    print(f"  {'-'*5}  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*10}")
    for tau in taus:
        r = results[tau]
        delta = r["accuracy"] - sc_acc
        print(f"  {tau:>5.2f}  {r['accuracy']:>9.2f}%  {r['routed_pct']:>9.1f}%  {r['sc_coverage_pct']:>9.1f}%  {delta:>+9.2f}pp")

def agreement_distribution(problems):
    """Print agreement score distribution."""
    bins = [0, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.01]
    labels = ["<0.5", "0.5-0.6", "0.6-0.7", "0.7-0.8", "0.8-0.9", "0.9-1.0", "=1.0"]
    counts = [0]*7
    for p in problems:
        a = p["agreement"]
        if a < 0.5: counts[0] += 1
        elif a < 0.6: counts[1] += 1
        elif a < 0.7: counts[2] += 1
        elif a < 0.8: counts[3] += 1
        elif a < 0.9: counts[4] += 1
        elif a < 1.0: counts[5] += 1
        else: counts[6] += 1
    print(f"\n  Agreement distribution (n={len(problems)}):")
    for l, c in zip(labels, counts):
        pct = c/len(problems)*100
        bar = "█" * int(pct/2)
        print(f"    {l:>8}: {c:>4} ({pct:>5.1f}%) {bar}")

# ---- Main ----
taus = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
base = "/root/symb_invariant_consensus/results"

experiments = [
    ("exp033_mistral_7b_folio204", "Mistral-7B / FOLIO-204"),
    ("exp036_qwen25_14b_folio204", "Qwen2.5-14B / FOLIO-204"),
    ("exp032_qwen25_14b_pw600", "Qwen2.5-14B / ProofWriter-600"),
]

all_results = {}
for exp_dir, label in experiments:
    idir = os.path.join(base, exp_dir, "intermediates")
    if not os.path.isdir(idir):
        print(f"SKIP {label}: {idir} not found")
        continue
    
    problems = load_and_analyze(idir, label)
    if not problems:
        print(f"SKIP {label}: no problems loaded")
        continue
    
    # Baselines
    sc_correct = sum(1 for p in problems if p["sc_answer"] == p["gt"])
    sica_correct = sum(1 for p in problems if p["sica_answer"] == p["gt"])
    sc_acc = sc_correct / len(problems) * 100
    sica_acc = sica_correct / len(problems) * 100
    
    results = drc_sweep(problems, taus)
    all_results[label] = {"results": results, "sc_acc": sc_acc, "sica_acc": sica_acc, "n": len(problems)}
    
    print_table(label, results, taus, sc_acc, sica_acc)
    agreement_distribution(problems)

# ---- Pareto summary ----
print(f"\n{'='*70}")
print("  PARETO SUMMARY: Best accuracy-cost tradeoffs")
print(f"{'='*70}")
for label, data in all_results.items():
    print(f"\n  {label}:")
    best_tau = None
    best_score = -1
    for tau in taus:
        r = data["results"][tau]
        # Find tau with best accuracy that also improves over SC
        if r["accuracy"] > data["sc_acc"] and r["accuracy"] > best_score:
            best_score = r["accuracy"]
            best_tau = tau
    if best_tau:
        r = data["results"][best_tau]
        print(f"    Sweet spot: τ={best_tau} → {r['accuracy']:.2f}% acc (+{r['accuracy']-data['sc_acc']:.2f}pp vs SC), {r['routed_pct']:.1f}% routed")
    else:
        print(f"    No τ improves over SC ({data['sc_acc']:.2f}%)")
    
    # Also report τ=1.0 (= pure SICA)
    r10 = data["results"][1.0]
    print(f"    τ=1.0 (all→verifier): {r10['accuracy']:.2f}% acc, {r10['routed_pct']:.1f}% routed")

# Save JSON
output = {
    "analysis": "DRC tau sensitivity",
    "verifier_proxy": "SICA answer (no standalone NLI verifier per-problem data available)",
    "taus": taus,
    "experiments": {}
}
for label, data in all_results.items():
    output["experiments"][label] = data
with open(os.path.join(base, "drc_tau_sensitivity.json"), "w") as f:
    json.dump(output, f, indent=2)
print(f"\nSaved to {base}/drc_tau_sensitivity.json")
