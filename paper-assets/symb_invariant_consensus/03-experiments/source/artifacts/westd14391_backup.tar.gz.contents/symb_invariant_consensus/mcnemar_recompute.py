"""McNemar exact test recomputation after SC tiebreaking fix."""
import json
import sys
from pathlib import Path
from scipy.stats import binomtest


def normalize_answer(ans):
    if not ans:
        return ""
    a = ans.strip().lower()
    mapping = {
        "true": "True", "false": "False", "unknown": "Unknown",
        "proved": "True", "disproved": "False",
    }
    return mapping.get(a, ans.strip())


def deterministic_sc(vote_dist):
    if not vote_dist:
        return ""
    return max(sorted(vote_dist.keys()), key=lambda k: vote_dist[k])


def compute_mcnemar(exp_info):
    path = Path(exp_info["path"])
    if not path.exists():
        return {"exp_id": exp_info["exp_id"], "error": f"File not found: {path}"}

    with open(path) as f:
        data = json.load(f)

    results = data.get("results", [])
    n = len(results)

    b = 0
    c = 0
    a_both = 0
    d_both = 0
    new_sc_correct_count = 0
    sica_correct_count = 0

    for r in results:
        gt = r.get("ground_truth", "")
        sica_correct = r.get("sica_correct", False)
        vote_dist = r.get("sc_vote_distribution", {})
        new_sc_answer = deterministic_sc(vote_dist)
        new_sc_correct = (normalize_answer(new_sc_answer) == normalize_answer(gt))

        if new_sc_correct:
            new_sc_correct_count += 1
        if sica_correct:
            sica_correct_count += 1

        if new_sc_correct and sica_correct:
            a_both += 1
        elif new_sc_correct and not sica_correct:
            b += 1
        elif not new_sc_correct and sica_correct:
            c += 1
        else:
            d_both += 1

    new_sc_pct = new_sc_correct_count / n * 100
    sica_pct = sica_correct_count / n * 100
    delta_pp = sica_pct - new_sc_pct

    if b + c == 0:
        p_value = 1.0
    else:
        result = binomtest(min(b, c), b + c, 0.5)
        p_value = result.pvalue

    if p_value < 0.02:
        sig = "**"
    elif p_value < 0.05:
        sig = "*"
    else:
        sig = "ns"

    return {
        "exp_id": exp_info["exp_id"],
        "label": exp_info["label"],
        "n": n,
        "new_sc_pct": round(new_sc_pct, 2),
        "sica_pct": round(sica_pct, 2),
        "delta_pp": round(delta_pp, 2),
        "a_both_correct": a_both,
        "b_sc_correct_sica_wrong": b,
        "c_sc_wrong_sica_correct": c,
        "d_both_wrong": d_both,
        "p_value": p_value,
        "sig": sig,
    }


EXPERIMENTS_25068 = [
    {"exp_id": "exp-033", "label": "Mistral-7B FOLIO-204 seed=42",
     "path": "/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json"},
    {"exp_id": "exp-057", "label": "Mistral-7B FOLIO-204 T=0.3",
     "path": "/root/symb_invariant_consensus/results/exp057_mistral_folio204_t03/exp057_results.json"},
    {"exp_id": "exp-058", "label": "Mistral-7B FOLIO-204 T=0.5",
     "path": "/root/symb_invariant_consensus/results/exp058_mistral_folio204_t05/exp058_results.json"},
    {"exp_id": "exp-054", "label": "Mistral-7B FOLIO-204 T=1.0",
     "path": "/root/symb_invariant_consensus/results/exp054_mistral_folio204_t10/exp054_results.json"},
    {"exp_id": "exp-051-k8", "label": "Mistral-7B FOLIO-204 K=8",
     "path": "/root/symb_invariant_consensus/results/exp051_mistral_k_sensitivity/k8/results.json"},
    {"exp_id": "exp-026", "label": "Qwen2.5-14B FOLIO-204",
     "path": "/root/symb_invariant_consensus/results/folio_204_14b/folio_204_results.json"},
    {"exp_id": "exp-027", "label": "Qwen3-14B FOLIO-204",
     "path": "/root/symb_invariant_consensus/results/exp027_qwen3_14b_nonthinking/exp027_results.json"},
    {"exp_id": "exp-046", "label": "Mistral-7B PW-600 (sanity)",
     "path": "/root/symb_invariant_consensus/results/exp046_mistral_7b_pw600/exp046_results.json"},
    {"exp_id": "exp-034", "label": "Qwen2.5-14B PW-600",
     "path": "/root/symb_invariant_consensus/results/exp034_qwen25_14b_proofwriter/exp034_results.json"},
]

EXPERIMENTS_16639 = [
    {"exp_id": "exp-052", "label": "Mistral-7B FOLIO-204 seed=123",
     "path": "/root/symb_invariant_consensus/results/exp052_mistral_folio204_seed123/exp052_results.json"},
    {"exp_id": "exp-053", "label": "Mistral-7B FOLIO-204 seed=456",
     "path": "/root/symb_invariant_consensus/results/exp053_mistral_folio204_seed456/exp053_results.json"},
    {"exp_id": "exp-039", "label": "Qwen2.5-14B PW-600",
     "path": "/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/results.json"},
]


def main():
    server = sys.argv[1] if len(sys.argv) > 1 else "25068"
    experiments = EXPERIMENTS_25068 if server == "25068" else EXPERIMENTS_16639

    all_results = []
    for exp in experiments:
        r = compute_mcnemar(exp)
        all_results.append(r)

    header = f"{'Exp':<14} {'n':>4} {'NewSC%':>8} {'SICA%':>8} {'D(pp)':>8} {'b':>4} {'c':>4} {'McNemar_p':>12} {'Sig':>5}"
    print(header)
    print("-" * len(header))
    for r in all_results:
        if "error" in r:
            print(f"{r['exp_id']:<14} ERROR: {r['error']}")
            continue
        print(f"{r['exp_id']:<14} {r['n']:>4} {r['new_sc_pct']:>7.2f}% {r['sica_pct']:>7.2f}% {r['delta_pp']:>+7.2f} {r['b_sc_correct_sica_wrong']:>4} {r['c_sc_wrong_sica_correct']:>4} {r['p_value']:>12.6f} {r['sig']:>5}")

    out = {"server": f"westd-{server}", "results": all_results}
    out_path = Path(f"/root/symb_invariant_consensus/results/mcnemar_recomputed_{server}.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    main()
