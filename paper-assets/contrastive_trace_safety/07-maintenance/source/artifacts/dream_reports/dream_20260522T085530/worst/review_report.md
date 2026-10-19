---
dream_id: dream_20260522T085530
tier: worst
overall_score: 2.5 — Borderline Findings
timestamp: 2026-05-22T10:13:39.910943+00:00
---

# Dream Review Report — Full Roundtable

**Paper**: "Layer Selection Matters: How Metric Choice Determines Hidden-State Probe Effectiveness for Reasoning-Model Safety Monitoring"
**Venue**: EMNLP 2026 (ARR)
**Review Mode**: Full (2 Reviewers + Roundtable)

---

## Roundtable Protocol

- **R1** (Methods + Experiments): Focused on statistical rigor, experimental design, sample sizes, multiplicity
- **R2** (Novelty + Related Work): Focused on contribution significance, positioning, external validity

### Step 1: Independent Reviews — Complete
### Step 2: Cross-Sharing — Key Exchanges
### Step 3: Convergence — Score Reconciliation
### Step 4: Consolidated Report — Below

---

## 1. Paper Summary

This paper investigates hidden-state (HS) probing for detecting "safety commitment points" in reasoning-model chains-of-thought, where the model transitions from safe deliberation to committed harmful generation. Across four models (R1-8B, OpenThinker-7B, QwQ-32B, R1-32B) spanning two architectures (Llama, Qwen) and two scales (7–8B, 32B), the paper compares HS probes against text-based probes (Sentence-BERT), GRU sequence models, BOCPD, CUSUM, Mahalanobis distance, cross-model transfer, and 16-label fine-grained supervision. Three contributions are claimed: (C1) the composite metric `bal_acc × crossing_rate` systematically biases layer selection toward shallow layers due to noise-driven threshold crossings, specific to temporal monitoring pipelines; (C2) HS probes outperform text probes by +15.4 to +23.6 pp precision at correctly selected layers (12/12 Holm–Bonferroni tests pass); (C3) six alternative methods fail comprehensively. An AdvBench boundary-condition analysis (§5.3) confirms C1 does not generalize to binary classification settings.

---

## 2. Strengths (Consensus)

- **Exceptional self-critical honesty.** Both reviewers independently highlight this as the paper's defining quality. The evidence gradient (cross-validated / significant / exploratory), encoder-quality conditionality analysis, position mediation controls, AdvBench boundary-condition analysis, and explicit acknowledgment that no deployment-ready operating point exists reflect a level of scientific integrity rarely seen. The bug disclosure (Appendix M) further builds trust. *[R1, R2 unanimous]*

- **Rigorous statistical methodology at 7–8B scale.** BCa bootstrap with cluster resampling, Holm–Bonferroni step-down correction, nested 5-fold CV, split-half replication, multi-seed stability, random-label controls, CP perturbation analysis, and exact permutation tests for small-n 32B models. This is substantially above the typical EMNLP submission. *[R1, R2 unanimous]*

- **C1 is a real methodological finding.** The demonstration that crossing-rate composite metrics select shallow layers due to cosine compression is supported by random-label decomposition (separating geometric from label-dependent components), cross-architecture comparison, and mechanistic explanation. The cosine compression analysis provides a clear causal account. *[R1 strong, R2 accepts the finding but disputes its significance]*

- **Systematic negative results with interpretable failure modes.** The failure taxonomy (BOCPD: graduality mismatch; Mahalanobis: variance subspace blindness; cross-model transfer: model-specificity; GRU: overfitting on small n; fine-grained taxonomy: non-separable in HS space) is more informative than a simple negative-result table. *[R1, R2 agree]*

- **Encoder-quality gradient is an important honesty check.** MiniLM-384d (4/4 HB) → E5-Mistral (2/4) → BGE-1024d (1/4) prevents over-interpretation of the HS advantage. *[R1, R2 agree]*

- **Reproducibility infrastructure is strong.** Thorough hyperparameter reporting, promised code/data release, multi-seed analyses, exact configurations per model. *[R1, R2 agree]*

---

## 3. Weaknesses (Consensus and Divergences)

### 3.1 Both Reviewers Agree

**W1: 32B sample sizes are severely limiting (n = 19–20 test traces).** The MDE at 80% power is 8.6–9.5 pp, meaning R1-32B's residualized HS-text gap of +1.9 pp is indistinguishable from zero. Per-seed FPR standard deviation for R1-32B reaches 0.145, with one seed at FPR = 0.483. Including these fragile 32B tests in the "12/12 HB pass" headline is misleading. The claim should be reframed as "8/8 HB pass on adequately-powered models (7–8B)" with 32B results clearly marked as exploratory/underpowered.

**W2: Multiplicity in the 12/12 HB claim is underdisclosed.** The 12 final tests are conducted after per-model optimization of (layer, W) from a search space of ~2,240 configurations. The nested CV at 7–8B shows 13–25% shrinkage (OT-7B: +21.9 pp holdout → +16.4 pp nested CV, with different layer selection L21–27 vs. L16). The "12/12 HB pass" is an upper bound, not a conservative estimate.

**W3: Position mediation undermines C2 at 32B.** QwQ-32B's HS advantage is fully absorbed by quadratic position (gap goes from +7.4 pp to −1.0 pp). R1-32B's residualized gap is +1.9 pp (NS). For 2/4 models, the HS "advantage" may primarily reflect position encoding. The paper's framing ("partially correlated factors") underplays this for the 32B models where position appears to be the dominant factor.

**W4: Single-dataset dependency.** All CP-dependent results use one dataset (HarmThoughts). The AdvBench analysis shows the CP framework breaks down under adversarial prompts (CP = 0 in ~90% of jailbroken traces). There is no cross-dataset replication of the HS advantage itself. The AdvBench IAA proxy shows only moderate agreement (κ = 0.606) and poor CP position agreement (37% exact match). The primary dataset lacks formal human IAA reporting.

**W5: Architecture narrowness (3/4 Qwen).** Only R1-8B provides Llama-family evidence. The random-label control reveals the geometric component of crossing-rate bias is Qwen-specific. Generalization to other architectures (Llama-3, Mistral, Gemma) is untested.

**W6: Practical significance is essentially null.** No operating point achieves >70% precision with >60% coverage simultaneously. Safe-trace FPR median ~39%. Cross-model transfer fails completely. Oracle decomposition reveals hidden states are reactive, not predictive (15–28 step gap). The paper arrives at the conclusion that nothing works well enough for deployment.

**W7: Missing stronger text baselines.** MiniLM-384d is a weak baseline by 2025–2026 standards. The encoder-quality gradient suggests the HS advantage would vanish with sufficiently strong text encoders (instruction-tuned embedders at native dimensionality, LLM-based classifiers). The E5-Mistral experiment PCA-reduces to 384d for "capacity matching," which is a control, not a test of the strongest available encoder.

### 3.2 Divergence: Is C1 a Contribution or a Methods Note?

**R2 argues (harsher):** C1 warns against a metric (`bal_acc × crossing_rate`) that no published study has used as a primary layer selection criterion. The finding prevents a hypothetical error, not an existing one. The reversal is predictable once one examines inter-layer cosine distances. The three-level mitigation protocol amounts to "use multiple metrics and check for consistency," which is standard careful practice. C1 is a methods note, not a standalone contribution for a top venue.

**R1 argues (more generous):** The random-label decomposition cleanly separates geometric artifacts from label-dependent signal. The cross-architecture comparison showing the bias is Qwen-specific adds mechanistic depth. Even if no prior study used this exact metric, the paper demonstrates a concrete way that composite metrics can introduce qualitative bias in probing studies more broadly. The cosine compression mechanism generalizes to any metric incorporating threshold-crossing statistics.

**Resolution:** Both reviewers agree C1 is a **real finding** with a **clear mechanism**, but disagree on whether its scope (specific to temporal monitoring pipelines using crossing-rate statistics, confirmed not to generalize to binary classification by the paper's own AdvBench analysis) meets the contribution threshold for EMNLP. The narrowing from "general model property" to "temporal-monitoring-specific pitfall" is honest but reduces impact.

---

## 4. Questions for Authors

1. **On the 12/12 HB claim**: If you restrict to adequately-powered models (7–8B, n ≥ 43) and report nested CV estimates instead of holdout estimates, how many HB tests still pass? The 25% shrinkage for OT-7B suggests the headline number is optimistic.

2. **On C1's real-world impact**: Has any published study used `bal_acc × crossing_rate` as a layer selection metric? If not, C1 prevents a hypothetical error. Could you cite concrete instances where researchers might encounter this bias?

3. **On position mediation at 32B**: Given QwQ-32B's HS advantage is fully absorbed by quadratic position and R1-32B's is NS after residualization, should C2 be explicitly restricted to 7–8B models?

4. **On text baselines**: What happens with E5-Mistral at native 4096d without PCA reduction? The monotonic encoder-quality gradient (4/4 → 2/4 → 1/4 HB) suggests the HS advantage would vanish with a strong enough encoder.

5. **On AdvBench scope**: The CP = 0 finding for ~90% of adversarial jailbreaks suggests the entire temporal framework is inapplicable to the most realistic threat model. Could you discuss applicability scope more prominently in the main text rather than only in §5.3?

6. **On dimensionality at 32B**: What is the effective rank of the learned weight vector for R1-32B at W = 1 (5120d features, n = 60 training)? Does L2 regularization adequately control overfitting, or are the 32B HS results partially a dimensionality artifact?

7. **On the ensemble**: The ensemble result (all 4 models significant at p < 0.002) uses the same split for layer selection and evaluation. What is the cross-validated estimate of ensemble performance?

---

## 5. Experiment Coverage Assessment

Comparing against the imagined experiment list:

| Experiment | Covered? | Notes |
|---|---|---|
| exp-001: Cross-arch layer sweep (32B) | ✅ | Tables 1, §4.3 |
| exp-002: Temporal window (32B) | ✅ | Table 2, §4.4 |
| exp-003: Cross-model transfer | ✅ | Table 8, §4.10 |
| exp-004: Lead time analysis | ✅ | Table 6, §4.8 |
| exp-005: Mahalanobis baseline | ✅ | Table 9, §4.11 |
| exp-006: Bootstrap CI + HB | ✅ | Table 4, §4.6 |
| exp-007: Window size ablation | ✅ | Table 3, §4.5 |
| exp-008: Layer selection ablation (5 metrics) | ✅ | Table 1, §4.2 |
| exp-009: 16-label taxonomy | ✅ | Table 12, §4.14 |
| exp-010: Oracle decomposition | ✅ | Table 7, §4.9 |
| exp-011: OT-7B full pipeline | ✅ | Table 5, §4.7 |
| exp-012: GRU/attention upper bound | ✅ | Table 11, §4.13 |
| exp-013: Text baseline | ✅ | §4.6 (HS vs Text) |
| exp-014: BOCPD/CUSUM | ✅ | Table 10, §4.12 |
| exp-015: False positive analysis | ✅ | Tables 13–14, §4.15 |
| AdvBench layer bias replication | ✅ | Tables 15–18, §5.3 |

**Coverage: 16/16 experiments present.** The paper reflects the full imagined experiment portfolio. All expected results are directionally consistent with the imagined outcomes.

---

## 6. Scores

### R1 Final Scores (Methods + Experiments)
| Dimension | Score |
|---|---|
| Soundness | 3.5 |
| Excitement | 3.0 |
| Reproducibility | 4.0 |
| Overall Assessment | 3.0 |
| Confidence | 4 |

### R2 Final Scores (Novelty + Related Work)
| Dimension | Score |
|---|---|
| Soundness | 3.5 |
| Excitement | 2.0 |
| Reproducibility | 4.0 |
| Overall Assessment | 2.5 |
| Confidence | 4 |

### Consolidated Scores (Chair Reconciliation)
| Dimension | Score | Rationale |
|---|---|---|
| **Soundness** | **3.5** | Unanimous. Statistical methodology is rigorous at 7–8B; 32B analyses are underpowered. Position confounding partially unresolved. Single dataset. |
| **Excitement** | **2.5** | Split R1=3.0, R2=2.0 → 2.5. C1 is real but narrow (temporal-monitoring-specific, metric nobody uses). C2 undermined by encoder-quality gradient and position confounding. Practical impact near-zero by authors' own admission. |
| **Reproducibility** | **4.0** | Unanimous. Excellent detail, code promised, bug disclosure exemplary. Minor deduction for lacking formal IAA on primary dataset. |
| **Overall Assessment** | **2.5** | Borderline Findings. The paper is methodologically exemplary in its rigor and honesty, but the contribution scope after the paper's own caveats is narrow: C1 warns against a specific metric in a specific pipeline setting; C2 is conditional on weak text baselines, 7–8B scale, and non-adversarial traces; C3 documents failures that are individually predictable. The paper arrives at the conclusion that current HS probing does not work for practical deployment, which is a useful negative finding but does not clear the novelty/significance bar for confident Findings acceptance. |
| **Confidence** | **4** | Both reviewers read thoroughly. Familiarity with probing methodology, bootstrap inference, and safety monitoring literature. |

---

## 7. Meta-Review Summary

This paper presents a methodologically careful investigation of hidden-state probing for safety commitment point detection in reasoning models. Its strongest asset is exceptional scientific honesty — the authors systematically surface evidence against their own claims (encoder-quality gradient, position mediation, AdvBench non-replication, deployment viability gap). The statistical methodology (nested CV, HB correction, permutation tests, random-label controls) is above the EMNLP baseline.

However, this honesty reveals that the contribution scope is narrow:
- **C1** (layer selection sensitivity) warns against a metric formulation nobody has published using, is specific to temporal monitoring pipelines, and does not generalize to binary classification (by the paper's own evidence).
- **C2** (HS advantage) collapses from 4/4 to 1/4 HB significance with a stronger text encoder, is position-confounded at 32B scale, and does not replicate on AdvBench.
- **C3** (negative results) documents individually predictable failures without a unifying theoretical account of why probing fails.

The paper's practical conclusion — that no probe achieves deployment-ready performance — is honest but leaves the reader without actionable positive findings. The 32B results (n = 19–20) are underpowered and should not be counted equally with 7–8B results in headline claims. Architecture coverage is narrow (3/4 Qwen).

**Recommendation**: 2.5 — Borderline Findings. The paper needs (1) replication on a second CP-annotated dataset, (2) stronger text baselines at native dimensionality, (3) broader architecture coverage beyond Qwen-family, and (4) recalibrated claims that restrict C2 to 7–8B scale with weak text encoders, to reach confident Findings acceptance.


---

## 引用验证结果

**统计**: 85 篇文献 / 121 处引用 / 在线验证 85/85 篇

### 问题 (23)

- ❌ `zou2023representation` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.23 below threshold 0.82
- ⚠️ `adams2007bayesian` — 元数据不匹配: year: bib=2007 vs api=2018, first_author: bib=adams vs api=
- ❌ `qwq` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.27 below threshold 0.82
- ❌ `hcot2025` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.75 below threshold 0.82
- ❌ `chen2025unfaithful` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.39 below threshold 0.82
- ⚠️ `wollschlager2025geometry` — 元数据不匹配: first_author: bib=wollschl\"ager vs api=wollschläger
- ⚠️ `qi2025shallow_alignment` — 元数据不匹配: first_author: bib=qi vs api=huang
- ❌ `mao2025selfjailbreak_reasoning` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.38 below threshold 0.82
- ❌ `baker2025monitoring` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.46 below threshold 0.82
- ❌ `boxo2025linear_probes` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.42 below threshold 0.82
- ❌ `gelman2013garden` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.23 below threshold 0.82
- ⚠️ `turpin2023language` — 元数据不匹配: first_author: bib=turpin vs api=bowman
- ⚠️ `rcs2026` — 元数据不匹配: first_author: bib=hua vs api=peichun
- ⚠️ `chan2025probing` — 元数据不匹配: first_author: bib=chan vs api=siu
- ⚠️ `chrabaszcz2026monitoring` — 元数据不匹配: first_author: bib=chrab\kaszcz vs api=chrabąszcz
- ❌ `zhang2025reasoning_right` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.37 below threshold 0.82
- ⚠️ `cohen1988statistical` — 元数据不匹配: year: bib=1988 vs api=2013
- ❌ `templeton2024scaling` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.26 below threshold 0.82
- ❌ `turner2023activation` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.20 below threshold 0.82
- ❌ `levinstein2024liedetector` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.65 below threshold 0.82
- ❌ `advbench` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.30 below threshold 0.82
- ⚠️ `vitel2025layer` — 元数据不匹配: first_author: bib=vitel vs api=dmytro
- ⚠️ `zhang2025reasoning_right` — 在 .bib 中但正文未引用

### ✅ 通过 (63)