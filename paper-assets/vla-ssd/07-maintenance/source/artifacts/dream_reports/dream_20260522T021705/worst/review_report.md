---
dream_id: dream_20260522T021705
tier: worst
overall_score: 4/10 — Reject
timestamp: 2026-05-22T03:33:18.636910+00:00
---

# Dream Review Report — Consolidated Roundtable Output

**Paper:** "A Systematic Diagnostic Framework for Analyzing Instruction Processing in Vision-Language-Action Models"
**Venue:** CoRL 2026
**Review mode:** Full (2 Reviewers, 4-step roundtable)
**Date:** 2026-05-22

---

## Venue Calibration

CoRL is a top robotics learning venue (acceptance rate ~25–30%) that evaluates submissions on significance and novelty of results (theoretical or empirical), their potential for scientific and technological impact, and their relevance to robot learning. Papers are expected to address a learning question for physical robots or test proposed solutions on physical robots/simulation with behavioral outcomes. Pure analysis papers without behavioral validation face a high bar. Scoring uses a 1–10 scale aligned with OpenReview conventions (1=trivial/wrong, 5=marginally below, 6=marginally above, 10=top 5%).

---

## Paper Summary

The paper presents a diagnostic framework for token-level analysis of VLA models, combining factorial experimental design (trained/untrained × instruction presence), six complementary probing methods (RSA, CKA, R² probes, counterfactual sensitivity, attention analysis, classification probes), and cross-architecture validation. Applied to three VLA families — OpenVLA (Llama-2-7B), TracVLA (Phi-3-mini), NORA (Qwen2.5-VL-3B) — across four LIBERO task suites (10/12 cells filled), the framework reveals two training-induced effects (R² exit collapse, counterfactual sensitivity), one base-model-dependent property (L1 attention heads previously misattributed to training), and metric dissociation between RSA and CKA. The framework itself is positioned as the primary contribution.

---

## Reviewer R1: Methods + Experiments

### Strengths

**S1. Sound factorial design.** The 2×2 (trained/untrained × instruction) design enables clean attribution of effects. The sanity check confirming frozen encoder weights (cosine similarity = 1.0) appropriately validates that observed changes originate in the LLM backbone.

**S2. Multi-method triangulation.** Using 6 complementary methods covering geometric (RSA), global (CKA), functional (R²), interventional (CF), attentional, and discriminative (classification) perspectives is methodologically rigorous. The RSA–CKA dissociation discovery directly demonstrates why this multi-method approach is necessary.

**S3. Cross-architecture scope.** Testing 3 architectures with different LLM backbones and vision encoders (10 evaluation cells) represents a meaningful attempt at generalization, significantly more thorough than typical single-architecture analysis papers.

**S4. Commendable scientific honesty.** The paper transparently acknowledges its limitations — removing L1 routing from the contribution list after discovering it is base-model-dependent (Table 9), flagging the missing NLP control, and explicitly listing 8 limitations. This is rare and admirable.

### Weaknesses

**W1. [Critical] Missing NLP fine-tuning control.** The paper's central empirical finding — R² exit collapse — cannot be established as VLA-specific without comparing to an LLM fine-tuned on standard NLP tasks. The Llama-2 base model already shows exit R² decline of Δ=0.090. If Llama-2 fine-tuned on any supervised task shows comparable exit collapse, the finding reduces to a generic supervised fine-tuning property of decoder-only models, not a VLA-specific routing phenomenon. The authors acknowledge this explicitly (Table 4, row "NLP fine-tuned: ? (missing)") but do not execute it. For a paper whose main empirical claim rests on this effect, this missing control is near-fatal.

**W2. [Critical] Highly inconsistent matrix results.** Of 10 filled cells, only 6 show clear collapse (Δ > 0.10). Four cells are weak or absent: OpenVLA Spatial (Δ=0.040), OpenVLA Long (Δ=0.004, effectively zero), TracVLA Goal (Δ=0.090, ratio 1.9×), and the overall magnitude range spans 172× (0.004 to 0.691). Critically, OpenVLA — the only community-released checkpoint — shows the weakest results across all three architectures (mean Δ=0.059). This raises the possibility that strong exit collapse correlates with self-trained checkpoints rather than being an intrinsic property of VLA training. The paper honestly characterizes this as "directionally consistent but magnitude-variable," but directional consistency alone (9/10 cells) is a weak finding — especially without a formal statistical test (e.g., sign test with effect size) demonstrating that this consistency exceeds chance.

**W3. [Major] Unfair counterfactual sensitivity baselines.** Untrained models are either randomly initialized (OpenVLA — no language capability at all) or base VLMs without action heads (TracVLA Phi-3-Vision, NORA Qwen2.5-VL — not functional action-producing models). Comparing CF sensitivity of a trained, functional model against a non-functional baseline is uninformative about VLA-specific routing — it merely confirms that trained models respond differently to inputs than random/base models. Additionally, NORA Goal yields a saturated cosine distance of 1.0, likely an architectural artifact rather than genuine routing evidence.

**W4. [Major] No behavioral validation.** The paper is entirely representational — no intervention experiments (early exit, attention masking, representation surgery) connecting observed patterns to task performance outcomes. For a robotics venue, the absence of any demonstration that representational findings matter for robot behavior is a significant limitation.

**W5. [Moderate] Three-tier gradient severely underpowered.** Tier-2 has N=1 (openvla-7b OXE-pretrained). A "gradient" with one intermediate data point is a step function, not a gradient. The paper appropriately hedges this as "preliminary observation" but it occupies a full subsection (§4.5) disproportionate to its evidential weight.

**W6. [Moderate] Incomplete cross-architecture data.** Per-layer RSA curves computed only for OpenVLA — so the inverted-U pattern cannot be generalized. NORA Object/Long missing (2/12 cells). Encoder comparison limited to OpenVLA's architecture. Many "cross-architecture" claims implicitly rest on single-architecture evidence.

**W7. [Minor] No formal statistical testing of directional consistency.** The claim "9/10 cells show trained > untrained delta" would benefit from a formal sign test or permutation test against the null hypothesis of random direction. Without this, the strength of directional consistency is unclear.

### R1 Score: 4/10 — Below acceptance threshold

---

## Reviewer R2: Novelty + Related Work

### Strengths

**S1. Addresses a genuine gap.** Prior VLA behavioral studies (Grant et al. 2026, Haon et al. 2025) operate at the input-output level. This paper fills an unoccupied niche by providing internal, layer-by-layer representational analysis of VLAs. The positioning relative to behavioral work is accurate.

**S2. Base-model attribution is a clean, novel finding.** The discovery that L1 instruction-dominant head counts are base-model-dependent rather than training-induced (Table 8) is the paper's most scientifically clean contribution. It corrects a misattribution that the community could have made and demonstrates the framework's unique analytical capability. The fact that the authors removed this from the contribution list (originally their most visually striking result) rather than misrepresenting it speaks to the paper's scientific integrity.

**S3. Metric dissociation is methodologically valuable.** The RSA-CKA ordering reversal (Table 11) is a useful cautionary finding for the emerging VLA analysis community. While not deep, it has practical implications for how future work should report representational similarity.

**S4. Framework design is sound.** The combination of factorial design, multi-method suite, and cross-architecture protocol is a well-conceived methodology. If released as a toolkit, it could benefit the growing VLA research community.

### Weaknesses

**W1. [Major] Thin novelty of individual methods.** RSA, CKA, R² probes, attention analysis, and classification probes are all well-established in the NLP/ML interpretability literature. The factorial experimental design is standard methodology. The novelty lies in combining and applying these to VLAs — which is valid as an empirical contribution, but only if the application yields strong findings. Given the inconclusive nature of the reported findings (exit collapse confounded, CF baselines unfair, L1 heads removed), the applied novelty is insufficient.

**W2. [Major] Findings do not substantially advance VLA understanding.** After the paper's own contribution audit (Table 9), the remaining training-induced effects are: (a) R² exit collapse — directionally consistent but magnitude-variable and potentially generic, and (b) CF sensitivity — with unfair baselines. The paper effectively self-demolishes its empirical contributions through honest analysis. What actionable insight does a VLA designer or roboticist take away? The paper does not answer "what should we build differently?" or "how should we debug VLA failures?"

**W3. [Major] Venue mismatch with CoRL.** CoRL evaluates papers on their relevance to robot learning and potential for impact on robotic systems. A pure analysis framework with (a) no behavioral validation, (b) no tested design implications, (c) no demonstrated utility for improving VLA performance, and (d) inconclusive findings is a poor fit. The paper reads as a workshop contribution (e.g., a NeurIPS workshop on foundation models for robotics or on interpretability) rather than a main-conference CoRL paper.

**W4. [Moderate] Thin related work.** The related work section is brief and narrowly scoped. Missing engagement with:
- Mechanistic interpretability literature (Elhage et al. on superposition, Conmy et al. on circuit discovery, Bills et al. on neuron interpretation) — directly relevant to understanding fine-tuning's effect on transformer internals.
- Representation collapse/compression literature in supervised fine-tuning — the R² exit collapse may be a known phenomenon under a different name.
- Probing methodology critiques (Hewitt & Liang 2019 on selectivity; Belinkov 2022 survey) — relevant for assessing what linear probes can and cannot tell us.

**W5. [Moderate] Unresolved metric authority crisis.** The paper discovers metric dissociation (RSA-CKA reversal) and correctly identifies this as motivating multi-metric frameworks. However, it simultaneously undermines the authority of its own quantitative findings. If changing the metric reverses the conclusion, how should the reader interpret the R² exit collapse? Is R² the "right" metric? The paper does not resolve this tension — it raises it and moves on, leaving every specific number in the paper under a cloud of metric dependence.

**W6. [Minor] Broken references.** Multiple citations appear as [? ?] and [? ] throughout the paper, indicating unresolved bibliography entries. This undermines the paper's presentation quality and makes it impossible to verify some related work claims.

**W7. [Minor] Redundant experimental space.** Three experiments (plan_006 instruction ablation, plan_007 2×2 matrix, plan_008 random instruction control) all verify instruction invariance of image-token RSA — a result that is structurally guaranteed by the causal mask. Spending ~1.5 pages verifying a structurally guaranteed null result is inefficient. The paper acknowledges this ("does not constitute a novel finding") but still allocates substantial space.

### R2 Score: 4/10 — Below acceptance threshold

---

## Roundtable Discussion

### Points of Agreement (R1 + R2)

1. **Missing NLP control is near-fatal.** Both reviewers identify this as the single most damaging gap. This one experiment — comparing R² exit curves of Llama-2 fine-tuned on an NLP task vs. VLA task — could have either (a) established VLA-specificity (if patterns differ) or (b) definitively shown the effect is generic (if patterns match). Its absence leaves the paper's central finding in an unresolvable limbo.

2. **No behavioral validation is critical for CoRL.** Pure representational analysis without any connection to robot task performance is a severe venue mismatch. Even a small-scale intervention (e.g., early-exit decoding showing that exit collapse predicts performance, or attention masking showing that identified routing patterns causally affect actions) would significantly strengthen the paper.

3. **OpenVLA weakness is concerning.** The community-released checkpoint showing the weakest exit collapse across all architectures raises the specter of training-procedure confounds. Self-trained checkpoints (TracVLA, NORA) show stronger effects, but the community cannot independently verify these results.

4. **Scientific honesty is commendable but insufficient.** Both reviewers appreciate the transparency. However, acknowledging a limitation does not eliminate its impact on the paper's contribution. The contribution audit (Table 9) is a remarkable piece of self-analysis that, ironically, makes the case for rejection more clearly than the reviewers could.

5. **Framework contribution is real but not enough alone for CoRL.** The diagnostic toolkit is well-designed and could benefit the community. However, at CoRL, a framework paper needs to demonstrate its value through strong findings that advance understanding of robot learning. The findings here are too inconclusive to serve this purpose.

### Points of Divergence

- R1 gives slightly more credit to the experimental scope; R2 emphasizes that scope without depth (missing controls, unfair baselines) is not sufficient.
- R2 is more concerned about venue fit; R1 focuses more on internal experimental validity.
- Both arrive at the same score (4/10), confirming convergence.

---

## Experiment Coverage Assessment

Comparing the paper against the full experiment design (review_context.yaml):

| Experiment | Status in Paper | Coverage |
|---|---|---|
| SigLIP+Projector RSA (plan_001) | §4.1, single-arch (OpenVLA only) | Partial |
| DINO baseline RSA (plan_002) | §4.1, §4.7 | Complete |
| Per-layer RSA curve (plan_003) | §4.1, OpenVLA only | Partial — no TracVLA/NORA |
| Output head analysis (plan_004) | §3.1 (brief mention) | Minimal |
| 6 probing methods (plan_005) | §4.1, Table 3 | Complete |
| Instruction ablation (plan_006) | §4.1, Table 1 | Complete |
| 2×2 matrix (plan_007) | §4.1, Table 1 | Complete |
| Random instruction control (plan_008) | §4.1, Table 2 | Complete |
| CKA verification (plan_009) | §4.6, Table 11 | Complete |
| LIBERO-Spatial (plan_010) | §4.2 | Complete |
| Full-layer R² scan (plan_011) | §4.2, Table 4 | Complete |
| CLIP-ViT control (plan_012) | §4.7, Table 12 | Complete |
| Branch-split RSA (plan_013) | §4.7 (brief) | Complete |
| Cross-arch R² matrix | §4.2, Table 5 | Complete (10/12 cells) |
| Cross-arch L1 attention | §4.4, Table 8 | Complete |
| Cross-arch CF sensitivity | §4.3, Table 7 | Complete (6 conditions) |
| Three-tier gradient | §4.5, Table 10 | Complete but N=1 at Tier-2 |
| OpenVLA Goal standardized | §4.2 | Complete (matches original) |
| OpenVLA Spatial standardized | §4.2 | Complete (weak result Δ=0.040) |
| D090 synthesis | §4.4, Table 9 | Complete |

**Coverage assessment:** The paper covers the experiment list well in breadth. The key gaps are not in coverage but in **missing controls** (NLP fine-tuning baseline) and **depth** (per-layer RSA only for OpenVLA, encoder comparison only for OpenVLA).

---

## Consolidated Scores

| Dimension | R1 | R2 | Consensus |
|---|---|---|---|
| Soundness | 4 | 4 | 4 |
| Novelty | 4 | 3 | 3.5 |
| Significance | 3 | 3 | 3 |
| Clarity/Presentation | 5 | 4 | 4.5 |
| **Overall** | **4** | **4** | **4** |
| Confidence | 4/5 | 4/5 | High |

**Overall Score: 4/10 — Below acceptance threshold (Reject)**

---

## Key Recommendations for Revision

1. **[Essential] Add NLP fine-tuning control.** Fine-tune Llama-2 on an NLP supervised task (e.g., instruction following or summarization) and run the same R² exit analysis. This single experiment would resolve whether exit collapse is VLA-specific or generic.

2. **[Essential] Add behavioral validation.** Even one intervention experiment connecting representational findings to task performance would transform the paper's fit for CoRL. Candidates: (a) early-exit decoding to test whether intermediate-layer representations outperform exit representations for action prediction, (b) attention masking on identified routing heads to measure behavioral impact.

3. **[Important] Resolve the baseline fairness issue.** Use NLP-fine-tuned LLMs (or at minimum, VLMs fine-tuned on non-robotic tasks) as CF sensitivity baselines instead of random-init or base VLM models.

4. **[Important] Add per-layer RSA curves for TracVLA/NORA.** The inverted-U pattern cannot be claimed as general without cross-architecture verification.

5. **[Important] Add formal statistical test for directional consistency.** A sign test or permutation test on the 9/10 directional result would strengthen the matrix analysis.

6. **[Moderate] Fix broken references.** Multiple [? ?] citations must be resolved.

7. **[Moderate] Compress instruction invariance experiments.** Plans 006/007/008 all verify a structurally guaranteed null result. Compress to a single paragraph with Table 2 in appendix.

8. **[Moderate] Expand related work.** Engage with mechanistic interpretability literature, representation compression in fine-tuning, and probing methodology critiques.

9. **[Moderate] Address training-procedure confound.** Discuss or control for the possibility that self-trained checkpoints (TracVLA, NORA) have stronger exit collapse due to training procedure differences rather than architectural generality.

---

## Summary

This paper presents a well-designed diagnostic framework for VLA representational analysis and demonstrates commendable scientific honesty in its self-critique. However, the central empirical finding (R² exit collapse) is critically confounded by the missing NLP fine-tuning control, the cross-architecture matrix shows high variability (172× range) with the community checkpoint yielding the weakest results, counterfactual sensitivity uses unfair baselines, and the paper lacks any behavioral validation connecting representational findings to robot task performance. The paper's own contribution audit (Table 9) leaves only thin, questionable findings after removing the base-model-dependent L1 routing. While the framework itself is a genuine contribution, it is insufficient to stand alone at a robot learning venue without stronger demonstrations of its analytical value. We recommend rejection with encouragement to resubmit after adding the NLP fine-tuning control and behavioral validation experiments.

**Verdict: Reject (4/10)**


---

## 引用验证结果

**统计**: 62 篇文献 / 98 处引用 / 在线验证 62/62 篇

### 问题 (14)

- ⚠️ `liu2023_libero` — 元数据不匹配: first_author: bib=liu vs api=feng
- ⚠️ `haon2025` — 元数据不匹配: first_author: bib=h\"aon vs api=häon
- ⚠️ `fei2025` — 元数据不匹配: first_author: bib=fei vs api=senyu
- ⚠️ `meng2022_rome` — 元数据不匹配: first_author: bib=meng vs api=andonian
- ❌ `elhage2021` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.22 below threshold 0.82
- ❌ `hewitt2019` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.32 below threshold 0.82
- ⚠️ `neo2025` — 元数据不匹配: first_author: bib=neo vs api=leng
- ⚠️ `lakens2017equivalence` — 元数据不匹配: title: similarity=0.34 (possible wrong DOI)
- ❌ `bills2023language` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.31 below threshold 0.82
- ❌ `templeton2024scaling` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.26 below threshold 0.82
- ❌ `nostalgebraist2020` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.35 below threshold 0.82
- ⚠️ `padalkar2023_oxe` — 元数据不匹配: first_author: bib=padalkar vs api=collaboration
- ⚠️ `michel2019sixteen` — 元数据不匹配: year: bib=2019 vs api=2014, first_author: bib=michel vs api=narla
- ⚠️ `ouyang2022training` — 元数据不匹配: first_author: bib=ouyang vs api=agarwal

### ✅ 通过 (48)