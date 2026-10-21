"""Batch SC tiebreaking revalidation: recompute SC with deterministic alphabetical tie-breaking."""
import json
from pathlib import Path

EXPERIMENTS = [
    {"exp_id": "exp-033", "label": "Mistral-7B FOLIO-204 seed=42 T=0.7 K=12",
     "path": "/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json",
     "old_sc": 54.41, "model": "Mistral-7B", "dataset": "FOLIO-204"},
    {"exp_id": "exp-057", "label": "Mistral-7B FOLIO-204 T=0.3",
     "path": "/root/symb_invariant_consensus/results/exp057_mistral_folio204_t03/exp057_results.json",
     "old_sc": 57.35, "model": "Mistral-7B", "dataset": "FOLIO-204"},
    {"exp_id": "exp-058", "label": "Mistral-7B FOLIO-204 T=0.5",
     "path": "/root/symb_invariant_consensus/results/exp058_mistral_folio204_t05/exp058_results.json",
     "old_sc": 57.84, "model": "Mistral-7B", "dataset": "FOLIO-204"},
    {"exp_id": "exp-054", "label": "Mistral-7B FOLIO-204 T=1.0",
     "path": "/root/symb_invariant_consensus/results/exp054_mistral_folio204_t10/exp054_results.json",
     "old_sc": 55.39, "model": "Mistral-7B", "dataset": "FOLIO-204"},
    {"exp_id": "exp-051-k4", "label": "Mistral-7B FOLIO-204 K=4",
     "path": "/root/symb_invariant_consensus/results/exp051_mistral_k_sensitivity/k4/results.json",
     "old_sc": 54.41, "model": "Mistral-7B", "dataset": "FOLIO-204"},
    {"exp_id": "exp-051-k8", "label": "Mistral-7B FOLIO-204 K=8",
     "path": "/root/symb_invariant_consensus/results/exp051_mistral_k_sensitivity/k8/results.json",
     "old_sc": 57.35, "model": "Mistral-7B", "dataset": "FOLIO-204"},
    {"exp_id": "exp-051-k16", "label": "Mistral-7B FOLIO-204 K=16",
     "path": "/root/symb_invariant_consensus/results/exp051_mistral_k_sensitivity/k16/results.json",
     "old_sc": 55.88, "model": "Mistral-7B", "dataset": "FOLIO-204"},
    {"exp_id": "exp-051-k20", "label": "Mistral-7B FOLIO-204 K=20",
     "path": "/root/symb_invariant_consensus/results/exp051_mistral_k_sensitivity/k20/results.json",
     "old_sc": 57.35, "model": "Mistral-7B", "dataset": "FOLIO-204"},
    {"exp_id": "exp-026", "label": "Qwen2.5-14B FOLIO-204",
     "path": "/root/symb_invariant_consensus/results/folio_204_14b/folio_204_results.json",
     "old_sc": 75.00, "model": "Qwen2.5-14B", "dataset": "FOLIO-204"},
    {"exp_id": "exp-027", "label": "Qwen3-14B FOLIO-204",
     "path": "/root/symb_invariant_consensus/results/exp027_qwen3_14b_nonthinking/exp027_results.json",
     "old_sc": 80.39, "model": "Qwen3-14B", "dataset": "FOLIO-204"},
    {"exp_id": "exp-046", "label": "Mistral-7B PW-600",
     "path": "/root/symb_invariant_consensus/results/exp046_mistral_7b_pw600/exp046_results.json",
     "old_sc": 39.33, "model": "Mistral-7B", "dataset": "PW-600"},
    {"exp_id": "exp-034", "label": "Qwen2.5-14B PW-600 (25068, incomplete n=93)",
     "path": "/root/symb_invariant_consensus/results/exp034_qwen25_14b_proofwriter/exp034_results.json",
     "old_sc": 70.33, "model": "Qwen2.5-14B", "dataset": "PW-600"},
]


def normalize_answer(ans):
    if not ans:
        return ""
    a = ans.strip().lower()
    mapping = {
        "true": "True", "false": "False", "unknown": "Unknown",
        "proved": "True", "disproved": "False",
        "a": "A", "b": "B", "c": "C", "d": "D",
    }
    return mapping.get(a, ans.strip())


def deterministic_sc(vote_dist):
    if not vote_dist:
        return ""
    return max(sorted(vote_dist.keys()), key=lambda k: vote_dist[k])


def process_experiment(exp_info):
    path = Path(exp_info["path"])
    if not path.exists():
        return {"exp_id": exp_info["exp_id"], "error": f"File not found: {path}"}

    with open(path) as f:
        data = json.load(f)

    results = data.get("results", [])
    if not results:
        return {"exp_id": exp_info["exp_id"], "error": "No results array"}

    n_total = len(results)
    old_sc_correct = 0
    new_sc_correct = 0
    affected = []
    sica_correct_count = 0

    for r in results:
        gt = r.get("ground_truth", "")
        old_sc_answer = r.get("sc_answer", "")
        vote_dist = r.get("sc_vote_distribution", {})
        sica_correct = r.get("sica_correct", False)

        if sica_correct:
            sica_correct_count += 1

        new_sc_answer = deterministic_sc(vote_dist)

        old_correct = (normalize_answer(old_sc_answer) == normalize_answer(gt))
        new_correct = (normalize_answer(new_sc_answer) == normalize_answer(gt))

        if old_correct:
            old_sc_correct += 1
        if new_correct:
            new_sc_correct += 1

        if old_sc_answer != new_sc_answer:
            affected.append({
                "problem_id": r.get("problem_id", f"idx_{r.get('problem_idx', '?')}"),
                "old_sc": old_sc_answer,
                "new_sc": new_sc_answer,
                "gt": gt,
                "vote_dist": vote_dist,
                "old_correct": old_correct,
                "new_correct": new_correct,
            })

    old_sc_pct = old_sc_correct / n_total * 100
    new_sc_pct = new_sc_correct / n_total * 100
    sica_pct = sica_correct_count / n_total * 100

    return {
        "exp_id": exp_info["exp_id"],
        "label": exp_info["label"],
        "model": exp_info["model"],
        "dataset": exp_info["dataset"],
        "n": n_total,
        "old_sc_pct": old_sc_pct,
        "new_sc_pct": new_sc_pct,
        "registry_sc": exp_info["old_sc"],
        "change": new_sc_pct - old_sc_pct,
        "sica_pct": sica_pct,
        "affected": affected,
    }


def main():
    print("=" * 100)
    print("SC TIEBREAKING REVALIDATION (westd-25068)")
    print("=" * 100)

    all_results = []
    for exp in EXPERIMENTS:
        result = process_experiment(exp)
        all_results.append(result)

    print(f"\n{'Exp':<14} {'Model':<14} {'Dataset':<10} {'N':>4} {'Registry%':>10} {'OldSC%':>8} {'NewSC%':>8} {'Change':>8} {'SICA%':>8} {'OldDelta':>8} {'NewDelta':>8} {'#Aff':>5}")
    print("-" * 130)

    for r in all_results:
        if "error" in r:
            print(f"{r['exp_id']:<14} ERROR: {r['error']}")
            continue

        old_delta = r["sica_pct"] - r["old_sc_pct"]
        new_delta = r["sica_pct"] - r["new_sc_pct"]
        marker = " ***" if abs(r["change"]) > 0.01 else ""

        print(f"{r['exp_id']:<14} {r['model']:<14} {r['dataset']:<10} {r['n']:>4} "
              f"{r['registry_sc']:>9.2f}% {r['old_sc_pct']:>7.2f}% {r['new_sc_pct']:>7.2f}% "
              f"{r['change']:>+7.2f}% {r['sica_pct']:>7.2f}% {old_delta:>+7.2f}% {new_delta:>+7.2f}% "
              f"{len(r['affected']):>4}{marker}")

    print("\n" + "=" * 100)
    print("AFFECTED QUESTIONS DETAIL")
    print("=" * 100)

    any_affected = False
    for r in all_results:
        if "error" in r or not r["affected"]:
            continue
        any_affected = True
        print(f"\n--- {r['exp_id']} ({r['label']}) ---")
        print(f"  SC change: {r['old_sc_pct']:.2f}% -> {r['new_sc_pct']:.2f}% ({r['change']:+.2f}%)")
        for a in r["affected"]:
            if a["old_correct"] and not a["new_correct"]:
                tag = " [LOST]"
            elif not a["old_correct"] and a["new_correct"]:
                tag = " [GAINED]"
            elif a["old_correct"] and a["new_correct"]:
                tag = " [BOTH CORRECT]"
            else:
                tag = " [BOTH WRONG]"
            print(f"  {a['problem_id']}: {a['old_sc']} -> {a['new_sc']} (GT={a['gt']}){tag}  votes={a['vote_dist']}")

    if not any_affected:
        print("\nNo affected questions found in any experiment.")

    output = {"summary": [], "details": {}}
    for r in all_results:
        if "error" in r:
            output["summary"].append({"exp_id": r["exp_id"], "error": r["error"]})
            continue
        old_delta = r["sica_pct"] - r["old_sc_pct"]
        new_delta = r["sica_pct"] - r["new_sc_pct"]
        output["summary"].append({
            "exp_id": r["exp_id"], "label": r["label"], "model": r["model"],
            "dataset": r["dataset"], "n": r["n"],
            "registry_sc": r["registry_sc"],
            "old_sc_pct": round(r["old_sc_pct"], 2),
            "new_sc_pct": round(r["new_sc_pct"], 2),
            "change": round(r["change"], 2),
            "sica_pct": round(r["sica_pct"], 2),
            "old_delta_pp": round(old_delta, 2),
            "new_delta_pp": round(new_delta, 2),
            "n_affected": len(r["affected"]),
        })
        if r["affected"]:
            output["details"][r["exp_id"]] = r["affected"]

    out_path = Path("/root/symb_invariant_consensus/results/sc_tiebreak_revalidation_25068.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nJSON saved to: {out_path}")


if __name__ == "__main__":
    main()
