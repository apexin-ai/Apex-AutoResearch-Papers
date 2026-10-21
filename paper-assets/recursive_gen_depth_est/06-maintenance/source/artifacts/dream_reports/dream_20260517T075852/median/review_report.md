---
dream_id: dream_20260517T075852
tier: median
overall_score: 3.0 - Findings acceptance / borderline reject
timestamp: 2026-05-17T08:58:07.358356+00:00
---

# Dream Review Report: "How Deep Is This Text? Ordinal Depth Estimation for Recursively Generated Content"

**Venue**: EMNLP 2026 Main
**Review Mode**: Full (2 Reviewers + Roundtable)
**Dream ID**: 20260517T075852

---

## Converged Scores

| Dimension | R1 (Methods+Exp) | R2 (Novelty+RW) | Converged |
|-----------|:-:|:-:|:-:|
| Soundness | 3.0 | 3.5 | 3.0 |
| Excitement | 3.5 | 3.0 | 3.0 |
| Overall | 3.0 | 3.0 | **3.0** (Findings accept / borderline reject) |
| Confidence | 4 | 4 | 4 |

**Headline**: Borderline. Well-motivated new task with thorough controlled experiments, but technical novelty of the classifier pipeline is limited, key baselines against existing detectors are missing, and the gap between controlled and realistic settings undermines practical claims. Findings-track viable; Main conference acceptance unlikely without revisions.

---

## 1. Paper Summary

The paper formalizes *ordinal generation depth estimation* as a new task: given text alone, predict how many recursive fine-tuning cycles it has undergone (depth 0-3). Using 19 reference-model perplexity features and Random Forest classifiers, the authors build a 3-model x 3-strategy benchmark at 1-1.5B scale (70-85% four-class accuracy), validate signal persistence at 14B (67%, ~13pp attenuation) and under prompted generation (67%, 80% retention), and construct a Depth Degradation Atlas documenting universal depth markers, non-uniform inter-depth distances, scale-dependent EDD, and strategy-dependent feature trajectory reversals. A cross-strategy two-stage pipeline validates the decomposition principle (oracle 78.4% ≈ within-strategy 78.2%) but identifies strategy classification (57.5%) as the practical bottleneck, with naive pooling (72.0%) as a strong zero-cost baseline.

---

## 2. Reviewer 1 (R1): Methods + Experiments

### Strengths
1. **Novel, well-defined task**: Ordinal depth estimation is a genuinely new problem formulation that fills a real gap between binary detection and model collapse characterization.
2. **Systematic benchmark**: The 3-model x 3-strategy x 4-depth grid is comprehensive at the 1B scale, and the paper honestly reports both successes and limitations.
3. **Useful concepts**: The EDD metric is cleanly formalized and the oracle-vs-within decomposition (78.4% ≈ 78.2%) is an elegant validation of the two-stage principle.
4. **Honest negative results**: The DCOL failure (Section 5.5) and the two-stage pipeline underperforming naive pooling are reported transparently, increasing credibility.
5. **Multiple robustness axes**: Scale (14B), generation mode (prompted), and cross-strategy transfer are all examined.

### Weaknesses
1. **(Major) Incomplete statistical reporting**: The core 1B benchmark (Table 1) lacks confidence intervals and no significance tests appear for systematic cross-condition comparisons. The 14B and prompted experiments do report CIs, creating an inconsistency. For a paper making quantitative claims about ~13pp attenuation and 80% retention, bootstrap tests or at minimum CIs on all main results are expected.
2. **(Major) No fine-tuning sensitivity analysis**: The entire depth signal is produced by LoRA fine-tuning with one configuration (r=16, alpha=32, lr=2e-4, 3 epochs). The paper includes a LoRA rank ablation (r=4 to 64, 4.65pp spread) and cross-seed replication (delta=1.05pp), which partially addresses this. However, the interaction between learning rate, epoch count, and depth signal magnitude remains unexplored. If a different fine-tuning recipe produces substantially different depth signals, the benchmark's generality is in question.
3. **(Major) Scale validation is thin**: The 14B experiment uses one model (Qwen2.5-14B) under one strategy (nucleus). "Scale-dependent attenuation" as a general claim requires more than one data point. The paper mentions preliminary 7B results with acknowledged confounds, but these are insufficient.
4. **(Minor) Single reference model**: All features depend on Pythia-410M. While the paper mentions an appendix ablation, the main text does not discuss sensitivity to reference model choice.
5. **(Minor) Narrow prompted generation evaluation**: 10 topic prompts on 1 model (GPT-2 XL) is a limited test of ecological validity. Prompt diversity, length, and style could all affect the 80% retention figure.
6. **(Minor) Cross-strategy d1-d3 accuracy is near-chance**: Excluding the trivially separable d0, d1-d3 cross-strategy accuracy drops to ~45.9%, barely above 33% chance. This is underemphasized relative to the practical deployment framing.

### Questions for Authors
1. Can you provide bootstrap CIs for all entries in Table 1?
2. What happens to depth estimation accuracy when LoRA learning rate or epoch count is varied by 2x?
3. Have you tried Pythia-160M or GPT-2 Small as alternative reference models?
4. For the prompted experiment, what is the variance across the 10 topic prompts?

---

## 3. Reviewer 2 (R2): Novelty + Related Work

### Strengths
1. **Task formalization is the core contribution**: Moving from "is this text AI-generated?" to "how many recursive generations deep is this text?" is a meaningful conceptual advance with clear practical motivation for data curation.
2. **Strategy-dependent trajectory reversal is genuinely surprising**: The finding that temperature sampling reverses the d1-d2 feature boundary (AUC as low as 0.13) is non-obvious and has real implications for detector deployment.
3. **Well-calibrated claims**: The paper does not overclaim. "Signal persists with attenuation" is more honest and informative than "robust across scales." The limitations section is thorough.
4. **Clean paper structure**: The narrative flows logically from task definition through atlas construction to robustness validation and deployment analysis.

### Weaknesses
1. **(Major) No comparison with existing detectors repurposed for ordinal estimation**: The paper positions against Binoculars and Fast-DetectGPT in the introduction but never tests whether their confidence scores, when recalibrated into ordinal bins, can estimate depth. This is the most critical missing experiment. Without it, the paper cannot establish that the task genuinely requires new methods rather than trivial recalibration of existing ones. Even a negative result (showing existing detectors fail at ordinal estimation) would strengthen the paper substantially.
2. **(Major) The Depth Degradation Atlas overpromises**: The name suggests a systematic theoretical framework, but the actual content is a collection of empirical observations (universal features, non-uniform distances, EDD, trajectory reversal) without unifying theory. Each observation is valuable individually, but packaging them as an "Atlas" implies more conceptual coherence than is delivered.
3. **(Major) Gap between controlled and realistic settings**: Real-world recursive contamination involves pretraining on mixed corpora at unknown proportions, not sequential LoRA fine-tuning on pure depth-k data. The 20-22% false positive rate on web-crawl data (mentioned in Limitations) and the cross-strategy fragility (59.1% LOO) suggest the controlled results may not transfer. The paper acknowledges this but the abstract and introduction frame the method as more broadly applicable than the evidence supports.
4. **(Minor) Related Work is thin**: 22 references is light for EMNLP. Missing: DetectGPT (Mitchell et al., 2023) is cited but DNA-GPT, RADAR, and other recent detection methods are absent. Model collapse mitigation work (e.g., Gerstgrasser et al.'s data mixing strategies) is mentioned but not discussed in depth. The Related Work reads more as a citation list than a positioning argument.
5. **(Minor) Zero figures in the paper**: The paper references figure environments but no actual figures appear in the PDF. For a paper whose core contribution is a "Depth Degradation Atlas," visual presentation is critical. Heatmaps, feature trajectory plots, and AUC decay curves would substantially improve comprehension and impact. (R1 notes this may be a compilation artifact, but the submitted PDF lacks them.)
6. **(Minor) Technical novelty of the pipeline is limited**: RF on 19 hand-crafted perplexity features is a straightforward approach. The features themselves (mean/std/percentiles of perplexity and surprisal) are standard statistical summaries. The contribution is in the task definition and empirical findings, not in methodological innovation.

### Questions for Authors
1. What happens when you threshold Binoculars or Fast-DetectGPT scores into 4 ordinal bins? Even a simple experiment would clarify whether existing detectors already solve the task.
2. Can you provide a theoretical or intuitive argument for why the Atlas observations should be expected to hold beyond LoRA fine-tuning on small models?
3. The 20% FPR on web-crawl data: does this mean 1 in 5 human-written web texts would be classified as depth-1+? How does this affect the practical data curation application?
4. Why are there no figures in the submitted PDF?

---

## 4. Roundtable Discussion Summary

### Points of Convergence
- **Both reviewers agree on Overall 3.0**: The paper defines a well-motivated new task and executes thorough experiments within a controlled scope, but falls short of Main conference acceptance due to limited technical novelty, missing baselines, and insufficient evidence for generalization beyond the controlled setting.
- **Missing existing-detector comparison is the single most actionable gap**: Both reviewers agree this is the highest-priority revision. Even showing existing detectors fail at ordinal estimation would substantially strengthen the contribution.
- **Scale validation is insufficient for generality claims**: One 14B model under one strategy does not support "scale-dependent" as a general phenomenon. Both reviewers agree additional scale points or qualifying the claim would help.
- **Statistical reporting needs strengthening**: CIs on all main results and significance tests for key comparisons are expected at EMNLP.
- **Cross-strategy fragility is underemphasized**: The 59.1% LOO (45.9% excluding d0) fundamentally limits practical deployment, yet the framing is more optimistic than the evidence warrants.

### Points of Disagreement
- **Missing LoRA hyperparameters (R1 W1)**: R2 found that hyperparameters are actually specified in Section 3.2 (r=16, alpha=32, lr=2e-4, 3 epochs). R1 may have missed this or the detail may be insufficiently prominent. Downgraded from major to minor after discussion.
- **Zero figures (R2 W5)**: R1 noted that LaTeX source contains figure environments with captions, suggesting a compilation artifact rather than deliberate omission. Kept as minor since the submitted PDF lacks them regardless.
- **Excitement weighting**: R1 finds the task formalization and Atlas more exciting (3.5) while R2 is more reserved (3.0), viewing the RF pipeline as technically lightweight. Converged to 3.0, reflecting that excitement for the task is tempered by limited methodological novelty.

### Newly Raised During Discussion
- **Cross-strategy d1-d3 near-chance performance**: R1 emphasized that excluding d0, cross-strategy accuracy is essentially near-chance (45.9% vs 33%). This is a serious practical limitation that both reviewers agree is underemphasized.
- **Ecological validity gap is more fundamental than hyperparameter gaps**: R2 argued that the distance between controlled LoRA fine-tuning and real-world recursive contamination (mixed corpora, unknown procedures, heterogeneous models) is the paper's deepest limitation, more important than any specific experimental detail.

---

## 5. Experiment Coverage Assessment

Comparing the paper against the experiment design reference (review_context.yaml):

| Experiment | Status in Paper | Assessment |
|---|---|---|
| 1B 3x3 Benchmark | Fully covered (Table 1) | Complete |
| DCOL Ablation | Cancelled (correctly); negative result reported (Sec 5.5) | Appropriate |
| 14B Scale Validation (plan_014) | Covered (Sec 5.2, Tables 2-5) | Present but thin (1 model, 1 strategy) |
| Wild-data Calibration (plan_015) | Deferred to AAAI; mentioned in Limitations | Acceptable deferral |
| Prompted Generation (plan_016) | Covered (Sec 5.3, Tables 6-8) | Present but narrow (1 model, 10 prompts) |
| Cross-Strategy Pipeline (plan_017) | Fully covered (Sec 5.4, Tables 9-11) | Complete and well-analyzed |

**Coverage**: 4 of 5 non-cancelled experiments are covered. The wild-data deferral is acceptable given the paper's scope. No critical experiments are missing from the design, though depth of coverage varies.

---

## 6. Actionable Recommendations (Priority-Ordered)

### Must-Fix for Main Conference Resubmission
1. **Add existing detector comparison**: Run Binoculars and/or Fast-DetectGPT on the benchmark, threshold scores into ordinal bins, report accuracy. Even a negative result is highly valuable.
2. **Strengthen scale validation**: Add at least one more model family at 7B+ scale (e.g., Llama-3-8B or Mistral-7B) under nucleus sampling. Alternatively, qualify "scale-dependent" claims to acknowledge the single-model limitation.
3. **Complete statistical reporting**: Add bootstrap CIs to all Table 1 entries. Add significance tests (paired bootstrap or McNemar's) for key comparisons (1B vs 14B, BOS vs prompted, within vs pooled).
4. **Fix figure compilation**: Ensure all referenced figures appear in the submitted PDF. The Atlas contribution depends heavily on visual presentation.

### Should-Fix
5. **Add fine-tuning sensitivity**: Vary lr by 2x and epoch count (1, 3, 5) to show depth signal robustness to fine-tuning recipe.
6. **Expand prompted evaluation**: Test on at least one additional model beyond GPT-2 XL; vary prompt diversity.
7. **Strengthen Related Work**: Add 8-10 references covering recent detection methods (DNA-GPT, RADAR), model collapse mitigation strategies, and data contamination detection work.
8. **Recalibrate practical claims**: The abstract and introduction should more clearly scope the contribution to controlled settings, acknowledging cross-strategy fragility and web-crawl FPR.

### Nice-to-Have
9. **Reference model ablation in main text**: Briefly discuss sensitivity to reference model choice.
10. **Unify Atlas framing**: Either provide a more cohesive theoretical framework connecting the four Atlas dimensions, or rename it to avoid overpromising.

---

## 7. Overall Assessment

This paper introduces a genuinely useful new task (ordinal generation depth estimation) and provides the first systematic empirical investigation across models, strategies, and scales. The Depth Degradation Atlas contains several interesting findings, particularly the strategy-dependent trajectory reversal and the scale-dependent EDD concept. The honest reporting of negative results and signal attenuation builds scientific credibility.

However, the paper falls short of EMNLP Main acceptance for three reasons: (1) the absence of existing detector baselines leaves the necessity of the proposed approach unestablished; (2) the technical pipeline (RF on perplexity features) is methodologically lightweight; and (3) the gap between controlled experiments and real-world applicability (20% web-crawl FPR, 59.1% cross-strategy LOO, single-model scale validation) limits the practical impact claimed in the framing.

The paper is well-suited for **EMNLP Findings** in its current form and could reach **Main conference** with the must-fix revisions above, particularly the existing detector comparison and strengthened statistical reporting.

**Converged Overall Score: 3.0 (Findings acceptance)**
