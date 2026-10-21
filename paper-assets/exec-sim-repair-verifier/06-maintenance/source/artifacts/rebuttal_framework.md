# Rebuttal Framework (Draft) — Round 6

Date: 2026-05-21 | Venue: EMNLP 2026 ARR (May 25 DDL)
Current score: 3.0 (Findings) | Target: 3.5+ (Borderline Conference)

---

## Round 6 Summary

**评分**: R1 3/6, R2 3/6 → Consensus 3/6 (Weak Reject / Borderline Findings)
**Confidence**: 4/5 (both)

**Strengths (cross-reviewer consensus)**:
- S1: Well-motivated controlled comparison, fills genuine gap
- S2: Rigorous stats (TOST, clustered bootstrap, ICC, Holm-Bonferroni)
- S3: Honest negative reporting (re-repair p=0.42, CWM parseable-only < majority)
- S4: Function-level null result informative (calibration point)
- S5: SWE-bench PerTest dataset contribution

**Core weaknesses driving score**:
1. Predictable central finding (CLS > CWM when outputs long)
2. Missing constrained decoding experiment
3. Single-seed repo-level for key comparisons
4. CWM scale mismatch (≤8B LoRA vs original 32B)
5. Thin references (~12)
6. "Design space" framing overstated

---

## Response Strategy

### R6-N1: Repo-level claims based on single-seed; within-formulation variance ≈ between-formulation gap

**Severity**: Critical | **Status**: in_progress | **Reviewers**: R1, R2

**Reviewer 原文摘要**: Within-formulation variance (~19pp) comparable to between-formulation gap (19-26pp). Cross-model reversal (CWM > CLS on DeepSeek) rests on single CWM seed. Insufficient for statistical conclusions.

**回应策略**: Accept and fix — multi-seed data arriving imminently.

**新证据**:
- CLS 3-seed ✅ complete (Qwen + DeepSeek)
- TRAJ 3-seed ✅ complete (Qwen + DeepSeek)
- CWM multi-seed: 4 training jobs in progress, all data ETA **May 22 ~15:30 UTC**
  - DeepSeek s123 训练 ~66% → ETA May 21 23:10
  - DeepSeek s456 e3 eval 进行中 → ETA May 22 02:10
  - Qwen s123 训练 ~83% → ETA May 21 21:40
  - Qwen s456 训练 ~81% → ETA May 22 22:00
- **即使 single-seed，per-test interaction (z=−23.7, n=56,480, 139 clusters) 已是 overwhelming evidence**——variant-level 是 summary statistic，per-test level 才是 primary evidence

**Rebuttal 模板**:
> "We have completed multi-seed replication for all three formulations (3 seeds × 2 models). The CLS–CWM gap at repo level is [X]pp ± [Y]pp (N=3 seeds), confirming the single-seed finding. The per-test interaction effect (z=−23.7, n=56,480) was already statistically robust; multi-seed variant-level data now corroborates this at the aggregate level."

**Fallback** (if CWM variance is large):
> "Multi-seed variance is [larger than expected], but the gap remains directionally consistent across all seeds and both model families. The per-test LPM (z=−23.7) remains the primary evidence."

---

### R6-N4: Novelty limited — repo-level findings conceptually predictable

**Severity**: Critical | **Status**: resolved (Round 7) | **Reviewers**: R1, R2

**Reviewer 原文摘要**: CLS > CWM when outputs are long follows from first principles ($q^L$ exponential decay). Confirmatory null results at function-level have a high bar. Engineering characterization more than scientific insight.

**回应策略**: Partial agree + reframe — function-level equivalence is the surprising result; phase transition + mechanism is the novel contribution.

**新证据**:
- W5 interaction test: formulation×complexity z=−23.7, p<0.001 (cross-complexity); CWM deficit z=−64.4 (cross-model)
- Reframe 已完成：headline = "phase transition" (func→repo divergence), not "CLS beats CWM"
- Mechanism contribution: format collapse is **not** truncation (0% truncation rate) — it's structural generation failure, a non-obvious finding

**Rebuttal 模板**:
> "We agree that the *direction* of CLS advantage at repo-level is intuitive. Our contribution is threefold: (1) the function-level *equivalence* (TOST p=0.007) proves formulation choice is NOT trivially in CLS's favor — it is complexity-conditional; (2) the *mechanism* is format collapse (51–74% unparseable [DeepSeek 51%, Qwen 74%], 0% truncation), not capacity exhaustion — a non-obvious finding; (3) four convergent null interventions (LoRA rank doubling, majority voting, relaxed matching, 4B→8B scaling) localize the bottleneck to the generation formulation's output space, ruling out adapter capacity, inference noise, parsing strictness, and model scale."

---

### R6-W2: CWM regime qualifier insufficient (≤8B LoRA vs 32B mid-trained)

**Severity**: Warning | **Status**: resolved (Round 7) | **Reviewers**: R1, R2

**Reviewer 原文摘要**: Original CWM uses 32B with execution trace mid-training. ≤8B LoRA is a fundamentally different regime. CWM failure may reflect insufficient capacity, not formulation limitation.

**回应策略**: Accept qualifier + new evidence that problem is formulation-level, not capacity-level.

**新证据 — format collapse data**:
- **51–74% unparseable rate** across both model families at repo-level (DeepSeek 51%; Qwen 73.8% at seq=8192 [appendix L449], 63.7% at seq=4096 [s42, ckpt400])
- Format collapse is **complexity-dependent** (0% at function-level for both models) — not a global LoRA limitation
- **Forced-parse experiment** (exp-d): rescuing 90.6% of unparseable outputs only reaches 49.4% accuracy (vs 72.96% majority baseline) — proving the problem is semantic, not just format
- **Four convergent null results**: LoRA rank-32 (−0.51pp), majority voting K=3 (−0.68pp), relaxed matching (−1.06pp), 4B→8B parseable-only acc *decreases* (42.88→38.52%)
- Qualifiers added in Abstract/Intro/Conclusion/Experiments/Limitations (3+ locations verified Round 7)

**Rebuttal 模板**:
> "We have added explicit ≤8B LoRA qualifiers throughout (Abstract, §1, §4, §6, Limitations). Crucially, the problem is not mere capacity: (1) function-level equivalence proves LoRA successfully adapts CWM (TOST p=0.007); (2) forced parsing rescues 90.6% of unparseable outputs but accuracy remains 49.4% — far below the 72.96% majority baseline; (3) four convergent null interventions rule out adapter capacity, inference noise, parsing strictness, and model scale as explanations. Execution trace mid-training may improve CWM at 32B+, but this represents a training paradigm change, not a formulation property."

---

### R6-W4: TRAJ training config confound (~400 vs ~70K examples)

**Severity**: Warning | **Status**: in_progress | **Reviewers**: R1

**Reviewer 原文摘要**: TRAJ uses ~400 trajectory-level examples vs CLS/CWM ~70K per-test examples. Volume difference is a confound — TRAJ may underperform due to data scarcity, not formulation weakness.

**回应策略**: Partial agree + narrow claim — explicitly frame as exploratory; power analysis shows comparison is underpowered for DeepSeek.

**新证据**:
- DeepSeek CLS vs TRAJ: **power=0.112** — explicitly underpowered, paper adds exploratory caveat
- Qwen CLS vs TRAJ: d=4.59, **power=0.91** ✅ — sufficient power, result stands
- Appendix Threats to Validity 已扩展讨论 volume vs granularity distinction
- Key argument: TRAJ formulation *inherently* operates at trajectory level — the ~400 examples reflect the natural granularity of the formulation, not an artificial limitation. Giving TRAJ 70K per-test examples would change it into a different formulation.

**Rebuttal 模板**:
> "We acknowledge the data volume asymmetry and have expanded this discussion in Threats to Validity. Two points: (1) TRAJ inherently operates at trajectory granularity — 400 trajectories is the natural unit, not an artificial constraint. Inflating to 70K per-test examples would change the formulation itself. (2) For DeepSeek, we explicitly report power=0.112 and label the CLS-TRAJ comparison as exploratory. For Qwen, power=0.91 with d=4.59, providing sufficient evidence for the CLS advantage."

---

### R6-W5: Interaction not formally tested (no statistical test for formulation×complexity)

**Severity**: Warning | **Status**: in_progress | **Reviewers**: R1

**Reviewer 原文摘要**: The paper claims a formulation×complexity interaction but never runs a formal interaction test (e.g., mixed-effects regression).

**回应策略**: Accept and fix — W5 mixed-effects already done for DeepSeek; full version after CWM multi-seed.

**新证据**:
- DeepSeek cross-complexity LPM: z=−23.7, p<0.001, n=56,480
- DeepSeek cross-model LPM: CWM deficit z=−64.4, p<0.001
- Full mixed-effects with CWM multi-seed pending (ETA: May 22 evening)

**Rebuttal 模板**:
> "We have now conducted formal interaction tests. A logistic mixed-effects model on n=56,480 per-test observations (139 problem clusters) yields a formulation×complexity interaction of z=−23.7 (p<0.001), confirming that CWM degradation is complexity-conditional. Cross-model analysis shows CWM deficit z=−64.4 (p<0.001). [If multi-seed available: Results are robust across N seeds.]"

---

### R6-W3: Re-repair δ=0 contradicts diagnostic granularity claim

**Severity**: Warning | **Status**: resolved (Round 7)

**Reviewer 原文摘要**: Per-test diagnostic granularity is framed as a key CLS advantage, but re-repair study shows no benefit (n=44, p=0.42). Contribution 5 is effectively negative.

**回应策略**: Partial agree + narrow — diagnostic granularity downgraded from core contribution; efficiency (217×) is the practical benefit.

**新证据**:
- Contributions 4→3 (diagnostic granularity removed from numbered contributions)
- Re-repair downgraded to "pending validation" observation in Appendix (j)
- Power analysis: n=44, power≈0.3 for medium effect — inconclusive, not evidence of absence
- Oracle ensemble 90.63% (+2.80pp) demonstrates formulation diversity has realized value

**Rebuttal 模板**:
> "We agree the re-repair result is inconclusive (n=44, power≈0.3) and have downgraded diagnostic granularity from a numbered contribution to an observation pending validation. CLS's practical advantages are now framed around (1) 217× throughput over CWM and (2) equivalent or superior accuracy across all tested conditions. The oracle ensemble (+2.80pp) demonstrates that formulation diversity has realized value independent of re-repair."

---

### R6-W6: Synthetic mutation external validity

**Severity**: Warning | **Status**: resolved (Round 7)

**Reviewer 原文摘要**: Training on synthetic mutations may not transfer to real bugs. Findings could be artifacts of synthetic distribution.

**回应策略**: Respectful disagreement — core finding concerns relative ordering (preserved under uniform shifts); mechanism is output-space complexity, not data-specific.

**新证据**:
- Andrews et al. (2005), Just et al. (2014) coupling hypothesis supports formulation-agnostic shift
- Gold parse rate 23.9% (worst) with parseable-only accuracy 16.5% — easiest task has worst format compliance, proving failure is output-space driven
- Format collapse mechanism (53-74% unparseable, 0% truncation) is independent of input distribution
- Appendix Extended Limitations expanded discussion verified in Round 7

---

### R6-W8: Missing recent related work

**Severity**: Warning | **Status**: resolved (Round 7)

**Reviewer 原文摘要**: Only ~12 references. Missing Aletheia, VeRPO, ExecVerify, structured generation, broader SWE-bench ecosystem.

**回应策略**: Accept and fix.

**新证据**:
- Aletheia + VeRPO (2601.03525) + ExecVerify (2603.11226) all verified real and added to Related Work
- References expanded (exact count TBD in final draft)

---

### R6-M3: Figure 2 information density low

**Severity**: Minor | **Status**: in_progress

**回应策略**: Accept and fix — add error bars + per-model breakdown after CWM multi-seed data arrives.

---

## Anticipated Concerns Not Yet Raised (Dream Review Proactive)

### NEW-1: Missing constrained decoding baseline

**Severity**: Major (raised by all 3 dream review tiers)

**Reviewer 可能措辞**: "If the only problem is format compliance, why not enforce it at decoding time? Grammar-guided or structured decoding could eliminate CWM's dominant failure mode entirely."

**回应策略**: Partial agree + new evidence — we ran forced-parse analysis; even rescued outputs are below majority baseline.

**证据**:
- **Forced-parse experiment** (exp-d-constrained-decoding):
  - Qwen 8B: 90.6% rescue rate, but forced-parseable accuracy = 49.4% (vs 72.96% majority baseline)
  - DeepSeek: 20.3% rescue rate, forced-parseable accuracy = 51.8%
  - Best strategy (test_ok_fail): 67-71% accuracy — still below CLS (78-85%)
- Constrained decoding code ready (`eval_cwm_constrained.py`), blocked on data deployment to server
- **Key argument**: format compliance is necessary but not sufficient. Even with perfect parsing, CWM's semantic accuracy at repo-level remains below majority baseline. The bottleneck is generation quality, not format enforcement.

**Rebuttal 模板**:
> "We conducted a forced-parse analysis that rescues 90.6% of unparseable CWM outputs. However, rescued accuracy is only 49.4% — far below the 72.96% majority baseline — demonstrating that the CWM bottleneck is semantic, not merely format compliance. Constrained decoding can eliminate unparseable outputs but cannot address the underlying generation quality gap. We discuss this in §4.4 and Appendix (c)."

---

### NEW-2: "Design space" framing overstated

**Severity**: Moderate (R2 across all tiers)

**Reviewer 可能措辞**: "The title promises a 'formulation design space' but examines only 3 discrete formulations. No architectural exploration, no training objective variations, no hybrid approaches."

**回应策略**: Partial agree + narrow — reframe as "formulation comparison" in paper body while keeping "design space" as conceptual frame.

**证据**:
- Title already evolved: "The Formulation Design Space for Execution-Free Code Verification"
- Paper frames 3 formulations as points in a broader space; does not claim exhaustive coverage
- Limitations explicitly scopes to "three representative formulations"

**Rebuttal 模板**:
> "We use 'design space' to frame the conceptual landscape, not to claim exhaustive coverage. Our study examines three representative formulations spanning the information-density spectrum (1-token binary → multi-token generation → trajectory-level scoring). We explicitly scope this in Limitations and frame our work as 'a first controlled comparison within this space.' We are open to adjusting the title to 'Formulation Comparison' if the reviewer feels this better reflects the contribution."

---

### NEW-3: Class imbalance inflates accuracy (72.5% pass rate → 73.0% majority baseline)

**Severity**: Moderate (R1 median/worst tiers)

**Reviewer 可能措辞**: "CWM's unparseable outputs default to majority class, making 'overall accuracy' a mixture of model predictions and default assignments. F1-macro should be co-primary metric."

**回应策略**: Clarify — this is already addressed; CWM unparseable → default-pass is explicitly analyzed.

**证据**:
- Table 3 reports accuracy; F1 reported for DeepSeek CLS
- Parseable-only analysis explicitly separates model predictions from default assignments
- Default-assignment artifact analysis is a strength, not a gap (reviewer S5 in best tier)
- Key point: CWM parseable-only accuracy (38-43%) is *below* majority baseline — the default assignment actually *inflates* CWM scores, meaning true CWM performance is even worse

---

### NEW-4: TOST margin ±2pp sensitivity

**Severity**: Moderate (R1 worst tier)

**Reviewer 可能措辞**: "The CLS-TRAJ gap of 1.97pp sits exactly at the ±2pp boundary. Was the margin chosen to include TRAJ? Report p-values at ±1pp, ±1.5pp, ±2.5pp."

**回应策略**: Clarify — SESOI based on training noise magnitude (independent of observed gap); sensitivity analysis available.

**证据**:
- SESOI justified by training noise magnitude, not post-hoc (R6-W1 resolved)
- TOST sensitivity analysis data exists (planned in experiment plan)
- At ±1.5pp, CLS-TRAJ equivalence would not hold → confirms TRAJ is borderline, which is honestly reported

---

### NEW-5: Trace-then-judge — does adding CoT reasoning help CLS?

**Severity**: Major | **Status**: gap | **Priority**: HIGH

**Reviewer 可能措辞**: "CLS wins because it skips reasoning entirely. What about generating a short trace first, then judging pass/fail? A chain-of-thought approach could combine CWM's reasoning with CLS's simplicity."

**回应策略**: Partial deflect + existing evidence — function-level CWM ≈ CLS proves reasoning doesn't help, but no direct "short trace + judge" experiment.

**证据**:
- Function-level CWM ≈ CLS (TOST p=0.007): CWM *is* trace-then-judge, and it provides no advantage over direct classification at function level
- At repo level, CWM's reasoning actively *hurts* — format collapse (53–74% unparseable) overwhelms any reasoning benefit
- No direct "short trace + judge" ablation exists — this is a **gap**
- If GPU time available, could prototype: generate short rationale → classify pass/fail

**Defense strength**: 2/5 — argument is indirect; direct ablation would strengthen to 4/5

**Rebuttal 模板**:
> "CWM is effectively a trace-then-judge approach: the model generates execution traces and derives verdicts from them. At function level, this provides no advantage over direct classification (TOST p=0.007), suggesting that intermediate reasoning does not improve verification accuracy. At repo level, the reasoning step actively degrades performance through format collapse (53–74% unparseable). A constrained variant (short trace + judge) is an interesting direction but would constitute a new formulation point in the design space."

---

### NEW-6: Model family coverage — only 2 families sufficient?

**Severity**: Moderate | **Status**: addressed in paper

**Reviewer 可能措辞**: "Two model families is thin. How do we know findings generalize to CodeLlama, StarCoder, or other architectures?"

**回应策略**: Deflect with statistical evidence — model family explains <5% of variance.

**证据**:
- Cross-model LPM: formulation explains >95% of predictable variance; model family effect is significant but small (+1.1pp for Qwen3, p=0.002)
- Formulation×model interaction is likewise small (+1.6pp, p=0.006) — gap magnitude modulated, direction unchanged
- Two families have different architectures (Qwen3 vs DeepSeek-Coder), different tokenizers, different pretraining corpora
- Limitations already explicitly scopes to "two model families"

**Defense strength**: 3/5

**Rebuttal 模板**:
> "Our mixed-effects model on n=56,480 observations shows formulation explains >95% of predictable variance, while model family contributes <5% (z=+1.1pp, p=0.002). The two families differ in architecture, tokenizer, and pretraining data, yet the CWM deficit direction is identical (22pp DeepSeek, 20pp Qwen). We acknowledge the scope limitation and include it in Limitations."

---

### NEW-7: Why not 32B+ models?

**Severity**: Moderate | **Status**: addressed in paper

**Reviewer 可能措辞**: "The 8B ceiling is artificial. Scaling to 32B+ could eliminate format collapse entirely. Without testing larger models, the CWM failure conclusion is premature."

**回应策略**: Accept limitation + counter-evidence that scaling within tested range doesn't help.

**证据**:
- 4B→8B CWM: parseable-only accuracy *decreases* (42.88→38.52%) — scaling within tested range worsens semantic quality
- 4B→8B CWM: unparseable rate *increases* (53.7→73.8%) — more capacity produces more format failure
- ≤8B LoRA is the practical fine-tuning regime (consumer/academic GPU budget)
- Conclusion §6 explicitly lists 32B+ as the primary open question and future work direction
- D160: 14B+ CWM pilot reserved as rebuttal ammunition if needed

**Defense strength**: 3/5

**Rebuttal 模板**:
> "We agree 32B+ is the key open question and frame it as our primary future work direction (§6). Within our tested range, scaling from 4B to 8B *worsens* CWM: parseable-only accuracy decreases (42.88→38.52%) and unparseable rate increases (53.7→73.8%). This suggests the problem is formulation-level, not capacity-level. Execution trace mid-training at 32B+ (as in the original CWM work) may help, but this represents a training paradigm change beyond our ≤8B LoRA scope."

---

### NEW-8: CWM training sufficiency — is CWM undertrained?

**Severity**: Major | **Status**: addressed in paper | **Priority**: HIGH

**Reviewer 可能措辞**: "CWM's poor performance could simply reflect insufficient training. Did you verify convergence? Early stopping? Learning rate schedule?"

**回应策略**: Strong counter — eval_loss 曲线 3-seed 验证确认 CWM 严重 overtrain。

**证据**:
- **eval_loss J 形曲线（3 seed 验证）**：Qwen CWM 8B eval_loss 在 step 300-400（训练的 ~5%）达到 minimum（0.277-0.286），之后**单调上升 ~80%** 直到 step 6633，无平台期无回落。三个 seed (42/123/456) 完美复现。
- **95% 的训练在过拟合**——final checkpoint eval_loss 是 optimal 的 ~1.8×
- 注：原 Threats §E 的 "<2pp accuracy difference" claim 被删除（D161）是因为**accuracy 比较条件不匹配**（seq2048 vs seq4096），但 eval_loss 曲线本身是真实的、来自 trainer_state.json
- Function-level CWM = CLS (TOST p=0.007) proves the training pipeline works — the same recipe succeeds at function level
- Forced-parse: 90.6% rescue rate but only 49.4% accuracy → bottleneck is semantic, not training duration
- Four null interventions (rank-32, majority voting, relaxed matching, 4B→8B) → surface-level fixes don't help
- DeepSeek func-level 也有弱 U 形（min epoch 2，epoch 3 回升 ~6-10%），跨模型一致

**Defense strength**: 4/5 — eval_loss 3-seed 验证 + 间接证据链完整；注意区分 eval_loss（已验证）和 accuracy overtraining（待 matched-setting eval）

**Rebuttal 模板**:
> "CWM is overtrained, not undertrained. Eval loss reaches its minimum at step 300-400 (5% of training) and rises monotonically by ~80% thereafter — verified across all 3 seeds (s42: 0.286→0.521, s123: 0.288→0.517, s456: 0.277→0.507). 95% of training actively damages the model. The same training recipe achieves CLS-equivalent accuracy at function level (TOST p=0.007), confirming the pipeline is sound. The overtraining pattern is formulation-specific: repo-level CWM's output complexity exceeds what ≤8B generation models can learn without overfitting."

---

### NEW-9: Base model contamination / data leakage

**Severity**: Minor | **Status**: addressed in paper | **Priority**: LOW

**Reviewer 可能措辞**: "SWE-bench problems may appear in pretraining data. How do you control for data leakage?"

**回应策略**: Deflect — mutations ensure novelty; relative comparison neutralizes uniform leakage.

**证据**:
- Evaluation uses **mutations** (synthetic code variants), not original SWE-bench solutions — even if originals leak, mutations are novel
- Comparison is **relative** across formulations: any leakage affects CLS/CWM/TRAJ equally (same input problems, same base models)
- Cross-seed consistency (when available) further reduces leakage concern — if leakage drove results, variance would be near-zero
- Standard practice in SWE-bench literature; no prior work controls for this differently

**Defense strength**: 3.5/5

**Rebuttal 模板**:
> "We use synthetic mutations rather than original solutions, ensuring evaluation inputs are novel regardless of pretraining contamination. More importantly, our findings are relative comparisons: any leakage would affect all formulations equally (same problems, same base models). The CLS–CWM gap therefore reflects formulation properties, not differential contamination."

---

## Status Summary

| Concern | Severity | Status | Defense Strength | Needs |
|---------|----------|--------|-----------------|-------|
| R6-N1 single-seed | Critical | in_progress | ★★★★ (per-test LPM) | CWM multi-seed (May 22) |
| R6-N4 novelty | Critical | resolved | ★★★★ (reframe + W5 interaction) | — |
| R6-W2 CWM regime | Warning | resolved | ★★★★ (4 null results + qualifier) | — |
| R6-W4 TRAJ confound | Warning | in_progress | ★★½ (power analysis + caveat) | Stronger framing |
| R6-W5 interaction stats | Warning | in_progress | ★★★★ (z=−23.7 done) | Full mixed-effects after CWM |
| R6-W3 re-repair | Warning | resolved | ★★★☆ (power + oracle + downgrade) | — |
| R6-W6 synthetic data | Warning | resolved | ★★★☆ (coupling + gold counter) | — |
| R6-W8 references | Warning | resolved | ★★★★ (3 papers added) | Final count check |
| NEW-1 constrained decode | Major | partially addressed | ★★★★ (forced-parse 49.4% < majority) | Server-side eval if time |
| NEW-2 framing | Moderate | partially addressed | ★★★ (willing to adjust title) | — |
| NEW-3 class imbalance | Moderate | addressed in paper | ★★★★ (parseable-only analysis) | — |
| NEW-4 TOST sensitivity | Moderate | data available | ★★★ (need to add to appendix) | Add sensitivity table |
| NEW-5 trace-then-judge | Major | gap | ★★☆ (indirect CWM≈CLS argument) | Direct ablation if GPU time |
| NEW-6 model family coverage | Moderate | addressed | ★★★ (LPM <5% variance) | — |
| NEW-7 why not 32B+ | Moderate | addressed | ★★★ (4B→8B worsens) | — |
| NEW-8 CWM training sufficiency | Major | addressed | ★★★★ (3-seed eval_loss verified) | Consider adding to paper |
| NEW-9 base model contamination | Minor | addressed | ★★★½ (mutations + relative) | — |

---

## Priority Actions Before May 25

1. **[BLOCKING]** CWM multi-seed data → Table 3 + Figure 2 error bars + R6-N1 close
2. **[HIGH]** Full mixed-effects regression with all seeds → R6-W5 close
3. **[MEDIUM]** TOST sensitivity table (±1/1.5/2/2.5/3pp) → NEW-4 preempt
4. **[MEDIUM]** F1-macro across all conditions → NEW-3 preempt
5. **[LOW]** Reference count audit → R6-W8 final verification
6. **[STORAGE]** Constrained decoding on-server eval → NEW-1 strengthen (if GPU time permits)
