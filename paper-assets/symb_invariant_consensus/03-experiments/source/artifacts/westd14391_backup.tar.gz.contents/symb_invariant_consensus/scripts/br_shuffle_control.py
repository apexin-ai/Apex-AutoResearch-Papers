import json, os, glob, numpy as np
from collections import defaultdict

RESULTS_DIR = "/root/symb_invariant_consensus/results"
N_SHUFFLE = 1000
SEED = 42

EXPERIMENTS = [
    ("exp_folio_2x2_qwen3", "per_trace_constraints", "Qwen3-FOLIO-2x2"),
    ("e6_gpt4o_folio204", "per_trace_constraints", "GPT4o-FOLIO"),
    ("exp033_mistral_7b_folio204", "constraint_cache", "Mistral7B-FOLIO"),
]


def load_question_data(exp_dir, ptc_subdir):
    ptc_dir = os.path.join(exp_dir, ptc_subdir)
    int_dir = os.path.join(exp_dir, "intermediates")

    if not os.path.isdir(ptc_dir):
        return None

    questions = []
    for f in sorted(glob.glob(os.path.join(ptc_dir, "*.json"))):
        pid = os.path.basename(f).replace(".json", "")
        ptc = json.load(open(f))

        int_file = os.path.join(int_dir, os.path.basename(f))
        if not os.path.exists(int_file):
            continue
        intdata = json.load(open(int_file))
        sica_answer = intdata.get("sica_result", {}).get("answer")
        if sica_answer is None:
            continue

        per_trace = ptc.get("per_trace", [])
        if not per_trace:
            continue

        trace_info = []
        total_c = 0
        for t in per_trace:
            ans = t["answer"]
            n_c = len(t.get("constraints", []))
            trace_info.append({"answer": ans, "n_constraints": n_c})
            total_c += n_c

        if total_c == 0:
            continue

        questions.append({
            "pid": pid,
            "gt": ptc.get("gt"),
            "sica_answer": sica_answer,
            "trace_info": trace_info,
            "total_constraints": total_c,
        })

    return questions


def compute_br(questions):
    """BR per question = total constraints from aligned traces / total from unaligned."""
    brs = []
    valid_qids = []
    for q in questions:
        sica_ans = q["sica_answer"]
        aligned = sum(t["n_constraints"] for t in q["trace_info"] if t["answer"] == sica_ans)
        unaligned = sum(t["n_constraints"] for t in q["trace_info"] if t["answer"] != sica_ans)

        if unaligned == 0 or aligned == 0:
            continue

        brs.append(aligned / unaligned)
        valid_qids.append(q["pid"])
    return brs, valid_qids


def shuffle_and_compute_br(questions, valid_qids, rng):
    """
    For each question, randomly redistribute constraints across traces
    (each constraint uniformly assigned to any trace), keeping trace
    answers fixed. Then recompute BR.
    """
    valid_set = set(valid_qids)
    brs = []
    for q in questions:
        if q["pid"] not in valid_set:
            continue

        sica_ans = q["sica_answer"]
        trace_info = q["trace_info"]
        n_traces = len(trace_info)
        total_c = q["total_constraints"]

        # Randomly assign each constraint to a trace
        assignments = rng.integers(0, n_traces, size=total_c)

        aligned = 0
        unaligned = 0
        for i, t in enumerate(trace_info):
            n_assigned = int(np.sum(assignments == i))
            if t["answer"] == sica_ans:
                aligned += n_assigned
            else:
                unaligned += n_assigned

        if unaligned == 0:
            # Under shuffle, can happen by chance; use BR=inf proxy
            # Skip to keep comparison fair
            continue
        brs.append(aligned / unaligned)

    return brs


def main():
    rng = np.random.default_rng(SEED)

    for exp_name, ptc_sub, label in EXPERIMENTS:
        exp_dir = os.path.join(RESULTS_DIR, exp_name)
        questions = load_question_data(exp_dir, ptc_sub)
        if questions is None:
            print(f"=== {label}: NO DATA ===\n")
            continue

        print(f"{'='*60}")
        print(f"{label} ({exp_name})")
        print(f"{'='*60}")
        print(f"Questions with constraints: {len(questions)}")

        # Original BR
        original_brs, valid_qids = compute_br(questions)
        if not original_brs:
            print(f"  No valid questions (all unanimous).\n")
            continue

        orig_mean = np.mean(original_brs)
        orig_median = np.median(original_brs)
        orig_std = np.std(original_brs)
        n_valid = len(original_brs)
        n_skipped = len(questions) - n_valid

        print(f"Valid questions (both aligned & unaligned traces): {n_valid}")
        print(f"Skipped (unanimous): {n_skipped}")
        print(f"\nOriginal BR:")
        print(f"  Mean:   {orig_mean:.4f}")
        print(f"  Median: {orig_median:.4f}")
        print(f"  Std:    {orig_std:.4f}")
        print(f"  Min:    {min(original_brs):.4f}")
        print(f"  Max:    {max(original_brs):.4f}")

        # Shuffle null distribution
        shuffle_means = []
        shuffle_medians = []
        for i in range(N_SHUFFLE):
            s_brs = shuffle_and_compute_br(questions, valid_qids, rng)
            if s_brs:
                shuffle_means.append(np.mean(s_brs))
                shuffle_medians.append(np.median(s_brs))

        shuffle_means = np.array(shuffle_means)
        shuffle_medians = np.array(shuffle_medians)
        s_mean = np.mean(shuffle_means)
        s_std = np.std(shuffle_means)
        p2_5, p50, p97_5 = np.percentile(shuffle_means, [2.5, 50, 97.5])

        # p-value
        p_value = np.mean(shuffle_means >= orig_mean)

        print(f"\nShuffle Null Distribution ({N_SHUFFLE} runs):")
        print(f"  Mean of means:  {s_mean:.4f} ± {s_std:.4f}")
        print(f"  Mean of medians: {np.mean(shuffle_medians):.4f}")
        print(f"  95% CI of means: [{p2_5:.4f}, {p97_5:.4f}]")
        print(f"  p-value (shuffle_mean >= orig_mean): {p_value:.4f}")

        if s_std > 0:
            cohen_d = (orig_mean - s_mean) / s_std
            print(f"  Cohen's d: {cohen_d:.2f}")

        # Constraint count asymmetry
        aligned_per_trace = []
        unaligned_per_trace = []
        for q in questions:
            sica_ans = q["sica_answer"]
            for t in q["trace_info"]:
                if t["answer"] == sica_ans:
                    aligned_per_trace.append(t["n_constraints"])
                else:
                    unaligned_per_trace.append(t["n_constraints"])

        print(f"\nConstraints per trace (diagnostic):")
        print(f"  Aligned:   mean={np.mean(aligned_per_trace):.2f}, median={np.median(aligned_per_trace):.1f}, n_traces={len(aligned_per_trace)}")
        print(f"  Unaligned: mean={np.mean(unaligned_per_trace):.2f}, median={np.median(unaligned_per_trace):.1f}, n_traces={len(unaligned_per_trace)}")

        # Answer distribution
        ans_counts = defaultdict(int)
        for q in questions:
            ans_counts[q["sica_answer"]] += 1
        print(f"\nSICA answer distribution: {dict(ans_counts)}")

        print()


if __name__ == "__main__":
    main()
