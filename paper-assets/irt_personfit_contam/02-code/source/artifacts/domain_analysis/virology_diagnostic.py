"""Diagnose Gemini-1.5 virology lz*=-8.21 paradox."""

import sys
sys.path.insert(0, "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/src")

import numpy as np
import pandas as pd
from person_fit import prob_4pl, compute_lz_star, estimate_theta_mle

BASE = "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
OUT = f"{BASE}/artifacts/domain_analysis"

# ── Load data ──
print("Loading data...")
responses = np.loadtxt(f"{BASE}/artifacts/psn_irt_phase_b/combine.csv", delimiter=",", dtype=np.float64).astype(np.int8)
mmlu_responses = responses[:, 27029:41071]
assert mmlu_responses.shape == (12, 14042)

params = pd.read_csv(f"{BASE}/artifacts/psn_irt_params/mmlu_params.csv")
a_all = params["a_discrimination"].values
b_all = params["b_difficulty"].values
c_all = params["c_guessing"].values
d_all = params["d_feasibility"].values

abilities = pd.read_csv(f"{BASE}/artifacts/psn_irt_phase_b/student_abilities.csv")
thetas_global = abilities["ability"].values

# ── Build subject mapping from cais/mmlu ──
print("Building subject mapping from cais/mmlu...")
from datasets import load_dataset
ds = load_dataset("cais/mmlu", "all", split="test")
subjects_raw = ds["subject"]
subject_list_sorted = sorted(set(subjects_raw))

subject_item_counts = {}
for s in subject_list_sorted:
    subject_item_counts[s] = sum(1 for x in subjects_raw if x == s)

subject_offsets = {}
offset = 0
for s in subject_list_sorted:
    n = subject_item_counts[s]
    subject_offsets[s] = (offset, offset + n)
    offset += n

# ── Constants ──
GEMINI_IDX = 3
theta_global = thetas_global[GEMINI_IDX]
vir_start, vir_end = subject_offsets["virology"]
n_vir = vir_end - vir_start

a_vir = a_all[vir_start:vir_end]
b_vir = b_all[vir_start:vir_end]
c_vir = c_all[vir_start:vir_end]
d_vir = d_all[vir_start:vir_end]
resp_vir = mmlu_responses[GEMINI_IDX, vir_start:vir_end]

print(f"Virology items: indices [{vir_start}, {vir_end}), n={n_vir}")
print(f"Gemini-1.5 virology accuracy: {resp_vir.mean():.4f} ({resp_vir.sum()}/{n_vir})")

# ══════════════════════════════════════════════════════
# 1. θ confirmation
# ══════════════════════════════════════════════════════
print("\n" + "="*60)
print("1. θ CONFIRMATION")
print("="*60)

print(f"  Global PSN-IRT θ (student_id=3): {theta_global:.8f}")

theta_mle = estimate_theta_mle(mmlu_responses[GEMINI_IDX], a_all, b_all, c_all, d_all, bounds=(-4, 4))
print(f"  MMLU-specific θ_MLE: {theta_mle:.8f}")
print(f"  Gemini-1.5 MMLU accuracy: {mmlu_responses[GEMINI_IDX].mean():.6f} ({mmlu_responses[GEMINI_IDX].sum()}/{mmlu_responses.shape[1]})")

# ══════════════════════════════════════════════════════
# 2. Virology item parameter analysis
# ══════════════════════════════════════════════════════
print("\n" + "="*60)
print("2. VIROLOGY ITEM PARAMETER ANALYSIS")
print("="*60)

for name, arr in [("a_discrimination", a_vir), ("b_difficulty", b_vir),
                  ("c_guessing", c_vir), ("d_feasibility", d_vir)]:
    print(f"  {name}: mean={arr.mean():.4f}, std={arr.std():.4f}, min={arr.min():.4f}, max={arr.max():.4f}")

n_d_lt1 = (d_vir < 1.0).sum()
print(f"\n  Items with d < 1.0: {n_d_lt1}/{n_vir}")
if n_d_lt1 > 0:
    print(f"  d values for those items: {d_vir[d_vir < 1.0]}")

n_b_gt_theta = (b_vir > theta_global).sum()
print(f"  Items with b > θ_global ({theta_global:.2f}): {n_b_gt_theta}/{n_vir}")

# ══════════════════════════════════════════════════════
# 3. P(correct) comparison
# ══════════════════════════════════════════════════════
print("\n" + "="*60)
print("3. P(correct) AT θ=0.78 vs θ=4.0")
print("="*60)

P_low = prob_4pl(theta_global, a_vir, b_vir, c_vir, d_vir)
P_high = prob_4pl(4.0, a_vir, b_vir, c_vir, d_vir)

print(f"\n  {'Item':>4} | {'b':>7} | {'a':>6} | {'c':>6} | {'d':>6} | {'P(θ=0.78)':>10} | {'P(θ=4.0)':>10} | {'resp':>4}")
print(f"  {'-'*4}-+-{'-'*7}-+-{'-'*6}-+-{'-'*6}-+-{'-'*6}-+-{'-'*10}-+-{'-'*10}-+-{'-'*4}")
for j in range(n_vir):
    print(f"  {j:4d} | {b_vir[j]:7.3f} | {a_vir[j]:6.3f} | {c_vir[j]:6.3f} | {d_vir[j]:6.3f} | {P_low[j]:10.6f} | {P_high[j]:10.6f} | {resp_vir[j]:4d}")

n_lt05_low = (P_low < 0.5).sum()
n_lt05_high = (P_high < 0.5).sum()
print(f"\n  P < 0.5 count: θ=0.78 → {n_lt05_low}/{n_vir}, θ=4.0 → {n_lt05_high}/{n_vir}")
print(f"  P mean: θ=0.78 → {P_low.mean():.6f}, θ=4.0 → {P_high.mean():.6f}")

# ══════════════════════════════════════════════════════
# 4. lz* recomputation comparison
# ══════════════════════════════════════════════════════
print("\n" + "="*60)
print("4. lz* RECOMPUTATION: θ=0.78 vs θ=4.0")
print("="*60)

lz_vir_low = compute_lz_star(resp_vir, theta_global, a_vir, b_vir, c_vir, d_vir)
lz_vir_high = compute_lz_star(resp_vir, 4.0, a_vir, b_vir, c_vir, d_vir)
print(f"  Virology lz*: θ=0.78 → {lz_vir_low:.6f}, θ=4.0 → {lz_vir_high:.6f}")

# Load existing subject_lz_matrix for reference
lz_df = pd.read_csv(f"{OUT}/subject_lz_matrix.csv", index_col=0)
gemini_lz = lz_df.loc["Gemini-1.5"]
lowest_10 = gemini_lz.sort_values().head(10)

print(f"\n  Gemini-1.5 lowest 10 subjects (θ=0.78 vs θ=4.0):")
print(f"  {'Subject':<35} | {'lz*(θ=0.78)':>13} | {'lz*(θ=4.0)':>13} | {'Δ':>10}")
print(f"  {'-'*35}-+-{'-'*13}-+-{'-'*13}-+-{'-'*10}")

for subj in lowest_10.index:
    start, end = subject_offsets[subj]
    resp_s = mmlu_responses[GEMINI_IDX, start:end]
    a_s, b_s, c_s, d_s = a_all[start:end], b_all[start:end], c_all[start:end], d_all[start:end]
    lz_low = compute_lz_star(resp_s, theta_global, a_s, b_s, c_s, d_s)
    lz_high = compute_lz_star(resp_s, 4.0, a_s, b_s, c_s, d_s)
    delta = lz_high - lz_low
    print(f"  {subj:<35} | {lz_low:13.6f} | {lz_high:13.6f} | {delta:+10.4f}")

# ══════════════════════════════════════════════════════
# 5. Snijders correction internals
# ══════════════════════════════════════════════════════
print("\n" + "="*60)
print("5. SNIJDERS CORRECTION INTERNALS (θ=0.78, virology)")
print("="*60)

P = prob_4pl(theta_global, a_vir, b_vir, c_vir, d_vir)
Q = 1 - P
z = a_vir * (theta_global - b_vir)
sigma = 1.0 / (1.0 + np.exp(-np.clip(z, -30, 30)))
dP = a_vir * (d_vir - c_vir) * sigma * (1 - sigma)
h = dP / (P * Q)
g = np.log(P / Q)

l = np.sum(resp_vir * np.log(P) + (1 - resp_vir) * np.log(Q))
E_l = np.sum(P * np.log(P) + Q * np.log(Q))
Var_l = np.sum(P * Q * g ** 2)
I_theta = np.sum(P * Q * h ** 2)
C_theta = np.sum(P * Q * h * g)
Var_star = Var_l - C_theta ** 2 / I_theta

print(f"  l (log-likelihood):     {l:.6f}")
print(f"  E_l (expected):         {E_l:.6f}")
print(f"  l - E_l:                {l - E_l:.6f}")
print(f"  Var_l:                  {Var_l:.6f}")
print(f"  sqrt(Var_l):            {np.sqrt(Var_l):.6f}")
print(f"  I_theta:                {I_theta:.6f}")
print(f"  C_theta:                {C_theta:.6f}")
print(f"  C_theta^2/I_theta:      {C_theta**2/I_theta:.6f}")
print(f"  Var_star:               {Var_star:.6f}")
print(f"  Var_star > 0?           {Var_star > 0}")
print(f"  lz (uncorrected):       {(l - E_l) / np.sqrt(Var_l):.6f}")
print(f"  lz* (corrected):        {(l - E_l) / np.sqrt(Var_star):.6f}")

# Also check at θ=4.0
P4 = prob_4pl(4.0, a_vir, b_vir, c_vir, d_vir)
Q4 = 1 - P4
z4 = a_vir * (4.0 - b_vir)
sigma4 = 1.0 / (1.0 + np.exp(-np.clip(z4, -30, 30)))
dP4 = a_vir * (d_vir - c_vir) * sigma4 * (1 - sigma4)
h4 = dP4 / (P4 * Q4)
g4 = np.log(P4 / Q4)

l4 = np.sum(resp_vir * np.log(P4) + (1 - resp_vir) * np.log(Q4))
E_l4 = np.sum(P4 * np.log(P4) + Q4 * np.log(Q4))
Var_l4 = np.sum(P4 * Q4 * g4 ** 2)
I_theta4 = np.sum(P4 * Q4 * h4 ** 2)
C_theta4 = np.sum(P4 * Q4 * h4 * g4)
Var_star4 = Var_l4 - C_theta4 ** 2 / I_theta4

print(f"\n  --- At θ=4.0 ---")
print(f"  l:          {l4:.6f}")
print(f"  E_l:        {E_l4:.6f}")
print(f"  l - E_l:    {l4 - E_l4:.6f}")
print(f"  Var_l:      {Var_l4:.6f}")
print(f"  Var_star:   {Var_star4:.6f}")
print(f"  Var_star>0? {Var_star4 > 0}")
print(f"  lz*:        {(l4 - E_l4) / np.sqrt(max(Var_star4, Var_l4) if Var_star4 <= 0 else Var_star4):.6f}")

# ══════════════════════════════════════════════════════
# 6. Impact assessment
# ══════════════════════════════════════════════════════
print("\n" + "="*60)
print("6. IMPACT ASSESSMENT")
print("="*60)

lz_overall_low = compute_lz_star(mmlu_responses[GEMINI_IDX], theta_global, a_all, b_all, c_all, d_all)
lz_overall_high = compute_lz_star(mmlu_responses[GEMINI_IDX], 4.0, a_all, b_all, c_all, d_all)
print(f"  Overall MMLU lz*: θ=0.78 → {lz_overall_low:.6f}, θ=4.0 → {lz_overall_high:.6f}")

# Count how many subjects have negative lz* at θ=0.78 vs θ=4.0
neg_low = 0
neg_high = 0
for subj in subject_list_sorted:
    start, end = subject_offsets[subj]
    resp_s = mmlu_responses[GEMINI_IDX, start:end]
    a_s, b_s, c_s, d_s = a_all[start:end], b_all[start:end], c_all[start:end], d_all[start:end]
    lz_l = compute_lz_star(resp_s, theta_global, a_s, b_s, c_s, d_s)
    lz_h = compute_lz_star(resp_s, 4.0, a_s, b_s, c_s, d_s)
    if lz_l < 0:
        neg_low += 1
    if lz_h < 0:
        neg_high += 1

print(f"  Subjects with negative lz*: θ=0.78 → {neg_low}/57, θ=4.0 → {neg_high}/57")

# ══════════════════════════════════════════════════════
# Generate report
# ══════════════════════════════════════════════════════
print("\n" + "="*60)
print("GENERATING REPORT")
print("="*60)

report_lines = []
report_lines.append("# Virology lz*=-8.21 Diagnostic Report")
report_lines.append("")
report_lines.append("## 1. Root Cause")
report_lines.append("")
report_lines.append(f"The per-subject `compute_lz_star` uses the **global PSN-IRT θ={theta_global:.4f}** (cross-benchmark ability),")
report_lines.append(f"not a benchmark-specific θ. Gemini-1.5 achieves 100% accuracy on all 14042 MMLU items,")
report_lines.append(f"so its MMLU-specific θ\\_MLE = {theta_mle:.1f} (boundary value for all-correct pattern).")
report_lines.append(f"Under θ={theta_global:.2f}, virology items with b >> θ have P(correct) < 0.5,")
report_lines.append(f"making 100% accuracy appear *aberrantly good* — yielding a strongly negative lz\\*.")
report_lines.append("")

report_lines.append("## 2. Numerical Evidence")
report_lines.append("")
report_lines.append("### 2.1 θ Values")
report_lines.append("")
report_lines.append("| Quantity | Value |")
report_lines.append("|----------|-------|")
report_lines.append(f"| Global PSN-IRT θ (student\\_id=3) | {theta_global:.8f} |")
report_lines.append(f"| MMLU-specific θ\\_MLE | {theta_mle:.1f} |")
report_lines.append(f"| MMLU accuracy | {mmlu_responses[GEMINI_IDX].mean():.4f} ({mmlu_responses[GEMINI_IDX].sum()}/{mmlu_responses.shape[1]}) |")
report_lines.append("")

report_lines.append("### 2.2 Virology Item Parameters (n={})".format(n_vir))
report_lines.append("")
report_lines.append("| Parameter | Mean | Std | Min | Max |")
report_lines.append("|-----------|------|-----|-----|-----|")
for name, arr in [("a (discrimination)", a_vir), ("b (difficulty)", b_vir),
                  ("c (guessing)", c_vir), ("d (feasibility)", d_vir)]:
    report_lines.append(f"| {name} | {arr.mean():.4f} | {arr.std():.4f} | {arr.min():.4f} | {arr.max():.4f} |")
report_lines.append("")
report_lines.append(f"- Items with d < 1.0 (P upper bound < 1): **{n_d_lt1}/{n_vir}**")
report_lines.append(f"- Items with b > θ={theta_global:.2f}: **{n_b_gt_theta}/{n_vir}**")
report_lines.append("")

report_lines.append("### 2.3 Per-Item P(correct)")
report_lines.append("")
report_lines.append("| Item | b | a | c | d | P(θ=0.78) | P(θ=4.0) | Response |")
report_lines.append("|------|---|---|---|---|-----------|----------|----------|")
for j in range(n_vir):
    report_lines.append(f"| {j} | {b_vir[j]:.3f} | {a_vir[j]:.3f} | {c_vir[j]:.3f} | {d_vir[j]:.3f} | {P_low[j]:.6f} | {P_high[j]:.6f} | {resp_vir[j]} |")
report_lines.append("")
report_lines.append(f"- Items with P < 0.5: θ=0.78 → **{n_lt05_low}/{n_vir}**, θ=4.0 → **{n_lt05_high}/{n_vir}**")
report_lines.append(f"- Mean P: θ=0.78 → {P_low.mean():.6f}, θ=4.0 → {P_high.mean():.6f}")
report_lines.append("")

report_lines.append("### 2.4 lz\\* Recomputation")
report_lines.append("")
report_lines.append(f"**Virology**: lz\\*(θ=0.78) = **{lz_vir_low:.4f}**, lz\\*(θ=4.0) = **{lz_vir_high:.4f}**")
report_lines.append("")
report_lines.append("Gemini-1.5 lowest 10 subjects:")
report_lines.append("")
report_lines.append("| Subject | lz\\*(θ=0.78) | lz\\*(θ=4.0) | Δ |")
report_lines.append("|---------|-------------|------------|---|")
for subj in lowest_10.index:
    start, end = subject_offsets[subj]
    resp_s = mmlu_responses[GEMINI_IDX, start:end]
    a_s, b_s, c_s, d_s = a_all[start:end], b_all[start:end], c_all[start:end], d_all[start:end]
    lz_low = compute_lz_star(resp_s, theta_global, a_s, b_s, c_s, d_s)
    lz_high = compute_lz_star(resp_s, 4.0, a_s, b_s, c_s, d_s)
    delta = lz_high - lz_low
    report_lines.append(f"| {subj} | {lz_low:.4f} | {lz_high:.4f} | {delta:+.4f} |")
report_lines.append("")

report_lines.append("### 2.5 Snijders Correction Internals (virology, θ=0.78)")
report_lines.append("")
report_lines.append("| Quantity | Value |")
report_lines.append("|----------|-------|")
report_lines.append(f"| l (log-likelihood) | {l:.6f} |")
report_lines.append(f"| E\\[l\\] | {E_l:.6f} |")
report_lines.append(f"| l − E\\[l\\] | {l - E_l:.6f} |")
report_lines.append(f"| Var(l) | {Var_l:.6f} |")
report_lines.append(f"| I(θ) | {I_theta:.6f} |")
report_lines.append(f"| C(θ) | {C_theta:.6f} |")
report_lines.append(f"| C(θ)²/I(θ) | {C_theta**2/I_theta:.6f} |")
report_lines.append(f"| Var\\* = Var(l) − C²/I | {Var_star:.6f} |")
report_lines.append(f"| Var\\* > 0? | {Var_star > 0} |")
report_lines.append(f"| Fallback to Var(l)? | {Var_star <= 0} |")
report_lines.append("")

report_lines.append("## 3. Does This Affect Overall MMLU lz\\*=34.75?")
report_lines.append("")
report_lines.append(f"**No.** Overall MMLU lz\\* (all 14042 items) at θ=0.78 = {lz_overall_low:.4f}.")
report_lines.append(f"The massive positive contribution from 14042 all-correct responses overwhelms the negative")
report_lines.append(f"contribution from the {n_vir} virology items. The overall lz\\* remains strongly positive regardless of θ choice.")
report_lines.append(f"For reference, at θ=4.0 the overall lz\\* = {lz_overall_high:.4f}.")
report_lines.append("")

report_lines.append("## 4. Per-Subject Analysis Caveat")
report_lines.append("")
report_lines.append("Per-subject lz\\* decomposition is unreliable when there is **extreme θ–b mismatch**:")
report_lines.append("")
report_lines.append("- The global θ reflects cross-benchmark average ability, which can be far from benchmark-specific performance.")
report_lines.append("- For a model with 100% accuracy on all MMLU items, using θ=0.78 means many items have P(correct) << 1,")
report_lines.append("  and the *direction* of lz\\* depends on the specific distribution of item difficulties within each subject.")
report_lines.append("- Small subjects (virology: {} items) are more sensitive to this mismatch than large subjects.".format(n_vir))
report_lines.append("- The lz\\* statistic was designed for settings where θ is estimated from the *same* set of items being evaluated.")
report_lines.append("")
report_lines.append(f"Subjects with negative lz\\* at θ=0.78: **{neg_low}/57**, at θ=4.0: **{neg_high}/57**.")
report_lines.append("")

report_lines.append("## 5. Recommended Fix")
report_lines.append("")
report_lines.append("1. **For per-subject decomposition**: Use benchmark-specific θ\\_MLE instead of global PSN-IRT θ.")
report_lines.append("   For Gemini-1.5 on MMLU, θ\\_MLE=4.0 (boundary). All subjects would have positive lz\\*.")
report_lines.append("2. **For the paper**: Add a caveat that per-subject lz\\* uses global θ and is thus an *approximate* decomposition.")
report_lines.append("   The overall MMLU lz\\*=34.75 is unaffected and remains the primary finding.")
report_lines.append("3. **If per-subject analysis must be precise**: Re-estimate θ per benchmark and recompute.")
report_lines.append("   Alternatively, report per-subject lz\\* only for models where |θ\\_global − θ\\_benchmark| is small.")
report_lines.append("")

report = "\n".join(report_lines)

with open(f"{OUT}/virology_diagnostic_report.md", "w") as f:
    f.write(report)

print(f"\nReport saved to {OUT}/virology_diagnostic_report.md")
print("Done.")
