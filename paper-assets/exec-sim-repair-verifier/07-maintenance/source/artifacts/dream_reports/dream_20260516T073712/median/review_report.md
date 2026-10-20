---
dream_id: dream_20260516T073712
tier: median
overall_score: weak reject
timestamp: 2026-05-16T08:28:50.819029+00:00
---

# Dream Review Report: Per-Test Classification for Code Execution Simulation

**Paper**: "Per-Test Classification for Code Execution Simulation: Classification Works Where Generation Fails"
**Review Mode**: Full (2 Reviewers, 4-Step Roundtable)
**Date**: 2026-05-16

---

## Roundtable Summary

| Reviewer | Focus | Score | Confidence |
|----------|-------|-------|------------|
| R1 | Methods + Experiments | 3/6 (Weak Reject) | 4/5 |
| R2 | Novelty + Related Work | 3/6 (Weak Reject) | 4/5 → 5/5 after cross-share |
| **Consensus** | | **3/6 (Weak Reject)** | **4.5/5** |

Both reviewers independently arrived at Weak Reject and maintained their scores after cross-sharing. Convergence was strong on the central weaknesses; no significant disagreements emerged.

---

## Step 1: Independent Reviews

### R1 (Methods + Experiments): 3/6 — Weak Reject

**Strengths:**
- S1: Careful controlled comparison design — same base models, LoRA config, training data, compute budget, and matched seeds. Isolates formulation effects cleanly.
- S2: Appropriate statistical methodology — clustered bootstrap (114 clusters, 10K resamples) for within-problem correlation, TOST equivalence test (correct for the equivalence claim), ICC analysis with design effect calculations.
- S3: Unusually honest about negative/null results — 4B gap p≈0.06, re-repair p=0.11, majority voting hurts, P2P regression negligible, DeepSeek reversal reported transparently.
- S4: Oracle accuracy-utility framework produces testable predictions validated empirically; ICC sensitivity analysis is principled.
- S5: Comprehensive ablations — LoRA rank sensitivity, majority voting, mutation-type breakdown, cross-architecture (DeepSeek).
- S6: Good reproducibility infrastructure — hyperparameters fully specified, seeds reported, standard HF/PEFT APIs.

**Weaknesses:**
- W1 (Major): **Repo-level CWM comparison is fundamentally confounded.** The 50–93% unparseable rate means CWM essentially did not produce valid outputs. This is documented as a formulation finding ("complexity-dependent advantage") but more parsimoniously interpreted as an implementation failure of LoRA fine-tuned CWM at small scale. The paper acknowledges this in a limitations paragraph but the main narrative treats the 19–26pp gap as evidence for the core claim.
- W2 (Major): **Single-seed repo-level comparisons.** Both CLS 4B and CLS 8B repo-level results rest primarily on seed42. The second CLS 4B seed (seed123) achieves only 75.33% — barely above majority baseline — revealing high checkpoint sensitivity. No confidence intervals are possible from single-seed comparisons.
- W3: **CWM 8B "degradation" (−0.23pp) may reflect hyperparameter transfer failure** — same LR/LoRA config used for 4B and 8B. Larger models commonly need different learning rates.
- W4: **TOST ±2pp margin is unjustified.** The paper does not explain why 2pp is an appropriate practical equivalence threshold. Additionally, 2 of 5 seeds used NF4 quantization while 3 used bf16, introducing a heterogeneity confound.
- W5: **Synthetic mutations only.** Five mutation operators (operator_swap, off_by_one, return_value, boundary_removal, gold) on HumanEval/MBPP generate a narrow bug distribution. Repo-level data is also synthetically mutated, not real developer patches. The entire pipeline operates in a synthetic-mutation bubble.
- W6: **No meaningful downstream validation.** The re-repair pilot (n=120, p=0.11, net +5 instances) is underpowered and inconclusive. Claim 2 ("diagnostic granularity") is supported only by showing per-test *can* identify which tests fail, not that this is *useful* in practice.
- W7: **DeepSeek reversal undermines generalizability.** CWM outperforms CLS by 0.7pp on DeepSeek-Coder-6.7B, reversing the Qwen finding. This suggests the CLS advantage may be architecture-specific rather than a general formulation property.

**Questions:**
- Q1: Has CWM been tried with structured output format (e.g., JSON), full fine-tuning, or max_new_tokens beyond 1024?
- Q2: What happens with TOST restricted to the 3 bf16 seeds only?
- Q3: Learning rate discrepancy: code shows 2e-4 default, paper Table 7 states 5e-5. Which was actually used?
- Q4: DeepSeek reversal — how many seeds? What is DeepSeek repo-level CWM performance?

### R2 (Novelty + Related Work): 3/6 — Weak Reject

**Strengths:**
- S1: Honest framing — does not overclaim novelty of the classification formulation itself. Contribution is explicitly empirical.
- S2: Related work section is more developed than it initially appears (22 references, 5 themed paragraphs), with explicit positioning against LEVER and CodeT.
- S3: NLP task-reformulation paragraph provides useful intellectual context connecting to broader literature.
- S4: Transparent about all mixed and negative results.

**Weaknesses:**
- W1 (Major): **Core idea is technically straightforward.** Per-test binary classification for code correctness is the simplest possible formulation. LEVER (ICML 2023) already trains classifiers for execution correctness prediction. The novelty lies entirely in the systematic comparison, which is thin for a ~25% acceptance rate venue.
- W2 (Major): **CWM comparison is against authors' own LoRA reproduction at 4B/8B, not the original 32B CWM.** The original CWM was designed and trained at 32B scale with execution traces. Comparing against a capacity-limited LoRA variant and declaring "generation fails" is potentially misleading. The paper does caveat this but the narrative still draws formulation-level conclusions from capacity-limited evidence.
- W3: **Missing important conceptual connections:**
  - **PRM vs ORM parallel** (Lightman et al., 2023; Wang et al., 2024): Per-test vs trajectory-level directly parallels process vs outcome reward models. The finding that per-test advantage concentrates in multi-test instances mirrors PRM findings in math reasoning. This is the most significant missing connection.
  - **Fault localization literature** (Ochiai, Tarantula, spectrum-based FL): Per-test verdicts are essentially a fault localization signal. Entirely absent.
  - **SWE-Judge** and other LLM-as-judge approaches for SWE-bench.
  - **RepoExec**, **CodeScore**, **LiveCodeBench** for execution prediction benchmarks.
- W4: **VG-Search** (Chen et al., 2025) directly studies verification granularity — the paper's core question — but gets only one-clause treatment.
- W5: No discussion of concurrent work on execution-free verification in production systems.

**Questions:**
- Q1: How is per-test CLS meaningfully different from LEVER applied at the per-test level?
- Q2: Have the authors considered that generation may simply need more capacity or specialized training (as the original 32B CWM was designed)?
- Q3: How does this work relate to PRM vs ORM in mathematical reasoning?
- Q4: Without downstream validation, is the per-test granularity advantage mostly theoretical?

---

## Step 2: Cross-Sharing Reactions

### R1's Reaction to R2

- **Partially agrees on novelty** but considers R2's 2/5 slightly harsh — the controlled comparison methodology itself has value. Suggests 2.5/5.
- **Strongly agrees the PRM vs ORM parallel is a significant omission** that R1 missed in the original review. Would strengthen theoretical grounding.
- **Confirms convergence on CWM comparison weakness**: R1's methods critique (confounded comparison) and R2's positioning critique (unfair to generation) are two facets of the same fundamental problem. Together they form the paper's most serious weakness.
- **Minor disagreement**: R1 thinks VG-Search one-sentence treatment is adequate; missing PRM/ORM and fault localization literature is more consequential than missing individual benchmarks.
- **Score maintained at 3/6** but notes a revision addressing CWM confound + PRM connection could move to 4.

### R2's Reaction to R1

- **Agrees R1's repo-level confound critique is sharper and more damaging** than R2's original framing. The 50–93% unparseable rate makes the comparison scientifically uninformative.
- **Alarmed by seed123 CLS 4B repo-level at 75.33%** — missed this in original review. Repo-level story rests almost entirely on a single seed.
- **Agrees learning rate discrepancy (code 2e-4 vs paper 5e-5)** is a reproducibility defect that could explain CWM 8B "degradation."
- **Accepts TOST margin criticism** — 2pp feels suspiciously convenient, just wide enough to capture observed gap.
- **Accepts synthetic mutation concern** — should have flagged this originally.
- **Score maintained at 3/6**, confidence increased to 5/5. Notes: "The function-level results are clean but incremental (1-2pp); the repo-level results are dramatic but unreliable. The paper falls between these two stories without convincingly delivering either."

---

## Step 3: Convergence

### Points of Strong Agreement (Both Reviewers)

1. **The repo-level CWM comparison is the paper's most serious problem.** From methods (R1): it's a confounded comparison where implementation failure masquerades as formulation failure. From positioning (R2): it's an unfair comparison against a handicapped baseline. Together: the paper's most dramatic result (25pp gap, 93% unparseable) is scientifically uninformative about whether classification is inherently superior to generation.

2. **Single-seed repo-level instability** fatally undermines the repo-level story. The seed123 CLS 4B at 75.33% shows that the repo-level results are checkpoint-dependent artifacts, not robust findings.

3. **The function-level results are clean but modest.** 1.24pp at 4B (p≈0.06, not significant) and 2.43pp at 8B (consistent direction but only 3 seeds) are real but do not constitute a strong contribution by themselves.

4. **Statistical methodology is a genuine strength.** Clustered bootstrap, TOST, ICC analysis — all appropriate and carefully implemented.

5. **Honesty about negative results is commendable** — this level of transparency is rare and should be preserved in revision.

6. **The paper lacks a convincing downstream story.** Re-repair pilot (p=0.11, n=120) does not validate the practical motivation.

### Points of Mild Disagreement

1. **Novelty severity**: R1 considers R2's 2/5 slightly harsh (suggests 2.5/5), viewing the systematic comparison methodology as having independent value. R2 maintains that for a top venue, "the obvious thing works and we measured when" is insufficient.

2. **VG-Search engagement**: R1 considers one-sentence adequate; R2 wants deeper discussion. Minor.

### Consensus Score: 3/6 (Weak Reject)

---

## Step 4: Consolidated Assessment

### Paper Contributions (as claimed vs. as supported)

| Claim | As Claimed | As Supported | Assessment |
|-------|-----------|-------------|------------|
| C1: Complexity-dependent formulation advantage | CLS > CWM, scaling with complexity | Function-level: modest (1–2pp, borderline significant). Repo-level: CWM implementation failure, not formulation comparison. DeepSeek reverses direction. | **Partially supported** (function-level only, modest effect) |
| C2: Diagnostic granularity at equivalent accuracy | Per-test ≈ trajectory (TOST p=0.007) | Statistically demonstrated but margin choice (±2pp) unjustified; mixed-precision confound; no downstream validation | **Methodologically supported but practically unvalidated** |
| C3: Accuracy-utility frontier (T≥2 advantage) | Per-test advantage in 31.3% of SWE-bench | Oracle analysis is principled and well-executed | **Well supported** (strongest contribution) |

### What Would Change Our Assessment

A revision addressing the following could move both reviewers to Weak Accept (4/6):

1. **Multi-seed repo-level experiments** (≥3 seeds for both CLS and CWM at both scales) with confidence intervals.
2. **Stronger CWM baseline** — either compare against the original 32B CWM, or try structured output format / longer generation / full fine-tuning to establish that the failure persists despite engineering effort.
3. **Justify the TOST margin** empirically (e.g., from downstream task sensitivity) or use a data-driven margin.
4. **Add PRM/ORM and fault localization connections** to related work.
5. **Resolve the learning rate discrepancy** and clarify actual training configurations.
6. Either **power up the re-repair experiment** (n≥400 per power analysis) or **drop the downstream utility framing** and reposition as a pure formulation comparison study.

### Strengths to Preserve

- The controlled comparison methodology is exemplary and should be the template for future formulation comparison papers.
- The statistical framework (clustered bootstrap, TOST, ICC, design effect) is more sophisticated than typical ML papers.
- The honesty about negative and mixed results (DeepSeek reversal, non-significant re-repair, majority voting failure, P2P negative finding) is refreshing.
- The oracle F2P-stratified analysis (Claim 3) is the paper's cleanest and most actionable contribution.

### Final Verdict

**Weak Reject (3/6).** The paper asks an important question (does formulation matter for code verification?) and uses sound methodology, but the evidence does not fully support the claims. The function-level story is clean but incremental (1–2pp effects). The repo-level story is dramatic but unreliable (single-seed, confounded CWM comparison, seed instability). The paper falls between these two narratives without convincingly delivering either. The technical novelty of per-test binary classification is low (LEVER precedent), and the missing PRM/ORM conceptual connection represents a significant gap in positioning. With multi-seed repo-level experiments, a stronger generation baseline, and the conceptual improvements suggested above, this could become a solid empirical contribution at a top venue.

### Detailed Scores

| Dimension | R1 | R2 | Consensus |
|-----------|----|----|-----------|
| Soundness | 3/5 | — | 3/5 |
| Empirical Rigor | 3/5 | — | 3/5 |
| Reproducibility | 4/5 | — | 3.5/5 (downgraded for LR discrepancy) |
| Novelty | — | 2/5 | 2.5/5 |
| Related Work | — | 3/5 | 3/5 |
| Significance | — | 3/5 | 3/5 |
| **Overall** | **3/6** | **3/6** | **3/6 (Weak Reject)** |
| Confidence | 4/5 | 5/5 | 4.5/5 |
