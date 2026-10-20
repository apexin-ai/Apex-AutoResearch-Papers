---
dream_id: dream_review
tier: median
overall_score: 3 - Weak Reject
timestamp: 2026-05-15T15:47:14.213040+00:00
---

# Reviewer 2 (R2): Novelty, Positioning, and Related Work

## 1. Summary

This paper studies "semantic stagnation" detection in LLM coding agents, proposing a weak supervision pipeline with three labeling functions (command repetition, file diff, outcome backpropagation) to generate silver labels over 205K windows from SWE-Agent and OpenHands. It systematically compares structural features, a GRU probe, and LLM judges, finding that lightweight structural features dominate in zero-data cross-agent transfer while the probe surpasses them with fine-tuning. Secondary contributions include a temporal dynamics analysis of labeling functions and a negative result showing five label models fail to beat majority vote.

## 2. Strengths

- **Practically relevant problem.** Semantic stagnation -- where agents appear productive but are stuck -- is a real and underexplored failure mode distinct from simple repetition loops. The paper correctly identifies that existing cycle detectors miss this.

- **Honest treatment of circularity.** The paper is admirably transparent about the circular evaluation problem (structural features reconstructing LFs that produced the labels). The cross-agent evaluation design (train on SWE-Agent, test on OpenHands) is a legitimate and well-motivated way to break this circularity. The feature overlap ablation (Section 5.2) and instance isolation analysis add rigor.

- **Thorough experimental coverage for a short paper.** The paper packs substantial empirical content: main results, cross-agent transfer, robustness ablations, temporal dynamics, label quality analysis, TLM negative results, gold set validation, error analysis, and LLM judge variants. The appendix is well-organized.

- **Useful deployment trade-off framing.** The finding that structural features win in zero-data settings but probes overtake with fine-tuning is a genuinely useful characterization for practitioners. The data efficiency result (GB 0.987 at 10% data) is practically significant.

- **Negative TLM result is informative.** Testing five label models and finding none improve over majority vote in the 3-LF regime is a useful data point for the weak supervision community, with a clear mechanistic explanation (insufficient inter-LF conflict).

- **The cmd_rep coverage analysis is insightful.** Showing that a high-precision, low-recall LF contributes value through coverage expansion rather than label refinement is a non-obvious finding with implications for LF design.

## 3. Weaknesses

- **Limited conceptual novelty -- the core contribution is feature engineering with heuristic labels.** Strip away the weak supervision framing and the paper reduces to: (1) define three heuristic rules for labeling agent stagnation, (2) majority-vote them, (3) train gradient boosted trees on hand-crafted features. Each component is standard. The three LFs -- command repetition, file modification frequency, and outcome backpropagation -- are straightforward heuristics that any practitioner monitoring agent logs would consider. The paper does not introduce a new algorithm, a new architecture, or a new theoretical insight. It is a competent empirical study, but the novelty bar for a top venue is high.

- **The "weak supervision" framing overpromises relative to what is delivered.** The paper invokes the data programming paradigm (Ratner et al.) but uses it in its simplest possible form: three hand-written LFs + majority vote. The temporal label models all fail. FlyingSquid and Snorkel MeTaL collapse. The paper effectively demonstrates that the sophisticated weak supervision machinery is unnecessary here -- majority vote over 3 heuristics suffices. This undermines the methodological positioning: the paper is not advancing weak supervision for agent monitoring so much as showing that basic heuristics work.

- **Cross-agent "transfer" is tested on exactly one pair of agents, both on the same benchmark.** SWE-Agent and OpenHands both operate on SWE-bench GitHub issues. The paper claims "zero-shot cross-coding-agent transfer" but this is transfer between two agents solving the same task distribution. True generalization to different agent architectures (web agents, data analysis agents, multi-agent systems) or different task distributions is untested. The Limitations section acknowledges this, but the title and abstract still overstate the generality.

- **The 20pp circularity gap (in-domain 0.995 vs gold 0.839 on GB; 0.995 vs 0.792 for MV) is severe and underweighted in the narrative.** The gold set reveals that the silver labels -- the evaluation standard for all main tables -- are substantially misaligned with human judgment. When the paper's primary metric shows 0.995 F1 but gold validation shows 0.839, the reader must question every silver-evaluated number. The paper acknowledges circularity but still foregrounds the silver numbers in the abstract, introduction, and conclusion. A more honest framing would lead with the gold set results and use silver metrics as secondary.

- **Gold set is underpowered and has concerning IAA.** Fleiss kappa = 0.39 is "fair" agreement at best. The gold set has only 505 windows (52 with all three annotators), which is small for validating claims over 205K windows. The SWE-only subset for probe evaluation is ~335 windows. The paper should be more cautious in how much weight it places on gold set conclusions.

- **Outcome backpropagation (lambda_3) is a privileged signal unavailable at inference time.** This is acknowledged in Limitations but not sufficiently addressed in the main text. A labeling function that requires knowing the task outcome cannot be used in a real-time monitoring system. Since lambda_3 contributes 33.5% of conf>=2 labels, the silver label quality depends substantially on a signal that breaks the deployment scenario the paper motivates. The 2-LF configuration (without lambda_3 and without cmd_rep) collapses cross-agent, highlighting this fragility.

- **Related work is organized topically but has notable gaps (detailed below).** With ~40 references in the bibliography, the paper has improved from an earlier version, but several important related areas remain underdiscussed.

- **No figures in the main paper body (aside from referenced pipeline/scaling figures).** The paper is extremely table-heavy. A well-designed figure showing, e.g., example stagnation trajectories, the temporal dynamics of LFs, or the cross-agent transfer gap would significantly improve readability and help the reader build intuition for the problem.

## 4. Questions for Authors

1. **On novelty:** What specific technical contribution does this paper make beyond "apply standard weak supervision + gradient boosted trees to agent monitoring"? If the answer is "the finding that structural features suffice," how is this different from the well-known result that hand-crafted features often beat learned representations for narrow classification tasks?

2. **On the gold set:** Given kappa=0.39, how confident are you that "stagnation" has a stable ground truth? Have you considered that the moderate IAA reflects fundamental ambiguity in the concept rather than annotator noise? If so, what does it mean to claim 0.967 F1 on a concept that humans agree on only fairly?

3. **On deployment:** You motivate the work with real-time monitoring (<5ms per window), but lambda_3 requires task outcomes. In a realistic deployment, you would have only lambda_1 and lambda_2. What is the expected performance with only deployment-available LFs? The 2-LF result in Table 5 (0.682 macro-F1) suggests a dramatic degradation.

4. **On the cross-agent claim:** Both agents operate on SWE-bench. Would you expect structural features to transfer to, say, a web navigation agent or a data analysis agent? If not, how should the reader scope the generality claim?

5. **On the negative TLM result:** You attribute the failure to LF quantity (3 LFs). Have you verified this hypothesis by, e.g., adding synthetic LFs with controlled noise to see if label models start helping at 5, 7, or 10 LFs?

6. **On label version bias:** You report that a "version mismatch in OH embedding vectors" caused stagnation rate to shift from 6.56% to 21.4%. This is presented as a finding about "label quality as transfer bottleneck," but it reads more like a bug fix. Can you clarify what exactly was wrong and why this constitutes a scientific contribution rather than an engineering correction?

## 5. Related Work Gaps

- **Anomaly detection in sequential data.** The paper's problem -- detecting anomalous behavioral patterns in action sequences -- is closely related to time-series anomaly detection. The Isolation Forest reference is insufficient. Missing: deep anomaly detection surveys (Pang et al., 2021, "Deep Learning for Anomaly Detection: A Review"), OC-SVM for sequential data, autoencoders for trajectory anomaly (Park et al., 2018). TrajAD is cited but not compared against.

- **Process mining and conformance checking.** Van der Aalst (2016) is cited once in passing, but the paper's structural features (repetition ratios, edit distances, command distributions) are essentially process mining features. The connection to conformance checking -- detecting deviations from expected process models -- deserves discussion.

- **Agent benchmarking beyond SWE-bench.** The paper cites SWE-bench but ignores AgentBench (Liu et al., 2023), MINT (Wang et al., 2024), and other multi-domain agent benchmarks where stagnation detection would be relevant. This limits the positioning.

- **Runtime verification and monitoring.** The real-time monitoring framing connects to runtime verification literature (Leucker & Schallhart, 2009; Bartocci et al., 2018). The paper's structural features are essentially runtime monitors for behavioral properties -- this connection is not drawn.

- **Active learning / human-in-the-loop for agent oversight.** The paper's deployment trade-off (structural for zero-data, probe with fine-tuning) naturally connects to active learning strategies for efficiently acquiring labels. This is not discussed.

- **Contemporary agent failure work.** DebugBench (Tian et al., 2024), AgentTrek (Xu et al., 2025), and other recent agent debugging/trajectory analysis works are not cited.

- **Feature importance / interpretability.** The paper relies heavily on GB feature importance but does not connect to the interpretable ML literature (SHAP, LIME) or discuss whether the structural features provide interpretable failure diagnoses.

## 6. Minor Issues

- The submitted title "Are Stagnation Signals Structural?" uses a question framing for a question the paper clearly answers affirmatively. Consider whether this is misleading vs. the more direct "Structural Features Dominate..." formulation.

- Table 1 footnotes are dense and hard to parse. Consider moving some information to the main text.

- The paper uses "cross-coding-agent" throughout when "cross-agent" would be clearer and more standard.

- Section 3.1 defines y=0 as stagnation and y=1 as progress, but the error analysis (Appendix C.8) uses "stagnation-positive convention." This convention inconsistency should be clarified.

- The paper could benefit from a running example showing what a stagnation window looks like vs. a progress window, to ground the reader's intuition.

- Cost comparison with LLM judges ($11.66-$40.56 per test set) is useful but the structural feature extraction cost is not quantified beyond "<5ms per window."

## 7. Overall Assessment

**Score: 3 (Weak Reject)**

This is a thorough and honest empirical study of a relevant problem. The authors deserve credit for transparent handling of circularity, comprehensive ablations, and informative negative results. However, the paper falls short of the novelty threshold for a top ML venue for several reasons:

(1) The core technical contribution -- three heuristic labeling functions + majority vote + gradient boosted trees on hand-crafted features -- uses only standard components with no methodological innovation. The "finding" that structural features beat learned representations in low-data transfer is well-established in ML.

(2) The weak supervision framing is undercut by the paper's own results: all sophisticated label models fail, and majority vote over 3 heuristics is all you need. The paper effectively argues against its own methodological framework.

(3) The evaluation relies predominantly on silver labels that have a ~16pp gap with human gold annotations (0.839 vs 0.995 in-domain), yet the main claims are stated in terms of the silver metrics. The gold set is too small (505 windows, kappa=0.39) to serve as a reliable corrective.

(4) Cross-agent transfer is demonstrated on a single agent pair over the same task benchmark, limiting the generality claim.

(5) One of three labeling functions (lambda_3) requires privileged information unavailable at deployment, and the deployment-available configuration (2-LF) degrades substantially.

The paper would be strengthened by: (a) a larger and higher-IAA gold set as the primary evaluation; (b) demonstration on at least one non-SE agent domain; (c) a more modest framing as an empirical analysis rather than a methodological contribution; (d) deeper engagement with anomaly detection and process mining literature.

## 8. Confidence

**4/5.** I am confident in this assessment. I have expertise in weak supervision, agent evaluation, and ML methodology. I have read the paper thoroughly including all appendices. My main uncertainty is whether the practical utility of the deployment trade-off finding is sufficient to overcome the novelty concerns -- reasonable reviewers could weigh this differently.