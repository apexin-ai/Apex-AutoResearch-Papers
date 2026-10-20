# Research conversation: The LLM Annotation Multiverse: Specification Curve Analysis for Robust Computational Social Science ### Motivation LLM-b

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-3/afead175-60c3-43af-a590-891e6a9fc223.jsonl`
- **Structured JSON:** [`0396e2d94f89fd6aa30e.json`](../../sessions/03/0396e2d94f89fd6aa30e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T04:02:22.782Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T04:02:22.782Z",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "content": "## The LLM Annotation Multiverse: Specification Curve Analysis for Robust Computational Social Science\n\n### Motivation\n\nLLM-based text annotation has become the default measurement instrument in computational social science (CSS), yet the pipeline involves numerous researcher degrees of freedom—model selection, prompt template, temperature, system instruction, output parsing—each capable of shifting substantive conclusions. Baumann et al. (arXiv:2509.08825, 2025) document a 31% \"LLM hacking\" risk across 18 LLMs × 37 tasks × 13M labels: for nearly one-third of hypothesis tests, a researcher can find a pipeline configuration that reverses the statistical conclusion. McLaren et al. (arXiv:2603.26898, 2026) show that interaction effects among pipeline dimensions dominate main effects, meaning pairwise sensitivity checks underestimate true instability. Messing (arXiv:2604.11581, 2026) demonstrates that naive standard errors in LLM pipelines are 40–60% smaller than TEE-corrected standard errors that account for prompt, temperature, and judge-model variance, with coverage of naive 95% CIs degrading as sample size increases. Kosch & Feger (CACM 2026) label this phenomenon \"prompt-hacking\"—the LLM analogue of p-hacking—but offer no formal remedy.\n\nThe methodological status quo offers two partial responses. First, diagnostic studies (Baumann et al. 2025; McLaren et al. 2026; arXiv:2601.02370, 2026) quantify instability but prescribe no inferential framework for deciding whether a finding is robust. Second, statistical correction methods—Design-based Supervised Learning (DSL; Egami et al., NeurIPS 2023), Prediction-Powered Inference / Confidence-Driven Inference (PPI/CDI; Gligorić et al., NAACL 2025), and their comparative benchmarking (Audinet de Pieuchon et al., EMNLP 2025)—use small human-label sets to debias LLM annotations within a single chosen pipeline configuration. These correction methods answer: \"Given my pipeline choice, how do I get an unbiased estimate?\" They cannot answer the logically prior question: \"Does my conclusion depend on which pipeline I chose?\" This is precisely the question multiverse analysis is designed to address.\n\n### Research Landscape\n\n**Diagnostic work.** Baumann et al. (arXiv:2509.08825) provide the largest controlled study of LLM annotation instability (18 models, 37 tasks, 21 mitigation strategies). McLaren et al. (arXiv:2603.26898) extend this to interaction effects in political science annotation. The Variance-Aware LLM Annotation framework (arXiv:2601.02370, 2026) uses generalizability theory to decompose five variance sources (construct, interface, model, output, aggregation), reporting 12–85 pp outcome shifts from minor design choices, but provides protocol guidance rather than statistical inference.\n\n**Measurement error correction.** Messing (arXiv:2604.11581, 2026) decomposes LLM pipeline uncertainty into variance components (prompt phrasing, temperature, judge model) and proposes TEE-corrected standard errors. This framework addresses measurement error within a design-study projection paradigm—it corrects the confidence interval around a single estimate but does not construct or traverse a multiverse of defensible configurations, nor does it classify pipeline dimensions or provide specification-curve-based joint inference. Our work is complementary: Messing's TEE can serve as the per-specification error estimator within each point on our specification curve, while our framework provides the global robustness assessment that TEE alone cannot deliver.\n\n**Single-pipeline correction.** DSL (Egami et al., NeurIPS 2023) uses a small human-label set to debias LLM annotations for downstream inference; CDI (Gligorić et al., NAACL 2025) combines LLM confidence scores with human labels for efficient estimation; Audinet de Pieuchon et al. (EMNLP 2025) benchmark DSL vs PPI across annotation budgets. All three assume a fixed pipeline configuration. They solve pipeline-internal error but are blind to pipeline-external robustness: if a researcher had chosen a different model or prompt, would the corrected conclusion still hold? This is the gap our framework fills.\n\n**Perspectivism.** Mehrotra et al. (arXiv:2603.21404, 2026) propose Perspective-Driven Inference for subjective annotation tasks, treating different LLM perspectives as legitimate viewpoints rather than errors. This reinforces our argument that for subjective tasks (sentiment, toxicity, stance), pipeline variation is not merely noise to be corrected but a substantive dimension that multiverse analysis should expose.\n\n**Multiverse methodology.** Simonsohn et al. (Nature Human Behaviour, 2020) formalize specification curve analysis: enumerate justified specifications, visualize the distribution of effects, and conduct permutation-based joint inference. Del Giudice & Gangestad (AMPPS, 2021) propose the E/N/U classification framework—Type E (equivalent: defensible alternatives that should all appear in the multiverse), Type N (nonequivalent: one option is clearly superior and should be fixed), Type U (uncertain: run separate multiverses under each option)—to discipline which specifications enter the multiverse. Auspurg (PNAS 2025) critiques brute-force multiverse analysis for mixing justified and unjustified models, diluting true signals; Ganslmeier & Vlandas (PNAS 2025) reply that restricting to \"justified\" models is itself contested. This debate remains unresolved in social science. Carlson & Burbano (SMJ 2026) recommend informal sensitivity analysis (run a few model+prompt combinations and check consistency) as practical guidance for management researchers.\n\n### Opportunity and Core Argument\n\n**The gap.** No existing work applies formal multiverse methodology—specification curve analysis with principled multiverse construction and joint statistical inference—to LLM annotation pipelines.\n\n**Why LLM annotation is an epistemically ideal setting for multiverse analysis.** Auspurg's (PNAS 2025) central critique of multiverse analysis—that it conflates justified and unjustified specifications, producing meaningless variance—rests on three conditions that are typically hard to satisfy in social science: (a) the estimand must remain constant across specifications, (b) included specifications must not be misspecified, and (c) researchers need a principled basis for classifying which specifications are defensible. LLM annotation pipelines satisfy all three conditions in ways that traditional social science modeling does not:\n\n- **(a) Constant estimand.** All pipeline configurations target the same annotation label for the same text—the estimand is defined by the coding scheme, not by the model. Unlike regression multiverse (where changing covariates may change the estimand), changing the model or prompt does not change what we are trying to measure.\n- **(b) No misspecification in the classical sense.** Each pipeline configuration is a deterministic (or stochastic with known seed) mapping from text to label. There is no omitted-variable bias or functional-form misspecification—only measurement quality variation.\n- **(c) Principled E/N/U classification is feasible.** Pipeline dimensions have well-defined semantics (model architecture, prompt verbosity, temperature value) with clear task-conditional constraints that make E/N/U classification less contested than in regression multiverse.\n\nThis epistemological argument is a core intellectual contribution of this paper: it demonstrates that the Auspurg critique, while valid for many social science applications, does not apply to LLM annotation, thereby establishing the first positive case where exhaustive multiverse enumeration is both theoretically justified and practically feasible.\n\n**Why principled multiverse, not ad hoc sensitivity checks?** Carlson & Burbano (SMJ 2026) and common practice suggest running 3–5 model+prompt combinations as informal sensitivity analysis. This is insufficient for three reasons: (1) ad hoc selection of configurations may cluster in a narrow region of the specification space, missing dimensions or interactions that reverse conclusions (McLaren et al. 2026 show interactions dominate); (2) without a principled construction of the defensible space, there is no basis for claiming \"I have checked enough\"; (3) ad hoc checks provide no formal joint inference—no p-value for \"the finding is robust across the defensible space.\" Our framework provides all three: principled construction (E/N/U), exhaustive traversal, and permutation-based joint significance testing.\n\n**Why multiverse, not just measurement error correction?** Messing's (arXiv:2604.11581) TEE framework corrects the standard error of a single estimate by accounting for pipeline variance components. This answers \"how uncertain is my point estimate?\" Our specification curve analysis answers the distinct question: \"across the entire space of defensible configurations, does my conclusion hold?\" These are complementary: TEE provides local precision, multiverse provides global robustness. A finding can have a narrow TEE-corrected CI (precise) yet be fragile across the multiverse (not robust to pipeline choice), or vice versa.\n\n### Approach\n\n**Stage 1: E/N/U Multiverse Construction (Primary Methodological Contribution)**\n\nAdapt the Del Giudice & Gangestad (AMPPS, 2021) E/N/U classification framework to LLM annotation pipeline dimensions. This adaptation is the paper's primary methodological contribution—no prior work has systematically classified LLM pipeline decisions using this framework.\n\nFive pipeline dimensions, each classified as E, N, or U with task-conditional rules:\n\n| Dimension | Options | Default classification | Task-conditional overrides |\n|-----------|---------|----------------------|---------------------------|\n| Model | 6 models (see below) | Type E | — |\n| Prompt template | 3 variants (minimal / instructed / chain-of-thought) | Type E | For simple binary tasks, CoT may be Type N (unnecessary complexity) |\n| Temperature | {0, 0.3, 0.7} | Type U | For deterministic factual tasks → temperature=0 is Type N; for subjective tasks → all three are Type E |\n| System instruction | {generic, domain-specific, none} | Type E | — |\n| Output parsing | {regex, structured JSON, first-token} | Type E for well-defined tasks | For free-form tasks → Type U |\n\nNaïve Cartesian product: 6 × 3 × 3 × 3 × 3 = 486 configurations per model choice, or 810 if model is included. After E/N/U pruning (fixing Type N to best option, splitting Type U into separate sub-multiverses), the defensible multiverse contains approximately 90–270 configurations per task, depending on task-type-triggered overrides.\n\nClassification criteria are formalized in a Boba-style DSL (Liu et al., CHI 2021) that encodes task-conditional constraints as executable rules, ensuring reproducibility and transparency of multiverse construction decisions.\n\n**E/N/U classification criteria (systematic rubric):**\n- **Type E**: Multiple options are defensible and no prior evidence or theoretical argument favors one over others for the given task type.\n- **Type N**: One option is clearly superior based on prior evidence (e.g., temperature=0 for factual extraction where determinism is preferred) or theoretical argument (e.g., CoT is unnecessary overhead for simple binary classification).\n- **Type U**: Genuine uncertainty about whether options target the same construct (e.g., temperature variation for subjective tasks may elicit different but legitimate annotation perspectives).\n\n**Stage 2: Specification Curve Analysis + Joint Inference**\n\nFor each task, execute all configurations in the pruned multiverse across all 6 models. For each configuration, compute the downstream hypothesis test (e.g., group comparison, correlation, regression coefficient) on the annotated data. Apply the specification curve methodology of Simonsohn et al. (Nature Human Behaviour, 2020):\n\n1. Rank specifications by effect size and visualize as a specification curve.\n2. Classify each hypothesis as **robust** (sign-consistent and jointly significant), **fragile** (sign-consistent but not jointly significant), or **sign-inconsistent** (effect direction reverses across defensible configurations).\n3. Conduct permutation-based joint inference (≥500 permutations): under the null, randomly shuffle the mapping between pipeline dimensions and annotations, re-compute the specification curve, and derive a joint p-value for the hypothesis of non-zero effect across the multiverse. Importantly, permutation re-computation operates on downstream statistics from cached annotation outputs—no re-annotation required, making this computationally feasible.\n\n**Stage 3: Variance Decomposition**\n\nDecompose specification-curve variance using factorial ANOVA over the full-factorial annotation results, quantifying the contribution of each pipeline dimension (model, prompt, temperature, system instruction, parsing) and their interactions to downstream inference instability. Model is nested within model-size class (large: >250B parameters; medium: <130B) to disentangle architecture/family effects from scale effects. Report main effects, two-way interactions, and the proportion of variance attributable to each source. Compare this downstream-inference-focused decomposition with Messing's (arXiv:2604.11581) annotation-accuracy-focused TEE decomposition on the same configurations, testing whether annotation accuracy variance predicts inference instability (they need not correlate—a model may produce biased but consistent annotations that support the same directional conclusion).\n\n### Experimental Design\n\n**Data source.** Baumann et al. (arXiv:2509.08825) public dataset (MIT license): 18 LLMs × 37 tasks × 13M labels with gold-standard human annotations.\n\n**Task selection.** 10 tasks selected from Baumann's 37, stratified to cover: binary classification (3 tasks), multi-class classification (3 tasks), ordinal rating (2 tasks), and subjective/contested annotation (2 tasks, e.g., sentiment, toxicity). Selection criteria: (i) gold labels available, (ii) sample size ≥1,000, (iii) task has a natural downstream hypothesis (group comparison or correlation) testable on the annotated data. Specific tasks and their downstream hypotheses will be pre-registered.\n\n**Models.** 6 models spanning architecture families, scale, and openness:\n- Open-weight large MoE: Llama 4 Maverick (400B MoE), Qwen 3.5 (397B MoE, 17B active; released Feb 2026, Apache 2.0)\n- Open-weight medium: Gemma 4 (26B MoE)\n- Proprietary anchor: GPT-4o (chosen over Claude to avoid circularity with any LLM-assisted E/N/U classification process)\n- Two additional models selected to fill gaps in the architecture/scale matrix (e.g., one dense mid-scale model, one additional proprietary model)\n\nModel size is recorded as a covariate/nested factor in the ANOVA to disentangle scale effects from family effects (补充: Baumann et al. 2025 find small LLMs roughly double hacking risk; McLaren et al. 2026 find model choice significant even among similar-scale models).\n\n**Execution.** Full-factorial execution of the pruned multiverse per task. Annotation uses 25-item batched prompts to reduce API overhead. Estimated total: 500M–1.2B tokens across all models, with cost estimated at $1,200–$2,000 (to be validated by pilot run on 1–2 tasks before full execution). A pilot run on 2 tasks (~$50–100) will verify token consumption estimates and annotation quality.\n\n**Evaluation and baselines.**\n1. *Specification curve + joint inference*: For each of the 10 tasks, produce specification curves and classify hypotheses as robust/fragile/sign-inconsistent.\n2. *Comparative evaluation with PPI/DSL*: On 2–3 representative tasks, run PPI (Gligorić et al., NAACL 2025) and DSL (Egami et al., NeurIPS 2023) using Baumann's gold labels as the human-annotation budget. Compare: (a) when multiverse says \"robust,\" does PPI/DSL-corrected inference agree? (b) when multiverse says \"fragile,\" can PPI/DSL resolve the fragility? This positions the two paradigms as complementary rather than competing.\n3. *Variance decomposition*: Factorial ANOVA with model size as nested factor, reporting main effects and interactions.\n4. *TEE comparison*: On the same configurations, compute Messing-style TEE decomposition alongside our downstream-inference decomposition; report correlation between annotation-accuracy variance and inference instability.\n\n**Ablation studies** (on 2–3 representative tasks):\n1. *E/N/U sensitivity analysis*: Perturb E/N/U boundary decisions (reclassify selected N→U or expand E ranges) and compare resulting specification curves and robustness classifications. Also compare the principled (E/N/U-pruned) multiverse against the naïve (full Cartesian product) multiverse to quantify the impact of principled pruning on robustness conclusions. This directly addresses Auspurg's (PNAS 2025) critique with empirical evidence.\n2. *Task-conditional constraint effect*: Remove task-type-specific constraints (e.g., allow all temperatures for deterministic tasks) and measure change in specification curve shape and robustness classification.\n3. *Model diversity curve*: Compute robustness classifications using 6 models, then 3 models, then 1 model; report stability of conclusions as a function of model count. This informs practical adoption—researchers with limited budgets need to know the minimum model diversity for reliable robustness assessment.\n4. *Batch size pilot*: Compare batch=25 vs batch=1 annotation on ≥1 task with ≥1 model to verify batching does not systematically degrade annotation quality.\n\n### Expected Contributions\n\n1. **Methodological (primary):** The first adaptation of E/N/U multiverse classification (Del Giudice & Gangestad, AMPPS 2021) to LLM annotation pipelines, with a task-conditional classification rubric formalized in executable DSL, enabling principled construction of the defensible configuration space.\n2. **Epistemological:** A formal argument that LLM annotation pipelines satisfy the conditions under which exhaustive multiverse analysis is theoretically justified—directly engaging the Auspurg (PNAS 2025) vs. Ganslmeier & Vlandas (PNAS 2025) debate and providing the first positive case study for principled exhaustive specification enumeration.\n3. **Empirical:** A robustness landscape across 10 CSS tasks: which tasks yield robust findings, which are fragile, which pipeline dimensions and interactions drive instability, and how principled multiverse assessment compares with both ad hoc sensitivity checks and PPI/DSL correction.\n\n### Budget and Feasibility\n\n- **API costs:** $1,200–$2,000 total (6 models × 10 tasks × 90–270 configs × 1,000–3,000 samples; batched at 25 items/prompt). Qwen 3.5 and Llama 4 Maverick via OpenRouter; GPT-4o via OpenAI API. Pilot run ($50–100) precedes full execution.\n- **Compute:** Permutation tests (≥500 permutations) and ANOVA operate on cached annotation outputs—no re-annotation required. Estimated compute for post-annotation analysis: <24 hours on a single GPU/CPU cluster.\n- **Data:** Baumann et al. public dataset (MIT license). No additional data collection or human annotation required (gold labels pre-exist).\n- **Timeline:** Pilot (1 week) → Full annotation (2–3 weeks, parallelized across models) → Analysis and ablations (2–3 weeks) → Writing (3–4 weeks). Total: ~8–10 weeks to submission-ready manuscript."
}
```

---

### Runtime record

_source line 2 · 2026-05-20T04:02:22.786Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T04:02:22.786Z",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223"
}
```

---

## Round 1

46 recorded events

### User

_source line 3 · 2026-05-20T04:02:22.810Z_

## The LLM Annotation Multiverse: Specification Curve Analysis for Robust Computational Social Science

### Motivation

LLM-based text annotation has become the default measurement instrument in computational social science (CSS), yet the pipeline involves numerous researcher degrees of freedom—model selection, prompt template, temperature, system instruction, output parsing—each capable of shifting substantive conclusions. Baumann et al. (arXiv:2509.08825, 2025) document a 31% "LLM hacking" risk across 18 LLMs × 37 tasks × 13M labels: for nearly one-third of hypothesis tests, a researcher can find a pipeline configuration that reverses the statistical conclusion. McLaren et al. (arXiv:2603.26898, 2026) show that interaction effects among pipeline dimensions dominate main effects, meaning pairwise sensitivity checks underestimate true instability. Messing (arXiv:2604.11581, 2026) demonstrates that naive standard errors in LLM pipelines are 40–60% smaller than TEE-corrected standard errors that account for prompt, temperature, and judge-model variance, with coverage of naive 95% CIs degrading as sample size increases. Kosch & Feger (CACM 2026) label this phenomenon "prompt-hacking"—the LLM analogue of p-hacking—but offer no formal remedy.

The methodological status quo offers two partial responses. First, diagnostic studies (Baumann et al. 2025; McLaren et al. 2026; arXiv:2601.02370, 2026) quantify instability but prescribe no inferential framework for deciding whether a finding is robust. Second, statistical correction methods—Design-based Supervised Learning (DSL; Egami et al., NeurIPS 2023), Prediction-Powered Inference / Confidence-Driven Inference (PPI/CDI; Gligorić et al., NAACL 2025), and their comparative benchmarking (Audinet de Pieuchon et al., EMNLP 2025)—use small human-label sets to debias LLM annotations within a single chosen pipeline configuration. These correction methods answer: "Given my pipeline choice, how do I get an unbiased estimate?" They cannot answer the logically prior question: "Does my conclusion depend on which pipeline I chose?" This is precisely the question multiverse analysis is designed to address.

### Research Landscape

**Diagnostic work.** Baumann et al. (arXiv:2509.08825) provide the largest controlled study of LLM annotation instability (18 models, 37 tasks, 21 mitigation strategies). McLaren et al. (arXiv:2603.26898) extend this to interaction effects in political science annotation. The Variance-Aware LLM Annotation framework (arXiv:2601.02370, 2026) uses generalizability theory to decompose five variance sources (construct, interface, model, output, aggregation), reporting 12–85 pp outcome shifts from minor design choices, but provides protocol guidance rather than statistical inference.

**Measurement error correction.** Messing (arXiv:2604.11581, 2026) decomposes LLM pipeline uncertainty into variance components (prompt phrasing, temperature, judge model) and proposes TEE-corrected standard errors. This framework addresses measurement error within a design-study projection paradigm—it corrects the confidence interval around a single estimate but does not construct or traverse a multiverse of defensible configurations, nor does it classify pipeline dimensions or provide specification-curve-based joint inference. Our work is complementary: Messing's TEE can serve as the per-specification error estimator within each point on our specification curve, while our framework provides the global robustness assessment that TEE alone cannot deliver.

**Single-pipeline correction.** DSL (Egami et al., NeurIPS 2023) uses a small human-label set to debias LLM annotations for downstream inference; CDI (Gligorić et al., NAACL 2025) combines LLM confidence scores with human labels for efficient estimation; Audinet de Pieuchon et al. (EMNLP 2025) benchmark DSL vs PPI across annotation budgets. All three assume a fixed pipeline configuration. They solve pipeline-internal error but are blind to pipeline-external robustness: if a researcher had chosen a different model or prompt, would the corrected conclusion still hold? This is the gap our framework fills.

**Perspectivism.** Mehrotra et al. (arXiv:2603.21404, 2026) propose Perspective-Driven Inference for subjective annotation tasks, treating different LLM perspectives as legitimate viewpoints rather than errors. This reinforces our argument that for subjective tasks (sentiment, toxicity, stance), pipeline variation is not merely noise to be corrected but a substantive dimension that multiverse analysis should expose.

**Multiverse methodology.** Simonsohn et al. (Nature Human Behaviour, 2020) formalize specification curve analysis: enumerate justified specifications, visualize the distribution of effects, and conduct permutation-based joint inference. Del Giudice & Gangestad (AMPPS, 2021) propose the E/N/U classification framework—Type E (equivalent: defensible alternatives that should all appear in the multiverse), Type N (nonequivalent: one option is clearly superior and should be fixed), Type U (uncertain: run separate multiverses under each option)—to discipline which specifications enter the multiverse. Auspurg (PNAS 2025) critiques brute-force multiverse analysis for mixing justified and unjustified models, diluting true signals; Ganslmeier & Vlandas (PNAS 2025) reply that restricting to "justified" models is itself contested. This debate remains unresolved in social science. Carlson & Burbano (SMJ 2026) recommend informal sensitivity analysis (run a few model+prompt combinations and check consistency) as practical guidance for management researchers.

### Opportunity and Core Argument

**The gap.** No existing work applies formal multiverse methodology—specification curve analysis with principled multiverse construction and joint statistical inference—to LLM annotation pipelines.

**Why LLM annotation is an epistemically ideal setting for multiverse analysis.** Auspurg's (PNAS 2025) central critique of multiverse analysis—that it conflates justified and unjustified specifications, producing meaningless variance—rests on three conditions that are typically hard to satisfy in social science: (a) the estimand must remain constant across specifications, (b) included specifications must not be misspecified, and (c) researchers need a principled basis for classifying which specifications are defensible. LLM annotation pipelines satisfy all three conditions in ways that traditional social science modeling does not:

- **(a) Constant estimand.** All pipeline configurations target the same annotation label for the same text—the estimand is defined by the coding scheme, not by the model. Unlike regression multiverse (where changing covariates may change the estimand), changing the model or prompt does not change what we are trying to measure.
- **(b) No misspecification in the classical sense.** Each pipeline configuration is a deterministic (or stochastic with known seed) mapping from text to label. There is no omitted-variable bias or functional-form misspecification—only measurement quality variation.
- **(c) Principled E/N/U classification is feasible.** Pipeline dimensions have well-defined semantics (model architecture, prompt verbosity, temperature value) with clear task-conditional constraints that make E/N/U classification less contested than in regression multiverse.

This epistemological argument is a core intellectual contribution of this paper: it demonstrates that the Auspurg critique, while valid for many social science applications, does not apply to LLM annotation, thereby establishing the first positive case where exhaustive multiverse enumeration is both theoretically justified and practically feasible.

**Why principled multiverse, not ad hoc sensitivity checks?** Carlson & Burbano (SMJ 2026) and common practice suggest running 3–5 model+prompt combinations as informal sensitivity analysis. This is insufficient for three reasons: (1) ad hoc selection of configurations may cluster in a narrow region of the specification space, missing dimensions or interactions that reverse conclusions (McLaren et al. 2026 show interactions dominate); (2) without a principled construction of the defensible space, there is no basis for claiming "I have checked enough"; (3) ad hoc checks provide no formal joint inference—no p-value for "the finding is robust across the defensible space." Our framework provides all three: principled construction (E/N/U), exhaustive traversal, and permutation-based joint significance testing.

**Why multiverse, not just measurement error correction?** Messing's (arXiv:2604.11581) TEE framework corrects the standard error of a single estimate by accounting for pipeline variance components. This answers "how uncertain is my point estimate?" Our specification curve analysis answers the distinct question: "across the entire space of defensible configurations, does my conclusion hold?" These are complementary: TEE provides local precision, multiverse provides global robustness. A finding can have a narrow TEE-corrected CI (precise) yet be fragile across the multiverse (not robust to pipeline choice), or vice versa.

### Approach

**Stage 1: E/N/U Multiverse Construction (Primary Methodological Contribution)**

Adapt the Del Giudice & Gangestad (AMPPS, 2021) E/N/U classification framework to LLM annotation pipeline dimensions. This adaptation is the paper's primary methodological contribution—no prior work has systematically classified LLM pipeline decisions using this framework.

Five pipeline dimensions, each classified as E, N, or U with task-conditional rules:

| Dimension | Options | Default classification | Task-conditional overrides |
|-----------|---------|----------------------|---------------------------|
| Model | 6 models (see below) | Type E | — |
| Prompt template | 3 variants (minimal / instructed / chain-of-thought) | Type E | For simple binary tasks, CoT may be Type N (unnecessary complexity) |
| Temperature | {0, 0.3, 0.7} | Type U | For deterministic factual tasks → temperature=0 is Type N; for subjective tasks → all three are Type E |
| System instruction | {generic, domain-specific, none} | Type E | — |
| Output parsing | {regex, structured JSON, first-token} | Type E for well-defined tasks | For free-form tasks → Type U |

Naïve Cartesian product: 6 × 3 × 3 × 3 × 3 = 486 configurations per model choice, or 810 if model is included. After E/N/U pruning (fixing Type N to best option, splitting Type U into separate sub-multiverses), the defensible multiverse contains approximately 90–270 configurations per task, depending on task-type-triggered overrides.

Classification criteria are formalized in a Boba-style DSL (Liu et al., CHI 2021) that encodes task-conditional constraints as executable rules, ensuring reproducibility and transparency of multiverse construction decisions.

**E/N/U classification criteria (systematic rubric):**
- **Type E**: Multiple options are defensible and no prior evidence or theoretical argument favors one over others for the given task type.
- **Type N**: One option is clearly superior based on prior evidence (e.g., temperature=0 for factual extraction where determinism is preferred) or theoretical argument (e.g., CoT is unnecessary overhead for simple binary classification).
- **Type U**: Genuine uncertainty about whether options target the same construct (e.g., temperature variation for subjective tasks may elicit different but legitimate annotation perspectives).

**Stage 2: Specification Curve Analysis + Joint Inference**

For each task, execute all configurations in the pruned multiverse across all 6 models. For each configuration, compute the downstream hypothesis test (e.g., group comparison, correlation, regression coefficient) on the annotated data. Apply the specification curve methodology of Simonsohn et al. (Nature Human Behaviour, 2020):

1. Rank specifications by effect size and visualize as a specification curve.
2. Classify each hypothesis as **robust** (sign-consistent and jointly significant), **fragile** (sign-consistent but not jointly significant), or **sign-inconsistent** (effect direction reverses across defensible configurations).
3. Conduct permutation-based joint inference (≥500 permutations): under the null, randomly shuffle the mapping between pipeline dimensions and annotations, re-compute the specification curve, and derive a joint p-value for the hypothesis of non-zero effect across the multiverse. Importantly, permutation re-computation operates on downstream statistics from cached annotation outputs—no re-annotation required, making this computationally feasible.

**Stage 3: Variance Decomposition**

Decompose specification-curve variance using factorial ANOVA over the full-factorial annotation results, quantifying the contribution of each pipeline dimension (model, prompt, temperature, system instruction, parsing) and their interactions to downstream inference instability. Model is nested within model-size class (large: >250B parameters; medium: <130B) to disentangle architecture/family effects from scale effects. Report main effects, two-way interactions, and the proportion of variance attributable to each source. Compare this downstream-inference-focused decomposition with Messing's (arXiv:2604.11581) annotation-accuracy-focused TEE decomposition on the same configurations, testing whether annotation accuracy variance predicts inference instability (they need not correlate—a model may produce biased but consistent annotations that support the same directional conclusion).

### Experimental Design

**Data source.** Baumann et al. (arXiv:2509.08825) public dataset (MIT license): 18 LLMs × 37 tasks × 13M labels with gold-standard human annotations.

**Task selection.** 10 tasks selected from Baumann's 37, stratified to cover: binary classification (3 tasks), multi-class classification (3 tasks), ordinal rating (2 tasks), and subjective/contested annotation (2 tasks, e.g., sentiment, toxicity). Selection criteria: (i) gold labels available, (ii) sample size ≥1,000, (iii) task has a natural downstream hypothesis (group comparison or correlation) testable on the annotated data. Specific tasks and their downstream hypotheses will be pre-registered.

**Models.** 6 models spanning architecture families, scale, and openness:
- Open-weight large MoE: Llama 4 Maverick (400B MoE), Qwen 3.5 (397B MoE, 17B active; released Feb 2026, Apache 2.0)
- Open-weight medium: Gemma 4 (26B MoE)
- Proprietary anchor: GPT-4o (chosen over Claude to avoid circularity with any LLM-assisted E/N/U classification process)
- Two additional models selected to fill gaps in the architecture/scale matrix (e.g., one dense mid-scale model, one additional proprietary model)

Model size is recorded as a covariate/nested factor in the ANOVA to disentangle scale effects from family effects (补充: Baumann et al. 2025 find small LLMs roughly double hacking risk; McLaren et al. 2026 find model choice significant even among similar-scale models).

**Execution.** Full-factorial execution of the pruned multiverse per task. Annotation uses 25-item batched prompts to reduce API overhead. Estimated total: 500M–1.2B tokens across all models, with cost estimated at $1,200–$2,000 (to be validated by pilot run on 1–2 tasks before full execution). A pilot run on 2 tasks (~$50–100) will verify token consumption estimates and annotation quality.

**Evaluation and baselines.**
1. *Specification curve + joint inference*: For each of the 10 tasks, produce specification curves and classify hypotheses as robust/fragile/sign-inconsistent.
2. *Comparative evaluation with PPI/DSL*: On 2–3 representative tasks, run PPI (Gligorić et al., NAACL 2025) and DSL (Egami et al., NeurIPS 2023) using Baumann's gold labels as the human-annotation budget. Compare: (a) when multiverse says "robust," does PPI/DSL-corrected inference agree? (b) when multiverse says "fragile," can PPI/DSL resolve the fragility? This positions the two paradigms as complementary rather than competing.
3. *Variance decomposition*: Factorial ANOVA with model size as nested factor, reporting main effects and interactions.
4. *TEE comparison*: On the same configurations, compute Messing-style TEE decomposition alongside our downstream-inference decomposition; report correlation between annotation-accuracy variance and inference instability.

**Ablation studies** (on 2–3 representative tasks):
1. *E/N/U sensitivity analysis*: Perturb E/N/U boundary decisions (reclassify selected N→U or expand E ranges) and compare resulting specification curves and robustness classifications. Also compare the principled (E/N/U-pruned) multiverse against the naïve (full Cartesian product) multiverse to quantify the impact of principled pruning on robustness conclusions. This directly addresses Auspurg's (PNAS 2025) critique with empirical evidence.
2. *Task-conditional constraint effect*: Remove task-type-specific constraints (e.g., allow all temperatures for deterministic tasks) and measure change in specification curve shape and robustness classification.
3. *Model diversity curve*: Compute robustness classifications using 6 models, then 3 models, then 1 model; report stability of conclusions as a function of model count. This informs practical adoption—researchers with limited budgets need to know the minimum model diversity for reliable robustness assessment.
4. *Batch size pilot*: Compare batch=25 vs batch=1 annotation on ≥1 task with ≥1 model to verify batching does not systematically degrade annotation quality.

### Expected Contributions

1. **Methodological (primary):** The first adaptation of E/N/U multiverse classification (Del Giudice & Gangestad, AMPPS 2021) to LLM annotation pipelines, with a task-conditional classification rubric formalized in executable DSL, enabling principled construction of the defensible configuration space.
2. **Epistemological:** A formal argument that LLM annotation pipelines satisfy the conditions under which exhaustive multiverse analysis is theoretically justified—directly engaging the Auspurg (PNAS 2025) vs. Ganslmeier & Vlandas (PNAS 2025) debate and providing the first positive case study for principled exhaustive specification enumeration.
3. **Empirical:** A robustness landscape across 10 CSS tasks: which tasks yield robust findings, which are fragile, which pipeline dimensions and interactions drive instability, and how principled multiverse assessment compares with both ad hoc sensitivity checks and PPI/DSL correction.

### Budget and Feasibility

- **API costs:** $1,200–$2,000 total (6 models × 10 tasks × 90–270 configs × 1,000–3,000 samples; batched at 25 items/prompt). Qwen 3.5 and Llama 4 Maverick via OpenRouter; GPT-4o via OpenAI API. Pilot run ($50–100) precedes full execution.
- **Compute:** Permutation tests (≥500 permutations) and ANOVA operate on cached annotation outputs—no re-annotation required. Estimated compute for post-annotation analysis: <24 hours on a single GPU/CPU cluster.
- **Data:** Baumann et al. public dataset (MIT license). No additional data collection or human annotation required (gold labels pre-exist).
- **Timeline:** Pilot (1 week) → Full annotation (2–3 weeks, parallelized across models) → Analysis and ablations (2–3 weeks) → Writing (3–4 weeks). Total: ~8–10 weeks to submission-ready manuscript.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "73ab1a43-96b2-4654-a2b9-23d82346af16",
  "type": "user",
  "uuid": "3c91ed1c-1dba-4899-b9f6-8c9fde419ec2",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T04:02:22.807Z_

```json
{
  "parentUuid": "3c91ed1c-1dba-4899-b9f6-8c9fde419ec2",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": [],
    "pendingMcpServers": []
  },
  "type": "attachment",
  "uuid": "cd68c42e-b844-4108-b9d2-499519c24de0",
  "timestamp": "2026-05-20T04:02:22.807Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T04:02:22.807Z_

```json
{
  "parentUuid": "cd68c42e-b844-4108-b9d2-499519c24de0",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "6183da0a-bd30-4926-a8fc-d75e174dbb6b",
  "timestamp": "2026-05-20T04:02:22.807Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "## The LLM Annotation Multiverse: Specification Curve Analysis for Robust Computational Social Science  ### Motivation  LLM-based text annotation has become the default measurement instrument in compu…",
  "leafUuid": "6183da0a-bd30-4926-a8fc-d75e174dbb6b",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "LLM annotation robustness via specification curve analysis",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223"
}
```

---

### Assistant

_source line 8 · 2026-05-20T04:02:28.479Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this proposal as the 补救 agent (remediation agent), focusing exclusively on experimental design and technical execution completeness. I need to first do thorough literature research to understand the current experimental standards in this field before giving any suggestions.

Let me start by searching for relevant recent work on:
1. Specification curve analysis / multiverse analysis in NLP/CSS
2. LLM annotation robustness experimental designs
3. The specific papers mentioned and their experimental setups
4. Current baseline standards in this area
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6183da0a-bd30-4926-a8fc-d75e174dbb6b",
  "isSidechain": false,
  "requestId": "req_011CbD9yTAPKQ3yHnLWpsPem",
  "type": "assistant",
  "uuid": "d0de91c4-eaba-4b07-aaea-072a52af2621",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186giFvjWRTEtqwPwCFN9zj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6076,
      "cache_read_input_tokens": 14448,
      "output_tokens": 234,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6076,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 234,
          "cache_read_input_tokens": 14448,
          "cache_creation_input_tokens": 6076,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6076
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-20T04:02:29.542Z_

I need to first thoroughly research the experimental standards in this field before evaluating the proposal. Let me do targeted searches on the key methodological areas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0de91c4-eaba-4b07-aaea-072a52af2621",
  "isSidechain": false,
  "requestId": "req_011CbD9yTAPKQ3yHnLWpsPem",
  "type": "assistant",
  "uuid": "6d27ac0f-665f-410d-a233-25d934a9f874",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186giFvjWRTEtqwPwCFN9zj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6076,
      "cache_read_input_tokens": 14448,
      "output_tokens": 234,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6076,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 234,
          "cache_read_input_tokens": 14448,
          "cache_creation_input_tokens": 6076,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6076
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T04:02:29.892Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NSUvEEy3MdJU6AxWoNftei`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d27ac0f-665f-410d-a233-25d934a9f874",
  "isSidechain": false,
  "requestId": "req_011CbD9yTAPKQ3yHnLWpsPem",
  "type": "assistant",
  "uuid": "cd048c5a-becd-4e9f-b416-4b207afbbc71",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186giFvjWRTEtqwPwCFN9zj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6076,
      "cache_read_input_tokens": 14448,
      "output_tokens": 234,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6076,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 234,
          "cache_read_input_tokens": 14448,
          "cache_creation_input_tokens": 6076,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6076
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-20T04:02:29.898Z_

<details><summary>↩ Tool result · `toolu_01NSUvEEy3MdJU6AxWoNftei`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd048c5a-becd-4e9f-b416-4b207afbbc71",
  "isSidechain": false,
  "promptId": "73ab1a43-96b2-4654-a2b9-23d82346af16",
  "type": "user",
  "uuid": "e2a1a4f6-5c52-4c76-a7a0-01642fb81dc8",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "cd048c5a-becd-4e9f-b416-4b207afbbc71",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-20T04:02:33.062Z_

Now let me conduct my pre-assessment research. I'll search for the key papers and experimental standards in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2a1a4f6-5c52-4c76-a7a0-01642fb81dc8",
  "isSidechain": false,
  "requestId": "req_011CbD9yyNaFpWyvMJxSpmZJ",
  "type": "assistant",
  "uuid": "2f2dfbb5-05fd-4811-b937-9ef9743ed424",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YQuHoMNh8Bu4yzLfGX9Ac1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 760,
      "cache_read_input_tokens": 20524,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 760,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 106,
          "cache_read_input_tokens": 20524,
          "cache_creation_input_tokens": 760,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 760
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T04:02:33.565Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011gfyvwCtty5e8nnX2ENupM`</summary>

```json
{
  "query": "Baumann et al 2025 LLM hacking risk annotation arXiv 2509.08825 experimental design baselines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f2dfbb5-05fd-4811-b937-9ef9743ed424",
  "isSidechain": false,
  "requestId": "req_011CbD9yyNaFpWyvMJxSpmZJ",
  "type": "assistant",
  "uuid": "20482a62-31a1-4e07-8e90-15ab47879a44",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YQuHoMNh8Bu4yzLfGX9Ac1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 760,
      "cache_read_input_tokens": 20524,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 760,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 106,
          "cache_read_input_tokens": 20524,
          "cache_creation_input_tokens": 760,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 760
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T04:02:41.735Z_

<details><summary>↩ Tool result · `toolu_011gfyvwCtty5e8nnX2ENupM`</summary>

```text
Web search results for query: "Baumann et al 2025 LLM hacking risk annotation arXiv 2509.08825 experimental design baselines"

Links: [{"title":"[2509.08825] Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation","url":"https://arxiv.org/abs/2509.08825"},{"title":"[2509.08825v2] Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation","url":"https://arxiv.org/abs/2509.08825v2"},{"title":"Paper page - Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation","url":"https://huggingface.co/papers/2509.08825"},{"title":"LLM Hacking Risks in Text Annotation","url":"https://www.emergentmind.com/papers/2509.08825"},{"title":"Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation | Request PDF","url":"https://www.researchgate.net/publication/395402972_Large_Language_Model_Hacking_Quantifying_the_Hidden_Risks_of_Using_LLMs_for_Text_Annotation"},{"title":"Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation","url":"https://arxiv.org/html/2509.08825v1"},{"title":"Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs","url":"https://arxiv.org/pdf/2509.08825"},{"title":"Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation | Scilit","url":"https://www.scilit.com/publications/e01f55e0f27c068e1a51cfa94f8cb986"},{"title":"Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/large-language-model-hacking-quantifying-hidden-risks"},{"title":"Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2509.08825"}]

I found the paper you're looking for. Here's what I found about the Baumann et al. 2025 paper on LLM hacking risk in annotation:

## Paper Overview

The paper is authored by Joachim Baumann, Paul Röttger, Aleksandra Urman, Albert Wendsjö, Flor Miriam Plaza-del-Arco, Johannes B. Gruber, and Dirk Hovy, and was submitted to arXiv on September 10, 2025.

## Experimental Design and Findings

The study quantifies the risk of LLM hacking by replicating 37 data annotation tasks from 21 published social science research studies with 18 different models, analyzing 13 million LLM labels while testing 2,361 realistic hypotheses to measure how plausible researcher choices affect statistical conclusions.

The researchers found incorrect conclusions in approximately 31% of hypotheses for state-of-the-art LLMs, and in half the hypotheses for smaller language models.

## Key Results and Baselines

The analysis of 21 mitigation techniques found that human annotations provide crucial protection against false positives. Common regression estimator correction techniques can restore valid inference but trade off Type I versus Type II errors.

While higher task performance and stronger general model capabilities reduce LLM hacking risk, even highly accurate models remain susceptible. The risk of LLM hacking decreases as effect sizes increase, indicating the need for more rigorous verification of LLM-based findings near significance thresholds.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "20482a62-31a1-4e07-8e90-15ab47879a44",
  "isSidechain": false,
  "promptId": "73ab1a43-96b2-4654-a2b9-23d82346af16",
  "type": "user",
  "uuid": "41c7e205-9164-459c-805d-f8f8b76498ec",
  "toolUseResult": {
    "query": "Baumann et al 2025 LLM hacking risk annotation arXiv 2509.08825 experimental design baselines",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BiwVqFuqvr2kBs6EbFEo6f",
        "content": [
          {
            "title": "[2509.08825] Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation",
            "url": "https://arxiv.org/abs/2509.08825"
          },
          {
            "title": "[2509.08825v2] Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation",
            "url": "https://arxiv.org/abs/2509.08825v2"
          },
          {
            "title": "Paper page - Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation",
            "url": "https://huggingface.co/papers/2509.08825"
          },
          {
            "title": "LLM Hacking Risks in Text Annotation",
            "url": "https://www.emergentmind.com/papers/2509.08825"
          },
          {
            "title": "Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation | Request PDF",
            "url": "https://www.researchgate.net/publication/395402972_Large_Language_Model_Hacking_Quantifying_the_Hidden_Risks_of_Using_LLMs_for_Text_Annotation"
          },
          {
            "title": "Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation",
            "url": "https://arxiv.org/html/2509.08825v1"
          },
          {
            "title": "Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs",
            "url": "https://arxiv.org/pdf/2509.08825"
          },
          {
            "title": "Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation | Scilit",
            "url": "https://www.scilit.com/publications/e01f55e0f27c068e1a51cfa94f8cb986"
          },
          {
            "title": "Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/large-language-model-hacking-quantifying-hidden-risks"
          },
          {
            "title": "Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/arXiv:2509.08825"
          }
        ]
      },
      "I found the paper you're looking for. Here's what I found about the Baumann et al. 2025 paper on LLM hacking risk in annotation:\n\n## Paper Overview\n\nThe paper is authored by Joachim Baumann, Paul Röttger, Aleksandra Urman, Albert Wendsjö, Flor Miriam Plaza-del-Arco, Johannes B. Gruber, and Dirk Hovy, and was submitted to arXiv on September 10, 2025.\n\n## Experimental Design and Findings\n\nThe study quantifies the risk of LLM hacking by replicating 37 data annotation tasks from 21 published social science research studies with 18 different models, analyzing 13 million LLM labels while testing 2,361 realistic hypotheses to measure how plausible researcher choices affect statistical conclusions.\n\nThe researchers found incorrect conclusions in approximately 31% of hypotheses for state-of-the-art LLMs, and in half the hypotheses for smaller language models.\n\n## Key Results and Baselines\n\nThe analysis of 21 mitigation techniques found that human annotations provide crucial protection against false positives. Common regression estimator correction techniques can restore valid inference but trade off Type I versus Type II errors.\n\nWhile higher task performance and stronger general model capabilities reduce LLM hacking risk, even highly accurate models remain susceptible. The risk of LLM hacking decreases as effect sizes increase, indicating the need for more rigorous verification of LLM-based findings near significance thresholds."
    ],
    "durationSeconds": 8.142388951,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "20482a62-31a1-4e07-8e90-15ab47879a44",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T04:02:44.590Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VZ9TZihzAyRjXiTVjPAwDu`</summary>

```json
{
  "query": "Messing 2026 TEE corrected standard errors LLM pipeline variance arXiv 2604.11581"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41c7e205-9164-459c-805d-f8f8b76498ec",
  "isSidechain": false,
  "requestId": "req_011CbD9zqrQvcAHocVi5VBhW",
  "type": "assistant",
  "uuid": "3bcda89c-ef6e-4cbf-90a7-51c4784bd460",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CkNiCHfwd2ro16Nmp9t6Qu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1079,
      "cache_read_input_tokens": 21284,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1079,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 21284,
          "cache_creation_input_tokens": 1079,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1079
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T04:02:51.564Z_

<details><summary>↩ Tool result · `toolu_01VZ9TZihzAyRjXiTVjPAwDu`</summary>

```text
Web search results for query: "Messing 2026 TEE corrected standard errors LLM pipeline variance arXiv 2604.11581"

Links: [{"title":"Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking","url":"https://arxiv.org/html/2604.11581"},{"title":"[2604.11581] Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking","url":"https://arxiv.org/abs/2604.11581"},{"title":"Hidden Measurement Error in LLM Pipelines Distorts Annotation,","url":"https://arxiv.org/pdf/2604.11581"},{"title":"Variance-Aware LLM Annotation for Strategy Research: Sources, Diagnostics, and a Protocol for Reliable Measurement","url":"https://arxiv.org/pdf/2601.02370"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2602.10144"},{"title":"Assessing the feasibility and acceptability of a bespoke large language model pipeline to extract data from different study designs for public health evidence reviews","url":"https://www.medrxiv.org/content/10.1101/2025.07.21.25331917.full.pdf"}]

I found the paper you're looking for. Here are the key details:

**Paper Title:** "Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking" by Solomon Messing from New York University (arXiv:2604.11581)

**Main Contribution:** The paper decomposes LLM pipeline uncertainty into its sources, distinguishes variance that shrinks with more data from sensitivity to researcher design choices, and uses design-study projections to reduce total evaluation error (TEE).

**Key Findings:**

1. **Underestimated Standard Errors:** Naive standard errors are 40-60% smaller than the TEE-corrected standard errors.

2. **Coverage Problem:** Using Chatbot Arena data, naive 95% confidence interval coverage drops as n grows while TEE-corrected coverage holds at 95%.

3. **Sources of Variance:** Standard confidence intervals ignore variability from judge model choice, model temperature, and prompt phrasing, producing under-coverage that worsens with more data.

4. **Real-World Impact:** The omitted variance can shift results enough to reverse conclusions and leaves the surface that "benchmark hacking" exploits.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3bcda89c-ef6e-4cbf-90a7-51c4784bd460",
  "isSidechain": false,
  "promptId": "73ab1a43-96b2-4654-a2b9-23d82346af16",
  "type": "user",
  "uuid": "eb2cf594-504b-4a0d-8181-915231fe513a",
  "toolUseResult": {
    "query": "Messing 2026 TEE corrected standard errors LLM pipeline variance arXiv 2604.11581",
    "results": [
      {
        "tool_use_id": "srvtoolu_01K9MG7ix87nmVStjastZwtc",
        "content": [
          {
            "title": "Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking",
            "url": "https://arxiv.org/html/2604.11581"
          },
          {
            "title": "[2604.11581] Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking",
            "url": "https://arxiv.org/abs/2604.11581"
          },
          {
            "title": "Hidden Measurement Error in LLM Pipelines Distorts Annotation,",
            "url": "https://arxiv.org/pdf/2604.11581"
          },
          {
            "title": "Variance-Aware LLM Annotation for Strategy Research: Sources, Diagnostics, and a Protocol for Reliable Measurement",
            "url": "https://arxiv.org/pdf/2601.02370"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2602.10144"
          },
          {
            "title": "Assessing the feasibility and acceptability of a bespoke large language model pipeline to extract data from different study designs for public health evidence reviews",
            "url": "https://www.medrxiv.org/content/10.1101/2025.07.21.25331917.full.pdf"
          }
        ]
      },
      "I found the paper you're looking for. Here are the key details:\n\n**Paper Title:** \"Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking\" by Solomon Messing from New York University (arXiv:2604.11581)\n\n**Main Contribution:** The paper decomposes LLM pipeline uncertainty into its sources, distinguishes variance that shrinks with more data from sensitivity to researcher design choices, and uses design-study projections to reduce total evaluation error (TEE).\n\n**Key Findings:**\n\n1. **Underestimated Standard Errors:** Naive standard errors are 40-60% smaller than the TEE-corrected standard errors.\n\n2. **Coverage Problem:** Using Chatbot Arena data, naive 95% confidence interval coverage drops as n grows while TEE-corrected coverage holds at 95%.\n\n3. **Sources of Variance:** Standard confidence intervals ignore variability from judge model choice, model temperature, and prompt phrasing, producing under-coverage that worsens with more data.\n\n4. **Real-World Impact:** The omitted variance can shift results enough to reverse conclusions and leaves the surface that \"benchmark hacking\" exploits."
    ],
    "durationSeconds": 6.9703543419999985,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3bcda89c-ef6e-4cbf-90a7-51c4784bd460",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T04:02:53.990Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014FyzmKStzmmsADXnsJgV7y`</summary>

```json
{
  "query": "specification curve analysis multiverse NLP text annotation 2025 2026 experimental design"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb2cf594-504b-4a0d-8181-915231fe513a",
  "isSidechain": false,
  "requestId": "req_011CbDA1ZmKCGBMvG7sHNB3h",
  "type": "assistant",
  "uuid": "667bd090-ce83-4630-ac0e-0048abb9b319",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XwyQQGk7bo6CFCySmCrFYF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 711,
      "cache_read_input_tokens": 22363,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 711,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 22363,
          "cache_creation_input_tokens": 711,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 711
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T04:03:02.707Z_

<details><summary>↩ Tool result · `toolu_014FyzmKStzmmsADXnsJgV7y`</summary>

```text
Web search results for query: "specification curve analysis multiverse NLP text annotation 2025 2026 experimental design"

Links: [{"title":"Specification Curve Analysis | FORRT - Framework for Open and Reproducible Research Training","url":"https://forrt.org/glossary/english/specification_curve_analysis/"},{"title":"POST-SELECTION INFERENCE IN MULTIVERSE ANALYSIS (PIMA):","url":"https://arxiv.org/pdf/2210.02794"},{"title":"Specification curve analysis | Semantic Scholar","url":"https://www.semanticscholar.org/paper/0a6f39bad41608b86673b6226f2893912b27a72c"},{"title":"42.2 Specification Curve Analysis | A Guide on Data Analysis","url":"https://bookdown.org/mike/data_analysis/specification-curve-analysis.html"},{"title":"Specification curve analysis and the multiverse | Statistical Modeling, Causal Inference, and Social Science","url":"https://statmodeling.stat.columbia.edu/2024/11/12/specification-curve-analysis-and-the-multiverse/"},{"title":"Into the (Bayesian) Multiverse!","url":"https://pab2163.github.io/amygdala_mpfc_multiverse/into_the_bayesian_multiverse.html"},{"title":"Conducting and Visualizing Specification Curve Analyses • specr","url":"https://masurp.github.io/specr/"},{"title":"Visualizing vastness: Graphical methods for multiverse analysis","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12875576/"}]

Based on the search results, here's what I found about specification curve analysis and multiverse analysis:

## Overview

Specification curve analysis (also known as multiverse analysis) provides a systematic way to examine how results vary across a large set of defensible specifications. It helps make transparent the influence of presumably arbitrary decisions during scientific progress such as experimental design, construct operationalization, and statistical models made by researchers by comprehensively reporting all non-redundant, sensible tests of the research question.

## Key Methodology

Specification curve analysis consists of three steps: (1) identifying the set of theoretically justified, statistically valid and non-redundant specifications; (2) displaying the results graphically, allowing readers to identify consequential specifications decisions; and (3) conducting joint inference across all specifications.

Rather than reporting a single "preferred" specification, this approach acknowledges that multiple specifications may be equally justifiable and examines the distribution of estimates across all of them.

## Relationship to Multiverse Analysis

Specification curve analysis differs from multiverse analysis with regards to the graphical displays (a specification curve plot rather than a histogram and tile plot) and the use of inferential statistics to interpret findings.

## Visualization Challenges

Specification curves face a fundamental limitation in that they do not scale well; while the number of multiverse specifications grows exponentially, specification curves typically max out at around 200 to 300 estimates before the decision dashboard collapses into visual "fuzz."

**Note:** The search results did not return specific recent papers (2025-2026) focused on applying these methods to NLP text annotation tasks. The results provide general information about specification curve and multiverse analysis methodologies across disciplines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "667bd090-ce83-4630-ac0e-0048abb9b319",
  "isSidechain": false,
  "promptId": "73ab1a43-96b2-4654-a2b9-23d82346af16",
  "type": "user",
  "uuid": "4494c1f7-b67f-4610-8f61-39dec177441e",
  "toolUseResult": {
    "query": "specification curve analysis multiverse NLP text annotation 2025 2026 experimental design",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QeXAsD75riYQWfGMimriH8",
        "content": [
          {
            "title": "Specification Curve Analysis | FORRT - Framework for Open and Reproducible Research Training",
            "url": "https://forrt.org/glossary/english/specification_curve_analysis/"
          },
          {
            "title": "POST-SELECTION INFERENCE IN MULTIVERSE ANALYSIS (PIMA):",
            "url": "https://arxiv.org/pdf/2210.02794"
          },
          {
            "title": "Specification curve analysis | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/0a6f39bad41608b86673b6226f2893912b27a72c"
          },
          {
            "title": "42.2 Specification Curve Analysis | A Guide on Data Analysis",
            "url": "https://bookdown.org/mike/data_analysis/specification-curve-analysis.html"
          },
          {
            "title": "Specification curve analysis and the multiverse | Statistical Modeling, Causal Inference, and Social Science",
            "url": "https://statmodeling.stat.columbia.edu/2024/11/12/specification-curve-analysis-and-the-multiverse/"
          },
          {
            "title": "Into the (Bayesian) Multiverse!",
            "url": "https://pab2163.github.io/amygdala_mpfc_multiverse/into_the_bayesian_multiverse.html"
          },
          {
            "title": "Conducting and Visualizing Specification Curve Analyses • specr",
            "url": "https://masurp.github.io/specr/"
          },
          {
            "title": "Visualizing vastness: Graphical methods for multiverse analysis",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12875576/"
          }
        ]
      },
      "Based on the search results, here's what I found about specification curve analysis and multiverse analysis:\n\n## Overview\n\nSpecification curve analysis (also known as multiverse analysis) provides a systematic way to examine how results vary across a large set of defensible specifications. It helps make transparent the influence of presumably arbitrary decisions during scientific progress such as experimental design, construct operationalization, and statistical models made by researchers by comprehensively reporting all non-redundant, sensible tests of the research question.\n\n## Key Methodology\n\nSpecification curve analysis consists of three steps: (1) identifying the set of theoretically justified, statistically valid and non-redundant specifications; (2) displaying the results graphically, allowing readers to identify consequential specifications decisions; and (3) conducting joint inference across all specifications.\n\nRather than reporting a single \"preferred\" specification, this approach acknowledges that multiple specifications may be equally justifiable and examines the distribution of estimates across all of them.\n\n## Relationship to Multiverse Analysis\n\nSpecification curve analysis differs from multiverse analysis with regards to the graphical displays (a specification curve plot rather than a histogram and tile plot) and the use of inferential statistics to interpret findings.\n\n## Visualization Challenges\n\nSpecification curves face a fundamental limitation in that they do not scale well; while the number of multiverse specifications grows exponentially, specification curves typically max out at around 200 to 300 estimates before the decision dashboard collapses into visual \"fuzz.\"\n\n**Note:** The search results did not return specific recent papers (2025-2026) focused on applying these methods to NLP text annotation tasks. The results provide general information about specification curve and multiverse analysis methodologies across disciplines."
    ],
    "durationSeconds": 8.713341760000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "667bd090-ce83-4630-ac0e-0048abb9b319",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T04:03:05.314Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013wHFgzCQjmX6guppbZsfCN`</summary>

```json
{
  "query": "Gligoric prediction powered inference LLM annotation NAACL 2025 CDI experimental evaluation baselines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4494c1f7-b67f-4610-8f61-39dec177441e",
  "isSidechain": false,
  "requestId": "req_011CbDA2PRFG4zvrEBh2u7z3",
  "type": "assistant",
  "uuid": "5b7e5afa-a180-4fb6-8d86-c2ca0b03de8f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P5cgBcNcE2S324yBTsHQ7S",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 865,
      "cache_read_input_tokens": 23074,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 865,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 23074,
          "cache_creation_input_tokens": 865,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 865
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "## The LLM Annotation Multiverse: Specification Curve Analysis for Robust Computational Social Science  ### Motivation  LLM-based text annotation has become the default measurement instrument in compu…",
  "leafUuid": "5b7e5afa-a180-4fb6-8d86-c2ca0b03de8f",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "LLM annotation robustness via specification curve analysis",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223"
}
```

---

### Tool result

_source line 22 · 2026-05-20T04:03:13.199Z_

<details><summary>↩ Tool result · `toolu_013wHFgzCQjmX6guppbZsfCN`</summary>

```text
Web search results for query: "Gligoric prediction powered inference LLM annotation NAACL 2025 CDI experimental evaluation baselines"

Links: [{"title":"GitHub - kristinagligoric/cdi-tutorial","url":"https://github.com/kristinagligoric/cdi-tutorial"},{"title":"Can Unconfident LLM Annotations Be Used for Confident Conclusions? - ACL Anthology","url":"https://aclanthology.org/2025.naacl-long.179/"},{"title":"Accepted Papers - NAACL-HLT 2025","url":"https://2025.naacl.org/program/accepted_papers/"},{"title":"PLD+: Accelerating LLM Inference by Leveraging ...","url":"https://aclanthology.org/2025.findings-naacl.338.pdf"},{"title":"[Literature Review] Can Unconfident LLM Annotations Be Used for Confident Conclusions?","url":"https://www.themoonlight.io/en/review/can-unconfident-llm-annotations-be-used-for-confident-conclusions"},{"title":"Multi-Perspective LLM Annotations for Valid Analyses in Subjective Tasks","url":"https://arxiv.org/pdf/2603.21404"},{"title":"Do More Predictions Improve Statistical Inference? Filtered Prediction-Powered Inference","url":"https://arxiv.org/pdf/2602.10464"}]

Based on the search results, I found relevant information about Gligoric's work on Confidence-Driven Inference (CDI) and LLM annotations at NAACL 2025:

## Main Research

Kristina Gligorić, Tijana Zrnic, Cinoo Lee, Emmanuel Candès, and Dan Jurafsky published "Can Unconfident LLM Annotations Be Used for Confident Conclusions?" at NAACL 2025.

## Core Methodology

The research presents an end-to-end, automated human-AI annotation pipeline based on Confidence-Driven Inference (CDI). The CDI methodology aims at effectively leveraging annotations generated by large language models for statistical estimation in computational social science research, proposing a way to combine LLM annotations with human annotations while ensuring valid statistical inference and maintaining confidence intervals.

## Experimental Evaluation

The researchers demonstrated the effectiveness of Confidence-driven inference over baselines in statistical estimation tasks across three computational social science settings—text politeness, stance, and bias—reducing the needed number of human annotations by over 25% in each.

The work also includes obtaining cheap-but-noisy labels from an LLM together with its confidence scores and iteratively sampling the most informative texts for additional human annotation using the CDI sampling rule.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5b7e5afa-a180-4fb6-8d86-c2ca0b03de8f",
  "isSidechain": false,
  "promptId": "73ab1a43-96b2-4654-a2b9-23d82346af16",
  "type": "user",
  "uuid": "65f4edb7-964f-407d-9464-7249162ff031",
  "toolUseResult": {
    "query": "Gligoric prediction powered inference LLM annotation NAACL 2025 CDI experimental evaluation baselines",
    "results": [
      {
        "tool_use_id": "srvtoolu_019AKDoKYQwc1VTyiN56BNAQ",
        "content": [
          {
            "title": "GitHub - kristinagligoric/cdi-tutorial",
            "url": "https://github.com/kristinagligoric/cdi-tutorial"
          },
          {
            "title": "Can Unconfident LLM Annotations Be Used for Confident Conclusions? - ACL Anthology",
            "url": "https://aclanthology.org/2025.naacl-long.179/"
          },
          {
            "title": "Accepted Papers - NAACL-HLT 2025",
            "url": "https://2025.naacl.org/program/accepted_papers/"
          },
          {
            "title": "PLD+: Accelerating LLM Inference by Leveraging ...",
            "url": "https://aclanthology.org/2025.findings-naacl.338.pdf"
          },
          {
            "title": "[Literature Review] Can Unconfident LLM Annotations Be Used for Confident Conclusions?",
            "url": "https://www.themoonlight.io/en/review/can-unconfident-llm-annotations-be-used-for-confident-conclusions"
          },
          {
            "title": "Multi-Perspective LLM Annotations for Valid Analyses in Subjective Tasks",
            "url": "https://arxiv.org/pdf/2603.21404"
          },
          {
            "title": "Do More Predictions Improve Statistical Inference? Filtered Prediction-Powered Inference",
            "url": "https://arxiv.org/pdf/2602.10464"
          }
        ]
      },
      "Based on the search results, I found relevant information about Gligoric's work on Confidence-Driven Inference (CDI) and LLM annotations at NAACL 2025:\n\n## Main Research\n\nKristina Gligorić, Tijana Zrnic, Cinoo Lee, Emmanuel Candès, and Dan Jurafsky published \"Can Unconfident LLM Annotations Be Used for Confident Conclusions?\" at NAACL 2025.\n\n## Core Methodology\n\nThe research presents an end-to-end, automated human-AI annotation pipeline based on Confidence-Driven Inference (CDI). The CDI methodology aims at effectively leveraging annotations generated by large language models for statistical estimation in computational social science research, proposing a way to combine LLM annotations with human annotations while ensuring valid statistical inference and maintaining confidence intervals.\n\n## Experimental Evaluation\n\nThe researchers demonstrated the effectiveness of Confidence-driven inference over baselines in statistical estimation tasks across three computational social science settings—text politeness, stance, and bias—reducing the needed number of human annotations by over 25% in each.\n\nThe work also includes obtaining cheap-but-noisy labels from an LLM together with its confidence scores and iteratively sampling the most informative texts for additional human annotation using the CDI sampling rule."
    ],
    "durationSeconds": 7.880498594000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5b7e5afa-a180-4fb6-8d86-c2ca0b03de8f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T04:03:15.998Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017WH7wRVyiSuzwDu4agVt8B`</summary>

```json
{
  "query": "McLaren et al 2026 arXiv 2603.26898 interaction effects LLM annotation pipeline political science"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65f4edb7-964f-407d-9464-7249162ff031",
  "isSidechain": false,
  "requestId": "req_011CbDA3AJEiLeKJEaGJZGoW",
  "type": "assistant",
  "uuid": "bcfaa19c-5d39-4154-80d8-0792485f4185",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SE3wLgQrZgdRdusdewa8Po",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 750,
      "cache_read_input_tokens": 23939,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 750,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 23939,
          "cache_creation_input_tokens": 750,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 750
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T04:03:22.586Z_

<details><summary>↩ Tool result · `toolu_017WH7wRVyiSuzwDu4agVt8B`</summary>

```text
Web search results for query: "McLaren et al 2026 arXiv 2603.26898 interaction effects LLM annotation pipeline political science"

Links: [{"title":"[2603.26898] Magic Words or Methodical Work? Challenging Conventional Wisdom in LLM-Based Political Text Annotation","url":"https://arxiv.org/abs/2603.26898"},{"title":"Magic Words or Methodical Work? Challenging Conventional Wisdom in LLM-Based Political Text Annotation","url":"https://arxiv.org/html/2603.26898"},{"title":"Bias in LLMs as Annotators: The Effect of Party Cues on Labelling   Decision by Large Language Models","url":"https://arxiv.org/pdf/2408.15895"},{"title":"Hidden Persuaders: LLMs' Political Leaning and Their Influence on Voters","url":"https://arxiv.org/pdf/2410.24190"},{"title":"Biased AI can Influence Political Decision-Making","url":"https://arxiv.org/pdf/2410.06415"},{"title":"Learning Through Dialogue: Engagement and Efficacy Matter More Than Explanations","url":"https://arxiv.org/pdf/2601.07796"},{"title":"Just Put a Human in the Loop? Investigating LLM-Assisted Annotation for Subjective Tasks","url":"https://arxiv.org/pdf/2507.15821"},{"title":"Fact or Fiction? Can LLMs be Reliable Annotators for Political Truths?","url":"https://arxiv.org/pdf/2411.05775"}]

Perfect! I found the paper you're looking for. Here are the details:

The paper is titled "Magic Words or Methodical Work? Challenging Conventional Wisdom in LLM-Based Political Text Annotation" by Lorca McLaren, James Cross, Zuzanna Krakowska, Robin Rauner, and Martijn Schoonvelde (arXiv:2603.26898), submitted on March 27, 2026.

**Key Findings:**

The central methodological finding is that interaction effects dominate main effects, so seemingly reasonable pipeline choices can become consequential researcher degrees of freedom. No single model, prompt style, or learning approach is uniformly superior, and the best-performing model varies across tasks.

**Methodology:**

The authors address that political scientists are rapidly adopting LLMs for text annotation yet the sensitivity of annotation results to implementation choices remains poorly understood. They present a controlled evaluation of pipeline choices, testing six open-weight models across four political science annotation tasks under identical quantisation, hardware, and prompt-template conditions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bcfaa19c-5d39-4154-80d8-0792485f4185",
  "isSidechain": false,
  "promptId": "73ab1a43-96b2-4654-a2b9-23d82346af16",
  "type": "user",
  "uuid": "ef58e717-8a42-437b-bd83-0f8baeb4d58f",
  "toolUseResult": {
    "query": "McLaren et al 2026 arXiv 2603.26898 interaction effects LLM annotation pipeline political science",
    "results": [
      {
        "tool_use_id": "srvtoolu_011kYUrJ67RNTTLuLmbJLZiq",
        "content": [
          {
            "title": "[2603.26898] Magic Words or Methodical Work? Challenging Conventional Wisdom in LLM-Based Political Text Annotation",
            "url": "https://arxiv.org/abs/2603.26898"
          },
          {
            "title": "Magic Words or Methodical Work? Challenging Conventional Wisdom in LLM-Based Political Text Annotation",
            "url": "https://arxiv.org/html/2603.26898"
          },
          {
            "title": "Bias in LLMs as Annotators: The Effect of Party Cues on Labelling   Decision by Large Language Models",
            "url": "https://arxiv.org/pdf/2408.15895"
          },
          {
            "title": "Hidden Persuaders: LLMs' Political Leaning and Their Influence on Voters",
            "url": "https://arxiv.org/pdf/2410.24190"
          },
          {
            "title": "Biased AI can Influence Political Decision-Making",
            "url": "https://arxiv.org/pdf/2410.06415"
          },
          {
            "title": "Learning Through Dialogue: Engagement and Efficacy Matter More Than Explanations",
            "url": "https://arxiv.org/pdf/2601.07796"
          },
          {
            "title": "Just Put a Human in the Loop? Investigating LLM-Assisted Annotation for Subjective Tasks",
            "url": "https://arxiv.org/pdf/2507.15821"
          },
          {
            "title": "Fact or Fiction? Can LLMs be Reliable Annotators for Political Truths?",
            "url": "https://arxiv.org/pdf/2411.05775"
          }
        ]
      },
      "Perfect! I found the paper you're looking for. Here are the details:\n\nThe paper is titled \"Magic Words or Methodical Work? Challenging Conventional Wisdom in LLM-Based Political Text Annotation\" by Lorca McLaren, James Cross, Zuzanna Krakowska, Robin Rauner, and Martijn Schoonvelde (arXiv:2603.26898), submitted on March 27, 2026.\n\n**Key Findings:**\n\nThe central methodological finding is that interaction effects dominate main effects, so seemingly reasonable pipeline choices can become consequential researcher degrees of freedom. No single model, prompt style, or learning approach is uniformly superior, and the best-performing model varies across tasks.\n\n**Methodology:**\n\nThe authors address that political scientists are rapidly adopting LLMs for text annotation yet the sensitivity of annotation results to implementation choices remains poorly understood. They present a controlled evaluation of pipeline choices, testing six open-weight models across four political science annotation tasks under identical quantisation, hardware, and prompt-template conditions."
    ],
    "durationSeconds": 6.583604736000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bcfaa19c-5d39-4154-80d8-0792485f4185",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T04:03:25.694Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0126Wui16UPXybJQQeaYGwta`</summary>

```json
{
  "query": "Audinet de Pieuchon EMNLP 2025 DSL PPI benchmark LLM annotation correction experimental design"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef58e717-8a42-437b-bd83-0f8baeb4d58f",
  "isSidechain": false,
  "requestId": "req_011CbDA3rPFai1wCs7rHDybN",
  "type": "assistant",
  "uuid": "234cce77-4a18-47eb-b35f-db93bfa467b6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019BJYHo3zcw3DoLoyiPfTYz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 726,
      "cache_read_input_tokens": 24689,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 726,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 24689,
          "cache_creation_input_tokens": 726,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 726
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T04:03:34.138Z_

<details><summary>↩ Tool result · `toolu_0126Wui16UPXybJQQeaYGwta`</summary>

```text
Web search results for query: "Audinet de Pieuchon EMNLP 2025 DSL PPI benchmark LLM annotation correction experimental design"

Links: [{"title":"Benchmarking Debiasing Methods for LLM-based Parameter Estimates","url":"https://arxiv.org/pdf/2506.09627"},{"title":"Benchmarking Debiasing Methods for LLM-based ...","url":"https://aclanthology.org/2025.emnlp-main.1000.pdf"},{"title":"Transcript - \"Benchmarking Debiasing Methods for LLM-based Parameter Estimates\" - Connor T. Jerzak","url":"https://connorjerzak.com/transcript-benchmarking-debiasing-methods/"},{"title":"(PDF) Benchmarking Debiasing Methods for LLM-based Parameter Estimates","url":"https://www.researchgate.net/publication/397421052_Benchmarking_Debiasing_Methods_for_LLM-based_Parameter_Estimates"},{"title":"Benchmarking Debiasing Methods for LLM-based Parameter Estimates - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1000/"},{"title":"Benchmarking Debiasing Methods for LLM-based Parameter Estimates - Connor T. Jerzak","url":"https://connorjerzak.com/benchmarking-ppi-dsl/"}]

Based on the search results, I found relevant information about the paper you're looking for. Here's what I found:

## Paper Overview

Nicolas Audinet de Pieuchon, Adel Daoud, Connor Thomas Jerzak, Moa Johansson, and Richard Johansson published "Benchmarking Debiasing Methods for LLM-based Parameter Estimates" in the Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (pages 19757–19772, Suzhou, China).

## Research Focus

The paper addresses how large language models (LLMs) offer an inexpensive way to annotate text but are often inconsistent when compared with experts, and these errors can bias downstream estimates of population parameters such as regression coefficients and causal effects.

## Experimental Design

The paper includes multiple experiments:

- Experiment 1 features a fixed N total samples with LLM annotations while varying n expert annotations for debiasing
- Experiment 2 varies the total number of samples while keeping the number of expert annotations fixed, targeting scenarios where the expert annotation budget is limited but unlabeled data is abundant

## Debiasing Methods

The paper compares Prediction-Powered Inference (PPI) and Design-based Supervised Learning (DSL) approaches for debiasing LLM annotations.

## Key Findings

The findings indicate that there is a bias-variance tradeoff at the level of debiasing methods, calling for more research on developing metrics for quantifying their efficiency in finite samples.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "234cce77-4a18-47eb-b35f-db93bfa467b6",
  "isSidechain": false,
  "promptId": "73ab1a43-96b2-4654-a2b9-23d82346af16",
  "type": "user",
  "uuid": "f3354ef0-d09c-4436-a555-27c16003fdb2",
  "toolUseResult": {
    "query": "Audinet de Pieuchon EMNLP 2025 DSL PPI benchmark LLM annotation correction experimental design",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JDxyrsBuyW5qpRCbbkDKhx",
        "content": [
          {
            "title": "Benchmarking Debiasing Methods for LLM-based Parameter Estimates",
            "url": "https://arxiv.org/pdf/2506.09627"
          },
          {
            "title": "Benchmarking Debiasing Methods for LLM-based ...",
            "url": "https://aclanthology.org/2025.emnlp-main.1000.pdf"
          },
          {
            "title": "Transcript - \"Benchmarking Debiasing Methods for LLM-based Parameter Estimates\" - Connor T. Jerzak",
            "url": "https://connorjerzak.com/transcript-benchmarking-debiasing-methods/"
          },
          {
            "title": "(PDF) Benchmarking Debiasing Methods for LLM-based Parameter Estimates",
            "url": "https://www.researchgate.net/publication/397421052_Benchmarking_Debiasing_Methods_for_LLM-based_Parameter_Estimates"
          },
          {
            "title": "Benchmarking Debiasing Methods for LLM-based Parameter Estimates - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.1000/"
          },
          {
            "title": "Benchmarking Debiasing Methods for LLM-based Parameter Estimates - Connor T. Jerzak",
            "url": "https://connorjerzak.com/benchmarking-ppi-dsl/"
          }
        ]
      },
      "Based on the search results, I found relevant information about the paper you're looking for. Here's what I found:\n\n## Paper Overview\n\nNicolas Audinet de Pieuchon, Adel Daoud, Connor Thomas Jerzak, Moa Johansson, and Richard Johansson published \"Benchmarking Debiasing Methods for LLM-based Parameter Estimates\" in the Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (pages 19757–19772, Suzhou, China).\n\n## Research Focus\n\nThe paper addresses how large language models (LLMs) offer an inexpensive way to annotate text but are often inconsistent when compared with experts, and these errors can bias downstream estimates of population parameters such as regression coefficients and causal effects.\n\n## Experimental Design\n\nThe paper includes multiple experiments:\n\n- Experiment 1 features a fixed N total samples with LLM annotations while varying n expert annotations for debiasing\n- Experiment 2 varies the total number of samples while keeping the number of expert annotations fixed, targeting scenarios where the expert annotation budget is limited but unlabeled data is abundant\n\n## Debiasing Methods\n\nThe paper compares Prediction-Powered Inference (PPI) and Design-based Supervised Learning (DSL) approaches for debiasing LLM annotations.\n\n## Key Findings\n\nThe findings indicate that there is a bias-variance tradeoff at the level of debiasing methods, calling for more research on developing metrics for quantifying their efficiency in finite samples."
    ],
    "durationSeconds": 8.438701071000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "234cce77-4a18-47eb-b35f-db93bfa467b6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T04:03:38.166Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VPmSBEhKBQ3XQyWrxD3jcw`</summary>

```json
{
  "query": "Boba specification DSL multiverse analysis Liu CHI 2021 executable specification"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3354ef0-d09c-4436-a555-27c16003fdb2",
  "isSidechain": false,
  "requestId": "req_011CbDA4ihAkSCAzAnuHTxAv",
  "type": "assistant",
  "uuid": "bb6d47a5-e93e-4715-976e-0a41ea8f98b9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TAxo5hfU2XWmtzTjUx42XL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 819,
      "cache_read_input_tokens": 25415,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 819,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 25415,
          "cache_creation_input_tokens": 819,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 819
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T04:03:45.362Z_

<details><summary>↩ Tool result · `toolu_01VPmSBEhKBQ3XQyWrxD3jcw`</summary>

```text
Web search results for query: "Boba specification DSL multiverse analysis Liu CHI 2021 executable specification"

Links: [{"title":"Boba: Authoring and Visualizing Multiverse Analyses","url":"https://idl.uw.edu/papers/boba"},{"title":"Boba: Authoring and Visualizing Multiverse Analyses","url":"https://idl.cs.washington.edu/files/2021-BobaMultiverse-VAST.pdf"},{"title":"Boba: Authoring and Visualizing Multiverse Analyses - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/33027002/"},{"title":"Boba: Authoring and Visualizing Multiverse Analyses","url":"https://arxiv.org/pdf/2007.05551"},{"title":"GitHub - uwdata/boba: Specifying and executing multiverse analysis · GitHub","url":"https://github.com/uwdata/boba"},{"title":"boba · PyPI","url":"https://pypi.org/project/boba/"},{"title":"[PDF] Boba: Authoring and Visualizing Multiverse Analyses | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Boba:-Authoring-and-Visualizing-Multiverse-Analyses-Liu-Kale/8498baead9ea8dc2bce5eec95dd357c62ed968d3"},{"title":"Boba: Authoring and Visualizing Multiverse Analyses | Request PDF","url":"https://www.researchgate.net/publication/345996760_Boba_Authoring_and_Visualizing_Multiverse_Analyses"},{"title":"Multiverse Analyses of Fear Acquisition and Extinction Retention in Posttraumatic Stress Disorder - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10330173/"}]

Based on the search results, I found comprehensive information about Boba:

## Boba: Authoring and Visualizing Multiverse Analyses

Boba is an integrated domain-specific language (DSL) and visual analysis system for authoring and reviewing multiverse analyses. The research was conducted by Yang Liu, Alex Kale, Tim Althoff, and Jeffrey Heer, and published in IEEE Transactions on Visualization and Computer Graphics in February 2021.

### Key Functionality

With the Boba DSL, analysts write the shared portion of analysis code only once, alongside local variations defining alternative decisions, from which the compiler generates a multiplex of scripts representing all possible analysis paths.

Multiverse analysis is an approach to data analysis in which all "reasonable" analytic decisions are evaluated in parallel and interpreted collectively, in order to foster robustness and transparency. However, specifying a multiverse is demanding because analysts must manage myriad variants from a cross-product of analytic decisions, and the results require nuanced interpretation.

### Implementation

Boba comes with a command line tool to parse your DSL specification and generate universe scripts, execute all scripts with a single command, merges outputs into a table, and invoke the visualizer. Boba has a domain specific language (Boba DSL) for writing multiverse specifications, and a visual analysis interface (Boba Visualizer) for exploring multiverse outcomes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb6d47a5-e93e-4715-976e-0a41ea8f98b9",
  "isSidechain": false,
  "promptId": "73ab1a43-96b2-4654-a2b9-23d82346af16",
  "type": "user",
  "uuid": "711f70f1-8984-41d8-bbdf-4f2af382e040",
  "toolUseResult": {
    "query": "Boba specification DSL multiverse analysis Liu CHI 2021 executable specification",
    "results": [
      {
        "tool_use_id": "srvtoolu_018K2cKFsCLi1WeQFZ3Cmusn",
        "content": [
          {
            "title": "Boba: Authoring and Visualizing Multiverse Analyses",
            "url": "https://idl.uw.edu/papers/boba"
          },
          {
            "title": "Boba: Authoring and Visualizing Multiverse Analyses",
            "url": "https://idl.cs.washington.edu/files/2021-BobaMultiverse-VAST.pdf"
          },
          {
            "title": "Boba: Authoring and Visualizing Multiverse Analyses - PubMed",
            "url": "https://pubmed.ncbi.nlm.nih.gov/33027002/"
          },
          {
            "title": "Boba: Authoring and Visualizing Multiverse Analyses",
            "url": "https://arxiv.org/pdf/2007.05551"
          },
          {
            "title": "GitHub - uwdata/boba: Specifying and executing multiverse analysis · GitHub",
            "url": "https://github.com/uwdata/boba"
          },
          {
            "title": "boba · PyPI",
            "url": "https://pypi.org/project/boba/"
          },
          {
            "title": "[PDF] Boba: Authoring and Visualizing Multiverse Analyses | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Boba:-Authoring-and-Visualizing-Multiverse-Analyses-Liu-Kale/8498baead9ea8dc2bce5eec95dd357c62ed968d3"
          },
          {
            "title": "Boba: Authoring and Visualizing Multiverse Analyses | Request PDF",
            "url": "https://www.researchgate.net/publication/345996760_Boba_Authoring_and_Visualizing_Multiverse_Analyses"
          },
          {
            "title": "Multiverse Analyses of Fear Acquisition and Extinction Retention in Posttraumatic Stress Disorder - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10330173/"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about Boba:\n\n## Boba: Authoring and Visualizing Multiverse Analyses\n\nBoba is an integrated domain-specific language (DSL) and visual analysis system for authoring and reviewing multiverse analyses. The research was conducted by Yang Liu, Alex Kale, Tim Althoff, and Jeffrey Heer, and published in IEEE Transactions on Visualization and Computer Graphics in February 2021.\n\n### Key Functionality\n\nWith the Boba DSL, analysts write the shared portion of analysis code only once, alongside local variations defining alternative decisions, from which the compiler generates a multiplex of scripts representing all possible analysis paths.\n\nMultiverse analysis is an approach to data analysis in which all \"reasonable\" analytic decisions are evaluated in parallel and interpreted collectively, in order to foster robustness and transparency. However, specifying a multiverse is demanding because analysts must manage myriad variants from a cross-product of analytic decisions, and the results require nuanced interpretation.\n\n### Implementation\n\nBoba comes with a command line tool to parse your DSL specification and generate universe scripts, execute all scripts with a single command, merges outputs into a table, and invoke the visualizer. Boba has a domain specific language (Boba DSL) for writing multiverse specifications, and a visual analysis interface (Boba Visualizer) for exploring multiverse outcomes."
    ],
    "durationSeconds": 7.191967554999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bb6d47a5-e93e-4715-976e-0a41ea8f98b9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-20T04:03:45.365Z_

```json
{
  "parentUuid": "711f70f1-8984-41d8-bbdf-4f2af382e040",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "c81d74b1-7f0c-4358-a9a4-49c3bbe5304c",
  "timestamp": "2026-05-20T04:03:45.365Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-20T04:03:48.148Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019GSy7doAvjsMoVpwtY7aDV`</summary>

```json
{
  "query": "Egami DSL design-based supervised learning NeurIPS 2023 LLM annotation debiasing experimental setup"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c81d74b1-7f0c-4358-a9a4-49c3bbe5304c",
  "isSidechain": false,
  "requestId": "req_011CbDA5XncJvsHJwmhJ2ciQ",
  "type": "assistant",
  "uuid": "84eb9dfe-960a-4385-ad67-29bf46564625",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DLBvKg2wKS4S77y83151Rh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 987,
      "cache_read_input_tokens": 26234,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 987,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 26234,
          "cache_creation_input_tokens": 987,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 987
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-20T04:03:56.054Z_

<details><summary>↩ Tool result · `toolu_019GSy7doAvjsMoVpwtY7aDV`</summary>

```text
Web search results for query: "Egami DSL design-based supervised learning NeurIPS 2023 LLM annotation debiasing experimental setup"

Links: [{"title":"Using Imperfect Surrogates for Downstream Inference: Design-based Supervised Learning for Social Science Applications of Large Language Models","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/d862f7f5445255090de13b825b880d59-Abstract-Conference.html"},{"title":"Design-based Supervised Learning • dsl","url":"http://naokiegami.com/dsl/"},{"title":"[2306.04746] Using Imperfect Surrogates for Downstream Inference: Design-based Supervised Learning for Social Science Applications of Large Language Models","url":"https://arxiv.org/abs/2306.04746"},{"title":"Get Started with dsl • dsl","url":"http://naokiegami.com/dsl/articles/intro.html"},{"title":"Using Imperfect Surrogates for Downstream Inference:","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/d862f7f5445255090de13b825b880d59-Paper-Conference.pdf"},{"title":"Benchmarking Debiasing Methods for LLM-based Parameter Estimates","url":"https://arxiv.org/html/2506.09627"},{"title":"Benchmarking Debiasing Methods for LLM-based ...","url":"https://aclanthology.org/2025.emnlp-main.1000.pdf"},{"title":"Using Large Language Model Annotations for the Social Sciences:","url":"https://naokiegami.com/paper/dsl_ss.pdf"},{"title":"Using Imperfect Surrogates for Downstream Inference: Design-based Supervised Learning for Social Science Applications of Large Language Models - Princeton University","url":"https://collaborate.princeton.edu/en/publications/using-imperfect-surrogates-for-downstream-inference-design-based-/"}]

Based on the search results, here's information about the Egami DSL work at NeurIPS 2023:

## Overview

Naoki Egami, Musashi Hinck, Brandon Stewart, and Hanying Wei presented their work at the Advances in Neural Information Processing Systems 36 (NeurIPS 2023) Main Conference Track.

## Research Problem

In computational social science, researchers analyze documents to explain social and political phenomena, first obtaining labels for documents and then explaining labels using interpretable regression analyses. While LLMs provide a common way to annotate documents cheaply at scale, such surrogate labels are often imperfect and biased.

## Key Findings

Direct use of surrogate labels in downstream statistical analyses leads to substantial bias and invalid confidence intervals, even with high surrogate accuracy of 80-90%.

## The DSL Method

To address this, the authors proposed the design-based supervised learning (DSL) estimator, which employs a doubly-robust procedure to combine surrogate labels with a smaller number of high-quality, gold-standard labels. The approach guarantees valid inference for downstream statistical analyses, even when surrogates are arbitrarily biased, by controlling the probability of sampling documents for gold-standard labeling.

## Experimental Setup

DSL combines large-scale (potentially biased) automated annotations and a smaller number of high-quality expensive expert annotations using a doubly robust bias-correction step.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84eb9dfe-960a-4385-ad67-29bf46564625",
  "isSidechain": false,
  "promptId": "73ab1a43-96b2-4654-a2b9-23d82346af16",
  "type": "user",
  "uuid": "6545f05a-f252-418c-b009-a9864f2ba68d",
  "toolUseResult": {
    "query": "Egami DSL design-based supervised learning NeurIPS 2023 LLM annotation debiasing experimental setup",
    "results": [
      {
        "tool_use_id": "srvtoolu_01N9Ej9wnFWbFiEjL1WToy1E",
        "content": [
          {
            "title": "Using Imperfect Surrogates for Downstream Inference: Design-based Supervised Learning for Social Science Applications of Large Language Models",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2023/hash/d862f7f5445255090de13b825b880d59-Abstract-Conference.html"
          },
          {
            "title": "Design-based Supervised Learning • dsl",
            "url": "http://naokiegami.com/dsl/"
          },
          {
            "title": "[2306.04746] Using Imperfect Surrogates for Downstream Inference: Design-based Supervised Learning for Social Science Applications of Large Language Models",
            "url": "https://arxiv.org/abs/2306.04746"
          },
          {
            "title": "Get Started with dsl • dsl",
            "url": "http://naokiegami.com/dsl/articles/intro.html"
          },
          {
            "title": "Using Imperfect Surrogates for Downstream Inference:",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2023/file/d862f7f5445255090de13b825b880d59-Paper-Conference.pdf"
          },
          {
            "title": "Benchmarking Debiasing Methods for LLM-based Parameter Estimates",
            "url": "https://arxiv.org/html/2506.09627"
          },
          {
            "title": "Benchmarking Debiasing Methods for LLM-based ...",
            "url": "https://aclanthology.org/2025.emnlp-main.1000.pdf"
          },
          {
            "title": "Using Large Language Model Annotations for the Social Sciences:",
            "url": "https://naokiegami.com/paper/dsl_ss.pdf"
          },
          {
            "title": "Using Imperfect Surrogates for Downstream Inference: Design-based Supervised Learning for Social Science Applications of Large Language Models - Princeton University",
            "url": "https://collaborate.princeton.edu/en/publications/using-imperfect-surrogates-for-downstream-inference-design-based-/"
          }
        ]
      },
      "Based on the search results, here's information about the Egami DSL work at NeurIPS 2023:\n\n## Overview\n\nNaoki Egami, Musashi Hinck, Brandon Stewart, and Hanying Wei presented their work at the Advances in Neural Information Processing Systems 36 (NeurIPS 2023) Main Conference Track.\n\n## Research Problem\n\nIn computational social science, researchers analyze documents to explain social and political phenomena, first obtaining labels for documents and then explaining labels using interpretable regression analyses. While LLMs provide a common way to annotate documents cheaply at scale, such surrogate labels are often imperfect and biased.\n\n## Key Findings\n\nDirect use of surrogate labels in downstream statistical analyses leads to substantial bias and invalid confidence intervals, even with high surrogate accuracy of 80-90%.\n\n## The DSL Method\n\nTo address this, the authors proposed the design-based supervised learning (DSL) estimator, which employs a doubly-robust procedure to combine surrogate labels with a smaller number of high-quality, gold-standard labels. The approach guarantees valid inference for downstream statistical analyses, even when surrogates are arbitrarily biased, by controlling the probability of sampling documents for gold-standard labeling.\n\n## Experimental Setup\n\nDSL combines large-scale (potentially biased) automated annotations and a smaller number of high-quality expensive expert annotations using a doubly robust bias-correction step."
    ],
    "durationSeconds": 7.902358619999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "84eb9dfe-960a-4385-ad67-29bf46564625",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "## The LLM Annotation Multiverse: Specification Curve Analysis for Robust Computational Social Science  ### Motivation  LLM-based text annotation has become the default measurement instrument in compu…",
  "leafUuid": "6545f05a-f252-418c-b009-a9864f2ba68d",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "LLM annotation robustness via specification curve analysis",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223"
}
```

---

### Tool call

_source line 34 · 2026-05-20T04:03:58.904Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UfFRTHPsxKwwPohtYoeMGc`</summary>

```json
{
  "query": "multiverse analysis specification curve visualization scalability 200+ specifications best practices 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6545f05a-f252-418c-b009-a9864f2ba68d",
  "isSidechain": false,
  "requestId": "req_011CbDA6KXCi16rSucPQA83w",
  "type": "assistant",
  "uuid": "9cd5c0dc-62b9-404d-a552-45c54cc6c102",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PedzouAQeV1zrmJsyJEiYQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 919,
      "cache_read_input_tokens": 27221,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 919,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 27221,
          "cache_creation_input_tokens": 919,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 919
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-20T04:04:05.713Z_

<details><summary>↩ Tool result · `toolu_01UfFRTHPsxKwwPohtYoeMGc`</summary>

```text
Web search results for query: "multiverse analysis specification curve visualization scalability 200+ specifications best practices 2024 2025"

Links: [{"title":"Visualizing vastness: Graphical methods for multiverse analysis | PLOS One","url":"https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0339452"},{"title":"Visualizing vastness: Graphical methods for multiverse analysis","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12875576/"},{"title":"Conducting and Visualizing Specification Curve Analyses • specr","url":"https://masurp.github.io/specr/"},{"title":"GitHub - masurp/specr: Conducting and Visualizing Specification Curve Analyses · GitHub","url":"https://github.com/masurp/specr"},{"title":"Specification curve analysis and the multiverse | Statistical Modeling, Causal Inference, and Social Science","url":"https://statmodeling.stat.columbia.edu/2024/11/12/specification-curve-analysis-and-the-multiverse/"},{"title":"The multiverse of universes: A tutorial to plan, execute and interpret multiverses analyses using the R package multiverse - Götz - 2024 - International Journal of Psychology - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1002/ijop.13229"}]

Based on the search results, here's what I found regarding multiverse analysis, specification curve visualization, and scalability:

## Key Findings

**Visualization Challenges and Solutions:**

Despite multiverse analysis's promise, the method faces a critical bottleneck in visualizing the multiverse in a way that is both scalable and interpretable, with existing approaches like specification curves and density plots falling short when multiverses grow large.

**Novel Approaches for Large Multiverses:**

Recent research introduces multiverse plots as a novel alternative to specification curves and density plots, demonstrating how multiverse plots can retain detailed information even in the face of thousands of model specifications. Multiverse plots overcome key limitations by eliminating arbitrary sampling and information loss on analytical decisions.

**Interactive Visualization Systems:**

For multiverses spanning hundreds or more universes, static visualizations may no longer be feasible; interactive visualization systems such as Milliways and Boba Visualizer allow users to explore results of large multiverse analyses.

**Current Tools and Updates:**

In May 2024, specr version 1.0.1 was released with new functions to conduct inferences on specification curve analysis.

**Interpretation Frameworks:**

Three broad approaches exist to make sense of multiverse results: assessing overall variability of parameters across the multiverse, identifying sources of variability, and drawing conclusions regarding the overall effect being studied.

The research indicates that best practices for handling 200+ specifications have evolved significantly in 2024-2025, with emphasis shifting from static specification curves to interactive and density-based visualization methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9cd5c0dc-62b9-404d-a552-45c54cc6c102",
  "isSidechain": false,
  "promptId": "73ab1a43-96b2-4654-a2b9-23d82346af16",
  "type": "user",
  "uuid": "f1e7db34-420c-4342-b595-21cce467f77a",
  "toolUseResult": {
    "query": "multiverse analysis specification curve visualization scalability 200+ specifications best practices 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01YEmUMdFTm3nFdLPbvuCtng",
        "content": [
          {
            "title": "Visualizing vastness: Graphical methods for multiverse analysis | PLOS One",
            "url": "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0339452"
          },
          {
            "title": "Visualizing vastness: Graphical methods for multiverse analysis",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12875576/"
          },
          {
            "title": "Conducting and Visualizing Specification Curve Analyses • specr",
            "url": "https://masurp.github.io/specr/"
          },
          {
            "title": "GitHub - masurp/specr: Conducting and Visualizing Specification Curve Analyses · GitHub",
            "url": "https://github.com/masurp/specr"
          },
          {
            "title": "Specification curve analysis and the multiverse | Statistical Modeling, Causal Inference, and Social Science",
            "url": "https://statmodeling.stat.columbia.edu/2024/11/12/specification-curve-analysis-and-the-multiverse/"
          },
          {
            "title": "The multiverse of universes: A tutorial to plan, execute and interpret multiverses analyses using the R package multiverse - Götz - 2024 - International Journal of Psychology - Wiley Online Library",
            "url": "https://onlinelibrary.wiley.com/doi/10.1002/ijop.13229"
          }
        ]
      },
      "Based on the search results, here's what I found regarding multiverse analysis, specification curve visualization, and scalability:\n\n## Key Findings\n\n**Visualization Challenges and Solutions:**\n\nDespite multiverse analysis's promise, the method faces a critical bottleneck in visualizing the multiverse in a way that is both scalable and interpretable, with existing approaches like specification curves and density plots falling short when multiverses grow large.\n\n**Novel Approaches for Large Multiverses:**\n\nRecent research introduces multiverse plots as a novel alternative to specification curves and density plots, demonstrating how multiverse plots can retain detailed information even in the face of thousands of model specifications. Multiverse plots overcome key limitations by eliminating arbitrary sampling and information loss on analytical decisions.\n\n**Interactive Visualization Systems:**\n\nFor multiverses spanning hundreds or more universes, static visualizations may no longer be feasible; interactive visualization systems such as Milliways and Boba Visualizer allow users to explore results of large multiverse analyses.\n\n**Current Tools and Updates:**\n\nIn May 2024, specr version 1.0.1 was released with new functions to conduct inferences on specification curve analysis.\n\n**Interpretation Frameworks:**\n\nThree broad approaches exist to make sense of multiverse results: assessing overall variability of parameters across the multiverse, identifying sources of variability, and drawing conclusions regarding the overall effect being studied.\n\nThe research indicates that best practices for handling 200+ specifications have evolved significantly in 2024-2025, with emphasis shifting from static specification curves to interactive and density-based visualization methods."
    ],
    "durationSeconds": 6.802695737000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9cd5c0dc-62b9-404d-a552-45c54cc6c102",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-20T04:04:09.252Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011BeRkpFfVzm1dXkk5irW6y`</summary>

```json
{
  "query": "Auspurg PNAS 2025 multiverse analysis critique Ganslmeier Vlandas reply justified specifications"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1e7db34-420c-4342-b595-21cce467f77a",
  "isSidechain": false,
  "requestId": "req_011CbDA72qsoLkUjSEW2k1WB",
  "type": "assistant",
  "uuid": "a7a45899-67b6-4ba9-9ad3-594a7397ad35",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012BaGp5pTRRQrbcfyAdUstB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 797,
      "cache_read_input_tokens": 28140,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 797,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 28140,
          "cache_creation_input_tokens": 797,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 797
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-20T04:04:16.378Z_

<details><summary>↩ Tool result · `toolu_011BeRkpFfVzm1dXkk5irW6y`</summary>

```text
Web search results for query: "Auspurg PNAS 2025 multiverse analysis critique Ganslmeier Vlandas reply justified specifications"

Links: [{"title":"Robustness is better assessed with a few thoughtful models than with billions of regressions | PNAS","url":"https://www.pnas.org/doi/10.1073/pnas.2521917122"},{"title":"Reply to Auspurg: On the limits of “justified” model spaces | PNAS","url":"https://www.pnas.org/doi/10.1073/pnas.2523374122"},{"title":"What’s a multiverse good for anyway?","url":"https://sites.stat.columbia.edu/gelman/research/unpublished/rohrer_multiverse.pdf"},{"title":"Reply to Auspurg: On the limits of “justified” model spaces","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12582334/"},{"title":"Robustness is better assessed with a few thoughtful models than with billions of regressions - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12582322/"},{"title":"Table of Contents — October 28, 2025, 122 (43) | PNAS","url":"https://www.pnas.org/toc/pnas/122/43"},{"title":"Estimating the extent and sources of model uncertainty in political science | PNAS","url":"https://www.pnas.org/doi/10.1073/pnas.2414926122"},{"title":"Blog – Tim Vlandas","url":"https://timvlandas.com/blog/"}]

Based on the search results, I found a detailed academic exchange on this topic published in PNAS in 2025:

## Overview

Ganslmeier and Vlandas conducted an ambitious multiverse analysis, estimating over 3.6 billion regression models across four political science topics by varying estimation strategies, covariates, operationalizations, and samples, documenting drastic model instability.

## Auspurg's Critique

Katrin Auspurg argues that their approach substantially overstates uncertainty. She contends that many models in the analysis are unjustified because they violate well-established econometric and multiverse standards. Her specific criticisms include:

- Many models regress the first-differenced outcome in ways that violate temporal order, and many do not include fixed effects or cluster-robust standard errors, which are standard in panel data analyses.
- Country subsetting reduces power and inflates instability, and it disregards that political science often predicts context-dependent effects.

## Ganslmeier and Vlandas Reply

Ganslmeier and Vlandas respond that what counts as "justified" is itself heavily contested. They argue their article provides a systematic method that enables researchers to assess sensitivity openly and identify which assumptions and empirical decisions matter most for their research question.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7a45899-67b6-4ba9-9ad3-594a7397ad35",
  "isSidechain": false,
  "promptId": "73ab1a43-96b2-4654-a2b9-23d82346af16",
  "type": "user",
  "uuid": "3fb37453-1c6a-45c8-b32d-08249d5b2ae5",
  "toolUseResult": {
    "query": "Auspurg PNAS 2025 multiverse analysis critique Ganslmeier Vlandas reply justified specifications",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RCxHesZWkzCzYQFfVsNeuH",
        "content": [
          {
            "title": "Robustness is better assessed with a few thoughtful models than with billions of regressions | PNAS",
            "url": "https://www.pnas.org/doi/10.1073/pnas.2521917122"
          },
          {
            "title": "Reply to Auspurg: On the limits of “justified” model spaces | PNAS",
            "url": "https://www.pnas.org/doi/10.1073/pnas.2523374122"
          },
          {
            "title": "What’s a multiverse good for anyway?",
            "url": "https://sites.stat.columbia.edu/gelman/research/unpublished/rohrer_multiverse.pdf"
          },
          {
            "title": "Reply to Auspurg: On the limits of “justified” model spaces",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12582334/"
          },
          {
            "title": "Robustness is better assessed with a few thoughtful models than with billions of regressions - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12582322/"
          },
          {
            "title": "Table of Contents — October 28, 2025, 122 (43) | PNAS",
            "url": "https://www.pnas.org/toc/pnas/122/43"
          },
          {
            "title": "Estimating the extent and sources of model uncertainty in political science | PNAS",
            "url": "https://www.pnas.org/doi/10.1073/pnas.2414926122"
          },
          {
            "title": "Blog – Tim Vlandas",
            "url": "https://timvlandas.com/blog/"
          }
        ]
      },
      "Based on the search results, I found a detailed academic exchange on this topic published in PNAS in 2025:\n\n## Overview\n\nGanslmeier and Vlandas conducted an ambitious multiverse analysis, estimating over 3.6 billion regression models across four political science topics by varying estimation strategies, covariates, operationalizations, and samples, documenting drastic model instability.\n\n## Auspurg's Critique\n\nKatrin Auspurg argues that their approach substantially overstates uncertainty. She contends that many models in the analysis are unjustified because they violate well-established econometric and multiverse standards. Her specific criticisms include:\n\n- Many models regress the first-differenced outcome in ways that violate temporal order, and many do not include fixed effects or cluster-robust standard errors, which are standard in panel data analyses.\n- Country subsetting reduces power and inflates instability, and it disregards that political science often predicts context-dependent effects.\n\n## Ganslmeier and Vlandas Reply\n\nGanslmeier and Vlandas respond that what counts as \"justified\" is itself heavily contested. They argue their article provides a systematic method that enables researchers to assess sensitivity openly and identify which assumptions and empirical decisions matter most for their research question."
    ],
    "durationSeconds": 7.121982459999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a7a45899-67b6-4ba9-9ad3-594a7397ad35",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-20T04:04:18.971Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019ozC2dQzkjc7LWwUrnheoz`</summary>

```json
{
  "query": "permutation test specification curve analysis joint inference implementation 500 permutations computational cost"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fb37453-1c6a-45c8-b32d-08249d5b2ae5",
  "isSidechain": false,
  "requestId": "req_011CbDA7pQ46iB38wXNwf53t",
  "type": "assistant",
  "uuid": "d629ab1b-fbf1-4ba8-95ae-b93e8d89d746",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gv8EKo1rdyaPsdEr1AJy5V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 805,
      "cache_read_input_tokens": 28937,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 805,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 28937,
          "cache_creation_input_tokens": 805,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 805
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-20T04:04:26.154Z_

<details><summary>↩ Tool result · `toolu_019ozC2dQzkjc7LWwUrnheoz`</summary>

```text
Web search results for query: "permutation test specification curve analysis joint inference implementation 500 permutations computational cost"

Links: [{"title":"Non‐parametric combination and related permutation tests for neuroimaging - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC4783210/"},{"title":"Covariance Correction for Permutation Statistics in Multiple Testing Problems","url":"https://arxiv.org/html/2604.06915"},{"title":"permutation_test — SciPy v1.17.0 Manual","url":"https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.permutation_test.html"},{"title":"Exact Combinatorial Inference for Brain Images","url":"https://arxiv.org/pdf/1807.02885"},{"title":"Parallelized calculation of permutation tests","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8016463/"},{"title":"STATISTICA, anno LXX, n. 4, 2010 THE PERMUTATION TESTING APPROACH: A REVIEW","url":"https://rivista-statistica.unibo.it/article/download/3599/2950/9070"},{"title":"permApprox: a general framework for accurate permutation p-value approximation","url":"https://arxiv.org/pdf/2602.22975"},{"title":"Optimized permutation testing for information theoretic measures of multi-gene interactions","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8028212/"}]

I've completed the web search for your query on permutation test specification curve analysis with joint inference implementation and computational costs. Here are the key findings:

## Joint Inference and Permutation Methods

Permutation methods can be applied to combination analyses including multiple imaging modalities or multiple hypotheses on the same data, using synchronized permutations to correct for multiplicity of tests. For joint inference problems, non-parametric combination (NPC) methodology can be modified to perform inference in a single phase with reasonable computational demands, rather than requiring a two-phase algorithm with large data storage requirements.

## Computational Cost Considerations

In most brain imaging studies, 5000-1000000 permutations are often used, which puts the total number of generated permutations usually less than 1% of all possible permutations. Permutation procedures become computationally demanding when accurate estimation of small p-values is required. 

For efficiency improvements, a computationally efficient methodology corrects the covariance matrix of multiple permutation statistics to restore correct joint asymptotic dependence structure, enabling asymptotically valid permutation tests in multiple testing frameworks.

The search results primarily focused on general permutation testing methodology and computational efficiency rather than specification curve analysis specifically. If you need more targeted information on specification curve analysis combined with permutation tests and 500 permutations specifically, you may want to search academic databases or the original specification curve methodology papers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d629ab1b-fbf1-4ba8-95ae-b93e8d89d746",
  "isSidechain": false,
  "promptId": "73ab1a43-96b2-4654-a2b9-23d82346af16",
  "type": "user",
  "uuid": "9a10c4de-a22e-4d1a-8b14-22b890402a92",
  "toolUseResult": {
    "query": "permutation test specification curve analysis joint inference implementation 500 permutations computational cost",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Foc3RgFSM8MYhjFNBvsBps",
        "content": [
          {
            "title": "Non‐parametric combination and related permutation tests for neuroimaging - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4783210/"
          },
          {
            "title": "Covariance Correction for Permutation Statistics in Multiple Testing Problems",
            "url": "https://arxiv.org/html/2604.06915"
          },
          {
            "title": "permutation_test — SciPy v1.17.0 Manual",
            "url": "https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.permutation_test.html"
          },
          {
            "title": "Exact Combinatorial Inference for Brain Images",
            "url": "https://arxiv.org/pdf/1807.02885"
          },
          {
            "title": "Parallelized calculation of permutation tests",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8016463/"
          },
          {
            "title": "STATISTICA, anno LXX, n. 4, 2010 THE PERMUTATION TESTING APPROACH: A REVIEW",
            "url": "https://rivista-statistica.unibo.it/article/download/3599/2950/9070"
          },
          {
            "title": "permApprox: a general framework for accurate permutation p-value approximation",
            "url": "https://arxiv.org/pdf/2602.22975"
          },
          {
            "title": "Optimized permutation testing for information theoretic measures of multi-gene interactions",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8028212/"
          }
        ]
      },
      "I've completed the web search for your query on permutation test specification curve analysis with joint inference implementation and computational costs. Here are the key findings:\n\n## Joint Inference and Permutation Methods\n\nPermutation methods can be applied to combination analyses including multiple imaging modalities or multiple hypotheses on the same data, using synchronized permutations to correct for multiplicity of tests. For joint inference problems, non-parametric combination (NPC) methodology can be modified to perform inference in a single phase with reasonable computational demands, rather than requiring a two-phase algorithm with large data storage requirements.\n\n## Computational Cost Considerations\n\nIn most brain imaging studies, 5000-1000000 permutations are often used, which puts the total number of generated permutations usually less than 1% of all possible permutations. Permutation procedures become computationally demanding when accurate estimation of small p-values is required. \n\nFor efficiency improvements, a computationally efficient methodology corrects the covariance matrix of multiple permutation statistics to restore correct joint asymptotic dependence structure, enabling asymptotically valid permutation tests in multiple testing frameworks.\n\nThe search results primarily focused on general permutation testing methodology and computational efficiency rather than specification curve analysis specifically. If you need more targeted information on specification curve analysis combined with permutation tests and 500 permutations specifically, you may want to search academic databases or the original specification curve methodology papers."
    ],
    "durationSeconds": 7.179609511000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d629ab1b-fbf1-4ba8-95ae-b93e8d89d746",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-20T04:04:28.930Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013vfGrym9Q7MST6Wj7MnQDj`</summary>

```json
{
  "query": "Simonsohn specification curve analysis Nature Human Behaviour 2020 permutation test 500 original methodology joint significance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a10c4de-a22e-4d1a-8b14-22b890402a92",
  "isSidechain": false,
  "requestId": "req_011CbDA8YCkEeN4dJngPyP6z",
  "type": "assistant",
  "uuid": "09708cf2-fa5b-496a-af75-b98f9bd07350",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KYt8Wcqivugx15UgvhGMsQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 793,
      "cache_read_input_tokens": 29742,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 793,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 29742,
          "cache_creation_input_tokens": 793,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 793
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-20T04:04:34.733Z_

<details><summary>↩ Tool result · `toolu_013vfGrym9Q7MST6Wj7MnQDj`</summary>

```text
Web search results for query: "Simonsohn specification curve analysis Nature Human Behaviour 2020 permutation test 500 original methodology joint significance"

Links: [{"title":"Publisher Correction: Specification curve analysis | Nature Human Behaviour","url":"https://www.nature.com/articles/s41562-020-00974-w"},{"title":"Specification curve analysis - Ramon Llull University","url":"https://merit.url.edu/en/publications/specification-curve-analysis-3/"},{"title":"Specification curve analysis | Semantic Scholar","url":"https://www.semanticscholar.org/paper/0a6f39bad41608b86673b6226f2893912b27a72c"},{"title":"Specification Curve","url":"https://aeturrell.github.io/specification_curve/"},{"title":"Specification curve analysis - Wharton Faculty Platform","url":"https://faculty.wharton.upenn.edu/wp-content/uploads/2016/11/33-Simonsohn-Simmons-Nelson-2020.pdf"},{"title":"Specification curve analysis | Nature Human Behaviour","url":"https://www.nature.com/articles/s41562-020-0912-z"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Specification+Curve+Analysis&amp=&author=U.+Simonsohn&amp=&author=J.+P.+Simmons&amp=&author=L.+D.+Nelson&amp=&publication_year=2020&amp=&journal=Nature+Human+Behaviour&amp=&volume=4&amp=&pages=1208-14"},{"title":"Google znalac","url":"https://scholar.google.com/scholar_lookup?title=Specification+curve+analysis&amp=&author=U.+Simonsohn&amp=&author=J.+P.+Simmons&amp=&author=L.+D.+Nelson&amp=&publication_year=2020&amp=&journal=Nature+Human+Behaviour&amp=&volume=4&amp=&pages=1208-1214"},{"title":"Specification analysis for technology use and teenager well-being:   statistical validity and a Bayesian proposal","url":"https://arxiv.org/pdf/2201.05381"}]

Based on the search results, I found comprehensive information about the Simonsohn et al. specification curve analysis paper published in Nature Human Behaviour in 2020.

## Overview

Simonsohn, Simmons, and Nelson (2020) published "Specification curve analysis" in Nature Human Behaviour, volume 4(11), pages 1208-1214.

## Core Methodology

The paper addresses how empirical results hinge on analytical decisions that are defensible, arbitrary and motivated, which probably introduce bias and involve variability not reflected by standard errors. The authors introduce specification curve analysis, which consists of three steps: (1) identifying the set of theoretically justified, statistically valid and non-redundant specifications; (2) displaying the results graphically, allowing readers to identify consequential specifications decisions; and (3) conducting joint inference across all specifications.

## Application

The authors illustrate the technique by applying it to three findings from two different papers, one investigating discrimination based on distinctively Black names, the other investigating the effect of assigning female versus male names to hurricanes.

The paper represents an important methodological contribution to addressing selective reporting and the "garden of forking paths" problem in empirical research by enabling researchers to display the robustness of their findings across multiple reasonable analytical specifications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "09708cf2-fa5b-496a-af75-b98f9bd07350",
  "isSidechain": false,
  "promptId": "73ab1a43-96b2-4654-a2b9-23d82346af16",
  "type": "user",
  "uuid": "55489271-faac-4179-8e88-81ffaa1bfe3a",
  "toolUseResult": {
    "query": "Simonsohn specification curve analysis Nature Human Behaviour 2020 permutation test 500 original methodology joint significance",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TphTPL9yRBjtM6jG4u93tL",
        "content": [
          {
            "title": "Publisher Correction: Specification curve analysis | Nature Human Behaviour",
            "url": "https://www.nature.com/articles/s41562-020-00974-w"
          },
          {
            "title": "Specification curve analysis - Ramon Llull University",
            "url": "https://merit.url.edu/en/publications/specification-curve-analysis-3/"
          },
          {
            "title": "Specification curve analysis | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/0a6f39bad41608b86673b6226f2893912b27a72c"
          },
          {
            "title": "Specification Curve",
            "url": "https://aeturrell.github.io/specification_curve/"
          },
          {
            "title": "Specification curve analysis - Wharton Faculty Platform",
            "url": "https://faculty.wharton.upenn.edu/wp-content/uploads/2016/11/33-Simonsohn-Simmons-Nelson-2020.pdf"
          },
          {
            "title": "Specification curve analysis | Nature Human Behaviour",
            "url": "https://www.nature.com/articles/s41562-020-0912-z"
          },
          {
            "title": "Google Scholar",
            "url": "https://scholar.google.com/scholar_lookup?title=Specification+Curve+Analysis&amp=&author=U.+Simonsohn&amp=&author=J.+P.+Simmons&amp=&author=L.+D.+Nelson&amp=&publication_year=2020&amp=&journal=Nature+Human+Behaviour&amp=&volume=4&amp=&pages=1208-14"
          },
          {
            "title": "Google znalac",
            "url": "https://scholar.google.com/scholar_lookup?title=Specification+curve+analysis&amp=&author=U.+Simonsohn&amp=&author=J.+P.+Simmons&amp=&author=L.+D.+Nelson&amp=&publication_year=2020&amp=&journal=Nature+Human+Behaviour&amp=&volume=4&amp=&pages=1208-1214"
          },
          {
            "title": "Specification analysis for technology use and teenager well-being:   statistical validity and a Bayesian proposal",
            "url": "https://arxiv.org/pdf/2201.05381"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about the Simonsohn et al. specification curve analysis paper published in Nature Human Behaviour in 2020.\n\n## Overview\n\nSimonsohn, Simmons, and Nelson (2020) published \"Specification curve analysis\" in Nature Human Behaviour, volume 4(11), pages 1208-1214.\n\n## Core Methodology\n\nThe paper addresses how empirical results hinge on analytical decisions that are defensible, arbitrary and motivated, which probably introduce bias and involve variability not reflected by standard errors. The authors introduce specification curve analysis, which consists of three steps: (1) identifying the set of theoretically justified, statistically valid and non-redundant specifications; (2) displaying the results graphically, allowing readers to identify consequential specifications decisions; and (3) conducting joint inference across all specifications.\n\n## Application\n\nThe authors illustrate the technique by applying it to three findings from two different papers, one investigating discrimination based on distinctively Black names, the other investigating the effect of assigning female versus male names to hurricanes.\n\nThe paper represents an important methodological contribution to addressing selective reporting and the \"garden of forking paths\" problem in empirical research by enabling researchers to display the robustness of their findings across multiple reasonable analytical specifications."
    ],
    "durationSeconds": 5.797642420999982,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "09708cf2-fa5b-496a-af75-b98f9bd07350",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-20T04:04:37.310Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019J53sAfoX96n8r9bJrhvs2`</summary>

```json
{
  "query": "LLM batch annotation quality degradation batch size prompting 2024 2025 evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55489271-faac-4179-8e88-81ffaa1bfe3a",
  "isSidechain": false,
  "requestId": "req_011CbDA9AwbrBo1ZoWPeTxR2",
  "type": "assistant",
  "uuid": "657cb378-3b43-42cd-85fc-de1c7e41b7c3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013PAR8Sq3NTp9e7srw98Pvc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 937,
      "cache_read_input_tokens": 30535,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 937,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 30535,
          "cache_creation_input_tokens": 937,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 937
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "## The LLM Annotation Multiverse: Specification Curve Analysis for Robust Computational Social Science  ### Motivation  LLM-based text annotation has become the default measurement instrument in compu…",
  "leafUuid": "657cb378-3b43-42cd-85fc-de1c7e41b7c3",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "LLM annotation robustness via specification curve analysis",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223"
}
```

---

### Tool result

_source line 45 · 2026-05-20T04:04:45.220Z_

<details><summary>↩ Tool result · `toolu_019J53sAfoX96n8r9bJrhvs2`</summary>

```text
Web search results for query: "LLM batch annotation quality degradation batch size prompting 2024 2025 evaluation"

Links: [{"title":"Published as a conference paper at ICLR 2024","url":"https://arxiv.org/pdf/2309.00384"},{"title":"Researchers waste 80% of LLM annotation costs by classifying one text at a time","url":"https://arxiv.org/pdf/2604.03684"},{"title":"1 TITLE Scaling the Prompt: How Batch Size Shapes Performance of Mid-2025","url":"https://www.medrxiv.org/content/10.1101/2025.09.02.25334159v1.full.pdf"},{"title":"Auto-Demo Prompting: Leveraging Generated Outputs as Demonstrations for   Enhanced Batch Prompting","url":"https://arxiv.org/pdf/2410.01724"},{"title":"Scaling the Prompt: How Batch Size Shapes Performance of Mid-2025 State-of-the-Art LLMs in Automated Title-and-Abstract Screening","url":"https://www.medrxiv.org/content/10.1101/2025.09.02.25334159.full.pdf"},{"title":"arXiv:2503.02756v1 [cs.CL] 4 Mar 2025","url":"https://arxiv.org/pdf/2503.02756"},{"title":"Efficient but Vulnerable: Benchmarking and Defending LLM Batch Prompting Attack","url":"https://arxiv.org/html/2503.15551"},{"title":"Efficient but Vulnerable: Benchmarking and Defending LLM Batch Prompting Attack","url":"https://arxiv.org/pdf/2503.15551"}]

Based on the search results, here's what I found about LLM batch annotation quality degradation with batch size in prompting:

## Key Findings

**Quality Degradation with Batch Size:**

Simple batching can degrade performance, especially as batch size increases, and data points can yield different answers depending on their position within a prompt. This is a well-documented issue in recent research.

**Recent 2024-2025 Evaluations:**

1. **ICLR 2024 Study**: Researchers introduced Batch Permutation and Ensembling (BPE) for BatchPrompt – a majority vote over repeated permutations of data, that recovers label quality at the cost of more token usage.

2. **Mid-2025 State-of-the-Art Evaluation**: GPT-5 mini's sensitivity degraded at higher batch sizes (from 0.88 at batch 200 to 0.48 at batch 400). However, at a practical batch size of 100, Gemini 2.5 Pro achieved the highest sensitivity (1.00), whereas GPT-5 delivered the highest specificity (0.98).

3. **Social Science Content Analysis (2025)**: Six of eight models maintained accuracy within 2 percentage points of the single-item baseline through batch sizes of 100.

**Root Causes:**

While batch prompting provides efficiency advantages, handling lengthy context inputs is particularly difficult for transformers, which experience significant performance degradation when accessing relevant information from the middle of long contexts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "657cb378-3b43-42cd-85fc-de1c7e41b7c3",
  "isSidechain": false,
  "promptId": "73ab1a43-96b2-4654-a2b9-23d82346af16",
  "type": "user",
  "uuid": "2666455c-a627-497d-83b3-73133454b38d",
  "toolUseResult": {
    "query": "LLM batch annotation quality degradation batch size prompting 2024 2025 evaluation",
    "results": [
      {
        "tool_use_id": "srvtoolu_0191gd22BTpYr4s6CvMvVmKa",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2024",
            "url": "https://arxiv.org/pdf/2309.00384"
          },
          {
            "title": "Researchers waste 80% of LLM annotation costs by classifying one text at a time",
            "url": "https://arxiv.org/pdf/2604.03684"
          },
          {
            "title": "1 TITLE Scaling the Prompt: How Batch Size Shapes Performance of Mid-2025",
            "url": "https://www.medrxiv.org/content/10.1101/2025.09.02.25334159v1.full.pdf"
          },
          {
            "title": "Auto-Demo Prompting: Leveraging Generated Outputs as Demonstrations for   Enhanced Batch Prompting",
            "url": "https://arxiv.org/pdf/2410.01724"
          },
          {
            "title": "Scaling the Prompt: How Batch Size Shapes Performance of Mid-2025 State-of-the-Art LLMs in Automated Title-and-Abstract Screening",
            "url": "https://www.medrxiv.org/content/10.1101/2025.09.02.25334159.full.pdf"
          },
          {
            "title": "arXiv:2503.02756v1 [cs.CL] 4 Mar 2025",
            "url": "https://arxiv.org/pdf/2503.02756"
          },
          {
            "title": "Efficient but Vulnerable: Benchmarking and Defending LLM Batch Prompting Attack",
            "url": "https://arxiv.org/html/2503.15551"
          },
          {
            "title": "Efficient but Vulnerable: Benchmarking and Defending LLM Batch Prompting Attack",
            "url": "https://arxiv.org/pdf/2503.15551"
          }
        ]
      },
      "Based on the search results, here's what I found about LLM batch annotation quality degradation with batch size in prompting:\n\n## Key Findings\n\n**Quality Degradation with Batch Size:**\n\nSimple batching can degrade performance, especially as batch size increases, and data points can yield different answers depending on their position within a prompt. This is a well-documented issue in recent research.\n\n**Recent 2024-2025 Evaluations:**\n\n1. **ICLR 2024 Study**: Researchers introduced Batch Permutation and Ensembling (BPE) for BatchPrompt – a majority vote over repeated permutations of data, that recovers label quality at the cost of more token usage.\n\n2. **Mid-2025 State-of-the-Art Evaluation**: GPT-5 mini's sensitivity degraded at higher batch sizes (from 0.88 at batch 200 to 0.48 at batch 400). However, at a practical batch size of 100, Gemini 2.5 Pro achieved the highest sensitivity (1.00), whereas GPT-5 delivered the highest specificity (0.98).\n\n3. **Social Science Content Analysis (2025)**: Six of eight models maintained accuracy within 2 percentage points of the single-item baseline through batch sizes of 100.\n\n**Root Causes:**\n\nWhile batch prompting provides efficiency advantages, handling lengthy context inputs is particularly difficult for transformers, which experience significant performance degradation when accessing relevant information from the middle of long contexts."
    ],
    "durationSeconds": 7.905629278000007,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "657cb378-3b43-42cd-85fc-de1c7e41b7c3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-20T04:06:56.143Z_

Now I have enough research context. Let me compile my assessment.

---

【状态】: 有缺陷待补救

【前置调研发现】
- **Baumann et al. (arXiv:2509.08825, 2025)**: 18 LLMs × 37 tasks × 13M labels；实验设计覆盖 21 种缓解策略、2,361 个假设检验；以 hacking risk（对同一假设存在可翻转结论的 pipeline 配置比例）为核心指标。该数据集已公开（MIT license），是当前最大规模的 LLM annotation instability 基准。
- **Messing (arXiv:2604.11581, 2026)**: TEE 框架在 Chatbot Arena 数据上实验；对比 naive SE vs TEE-corrected SE，报告 40–60% 的低估幅度；分解 variance 来源（judge model, temperature, prompt phrasing）。实验偏统计方法论验证，没有 multiverse traversal。
- **McLaren et al. (arXiv:2603.26898, 2026)**: 6 个开源模型 × 4 个政治学任务，全因子实验设计（quantisation, hardware, prompt template 控制变量）；核心发现交互效应主导主效应。
- **Gligorić et al. (NAACL 2025, CDI)**: 3 个 CSS 任务（politeness, stance, bias），对比 CDI vs 纯 LLM vs 纯人工，以 MSE、CI coverage、human annotation savings 为指标。
- **Audinet de Pieuchon et al. (EMNLP 2025)**: 对比 DSL vs PPI，两组实验——固定总样本变人工标注量，固定人工标注量变总样本——评估 bias-variance tradeoff。
- **Simonsohn et al. (Nature Human Behaviour, 2020)**: 原始 specification curve analysis 方法论，三步走（枚举、可视化、联合推断），使用 500 次置换检验。
- **Batch prompting research (ICLR 2024; 2025 多篇)**: 批量大小增大会导致质量退化，尤其是位置效应（中间位置信息被忽略）；6/8 模型在 batch=100 时准确率仅下降 2pp，但更大 batch 时退化显著。

- **调研总结**: 该领域的实验设计标准要求：(1) 对 pipeline 各维度进行全因子或接近全因子的覆盖；(2) 明确的 variance decomposition（主效应+交互效应）；(3) 与已有 correction 方法（PPI/DSL/TEE）的定位对比；(4) 使用公开 benchmark 数据且有 gold label；(5) 审稿人会关注 multiverse 规模的可视化可解释性、batch prompting 的质量影响、以及模型选择的代表性。

---

【缺陷 1】
- 类别: baseline 不足或过时
- 问题: Proposal 的 comparative evaluation（Stage 2 评估部分）仅计划在 2–3 个任务上与 PPI/DSL 对比，但缺少一个关键 baseline：**ad hoc sensitivity analysis（Carlson & Burbano SMJ 2026 风格的 3–5 配置抽样检查）**。Proposal 在 "Why principled multiverse, not ad hoc sensitivity checks?" 一节中论证了 ad hoc 的不足，但实验设计中没有将其作为 baseline 实际跑出来做定量对比。审稿人很可能要求：你说 ad hoc 不够，那请证明——在同样的任务上，随机抽 3/5/10 个配置做 sensitivity check，其 robustness 结论与 full multiverse 的一致率是多少？
- 严重度: 可补救
- 补救方案: 在实验设计中增加一个 "ad hoc sensitivity baseline"：对每个任务，随机抽取 k=3, 5, 10 个配置（重复 100 次），计算其 robustness 分类（robust/fragile/sign-inconsistent）与 full multiverse 结论的一致率。这直接量化了 principled multiverse 相对于 ad hoc 检查的增量价值，也与 ablation 3（model diversity curve）互补。该实验无额外 API 成本（使用缓存的 annotation 输出）。
- 调研依据: Carlson & Burbano (SMJ 2026) 推荐 3–5 配置的 informal sensitivity analysis 作为实践指南；Baumann et al. (2025) 的 2,361 个假设检验提供了 hacking risk 的量化基准。将 ad hoc 方法作为 baseline 进行定量对比是验证 proposal 核心论点的必要实验。

【缺陷 2】
- 类别: 实验设计不足
- 问题: Proposal 提出 10 个任务从 Baumann et al. 的 37 个任务中选取，但**任务选取标准缺乏操作化细节**。具体问题：(1) "task has a natural downstream hypothesis" 未说明这些假设从何而来——是从 Baumann et al. 的原始论文中复现，还是 proposal 作者自行设计？如果是自行设计，存在 researcher degrees of freedom 问题（选择有利于展示 fragility 的假设）；(2) "pre-registered" 仅作为一句承诺，但没有说明 pre-registration 的具体内容和时间节点。
- 严重度: 可补救
- 补救方案: (1) 明确说明 downstream hypothesis 的来源——建议优先使用 Baumann et al. (2025) 原始研究中已有的假设检验（该数据集来自 21 篇已发表的社会科学论文，每篇有明确的研究假设），这样既避免了 researcher degrees of freedom，又增强了与 Baumann et al. 31% hacking risk 发现的直接可比性；(2) 在 proposal 中明确 pre-registration 平台（如 OSF）和时间节点（在任何 annotation 执行之前）。
- 调研依据: Baumann et al. (2025) 的数据集来源于 21 篇已发表研究的 2,361 个假设检验，直接复用这些假设是最自然且无争议的选择。

【缺陷 3】
- 类别: 评估方案缺陷
- 问题: 在 specification curve 可视化方面，proposal 计划每个任务生成 90–270 个 specification points。调研显示，specification curve 在 200–300 个 specifications 以上会出现 "visual fuzz" 问题（Visualizing Vastness, PLOS One 2025），且 Simonsohn et al. (2020) 的原始方法论主要在较小规模 multiverse 上验证。Proposal 未讨论**可视化和可解释性方案**——审稿人需要看到清晰的 specification curve，而 270 个 specifications 可能处于 interpretability 的边界。
- 严重度: 可补救
- 补救方案: (1) 在方法论部分明确可视化策略：对 ≤150 个 specifications 的任务使用标准 specification curve（Simonsohn 风格）；对 >150 个的任务补充 multiverse plot（参考 Visualizing Vastness, PLOS One 2025）或交互式 Boba Visualizer；(2) 在 specification curve 图中加入 pipeline dimension 的色彩编码（model 用颜色、prompt 用形状等），帮助识别哪些维度驱动了排序变化。这不增加实验成本，只影响 presentation。
- 调研依据: "Visualizing Vastness: Graphical methods for multiverse analysis" (PLOS One, 2025) 明确指出 specification curve 在大规模 multiverse 中的可解释性问题，并提出 multiverse plot 作为替代方案。

【缺陷 4】
- 类别: 可行性问题
- 问题: **批量标注（batch=25）的质量影响未被充分控制**。Proposal 在 ablation 4 中计划 "Compare batch=25 vs batch=1 annotation on ≥1 task with ≥1 model"，但调研显示 batch prompting 的质量退化是一个已被充分记录的问题（ICLR 2024; 多篇 2025 论文），且存在显著的**位置效应**（中间位置 items 被忽略）。batch=25 在现有文献中属于较大的 batch size（多数研究测试到 batch=10–20 时已观察到退化），且 proposal 的全部 annotation 都使用 batch=25，意味着如果 batch 效应显著，所有结果的有效性都会受质疑。
- 严重度: 可补救
- 补救方案: (1) 将 batch ablation 升级为**先决条件验证（pilot validation）**，而非事后 ablation——在全量 annotation 执行之前，先在 2 个任务 × 2 个模型上对比 batch=1 vs batch=10 vs batch=25，如果 batch=25 退化 >3pp 准确率，则回退到更小 batch size；(2) 在 ablation 中加入位置效应分析（对 batch 内不同位置的 items 分别计算准确率）；(3) 明确在论文中报告 batch size 的选择依据和验证结果。这可能增加少量 pilot 成本（$20–50），但能防止全量数据的有效性被质疑。
- 调研依据: ICLR 2024 Batch Permutation and Ensembling 论文及 2025 mid-year evaluation 均显示 batch size 增大导致准确率退化，尤其是位置效应；6/8 模型在 batch=100 时仍可接受但 batch>100 显著退化，batch=25 虽在可接受范围但需要验证。

【缺陷 5】
- 类别: ablation 不完整
- 问题: Ablation 设计缺少一个关键的对照实验——**E/N/U 分类的 inter-annotator agreement / sensitivity to expert judgment**。Proposal 的核心贡献是 E/N/U 分类框架，但 E/N/U 分类本身是 researcher judgment（哪些配置是 Type E、N、U），这引入了新的 researcher degrees of freedom。Ablation 1 只测试了 "扰动 E/N/U 边界"，但未涉及分类的可靠性——如果让不同的 CSS 研究者独立做 E/N/U 分类，结论一致吗？
- 严重度: 可补救
- 补救方案: 有两种方案，视资源而定：(A) **理想方案**：邀请 2–3 位 CSS 领域的独立研究者对 10 个任务的 5 个 pipeline 维度独立做 E/N/U 分类（这只需要填表，不需要跑实验），计算 inter-rater agreement（Cohen's kappa 或 Fleiss' kappa），然后对分歧点进行 sensitivity analysis——如果分歧导致不同的 multiverse 和不同的 robustness 结论，这是一个严重问题。(B) **最低方案**：如果无法获得独立评审，至少应在 Ablation 1 中系统性地测试所有 "边界案例"（如 CoT 在 binary tasks 上是 N 还是 E、temperature 在 subjective tasks 上是 E 还是 U），并报告这些边界案例的翻转对最终 robustness 分类的影响。
- 调研依据: Del Giudice & Gangestad (AMPPS 2021) 的原始 E/N/U 框架本身就承认分类存在主观性；Auspurg (PNAS 2025) 的核心批评正是 "justified" 和 "unjustified" 的边界是主观的——如果 proposal 不提供 E/N/U 分类可靠性的证据，审稿人很可能沿此线路质疑。

【缺陷 6】
- 类别: 实验设计不足
- 问题: 模型选择中有两个模型"待定"——"Two additional models selected to fill gaps in the architecture/scale matrix (e.g., one dense mid-scale model, one additional proprietary model)"。对于 EMNLP 投稿来说，审稿人会期望看到**明确的模型列表和选择理由**。更重要的是，模型选择中**缺少 Claude 系列模型**的理由不够充分——proposal 称 "chosen over Claude to avoid circularity with any LLM-assisted E/N/U classification process"，但 (1) E/N/U 分类是否实际使用了 LLM 辅助未说明，如果是纯人工分类则不存在 circularity；(2) Claude 是当前最广泛使用的 annotation LLM 之一，不包含它会被质疑 model coverage 的代表性。
- 严重度: 可补救
- 补救方案: (1) 明确补全两个待定模型的具体选择——建议一个 dense mid-scale 开源模型（如 Mistral Large 或 Llama 4 Scout）和一个 proprietary 模型（如 Claude 3.5 Sonnet 或 Gemini 2.5 Pro）；(2) 如果 E/N/U 分类是纯人工完成，则 Claude 的 circularity 理由不成立，应将其纳入模型选择；如果确实使用了 LLM 辅助分类，则 (a) 明确说明这一点，(b) 在 ablation 中比较 LLM-assisted vs 纯人工 E/N/U 分类的一致性；(3) 在 proposal 中给出模型选择的完整矩阵（architecture family × scale × open/proprietary），确保没有明显空白。
- 调研依据: Baumann et al. (2025) 使用 18 个模型覆盖广泛；McLaren et al. (2026) 使用 6 个开源模型但限于特定 quantisation；同领域论文普遍期望覆盖至少 2 个 proprietary + 2–3 个开源模型。

【缺陷 7】
- 类别: compute 公平性问题
- 问题: Proposal 使用的 6 个模型横跨不同规模（26B MoE 到 400B MoE），但在 specification curve 中**所有模型被等权对待**。问题是：如果小模型系统性地表现更差（Baumann et al. 2025 发现小模型 hacking risk 翻倍），它们会在 specification curve 中贡献更多 "fragile" 或 "sign-inconsistent" 的 specifications，从而系统性地拉低 robustness 评分。这可能导致一种偏差：一个在所有大模型上都 robust 的发现，仅因为包含了表现较差的小模型而被分类为 "fragile"。Proposal 提到了 "model-size class as nested factor in ANOVA"，但未讨论这个问题在 specification curve 和 joint inference 层面的影响。
- 严重度: 可补救
- 补救方案: (1) 在 specification curve 和 joint inference 分析中，除了 full multiverse 结果外，额外报告**按模型规模分层的 specification curve**（如 large-model-only multiverse vs full multiverse），明确展示模型规模对 robustness 分类的影响；(2) 这实际上也应作为 model diversity curve（ablation 3）的扩展——不仅报告 "6 models vs 3 models vs 1 model"，还应区分 "top-3 performing models" vs "random 3 models" vs "bottom-3 performing models"，以揭示 model quality 对 robustness 结论的影响。
- 调研依据: Baumann et al. (2025) 明确报告小模型 hacking risk 是大模型的约两倍；这意味着模型规模/质量会系统性地影响 specification curve 的形态，不做分层分析会混淆 "pipeline instability" 和 "model quality variation"。

【缺陷 8】
- 类别: 评估方案缺陷
- 问题: Stage 3 Variance Decomposition 使用 factorial ANOVA，但 proposal 未讨论**ANOVA 假设的适用性**。LLM annotation outputs 在多数任务上产生的 downstream statistics（如 regression coefficients, group differences）不一定满足 ANOVA 的正态性和方差齐性假设，尤其是在只有 10 个任务的情况下，task 层面的 generalizability 依赖很少的数据点。此外，5 个维度（model × prompt × temperature × system instruction × output parsing）的全因子 ANOVA 有 2^5-1=31 个效应项（主效应+交互），但 proposal 只明确提到报告 "main effects and two-way interactions"，高阶交互被忽略可能遗漏重要模式。
- 严重度: 可补救
- 补救方案: (1) 补充对 ANOVA 假设的验证（正态性检验、方差齐性检验），如不满足则使用非参数替代（如 permutation-based ANOVA 或 aligned rank transform）；(2) 对于高阶交互，至少报告三阶交互中 variance 贡献最大的前 3–5 个，即使不逐一讨论；(3) 补充效应量（η² 或 ω²）的报告，而不仅是显著性——ANOVA 在这个场景下更关注的是哪些因素的 variance contribution 大，而非 p 值。
- 调研依据: McLaren et al. (2026) 的核心发现是交互效应 dominate 主效应，这暗示高阶交互可能同样重要；Baumann et al. (2025) 使用的是更灵活的回归分析而非 ANOVA。基于领域实验规范判断，CSS 方法论论文通常要求 ANOVA 假设的明确检验。

---

**总结**：以上 8 个缺陷均为**可补救**的实验设计层面问题，没有发现致命的不可补救缺陷。Proposal 的整体实验框架是 solid 的——使用公开数据集（无需额外数据采集）、计算成本可控（$1,200–$2,000 + 缓存后的分析计算）、时间线合理（8–10 周）。核心补救优先级排序：缺陷 1（ad hoc baseline）和缺陷 5（E/N/U reliability）是审稿人最可能提出的 mandatory revision，应优先处理；缺陷 4（batch validation）虽技术简单但影响全部数据有效性，应在 pilot 阶段解决；其余缺陷可在写作阶段补充。

Sources:
- [Baumann et al. 2025 - LLM Hacking](https://arxiv.org/abs/2509.08825)
- [Messing 2026 - TEE Framework](https://arxiv.org/abs/2604.11581)
- [McLaren et al. 2026 - Interaction Effects](https://arxiv.org/abs/2603.26898)
- [Gligorić et al. NAACL 2025 - CDI](https://aclanthology.org/2025.naacl-long.179/)
- [Audinet de Pieuchon et al. EMNLP 2025 - DSL vs PPI](https://aclanthology.org/2025.emnlp-main.1000/)
- [Simonsohn et al. 2020 - Specification Curve Analysis](https://www.nature.com/articles/s41562-020-0912-z)
- [Visualizing Vastness - PLOS One 2025](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0339452)
- [Auspurg PNAS 2025 - Multiverse Critique](https://www.pnas.org/doi/10.1073/pnas.2521917122)
- [Ganslmeier & Vlandas PNAS 2025 - Reply](https://www.pnas.org/doi/10.1073/pnas.2523374122)
- [ICLR 2024 - Batch Prompting](https://arxiv.org/pdf/2309.00384)
- [Batch Annotation Cost Study 2026](https://arxiv.org/pdf/2604.03684)
- [Boba DSL - Liu et al.](https://idl.uw.edu/papers/boba)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2666455c-a627-497d-83b3-73133454b38d",
  "isSidechain": false,
  "requestId": "req_011CbDA9whto9K6zPphVhhiS",
  "type": "assistant",
  "uuid": "db8e10a4-1466-4983-b7d4-6c0376a46867",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RH3iJbJvYqT6f7xzG8L8bH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 872,
      "cache_read_input_tokens": 31472,
      "output_tokens": 6016,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 872,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6016,
          "cache_read_input_tokens": 31472,
          "cache_creation_input_tokens": 872,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 872
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "## The LLM Annotation Multiverse: Specification Curve Analysis for Robust Computational Social Science  ### Motivation  LLM-based text annotation has become the default measurement instrument in compu…",
  "leafUuid": "db8e10a4-1466-4983-b7d4-6c0376a46867",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "LLM annotation robustness via specification curve analysis",
  "sessionId": "afead175-60c3-43af-a590-891e6a9fc223"
}
```

---
