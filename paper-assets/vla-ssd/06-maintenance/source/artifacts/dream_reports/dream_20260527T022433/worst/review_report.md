---
dream_id: dream_20260527T022433
tier: worst
overall_score: Reject (4/10)
timestamp: 2026-05-27T03:39:05.018053+00:00
---

# Dream Review Report — CoRL 2026 Submission

**Paper:** "Profiling Instruction Routing in Vision-Language-Action Models: A Cross-Architecture Diagnostic Framework"
**Venue:** CoRL 2026 (Austin, TX; acceptance rate ~30%)
**Review Mode:** Full (2 Reviewers + Roundtable)
**Dream ID:** 20260527T022433

---

## Venue Calibration

CoRL uses a 1–10 scale (1 = strong reject, 5 = marginally below threshold, 6 = marginally above, 10 = strong accept). CoRL strongly values behavioral/systems results and relevance to robot learning. Purely analytical work without closed-loop or at minimum open-loop policy evaluation faces a high bar. Historical acceptance ~30%.

---

## Reviewer R1 — Methods & Experiments

### Summary
The paper presents a factorial diagnostic framework (3 architectures × 4 task suites, 6 probing methods, counterfactual perturbation) for profiling instruction routing in decoder-only VLAs. It identifies R² exit collapse as a VLM→VLA transition marker and counterfactual sensitivity in trained VLAs, while honestly reporting that L1 attention patterns are base-model artifacts and that metrics disagree (CKA reverses RSA ordering). The analysis is entirely open-loop with no behavioral validation.

### Strengths
- **Well-structured factorial design.** The 3-arch × 4-suite matrix with explicit VLM→VLA vs VLA→VLA separation is principled. Asymmetric baselines are correctly identified rather than hidden.
- **Thorough statistical methodology on exit collapse.** MCCV n=1000, demo-level splitting (no train-test leakage), winner's-curse mitigation (fixed canonical peak layer), permutation tests (p=0.008), seed sensitivity (4 seeds, std<0.02), threshold robustness over (0.097, 0.156) interval.
- **Commendable self-critique.** Honest flagging of metric incommensurability (5/7 CF pairs), N=1 at Tier-2, non-significant behavioral correlation (ρ=0.583, p=0.10), CKA reversal, and unreliable NORA-Goal bootstrap CIs.
- **NLP fine-tuning controls.** Three backbone-matched chat models all show ΔR²=0.000, confirming exit collapse is action-training-specific, not generic fine-tuning.
- **Extensive appendix** (50+ pages) enabling replication.

### Weaknesses
- **No behavioral validation — fatal at CoRL.** The entire paper operates in open-loop representational analysis. The 0/3 closed-loop deployment failure is reported but not resolved. Behavioral correlation ρ=0.583 (p=0.10, power=0.37) is non-significant and underpowered. At a robotics venue, inability to connect any finding to task performance is disqualifying.
- **Head ablation reveals no functional specificity.** Specificity ratio = 1.08× (instruction-dominant d=0.651 vs random d=0.601). Most critically, ΔMSE = −0.001 (p=0.52) — ablating 24/32 "instruction routing" heads does not degrade action quality. This directly contradicts functional relevance claims and suggests routing is epiphenomenal.
- **CF metric incommensurability undermines cross-architecture claims.** 5/7 trained-vs-untrained pairs use incomparable metrics (Cohen's d in action space vs cosine in hidden space). Only OpenVLA allows fair comparison (Δ = +12–25%), but this is VLA→VLA marginal improvement, not dramatic VLM→VLA change.
- **N=2 for primary finding.** Exit collapse rests on 2 independent VLM→VLA transitions (TracVLA, NORA). OpenVLA's baseline is already a VLA so it doesn't contribute. N=2 is thin for "cross-architecture" generality.
- **CKA reversal undermines metric reliability.** RSA says training degrades geometry; CKA says training preserves/improves structure (Table 5). Proceeding with RSA throughout lacks principled justification. Conclusions are metric-dependent.
- **Trivially easy classification.** 10-way on 4096-dim features — even random-init achieves 100% at L1 (Table 1). The ceiling effect prevents meaningful gradient analysis.
- **2×2 factorial yields structurally guaranteed nulls.** RSA values 0.480–0.489 across all cells (Table 2). Instruction invariance is guaranteed by causal mask; training invariance by frozen encoder. Three experiments (plans 006/007/008) verify the same structural guarantee — over-verification, not contribution.
- **Permutation test fragility.** With choose(9,4)=126 permutations, p=0.008 means exactly 1/126 exceeds the observed gap — the test is at minimum resolution.

### Questions for Authors
1. Can you provide a unified CF metric (e.g., hidden-state cosine for all models) to enable true cross-architecture comparison?
2. How do you reconcile ΔMSE≈0 with claims of functional instruction routing? If ablating 75% of "routing" heads doesn't affect quality, what evidence supports functional relevance?
3. What would closed-loop evaluation require? Is the 0/3 failure a checkpoint issue or fundamental?
4. The R²≈0.155 noise floor is suspiciously uniform across 3 backbone families — can you confirm probes aren't learning marginal action distribution?

### R1 Scores
| Criterion | Score |
|-----------|-------|
| Soundness | 2/4 |
| Contribution | 2/4 |
| **Overall** | **4/10** |
| Confidence | 4/5 |

**R1 Recommendation: Reject**

---

## Reviewer R2 — Novelty & Related Work

### Summary
The paper applies existing interpretability methods (probing, RSA, CKA, attention profiling, counterfactual perturbation) to VLAs in a systematic manner. While the "first systematic VLA profiling toolkit" claim may be technically correct, the novelty is in application rather than methodology. The paper's own rigorous self-analysis (D090, ΔMSE≈0, metric dependence) systematically dismantles its empirical contributions, leaving the framework itself as the primary surviving contribution.

### Strengths
- **First-mover in VLA representational profiling.** No prior work has systematically applied multi-method representational analysis to VLAs. The framework is potentially reusable.
- **Exceptional intellectual honesty.** The D090 finding (L1 heads are base-model artifacts), openly reported ΔMSE≈0, CKA reversal, metric incommensurability, and self-predicted scores (Table 19: mean 4.67) are rare in ML papers. This transparency is scientifically commendable.
- **Proper scope calibration.** The abstract, discussion, and conclusion consistently avoid over-claiming. The paper positions findings as "primarily descriptive" and explicitly lists what it cannot conclude.
- **Cross-architecture design fills a gap.** Most VLA analysis papers study single architectures. The 3-architecture comparison, even with limitations, provides broader perspective.

### Weaknesses
- **Limited novelty — application, not innovation.** No new analysis methods, metrics, or theoretical frameworks are introduced. Every component (RSA, CKA, linear probes, attention profiling, counterfactual perturbation) is standard. The contribution is assembling them for VLAs, which is engineering rather than scientific novelty.
- **Significant related work gaps.** Missing citations that would contextualize findings:
  - *Neural collapse* (Papyan et al. 2020) — exit collapse may be a known fine-tuning phenomenon
  - *Logit lens / tuned lens* (nostalgebraist 2020; Belrose et al. 2023) — standard layer-wise analysis tools
  - *Fine-tuning distortion* (Merchant et al. 2020; Mosbach et al. 2020) — known that fine-tuning reorganizes deep layers
  - *Layer-wise probing* (Tenney et al. 2019; Rogers et al. 2020 "BERTology" survey) — canonical references
  - *Attention head pruning* (Voita et al. 2019; Michel et al. 2019) — directly relevant to head ablation analysis
  Without these, the paper cannot assess whether its findings are VLA-novel or already known in NLP/CV.
- **The paper's own evidence argues against its premise.** DINO achieves R²=0.687 without language or action training → actions are largely visual. Grant et al. shows visual dominance in VLA behavior. ΔMSE≈0 shows ablating routing heads doesn't matter. Token overlap ρ=1.0 shows CF sensitivity is lexical, not semantic. Together: instruction routing appears to be representationally present but functionally epiphenomenal. The paper is studying a phenomenon that its own data suggests doesn't matter.
- **Format specialization is the most parsimonious explanation for exit collapse** and has not been ruled out. When a language model is adapted to output 7-DoF actions, the exit layer naturally reorganizes for the new output format — this is architectural necessity, not a "routing mechanism." The NLP control (ΔR²=0.000) rules out generic fine-tuning but not domain-adaptation format change. Any LLM→specialist adaptation (e.g., LLM→code generation) likely shows similar exit reorganization.
- **Self-critique is honest but strategically devastating.** After D090 (L1 heads removed), Table 17 shows: L1 routing gradient = zero remaining value; bookend attention = exit engagement only; R² exit collapse = "one-time transition marker"; CF sensitivity = "unfair baselines"; framework = "primary contribution." The paper has effectively reviewed itself and found insufficient contribution. The self-predicted 4.67/10 mean is well-calibrated.
- **Three-tier gradient is under-supported.** N=1 at Tier-2, non-monotonic L1 head counts across tiers, exit collapse binary (not gradient). This finding should be removed or explicitly flagged as preliminary hypothesis, not presented in a numbered section.

### Questions for Authors
1. How does exit collapse relate to neural collapse (Papyan et al. 2020) and known fine-tuning distortion (Merchant et al. 2020)? Have you verified it's genuinely novel vs. a known phenomenon in a new domain?
2. Given DINO R²=0.687 and ΔMSE≈0, what is the practical value of understanding instruction routing if it doesn't functionally matter?
3. Could you test exit collapse in a non-VLA domain adaptation (e.g., LLM→code) to verify it's VLA-specific rather than generic domain-adaptation format specialization?
4. The "first systematic VLA profiling toolkit" claim — can you point to specific design decisions or methodological innovations that go beyond applying standard tools to a new domain?
5. If the framework's primary value is reusability, can you demonstrate it discovering something non-obvious and actionable on a new VLA?

### R2 Scores
| Criterion | Score |
|-----------|-------|
| Novelty | 1/4 |
| Significance | 1/4 |
| **Overall** | **4/10** |
| Confidence | 4/5 |

**R2 Recommendation: Reject**

---

## Roundtable Discussion

### Step 2: Cross-Sharing — Key Convergences
Both reviewers independently converge on score 4/10 (Reject) with high confidence (4/5). Major agreement areas:

1. **No behavioral validation is fatal at CoRL.** Both reviewers flag this as the single most impactful weakness. CoRL is a robotics venue; open-loop representational analysis without any connection to task performance falls below the venue's bar.
2. **ΔMSE≈0 undermines the entire instruction routing premise.** If ablating 75% of identified "instruction routing" heads doesn't degrade action quality, the phenomenon being studied appears epiphenomenal.
3. **Metric dependence (CKA reversal) undermines reliability.** Conclusions change depending on which metric is used, and no principled metric selection criterion is provided.
4. **The paper's honest self-critique is commendable but damaging.** Both reviewers appreciate the transparency but agree it effectively argues the paper isn't ready.

### Step 2: Cross-Sharing — Complementary Points
- **R1 adds:** Statistical fragility (permutation test at minimum resolution, N=2), over-verification of structural nulls (3 experiments for causal mask guarantee), per-layer RSA rise phase Δρ=0.016 within noise.
- **R2 adds:** Missing related work (neural collapse, logit lens, fine-tuning distortion, attention pruning), format specialization as alternative explanation, premise questioning (DINO superiority + visual dominance literature).

### Step 3: Convergence
No significant disagreements between reviewers. Both agree on:
- **Score range: 3.5–4.5** (consensus: 4)
- **Recommendation: Reject** (not borderline — multiple compounding issues)
- **The paper would be better suited** to an interpretability workshop or analysis-focused venue (ICLR, NeurIPS workshop on interpretability) rather than CoRL.
- **The framework has potential** if future work adds behavioral grounding and addresses the functional significance gap.

---

## Step 4: Consolidated Assessment

### Overall Scores

| Dimension | R1 | R2 | Consensus |
|-----------|----|----|-----------|
| Soundness / Novelty | 2/4 | 1/4 | 1.5/4 |
| Contribution / Significance | 2/4 | 1/4 | 1.5/4 |
| **Overall** | **4/10** | **4/10** | **4/10** |
| Confidence | 4/5 | 4/5 | 4/5 |

### Final Recommendation: **Reject** (4/10)

### Verdict Summary
The paper presents the first systematic multi-method, cross-architecture representational profiling framework for VLAs — a genuine first-mover contribution in methodology. The experimental execution is thorough, the statistical methodology on core findings is sound, and the intellectual honesty (D090, ΔMSE≈0, metric dependence, self-predicted scores) is rare and commendable.

However, multiple compounding issues prevent acceptance at CoRL:

1. **No behavioral validation** — fatal at a robotics venue. Open-loop representational analysis with 0/3 closed-loop deployment and non-significant behavioral correlation (p=0.10).
2. **ΔMSE≈0 from head ablation** — ablating 24/32 "instruction routing" heads doesn't degrade action quality, directly contradicting functional relevance and suggesting instruction routing is epiphenomenal.
3. **5/7 CF pairs are metric-incommensurable** — the cross-architecture comparison that justifies the paper cannot actually be made for 71% of cases.
4. **CKA reverses RSA ordering** — conclusions about representational structure are metric-dependent with no principled resolution.
5. **Token overlap ρ=1.0 with CF sensitivity** — counterfactual sensitivity tracks surface-level lexical distance, not semantic instruction understanding.
6. **N=2 for the primary finding** (exit collapse) and **N=1 at Tier-2** for the three-tier gradient.
7. **Missing related work** — neural collapse, logit lens, fine-tuning distortion, and attention pruning literatures would contextualize whether findings are VLA-novel.
8. **The paper's own evidence argues against its premise** — DINO R²=0.687 without any language/action training, combined with visual dominance literature and ΔMSE≈0, suggests instruction routing is representationally present but functionally irrelevant.

### What Would Improve This Paper
- **Closed-loop behavioral validation** connecting representational findings to task success rates (e.g., does exit collapse magnitude predict transfer performance? Does CF sensitivity correlate with instruction-following accuracy?)
- **Unified CF metric** across all architectures to enable true cross-architecture comparison
- **Domain-adaptation control** (LLM→code or LLM→math) to test whether exit collapse is VLA-specific or generic format specialization
- **Engagement with neural collapse and fine-tuning distortion literature** to contextualize exit collapse
- **Additional VLM→VLA transitions** (N>2) and intermediate-tier checkpoints (N>1) for the gradient claim
- **Actionable insight demonstration** — showing the framework discovers something non-obvious that improves VLA design

### Estimated Outcome at CoRL 2026
- Accept probability: **5–15%**
- Most likely outcome: **Reject** with encouragement to resubmit after behavioral grounding
- The paper is not a strong reject — the methodology is sound and the honesty is valued — but the findings are too thin and too disconnected from robotics practice for a top robotics venue.

---

*Review completed: 2 reviewers, full roundtable (Steps 1–4). Consensus: Reject 4/10.*


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