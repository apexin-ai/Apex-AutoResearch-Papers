---
dream_id: dream_20260522T023801
tier: worst
overall_score: Weak Reject (4/10)
timestamp: 2026-05-22T03:37:27.537441+00:00
---

# Dream Review Report — Full Review

**Paper:** "Architecture-Dependent Cross-Lingual Conflict Processing: Probing Knowledge Conflict Signals in Multilingual LLMs"
**Target Venue:** ICLR 2026
**Rating Scale:** {0, 2, 4, 6, 8, 10}
**Review Mode:** Full (2 Reviewers, 4-Step Roundtable)

---

## Reviewer Panel

| Reviewer | Focus | Soundness | Presentation | Contribution | Overall | Confidence |
|----------|-------|-----------|-------------|-------------|---------|------------|
| R1 | Methods + Experiments | 2/4 | 3/4 | 2/4 | 4/10 | 4/5 |
| R2 | Novelty + Related Work | 2/4 | 3/4 | 1/4 | 4/10 | 4/5 |
| **Consensus** | | **2/4** | **3/4** | **1.5/4** | **4/10** | **4/5** |

**Overall Assessment: Weak Reject (4/10)**

---

## Step 1: Independent Reviews

### Reviewer 1 — Methods and Experiments

#### Summary
The paper probes residual stream activations in three multilingual LLMs (Llama-3.1-8B, Qwen3-8B, Gemma-2-9B) using EN-ZH ConflictQA instances. It claims conflict signals are robustly detectable (C1: 68-77% within-language), directional asymmetry is architecture-dependent (C2: ~7pp in Llama/Qwen, ~0 in Gemma), and CKA analysis reveals layer structure (C3). Steering experiments yield very weak results (≤8% flip rates). Tracks 2-3 (SAE analysis, causal steering) are entirely absent.

#### Strengths
- Well-structured hypothesis-driven design (H1 vs H2 with falsifiable predictions)
- Thorough confound exclusion: COMET tercile ablation shows reversed direction (high-COMET → lower accuracy), ruling out translation quality as confound; token overlap Jaccard (3-4%) rules out shared-vocabulary artifacts
- Permutation testing (n=1000, all p<0.001) is appropriate for within-language detection
- Label noise ablation (~3.3pp per 5% noise) provides useful calibration of pipeline robustness
- Admirably candid limitations section acknowledging absent Tracks 2-3, weak steering, 8% label noise
- Multi-architecture replication across three model families with different designs

#### Weaknesses

**W1 (Major). C2 (directional asymmetry) is supported by only 1/3 models.** Table 1 shows Llama significant (+7.2pp, CI [1.1, 13.6]), Qwen non-significant (+7.2pp, CI [-1.2, 13.4]), Gemma null (+1.0pp, CI [-4.5, 6.8]). Framing this as "architecture-dependent asymmetry" is post-hoc rationalization of a failed replication. The paper should either provide a mechanistic explanation for Gemma's divergence or downgrade C2 to "inconsistent across architectures."

**W2 (Major). Steering results are essentially null.** Flip rates of 3-8% (Table 8) are barely above what random perturbations would produce. No random-direction control is reported. Without this baseline, the steering experiment cannot establish that the probe direction is causally relevant.

**W3 (Major). Bootstrap n=100 is inadequate.** At n=100, the 95% CI endpoints correspond to the 2nd-3rd most extreme bootstrap values — highly unstable. Qwen's CI of [-1.2, 13.4] could easily shift to exclude or include zero with a different seed. The conventional minimum is n≥1000 (Efron & Tibshirani, 1993). This is computationally trivial for logistic regression.

**W4 (Major). Missing non-conflict control.** The ZH→EN > EN→ZH asymmetry could be a general property of cross-lingual probing in English-dominant models. English representations have more training data, so probes trained on any English feature may transfer better FROM other languages TO English. Probing a non-conflict binary semantic feature (entity type, sentiment) with identical methodology would establish conflict-specificity. Its absence leaves the asymmetry interpretation fundamentally ambiguous.

**W5 (Moderate). CKA "correlation" on 3 data points (Table 6) is statistically meaningless.** Any 3 non-collinear points yield |r| > 0.5 roughly 50% of the time by chance. The paper should report raw values without computing a correlation.

**W6 (Moderate). COMET scores are low (mean 0.68-0.70, only 12-18.5% pass 0.80).** While the tercile ablation argues quality is not a confound, the mediocre translations raise concerns about label preservation. The verification step partially addresses this, but how many samples fail verification and whether they differ systematically is unreported.

**W7 (Moderate). Single language pair (EN-ZH).** Cannot distinguish H1 (universal English anchoring) from ZH-specific phenomena.

**W8 (Moderate). Probe accuracy ceiling (68-77%) unexplained.** Prior monolingual conflict probing achieves ~90%+. The 23-32% undetectable fraction is large and unexplored — is it due to cross-lingual setting, label errors, or inherently weaker signal?

**W9 (Minor). MLP vs linear comparison lacks overfitting diagnostic.** A 2-layer MLP (hidden 256, ~1M parameters) trained on ~1000 samples with ~4000 features risks overfitting. Training accuracy alongside test accuracy is not reported.

**W10 (Minor). Inconsistent label noise estimates.** Section 6 states ~8% label error, but the safety margin discussion implies <5%. These should be reconciled.

#### Questions for Authors (R1)
1. Have you tested the asymmetry direction on a non-conflict binary classification task using identical methodology?
2. Why was bootstrap n set to 100 rather than ≥1000?
3. What is the random-direction baseline flip rate for steering?
4. For Gemma's +1.0pp: do you have a principled mechanistic explanation?
5. How many samples fail verification, and do they differ systematically?
6. What is the class balance (conflict vs non-conflict) in test sets?
7. What are MLP training accuracies?

#### Missing Experiments (R1)
- **Non-conflict semantic baseline** (Critical) — probe entity type or sentiment with same pipeline
- **Random-direction steering control** (Critical)
- **Bootstrap n≥2000** (High priority, trivial cost)
- **Non-CJK language pair** (High priority)
- **MLP overfitting diagnostic** (Medium)
- **Characterization of undetectable fraction** (Medium)

---

### Reviewer 2 — Novelty and Related Work

#### Summary
The paper applies standard residual-stream probing to cross-lingual conflict detection across three architectures. Its central claim — that transfer asymmetry is "architecture-dependent" — rests on an N=3 sample with 1 significant, 1 borderline, and 1 null result. The methodology is not novel; the contribution is positioned as "empirical characterization + methodology" after the originally planned mechanistic contributions (SAE, causal steering) were not completed.

#### Strengths
- Well-defined H1 vs H2 hypothesis framework with falsifiable predictions
- Rigorous confound exclusion (COMET tercile ablation, token overlap analysis)
- Honest reporting of negative/null results throughout
- Multi-architecture replication finding both consistent (C1) and divergent (C2) results
- Appropriate statistical methodology (permutation tests, bootstrap CIs)

#### Weaknesses

**W1 (Major). "Architecture-dependent" finding is severely underpowered (N=3).** Only 1/3 models reaches significance. The framing converts an inconsistent result into a finding without proposing a mechanism for why Gemma differs.

**W2 (Major). Standard methodology applied to new domain, limited methodological novelty.** Logistic regression probing has been standard since Belinkov (2022) and Hewitt & Manning (2019). No methodological innovation is introduced. The 68-77% balanced accuracy is substantially below what recent work achieves for monolingual conflict probing (~90%+ F1), making the cross-lingual results (63-72%) modest.

**W3 (Major). Tracks 2-3 absence removes planned mechanistic contributions.** Without SAE feature decomposition or successful causal intervention, the paper cannot distinguish between (a) conflict signals genuinely encoded in the residual stream and (b) statistical artifacts of input features propagating through layers. The steering results (≤8%) are too weak for causal evidence.

**W4 (Major). Missing critical related work:**
- Zhao et al. (2024/2025) "Analysing the Residual Stream of Language Models Under Knowledge Conflicts" — direct monolingual precursor achieving ~90% accuracy with same methodology. The submitted paper's 68-77% must be contextualized against this ceiling.
- Zhao et al. (2025) SpARE (NAACL 2025 Oral) — most relevant work on SAE-based conflict steering, which Track 3 was supposed to extend.
- Boer et al. (2026) "Probing for Knowledge Attribution in LLMs" — 0.96 F1 for monolingual conflict probing.
- Wang et al. (2025) "Lost in Multilinguality" (ACL 2025) — directly relevant to CKA analysis.
- Pham et al. (2026) "Where Knowledge Collides" — mechanistic study using activation patching.
- Kialy et al. (2026) "A Universal Vibe?" — first cross-lingual SAE feature discovery.

**W5 (Major). CLEAR connection is superficial (Section 5).** The paper claims "mechanistic grounding" but the connection is purely correlational and arguably circular: "ZH→EN transfer stronger → consistent with English-anchored representations → explains linguistic affinity." A genuine mechanistic account requires showing probe directions causally influence conflict resolution, which the weak steering fails to demonstrate.

**W6 (Moderate). CKA analysis (C3) replicates known findings.** Monotonic CKA decrease across layers and language-specific information in later layers have been established by Wendler et al. (2024), Wang et al. (2025), and Libovický et al. (2020). The added observation that probe peaks occur after the transition point is descriptive only with N=3.

**W7 (Moderate). Single language pair limits generalizability severely.** Cannot distinguish "English-anchored" (H1) from "dominant-language-anchored" or from CJK-specific phenomena. Interestingly, Qwen has substantially more Chinese training data than Llama yet shows near-identical asymmetry — this is unexplored.

#### Questions for Authors (R2)
1. How do you reconcile "architecture-dependent asymmetry" with Gemma's result directly contradicting the Llama/Qwen pattern?
2. How does your 68-77% accuracy compare to Zhao et al.'s ~90% on monolingual conflict probing? What explains the gap?
3. If the detected signal is a genuine "conflict signal" used for resolution, why does steering produce ≤8% flip rates?
4. Have you considered whether Gemma's attention architecture (multi-query) vs Llama/Qwen (grouped-query) explains the asymmetry collapse?
5. Does the noise-corrected accuracy (~74.5%) change your significance conclusions?

#### Assessment of Novelty and Positioning
The novelty is limited. The core methodology is standard linear probing applied to a new domain. The empirical findings are modest: C1 (detectability) is expected given monolingual baselines; C2 (asymmetry) is undermined by N=3 with 1 significant; C3 (CKA) replicates known findings. The paper's positioning as mechanistic grounding for CLEAR is overclaimed — probing demonstrates information *presence*, not *usage*. Compared to direct competitors (SpARE's effective SAE steering, Boer et al.'s 0.96 F1, Pham et al.'s activation patching), this paper's contribution appears incremental. The incomplete Tracks 2-3 represent the most novel planned contributions; their absence leaves the paper as a probing study without sufficient depth for ICLR.

---

## Step 2: Cross-Sharing — Unique Contributions from Each Reviewer

**R1 contributions not in R2:**
- Non-conflict control baseline as the single most critical missing experiment (W4)
- MLP overfitting diagnostic concern (W9)
- CKA correlation on 3 points is statistically invalid (W5)
- Inconsistent label noise estimates between sections (W10)
- Translation circularity risk if target models are used for translation

**R2 contributions not in R1:**
- Six specific missing references that directly compete with or contextualize this work
- Monolingual probing accuracy ceiling (~90%) contextualizing the 68-77% result
- Deeper novelty assessment: standard method in new domain
- Qwen's near-identical asymmetry despite more Chinese data is unexplored
- The "architecture-dependent" framing as post-hoc narrative on N=3

---

## Step 3: Convergence — Areas of Agreement and Disagreement

### Full Agreement (Both Reviewers)
1. **C2 (asymmetry) is the paper's weakest claim** — 1/3 significant, no mechanism for Gemma divergence
2. **Steering is essentially null** — ≤8% flip rates provide no causal evidence, missing random-direction control
3. **Track 2/3 absence is a major gap** — removes mechanistic and causal contributions
4. **Bootstrap n=100 is inadequate** — computationally trivial to fix
5. **Single language pair is a significant limitation**
6. **Presentation is above average** — clear structure, honest limitations, readable tables
7. **Confound exclusion is well-executed** — COMET ablation and token overlap controls are good methodology
8. **Overall: 4/10 (Weak Reject)**

### Partial Disagreement
- **Contribution score:** R1 gives 2/4 (confound-exclusion methodology has value), R2 gives 1/4 (standard method, modest results, missing references make contribution incremental). **Resolution:** The methodology for confound exclusion is a genuine contribution, but it is insufficient to carry the paper without stronger findings. **Consensus: 1.5/4**, closer to R2's assessment given the ICLR bar.

### Key Convergent Criticism
Both reviewers independently identify the same fundamental problem: **the paper's central novel claim (architecture-dependent asymmetry) is a post-hoc interpretation of inconsistent results across an underpowered sample (N=3), without a mechanistic explanation for the divergence, and without the critical non-conflict control that would establish conflict-specificity.** The supporting evidence (steering, CKA) is either null or descriptive. The most novel planned contributions (SAE, causal steering) are absent.

---

## Step 4: Consolidated Assessment

### Paper Strengths (Consensus)
1. **Robust confound exclusion methodology.** The COMET tercile ablation and token overlap analysis are model practices for cross-lingual probing studies. Future work in this area should adopt these controls.
2. **C1 (detectability) is well-supported.** Within-language probe accuracy 68-77% across three architectures, all p<0.001, with cross-lingual transfer exceeding chance (63-72%). This is a genuine, if unsurprising, finding.
3. **Transparent reporting.** The limitations section is unusually honest about incomplete experiments, weak steering, and label noise. This builds credibility.
4. **Clear writing and structure.** The H1/H2 framework, well-formatted tables, and logical flow make the paper accessible.

### Paper Weaknesses (Consensus, Priority-Ordered)

1. **[Critical] No non-conflict control baseline.** Without probing a non-conflict semantic feature using identical methodology, the paper cannot establish that the observed asymmetry (ZH→EN > EN→ZH) is conflict-specific rather than a general property of cross-lingual transfer in English-dominant models. This is the single most important missing experiment.

2. **[Critical] C2 (asymmetry) underpowered and post-hoc.** N=3 architectures with 1 significant, 1 non-significant, 1 null. The "architecture-dependent" framing is a narrative imposed after results, not a pre-registered hypothesis with mechanistic backing. No explanation is provided for why Gemma specifically should differ.

3. **[Critical] Tracks 2-3 (SAE + causal steering) entirely absent.** The paper cannot move beyond "conflict signals are present" to "what they are" or "whether they matter." The steering experiment (≤8% flip rates, no random control) is too weak for any causal claim.

4. **[Major] Missing critical related work.** At least 4-6 directly relevant papers are absent, including the monolingual probing precedent (~90% accuracy), SpARE (SAE-based conflict steering), and recent cross-lingual mechanistic work. The paper cannot be properly evaluated without positioning against these.

5. **[Major] Bootstrap n=100 is below accepted standards.** CI boundaries are unstable; Qwen's significance conclusion could change with a different seed. Trivially fixable.

6. **[Moderate] CKA analysis (C3) is descriptive, not novel.** Monotonic CKA decrease across layers is well-established. The probe-peak-after-transition observation on N=3 cannot support statistical claims.

7. **[Moderate] Single language pair (EN-ZH).** Cannot test typological distance hypotheses or distinguish H1 from H2. The EN-JA extension was planned but not completed.

### Experiment Coverage Assessment

| Planned Experiment | Status | Impact on Claims |
|---|---|---|
| Cross-lingual probing (3 models) | ✅ Complete | Supports C1, weakly supports C2 |
| COMET quality ablation | ✅ Complete | Excludes translation confound |
| CKA layer analysis | ✅ Complete | Descriptive C3 observation |
| MLP vs linear probes | ✅ Complete | Mild support for non-linear components |
| Label noise ablation | ✅ Complete | Calibrates pipeline robustness |
| Representation steering | ✅ Complete but null | Fails to provide causal evidence |
| Token overlap control | ✅ Complete | Excludes shared-token confound |
| PCA visualization | ✅ Complete | Descriptive, relegated to appendix |
| EN↔JA extension | ❌ 15% complete | Cannot test typological hypotheses |
| SAE feature identification | ❌ Not started | C5 unsupported, no mechanistic decomposition |
| LangFIR disentangling | ❌ Not started | Cannot separate language from conflict features |
| SAE Jaccard analysis | ❌ Not started | Cannot test H1 vs H2 at feature level |
| SAE-based steering | ❌ Not started | No causal evidence from Track 3 |
| Larger dataset | ❌ Not started | Limited statistical power |
| Non-conflict control baseline | ❌ Not conducted | Cannot establish conflict-specificity of asymmetry |

**Coverage: 8/15 experiments complete; 3 critical experiments missing (non-conflict control, SAE decomposition, effective steering)**

### Scores (Consensus)

| Dimension | Score | Justification |
|---|---|---|
| Soundness | 2/4 | Probing framework correct but central claim (C2) underpowered (1/3 significant), missing non-conflict control, bootstrap n=100 inadequate, CKA on N=3 invalid, steering null |
| Presentation | 3/4 | Clear writing, honest limitations, good table design. Deductions: "architecture-dependent" framing of inconsistent results, missing references |
| Contribution | 1.5/4 | C1 (detectability) is genuine but expected; C2 (asymmetry) undermined; confound-exclusion methodology is useful but insufficient alone; standard probing in new domain without mechanistic depth |
| **Overall** | **4/10** | **Weak Reject** |
| Confidence | 4/5 | Both reviewers confident in assessment |

### Recommendation

**Weak Reject.** The paper asks a genuinely interesting question and demonstrates methodological care in confound exclusion, but the gap between what the paper frames (mechanistic grounding for CLEAR, architecture-dependent asymmetry) and what it delivers (one significant probing result out of three, null steering, absent mechanistic decomposition) is too large for ICLR acceptance. The most impactful improvements would be: (1) adding a non-conflict control baseline, (2) increasing bootstrap to n≥2000, (3) completing SAE analysis for at least one model, and (4) adding the missing related work. With these additions, the paper could be competitive at ACL/EMNLP where empirical characterization papers face a somewhat lower novelty bar, provided the asymmetry result is reframed more cautiously.

### Actionable Revision Priorities

1. **Non-conflict probing baseline** — probe entity type or sentiment with identical pipeline to establish conflict-specificity. If asymmetry persists for non-conflict features, reframe the entire paper.
2. **Bootstrap n≥2000** — trivial fix that stabilizes all CI conclusions.
3. **Random-direction steering control** — report flip rates for random vectors of matching norm. If probe direction doesn't outperform random, remove Section 4.7 entirely.
4. **Add missing references and contextualize** — especially monolingual probing baselines (~90%) and SpARE. Explain the accuracy gap.
5. **SAE analysis on at least one model** — even partial Track 2 results would substantially strengthen the contribution.
6. **EN-JA or EN-DE extension** — one additional language pair would transform the asymmetry claim from N=3 to a testable typological hypothesis.
7. **Reframe C2 cautiously** — "inconsistent asymmetry across architectures" rather than "architecture-dependent," unless a mechanism is proposed.


---

引用验证失败: 目录不存在: /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/paper