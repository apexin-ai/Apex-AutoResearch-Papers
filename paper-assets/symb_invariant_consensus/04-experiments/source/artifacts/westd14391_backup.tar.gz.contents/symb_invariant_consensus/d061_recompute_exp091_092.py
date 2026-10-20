"""D061 canonical tiebreaking recompute for exp-091 and exp-092.

Compares insertion-order tiebreaking (old bug) vs alphabetical tiebreaking (D061 fix).
"""
import json
from scipy.stats import binomtest

EXPERIMENTS = {
    "exp-092": {
        "label": "LLaMA-3.1-8B × PW-600",
        "results_path": "/root/symb_invariant_consensus/results/exp092_llama8b_pw_nli_combo/results.json",
        "sc_data_path": "/root/symb_invariant_consensus/results/exp048_llama8b_pw600/exp048_results.json",
        "nli_data_path": "/root/symb_invariant_consensus/results/d116_qwen3_pw_deberta_large/results.json",
    },
    "exp-091": {
        "label": "Qwen2.5-14B × PW-600",
        "results_path": "/root/symb_invariant_consensus/results/qwen14b_pw_nli_combo/results.json",
        "sc_data_path": "/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/results.json",
        "nli_data_path": "/root/symb_invariant_consensus/results/d116_qwen3_pw_deberta_large/results.json",
    },
}

WEIGHTS = [1, 3, 5]
CLASSES = ["True", "False", "Unknown"]


def mcnemar_test(b, c):
    n = b + c
    if n == 0:
        return 1.0
    return binomtest(min(b, c), n, 0.5).pvalue


def combo_vote(sc_vote_dist, nli_pred, w, tiebreak="alphabetical"):
    """Compute combo answer with specified tiebreaking."""
    votes = {}
    for cls in CLASSES:
        votes[cls] = sc_vote_dist.get(cls, 0) + (w if cls == nli_pred else 0)

    max_v = max(votes.values())
    tied = [k for k, v in votes.items() if v == max_v]

    if tiebreak == "alphabetical":
        return sorted(tied)[0]
    else:
        return max(votes, key=votes.get)


def recompute_experiment(exp_id, exp_info):
    with open(exp_info["sc_data_path"]) as f:
        sc_data = json.load(f)
    with open(exp_info["nli_data_path"]) as f:
        nli_data = json.load(f)

    results_list = sc_data["results"]
    nli_pq = nli_data["per_question"]
    total = len(results_list)

    gt = {}
    sc_answers = {}
    sc_vote_dists = {}
    for r in results_list:
        pid = r["problem_id"]
        gt[pid] = r["ground_truth"]
        sc_answers[pid] = r["sc_answer"]
        sc_vote_dists[pid] = r["sc_vote_distribution"]

    nli_preds = {pid: nli_pq[pid]["deberta_pred"] for pid in gt}

    sc_correct_n = sum(1 for pid in gt if sc_answers[pid] == gt[pid])
    sc_acc = sc_correct_n / total

    combo_comparison = {}
    for w in WEIGHTS:
        old_correct = 0
        new_correct = 0
        old_b = old_c = 0
        new_b = new_c = 0
        affected = []

        for pid in gt:
            gold = gt[pid]
            sc_correct = sc_answers[pid] == gold

            old_answer = combo_vote(sc_vote_dists[pid], nli_preds[pid], w, "insertion_order")
            new_answer = combo_vote(sc_vote_dists[pid], nli_preds[pid], w, "alphabetical")

            old_is_correct = old_answer == gold
            new_is_correct = new_answer == gold

            if old_is_correct:
                old_correct += 1
            if new_is_correct:
                new_correct += 1
            if old_is_correct and not sc_correct:
                old_b += 1
            if not old_is_correct and sc_correct:
                old_c += 1
            if new_is_correct and not sc_correct:
                new_b += 1
            if not new_is_correct and sc_correct:
                new_c += 1

            if old_answer != new_answer:
                affected.append({
                    "pid": pid,
                    "old": old_answer,
                    "new": new_answer,
                    "gold": gold,
                    "sc": sc_answers[pid],
                    "nli": nli_preds[pid],
                    "sc_dist": sc_vote_dists[pid],
                    "old_correct": old_is_correct,
                    "new_correct": new_is_correct,
                })

        old_acc = old_correct / total
        new_acc = new_correct / total
        old_delta = old_acc - sc_acc
        new_delta = new_acc - sc_acc
        old_p = mcnemar_test(old_b, old_c)
        new_p = mcnemar_test(new_b, new_c)

        combo_comparison[f"w{w}"] = {
            "old_accuracy": round(old_acc, 4),
            "new_accuracy": round(new_acc, 4),
            "old_correct": old_correct,
            "new_correct": new_correct,
            "old_delta_pp": round(old_delta * 100, 2),
            "new_delta_pp": round(new_delta * 100, 2),
            "old_mcnemar_p": round(old_p, 4),
            "new_mcnemar_p": round(new_p, 4),
            "old_discordant": [old_b, old_c],
            "new_discordant": [new_b, new_c],
            "n_affected": len(affected),
            "affected_details": affected,
        }

    return {
        "exp_id": exp_id,
        "label": exp_info["label"],
        "n": total,
        "sc_baseline": round(sc_acc, 4),
        "sc_baseline_pct": round(sc_acc * 100, 2),
        "sc_correct": sc_correct_n,
        "combo_comparison": combo_comparison,
    }


def main():
    all_results = {}
    for exp_id, exp_info in EXPERIMENTS.items():
        print(f"\n{'='*60}")
        print(f"  {exp_id}: {exp_info['label']}")
        print(f"{'='*60}")

        result = recompute_experiment(exp_id, exp_info)
        all_results[exp_id] = result

        print(f"  SC baseline: {result['sc_baseline_pct']:.2f}% ({result['sc_correct']}/{result['n']})")
        print(f"\n  {'Weight':<8} {'Old Combo':>10} {'New Combo':>10} {'Old Δ':>8} {'New Δ':>8} {'Old p':>8} {'New p':>8} {'#Aff':>5}")
        print(f"  {'-'*67}")
        for w in WEIGHTS:
            c = result["combo_comparison"][f"w{w}"]
            print(f"  w={w:<5} {c['old_accuracy']*100:>9.2f}% {c['new_accuracy']*100:>9.2f}% "
                  f"{c['old_delta_pp']:>+7.2f} {c['new_delta_pp']:>+7.2f} "
                  f"{c['old_mcnemar_p']:>7.4f} {c['new_mcnemar_p']:>7.4f} {c['n_affected']:>5}")

        for w in WEIGHTS:
            c = result["combo_comparison"][f"w{w}"]
            if c["affected_details"]:
                print(f"\n  Affected questions (w={w}):")
                for a in c["affected_details"]:
                    tag = ""
                    if a["old_correct"] and not a["new_correct"]:
                        tag = " [LOST]"
                    elif not a["old_correct"] and a["new_correct"]:
                        tag = " [GAINED]"
                    elif a["old_correct"] and a["new_correct"]:
                        tag = " [BOTH OK]"
                    else:
                        tag = " [BOTH WRONG]"
                    print(f"    {a['pid']}: {a['old']} -> {a['new']} (GT={a['gold']}, SC={a['sc']}, NLI={a['nli']}){tag}")
                    print(f"      sc_dist={a['sc_dist']}")

    # Remove affected_details from saved JSON (too verbose)
    save_results = json.loads(json.dumps(all_results))
    for exp_id in save_results:
        for wk in save_results[exp_id]["combo_comparison"]:
            details = save_results[exp_id]["combo_comparison"][wk].pop("affected_details")
            save_results[exp_id]["combo_comparison"][wk]["affected_pids"] = [d["pid"] for d in details]

    out_path = "/root/symb_invariant_consensus/artifacts/nli_recompute_exp091_exp092.json"
    with open(out_path, "w") as f:
        json.dump(save_results, f, indent=2)
    print(f"\n\nSaved: {out_path}")


if __name__ == "__main__":
    main()
