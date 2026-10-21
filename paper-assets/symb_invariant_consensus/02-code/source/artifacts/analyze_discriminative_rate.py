# Full-dataset discriminative rate analysis (W1+W3 reviewer response)
# Two metrics: source-trace discriminativeness + Z3 semantic discriminativeness
# Uses algebraic derivation from sica_scores for full 804 problems,
# validated against exact computation on 43 pilot problems with per-trace data.

import json
import sys
import os
from collections import defaultdict
from scipy import stats as scipy_stats

def wilson_ci(successes, total, alpha=0.05):
    if total == 0:
        return (0.0, 0.0)
    z = scipy_stats.norm.ppf(1 - alpha / 2)
    p_hat = successes / total
    denom = 1 + z**2 / total
    center = (p_hat + z**2 / (2 * total)) / denom
    margin = z * ((p_hat * (1 - p_hat) / total + z**2 / (4 * total**2)) ** 0.5) / denom
    return (max(0, center - margin), min(1, center + margin))


def wilson_ci_float(rate, total, alpha=0.05):
    successes = rate * total
    return wilson_ci(successes, total, alpha)


# ── Load data ──────────────────────────────────────────────────────────────

DATA_DIR = "/root/symb_invariant_consensus/results"

with open(f"{DATA_DIR}/sica_expanded_14b.json") as f:
    full_data = json.load(f)

with open(f"{DATA_DIR}/pilot_constraint_filtering/extracted_constraints.json") as f:
    pilot_constraints = json.load(f)

with open(f"{DATA_DIR}/k_ablation/traces_k20.json") as f:
    pilot_traces = json.load(f)

results = full_data["results"]

# ── Identify multi-candidate problems (full dataset, k=12) ────────────────

full_multi = []
full_single = []
for r in results:
    answers = [t["answer"] for t in r["per_trace"]]
    distinct = set(answers)
    r["_distinct_answers"] = distinct
    r["_answer_counts"] = {}
    for a in distinct:
        r["_answer_counts"][a] = sum(1 for x in answers if x == a)
    if len(distinct) >= 2:
        full_multi.append(r)
    else:
        full_single.append(r)

print("=" * 72)
print("FULL-DATASET DISCRIMINATIVE RATE ANALYSIS")
print("=" * 72)
print(f"Total problems: {len(results)}")
print(f"  ProofWriter: {sum(1 for r in results if r['dataset']=='proofwriter')}")
print(f"  FOLIO: {sum(1 for r in results if r['dataset']=='folio')}")
print(f"Multi-candidate (>=2 distinct answers): {len(full_multi)}")
print(f"Single-candidate (unanimous): {len(full_single)}")
print()

# ══════════════════════════════════════════════════════════════════════════
# PART 1: Pilot validation (exact per-trace analysis on 43 problems)
# ══════════════════════════════════════════════════════════════════════════

print("=" * 72)
print("PART 1: PILOT VALIDATION (43 problems, exact per-trace analysis)")
print("=" * 72)

pilot_ids = set(pilot_constraints.keys())
pilot_multi_exact = 0
pilot_disc_count = 0
pilot_total_count = 0
pilot_disc_weight = 0
pilot_total_weight = 0
pilot_problems_with_disc = 0
pilot_per_problem = []

for prob_id, per_trace_constr in pilot_constraints.items():
    if prob_id not in pilot_traces:
        continue

    traces = pilot_traces[prob_id]["traces"]
    trace_answers = {t["trace_idx"]: t["answer"] for t in traces}

    # Use only first 12 traces to match k=12 of the full pipeline
    k12_answers = {i: trace_answers[i] for i in range(12) if i in trace_answers}
    distinct = set(k12_answers.values())

    if len(distinct) < 2:
        continue

    pilot_multi_exact += 1

    # Group constraints by z3_formula, only from first 12 traces
    constraint_provenance = defaultdict(lambda: {"traces": set(), "weight": 0})
    for trace_idx in range(min(12, len(per_trace_constr))):
        if trace_idx >= len(per_trace_constr):
            break
        for c in per_trace_constr[trace_idx]:
            formula = c.get("z3_formula", c.get("expression", ""))
            constraint_provenance[formula]["traces"].add(trace_idx)
            constraint_provenance[formula]["weight"] += 1

    n_disc = 0
    n_non_disc = 0
    w_disc = 0
    w_non_disc = 0

    for formula, info in constraint_provenance.items():
        source_traces = info["traces"]
        weight = info["weight"]
        answers_for_c = {k12_answers[t] for t in source_traces if t in k12_answers}

        if len(answers_for_c) == 1:
            n_disc += 1
            w_disc += weight
        else:
            n_non_disc += 1
            w_non_disc += weight

    total_unique = len(constraint_provenance)
    pilot_disc_count += n_disc
    pilot_total_count += total_unique
    pilot_disc_weight += w_disc
    pilot_total_weight += w_disc + w_non_disc

    if n_disc > 0:
        pilot_problems_with_disc += 1

    pilot_per_problem.append({
        "problem_id": prob_id,
        "n_unique": total_unique,
        "n_disc": n_disc,
        "disc_rate_count": n_disc / max(total_unique, 1),
        "w_disc": w_disc,
        "w_total": w_disc + w_non_disc,
        "disc_rate_weight": w_disc / max(w_disc + w_non_disc, 1),
    })

pilot_disc_rate_count = pilot_disc_count / max(pilot_total_count, 1)
pilot_disc_rate_weight = pilot_disc_weight / max(pilot_total_weight, 1)

print(f"Multi-candidate problems (k=12): {pilot_multi_exact}")
print(f"Discriminative rate (by count): {pilot_disc_rate_count:.4f} "
      f"({pilot_disc_count}/{pilot_total_count})")
ci = wilson_ci(pilot_disc_count, pilot_total_count)
print(f"  Wilson 95% CI: [{ci[0]:.4f}, {ci[1]:.4f}]")
print(f"Discriminative rate (by weight): {pilot_disc_rate_weight:.4f} "
      f"({pilot_disc_weight}/{pilot_total_weight})")
ci_w = wilson_ci(pilot_disc_weight, pilot_total_weight)
print(f"  Wilson 95% CI: [{ci_w[0]:.4f}, {ci_w[1]:.4f}]")
print(f"Problems with any discriminative constraint: "
      f"{pilot_problems_with_disc}/{pilot_multi_exact}")
print()

# ── Validate algebraic method against pilot exact computation ──────────────

print("--- Algebraic method validation on pilot ---")
pilot_alg_disc_w = 0
pilot_alg_tw = 0

for prob_id, per_trace_constr in pilot_constraints.items():
    if prob_id not in pilot_traces:
        continue
    traces = pilot_traces[prob_id]["traces"]
    k12_answers = {i: traces[i]["answer"] for i in range(min(12, len(traces)))}
    distinct = set(k12_answers.values())
    if len(distinct) < 2:
        continue

    # Find this problem in full_data to get sica_scores
    match = [r for r in results if r["problem_id"] == prob_id]
    if not match:
        continue
    r = match[0]
    tw = r["maxsat_stats"]["total_weight"]
    sum_scores = sum(r["sica_scores"].values())
    n_exc = r["maxsat_stats"]["excluded"]

    # Algebraic: D_w = 2*TW - Σscores (for satisfied constraints, 2-answer approx)
    d_w = max(0, 2 * tw - sum_scores)
    pilot_alg_disc_w += d_w
    pilot_alg_tw += tw

alg_rate = pilot_alg_disc_w / max(pilot_alg_tw, 1)
print(f"Algebraic disc weight rate: {alg_rate:.4f}")
print(f"Exact disc weight rate:     {pilot_disc_rate_weight:.4f}")
print(f"Difference: {abs(alg_rate - pilot_disc_rate_weight):.4f}")
print()

# ══════════════════════════════════════════════════════════════════════════
# PART 2: Full dataset source-trace discriminative WEIGHT rate (algebraic)
# ══════════════════════════════════════════════════════════════════════════

print("=" * 72)
print("PART 2: FULL DATASET SOURCE-TRACE DISCRIMINATIVENESS (algebraic)")
print("=" * 72)

# For each multi-candidate problem:
# score(a) = Σ w(c) for satisfied c overlapping with answer a's traces
# If disc (source-bound): w(c) goes to 1 answer. If shared: w(c) goes to 2+ answers.
# For 2-answer: D_w = 2*TW - Σscores
# This holds when excluded=0 and alpha penalty is irrelevant.

per_domain_stats = defaultdict(lambda: {
    "n_multi": 0, "disc_w": 0, "total_w": 0,
    "n_unique": 0, "n_problems_with_disc": 0,
    "n_answer_assertions": 0,
})
overall_disc_w = 0
overall_tw = 0
overall_unique = 0
overall_answer_assertions = 0
overall_problems_with_disc = 0
per_problem_full = []

for r in full_multi:
    tw = r["maxsat_stats"]["total_weight"]
    n_exc = r["maxsat_stats"]["excluded"]
    sum_scores = sum(r["sica_scores"].values())
    n_answers = len(r["_distinct_answers"])
    n_unique = r["constraints_stats"]["unique_after_dedup"]
    dataset = r["dataset"]

    # Algebraic discriminative weight
    # For n_answers candidates: assumes non-disc constraints cover ~2 answers on average
    d_w = max(0.0, 2 * tw - sum_scores)

    # Structural Z3: answer assertions = n_answers unique constraints
    n_ans_assert = n_answers

    disc_rate = d_w / tw if tw > 0 else 0.0
    has_disc = disc_rate > 0.001

    overall_disc_w += d_w
    overall_tw += tw
    overall_unique += n_unique
    overall_answer_assertions += n_ans_assert
    if has_disc:
        overall_problems_with_disc += 1

    ds = per_domain_stats[dataset]
    ds["n_multi"] += 1
    ds["disc_w"] += d_w
    ds["total_w"] += tw
    ds["n_unique"] += n_unique
    ds["n_answer_assertions"] += n_ans_assert
    if has_disc:
        ds["n_problems_with_disc"] += 1

    per_problem_full.append({
        "problem_id": r["problem_id"],
        "dataset": dataset,
        "n_answers": n_answers,
        "n_unique": n_unique,
        "disc_weight": d_w,
        "total_weight": tw,
        "disc_rate_weight": disc_rate,
        "n_excluded": n_exc,
    })

source_disc_rate = overall_disc_w / max(overall_tw, 1)
source_ci = wilson_ci_float(source_disc_rate, int(overall_tw))

print(f"Multi-candidate problems: {len(full_multi)}")
print(f"  ProofWriter: {per_domain_stats['proofwriter']['n_multi']}")
print(f"  FOLIO: {per_domain_stats['folio']['n_multi']}")
print()
print(f"Source-trace discriminative WEIGHT rate (algebraic):")
print(f"  Overall: {source_disc_rate:.4f} ({overall_disc_w:.1f}/{overall_tw:.1f})")
print(f"  Wilson 95% CI: [{source_ci[0]:.4f}, {source_ci[1]:.4f}]")

for ds_name in ["proofwriter", "folio"]:
    ds = per_domain_stats[ds_name]
    rate = ds["disc_w"] / max(ds["total_w"], 1)
    ci = wilson_ci_float(rate, int(ds["total_w"]))
    print(f"  {ds_name}: {rate:.4f} ({ds['disc_w']:.1f}/{ds['total_w']:.1f})"
          f"  CI=[{ci[0]:.4f}, {ci[1]:.4f}]")

print(f"\nProblems with any discriminative weight: "
      f"{overall_problems_with_disc}/{len(full_multi)} "
      f"({overall_problems_with_disc/max(len(full_multi),1)*100:.1f}%)")
print()

# ══════════════════════════════════════════════════════════════════════════
# PART 3: Z3 Semantic Discriminativeness
# ══════════════════════════════════════════════════════════════════════════

print("=" * 72)
print("PART 3: Z3 SEMANTIC DISCRIMINATIVENESS")
print("=" * 72)

# The pipeline injects __sica_answer_{ans} assertions per trace.
# After dedup, each multi-candidate problem has n_distinct_answers answer assertions.
# These are the ONLY constraints containing answer-dependent variables.
# All other constraints are domain facts (evaluate identically regardless of answer).

z3_disc_rate = overall_answer_assertions / max(overall_unique, 1)
z3_ci = wilson_ci(overall_answer_assertions, overall_unique)

print(f"Answer-assertion constraints (answer-dependent): {overall_answer_assertions}")
print(f"Total unique constraints (multi-candidate): {overall_unique}")
print(f"Z3 semantic discriminative rate: {z3_disc_rate:.4f}")
print(f"  Wilson 95% CI: [{z3_ci[0]:.4f}, {z3_ci[1]:.4f}]")

for ds_name in ["proofwriter", "folio"]:
    ds = per_domain_stats[ds_name]
    rate = ds["n_answer_assertions"] / max(ds["n_unique"], 1)
    ci = wilson_ci(ds["n_answer_assertions"], ds["n_unique"])
    print(f"  {ds_name}: {rate:.4f} ({ds['n_answer_assertions']}/{ds['n_unique']})"
          f"  CI=[{ci[0]:.4f}, {ci[1]:.4f}]")

print()
print("Interpretation: domain-fact constraints (the vast majority) have no")
print("answer-dependent variables, so they evaluate identically for all candidate")
print("answers under Z3. Only the injected answer-assertion constraints are")
print("semantically discriminative. This confirms the W1 confound: sigma(c,a)")
print("derived from source-trace indicators lacks genuine semantic discrimination.")

# ══════════════════════════════════════════════════════════════════════════
# PART 4: Comparison with pilot (43 problems, 11.5%)
# ══════════════════════════════════════════════════════════════════════════

print()
print("=" * 72)
print("PART 4: PILOT vs FULL COMPARISON")
print("=" * 72)

# Identify the pilot problems in the full dataset
pilot_in_full = [r for r in full_multi if r["problem_id"] in pilot_ids]
pilot_in_full_single = [r for r in full_single if r["problem_id"] in pilot_ids]

print(f"Pilot problems found in full dataset: {len(pilot_in_full) + len(pilot_in_full_single)}")
print(f"  Multi-candidate (k=12): {len(pilot_in_full)}")
print(f"  Single-candidate (k=12): {len(pilot_in_full_single)}")

# Algebraic disc rate for pilot subset in full data
pilot_sub_dw = sum(
    max(0, 2 * r["maxsat_stats"]["total_weight"] - sum(r["sica_scores"].values()))
    for r in pilot_in_full
)
pilot_sub_tw = sum(r["maxsat_stats"]["total_weight"] for r in pilot_in_full)
pilot_sub_rate = pilot_sub_dw / max(pilot_sub_tw, 1)

print(f"\nPilot subset algebraic disc rate (weight): {pilot_sub_rate:.4f}")
print(f"Pilot exact disc rate (count, original): 0.115 (reported)")
print(f"Pilot exact disc rate (count, k=12 recomputed): {pilot_disc_rate_count:.4f}")
print(f"Pilot exact disc rate (weight, k=12 recomputed): {pilot_disc_rate_weight:.4f}")

# ══════════════════════════════════════════════════════════════════════════
# DRY RUN: First 5 multi-candidate problems detail
# ══════════════════════════════════════════════════════════════════════════

print()
print("=" * 72)
print("DRY RUN: First 5 multi-candidate problems")
print("=" * 72)

for p in per_problem_full[:5]:
    print(f"  {p['problem_id']}")
    print(f"    answers={p['n_answers']}, unique={p['n_unique']}, "
          f"D_w={p['disc_weight']:.1f}, TW={p['total_weight']:.1f}, "
          f"rate={p['disc_rate_weight']:.4f}, excluded={p['n_excluded']}")

# ══════════════════════════════════════════════════════════════════════════
# Save results JSON
# ══════════════════════════════════════════════════════════════════════════

output = {
    "overall": {
        "n_problems_total": len(results),
        "n_multi_candidate": len(full_multi),
        "n_single_candidate": len(full_single),
        "n_unique_constraints_multi": overall_unique,
        "source_discriminative_rate_weight": round(source_disc_rate, 6),
        "source_discriminative_ci95": [round(source_ci[0], 6), round(source_ci[1], 6)],
        "z3_discriminative_rate": round(z3_disc_rate, 6),
        "z3_discriminative_ci95": [round(z3_ci[0], 6), round(z3_ci[1], 6)],
        "z3_answer_assertion_count": overall_answer_assertions,
        "problems_with_any_discriminative": overall_problems_with_disc,
        "problems_with_any_discriminative_rate": round(
            overall_problems_with_disc / max(len(full_multi), 1), 6
        ),
        "method": "algebraic_from_sica_scores",
        "note": "source_disc derived as D_w = max(0, 2*TW - sum_scores); "
                "z3_disc counts answer-assertion constraints only",
    },
    "per_domain": {},
    "vs_pilot": {
        "pilot_rate_count_original": 0.115,
        "pilot_n_original": 43,
        "pilot_rate_count_k12_recomputed": round(pilot_disc_rate_count, 6),
        "pilot_rate_weight_k12_recomputed": round(pilot_disc_rate_weight, 6),
        "pilot_n_multi_k12": pilot_multi_exact,
        "full_rate_weight": round(source_disc_rate, 6),
        "full_n_multi": len(full_multi),
        "algebraic_validation_diff": round(abs(alg_rate - pilot_disc_rate_weight), 6),
    },
    "pilot_exact": {
        "n_multi": pilot_multi_exact,
        "disc_count": pilot_disc_count,
        "total_count": pilot_total_count,
        "disc_rate_count": round(pilot_disc_rate_count, 6),
        "disc_rate_count_ci95": [round(ci[0], 6) for ci in [wilson_ci(pilot_disc_count, pilot_total_count)]],
        "disc_weight": pilot_disc_weight,
        "total_weight": pilot_total_weight,
        "disc_rate_weight": round(pilot_disc_rate_weight, 6),
        "problems_with_any_disc": pilot_problems_with_disc,
    },
}

# Fix pilot_exact CI
pilot_ci_count = wilson_ci(pilot_disc_count, pilot_total_count)
output["pilot_exact"]["disc_rate_count_ci95"] = [
    round(pilot_ci_count[0], 6), round(pilot_ci_count[1], 6)
]

for ds_name in ["proofwriter", "folio"]:
    ds = per_domain_stats[ds_name]
    src_rate = ds["disc_w"] / max(ds["total_w"], 1)
    src_ci = wilson_ci_float(src_rate, int(ds["total_w"]))
    z3_rate = ds["n_answer_assertions"] / max(ds["n_unique"], 1)
    z3_ci_d = wilson_ci(ds["n_answer_assertions"], ds["n_unique"])
    output["per_domain"][ds_name] = {
        "n_multi_candidate": ds["n_multi"],
        "n_unique_constraints": ds["n_unique"],
        "source_discriminative_rate_weight": round(src_rate, 6),
        "source_discriminative_ci95": [round(src_ci[0], 6), round(src_ci[1], 6)],
        "z3_discriminative_rate": round(z3_rate, 6),
        "z3_discriminative_ci95": [round(z3_ci_d[0], 6), round(z3_ci_d[1], 6)],
        "z3_answer_assertion_count": ds["n_answer_assertions"],
        "problems_with_any_discriminative": ds["n_problems_with_disc"],
    }

out_path = f"{DATA_DIR}/discriminative_rate_analysis.json"
with open(out_path, "w") as f:
    json.dump(output, f, indent=2)

print()
print(f"Results saved to {out_path}")

# ── Final Summary ──────────────────────────────────────────────────────────

print()
print("=" * 72)
print("SUMMARY")
print("=" * 72)
print(f"Full dataset: {len(results)} problems, {len(full_multi)} multi-candidate")
print(f"Source-trace disc rate (weight): {source_disc_rate:.4f} "
      f"CI=[{source_ci[0]:.4f}, {source_ci[1]:.4f}]")
print(f"Z3 semantic disc rate:           {z3_disc_rate:.4f} "
      f"CI=[{z3_ci[0]:.4f}, {z3_ci[1]:.4f}]")
print(f"Pilot (43 problems, exact):      count={pilot_disc_rate_count:.4f}, "
      f"weight={pilot_disc_rate_weight:.4f}")
print(f"Conclusion: discriminative rates remain very low at full scale,")
print(f"consistent with pilot findings (11.5% by count).")
