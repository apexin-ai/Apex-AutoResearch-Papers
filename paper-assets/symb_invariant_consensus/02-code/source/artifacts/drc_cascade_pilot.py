"""DRC (Disagreement-Routed Cascade) pilot: Mistral-7B ProofWriter 600."""
import json
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

RESULTS_DIR = "/root/symb_invariant_consensus/results"
SC_PATH = f"{RESULTS_DIR}/exp046_mistral_7b_pw600/exp046_results.json"
NLI_PATH = f"{RESULTS_DIR}/direction_r_nli_pw600/results.json"
OUT_DIR = f"{RESULTS_DIR}/drc_cascade_pilot"
VALID_ANSWERS = {"True", "False", "Unknown"}
K = 12
W = 3
TAUS = [0.3, 0.5, 0.7, 0.9]


def majority_vote(vote_dist, tiebreak_alpha=True):
    if not vote_dist:
        return "Unknown"
    max_count = max(vote_dist.values())
    winners = [k for k, v in vote_dist.items() if v == max_count]
    if tiebreak_alpha:
        winners.sort()
    return winners[0]


def filter_valid(vote_dist):
    return {k: v for k, v in vote_dist.items() if k in VALID_ANSWERS}


def combo_answer(sc_dist, nli_pred, w):
    combined = dict(filter_valid(sc_dist))
    combined[nli_pred] = combined.get(nli_pred, 0) + w
    return majority_vote(combined)


def main():
    with open(SC_PATH) as f:
        sc_data = json.load(f)
    with open(NLI_PATH) as f:
        nli_data = json.load(f)

    sc_results = sc_data["results"]
    nli_per_q = nli_data["per_question"]

    questions = []
    for r in sc_results:
        pid = r["problem_id"]
        if pid not in nli_per_q:
            continue
        nli_q = nli_per_q[pid]
        valid_dist = filter_valid(r["sc_vote_distribution"])
        total_valid = sum(valid_dist.values())
        if total_valid == 0:
            agreement = 0.0
        else:
            agreement = max(valid_dist.values()) / total_valid
        sc_ans = majority_vote(valid_dist)
        questions.append({
            "pid": pid,
            "gold": r["ground_truth"],
            "sc_dist": r["sc_vote_distribution"],
            "sc_answer": sc_ans,
            "agreement": agreement,
            "nli_pred": nli_q["deberta_pred"],
            "combo_w3": combo_answer(r["sc_vote_distribution"], nli_q["deberta_pred"], W),
        })

    n = len(questions)
    sc_correct = sum(1 for q in questions if q["sc_answer"] == q["gold"])
    combo_correct = sum(1 for q in questions if q["combo_w3"] == q["gold"])

    results = {
        "n_questions": n,
        "baselines": {
            "sc_only": {"accuracy": sc_correct / n, "correct": sc_correct},
            "full_combo_w3": {"accuracy": combo_correct / n, "correct": combo_correct},
        },
        "taus": {},
    }

    for tau in TAUS:
        drc_correct = 0
        nli_invoked = 0
        for q in questions:
            if q["agreement"] > tau:
                pred = q["sc_answer"]
            else:
                pred = q["combo_w3"]
                nli_invoked += 1
            if pred == q["gold"]:
                drc_correct += 1

        results["taus"][str(tau)] = {
            "accuracy": drc_correct / n,
            "correct": drc_correct,
            "nli_invocation_rate": nli_invoked / n,
            "nli_invoked": nli_invoked,
            "sc_only_count": n - nli_invoked,
        }

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(f"{OUT_DIR}/results.json", "w") as f:
        json.dump(results, f, indent=2)

    # Pareto front plot
    fig, ax = plt.subplots(1, 1, figsize=(6, 4))
    xs, ys, labels = [], [], []
    for tau in TAUS:
        r = results["taus"][str(tau)]
        xs.append(r["nli_invocation_rate"] * 100)
        ys.append(r["accuracy"] * 100)
        labels.append(f"τ={tau}")

    ax.plot(xs, ys, "o-", color="#2563eb", markersize=8, linewidth=2, zorder=3)
    for x, y, label in zip(xs, ys, labels):
        ax.annotate(label, (x, y), textcoords="offset points", xytext=(8, 6), fontsize=9)

    sc_acc = results["baselines"]["sc_only"]["accuracy"] * 100
    combo_acc = results["baselines"]["full_combo_w3"]["accuracy"] * 100
    ax.axhline(sc_acc, color="gray", linestyle="--", linewidth=1, label=f"SC-only ({sc_acc:.1f}%)")
    ax.axhline(combo_acc, color="orange", linestyle="--", linewidth=1, label=f"Full combo w=3 ({combo_acc:.1f}%)")

    ax.set_xlabel("NLI Invocation Rate (%)", fontsize=11)
    ax.set_ylabel("Accuracy (%)", fontsize=11)
    ax.set_title("DRC Cascade: Mistral-7B ProofWriter-600", fontsize=12)
    ax.legend(fontsize=9, loc="lower right")
    ax.set_xlim(-5, 105)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{OUT_DIR}/pareto_front.pdf", bbox_inches="tight")
    plt.savefig(f"{OUT_DIR}/pareto_front.png", dpi=150, bbox_inches="tight")

    # Agreement distribution histogram
    fig2, ax2 = plt.subplots(1, 1, figsize=(6, 3.5))
    agreements = [q["agreement"] for q in questions]
    ax2.hist(agreements, bins=20, color="#2563eb", alpha=0.7, edgecolor="white")
    for tau in TAUS:
        ax2.axvline(tau, color="red", linestyle="--", alpha=0.5, linewidth=1)
    ax2.set_xlabel("SC Agreement (majority fraction)", fontsize=11)
    ax2.set_ylabel("Count", fontsize=11)
    ax2.set_title("Distribution of Per-Question SC Agreement", fontsize=12)
    plt.tight_layout()
    plt.savefig(f"{OUT_DIR}/agreement_distribution.png", dpi=150, bbox_inches="tight")

    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
