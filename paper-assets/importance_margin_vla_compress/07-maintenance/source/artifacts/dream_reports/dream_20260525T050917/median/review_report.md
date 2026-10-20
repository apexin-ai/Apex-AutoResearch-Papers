---
dream_id: dream_20260525T050917
tier: median
overall_score: borderline (5.5/10)
timestamp: 2026-05-25T06:17:01.057818+00:00
---

# Dream Review Report: "How Vision Connectors Shape Token Pruning Robustness in Vision-Language-Action Models"

**Venue**: CoRL 2026  
**Review Mode**: Full (2 Reviewers + Roundtable)  
**Date**: 2026-05-25

---

## Reviewer Assignments

- **R1** — Methods & Experiments  
- **R2** — Novelty & Related Work  

---

## Step 1: Independent Reviews

### Reviewer R1 (Methods & Experiments)

#### Summary
Systematic empirical study of how vision connector architecture determines VLA robustness to post-connector token pruning. Six VLA architectures (450M–7B) across three connector families are evaluated on four LIBERO task suites under L2-norm, random, and attention-based pruning. Key findings: token-independent connectors degrade gracefully while token-entangling connectors exhibit catastrophic collapse amplified by task complexity; CV of token L2-norms serves as a zero-cost diagnostic; VTR (~22M params) recovers SmolVLA from 0% to ~60% SR at 75% compression.

#### Strengths

- **S1: Breadth of experimental coverage.** 6 architectures, 3 connector families, 4 task suites, 3 pruning strategies, k=0.3–0.95. Genuinely the first cross-architecture, cross-task VLA token pruning study, filling an important gap.
- **S2: Double dissociation finding is compelling.** Attention-based scoring effective on X-VLA but harmful on π0.5, while L2-norm shows the converse. Well-supported by data from multiple suites and retention ratios. Immediate practical implications and hard to dismiss as noise.
- **S3: Thorough SmolVLA cliff characterization.** Multiple checkpoints (LoRA and official), multiple methods (L2, random, attention, ToMe), all 4 suites. Two independent baselines both show 0% under any pruning. Conclusively establishes the architectural cliff.
- **S4: VTR with proper controls.** Flat M-curve (M=16–128 within ±5pp), parameter-matched MLP adapter control (p=0.15), M=128 passthrough demonstrating re-encoding mechanism, 3-seed validation. Careful experimental design.
- **S5: Honest limitation acknowledgment.** Confounders, small CV sample, sim-only evaluation, lack of causal isolation all explicitly flagged. Unusual intellectual honesty for this space.
- **S6: Non-monotonic phenomena well-documented.** π0.5 random cliff at k=0.85–0.925, X-VLA k=0.85/k=0.80 inversion, all multi-seed confirmed. Hypergeometric cliff model provides mechanistic account.

#### Weaknesses

- **W1: CV diagnostic severely underpowered.** Only 4 closed-loop data points. With n=4, any monotonic ordering yields high Spearman ρ trivially. CV range confounds with connector type — cannot distinguish "CV predicts robustness" from "connector type predicts robustness." More models needed.
- **W2: 2-axis framework lacks testable boundaries.** Does not specify expected amplification factors or predict where thresholds occur. Post-hoc descriptive rather than predictive.
- **W3: OpenVLA coverage notably sparse.** Only Object suite in main results. Many Table cells marked "—". Cannot make strong claims about MLP connector × task complexity interaction without Goal/Long/Spatial data for OpenVLA.
- **W4: VTR universality falsified but underexplored.** 0% SR on OpenVLA mentioned in passing. No investigation of why (overfitting? training protocol? learning rate?). Missing training loss curves.
- **W5: Seed and statistical rigor concerns.** Most conditions single-seed. Some cross-model comparisons mix seeds (L2: seed42, Random: seed7). "Scaling law" table uses inconsistent statistical treatment across models.
- **W6: VTR baseline discrepancy.** VTR trained baseline = 44.8% vs official 59.2%. The "exceeds baseline" framing depends on which baseline. Should be framed as "recovery from 0% to functional performance."
- **W7: No real-robot evaluation.** For a CoRL submission, sim-only is a notable gap. LIBERO is respected but VLA pruning behavior could differ under real-world visual conditions.
- **W8: π0.5 attention extraction protocol questionable.** Attention scores in [2e-6, 3.6e-3] with position bias. No discussion of whether different extraction methods might produce different results.

#### Questions to Authors (R1)

1. Can you provide evidence that CV is predictive beyond what connector type already tells us? Within the MLP family (OpenVLA CV=0.215, OFT CV=0.219), is there measurable pruning robustness difference consistent with the 0.004 CV gap?
2. The π0.5 cliff at k=0.85–0.925 and X-VLA's non-monotonic recovery at k=0.85/0.80 both involve similar k values but different connectors. How do you reconcile the mechanistic explanations?
3. For VTR failure on OpenVLA, did you attempt different learning rates, fewer training steps, or freezing strategies? Training loss curves?
4. Why is OpenVLA evaluated on only Object in main results? If cross-suite data exists, omitting it weakens the cross-task claims.
5. The Spearman ρ=0.82 (p=0.03) — how many data points? With only 3 models in the scaling law table, any monotonic ordering gives ρ=1.0.

#### R1 Scores

| Dimension | Score |
|-----------|-------|
| Soundness | 3/4 |
| Presentation | 3/4 |
| Contribution | 3/4 |
| Overall | 6/10 |
| Confidence | 4/5 |

---

### Reviewer R2 (Novelty & Related Work)

#### Summary
The paper systematically studies how vision connector architecture and task complexity jointly determine whether token pruning preserves or destroys VLA performance. The main novelty claims are a 2-axis framework (connector coupling × task complexity), CV as a zero-cost diagnostic, and VTR as a targeted recovery method for pixel-shuffle architectures. The paper is positioned as "primarily analysis with targeted method for worst-case architecture."

#### Strengths

- **S1: Timely and well-scoped question.** VLA efficiency literature has grown rapidly but each work validates on a single architecture. First paper to ask whether pruning transferability is architecture-dependent, with clear mechanistic explanations.
- **S2: Empirical breadth.** 5 models in closed-loop evaluation, 4 LIBERO suites, 3 pruning methods, 6+ retention ratios, multi-seed for key claims. Cross-model, cross-suite, cross-method factorial design considerably more thorough than typical VLA papers.
- **S3: Double dissociation is genuinely novel.** Goes beyond "different models behave differently" into identifying a structural interaction between scoring mechanism and connector architecture. The paper's strongest contribution.
- **S4: Pixel-shuffle cliff is a valuable negative result.** Practically important documentation. Mechanism clearly explained and architecturally motivated.
- **S5: Honest self-assessment.** Unusual candor about confounders, small N, sim-only evaluation.

#### Weaknesses

- **W1: 2-axis framework is descriptive, not predictive.** The "two axes" are really one axis (connector coupling) with a moderating variable. Framework does not predict where thresholds occur, only that entangling = bad for pruning — arguably expected once pixel-shuffle's non-overlapping receptive fields are understood.
- **W2: CV diagnostic underpowered and elementary.** Correlation on 3–4 points. CV = σ/μ of L2 norms is a trivial statistic. No comparison against alternative diagnostics (kurtosis, effective rank, pairwise cosine similarity). Cannot assess if CV is the best diagnostic or merely a diagnostic.
- **W3: VTR novelty is limited.** Structurally identical to Perceiver Resampler (Flamingo) and Q-Former (BLIP-2). The paper itself notes this. Novelty limited to applying known architecture in a new setting. Validated on only one model (SmolVLA); fails on OpenVLA.
- **W4: Missing important related work.**
  - Token Merging (ToMe) tested only on SmolVLA, not on token-independent architectures where it might succeed.
  - SparseVLM (Zhang et al., 2024, NeurIPS) not discussed — also analyzes visual token sparsity in VLMs.
  - "Don't Run with Scissors" dismissed in one sentence despite analyzing how architectural choices affect pruning robustness — a direct conceptual precursor.
  - VLA-IAP positioning thin: no discussion of whether VLA-IAP's specific scoring mechanism would succeed/fail on entangling connectors (would demonstrate framework's predictive utility).
- **W5: Simulation-only, no sim-to-real evidence.** LIBERO baselines vary widely across models (SmolVLA 44.8–59.2% vs X-VLA 99.2%), complicating cross-model comparisons. Models with higher baselines have more room for graceful degradation.
- **W6: Connector-type confounds only partially addressed.** No controlled comparison isolates connector while controlling backbone, encoder, and scale. Causal claim "connector is the primary determinant" should be softened.
- **W7: Data gaps in main results.** Multiple "—" entries in cross-suite tables. Undermines the "systematic" claim.

#### Questions to Authors (R2)

1. The hypergeometric cliff model fits C=106, T=7 to 3 data points with 2 free parameters — effectively interpolation. Can you validate on held-out retention ratios?
2. Why was attention-based scoring not evaluated on OpenVLA? Would complete the dissociation pattern.
3. X-VLA (CV=0.151, "entangling") has lower CV than OpenVLA (CV=0.215, "independent"). Entangling connectors should produce more heterogeneous tokens. How do you reconcile?
4. How stable is CV across different inputs? Is CV=0.055 for π0.5 consistent across tasks, images, timesteps?
5. Can you compare CV against alternative diagnostic metrics (kurtosis, effective rank, cosine similarity)?

#### R2 Scores

| Dimension | Score |
|-----------|-------|
| Soundness | 3/4 |
| Presentation | 3/4 |
| Contribution | 2/4 |
| Overall | 5/10 |
| Confidence | 4/5 |

---

## Step 2: Cross-Sharing Summary

Both reviewers independently identified the same strongest result (double dissociation / scoring crossover), same critical weaknesses (CV underpowered, OpenVLA incomplete, VTR limited novelty, sim-only), and same praise (empirical breadth, honest limitations).

Key divergence: R1 values the practical/actionable contribution more highly (Contribution 3/4), while R2 emphasizes that the conceptual novelty is limited — framework is descriptive, CV is elementary, VTR is derivative (Contribution 2/4).

## Step 3: Convergence

### Consensus Points

1. **Strongest contribution**: Cross-architecture empirical analysis breadth + double dissociation finding (attention vs L2-norm crossover across connector types). This is novel, well-evidenced, and practically valuable.

2. **Weakest claims**: CV as an independent diagnostic predictor. With n=3–4, the correlation is trivially achievable and confounded with connector type. The "scaling law" framing is inappropriate for 3 data points.

3. **Framework assessment**: The 2-axis framework organizes observations well but is descriptive, not predictive. It does not predict thresholds, cliff locations, or amplification magnitudes. "Connector coupling determines pruning robustness" is useful but arguably expected once the architecture differences are understood.

4. **VTR assessment**: Engineering contribution (applying cross-attention bottleneck to pixel-shuffle recovery), not methodological novelty. Validated on only 1 model, fails on OpenVLA. The failure investigation is insufficient — the paper cannot distinguish "VTR is fundamentally connector-specific" from "VTR training protocol was inappropriate for 7B models."

5. **Critical missing elements for CoRL**: (a) OpenVLA multi-suite data, (b) real-robot validation, (c) more models for CV correlation, (d) attention-based pruning on OpenVLA.

6. **Paper identity**: Clear and appropriately scoped as "primarily analysis with targeted method." The paper correctly downscales its method claims relative to its analysis claims.

### Post-Convergence Score Calibration

Both reviewers agree the paper falls in the borderline-to-weak-accept range. The empirical breadth and double dissociation finding argue for acceptance; the underpowered CV diagnostic, OpenVLA gaps, VTR limited novelty, and sim-only evaluation argue against.

---

## Step 4: Consolidated Assessment

### Overall Recommendation: **Borderline** (5.5/10)

### Consolidated Scores

| Dimension | R1 | R2 | Consolidated |
|-----------|----|----|-------------|
| Soundness | 3/4 | 3/4 | 3/4 |
| Presentation | 3/4 | 3/4 | 3/4 |
| Contribution | 3/4 | 2/4 | 2.5/4 |
| Overall | 6/10 | 5/10 | 5.5/10 |
| Confidence | 4/5 | 4/5 | 4/5 |

### What Would Move This Paper to Accept

1. **CV diagnostic**: Add 2–3 more VLA models (even offline CV measurements without closed-loop eval) to demonstrate CV predicts beyond connector type. Compare CV against alternative diagnostics (kurtosis, effective rank).
2. **OpenVLA multi-suite**: Complete the Object/Spatial/Goal/Long grid for OpenVLA. This is the only MLP-projector model with closed-loop eval — its data gaps are disproportionately damaging.
3. **VTR failure investigation**: Provide OpenVLA training loss curves, try different learning rates / training durations, discuss whether the failure is architectural or procedural.
4. **Real-robot validation**: Even a single model on 1–2 tasks would substantially strengthen the CoRL submission.
5. **Attention on OpenVLA**: Complete the double dissociation table with OpenVLA attention-based pruning.

### What Would Move This Paper to Reject

1. If the CV diagnostic cannot survive additional models (i.e., new models break the monotonic ordering).
2. If OpenVLA multi-suite data reveals the framework's predictions are wrong (e.g., MLP projectors also cliff on complex tasks).
3. If VTR failure on OpenVLA is shown to be a training protocol issue rather than architectural, undermining the "connector-dependent" narrative.

### Coverage vs. Experimental Design

The paper covers 10 of 12 imagined experiments from the design document. Two were dropped with acknowledgment:
- OpenVLA-OFT cross-suite pruning (blocked by GPU incompatibility) → properly acknowledged as limitation
- RoboFlamingo Perceiver Resampler (training killed) → acknowledged as future work

The remaining 10 are reflected in the paper with appropriate qualification of edge cases (π0.5 Axis-2 reversal, X-VLA non-monotonicity, k=0.3 CV reversal).

### Key Risks for This Paper at CoRL

1. **"Obvious once explained" criticism**: Reviewers may argue that pixel-shuffle destroying spatial information under deletion is architecturally obvious, reducing the 2-axis framework to a post-hoc rationalization.
2. **Statistical power**: The n=3 scaling law and n=4 CV spectrum are vulnerable to criticism. The Spearman ρ=0.82 at k=0.5 with potentially only 3 data points is a red flag.
3. **Sim-to-real gap**: CoRL increasingly expects real-robot results. A pure LIBERO study, even a thorough one, may be seen as belonging more at an NLP/ML venue.
4. **VTR circularity**: "VTR only works on pixel-shuffle, and pixel-shuffle is the architecture you're warning against" — the method contribution may be seen as circular.

### Final Summary

A thorough empirical study addressing an important and timely question — why does token pruning work on some VLAs but not others? The double dissociation finding (attention helps entangling connectors but hurts independent ones; L2-norm shows the reverse) is the strongest novel contribution and has immediate practical value. The pixel-shuffle cliff documentation is rigorous and practically important. However, the conceptual framework is descriptive rather than predictive, the CV diagnostic is statistically underpowered, VTR is architecturally derivative with limited scope, and the absence of real-robot evaluation weakens the CoRL fit. The paper is at the borderline — strong empirical work with useful practical implications, but the contributions are collectively incremental rather than individually compelling.


---

## 引用验证结果

**统计**: 62 篇文献 / 52 处引用 / 在线验证 62/62 篇

### 问题 (45)

- ⚠️ `black2025pi05` — 元数据不匹配: first_author: bib=black vs api=intelligence
- ⚠️ `ghosh2024octo` — 元数据不匹配: first_author: bib=team vs api=ghosh
- ⚠️ `liu2023libero` — 元数据不匹配: first_author: bib=liu vs api=feng
- ⚠️ `yang2025efficientvla` — 元数据不匹配: first_author: bib=yang vs api=yantai
- ⚠️ `liu2025vlapruner` — 元数据不匹配: first_author: bib=liu vs api=ziyan
- ⚠️ `liu2023llava` — 元数据不匹配: first_author: bib=liu vs api=lee
- ⚠️ `yang2024qwen2` — 元数据不匹配: first_author: bib=yang vs api=an
- ⚠️ `zhang2024fastervlm` — 元数据不匹配: title: similarity=0.48 (possible wrong arXiv ID)
- ⚠️ `zitkovich2023rt2` — 元数据不匹配: first_author: bib=zitkovich vs api=brohan
- ⚠️ `bouthillier2024negative` — 元数据不匹配: first_author: bib=bouthillier vs api=karl
- ⚠️ `wang2025specprunevla` — 在 .bib 中但正文未引用
- ⚠️ `feng2026seewhatmatters` — 在 .bib 中但正文未引用
- ⚠️ `zhang2025sparsevlm` — 在 .bib 中但正文未引用
- ⚠️ `khaki2025sparsevila` — 在 .bib 中但正文未引用
- ⚠️ `li2024roboflamingo` — 在 .bib 中但正文未引用
- ⚠️ `brohan2023rt2` — 在 .bib 中但正文未引用
- ⚠️ `ghosh2024octo` — 在 .bib 中但正文未引用
- ⚠️ `brohan2023rt1` — 在 .bib 中但正文未引用
- ⚠️ `alayrac2022flamingo` — 在 .bib 中但正文未引用
- ⚠️ `chen2024internvl` — 在 .bib 中但正文未引用
- ⚠️ `jaegle2021perceiver` — 在 .bib 中但正文未引用
- ⚠️ `oquab2023dinov2` — 在 .bib 中但正文未引用
- ⚠️ `zhai2023siglip` — 在 .bib 中但正文未引用
- ⚠️ `yang2024qwen2` — 在 .bib 中但正文未引用
- ⚠️ `lipman2023flow` — 在 .bib 中但正文未引用
- ⚠️ `li2024tokenpacker` — 在 .bib 中但正文未引用
- ⚠️ `wen2024tinyvla` — 在 .bib 中但正文未引用
- ⚠️ `ryoo2021tokenlearner` — 在 .bib 中但正文未引用
- ⚠️ `meng2022adavit` — 在 .bib 中但正文未引用
- ⚠️ `chen2023sparsevit` — 在 .bib 中但正文未引用
- ⚠️ `ye2025fitprune` — 在 .bib 中但正文未引用
- ⚠️ `shi2024crossget` — 在 .bib 中但正文未引用
- ⚠️ `zhang2024fastervlm` — 在 .bib 中但正文未引用
- ⚠️ `liu2024llava15` — 在 .bib 中但正文未引用
- ⚠️ `chen2024internvl25` — 在 .bib 中但正文未引用
- ⚠️ `gao2024miniinternvl` — 在 .bib 中但正文未引用
- ⚠️ `zitkovich2023rt2` — 在 .bib 中但正文未引用
- ⚠️ `openxembodiment2024` — 在 .bib 中但正文未引用
- ⚠️ `zhang2023h2o` — 在 .bib 中但正文未引用
- ⚠️ `xiao2024streamingllm` — 在 .bib 中但正文未引用
- ⚠️ `mees2022calvin` — 在 .bib 中但正文未引用
- ⚠️ `chi2023diffusionpolicy` — 在 .bib 中但正文未引用
- ⚠️ `zeng2023transformers_tsf` — 在 .bib 中但正文未引用
- ⚠️ `bouthillier2024negative` — 在 .bib 中但正文未引用
- ⚠️ `oquab2024dinov2` — 在 .bib 中但正文未引用

### ✅ 通过 (52)