---
dream_id: dream_20260522T085530
tier: median
overall_score: 2.5 — Borderline Findings
timestamp: 2026-05-22T10:06:57.262048+00:00
---

# Dream Review Report — Full Roundtable

**Paper:** "Cross-Dataset Validation of Hidden-State Safety Probing: Layer Selection Bias as a Probe-Task-Modulated Property"
**Venue:** EMNLP 2026 (ARR)
**Mode:** Full (2 Reviewers, 4-step roundtable)
**Dream ID:** 20260522T085530

---

## Step 1: Independent Reviews

### Reviewer 1 (R1) — Methods and Experiments

#### 1.1 Summary
This paper extends a prior 4-model evaluation of hidden-state safety probing to AdvBench, a binary jailbreak/safe classification benchmark without step-level commitment-point labels. Across two models (R1-8B and OT-7B), the authors replicate the layer selection bias (CR-composite → shallow layers) and HS-vs-text modality advantage, but with substantially attenuated effects: the layer gap shrinks from 23 layers (72%) to 7 layers (23%), the HS precision advantage drops from +22pp to +6.5pp, and only 1 of 6 Holm–Bonferroni-corrected tests passes. The paper reframes the HS advantage as a "probe-task-modulated geometric property."

#### 1.2 Strengths
- **Comprehensive experiment coverage.** The paper covers 11 of 15 planned experiments, with the 4 omissions well-justified (cross-model transfer skipped for single-model scope, fine-grained labels and BOCPD/CUSUM inapplicable to binary setup). The coverage includes layer sweeps, 5-metric analysis, temporal ablation, bootstrap statistics, cross-model extension, Mahalanobis negative result, GRU comparison, text baseline, FPR analysis, oracle ceiling, and early detection timing.
- **Honest statistical reporting.** The paper is transparent about its weak statistical evidence: 1/6 HB passes, MDE of 12–14pp exceeding observed deltas of 3–6.5pp, and power limitations at n=33–36. The three-way decomposition of why effects attenuate (binary labels → uniform crossing-rate profile, shorter traces, mid-depth optimal layer) is mechanistically informed.
- **Useful negative results.** Mahalanobis distance failure replicates cross-dataset (Table 12, max separation 0.04), strengthening the "variance-based unsupervised detection is fundamentally inapplicable" conclusion across now 5 model-dataset combinations. GRU non-improvement (Table 13) cross-validates the linear-probes-sufficient finding.
- **Oracle ceiling analysis (Table 11).** The ~0.85 step-level ceiling under binary labels (vs ~0.95 with CP) provides a principled explanation for attenuated effects — smaller achievable deltas mean the HS-text gap compression is partially a ceiling effect, not purely a signal weakness.
- **HS-Text gap compression quantification (Table 7).** The 3.3× (bal_acc) and 5.6× (precision) compression factors, with the mechanistic explanation that binary classification makes surface patterns (keywords, refusal phrases) more competitive, is the paper's most interpretable finding.

#### 1.3 Weaknesses
- **Severely underpowered design undermines the core contribution.** With n=36 (R1-8B) and n=33 (OT-7B) test traces, the MDE at 80% power is 12–14pp. Every observed HS-text delta (3–6.5pp) falls below MDE. Only 1/6 HB passes. The paper honestly reports this, but the fundamental problem is that the experiment was designed at a scale that cannot resolve the effects it seeks to measure. This is not a limitation to note — it is a design flaw that prevents the paper from making its claimed contribution. The "directional replication" framing (all deltas favor HS) is suggestive but does not meet the evidentiary standard for a top venue.
- **Only two models, no 32B coverage.** The original study used 4 models (2 architectures, 2 scales). This replication uses only 2 models at the smaller scale. The Limitations section notes this, but the absence of 32B models — where the original study found the most interesting results (layer selection reversal masking HS advantage) — limits the cross-dataset claim's scope. The paper cannot address whether binary-label attenuation interacts with scale.
- **No figures in the entire paper.** The paper contains 14 tables and zero figures. This is a severe presentation issue. The layer selection bias pattern, the gap compression, the crossing-rate profiles, and the bootstrap distributions would all be far more accessible as figures. Key results (e.g., Table 3's 2-row comparison of original vs. AdvBench layer gaps) cry out for visual representation. The dense table-only format makes the paper difficult to parse and reduces its communicative impact.
- **No references section.** The PDF contains no bibliography/references section. This is a fatal formatting issue — EMNLP 2026 would desk-reject a submission with no references. Claims about "prior work," "concurrent works," and specific methods (TrajGuard, SafeSwitch, SIREN, MiniLM-L6) cannot be verified. If this is a PDF rendering artifact, it needs to be fixed; if references were omitted, the paper is incomplete.
- **Binary label ceiling confounds interpretation.** The paper acknowledges the ~0.85 ceiling (Table 11) but does not adequately address how this confounds the "probe-task-modulated" conclusion. If the ceiling itself is lower, smaller HS-text deltas are expected mechanically — the attenuation could reflect a ceiling effect rather than genuine task modulation of the HS advantage. The paper conflates these two explanations without disentangling them.
- **The adapted early detection metric (Table 10) is not rigorous.** The paper acknowledges this ("adapted metric is less rigorous than the original lead-time analysis and should be interpreted with caution"), but still presents it as Section 4.10 in the main text. An acknowledged-weak analysis in the main body weakens overall credibility; it belongs in an appendix at most.

#### 1.4 Questions for Authors
1. **Power analysis a priori:** Was a power analysis conducted before running the AdvBench experiments? Given the known effect sizes from the original study and the available sample sizes, could you have predicted that the study would be underpowered? If so, why was the design not adjusted (e.g., larger AdvBench sample, pooling across more models)?
2. **Ceiling disentanglement:** Can you separate the ceiling effect (~0.85 vs ~0.95) from the task-modulation effect? For instance, if you normalized the HS-text gap by the available ceiling room (gap / (ceiling - 0.5)), would the relative advantage still attenuate?
3. **Binary label noise model:** You note that early steps in jailbreak traces are labeled positive despite being "genuinely safety-aware." Have you quantified what fraction of steps are mislabeled under binary assignment? A simple analysis of probe confidence by trace position would characterize the noise floor.
4. **Why no figures?** Was this a deliberate choice or a page-budget constraint? The paper would benefit enormously from even 2-3 figures.

#### 1.5 Minor Issues
- Table 1 is referenced as "Table 1" but the reference formatting (red "[1]" in PDF) suggests a LaTeX cross-reference issue.
- Similarly, Tables 2, 4, 5, 6, 7, 8, 10, 11, 12 all show red reference markers — suggests `\ref` compilation issues.
- The Limitations section spans pages 8–9. Verify it does not push the main text beyond 8 pages (EMNLP 2026 limit).
- Page 9 contains Tables 12–13 and page 10 contains Table 14, but these seem to be appendix-level material presented in the main text body. The paper lacks appendix delineation.
- "bal_acc × CR" in Table 2 uses a code-style name rather than a properly formatted metric name.

#### 1.6 Scores
| Dimension | Score | Justification |
|-----------|-------|---------------|
| Soundness | 2.5 | Experimental coverage is broad but the core comparison is underpowered by design. 1/6 HB passes. Missing references. The "directional replication" framing is below standard for statistical evidence. |
| Excitement | 2 | The finding is essentially that effects attenuate when you weaken supervision — expected, not surprising. The gap compression quantification is mildly interesting but not actionable. |
| Reproducibility | 3 | Hyperparameters, splits, and statistical procedures are documented. However, missing references prevent verification of baseline methods. Code/data availability unclear. |
| Overall | 2.5 | Borderline Findings |
| Confidence | 4 | |

---

### Reviewer 2 (R2) — Novelty and Related Work

#### 2.1 Summary
The paper replicates a prior hidden-state safety probing study on AdvBench, finding that the core layer selection bias and HS advantage replicate directionally but with 3–5× smaller effects under binary labels. The main conceptual contribution is reframing the HS advantage as "probe-task-modulated" rather than unconditional. The paper systematically documents the attenuation across 12 subsections of experiments.

#### 2.2 Strengths
- **Addresses a genuine generality question.** The prior work's claims were based on a single (proprietary) dataset with specialized CP labels. Testing whether findings hold on a publicly available benchmark with different label structure is a natural and worthwhile follow-up.
- **Transparent about its own limitations.** The paper does not overclaim. The Discussion section explicitly states "reaching 3.5+ reviewer scores would require either larger AdvBench samples or a second binary-label dataset," showing awareness of the evidence threshold. This metacognitive transparency is unusual and commendable.
- **Mechanistic explanation for attenuation.** The three-factor explanation (Section 4.4: more uniform CR profile under binary labels, shorter traces, mid-depth optimal layer for binary discrimination) goes beyond simply reporting smaller numbers and provides interpretable reasoning.
- **Clean negative result replication.** The Mahalanobis failure (Table 12) and GRU non-improvement (Table 13) replicating cross-dataset adds genuine evidence to the conclusion that these methods are fundamentally unsuitable, not just dataset-specific failures.

#### 2.3 Weaknesses
- **Extremely low novelty — this is an incremental replication study.** The paper applies the exact same methods (LR probes, 5 layer selection metrics, bootstrap HB, Mahalanobis, GRU) from the prior work to a new dataset. No new methods, metrics, theoretical frameworks, or detection approaches are introduced. The "probe-task-modulated geometric property" is a reframing of existing results, not a new conceptual contribution. The core finding — that effects are weaker with weaker supervision — is predictable from first principles (binary labels have higher noise floor, less discriminative signal). For EMNLP 2026 main conference (~21% acceptance), the novelty threshold requires more than demonstrating that a known phenomenon attenuates under degraded conditions.
- **The results are essentially null.** Of 6 hypothesis tests, 5 fail. The bootstrap CIs for bal_acc and FPR include zero. The single passing test (R1-8B precision, p=0.014) would not survive a more conservative correction (e.g., Bonferroni at 6 tests: threshold 0.0083, and indeed in the combined analysis in Table 9, R1-8B precision at HB rank 1 has threshold 0.0083, and p=0.014 > 0.0083 — wait, the paper says it passes at rank 1/3 within R1-8B). The "directional consistency" argument (all 6 deltas favor HS) is a sign test with p = 0.016 for 6/6 positive — barely significant and ignoring effect magnitudes. A paper whose main message is "we tried to replicate and mostly failed, but the direction is right" provides limited evidence.
- **Related work is inadequate.** Section 2 contains three short paragraphs (~200 words total) that are far too thin for a research paper:
  - "Hidden-state safety monitoring" paragraph names TrajGuard, SafeSwitch, SIREN without substantive discussion of their methods, limitations, or relevance.
  - "Reasoning model safety" paragraph vaguely references "several concurrent works" without naming them.
  - "Layer selection in probing" paragraph alludes to "prior work" showing different layers encode different properties without citing specific studies (Belinkov 2022, Hewitt & Liang 2019, Tenney et al. 2019, etc.).
  - Missing entirely: probing methodology critiques (control tasks, selectivity), representation engineering (RepE, DAS), broader AI safety monitoring literature.
  - **No references section exists in the PDF** — making the Related Work section unverifiable.
- **The "probe-task-modulated" reframing is terminologically novel but conceptually thin.** The paper's contribution can be summarized as: "HS advantage is larger with better labels." This is expected from any supervised learning perspective — better labels produce better-separated classes, benefiting the higher-capacity representation (HS) more. Calling this "probe-task-modulated" adds terminology but not insight. The paper does not provide a formal definition, testable predictions, or a theoretical framework for when modulation will be strong vs. weak.
- **AdvBench is a weak test of generality.** AdvBench uses binary trace-level labels (fundamentally different supervision), shorter traces (~38 vs ~46), and a different target ("is response harmful?" vs. "when does model commit?"). The paper acknowledges these differences create a "natural contrast" but this means AdvBench tests a substantially different task, not just the same task on different data. Showing that the HS advantage is smaller on a different and easier task is not compelling evidence about generality — it's evidence about task difficulty. A true generality test would use a second CP-annotated dataset, which the paper notes would be ideal but does not provide.
- **No contribution beyond the prior work's scope.** The paper's value is entirely parasitic on the prior work — it validates some findings, fails to validate others, and provides no independent contributions. The prior work already identified the layer selection bias, the HS advantage, the temporal improvement, the Mahalanobis failure, and the GRU non-improvement. This paper confirms "same direction, smaller magnitude" for each. The deployment implication ("match modality to detection granularity") is one sentence of practical wisdom that does not require 10 pages to derive.

#### 2.4 Questions for Authors
1. **What is the independent contribution?** If removed from the context of the prior work, what does this paper teach us? Can you state a finding that a reader could not predict from knowing (a) the original results and (b) that binary labels have higher noise?
2. **Why not use a second CP-annotated dataset?** You frame the work as testing "generality across datasets" but test on a fundamentally different task (binary classification). Would annotating CP labels on even a subset of AdvBench provide a stronger generality test?
3. **How does "probe-task-modulated" differ from "label-quality-dependent"?** The attenuation appears to track label quality (CP > binary). Is there a scenario where the task changes but label quality is held constant, which would distinguish task modulation from label modulation?
4. **Missing references:** Can you confirm whether the PDF's lack of a references section is a rendering artifact or an actual omission? If the latter, this would be a desk-reject condition.

#### 2.5 Minor Issues
- The title is 15 words and somewhat unwieldy. Consider whether "Probe-Task-Modulated" in the subtitle earns its place given that the paper provides limited formal development of this concept.
- Section 4 has 12 subsections (4.1–4.12), which is excessive fragmentation. Several subsections (4.10 Early Detection, 4.11 Oracle Ceiling, 4.12 Negative Results) present appendix-grade material in the main text.
- The paper reads as a technical report or extended abstract of a replication study rather than a self-standing research contribution.
- "Anonymous" author block is correct for ARR but the writing style suggests strong familiarity with the prior work — if the authors are the same group, the paper should be framed as a follow-up, not a third-party replication.

#### 2.6 Scores
| Dimension | Score | Justification |
|-----------|-------|---------------|
| Soundness | 3 | The experiments are properly executed and honestly reported. Statistical procedures are appropriate. Deductions for underpowered design and missing references. |
| Excitement | 1.5 | Minimal novelty — a replication study with predictable attenuation, no new methods, and essentially null results. The "probe-task-modulated" reframing is terminological, not conceptual. |
| Reproducibility | 2.5 | Methods are described but missing references prevent baseline verification. Data is from a public benchmark (AdvBench) which helps, but the original dataset's CP annotations are proprietary. |
| Overall | 2 | Resubmit next cycle |
| Confidence | 4 | |

---

## Step 2: Cross-Sharing

### R1 → R2 observations:
R1 notes that R2's excitement concern (1.5) is well-founded — the paper's contribution is incremental. R1 agrees that the "probe-task-modulated" framing lacks formal development. However, R1 gives partial credit for the gap compression quantification (Table 7) and the mechanistic three-factor explanation (Section 4.4), which go slightly beyond "effects attenuate with worse labels."

### R2 → R1 observations:
R2 agrees with R1's identification of the underpowered design as a fundamental flaw, not just a limitation. R2 further notes that R1's soundness score (2.5) may be too generous given the missing references section — without a bibliography, the paper cannot be evaluated as a complete submission. R2 reinforces that the 14-table, 0-figure format is problematic for readability.

### Shared concerns:
1. **Missing references section** — both reviewers flag this as potentially fatal.
2. **Underpowered design** — both agree 1/6 HB passes is insufficient evidence.
3. **Low novelty** — both agree no new methods or frameworks.
4. **No figures** — both note the paper is hard to read.
5. **Adapted metrics are weak** — the early detection timing metric is acknowledged as less rigorous.

---

## Step 3: Convergence

### Points of agreement:
- **Overall assessment range: 2.0–2.5.** R1 at 2.5 (Borderline Findings), R2 at 2.0 (Resubmit next cycle). After discussion, both converge toward **2.5** — the honest reporting and comprehensive experiment coverage save it from "resubmit," but the null results, low novelty, and missing references prevent Findings acceptance.
- **Soundness: 2.5–3.** The experiments are correctly executed but underpowered by design. Missing references reduce soundness. Converge at **3**.
- **Excitement: 1.5–2.** Low novelty, predictable findings, no new methods. Converge at **2**.
- **Reproducibility: 2.5–3.** Methods documented but references missing and original CP data proprietary. Converge at **3**.

### Points of disagreement (resolved):
- R1 initially gave more credit for the mechanistic explanation; R2 argued this is post-hoc rationalization of expected attenuation. **Resolution:** The three-factor explanation (Section 4.4) is informative but not novel — it describes why binary labels produce weaker supervision, which is known. Partial credit retained.
- R2 initially scored overall at 2.0; R1 argued the honest power analysis and comprehensive coverage merit Borderline Findings rather than Resubmit. **Resolution:** The paper's transparency is valued but cannot compensate for the fundamental issue that 1/6 HB passes is insufficient evidence. The missing references further weigh against. **Converge at 2.5.**

---

## Step 4: Consolidated Assessment

### Final Scores
| Dimension | Score |
|-----------|-------|
| **Soundness** | 3 |
| **Excitement** | 2 |
| **Reproducibility** | 3 |
| **Overall Assessment** | **2.5 — Borderline Findings** |
| **Confidence** | 4 |

### Recommendation
**Borderline Findings (2.5).** The paper is below the threshold for Findings acceptance in its current form, primarily due to (1) insufficient statistical evidence (1/6 HB passes), (2) low novelty (incremental replication with predictable attenuation), and (3) a critical formatting issue (missing references section). With revisions, it could potentially reach Findings level.

### Key Strengths (Consolidated)
1. **Comprehensive experiment coverage.** 11 of 15 planned experiments executed, with well-justified omissions. The breadth of analyses (layer sweep, 5-metric comparison, temporal ablation, bootstrap, cross-model, Mahalanobis, GRU, text baseline, FPR, oracle ceiling, early detection) is thorough.
2. **Honest statistical reporting.** The paper is transparent about its weak evidence: 1/6 HB passes, MDE exceeding observed deltas, and power limitations. The Discussion section explicitly states what evidence would be needed for stronger conclusions.
3. **HS-Text gap compression quantification (Table 7).** The 3.3–5.6× compression factors are the paper's most concrete finding, with a mechanistic explanation connecting binary labels to increased text-probe competitiveness via surface-pattern discriminability.
4. **Clean negative result replications.** Mahalanobis failure (Table 12) and GRU non-improvement (Table 13) replicating cross-dataset adds genuine cross-dataset evidence for these specific conclusions.
5. **Oracle ceiling analysis (Table 11).** The ~0.85 ceiling under binary labels provides a principled constraint on achievable HS-text deltas.

### Key Weaknesses (Consolidated)
1. **Missing references section — potential desk-reject.** The PDF contains no bibliography. This prevents verification of cited methods, violates submission formatting requirements, and would trigger desk rejection at EMNLP 2026.
2. **Severely underpowered design.** With n=33–36 test traces and MDE of 12–14pp, the study cannot resolve the observed 3–6.5pp deltas. Only 1/6 HB passes. The "directional consistency" framing (all deltas favor HS) is suggestive but does not meet the evidentiary standard for a peer-reviewed venue. This is a design-level issue, not just a limitation.
3. **Low novelty.** No new methods, metrics, theoretical frameworks, or detection approaches. The same pipeline from prior work is applied to a new dataset. The "probe-task-modulated geometric property" is a terminological contribution without formal definition, testable predictions, or theoretical grounding. The core finding — effects weaken with weaker supervision — is predictable.
4. **No figures in the entire paper.** 14 tables and 0 figures make the paper exceptionally difficult to parse. The layer selection bias, gap compression, and bootstrap distributions all need visual representation. This severely impacts readability and accessibility.
5. **Only 2 models, no 32B scale.** The prior work's most interesting findings (scale-dependent layer selection reversal) cannot be tested. The replication covers only the easier scale (7–8B) where original effects were already strong.
6. **AdvBench tests a different task, not just different data.** Binary jailbreak/safe classification ("is the response harmful?") is fundamentally different from commitment-point detection ("when does the model commit?"). Showing attenuation on a different and easier task does not straightforwardly test the generality of findings on the original task. The paper partially conflates task difficulty with task modulation.

### Actionable Revision Suggestions
1. **Fix the references section** — this is a prerequisite for any submission.
2. **Add 3–4 figures:** (a) 5-metric layer profile comparison (original vs AdvBench), (b) bootstrap delta distributions or forest plot, (c) HS-Text gap compression bar chart, (d) crossing-rate vs depth overlay.
3. **Increase sample size or scope.** Either collect more AdvBench traces to bring MDE below observed deltas (~6pp), or add a second binary-label dataset, or extend to 32B models.
4. **Move peripheral analyses to appendix.** Sections 4.10 (Early Detection), 4.11 (Oracle Ceiling), and 4.12 (Negative Results — Mahalanobis/GRU/FPR) are supplementary. Moving them to an appendix would free space for figures and deeper analysis of the core 5-metric and bootstrap results.
5. **Formalize "probe-task-modulated."** Define it precisely, state testable predictions (e.g., "the HS advantage should scale monotonically with label granularity"), and distinguish it from "label-quality-dependent."
6. **Disentangle ceiling effects from task modulation.** Normalize HS-text deltas by available ceiling room to test whether the attenuation exceeds what the ceiling alone predicts.


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