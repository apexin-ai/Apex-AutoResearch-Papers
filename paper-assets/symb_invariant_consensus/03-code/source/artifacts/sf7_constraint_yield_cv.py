import json, os, sys
from collections import Counter, defaultdict
import numpy as np
from scipy import stats

BASE = "/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204"
CACHE_DIR = os.path.join(BASE, "constraint_cache")
OUT_PATH = os.path.join(BASE, "sf7_constraint_yield_cv.json")

def load_all():
    problems = []
    for fname in sorted(os.listdir(CACHE_DIR)):
        if not fname.endswith(".json"):
            continue
        with open(os.path.join(CACHE_DIR, fname)) as f:
            d = json.load(f)
        problems.append(d)
    return problems

def compute_group_stats(yields):
    if len(yields) == 0:
        return {"mean": None, "std": None, "cv": None, "n": 0}
    arr = np.array(yields, dtype=float)
    m = float(np.mean(arr))
    s = float(np.std(arr, ddof=1)) if len(arr) > 1 else 0.0
    cv = s / m if m > 0 else float("inf")
    return {"mean": round(m, 4), "std": round(s, 4), "cv": round(cv, 4), "n": len(arr)}

def main():
    problems = load_all()
    print(f"Loaded {len(problems)} problems")

    all_yields = []
    majority_yields = []
    minority_yields = []
    correct_yields = []
    incorrect_yields = []
    per_problem_cvs = []
    per_problem_details = []
    per_answer_group_yields = defaultdict(list)

    for prob in problems:
        pid = prob["pid"]
        gt = prob.get("gt", None)
        traces = prob["per_trace"]

        trace_answers = []
        trace_yields = []
        for t in traces:
            ans = t.get("answer", "")
            if ans == "":
                ans = "NO_ANSWER"
            n_c = len(t.get("constraints", []))
            trace_answers.append(ans)
            trace_yields.append(n_c)
            all_yields.append(n_c)
            per_answer_group_yields[ans].append(n_c)

        if len(trace_yields) == 0:
            continue

        # majority answer
        cnt = Counter(trace_answers)
        majority_ans = cnt.most_common(1)[0][0]

        for ans, y in zip(trace_answers, trace_yields):
            if ans == majority_ans:
                majority_yields.append(y)
            else:
                minority_yields.append(y)

            if gt is not None and gt != "":
                if ans == gt:
                    correct_yields.append(y)
                else:
                    incorrect_yields.append(y)

        # per-problem CV
        arr = np.array(trace_yields, dtype=float)
        if len(arr) > 1 and np.mean(arr) > 0:
            cv = float(np.std(arr, ddof=1) / np.mean(arr))
        else:
            cv = 0.0
        per_problem_cvs.append(cv)
        per_problem_details.append({
            "pid": pid,
            "gt": gt,
            "n_traces": len(traces),
            "yield_mean": round(float(np.mean(arr)), 2),
            "yield_std": round(float(np.std(arr, ddof=1)), 2) if len(arr) > 1 else 0.0,
            "yield_cv": round(cv, 4),
            "yield_min": int(np.min(arr)),
            "yield_max": int(np.max(arr)),
            "majority_answer": majority_ans,
            "answer_distribution": dict(cnt),
        })

    # Statistical tests
    # Mann-Whitney U: majority vs minority
    if len(majority_yields) > 0 and len(minority_yields) > 0:
        u_stat, mw_p = stats.mannwhitneyu(majority_yields, minority_yields, alternative="two-sided")
        maj_vs_min_p = float(mw_p)
        maj_vs_min_u = float(u_stat)
    else:
        maj_vs_min_p = None
        maj_vs_min_u = None

    # Mann-Whitney U: correct vs incorrect
    if len(correct_yields) > 0 and len(incorrect_yields) > 0:
        u_stat2, mw_p2 = stats.mannwhitneyu(correct_yields, incorrect_yields, alternative="two-sided")
        cor_vs_inc_p = float(mw_p2)
        cor_vs_inc_u = float(u_stat2)
    else:
        cor_vs_inc_p = None
        cor_vs_inc_u = None

    # Per-answer-group stats
    answer_group_stats = {}
    for ans, ys in sorted(per_answer_group_yields.items(), key=lambda x: -len(x[1])):
        answer_group_stats[ans] = compute_group_stats(ys)

    # Per-problem CV distribution
    cv_arr = np.array(per_problem_cvs)

    result = {
        "overall": compute_group_stats(all_yields),
        "majority_group": compute_group_stats(majority_yields),
        "minority_group": compute_group_stats(minority_yields),
        "correct_group": compute_group_stats(correct_yields),
        "incorrect_group": compute_group_stats(incorrect_yields),
        "majority_vs_minority": {
            "mann_whitney_u": maj_vs_min_u,
            "pvalue": maj_vs_min_p,
            "majority_mean": round(float(np.mean(majority_yields)), 4) if majority_yields else None,
            "minority_mean": round(float(np.mean(minority_yields)), 4) if minority_yields else None,
            "effect_size_r": round(maj_vs_min_u / (len(majority_yields) * len(minority_yields)), 4) if maj_vs_min_u is not None else None,
        },
        "correct_vs_incorrect": {
            "mann_whitney_u": cor_vs_inc_u,
            "pvalue": cor_vs_inc_p,
            "correct_mean": round(float(np.mean(correct_yields)), 4) if correct_yields else None,
            "incorrect_mean": round(float(np.mean(incorrect_yields)), 4) if incorrect_yields else None,
            "effect_size_r": round(cor_vs_inc_u / (len(correct_yields) * len(incorrect_yields)), 4) if cor_vs_inc_u is not None else None,
        },
        "per_answer_group": answer_group_stats,
        "per_problem_cv_distribution": {
            "mean": round(float(np.mean(cv_arr)), 4),
            "median": round(float(np.median(cv_arr)), 4),
            "std": round(float(np.std(cv_arr, ddof=1)), 4),
            "q25": round(float(np.percentile(cv_arr, 25)), 4),
            "q75": round(float(np.percentile(cv_arr, 75)), 4),
            "pct_below_0.3": round(float(np.mean(cv_arr < 0.3)), 4),
            "pct_below_0.5": round(float(np.mean(cv_arr < 0.5)), 4),
        },
        "per_problem_details": per_problem_details,
    }

    with open(OUT_PATH, "w") as f:
        json.dump(result, f, indent=2)
    print(f"Saved to {OUT_PATH}")

    # Print summary
    print(f"\n=== SF7 Constraint Yield CV Analysis ===")
    print(f"Total traces: {result['overall']['n']}")
    print(f"Overall yield: mean={result['overall']['mean']}, std={result['overall']['std']}, CV={result['overall']['cv']}")
    print(f"\nMajority group: mean={result['majority_group']['mean']}, std={result['majority_group']['std']}, CV={result['majority_group']['cv']}, n={result['majority_group']['n']}")
    print(f"Minority group: mean={result['minority_group']['mean']}, std={result['minority_group']['std']}, CV={result['minority_group']['cv']}, n={result['minority_group']['n']}")
    print(f"Majority vs Minority p-value: {result['majority_vs_minority']['pvalue']}")
    print(f"\nCorrect group: mean={result['correct_group']['mean']}, std={result['correct_group']['std']}, CV={result['correct_group']['cv']}, n={result['correct_group']['n']}")
    print(f"Incorrect group: mean={result['incorrect_group']['mean']}, std={result['incorrect_group']['std']}, CV={result['incorrect_group']['cv']}, n={result['incorrect_group']['n']}")
    print(f"Correct vs Incorrect p-value: {result['correct_vs_incorrect']['pvalue']}")
    print(f"\nPer-answer-group yield:")
    for ans, st in result["per_answer_group"].items():
        print(f"  {ans}: mean={st['mean']}, std={st['std']}, CV={st['cv']}, n={st['n']}")
    print(f"\nPer-problem CV distribution:")
    cvd = result["per_problem_cv_distribution"]
    print(f"  mean={cvd['mean']}, median={cvd['median']}, std={cvd['std']}")
    print(f"  Q25={cvd['q25']}, Q75={cvd['q75']}")
    print(f"  % problems with CV < 0.3: {cvd['pct_below_0.3']*100:.1f}%")
    print(f"  % problems with CV < 0.5: {cvd['pct_below_0.5']*100:.1f}%")

    # Observation 1 assessment
    overall_cv = result["overall"]["cv"]
    median_cv = cvd["median"]
    print(f"\n=== Observation 1 Assessment ===")
    if median_cv < 0.3:
        print(f"SUPPORTED: Median per-problem CV = {median_cv:.4f} < 0.3 → approximately uniform yield")
    elif median_cv < 0.5:
        print(f"PARTIALLY SUPPORTED: Median per-problem CV = {median_cv:.4f} (0.3-0.5 range, moderate variation)")
    else:
        print(f"NOT SUPPORTED: Median per-problem CV = {median_cv:.4f} >= 0.5 → high variation in yield")

    maj_p = result["majority_vs_minority"]["pvalue"]
    if maj_p is not None:
        if maj_p < 0.05:
            print(f"WARNING: Majority vs minority yield differs significantly (p={maj_p:.4e})")
            print(f"  Majority mean={result['majority_vs_minority']['majority_mean']}, Minority mean={result['majority_vs_minority']['minority_mean']}")
        else:
            print(f"OK: No significant difference between majority/minority yield (p={maj_p:.4f})")

    cor_p = result["correct_vs_incorrect"]["pvalue"]
    if cor_p is not None:
        if cor_p < 0.05:
            print(f"WARNING: Correct vs incorrect yield differs significantly (p={cor_p:.4e})")
            print(f"  Correct mean={result['correct_vs_incorrect']['correct_mean']}, Incorrect mean={result['correct_vs_incorrect']['incorrect_mean']}")
        else:
            print(f"OK: No significant difference between correct/incorrect yield (p={cor_p:.4f})")

if __name__ == "__main__":
    main()
