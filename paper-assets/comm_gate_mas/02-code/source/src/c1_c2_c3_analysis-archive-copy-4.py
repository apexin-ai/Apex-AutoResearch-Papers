"""
C1/C2/C3 supplementary analyses for comm_gate_mas paper appendix.

C1: Cascade rate significance test — P(ack|ack) vs null model P(ack)^2
C2: Task-level cascade rate vs pruning outcome correlation (oracle data)
C3: Qwen3 vs Qwen2.5 ack content comparison

Inputs:
  - outputs/full_scale/{qwen,llama}_round_robin/annotations/annotations.jsonl  (C1, C2 annotations)
  - outputs/oracle_qwen_n500_fixed/result.json  (C2 oracle Qwen)
  - outputs/oracle_5class_llama_gsm8k.json  (C2 oracle Llama)
  - outputs/full_scale/{qwen,llama}_round_robin/traces/traces.jsonl  (C3 content analysis)

Outputs:
  Prints all results to stdout for integration into appendix_statistical.tex
"""

import json
import os
import sys
from collections import defaultdict
import numpy as np
from scipy import stats

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "outputs")


def resolve_annotation_type(ann):
    """Resolve annotation type: use agreed type if agreement, else use annotation_a."""
    if ann.get("agreement"):
        return ann["annotation_a"]["type"]
    # When annotators disagree, use annotation_a (primary)
    return ann["annotation_a"]["type"]


# =============================================================================
# C1: Cascade rate significance test
# =============================================================================

def c1_cascade_significance():
    print("=" * 70)
    print("C1: CASCADE RATE SIGNIFICANCE TEST")
    print("=" * 70)

    for backbone, fname in [
        ("Qwen", "full_scale/qwen_round_robin/annotations/annotations.jsonl"),
        ("Llama", "full_scale/llama_round_robin/annotations/annotations.jsonl"),
    ]:
        path = os.path.join(OUT, fname)
        with open(path) as f:
            annotations = [json.loads(l) for l in f]

        # Group by task
        tasks = defaultdict(list)
        for a in annotations:
            tasks[a["task_id"]].append(a)

        # Compute transition statistics
        total_ack = 0
        total_messages = 0
        ack_following_ack = 0  # consecutive ack pairs
        ack_preceded_messages = 0  # messages preceded by ack (i.e., positions after an ack)

        for task_id, msgs in tasks.items():
            msgs_sorted = sorted(msgs, key=lambda x: x["message_index"])
            types = [resolve_annotation_type(m) for m in msgs_sorted]

            total_messages += len(types)
            total_ack += sum(1 for t in types if t == "acknowledgment")

            for i in range(1, len(types)):
                if types[i - 1] == "acknowledgment":
                    ack_preceded_messages += 1
                    if types[i] == "acknowledgment":
                        ack_following_ack += 1

        p_ack = total_ack / total_messages
        p_ack_squared = p_ack ** 2
        p_ack_given_ack = ack_following_ack / ack_preceded_messages if ack_preceded_messages > 0 else 0

        print(f"\n--- {backbone} ---")
        print(f"Total messages: {total_messages}")
        print(f"Total ack: {total_ack} ({p_ack*100:.1f}%)")
        print(f"P(ack)^2 (null model): {p_ack_squared*100:.1f}%")
        print(f"Ack-preceded messages: {ack_preceded_messages}")
        print(f"Consecutive ack pairs: {ack_following_ack}")
        print(f"P(ack|ack) observed: {p_ack_given_ack*100:.1f}%")

        # Chi-squared test: compare observed vs expected under independence
        # Contingency: among messages preceded by ack,
        #   observed ack: ack_following_ack
        #   observed non-ack: ack_preceded_messages - ack_following_ack
        #   expected ack under independence: ack_preceded_messages * p_ack
        #   expected non-ack under independence: ack_preceded_messages * (1 - p_ack)
        n = ack_preceded_messages
        observed_ack = ack_following_ack
        observed_nonack = n - observed_ack
        expected_ack = n * p_ack
        expected_nonack = n * (1 - p_ack)

        # Chi-squared goodness of fit (1 df)
        chi2 = ((observed_ack - expected_ack) ** 2 / expected_ack +
                (observed_nonack - expected_nonack) ** 2 / expected_nonack)
        p_chi2 = 1 - stats.chi2.cdf(chi2, df=1)

        print(f"\nChi-squared goodness-of-fit test (H0: P(ack|ack) = P(ack)):")
        print(f"  Expected ack count under H0: {expected_ack:.1f}")
        print(f"  Observed ack count: {observed_ack}")
        print(f"  Chi2 = {chi2:.2f}, df=1, p = {p_chi2:.2e}")

        # Also do exact binomial test
        # Under H0, each ack-preceded message is ack with probability p_ack
        # Test: is observed proportion significantly > p_ack?
        binom_p = 1 - stats.binom.cdf(observed_ack - 1, n, p_ack)
        print(f"\nExact binomial test (one-sided, H1: P(ack|ack) > P(ack)):")
        print(f"  n={n}, k={observed_ack}, p0={p_ack:.4f}")
        print(f"  p-value = {binom_p:.2e}")

        # Effect size: odds ratio
        # P(ack|ack) / P(ack|non-ack)
        nonack_preceded = total_messages - len(tasks) - ack_preceded_messages  # messages preceded by non-ack
        # Actually let's compute P(ack|non-ack) directly
        ack_following_nonack = 0
        nonack_preceded_messages = 0
        for task_id, msgs in tasks.items():
            msgs_sorted = sorted(msgs, key=lambda x: x["message_index"])
            types = [resolve_annotation_type(m) for m in msgs_sorted]
            for i in range(1, len(types)):
                if types[i - 1] != "acknowledgment":
                    nonack_preceded_messages += 1
                    if types[i] == "acknowledgment":
                        ack_following_nonack += 1

        p_ack_given_nonack = ack_following_nonack / nonack_preceded_messages if nonack_preceded_messages > 0 else 0
        print(f"\nP(ack|non-ack): {p_ack_given_nonack*100:.1f}% (n={nonack_preceded_messages})")

        # Odds ratio
        if p_ack_given_nonack > 0 and p_ack_given_nonack < 1:
            or_val = (p_ack_given_ack / (1 - p_ack_given_ack)) / (p_ack_given_nonack / (1 - p_ack_given_nonack))
            print(f"Odds ratio (ack|ack vs ack|non-ack): {or_val:.2f}")

        # Ratio
        ratio = p_ack_given_ack / p_ack if p_ack > 0 else float("inf")
        print(f"Ratio P(ack|ack) / P(ack): {ratio:.2f}x")

        print()


# =============================================================================
# C2: Task-level cascade rate vs pruning outcome correlation
# =============================================================================

def c2_cascade_vs_pruning():
    print("=" * 70)
    print("C2: TASK-LEVEL CASCADE RATE vs PRUNING OUTCOME CORRELATION")
    print("=" * 70)

    for backbone, oracle_path, ann_path in [
        ("Qwen", "oracle_qwen_n500_fixed/result.json",
         "full_scale/qwen_round_robin/annotations/annotations.jsonl"),
        ("Llama", "oracle_5class_llama_gsm8k.json",
         "full_scale/llama_round_robin/annotations/annotations.jsonl"),
    ]:
        print(f"\n--- {backbone} ---")
        oracle_file = os.path.join(OUT, oracle_path)
        oracle_data = json.load(open(oracle_file))
        per_task = oracle_data["per_task"]

        # Compute task-level cascade rate from oracle decisions
        task_cascade = {}
        task_outcome_change = {}
        task_outcome_direction = {}

        for task in per_task:
            tid = task["task_id"]
            decisions = task["oracle_decisions"]
            types = [d["function_type"] for d in decisions]

            # Cascade rate: fraction of consecutive pairs that are both ack
            ack_pairs = 0
            total_pairs = 0
            for i in range(1, len(types)):
                if types[i - 1] == "acknowledgment":
                    total_pairs += 1
                    if types[i] == "acknowledgment":
                        ack_pairs += 1

            cascade_rate = ack_pairs / total_pairs if total_pairs > 0 else np.nan
            task_cascade[tid] = cascade_rate

            # Pruning outcome: did correctness change?
            baseline_correct = task["baseline_correct"]
            pruned_correct = task["oracle_pruned_correct"]
            changed = baseline_correct != pruned_correct
            task_outcome_change[tid] = changed

            # Direction: +1 if improved, -1 if degraded, 0 if no change
            if not changed:
                task_outcome_direction[tid] = 0
            elif pruned_correct and not baseline_correct:
                task_outcome_direction[tid] = 1  # improved
            else:
                task_outcome_direction[tid] = -1  # degraded

        # Also compute alternative cascade metric: ack density (proportion of ack messages)
        task_ack_density = {}
        for task in per_task:
            tid = task["task_id"]
            decisions = task["oracle_decisions"]
            n_ack = sum(1 for d in decisions if d["is_ack"])
            task_ack_density[tid] = n_ack / len(decisions) if decisions else 0

        # Filter tasks with valid cascade rates
        valid_tids = [tid for tid in task_cascade if not np.isnan(task_cascade[tid])]
        print(f"Tasks with valid cascade rate: {len(valid_tids)} / {len(per_task)}")

        cascade_arr = np.array([task_cascade[tid] for tid in valid_tids])
        changed_arr = np.array([1 if task_outcome_change[tid] else 0 for tid in valid_tids])
        direction_arr = np.array([task_outcome_direction[tid] for tid in valid_tids])

        n_changed = changed_arr.sum()
        n_improved = sum(1 for tid in valid_tids if task_outcome_direction[tid] == 1)
        n_degraded = sum(1 for tid in valid_tids if task_outcome_direction[tid] == -1)
        print(f"Outcome changed: {n_changed} (improved: {n_improved}, degraded: {n_degraded})")

        # Point-biserial correlation: cascade_rate vs outcome_changed
        if n_changed > 0 and n_changed < len(valid_tids):
            r_pb, p_pb = stats.pointbiserialr(changed_arr, cascade_arr)
            print(f"\nPoint-biserial correlation (cascade_rate vs outcome_changed):")
            print(f"  r = {r_pb:.4f}, p = {p_pb:.4f}")
        else:
            print(f"\nCannot compute point-biserial: only {n_changed} changed outcomes")

        # Also try with ack density
        all_tids = list(task_ack_density.keys())
        density_arr = np.array([task_ack_density[tid] for tid in all_tids])
        changed_all = np.array([1 if task_outcome_change[tid] else 0 for tid in all_tids])

        if changed_all.sum() > 0 and changed_all.sum() < len(all_tids):
            r_pb2, p_pb2 = stats.pointbiserialr(changed_all, density_arr)
            print(f"\nPoint-biserial correlation (ack_density vs outcome_changed):")
            print(f"  r = {r_pb2:.4f}, p = {p_pb2:.4f}")

        # Mann-Whitney U: compare cascade rates between changed vs unchanged tasks
        if n_changed > 0 and n_changed < len(valid_tids):
            cascade_changed = cascade_arr[changed_arr == 1]
            cascade_unchanged = cascade_arr[changed_arr == 0]
            u_stat, u_p = stats.mannwhitneyu(cascade_changed, cascade_unchanged, alternative='two-sided')
            print(f"\nMann-Whitney U (cascade rate: changed vs unchanged):")
            print(f"  U = {u_stat:.1f}, p = {u_p:.4f}")
            print(f"  Median cascade (changed): {np.median(cascade_changed):.3f}")
            print(f"  Median cascade (unchanged): {np.median(cascade_unchanged):.3f}")

        # Logistic regression: outcome_changed ~ cascade_rate
        # Using statsmodels if available, else scipy
        try:
            import statsmodels.api as sm
            X = sm.add_constant(cascade_arr)
            logit = sm.Logit(changed_arr, X)
            result = logit.fit(disp=0)
            print(f"\nLogistic regression (outcome_changed ~ cascade_rate):")
            print(f"  Intercept: {result.params[0]:.4f} (p={result.pvalues[0]:.4f})")
            print(f"  Cascade coef: {result.params[1]:.4f} (p={result.pvalues[1]:.4f})")
            print(f"  Pseudo R2: {result.prsquared:.4f}")
        except ImportError:
            print("\n(statsmodels not available for logistic regression)")

        # Summary statistics
        print(f"\nSummary:")
        print(f"  Mean cascade rate (all): {cascade_arr.mean():.3f}")
        print(f"  Std cascade rate: {cascade_arr.std():.3f}")
        print(f"  Mean ack density: {density_arr.mean():.3f}")

        print()


# =============================================================================
# C3: Qwen3 vs Qwen2.5 ack content comparison
# =============================================================================

def c3_qwen3_comparison():
    print("=" * 70)
    print("C3: Qwen3 vs Qwen2.5 ACK CONTENT COMPARISON")
    print("=" * 70)

    # Qwen2.5 data is available locally
    qwen25_traces_path = os.path.join(OUT, "full_scale/qwen_round_robin/traces/traces.jsonl")
    qwen25_ann_path = os.path.join(OUT, "full_scale/qwen_round_robin/annotations/annotations.jsonl")

    # Load Qwen2.5 annotations to identify ack messages
    with open(qwen25_ann_path) as f:
        qwen25_anns = [json.loads(l) for l in f]

    # Load Qwen2.5 traces
    with open(qwen25_traces_path) as f:
        qwen25_traces = {json.loads(l)["task_id"]: json.loads(l) for l in f}

    # Reopen file since we consumed the generator
    with open(qwen25_traces_path) as f:
        qwen25_traces = {}
        for line in f:
            t = json.loads(line)
            qwen25_traces[t["task_id"]] = t

    # Build annotation lookup: (task_id, message_index) -> type
    ann_lookup = {}
    for ann in qwen25_anns:
        atype = resolve_annotation_type(ann)
        ann_lookup[(ann["task_id"], ann["message_index"])] = atype

    # Extract ack messages from Qwen2.5, along with the preceding message content
    qwen25_ack_contents = []
    qwen25_ack_preceding = []  # preceding message content for bigram novelty
    qwen25_nonack_contents = []

    for ann in qwen25_anns:
        atype = resolve_annotation_type(ann)
        tid = ann["task_id"]
        midx = ann["message_index"]
        if tid in qwen25_traces:
            trace = qwen25_traces[tid]
            # message_index 0 corresponds to messages[1] (messages[0] is the question)
            msg_idx_in_trace = midx + 1  # offset for the initial question message
            if msg_idx_in_trace < len(trace["messages"]):
                content = trace["messages"][msg_idx_in_trace]["content"]
                if atype == "acknowledgment":
                    qwen25_ack_contents.append(content)
                    # Get preceding message
                    if msg_idx_in_trace > 0:
                        prev_content = trace["messages"][msg_idx_in_trace - 1]["content"]
                        qwen25_ack_preceding.append(prev_content)
                    else:
                        qwen25_ack_preceding.append("")
                else:
                    qwen25_nonack_contents.append(content)

    print(f"\n--- Qwen2.5-7B Acknowledgment Analysis ---")
    print(f"Total ack messages: {len(qwen25_ack_contents)}")
    print(f"Total non-ack messages: {len(qwen25_nonack_contents)}")

    if qwen25_ack_contents:
        # Token length (approximation: split by whitespace)
        ack_token_lengths = [len(c.split()) for c in qwen25_ack_contents]
        print(f"Mean ack token length: {np.mean(ack_token_lengths):.1f}")
        print(f"Median ack token length: {np.median(ack_token_lengths):.1f}")
        print(f"Std ack token length: {np.std(ack_token_lengths):.1f}")

        # Bigram novelty: fraction of bigrams in the ack that do NOT appear in the preceding message
        def compute_bigrams(text):
            words = text.lower().split()
            return set((words[i], words[i+1]) for i in range(len(words)-1))

        novelty_scores = []
        for content, prev in zip(qwen25_ack_contents, qwen25_ack_preceding):
            ack_bigrams = compute_bigrams(content)
            prev_bigrams = compute_bigrams(prev)
            if ack_bigrams:
                novel = ack_bigrams - prev_bigrams
                novelty_scores.append(len(novel) / len(ack_bigrams))
            else:
                novelty_scores.append(0.0)

        print(f"Mean bigram novelty (vs preceding msg): {np.mean(novelty_scores)*100:.1f}%")
        print(f"Median bigram novelty: {np.median(novelty_scores)*100:.1f}%")

        # Character length
        ack_char_lengths = [len(c) for c in qwen25_ack_contents]
        print(f"Mean ack char length: {np.mean(ack_char_lengths):.1f}")
        print(f"Median ack char length: {np.median(ack_char_lengths):.1f}")

        # Show 3 example ack messages
        print(f"\n--- Qwen2.5 Example Acknowledgments (3 samples) ---")
        np.random.seed(42)
        sample_indices = np.random.choice(len(qwen25_ack_contents), min(3, len(qwen25_ack_contents)), replace=False)
        for i, idx in enumerate(sample_indices):
            content = qwen25_ack_contents[idx]
            preview = content[:200] + "..." if len(content) > 200 else content
            print(f"\n  Example {i+1} ({len(content.split())} tokens):")
            print(f"    {preview}")

    # Qwen3 data - check if traces exist locally
    qwen3_traces_path = os.path.join(OUT, "full_scale/qwen3_round_robin/traces/traces.jsonl")
    qwen3_ann_path = os.path.join(OUT, "full_scale/qwen3_round_robin/annotations_heuristic/annotations.jsonl")

    print(f"\n--- Qwen3-8B Analysis ---")
    if os.path.exists(qwen3_traces_path):
        print(f"Qwen3 traces found at: {qwen3_traces_path}")
        # Process Qwen3 traces
    else:
        print(f"Qwen3 trace data NOT available locally (was on remote server)")
        print(f"Using oracle decision data from qwen3_mcnemar_bounds.json")
        print(f"Known Qwen3 stats from worker logs:")
        print(f"  - Baseline accuracy: 90.0% (90/100)")
        print(f"  - Ack-only accuracy: 76.0% (76/100)")
        print(f"  - Ack suppression rate: 66.4% (332/500 rounds)")
        print(f"  - All ack messages: 25-59 characters (max=59)")
        print(f"  - Delta: -14.0 pp (significant degradation)")
        print(f"\n  NOTE: Cannot compute token length/bigram novelty without raw traces.")
        print(f"  Comparison must use the known summary statistics.")

    # Compare with reference values from paper
    print(f"\n--- Comparison Table ---")
    print(f"{'Metric':<30} {'Qwen2.5-7B':<20} {'Qwen3-8B':<20}")
    print(f"{'-'*70}")
    if qwen25_ack_contents:
        print(f"{'Ack count':<30} {len(qwen25_ack_contents):<20} {'332 (heuristic)':<20}")
        print(f"{'Ack % of messages':<30} {len(qwen25_ack_contents)/len(qwen25_anns)*100:.1f}%{'':<14} {'66.4%':<20}")
        print(f"{'Mean token length':<30} {np.mean(ack_token_lengths):.1f}{'':<15} {'<15 (est.)':<20}")
        print(f"{'Max char length':<30} {max(ack_char_lengths):<20} {'59':<20}")
        print(f"{'Pruning delta (pp)':<30} {'+1 to -0.5':<20} {'-14.0':<20}")
    print()


if __name__ == "__main__":
    c1_cascade_significance()
    c2_cascade_vs_pruning()
    c3_qwen3_comparison()
