---
dream_id: dream_20260525T050917
tier: worst
overall_score: 5/10 — Weak Reject (Marginally Below)
timestamp: 2026-05-25T06:34:52.067450+00:00
---

# Dream Review Report: "A Systematic Study of Token Pruning Strategies Across VLA Architectures"

**Venue**: CoRL 2026
**Review Mode**: Full (2 Reviewers + AC Roundtable)
**R1 Score**: 6/10 (Methods + Experiments) | **R2 Score**: 5/10 (Novelty + Related Work) | **AC Consolidated**: 5.5/10

---

## 1. Paper Summary

This paper presents a systematic empirical study of vision token pruning across 5 VLA architectures (π0 3.3B, π0.5 4B, X-VLA 880M, OpenVLA 7B, SmolVLA 450M) spanning 3 connector families (linear projection, MLP, pixel-shuffle), evaluated on 4 LIBERO task suites (Object, Spatial, Goal, Long-horizon) with 3 pruning methods (L2-norm, random, attention-based). The study reveals three principal findings: (1) pixel-shuffle connectors create irreversible token entanglement where removing even 5% of tokens collapses SR to 0% across all suites; (2) importance metric selection produces larger performance gaps (56.6pp) than connector architecture variation; (3) VTR recovers pixel-shuffle models from 0% to ~59% ≈ baseline but fails entirely on MLP-projector architectures. A CV-based diagnostic and 2-axis framework are proposed but achieve only ~62% prediction accuracy cross-suite.

---

## 2. Agreed Strengths

**S1. Unprecedented cross-architecture breadth.** 5 models × 4 suites × 3 methods × 6+ retention ratios is the most comprehensive VLA pruning comparison to date. No concurrent work (SP-VLA, VLA-IAP, LightVLA, EfficientVLA, Compressor-VLA, See What Matters) evaluates pruning across more than 1-2 architectures. The factorial design enables interaction effects that single-architecture studies cannot detect.

**S2. Pixel-shuffle catastrophic cliff is definitive.** SmolVLA collapses to 0% SR at k=0.95 (removing only 6 of 128 tokens) across all 4 LIBERO suites, all pruning methods tested (L2-norm, random, attention, geometric prior), and both checkpoints (LoRA-reproduced and official HuggingFace). The mechanism is clearly explained: pixel-shuffle 4×4 folding creates non-overlapping receptive fields with zero inter-token redundancy. This is a rigorous, practically important negative result.

**S3. Double dissociation between scoring method and connector type.** The paper's strongest and most novel finding. Attention-based scoring achieves 99.2% on X-VLA Object at k=0.5 while L2-norm achieves 42.6% (56.6pp gap). Conversely, on π0.5, L2-norm outperforms random by up to 93pp at k=0.85. This structural interaction is non-obvious, validated across multiple suites and retention ratios, and has immediate practical implications.

**S4. Intellectual honesty and transparent limitations.** Both reviewers commend the paper's unusual candor. The confounder analysis acknowledges that models differ simultaneously in backbone, encoder, scale, and connector. VTR failure on OpenVLA is reported rather than suppressed. The CV diagnostic's small sample size is flagged. The paper refrains from overclaiming VTR "exceeds baseline." This level of honesty is rare and scientifically valuable.

**S5. Multi-seed validation for key claims.** SmolVLA cliff (dual-seed, dual-checkpoint), π0.5 cliff zone (sub-1pp std), X-VLA cliff localization (3-seed, std=0.31pp at k=0.85), and VTR M-curve (3-seed for all M values) are all multi-seed validated. Cross-seed deltas are typically under 5pp, confirming architectural rather than stochastic phenomena.

**S6. Non-monotonic phenomena carefully documented.** The π0.5 random cliff at k=0.85-0.925, the X-VLA k=0.85/k=0.80 inversion (21pp gap from 2 tokens), and the π0.5 L2-norm V-shaped curve are all multi-seed confirmed with mechanistic accounts.

---

## 3. Agreed Weaknesses

**W1. CV diagnostic is statistically underpowered.** The "scaling law" and "continuous spectrum" claims rest on only 3 closed-loop data points for strategy prediction (π0.5, X-VLA, OpenVLA). SmolVLA contributes nothing to strategy comparison (both methods = 0%). A perfect monotonic ordering with n=3 has probability 1/6 under null — barely significant. OFT and π0 contribute offline metrics only, padding model count to 6 without adding closed-loop validation. CV may be a proxy for connector type membership rather than an independent predictor.

**W2. Incomplete data matrix undermines "systematic" claim.** Main results have multiple "--" entries, particularly OpenVLA (only Object suite in most conditions; Goal/Spatial/Long missing or partial). Several X-VLA cells are absent. For a paper claiming "first systematic cross-architecture study," structural gaps are notable.

**W3. LIBERO-only evaluation.** All results from one simulation benchmark, one robot platform. No real-robot or multi-simulator validation. CoRL increasingly expects deployment evidence (acceptance rate 25-33%). LIBERO baselines vary widely across models (SmolVLA 59.2% vs X-VLA 99.2%), potentially confounding cross-model comparisons via headroom effects.

**W4. Confounded cross-model comparisons.** Models differ simultaneously in LLM backbone, vision encoder, scale (450M to 7B), training data, and connector. Only OFT vs OpenVLA provides semi-controlled comparison (same connector, same backbone), but OFT lacks closed-loop evaluation. The paper's language often implies connector is causally isolated when evidence is strictly correlational.

**W5. VTR contribution is narrow and architecturally derivative.** VTR is structurally identical to Perceiver Resampler / Q-Former. Validated on SmolVLA only; fails on OpenVLA (0% SR across all M values). The investigation of failure is insufficient: no alternative learning rates, no frozen-backbone ablation. VTR training uses batch size 4 vs official 512, creating a baseline discrepancy (44.8% vs 59.2%).

**W6. No efficiency measurements.** The abstract motivates work by "computational bottleneck for real-time robotic control," yet contains no systematic latency, throughput, or memory benchmarks. The only efficiency figure is a brief 6% VTR speedup mention. For an efficiency-motivated paper, this is a notable omission.

---

## 4. Contested Points (AC Resolution)

**4a. Contribution novelty (R1: 3/4 vs R2: 2/4).**
R1 values the practical breadth; R2 emphasizes limited methodological novelty (CV is trivial, VTR is derivative, framework is descriptive). **AC Resolution**: The cross-architecture breadth and double dissociation are genuine contributions exceeding "running existing methods on more models" — interaction effects could not have been discovered by single-architecture studies. However, the 2-axis framework is descriptive rather than predictive. **Consolidated: 2.5/4.**

**4b. Paper framing of the 2-axis framework.**
The framework is listed as Contribution #1 in the introduction. The 62% accuracy figure appears in project documents but the submitted paper presents the framework more positively. Both reviewers are justified in engaging with it as a positive claim. **AC Resolution**: Reviewers' treatment is appropriate; the paper would benefit from more explicit main-text acknowledgment of framework limitations.

---

## 5. Factual Corrections

**5a. "Single pruning ratio" (both R1 and R2).** INCORRECT. The paper evaluates k ∈ {0.30, 0.50, 0.70, 0.85, 0.90, 0.925, 0.95} with additional values for specific models. Tables 3, 5, 6 show full degradation curves. This criticism is struck from the record.

**5b. "No figures" (R2).** The paper is table-dense (11 tables) but the concern about visual density is legitimate. The paper would benefit from consolidating some tabular data into degradation curve plots.

**5c. Neither factual error changes the overall assessment by more than ~0.5 points.** The substantive concerns about CV validation, sim-only evaluation, VTR scope, and data completeness remain.

---

## 6. Key Questions for Rebuttal

**Q1. CV beyond connector type membership.** Can you demonstrate CV is predictive beyond what connector family already tells you? Within MLP family (OpenVLA CV=0.215 vs OFT CV=0.219, Δ=0.004), does the CV difference correspond to measurable pruning robustness difference? If not, CV is a 3-bin discrete classifier, not a continuous predictor.

**Q2. Attention-based scoring on additional models.** The double dissociation has only two entries: X-VLA (attention effective) and π0.5 (attention harmful on Object). Does attention help or hurt on OpenVLA (MLP, CV=0.215)? Completing this cell would either strengthen or complicate the dissociation pattern.

**Q3. Efficiency measurements.** Can you provide wall-clock latency and peak GPU memory for at least two models at two retention ratios? A paper motivating pruning by efficiency must quantify efficiency gains, not just accuracy costs.

**Q4. VTR batch size confound.** VTR trained at batch=4 yields LoRA baseline 44.8% vs official 59.2% at batch=512. VTR recovery to ~60% could partly reflect reduced baseline training quality. How confident are you VTR at official batch size would still exceed baseline?

**Q5. X-VLA CV reconciliation.** X-VLA (CV=0.151, "entangling") has lower CV than OpenVLA (CV=0.215, "independent"). If CV measures entanglement, entangling connectors should produce higher CV. How do you reconcile this ordering?

---

## 7. Missing Elements (ranked by impact)

1. **Complete data matrix** — fill all "--" entries, especially OpenVLA cross-suite
2. **Efficiency benchmarks** — latency (ms/action), peak GPU memory, throughput (Hz)
3. **Attention-based scoring on OpenVLA** — completes the dissociation table
4. **Head-to-head with one concurrent method** — e.g., VLA-IAP or SP-VLA on same LIBERO setup
5. **Position-preserving ablation** — zero-mask control for π0.5 to isolate positional disruption
6. **Additional benchmark or real-robot validation** — even one model on one non-LIBERO benchmark
7. **Alternative diagnostic metrics** — compare CV against kurtosis, effective rank, pairwise cosine similarity

---

## 8. Limitations Assessment

The paper's limitation reporting is **above average** for the field:
- Simulation-only evaluation explicitly stated
- Confounder analysis discusses backbone/encoder/scale confounds
- CV sample size hedged ("validated on four closed-loop architectures")
- VTR scope acknowledged (fails on OpenVLA)
- Baseline discrepancy noted (LoRA-reproduced vs official)
- Single-seed caveat provided

**Gap**: Some deeper self-awareness (e.g., the 62% framework accuracy, data matrix incompleteness) surfaces in project documents but not fully in the submitted paper. Key caveats are in the appendix; a main-text reader may overestimate claim strength.

---

## 9. CoRL Relevance

Token pruning for VLA efficiency is directly relevant to robot learning. The cross-architecture perspective fills a genuine gap as concurrent works each validate on 1-2 architectures. Practical recommendations (measure CV, use attention on entangling connectors, use L2-norm on independent connectors, avoid deletion on pixel-shuffle) are immediately actionable.

**However**, CoRL increasingly expects real-robot or multi-simulator validation. A pure LIBERO simulation study may be better suited to NeurIPS/ICML where empirical analysis is more valued and sim-only less penalized. The paper's analysis contribution is stronger than its method contribution, which slightly misaligns with CoRL's emphasis on methods and systems.

**Verdict**: Topically appropriate for CoRL; sim-only limitation is more significant here than at ML venues.

---

## 10. Final Scores

| Dimension | R1 | R2 | AC Consolidated |
|-----------|----|----|-----------------|
| Soundness | 2/4 | 2/4 | **3/4** (upgraded: "single ratio" error corrected; methodology is rigorous where data exists) |
| Presentation | 3/4 | 2/4 | **2.5/4** (well-organized but 11-table density, key caveats in appendix) |
| Contribution | 3/4 | 2/4 | **2.5/4** (genuine empirical novelty but limited theoretical/methodological advance) |
| **Overall** | **6/10** | **5/10** | **5/10** |
| Confidence | 4/5 | 4/5 | **4/5** |

**Overall Justification (5/10 — Marginally Below)**: The paper addresses a timely question with the most comprehensive cross-architecture VLA pruning evaluation to date. The double dissociation and pixel-shuffle cliff are genuinely novel and practically valuable findings. Intellectual honesty is exemplary.

However, the combination of weaknesses places it below CoRL acceptance threshold:
- CV "scaling law" is a 3-point correlation, possibly a proxy for connector type
- Structural data gaps in main results
- No efficiency measurements for an efficiency-motivated paper
- VTR narrowly validated (1 model) and architecturally derivative
- Simulation-only on single benchmark
- 2-axis framework is descriptive, not predictive

No single weakness is fatal, but their combination places the paper below the top 25-33%.

---

## 11. Recommendation

**Weak Reject (5/10).**

The paper provides genuinely useful empirical knowledge — the cross-architecture breadth is a real differentiator, and the double dissociation and pixel-shuffle cliff are findings the community needs. Intellectual honesty throughout is exemplary. However, the combination of underpowered CV validation, structural data gaps, absent efficiency benchmarks, narrow VTR scope, simulation-only evaluation, and a descriptive (not predictive) theoretical framework collectively place it below the CoRL acceptance threshold.

**What would move to accept**: (a) Complete OpenVLA cross-suite data; (b) add attention scoring on OpenVLA; (c) validate CV on 2-3 additional VLAs; (d) provide wall-clock efficiency measurements; (e) any non-LIBERO validation. Items (a), (b), (d) are achievable within a revision cycle and would likely move to solid accept.

**What would move to clear reject**: (a) Additional VLA models break monotonic CV ordering; (b) OpenVLA cross-suite reveals MLP projectors also cliff on complex tasks; (c) VTR failure on OpenVLA shown to be training protocol issue rather than architectural.

**Alternative venues if rejected**: NeurIPS 2026 (empirical analysis track), ICML 2026 (sim-only less penalized), RSS 2027 (if real-robot validation added).

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