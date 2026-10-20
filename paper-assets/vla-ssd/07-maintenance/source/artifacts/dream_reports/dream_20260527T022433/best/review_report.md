---
dream_id: dream_20260527T022433
tier: best
overall_score: borderline accept
timestamp: 2026-05-27T03:24:21.209407+00:00
---

# Dream Review Report: Instruction Routing in Vision-Language-Action Models

**Paper:** Instruction Routing in Vision-Language-Action Models: A Cross-Architecture Token-Level Analysis
**Venue:** CoRL 2026
**Dream ID:** 20260527T022433
**Review Mode:** Full (2 Reviewers + Roundtable)

---

## 1. Paper Summary

This paper presents a systematic experimental framework for token-level analysis of decoder-only Vision-Language-Action models (VLAs), validated across three architectures (OpenVLA/Llama-2-7B, TracVLA/Phi-3-mini, NORA/Qwen2.5-VL-3B) and four LIBERO task suites. Using six complementary methods (RSA, CKA, action probes, cross-instruction classification, attention profiling, counterfactual perturbation), the paper reports three main findings: (1) VLA fine-tuning reorganizes instruction attention from mid-layer inverted-U to entry-exit bookend pattern with immediate L1 routing (99.6%); (2) R² exit collapse is a one-time signature of VLM→VLA transitions (6/6 cells, Δ=0.138–0.691) absent in VLA→VLA (0/4 cells); (3) vision encoder geometry under RSA is invariant to training and instruction content (Δρ<0.017). These are unified by a three-tier routing gradient from VLM base through general VLA to task-specific VLA.

---

## 2. Reviewer Assignments & Scores

### R1: Methods & Experiments

| Dimension | Score |
|-----------|-------|
| Quality | 7/10 |
| Clarity | 6/10 |
| Significance | 5/10 |
| Relevance | 6/10 |
| Overall | 6/10 |
| Confidence | 4/5 |

### R2: Novelty & Related Work

| Dimension | Score |
|-----------|-------|
| Originality | 6/10 |
| Clarity | 8/10 |
| Significance | 5/10 |
| Relevance | 8/10 |
| Overall | 6/10 |
| Confidence | 4/5 |

### Roundtable Consensus Scores

| Dimension | Consensus | Rationale |
|-----------|-----------|-----------|
| Originality | 6/10 | Trained-vs-reference decomposition and exit-collapse transition specificity are genuinely new; individual methods are standard |
| Quality | 7/10 | Thorough methodology with appropriate controls, robustness checks, and unusually honest statistics; limited by N=2 for core finding |
| Clarity | 7/10 | Well-organized with careful claim-evidence mapping; occasional overclaiming relative to evidence strength |
| Significance | 5/10 | Observational characterization without behavioral validation or actionable design guidance |
| Relevance | 7/10 | VLA+LIBERO directly relevant to CoRL; purely analytical nature somewhat attenuates robotics fit |
| **Overall** | **6/10** | **Marginally above acceptance threshold** |

---

## 3. Consolidated Strengths

### S1. Well-designed factorial controls and cross-architecture validation (R1, R2)
The 3×4 matrix spanning three distinct backbone families (Llama-2, Phi-3, Qwen2.5) with different attention mechanisms (MHA vs GQA), vision encoders, and training pipelines provides genuine evidence of generality. The natural experiment created by different reference baselines (VLA→VLA for OpenVLA vs VLM→VLA for TracVLA/NORA) cleanly isolates the contribution of action-oriented training. The NLP finetuning control across all three backbone families (ΔR²=0.000 uniformly) is a compelling negative control.

### S2. Triangulation across complementary methods (R1)
The paper combines correlational/decodability (probing), behavioral/input-output (counterfactual perturbation), and interventional (attention head ablation) evidence. The six-method consistency table and convergent evidence mapping across methods is methodologically rigorous and demonstrates framework robustness.

### S3. Unusually honest statistical reporting (R1, R2)
The paper explicitly acknowledges underpowered analyses (RSA training effect power=0.356), reports Bonferroni correction across all 63 tests (40/45 survive), flags which comparisons lose significance under correction, uses careful correlational language throughout, and presents a claim-evidence-scope mapping that distinguishes what training creates versus what it inherits. This level of transparency exceeds the norm for the field.

### S4. The exit-collapse finding is non-obvious and well-supported (R2)
The clean binary separation between VLM→VLA (6/6 above threshold) and VLA→VLA (0/4 below) was not predictable from prior work. Combined with the NLP control (ΔR²=0.000 across three backbones), this constitutes genuine evidence that exit collapse is specific to the VLM-to-VLA transition rather than a generic fine-tuning artifact.

### S5. The trained-vs-reference decomposition is novel in VLA literature (R2)
No prior VLA interpretability work performs systematic comparison of trained versus untrained/reference representations within the same architecture. The distinction between training-induced effects (exit collapse, counterfactual sensitivity) and inherited properties (L1 head counts) is a genuine conceptual contribution.

### S6. Comprehensive engagement with concurrent VLA interpretability work (R2)
The related work section engages substantively with the recent explosion of VLA interpretability studies (Grant et al. 2026, Swann et al. 2026, Haon et al. 2025, etc.) and core mechanistic interpretability references (Elhage et al. 2021, Olsson et al. 2022, etc.).

---

## 4. Consolidated Weaknesses

### W1. [Major] N=2 independent VLM→VLA transitions limits the core finding (R1, R2)
The exit collapse finding—the paper's strongest result—rests on only two independent VLM→VLA transitions (TracVLA and NORA). While the permutation test yields p=0.008, this is across 9 cells from only 2 architectures (not independent). The three-tier gradient has N=1 at Tier 2 (only OpenVLA). Architectures outside the causal-decoder family (flow-matching, diffusion-based VLAs like π₀ or Octo) are entirely untested. A two-tier distinction (VLM vs VLA) would be better supported; the three-tier framing is speculative given N=1 at Tier 2.

### W2. [Major] No closed-loop behavioral validation (R1, R2)
All analyses are open-loop. The paper reports a failed closed-loop attempt (SR=0/3). The correlation between ΔR² and published success rates (ρ=0.583, p=0.10, n=9) is non-significant and underpowered. The discovery that ablating 24/32 instruction-dominant heads produces d=0.65 trajectory divergence but near-zero change in ground-truth MSE (p=0.52) raises a genuine question: if removing most instruction heads doesn't increase action error, what is their functional significance? The "direction rather than precision" interpretation is post-hoc. For a robotics venue, this gap substantially weakens practical impact claims.

### W3. [Moderate] Counterfactual metric incomparability (5/8 cross-architecture cells) (R1)
NORA and reference VLMs use cosine distance on hidden representations while OpenVLA and TracVLA use Cohen's d on action outputs. This means the counterfactual finding cannot be uniformly evaluated across the full matrix. The paper correctly identifies this limitation and avoids cross-metric ratios, but it constrains the strength of the cross-architecture counterfactual claim. NORA Goal saturation (cos=1.0) likely reflects numerical issues rather than genuine maximal sensitivity.

### W4. [Moderate] Δ>0.10 threshold is descriptive, not principled (R1)
The threshold is presented as a "natural effect-size boundary" with threshold sensitivity analysis showing any value in (0.097, 0.156) yields identical grouping. However, the gap between groups is 0.059, and 2 of 9 CIs overlap. There is no theoretical grounding for why 10% explained variance drop should be the meaningful boundary. The analysis is performed on the same data used to establish the pattern.

### W5. [Moderate] Specificity control undermines the "dedicated routing" narrative (R1)
Instruction-dominant head ablation (d=0.65) vs random-24 head ablation (d=0.60) yields only an 8% gap. The identified instruction-dominant heads are not substantially more important than arbitrary head selections. The random-subset analysis shows dominant-head ablation falls below all 30 random subsets for R² increase. The paper honestly acknowledges this but it substantially reduces the practical value of the instruction-dominant head classification.

### W6. [Moderate] Insufficient engagement with representation transformation literature (R2)
The exit-collapse phenomenon has parallels to the "logit lens" / "tuned lens" literature (Belrose et al. 2023) showing intermediate layers can be more informative than final layers. The paper does not connect to the broader fine-tuning distortion literature (Merchant et al. 2020). Missing NLP probing references: Tenney et al. (2019), Jawahar et al. (2019), Rogers et al. (2020). Voita et al. (2019) on attention head pruning is directly relevant but absent.

### W7. [Moderate] NORA analyses are incomplete (R1)
Only 2/4 LIBERO suites are available for NORA. NORA Goal has unreliable bootstrap CIs (exit-layer R²≈-0.006). NORA counterfactual is limited to cosine distance. The third architecture contributes substantially less evidence than the other two.

### W8. [Moderate] NLP control design gap (R1, R2)
The NLP controls (chat-finetuned models) lack vision encoders—they test whether NLP finetuning of a *text-only* model produces exit collapse, not whether NLP finetuning of a *VLM* produces exit collapse. A more compelling control would be an instruction-tuned VLM (e.g., LLaVA-chat or InstructBLIP) finetuned on visual QA but not actions.

### W9. [Minor] Some findings confirm rather than extend prior work (R2)
The L1 inherited routing finding is largely expected from Zhang et al. (2026, "Instruction Anchor"). The RSA-CKA dissociation is well-established in the representation similarity literature (Ding et al. 2021, Raghu et al. 2017). The counterfactual perturbation methodology is adapted from existing behavioral protocols (Fang et al. 2026, Hou et al. 2026). The paper should more explicitly distinguish confirming versus extending contributions.

---

## 5. Key Questions for Authors

1. **Functional significance of instruction heads:** The ablation produces d=0.65 divergence with ΔMSE≈0. Can you provide success rate impact or any behavioral grounding for the "direction rather than precision" interpretation?

2. **Multimodal NLP control:** Have you considered running analysis on instruction-tuned VLMs (e.g., LLaVA-chat) that receive visual input but have no action training? This would close the most significant control gap.

3. **Permutation test independence:** The p=0.008 treats architecture-suite cells as independent, but cells from the same architecture share weights. How does this dependence affect validity?

4. **OpenVLA exit collapse convergence:** Could the VLA→VLA absence of exit collapse simply reflect that OpenVLA already underwent exit collapse during OXE pretraining, leaving no further collapse to occur? This would make it a convergence statement rather than a qualitative transition-type distinction.

5. **Training dynamics:** Even 2-3 intermediate checkpoints would reveal whether exit collapse is sudden or gradual. Is this feasible?

6. **L1 attention reconciliation:** How do you reconcile "L1 routing is inherited" with the OpenVLA gradient (0→9→24 heads)? The 9→24 jump appears training-induced.

7. **R²=0.155 floor in NLP controls:** Can you confirm this is not an artifact? What action labels are text-only NLP models being probed against?

---

## 6. Missing Experiments (Priority-Ordered)

1. **Closed-loop behavioral validation** — Even simplified action-prediction accuracy on held-out demos would help. This is the single most impactful addition for CoRL.
2. **Additional VLA architecture family** — One diffusion or flow-matching VLA (π₀, Octo) would test whether findings are specific to autoregressive/tokenized-action models.
3. **Multimodal NLP control** — Instruction-tuned VLM without action training (LLaVA-chat, InstructBLIP).
4. **Training dynamics** — 2-3 intermediate checkpoints to reveal exit collapse onset timing.
5. **Second Tier-2 architecture** — Another general-purpose VLA to validate the three-tier gradient beyond N=1.

---

## 7. Missing Related Work

- Belrose et al. (2023), "Eliciting Latent Predictions from Transformers with the Tuned Lens" — exit collapse parallel
- Tenney et al. (2019), "BERT Rediscovers the Classical NLP Pipeline" — canonical layer-wise probing
- Rogers et al. (2020), "A Primer in BERTology" — probing methodology survey
- Voita et al. (2019), "Analyzing Multi-Head Self-Attention" — attention head pruning/specialization
- Merchant et al. (2020), "What Happens to BERT Embeddings During Fine-tuning?" — fine-tuning distortion
- Geva et al. (2023), "Dissecting Recall of Factual Associations" — layer-wise information flow
- Ding et al. (2021), "Grounding Representation Similarity Through Statistical Testing" — RSA/CKA comparison methodology

---

## 8. Experiment Coverage Assessment

The paper covers the experimental design comprehensively. Cross-referencing against the 20 imagined experiments in `review_context.yaml`:

| Experiment | Covered? | Notes |
|------------|----------|-------|
| SigLIP+Projector RSA (plan_001) | ✓ | Table 2 |
| DINOv2 Baseline (plan_002) | ✓ | Table 3 |
| Per-layer RSA (plan_003) | ✓ | Table 6 |
| Output Head Analysis (plan_004) | ✓ | Table 1 |
| 6 Methods × 2 Benchmarks (plan_005) | ✓ | Table 8 |
| Instruction Ablation (plan_006) | ✓ | Table 10 |
| 2×2 Matrix (plan_007) | ✓ | Table 9 |
| Random Instruction Control (plan_008) | ✓ | Table 11 |
| CKA Verification (plan_009) | ✓ | Table 7 |
| LIBERO-Spatial Extension (plan_010) | ✓ | Table 24 |
| Full-layer R² Scan (plan_011) | ✓ | Table 15 |
| CLIP Control (plan_012) | ✓ | Table 4 |
| Branch-Split RSA (plan_013) | ✓ | Table 5 |
| Cross-Arch R² Collapse (cross_arch_r2_collapse) | ✓ | Table 18 |
| Cross-Arch CF (cross_arch_cf) | ✓ | Tables 20-21 |
| Three-Tier Gradient (three_tier_gradient) | ✓ | Table 22 |
| NLP Control (nlp_control) | ✓ | Table 19 |
| Cross-Arch L1 Heads (cross_arch_l1_heads) | ✓ | Table 23 |
| Cross-Instruction Probe (cross_inst_probe) | ✓ | Table 12 |
| Dense Attention Profile (dense_attention_profile) | ✓ | Table 14 |
| CF Trajectory Analysis (cf_trajectory_analysis) | ✓ | Table 16 |
| Training Trajectory (training_trajectory) | ✓ | Table 17 |
| TracVLA Mixed Heads (tracvla_mixed_heads) | ✓ | Table 25 |
| L1 Attention Three-Condition (l1_attention_three_cond) | ✓ | Table 13 |

**Coverage: 24/24 (100%).** All imagined experiments are represented in the paper. The numerical values in the paper are consistent with the expected results in the design document.

---

## 9. Overall Assessment

### Verdict

This paper presents a methodologically rigorous representational analysis of VLA fine-tuning with several genuine contributions: the trained-vs-reference decomposition is novel in VLA literature, the R² exit collapse finding (6/6 VLM→VLA vs 0/4 VLA→VLA) is non-obvious and well-controlled, and the statistical reporting is unusually honest. The experimental coverage of the design space is comprehensive (100% of planned experiments executed).

However, the paper faces significant limitations for a robotics venue. The core finding rests on N=2 independent VLM→VLA transitions within a single architecture family (causal-decoder). The complete absence of closed-loop behavioral validation—combined with the counter-intuitive result that ablating 24/32 instruction heads produces near-zero MSE change—leaves the functional significance of the identified routing structures unresolved. The three-tier routing gradient is overstated given N=1 at Tier 2. Some findings (inherited L1 routing, RSA-CKA dissociation) confirm rather than extend prior knowledge.

The paper sits at the CoRL acceptance boundary. The methodology and framework design are strong contributions to VLA understanding, but the limited architectural scope, absent behavioral grounding, and primarily observational nature constrain the impact. Adding one non-autoregressive VLA architecture and any form of behavioral validation would move this decisively above the threshold.

### Recommendation: **Borderline Accept** (6/10)

The paper merits publication if the authors can address the most critical gaps in revision (behavioral validation, positioning relative to representation transformation literature). In its current form, it represents solid foundational work that the VLA community would benefit from, but falls short of the impact expected at a top robotics venue.

---

*Review completed by 2 independent reviewers (R1: Methods & Experiments, R2: Novelty & Related Work) with full roundtable convergence (Steps 1-4).*

---

## 引用验证结果

**统计**: 55 篇文献 / 102 处引用 / 在线验证 55/55 篇

### 问题 (14)

- ❌ `hancock2025actions` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.33 below threshold 0.82
- ⚠️ `mitra2025mechanistic` — 元数据不匹配: first_author: bib=mitra vs api=chancharik
- ⚠️ `grover2025preserving` — 元数据不匹配: first_author: bib=grover vs api=shresth
- ⚠️ `liu2023_libero` — 元数据不匹配: first_author: bib=liu vs api=feng
- ⚠️ `haon2025` — 元数据不匹配: first_author: bib=h\"aon vs api=häon
- ⚠️ `fei2025` — 元数据不匹配: first_author: bib=fei vs api=senyu
- ⚠️ `meng2022_rome` — 元数据不匹配: first_author: bib=meng vs api=andonian
- ❌ `elhage2021` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.22 below threshold 0.82
- ⚠️ `lakens2017equivalence` — 元数据不匹配: title: similarity=0.34 (possible wrong DOI)
- ⚠️ `padalkar2023_oxe` — 元数据不匹配: first_author: bib=padalkar vs api=collaboration
- ⚠️ `michel2019sixteen` — 元数据不匹配: year: bib=2019 vs api=2014, first_author: bib=michel vs api=narla
- ⚠️ `ouyang2022training` — 元数据不匹配: first_author: bib=ouyang vs api=agarwal
- ⚠️ `long2026understanding` — 元数据不匹配: first_author: bib=long vs api=lin
- ⚠️ `xiao2025ava` — 元数据不匹配: first_author: bib=xiao vs api=lei

### ✅ 通过 (41)