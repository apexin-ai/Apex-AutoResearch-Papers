# Research conversation: The LLM Annotation Multiverse: Specification Curve Analysis for Robust Computational Social Science ### Motivation LLM-b

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/3976331e-36ff-46c2-b0a6-249940c3361d.jsonl`
- **Structured JSON:** [`fe68e8c9c1f6b47fdf7d.json`](../../sessions/fe/fe68e8c9c1f6b47fdf7d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T04:02:22.908Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T04:02:22.908Z",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d",
  "content": "## The LLM Annotation Multiverse: Specification Curve Analysis for Robust Computational Social Science\n\n### Motivation\n\nLLM-based text annotation has become the default measurement instrument in computational social science (CSS), yet the pipeline involves numerous researcher degrees of freedom—model selection, prompt template, temperature, system instruction, output parsing—each capable of shifting substantive conclusions. Baumann et al. (arXiv:2509.08825, 2025) document a 31% \"LLM hacking\" risk across 18 LLMs × 37 tasks × 13M labels: for nearly one-third of hypothesis tests, a researcher can find a pipeline configuration that reverses the statistical conclusion. McLaren et al. (arXiv:2603.26898, 2026) show that interaction effects among pipeline dimensions dominate main effects, meaning pairwise sensitivity checks underestimate true instability. Messing (arXiv:2604.11581, 2026) demonstrates that naive standard errors in LLM pipelines are 40–60% smaller than TEE-corrected standard errors that account for prompt, temperature, and judge-model variance, with coverage of naive 95% CIs degrading as sample size increases. Kosch & Feger (CACM 2026) label this phenomenon \"prompt-hacking\"—the LLM analogue of p-hacking—but offer no formal remedy.\n\nThe methodological status quo offers two partial responses. First, diagnostic studies (Baumann et al. 2025; McLaren et al. 2026; arXiv:2601.02370, 2026) quantify instability but prescribe no inferential framework for deciding whether a finding is robust. Second, statistical correction methods—Design-based Supervised Learning (DSL; Egami et al., NeurIPS 2023), Prediction-Powered Inference / Confidence-Driven Inference (PPI/CDI; Gligorić et al., NAACL 2025), and their comparative benchmarking (Audinet de Pieuchon et al., EMNLP 2025)—use small human-label sets to debias LLM annotations within a single chosen pipeline configuration. These correction methods answer: \"Given my pipeline choice, how do I get an unbiased estimate?\" They cannot answer the logically prior question: \"Does my conclusion depend on which pipeline I chose?\" This is precisely the question multiverse analysis is designed to address.\n\n### Research Landscape\n\n**Diagnostic work.** Baumann et al. (arXiv:2509.08825) provide the largest controlled study of LLM annotation instability (18 models, 37 tasks, 21 mitigation strategies). McLaren et al. (arXiv:2603.26898) extend this to interaction effects in political science annotation. The Variance-Aware LLM Annotation framework (arXiv:2601.02370, 2026) uses generalizability theory to decompose five variance sources (construct, interface, model, output, aggregation), reporting 12–85 pp outcome shifts from minor design choices, but provides protocol guidance rather than statistical inference.\n\n**Measurement error correction.** Messing (arXiv:2604.11581, 2026) decomposes LLM pipeline uncertainty into variance components (prompt phrasing, temperature, judge model) and proposes TEE-corrected standard errors. This framework addresses measurement error within a design-study projection paradigm—it corrects the confidence interval around a single estimate but does not construct or traverse a multiverse of defensible configurations, nor does it classify pipeline dimensions or provide specification-curve-based joint inference. Our work is complementary: Messing's TEE can serve as the per-specification error estimator within each point on our specification curve, while our framework provides the global robustness assessment that TEE alone cannot deliver.\n\n**Single-pipeline correction.** DSL (Egami et al., NeurIPS 2023) uses a small human-label set to debias LLM annotations for downstream inference; CDI (Gligorić et al., NAACL 2025) combines LLM confidence scores with human labels for efficient estimation; Audinet de Pieuchon et al. (EMNLP 2025) benchmark DSL vs PPI across annotation budgets. All three assume a fixed pipeline configuration. They solve pipeline-internal error but are blind to pipeline-external robustness: if a researcher had chosen a different model or prompt, would the corrected conclusion still hold? This is the gap our framework fills.\n\n**Perspectivism.** Mehrotra et al. (arXiv:2603.21404, 2026) propose Perspective-Driven Inference for subjective annotation tasks, treating different LLM perspectives as legitimate viewpoints rather than errors. This reinforces our argument that for subjective tasks (sentiment, toxicity, stance), pipeline variation is not merely noise to be corrected but a substantive dimension that multiverse analysis should expose.\n\n**Multiverse methodology.** Simonsohn et al. (Nature Human Behaviour, 2020) formalize specification curve analysis: enumerate justified specifications, visualize the distribution of effects, and conduct permutation-based joint inference. Del Giudice & Gangestad (AMPPS, 2021) propose the E/N/U classification framework—Type E (equivalent: defensible alternatives that should all appear in the multiverse), Type N (nonequivalent: one option is clearly superior and should be fixed), Type U (uncertain: run separate multiverses under each option)—to discipline which specifications enter the multiverse. Auspurg (PNAS 2025) critiques brute-force multiverse analysis for mixing justified and unjustified models, diluting true signals; Ganslmeier & Vlandas (PNAS 2025) reply that restricting to \"justified\" models is itself contested. This debate remains unresolved in social science. Carlson & Burbano (SMJ 2026) recommend informal sensitivity analysis (run a few model+prompt combinations and check consistency) as practical guidance for management researchers.\n\n### Opportunity and Core Argument\n\n**The gap.** No existing work applies formal multiverse methodology—specification curve analysis with principled multiverse construction and joint statistical inference—to LLM annotation pipelines.\n\n**Why LLM annotation is an epistemically ideal setting for multiverse analysis.** Auspurg's (PNAS 2025) central critique of multiverse analysis—that it conflates justified and unjustified specifications, producing meaningless variance—rests on three conditions that are typically hard to satisfy in social science: (a) the estimand must remain constant across specifications, (b) included specifications must not be misspecified, and (c) researchers need a principled basis for classifying which specifications are defensible. LLM annotation pipelines satisfy all three conditions in ways that traditional social science modeling does not:\n\n- **(a) Constant estimand.** All pipeline configurations target the same annotation label for the same text—the estimand is defined by the coding scheme, not by the model. Unlike regression multiverse (where changing covariates may change the estimand), changing the model or prompt does not change what we are trying to measure.\n- **(b) No misspecification in the classical sense.** Each pipeline configuration is a deterministic (or stochastic with known seed) mapping from text to label. There is no omitted-variable bias or functional-form misspecification—only measurement quality variation.\n- **(c) Principled E/N/U classification is feasible.** Pipeline dimensions have well-defined semantics (model architecture, prompt verbosity, temperature value) with clear task-conditional constraints that make E/N/U classification less contested than in regression multiverse.\n\nThis epistemological argument is a core intellectual contribution of this paper: it demonstrates that the Auspurg critique, while valid for many social science applications, does not apply to LLM annotation, thereby establishing the first positive case where exhaustive multiverse enumeration is both theoretically justified and practically feasible.\n\n**Why principled multiverse, not ad hoc sensitivity checks?** Carlson & Burbano (SMJ 2026) and common practice suggest running 3–5 model+prompt combinations as informal sensitivity analysis. This is insufficient for three reasons: (1) ad hoc selection of configurations may cluster in a narrow region of the specification space, missing dimensions or interactions that reverse conclusions (McLaren et al. 2026 show interactions dominate); (2) without a principled construction of the defensible space, there is no basis for claiming \"I have checked enough\"; (3) ad hoc checks provide no formal joint inference—no p-value for \"the finding is robust across the defensible space.\" Our framework provides all three: principled construction (E/N/U), exhaustive traversal, and permutation-based joint significance testing.\n\n**Why multiverse, not just measurement error correction?** Messing's (arXiv:2604.11581) TEE framework corrects the standard error of a single estimate by accounting for pipeline variance components. This answers \"how uncertain is my point estimate?\" Our specification curve analysis answers the distinct question: \"across the entire space of defensible configurations, does my conclusion hold?\" These are complementary: TEE provides local precision, multiverse provides global robustness. A finding can have a narrow TEE-corrected CI (precise) yet be fragile across the multiverse (not robust to pipeline choice), or vice versa.\n\n### Approach\n\n**Stage 1: E/N/U Multiverse Construction (Primary Methodological Contribution)**\n\nAdapt the Del Giudice & Gangestad (AMPPS, 2021) E/N/U classification framework to LLM annotation pipeline dimensions. This adaptation is the paper's primary methodological contribution—no prior work has systematically classified LLM pipeline decisions using this framework.\n\nFive pipeline dimensions, each classified as E, N, or U with task-conditional rules:\n\n| Dimension | Options | Default classification | Task-conditional overrides |\n|-----------|---------|----------------------|---------------------------|\n| Model | 6 models (see below) | Type E | — |\n| Prompt template | 3 variants (minimal / instructed / chain-of-thought) | Type E | For simple binary tasks, CoT may be Type N (unnecessary complexity) |\n| Temperature | {0, 0.3, 0.7} | Type U | For deterministic factual tasks → temperature=0 is Type N; for subjective tasks → all three are Type E |\n| System instruction | {generic, domain-specific, none} | Type E | — |\n| Output parsing | {regex, structured JSON, first-token} | Type E for well-defined tasks | For free-form tasks → Type U |\n\nNaïve Cartesian product: 6 × 3 × 3 × 3 × 3 = 486 configurations per model choice, or 810 if model is included. After E/N/U pruning (fixing Type N to best option, splitting Type U into separate sub-multiverses), the defensible multiverse contains approximately 90–270 configurations per task, depending on task-type-triggered overrides.\n\nClassification criteria are formalized in a Boba-style DSL (Liu et al., CHI 2021) that encodes task-conditional constraints as executable rules, ensuring reproducibility and transparency of multiverse construction decisions.\n\n**E/N/U classification criteria (systematic rubric):**\n- **Type E**: Multiple options are defensible and no prior evidence or theoretical argument favors one over others for the given task type.\n- **Type N**: One option is clearly superior based on prior evidence (e.g., temperature=0 for factual extraction where determinism is preferred) or theoretical argument (e.g., CoT is unnecessary overhead for simple binary classification).\n- **Type U**: Genuine uncertainty about whether options target the same construct (e.g., temperature variation for subjective tasks may elicit different but legitimate annotation perspectives).\n\n**Stage 2: Specification Curve Analysis + Joint Inference**\n\nFor each task, execute all configurations in the pruned multiverse across all 6 models. For each configuration, compute the downstream hypothesis test (e.g., group comparison, correlation, regression coefficient) on the annotated data. Apply the specification curve methodology of Simonsohn et al. (Nature Human Behaviour, 2020):\n\n1. Rank specifications by effect size and visualize as a specification curve.\n2. Classify each hypothesis as **robust** (sign-consistent and jointly significant), **fragile** (sign-consistent but not jointly significant), or **sign-inconsistent** (effect direction reverses across defensible configurations).\n3. Conduct permutation-based joint inference (≥500 permutations): under the null, randomly shuffle the mapping between pipeline dimensions and annotations, re-compute the specification curve, and derive a joint p-value for the hypothesis of non-zero effect across the multiverse. Importantly, permutation re-computation operates on downstream statistics from cached annotation outputs—no re-annotation required, making this computationally feasible.\n\n**Stage 3: Variance Decomposition**\n\nDecompose specification-curve variance using factorial ANOVA over the full-factorial annotation results, quantifying the contribution of each pipeline dimension (model, prompt, temperature, system instruction, parsing) and their interactions to downstream inference instability. Model is nested within model-size class (large: >250B parameters; medium: <130B) to disentangle architecture/family effects from scale effects. Report main effects, two-way interactions, and the proportion of variance attributable to each source. Compare this downstream-inference-focused decomposition with Messing's (arXiv:2604.11581) annotation-accuracy-focused TEE decomposition on the same configurations, testing whether annotation accuracy variance predicts inference instability (they need not correlate—a model may produce biased but consistent annotations that support the same directional conclusion).\n\n### Experimental Design\n\n**Data source.** Baumann et al. (arXiv:2509.08825) public dataset (MIT license): 18 LLMs × 37 tasks × 13M labels with gold-standard human annotations.\n\n**Task selection.** 10 tasks selected from Baumann's 37, stratified to cover: binary classification (3 tasks), multi-class classification (3 tasks), ordinal rating (2 tasks), and subjective/contested annotation (2 tasks, e.g., sentiment, toxicity). Selection criteria: (i) gold labels available, (ii) sample size ≥1,000, (iii) task has a natural downstream hypothesis (group comparison or correlation) testable on the annotated data. Specific tasks and their downstream hypotheses will be pre-registered.\n\n**Models.** 6 models spanning architecture families, scale, and openness:\n- Open-weight large MoE: Llama 4 Maverick (400B MoE), Qwen 3.5 (397B MoE, 17B active; released Feb 2026, Apache 2.0)\n- Open-weight medium: Gemma 4 (26B MoE)\n- Proprietary anchor: GPT-4o (chosen over Claude to avoid circularity with any LLM-assisted E/N/U classification process)\n- Two additional models selected to fill gaps in the architecture/scale matrix (e.g., one dense mid-scale model, one additional proprietary model)\n\nModel size is recorded as a covariate/nested factor in the ANOVA to disentangle scale effects from family effects (补充: Baumann et al. 2025 find small LLMs roughly double hacking risk; McLaren et al. 2026 find model choice significant even among similar-scale models).\n\n**Execution.** Full-factorial execution of the pruned multiverse per task. Annotation uses 25-item batched prompts to reduce API overhead. Estimated total: 500M–1.2B tokens across all models, with cost estimated at $1,200–$2,000 (to be validated by pilot run on 1–2 tasks before full execution). A pilot run on 2 tasks (~$50–100) will verify token consumption estimates and annotation quality.\n\n**Evaluation and baselines.**\n1. *Specification curve + joint inference*: For each of the 10 tasks, produce specification curves and classify hypotheses as robust/fragile/sign-inconsistent.\n2. *Comparative evaluation with PPI/DSL*: On 2–3 representative tasks, run PPI (Gligorić et al., NAACL 2025) and DSL (Egami et al., NeurIPS 2023) using Baumann's gold labels as the human-annotation budget. Compare: (a) when multiverse says \"robust,\" does PPI/DSL-corrected inference agree? (b) when multiverse says \"fragile,\" can PPI/DSL resolve the fragility? This positions the two paradigms as complementary rather than competing.\n3. *Variance decomposition*: Factorial ANOVA with model size as nested factor, reporting main effects and interactions.\n4. *TEE comparison*: On the same configurations, compute Messing-style TEE decomposition alongside our downstream-inference decomposition; report correlation between annotation-accuracy variance and inference instability.\n\n**Ablation studies** (on 2–3 representative tasks):\n1. *E/N/U sensitivity analysis*: Perturb E/N/U boundary decisions (reclassify selected N→U or expand E ranges) and compare resulting specification curves and robustness classifications. Also compare the principled (E/N/U-pruned) multiverse against the naïve (full Cartesian product) multiverse to quantify the impact of principled pruning on robustness conclusions. This directly addresses Auspurg's (PNAS 2025) critique with empirical evidence.\n2. *Task-conditional constraint effect*: Remove task-type-specific constraints (e.g., allow all temperatures for deterministic tasks) and measure change in specification curve shape and robustness classification.\n3. *Model diversity curve*: Compute robustness classifications using 6 models, then 3 models, then 1 model; report stability of conclusions as a function of model count. This informs practical adoption—researchers with limited budgets need to know the minimum model diversity for reliable robustness assessment.\n4. *Batch size pilot*: Compare batch=25 vs batch=1 annotation on ≥1 task with ≥1 model to verify batching does not systematically degrade annotation quality.\n\n### Expected Contributions\n\n1. **Methodological (primary):** The first adaptation of E/N/U multiverse classification (Del Giudice & Gangestad, AMPPS 2021) to LLM annotation pipelines, with a task-conditional classification rubric formalized in executable DSL, enabling principled construction of the defensible configuration space.\n2. **Epistemological:** A formal argument that LLM annotation pipelines satisfy the conditions under which exhaustive multiverse analysis is theoretically justified—directly engaging the Auspurg (PNAS 2025) vs. Ganslmeier & Vlandas (PNAS 2025) debate and providing the first positive case study for principled exhaustive specification enumeration.\n3. **Empirical:** A robustness landscape across 10 CSS tasks: which tasks yield robust findings, which are fragile, which pipeline dimensions and interactions drive instability, and how principled multiverse assessment compares with both ad hoc sensitivity checks and PPI/DSL correction.\n\n### Budget and Feasibility\n\n- **API costs:** $1,200–$2,000 total (6 models × 10 tasks × 90–270 configs × 1,000–3,000 samples; batched at 25 items/prompt). Qwen 3.5 and Llama 4 Maverick via OpenRouter; GPT-4o via OpenAI API. Pilot run ($50–100) precedes full execution.\n- **Compute:** Permutation tests (≥500 permutations) and ANOVA operate on cached annotation outputs—no re-annotation required. Estimated compute for post-annotation analysis: <24 hours on a single GPU/CPU cluster.\n- **Data:** Baumann et al. public dataset (MIT license). No additional data collection or human annotation required (gold labels pre-exist).\n- **Timeline:** Pilot (1 week) → Full annotation (2–3 weeks, parallelized across models) → Analysis and ablations (2–3 weeks) → Writing (3–4 weeks). Total: ~8–10 weeks to submission-ready manuscript."
}
```

---

### Runtime record

_source line 2 · 2026-05-20T04:02:22.912Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T04:02:22.912Z",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d"
}
```

---

## Round 1

42 recorded events

### User

_source line 3 · 2026-05-20T04:02:22.926Z_

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
  "promptId": "95a611a0-5f01-4610-9b3e-1c678c101211",
  "type": "user",
  "uuid": "1756b032-12e9-484e-af38-9f59183cbc48",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T04:02:22.925Z_

```json
{
  "parentUuid": "1756b032-12e9-484e-af38-9f59183cbc48",
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
  "uuid": "a9bf9446-a574-4310-a241-88ee573b2ff8",
  "timestamp": "2026-05-20T04:02:22.925Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T04:02:22.925Z_

```json
{
  "parentUuid": "a9bf9446-a574-4310-a241-88ee573b2ff8",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ee555009-e9e7-4adb-b1e1-a22e16714055",
  "timestamp": "2026-05-20T04:02:22.925Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d",
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
  "leafUuid": "ee555009-e9e7-4adb-b1e1-a22e16714055",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Specification curve analysis for LLM annotation robustness",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d"
}
```

---

### Assistant

_source line 8 · 2026-05-20T04:02:33.464Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully read and analyze this proposal before doing any web searches. The proposal is about applying specification curve analysis (multiverse analysis) to LLM annotation pipelines in computational social science. Let me understand the key claims:

1. LLM annotation pipelines have many researcher degrees of freedom (model, prompt, temperature, etc.)
2. Existing work diagnoses instability but doesn't provide inferential frameworks
3. Existing correction methods (DSL, PPI/CDI) work within a single pipeline but don't assess cross-pipeline robustness
4. The proposal adapts the E/N/U classification framework from Del Giudice & Gangestad to LLM pipelines


5. There's an epistemological argument that LLM pipelines meet the conditions justifying exhaustive multiverse analysis, which would address Auspurg's critique of the approach

Now I need to search the literature to understand the current landscape and whether this work is already being done elsewhere. I'm looking for recent developments in LLM annotation robustness, any existing applications of specification curve analysis to LLM pipelines, the ongoing debate around multiverse analysis validity, and how E/N/U classification might apply in computational contexts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee555009-e9e7-4adb-b1e1-a22e16714055",
  "isSidechain": false,
  "requestId": "req_011CbD9yTQmWNCwHr9npyKH9",
  "type": "assistant",
  "uuid": "ce51901a-f22c-47f3-a061-f4905cf61fb4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DFERf6bA8VuEp3nH4zjhUU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6076,
      "cache_read_input_tokens": 14549,
      "output_tokens": 424,
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
          "output_tokens": 424,
          "cache_read_input_tokens": 14549,
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

_source line 9 · 2026-05-20T04:02:33.466Z_

I'll start by reading the proposal carefully and then conducting targeted web searches to understand the current landscape before making any assessments.

Let me do my pre-assessment literature searches in parallel:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce51901a-f22c-47f3-a061-f4905cf61fb4",
  "isSidechain": false,
  "requestId": "req_011CbD9yTQmWNCwHr9npyKH9",
  "type": "assistant",
  "uuid": "6917f6e9-53c5-4de9-a771-5798b28f5846",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DFERf6bA8VuEp3nH4zjhUU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6076,
      "cache_read_input_tokens": 14549,
      "output_tokens": 424,
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
          "output_tokens": 424,
          "cache_read_input_tokens": 14549,
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

_source line 10 · 2026-05-20T04:02:33.469Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NJuNjxMUPPA8bTzTt1bqnf`</summary>

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
  "parentUuid": "6917f6e9-53c5-4de9-a771-5798b28f5846",
  "isSidechain": false,
  "requestId": "req_011CbD9yTQmWNCwHr9npyKH9",
  "type": "assistant",
  "uuid": "e47fe5f6-d5af-407b-abd4-0eba110533a3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DFERf6bA8VuEp3nH4zjhUU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6076,
      "cache_read_input_tokens": 14549,
      "output_tokens": 424,
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
          "output_tokens": 424,
          "cache_read_input_tokens": 14549,
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

_source line 11 · 2026-05-20T04:02:33.476Z_

<details><summary>↩ Tool result · `toolu_01NJuNjxMUPPA8bTzTt1bqnf`</summary>

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
  "parentUuid": "e47fe5f6-d5af-407b-abd4-0eba110533a3",
  "isSidechain": false,
  "promptId": "95a611a0-5f01-4610-9b3e-1c678c101211",
  "type": "user",
  "uuid": "9b9cd139-ab31-4f5e-b892-58b10b5c9892",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "e47fe5f6-d5af-407b-abd4-0eba110533a3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-20T04:02:36.746Z_

Now let me conduct my targeted literature searches in parallel:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b9cd139-ab31-4f5e-b892-58b10b5c9892",
  "isSidechain": false,
  "requestId": "req_011CbD9zFA6sCrkdxC4cZXZz",
  "type": "assistant",
  "uuid": "68638b77-5231-4a3e-a4d8-e9cd80f8f010",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mck2SvQV6TV6Z1YFhvhZuA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 951,
      "cache_read_input_tokens": 20625,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 951,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 81,
          "cache_read_input_tokens": 20625,
          "cache_creation_input_tokens": 951,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 951
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

_source line 13 · 2026-05-20T04:02:36.932Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01M4nxDSxnSwWVqfRn7zBKWa`</summary>

```json
{
  "query": "specification curve analysis multiverse analysis LLM annotation pipeline 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68638b77-5231-4a3e-a4d8-e9cd80f8f010",
  "isSidechain": false,
  "requestId": "req_011CbD9zFA6sCrkdxC4cZXZz",
  "type": "assistant",
  "uuid": "fe2baf07-4840-4162-8258-f7cc5484afec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mck2SvQV6TV6Z1YFhvhZuA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 951,
      "cache_read_input_tokens": 20625,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 951,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 81,
          "cache_read_input_tokens": 20625,
          "cache_creation_input_tokens": 951,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 951
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

_source line 14 · 2026-05-20T04:02:44.232Z_

<details><summary>↩ Tool result · `toolu_01M4nxDSxnSwWVqfRn7zBKWa`</summary>

```text
Web search results for query: "specification curve analysis multiverse analysis LLM annotation pipeline 2025 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2510.27246"},{"title":"Multi-Perspective LLM Annotations for Valid Analyses in Subjective Tasks","url":"https://arxiv.org/html/2603.21404"},{"title":"Specification curve analysis and the multiverse | Statistical Modeling, Causal Inference, and Social Science","url":"https://statmodeling.stat.columbia.edu/2024/11/12/specification-curve-analysis-and-the-multiverse/"},{"title":"Visualizing vastness: Graphical methods for multiverse analysis","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12875576/"},{"title":"Specification Curve Analysis | FORRT - Framework for Open and Reproducible Research Training","url":"https://forrt.org/glossary/english/specification_curve_analysis/"},{"title":"A large-scale pipeline for automatic corpus annotation using LLMs: variation and change in the English consider construction","url":"https://arxiv.org/pdf/2510.12306"},{"title":"Variance-Aware LLM Annotation for Strategy Research: Sources, Diagnostics, and a Protocol for Reliable Measurement","url":"https://arxiv.org/pdf/2601.02370"},{"title":"Exploring the multiverse of analysis options for the alcohol Stroop","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11133151/"}]

I've completed the web search for your query. Here's a summary of the relevant findings:

## Key Results

**LLM Annotation Pipelines (2025-2026):**

LLM annotation pipelines can combine automated synthesis with human validation, where LLMs first produce candidate annotations which annotators review to select valid ones. 

Large language models represent a potentially transformative solution to annotation challenges, with conversational LLMs like ChatGPT and Claude able to be prompted in natural language to perform sophisticated classification tasks with minimal setup.

Researchers use LLMs to annotate, score, rank, and classify text corpora across various domains including business plans, investor pitches, and corporate disclosures. However, LLM annotations are not deterministic or unbiased, and LLM annotation output can be characterized by undesired variance that must be understood and mitigated if used as data in studies.

**Specification Curve & Multiverse Analysis (2025-2026):**

Multiverse analysis is an increasingly popular tool for improving robustness and transparency of empirical research, though visualization techniques for multiverse analysis are underdeveloped, with researchers identifying critical weaknesses in existing multiverse visualizations like specification curves and density plots.

Multiverse plots overcome key limitations by eliminating arbitrary sampling and information loss, effectively showing what conclusions a dataset can reasonably support and which researcher decisions drive variation in results.

The search results show active recent research combining these methodologies for more robust and transparent empirical analysis.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe2baf07-4840-4162-8258-f7cc5484afec",
  "isSidechain": false,
  "promptId": "95a611a0-5f01-4610-9b3e-1c678c101211",
  "type": "user",
  "uuid": "2d3a9c6d-672c-4ce2-b528-54472d6952fc",
  "toolUseResult": {
    "query": "specification curve analysis multiverse analysis LLM annotation pipeline 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VPKwqKCpXzpF4DKWTSZdvi",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2510.27246"
          },
          {
            "title": "Multi-Perspective LLM Annotations for Valid Analyses in Subjective Tasks",
            "url": "https://arxiv.org/html/2603.21404"
          },
          {
            "title": "Specification curve analysis and the multiverse | Statistical Modeling, Causal Inference, and Social Science",
            "url": "https://statmodeling.stat.columbia.edu/2024/11/12/specification-curve-analysis-and-the-multiverse/"
          },
          {
            "title": "Visualizing vastness: Graphical methods for multiverse analysis",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12875576/"
          },
          {
            "title": "Specification Curve Analysis | FORRT - Framework for Open and Reproducible Research Training",
            "url": "https://forrt.org/glossary/english/specification_curve_analysis/"
          },
          {
            "title": "A large-scale pipeline for automatic corpus annotation using LLMs: variation and change in the English consider construction",
            "url": "https://arxiv.org/pdf/2510.12306"
          },
          {
            "title": "Variance-Aware LLM Annotation for Strategy Research: Sources, Diagnostics, and a Protocol for Reliable Measurement",
            "url": "https://arxiv.org/pdf/2601.02370"
          },
          {
            "title": "Exploring the multiverse of analysis options for the alcohol Stroop",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11133151/"
          }
        ]
      },
      "I've completed the web search for your query. Here's a summary of the relevant findings:\n\n## Key Results\n\n**LLM Annotation Pipelines (2025-2026):**\n\nLLM annotation pipelines can combine automated synthesis with human validation, where LLMs first produce candidate annotations which annotators review to select valid ones. \n\nLarge language models represent a potentially transformative solution to annotation challenges, with conversational LLMs like ChatGPT and Claude able to be prompted in natural language to perform sophisticated classification tasks with minimal setup.\n\nResearchers use LLMs to annotate, score, rank, and classify text corpora across various domains including business plans, investor pitches, and corporate disclosures. However, LLM annotations are not deterministic or unbiased, and LLM annotation output can be characterized by undesired variance that must be understood and mitigated if used as data in studies.\n\n**Specification Curve & Multiverse Analysis (2025-2026):**\n\nMultiverse analysis is an increasingly popular tool for improving robustness and transparency of empirical research, though visualization techniques for multiverse analysis are underdeveloped, with researchers identifying critical weaknesses in existing multiverse visualizations like specification curves and density plots.\n\nMultiverse plots overcome key limitations by eliminating arbitrary sampling and information loss, effectively showing what conclusions a dataset can reasonably support and which researcher decisions drive variation in results.\n\nThe search results show active recent research combining these methodologies for more robust and transparent empirical analysis."
    ],
    "durationSeconds": 7.294462685999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fe2baf07-4840-4162-8258-f7cc5484afec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T04:02:48.445Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FgNoUZeTecGYBeNjYsbiu2`</summary>

```json
{
  "query": "Baumann et al 2025 LLM hacking risk annotation arXiv 2509.08825 follow-up work"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d3a9c6d-672c-4ce2-b528-54472d6952fc",
  "isSidechain": false,
  "requestId": "req_011CbDA12VdDWmD5EQeDhaFr",
  "type": "assistant",
  "uuid": "f4da20c2-4422-42f0-8ca4-6316d0686c0d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LVfTcdaQi6oP9q3JucNDXA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 838,
      "cache_read_input_tokens": 21576,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 838,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 21576,
          "cache_creation_input_tokens": 838,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 838
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

_source line 16 · 2026-05-20T04:02:57.644Z_

<details><summary>↩ Tool result · `toolu_01FgNoUZeTecGYBeNjYsbiu2`</summary>

```text
Web search results for query: "Baumann et al 2025 LLM hacking risk annotation arXiv 2509.08825 follow-up work"

Links: [{"title":"[2509.08825] Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation","url":"https://arxiv.org/abs/2509.08825"},{"title":"[2509.08825v2] Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation","url":"https://arxiv.org/abs/2509.08825v2"},{"title":"Paper page - Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation","url":"https://huggingface.co/papers/2509.08825"},{"title":"LLM Hacking Risks in Text Annotation","url":"https://www.emergentmind.com/papers/2509.08825"},{"title":"Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation","url":"https://arxiv.org/html/2509.08825v1"},{"title":"Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation | Request PDF","url":"https://www.researchgate.net/publication/395402972_Large_Language_Model_Hacking_Quantifying_the_Hidden_Risks_of_Using_LLMs_for_Text_Annotation"},{"title":"Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs","url":"https://arxiv.org/pdf/2509.08825"},{"title":"Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation | Scilit","url":"https://www.scilit.com/publications/e01f55e0f27c068e1a51cfa94f8cb986"},{"title":"Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/large-language-model-hacking-quantifying-hidden-risks"},{"title":"Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2509.08825"}]

I found the Baumann et al. 2025 paper on arXiv. Here's what I found:

## Paper Overview

The paper "Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation" is authored by Joachim Baumann, Paul Röttger, Aleksandra Urman, Albert Wendsjö, Flor Miriam Plaza-del-Arco, Johannes B. Gruber, and Dirk Hovy.

## Key Findings

The study found incorrect conclusions in approximately 31% of hypotheses for state-of-the-art LLMs, and in half the hypotheses for smaller language models. The research quantified the risk of LLM hacking by replicating 37 data annotation tasks from 21 published social science research studies with 18 different models, analyzing 13 million LLM labels and testing 2,361 realistic hypotheses.

## Mitigation Strategies

The authors analyzed 21 mitigation techniques and found that human annotations provide crucial protection against false positives. The risk of LLM hacking decreases as effect sizes increase, indicating the need for more rigorous verification of LLM-based findings near significance thresholds.

However, I did not find specific information about follow-up work to this paper in these search results. If you're looking for papers that cite or build upon this work, please let me know and I can search for that specifically.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4da20c2-4422-42f0-8ca4-6316d0686c0d",
  "isSidechain": false,
  "promptId": "95a611a0-5f01-4610-9b3e-1c678c101211",
  "type": "user",
  "uuid": "be1124f2-c875-43f4-8b1f-2ccce12af227",
  "toolUseResult": {
    "query": "Baumann et al 2025 LLM hacking risk annotation arXiv 2509.08825 follow-up work",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QKBf7YcfMVVURn3impPkAD",
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
            "title": "Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation",
            "url": "https://arxiv.org/html/2509.08825v1"
          },
          {
            "title": "Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation | Request PDF",
            "url": "https://www.researchgate.net/publication/395402972_Large_Language_Model_Hacking_Quantifying_the_Hidden_Risks_of_Using_LLMs_for_Text_Annotation"
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
      "I found the Baumann et al. 2025 paper on arXiv. Here's what I found:\n\n## Paper Overview\n\nThe paper \"Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation\" is authored by Joachim Baumann, Paul Röttger, Aleksandra Urman, Albert Wendsjö, Flor Miriam Plaza-del-Arco, Johannes B. Gruber, and Dirk Hovy.\n\n## Key Findings\n\nThe study found incorrect conclusions in approximately 31% of hypotheses for state-of-the-art LLMs, and in half the hypotheses for smaller language models. The research quantified the risk of LLM hacking by replicating 37 data annotation tasks from 21 published social science research studies with 18 different models, analyzing 13 million LLM labels and testing 2,361 realistic hypotheses.\n\n## Mitigation Strategies\n\nThe authors analyzed 21 mitigation techniques and found that human annotations provide crucial protection against false positives. The risk of LLM hacking decreases as effect sizes increase, indicating the need for more rigorous verification of LLM-based findings near significance thresholds.\n\nHowever, I did not find specific information about follow-up work to this paper in these search results. If you're looking for papers that cite or build upon this work, please let me know and I can search for that specifically."
    ],
    "durationSeconds": 9.194002777000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f4da20c2-4422-42f0-8ca4-6316d0686c0d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T04:03:00.258Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NPAjixzQjyoybRwx1fYceN`</summary>

```json
{
  "query": "Messing 2026 TEE standard errors LLM pipeline variance arXiv 2604.11581"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be1124f2-c875-43f4-8b1f-2ccce12af227",
  "isSidechain": false,
  "requestId": "req_011CbDA21qDbMJY6KjKj9CFT",
  "type": "assistant",
  "uuid": "17b70612-8676-4dac-acdb-768dcad8ccf2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RN4kfaPYW29rDmEbRp2nnz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1037,
      "cache_read_input_tokens": 22414,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1037,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 22414,
          "cache_creation_input_tokens": 1037,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1037
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

_source line 18 · 2026-05-20T04:03:06.789Z_

<details><summary>↩ Tool result · `toolu_01NPAjixzQjyoybRwx1fYceN`</summary>

```text
Web search results for query: "Messing 2026 TEE standard errors LLM pipeline variance arXiv 2604.11581"

Links: [{"title":"Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking","url":"https://arxiv.org/html/2604.11581"},{"title":"[2604.11581] Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking","url":"https://arxiv.org/abs/2604.11581"},{"title":"Variance-Aware LLM Annotation for Strategy Research: Sources, Diagnostics, and a Protocol for Reliable Measurement","url":"https://arxiv.org/pdf/2601.02370"},{"title":"Development of an LLM Pipeline Surpassing Physicians in Cardiovascular Risk Score Calculation","url":"https://www.medrxiv.org/content/10.1101/2025.11.11.25340002.full.pdf"},{"title":"A model of errors in transformers","url":"https://arxiv.org/pdf/2601.14175"},{"title":"Understanding LLM Failures: A Multi-Tape Turing Machine Analysis of Systematic Errors in Language Model Reasoning","url":"https://arxiv.org/pdf/2602.15868"}]

Based on the search results, I found the paper you're looking for:

The paper "Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking" (arXiv:2604.11581) is authored by Solomon Messing from the Center for Social Media, AI, and Politics at New York University, with a version dated May 7, 2026.

**Key findings:**

The paper shows that standard confidence intervals ignore variability from judge model choice, model temperature, and prompt phrasing, producing under-coverage that worsens with more data.

The paper decomposes LLM pipeline uncertainty into its sources, distinguishes variance that shrinks with more data from sensitivity to researcher design choices, and uses design-study projections to reduce total evaluation error (TEE).

**Performance metrics:**

Across demonstrations, naive standard errors are 40-60% smaller than the TEE-corrected standard errors, and using Chatbot Arena data, naive 95% confidence interval coverage drops as sample size grows while TEE-corrected coverage holds at 95%.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "17b70612-8676-4dac-acdb-768dcad8ccf2",
  "isSidechain": false,
  "promptId": "95a611a0-5f01-4610-9b3e-1c678c101211",
  "type": "user",
  "uuid": "18bbf7a1-49e8-4523-b23f-3ecd3281d3b6",
  "toolUseResult": {
    "query": "Messing 2026 TEE standard errors LLM pipeline variance arXiv 2604.11581",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Cy7dHUhJVN9rDV5SDGjUum",
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
            "title": "Variance-Aware LLM Annotation for Strategy Research: Sources, Diagnostics, and a Protocol for Reliable Measurement",
            "url": "https://arxiv.org/pdf/2601.02370"
          },
          {
            "title": "Development of an LLM Pipeline Surpassing Physicians in Cardiovascular Risk Score Calculation",
            "url": "https://www.medrxiv.org/content/10.1101/2025.11.11.25340002.full.pdf"
          },
          {
            "title": "A model of errors in transformers",
            "url": "https://arxiv.org/pdf/2601.14175"
          },
          {
            "title": "Understanding LLM Failures: A Multi-Tape Turing Machine Analysis of Systematic Errors in Language Model Reasoning",
            "url": "https://arxiv.org/pdf/2602.15868"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nThe paper \"Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking\" (arXiv:2604.11581) is authored by Solomon Messing from the Center for Social Media, AI, and Politics at New York University, with a version dated May 7, 2026.\n\n**Key findings:**\n\nThe paper shows that standard confidence intervals ignore variability from judge model choice, model temperature, and prompt phrasing, producing under-coverage that worsens with more data.\n\nThe paper decomposes LLM pipeline uncertainty into its sources, distinguishes variance that shrinks with more data from sensitivity to researcher design choices, and uses design-study projections to reduce total evaluation error (TEE).\n\n**Performance metrics:**\n\nAcross demonstrations, naive standard errors are 40-60% smaller than the TEE-corrected standard errors, and using Chatbot Arena data, naive 95% confidence interval coverage drops as sample size grows while TEE-corrected coverage holds at 95%."
    ],
    "durationSeconds": 6.526416990999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "17b70612-8676-4dac-acdb-768dcad8ccf2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T04:03:09.344Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013LSm3nZGoKjjfFrw6PnxZ9`</summary>

```json
{
  "query": "Auspurg PNAS 2025 multiverse analysis critique brute force specification \"Del Giudice\" E/N/U classification"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18bbf7a1-49e8-4523-b23f-3ecd3281d3b6",
  "isSidechain": false,
  "requestId": "req_011CbDA2gsUYkyiSTe9ToYNw",
  "type": "assistant",
  "uuid": "3e11650e-ae4f-4182-a4d4-b4fc6951f97d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SixJw61Qrc5e6BVKtXUZp1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 674,
      "cache_read_input_tokens": 23451,
      "output_tokens": 83,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 674,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 83,
          "cache_read_input_tokens": 23451,
          "cache_creation_input_tokens": 674,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 674
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
  "leafUuid": "3e11650e-ae4f-4182-a4d4-b4fc6951f97d",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Specification curve analysis for LLM annotation robustness",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d"
}
```

---

### Tool result

_source line 22 · 2026-05-20T04:03:28.354Z_

<details><summary>↩ Tool result · `toolu_013LSm3nZGoKjjfFrw6PnxZ9`</summary>

```text
Web search results for query: "Auspurg PNAS 2025 multiverse analysis critique brute force specification "Del Giudice" E/N/U classification"

Links: [{"title":"What’s a multiverse good for anyway?","url":"https://sites.stat.columbia.edu/gelman/research/unpublished/rohrer_multiverse.pdf"},{"title":"What’s a multiverse good for anyway?","url":"https://juliarohrer.com/wp-content/uploads/2026/02/multiverse_draft-preprint-version.pdf"},{"title":"Robustness is better assessed with a few thoughtful models than with billions of regressions | PNAS","url":"https://www.pnas.org/doi/10.1073/pnas.2521917122"},{"title":"Robustness is better assessed with a few thoughtful models than with billions of regressions - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12582322/"},{"title":"Toward a more credible assessment of the credibility of science by many-analyst studies - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11420151/"},{"title":"Reply to Auspurg: On the limits of “justified” model spaces | PNAS","url":"https://www.pnas.org/doi/10.1073/pnas.2523374122"},{"title":"Reply to Auspurg: On the limits of “justified” model spaces","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12582334/"},{"title":"Observing many researchers using the same data and hypothesis reveals a hidden universe of uncertainty | PNAS","url":"https://www.pnas.org/doi/10.1073/pnas.2203150119"},{"title":"Toward a more credible assessment of the credibility of science by many-analyst studies | PNAS","url":"https://www.pnas.org/doi/10.1073/pnas.2404035121"}]

Now let me search for information about the E/N/U classification mentioned in your query:

Links: [{"title":"Can large language models assist choice modelling? Insights into prompting strategies and current models capabilities","url":"https://arxiv.org/pdf/2507.21790"},{"title":"Method for classifying test subjects in knowledge and functionality states","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5855011"},{"title":"Making Decisions under Model Misspecification","url":"https://arxiv.org/pdf/2008.01071"},{"title":"Modification Indices for Diagnostic Classification Models","url":"https://arxiv.org/pdf/2003.05880"},{"title":"Where do statistical models come from? Revisiting the problem of   specification","url":"https://arxiv.org/pdf/math/0610849"},{"title":"Framework for multi-criteria assessment of classification models for the purposes of credit scoring","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10237068/"},{"title":"Method and data processing system for specifying and applying rules to classification-based decision points in an application system","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6341369"},{"title":"Binary classification models with \"Uncertain\" predictions","url":"https://arxiv.org/pdf/1711.09677"}]

Let me search more specifically for the Del Giudice E/N/U framework:

Links: [{"title":"Researcher Degrees of Freedom","url":"https://www.numberanalytics.com/blog/ultimate-guide-researcher-degrees-freedom"},{"title":"Researcher degrees of freedom — Grokipedia","url":"https://grokipedia.com/page/researcher_degrees_of_freedom"},{"title":"Addressing researcher degrees of freedom through minP adjustment","url":"https://arxiv.org/pdf/2401.11537"},{"title":"Addressing researcher degrees of freedom through minP adjustment - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11253496/"},{"title":"Researcher degrees of freedom | FORRT - Framework for Open and Reproducible Research Training","url":"https://forrt.org/glossary/english/researcher_degrees_of_freedom/"},{"title":"Addressing researcher degrees of freedom through minP adjustment","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11253496/"},{"title":"Freedom of choice vs. undisclosed flexibility: Researcher degrees of freedom in model-based inference – I'm a Bayesian and I do what I want","url":"https://sites.uci.edu/joachim/2018/12/13/freedom-of-choice-vs-undisclosed-flexibility-researcher-degrees-of-freedom-in-model-based-inference/"},{"title":"Freedom of choice vs. undisclosed flexibility: Researcher degrees of freedom in model-based inference – Psychonomic Society Featured Content","url":"https://featuredcontent.psychonomic.org/freedom-of-choice-vs-undisclosed-flexibility-researcher-degrees-of-freedom-in-model-based-inference/"}]

Let me try one more specific search for the Del Giudice framework:

Links: [{"title":"Making Decisions under Model Misspecification","url":"https://arxiv.org/pdf/2008.01071"},{"title":"A recourse certainty equivalent for decisions under uncertainty | Annals of Operations Research | Springer Nature Link","url":"https://link.springer.com/article/10.1007/BF02204807"},{"title":"Qualitative Models for Decision Under Uncertainty without the   Commensurability Assumption","url":"https://arxiv.org/pdf/1301.6694"},{"title":"Modeling decision-making under uncertainty with qualitative outcomes","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11918403/"},{"title":"Uncertain Decisions Facilitate Better Preference Learning","url":"https://arxiv.org/pdf/2106.10394"}]

Let me try a more targeted search:

Links: [{"title":"Robustness is better assessed with a few thoughtful models than with billions of regressions | PNAS","url":"https://www.pnas.org/doi/10.1073/pnas.2521917122"},{"title":"Reply to Auspurg: On the limits of “justified” model spaces | PNAS","url":"https://www.pnas.org/doi/10.1073/pnas.2523374122"},{"title":"Reply to Auspurg: On the limits of “justified” model spaces","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12582334/"},{"title":"PNAS 2025 Vol. 122 No. 27 e2400928121\b","url":"https://www.pnas.org/doi/pdf/10.1073/pnas.2400928121"},{"title":"When the role of uncertainty is…uncertain | PNAS","url":"https://www.pnas.org/doi/10.1073/pnas.2305856120"},{"title":"Stochastic responses and marginal valuation | PNAS","url":"https://www.pnas.org/doi/abs/10.1073/pnas.2520857122?af=R"}]

Based on my web search results, I have found relevant information about the Auspurg PNAS 2025 debate on multiverse analysis and specification decisions. However, I was unable to find specific information about the "Del Giudice" E/N/U classification framework in my searches. Let me provide you with what I found:

## Summary of Search Results

Katrin Auspurg published a critique in PNAS 2025 responding to Ganslmeier and Vlandas who conducted an ambitious multiverse analysis estimating over 3.6 billion regression models across four political science topics. By varying estimation strategies, covariates, operationalizations, and samples, they documented drastic model instability with estimates often changing in sign or significance due to "minor alterations."

Auspurg argues that their approach substantially overstates uncertainty, asserting that multiverse analyses are only informative when all included models represent equally plausible strategies for estimating the same estimand.

Auspurg contends that the brute force of the multiverse cannot fix certain issues, and there is a risk that researchers mistake it for a silver bullet.

Auspurg concludes that multiverse analyses require thorough, theory-based model selection, otherwise they become a "dangerous tool" that drowns valid models in misspecified ones, needlessly eroding trust in science.

However, I was unable to locate information in the search results about the specific "Del Giudice E/N/U classification" framework you mentioned. If you have more details about this framework or would like me to search for other aspects of this debate, please let me know.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e11650e-ae4f-4182-a4d4-b4fc6951f97d",
  "isSidechain": false,
  "promptId": "95a611a0-5f01-4610-9b3e-1c678c101211",
  "type": "user",
  "uuid": "8c3fd52f-68f0-44b5-b64d-512d27c4afa2",
  "toolUseResult": {
    "query": "Auspurg PNAS 2025 multiverse analysis critique brute force specification \"Del Giudice\" E/N/U classification",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BuPBAQKj4mckM7xn9xzGSp",
        "content": [
          {
            "title": "What’s a multiverse good for anyway?",
            "url": "https://sites.stat.columbia.edu/gelman/research/unpublished/rohrer_multiverse.pdf"
          },
          {
            "title": "What’s a multiverse good for anyway?",
            "url": "https://juliarohrer.com/wp-content/uploads/2026/02/multiverse_draft-preprint-version.pdf"
          },
          {
            "title": "Robustness is better assessed with a few thoughtful models than with billions of regressions | PNAS",
            "url": "https://www.pnas.org/doi/10.1073/pnas.2521917122"
          },
          {
            "title": "Robustness is better assessed with a few thoughtful models than with billions of regressions - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12582322/"
          },
          {
            "title": "Toward a more credible assessment of the credibility of science by many-analyst studies - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11420151/"
          },
          {
            "title": "Reply to Auspurg: On the limits of “justified” model spaces | PNAS",
            "url": "https://www.pnas.org/doi/10.1073/pnas.2523374122"
          },
          {
            "title": "Reply to Auspurg: On the limits of “justified” model spaces",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12582334/"
          },
          {
            "title": "Observing many researchers using the same data and hypothesis reveals a hidden universe of uncertainty | PNAS",
            "url": "https://www.pnas.org/doi/10.1073/pnas.2203150119"
          },
          {
            "title": "Toward a more credible assessment of the credibility of science by many-analyst studies | PNAS",
            "url": "https://www.pnas.org/doi/10.1073/pnas.2404035121"
          }
        ]
      },
      "Now let me search for information about the E/N/U classification mentioned in your query:",
      {
        "tool_use_id": "srvtoolu_01Fv4CpYzQP9kKYRuHqAwb27",
        "content": [
          {
            "title": "Can large language models assist choice modelling? Insights into prompting strategies and current models capabilities",
            "url": "https://arxiv.org/pdf/2507.21790"
          },
          {
            "title": "Method for classifying test subjects in knowledge and functionality states",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5855011"
          },
          {
            "title": "Making Decisions under Model Misspecification",
            "url": "https://arxiv.org/pdf/2008.01071"
          },
          {
            "title": "Modification Indices for Diagnostic Classification Models",
            "url": "https://arxiv.org/pdf/2003.05880"
          },
          {
            "title": "Where do statistical models come from? Revisiting the problem of   specification",
            "url": "https://arxiv.org/pdf/math/0610849"
          },
          {
            "title": "Framework for multi-criteria assessment of classification models for the purposes of credit scoring",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10237068/"
          },
          {
            "title": "Method and data processing system for specifying and applying rules to classification-based decision points in an application system",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6341369"
          },
          {
            "title": "Binary classification models with \"Uncertain\" predictions",
            "url": "https://arxiv.org/pdf/1711.09677"
          }
        ]
      },
      "Let me search more specifically for the Del Giudice E/N/U framework:",
      {
        "tool_use_id": "srvtoolu_01LnBpminnB7q9tNyGmGHrkR",
        "content": [
          {
            "title": "Researcher Degrees of Freedom",
            "url": "https://www.numberanalytics.com/blog/ultimate-guide-researcher-degrees-freedom"
          },
          {
            "title": "Researcher degrees of freedom — Grokipedia",
            "url": "https://grokipedia.com/page/researcher_degrees_of_freedom"
          },
          {
            "title": "Addressing researcher degrees of freedom through minP adjustment",
            "url": "https://arxiv.org/pdf/2401.11537"
          },
          {
            "title": "Addressing researcher degrees of freedom through minP adjustment - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11253496/"
          },
          {
            "title": "Researcher degrees of freedom | FORRT - Framework for Open and Reproducible Research Training",
            "url": "https://forrt.org/glossary/english/researcher_degrees_of_freedom/"
          },
          {
            "title": "Addressing researcher degrees of freedom through minP adjustment",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11253496/"
          },
          {
            "title": "Freedom of choice vs. undisclosed flexibility: Researcher degrees of freedom in model-based inference – I'm a Bayesian and I do what I want",
            "url": "https://sites.uci.edu/joachim/2018/12/13/freedom-of-choice-vs-undisclosed-flexibility-researcher-degrees-of-freedom-in-model-based-inference/"
          },
          {
            "title": "Freedom of choice vs. undisclosed flexibility: Researcher degrees of freedom in model-based inference – Psychonomic Society Featured Content",
            "url": "https://featuredcontent.psychonomic.org/freedom-of-choice-vs-undisclosed-flexibility-researcher-degrees-of-freedom-in-model-based-inference/"
          }
        ]
      },
      "Let me try one more specific search for the Del Giudice framework:",
      {
        "tool_use_id": "srvtoolu_018BnE2zgq7dfyWH9a2tG83q",
        "content": [
          {
            "title": "Making Decisions under Model Misspecification",
            "url": "https://arxiv.org/pdf/2008.01071"
          },
          {
            "title": "A recourse certainty equivalent for decisions under uncertainty | Annals of Operations Research | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/BF02204807"
          },
          {
            "title": "Qualitative Models for Decision Under Uncertainty without the   Commensurability Assumption",
            "url": "https://arxiv.org/pdf/1301.6694"
          },
          {
            "title": "Modeling decision-making under uncertainty with qualitative outcomes",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11918403/"
          },
          {
            "title": "Uncertain Decisions Facilitate Better Preference Learning",
            "url": "https://arxiv.org/pdf/2106.10394"
          }
        ]
      },
      "Let me try a more targeted search:",
      {
        "tool_use_id": "srvtoolu_01DuKankV7E4kzoR3ufDyEiz",
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
            "title": "Reply to Auspurg: On the limits of “justified” model spaces",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12582334/"
          },
          {
            "title": "PNAS 2025 Vol. 122 No. 27 e2400928121\b",
            "url": "https://www.pnas.org/doi/pdf/10.1073/pnas.2400928121"
          },
          {
            "title": "When the role of uncertainty is…uncertain | PNAS",
            "url": "https://www.pnas.org/doi/10.1073/pnas.2305856120"
          },
          {
            "title": "Stochastic responses and marginal valuation | PNAS",
            "url": "https://www.pnas.org/doi/abs/10.1073/pnas.2520857122?af=R"
          }
        ]
      },
      "Based on my web search results, I have found relevant information about the Auspurg PNAS 2025 debate on multiverse analysis and specification decisions. However, I was unable to find specific information about the \"Del Giudice\" E/N/U classification framework in my searches. Let me provide you with what I found:\n\n## Summary of Search Results\n\nKatrin Auspurg published a critique in PNAS 2025 responding to Ganslmeier and Vlandas who conducted an ambitious multiverse analysis estimating over 3.6 billion regression models across four political science topics. By varying estimation strategies, covariates, operationalizations, and samples, they documented drastic model instability with estimates often changing in sign or significance due to \"minor alterations.\"\n\nAuspurg argues that their approach substantially overstates uncertainty, asserting that multiverse analyses are only informative when all included models represent equally plausible strategies for estimating the same estimand.\n\nAuspurg contends that the brute force of the multiverse cannot fix certain issues, and there is a risk that researchers mistake it for a silver bullet.\n\nAuspurg concludes that multiverse analyses require thorough, theory-based model selection, otherwise they become a \"dangerous tool\" that drowns valid models in misspecified ones, needlessly eroding trust in science.\n\nHowever, I was unable to locate information in the search results about the specific \"Del Giudice E/N/U classification\" framework you mentioned. If you have more details about this framework or would like me to search for other aspects of this debate, please let me know."
    ],
    "durationSeconds": 19.006033877,
    "searchCount": 5
  },
  "sourceToolAssistantUUID": "3e11650e-ae4f-4182-a4d4-b4fc6951f97d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T04:03:31.055Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YJhoL9rf2ZxS8aMUGQGQpw`</summary>

```json
{
  "query": "McLaren et al 2026 interaction effects LLM annotation political science arXiv 2603.26898"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c3fd52f-68f0-44b5-b64d-512d27c4afa2",
  "isSidechain": false,
  "requestId": "req_011CbDA4H5oEHcY6B1jii7rH",
  "type": "assistant",
  "uuid": "9d310a53-61b5-4c55-ad79-8bd0143270c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RNMyW8FxSNQULjpRSEKg9p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2264,
      "cache_read_input_tokens": 24125,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2264,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 24125,
          "cache_creation_input_tokens": 2264,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2264
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

_source line 24 · 2026-05-20T04:03:38.038Z_

<details><summary>↩ Tool result · `toolu_01YJhoL9rf2ZxS8aMUGQGQpw`</summary>

```text
Web search results for query: "McLaren et al 2026 interaction effects LLM annotation political science arXiv 2603.26898"

Links: [{"title":"[2603.26898] Magic Words or Methodical Work? Challenging Conventional Wisdom in LLM-Based Political Text Annotation","url":"https://arxiv.org/abs/2603.26898"},{"title":"Magic Words or Methodical Work? Challenging Conventional Wisdom in LLM-Based Political Text Annotation","url":"https://arxiv.org/html/2603.26898"},{"title":"Bias in LLMs as Annotators: The Effect of Party Cues on Labelling   Decision by Large Language Models","url":"https://arxiv.org/pdf/2408.15895"},{"title":"Biased AI can Influence Political Decision-Making","url":"https://arxiv.org/pdf/2410.06415"},{"title":"Hidden Persuaders: LLMs' Political Leaning and Their Influence on Voters","url":"https://arxiv.org/pdf/2410.24190"},{"title":"Fact or Fiction? Can LLMs be Reliable Annotators for Political Truths?","url":"https://arxiv.org/pdf/2411.05775"},{"title":"Just Put a Human in the Loop? Investigating LLM-Assisted Annotation for Subjective Tasks","url":"https://arxiv.org/pdf/2507.15821"}]

Based on the search results, I found the paper you're looking for:

The paper is titled "Magic Words or Methodical Work? Challenging Conventional Wisdom in LLM-Based Political Text Annotation" by Lorca McLaren, James Cross, Zuzanna Krakowska, Robin Rauner, and Martijn Schoonvelde, with arXiv identifier 2603.26898.

The paper addresses how political scientists are rapidly adopting large language models for text annotation, yet the sensitivity of annotation results to implementation choices remains poorly understood, and how model choice, model size, learning approach, and prompt style interact.

The central finding is methodological: interaction effects dominate main effects, so seemingly reasonable pipeline choices can become consequential researcher degrees of freedom. No single model, prompt style, or learning approach is uniformly superior, and the best-performing model varies across tasks.

The research presents a controlled evaluation of pipeline choices, testing six open-weight models across four political science annotation tasks under identical quantisation, hardware, and prompt-template conditions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d310a53-61b5-4c55-ad79-8bd0143270c0",
  "isSidechain": false,
  "promptId": "95a611a0-5f01-4610-9b3e-1c678c101211",
  "type": "user",
  "uuid": "01b6e9b7-6bae-472c-bd82-f4d88de62ec1",
  "toolUseResult": {
    "query": "McLaren et al 2026 interaction effects LLM annotation political science arXiv 2603.26898",
    "results": [
      {
        "tool_use_id": "srvtoolu_019MkyNKNUB6azjzVV2XFaCo",
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
            "title": "Biased AI can Influence Political Decision-Making",
            "url": "https://arxiv.org/pdf/2410.06415"
          },
          {
            "title": "Hidden Persuaders: LLMs' Political Leaning and Their Influence on Voters",
            "url": "https://arxiv.org/pdf/2410.24190"
          },
          {
            "title": "Fact or Fiction? Can LLMs be Reliable Annotators for Political Truths?",
            "url": "https://arxiv.org/pdf/2411.05775"
          },
          {
            "title": "Just Put a Human in the Loop? Investigating LLM-Assisted Annotation for Subjective Tasks",
            "url": "https://arxiv.org/pdf/2507.15821"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nThe paper is titled \"Magic Words or Methodical Work? Challenging Conventional Wisdom in LLM-Based Political Text Annotation\" by Lorca McLaren, James Cross, Zuzanna Krakowska, Robin Rauner, and Martijn Schoonvelde, with arXiv identifier 2603.26898.\n\nThe paper addresses how political scientists are rapidly adopting large language models for text annotation, yet the sensitivity of annotation results to implementation choices remains poorly understood, and how model choice, model size, learning approach, and prompt style interact.\n\nThe central finding is methodological: interaction effects dominate main effects, so seemingly reasonable pipeline choices can become consequential researcher degrees of freedom. No single model, prompt style, or learning approach is uniformly superior, and the best-performing model varies across tasks.\n\nThe research presents a controlled evaluation of pipeline choices, testing six open-weight models across four political science annotation tasks under identical quantisation, hardware, and prompt-template conditions."
    ],
    "durationSeconds": 6.978682325999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9d310a53-61b5-4c55-ad79-8bd0143270c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T04:03:40.827Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015h5yXHGiZS3iSJ2cL81guX`</summary>

```json
{
  "query": "\"researcher degrees of freedom\" LLM prompt hacking p-hacking annotation robustness framework 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01b6e9b7-6bae-472c-bd82-f4d88de62ec1",
  "isSidechain": false,
  "requestId": "req_011CbDA4zWgPwDMSNv78cS4Y",
  "type": "assistant",
  "uuid": "796285d0-417b-41b5-876a-957c63e11761",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UkH2TJHGmtCYMT273avcb2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 683,
      "cache_read_input_tokens": 26389,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 683,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 26389,
          "cache_creation_input_tokens": 683,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 683
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

_source line 26 · 2026-05-20T04:03:49.279Z_

<details><summary>↩ Tool result · `toolu_015h5yXHGiZS3iSJ2cL81guX`</summary>

```text
Web search results for query: ""researcher degrees of freedom" LLM prompt hacking p-hacking annotation robustness framework 2025 2026"

Links: [{"title":"LLM Hacking: Techniques, Risks, and Mitigations","url":"https://www.emergentmind.com/topics/llm-hacking"},{"title":"The use of LLMs to annotate data in management research: Foundational guidelines and warnings - Carlson - 2026 - Strategic Management Journal - Wiley Online Library","url":"https://sms.onlinelibrary.wiley.com/doi/10.1002/smj.70023"},{"title":"Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs","url":"https://arxiv.org/pdf/2509.08825"},{"title":"Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation","url":"https://arxiv.org/html/2509.08825v1"},{"title":"LLM Hacking Risks in Text Annotation","url":"https://www.emergentmind.com/papers/2509.08825"},{"title":"[2509.08825] Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation","url":"https://arxiv.org/abs/2509.08825"},{"title":"Large Language Model Hacking","url":"https://www.emergentmind.com/topics/large-language-model-hacking"}]

Based on the search results, here's what I found about researcher degrees of freedom, LLM prompt hacking, p-hacking, and annotation robustness frameworks from recent 2025-2026 research:

## LLM Hacking and Researcher Degrees of Freedom

LLM hacking is related to p-hacking in its susceptibility to researcher degrees of freedom, but it operates at the data generation stage rather than during the analysis stage. LLM hacking is a consequence of the researchers' vast degrees of freedom in LLM configuration choices.

## How Configuration Choices Enable "P-Hacking"

One could potentially iterate on plausible-sounding prompts until one is found that generates the preferred downstream results, and the use of LLMs for this type of application lowers the cost of p-hacking, making comprehensive sensitivity analysis more urgent. The configuration space encompasses all choices affecting LLM outputs, such as model selection, prompt formulation, temperature and other decoding parameters, and output mapping strategies.

## PARKing: Prompt Adjustments Reaching Known Outcomes

Prompt-hacking and PARKing: Strategic prompt modification (PARKing: Prompt Adjustments to Reach Known Outcomes) closely parallels p-hacking in statistics, undermining reproducibility and impartiality in empirical research.

## Robustness and Mitigation Frameworks

The most robust mitigations involve human-in-the-loop annotation or hybrid models with transparent, preregistered model and prompt dependencies, and human-complemented annotation with rigorous documentation is essential for reducing research-induced hacking risk. The study provides practical recommendations to limit LLM hacking, advocating for transparency standards and pre-registration of LLM configuration choices.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "796285d0-417b-41b5-876a-957c63e11761",
  "isSidechain": false,
  "promptId": "95a611a0-5f01-4610-9b3e-1c678c101211",
  "type": "user",
  "uuid": "657b9bab-2090-4917-8d7a-a9346892762d",
  "toolUseResult": {
    "query": "\"researcher degrees of freedom\" LLM prompt hacking p-hacking annotation robustness framework 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RjFksXjbxwdLdEtqGkRgca",
        "content": [
          {
            "title": "LLM Hacking: Techniques, Risks, and Mitigations",
            "url": "https://www.emergentmind.com/topics/llm-hacking"
          },
          {
            "title": "The use of LLMs to annotate data in management research: Foundational guidelines and warnings - Carlson - 2026 - Strategic Management Journal - Wiley Online Library",
            "url": "https://sms.onlinelibrary.wiley.com/doi/10.1002/smj.70023"
          },
          {
            "title": "Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs",
            "url": "https://arxiv.org/pdf/2509.08825"
          },
          {
            "title": "Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation",
            "url": "https://arxiv.org/html/2509.08825v1"
          },
          {
            "title": "LLM Hacking Risks in Text Annotation",
            "url": "https://www.emergentmind.com/papers/2509.08825"
          },
          {
            "title": "[2509.08825] Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation",
            "url": "https://arxiv.org/abs/2509.08825"
          },
          {
            "title": "Large Language Model Hacking",
            "url": "https://www.emergentmind.com/topics/large-language-model-hacking"
          }
        ]
      },
      "Based on the search results, here's what I found about researcher degrees of freedom, LLM prompt hacking, p-hacking, and annotation robustness frameworks from recent 2025-2026 research:\n\n## LLM Hacking and Researcher Degrees of Freedom\n\nLLM hacking is related to p-hacking in its susceptibility to researcher degrees of freedom, but it operates at the data generation stage rather than during the analysis stage. LLM hacking is a consequence of the researchers' vast degrees of freedom in LLM configuration choices.\n\n## How Configuration Choices Enable \"P-Hacking\"\n\nOne could potentially iterate on plausible-sounding prompts until one is found that generates the preferred downstream results, and the use of LLMs for this type of application lowers the cost of p-hacking, making comprehensive sensitivity analysis more urgent. The configuration space encompasses all choices affecting LLM outputs, such as model selection, prompt formulation, temperature and other decoding parameters, and output mapping strategies.\n\n## PARKing: Prompt Adjustments Reaching Known Outcomes\n\nPrompt-hacking and PARKing: Strategic prompt modification (PARKing: Prompt Adjustments to Reach Known Outcomes) closely parallels p-hacking in statistics, undermining reproducibility and impartiality in empirical research.\n\n## Robustness and Mitigation Frameworks\n\nThe most robust mitigations involve human-in-the-loop annotation or hybrid models with transparent, preregistered model and prompt dependencies, and human-complemented annotation with rigorous documentation is essential for reducing research-induced hacking risk. The study provides practical recommendations to limit LLM hacking, advocating for transparency standards and pre-registration of LLM configuration choices."
    ],
    "durationSeconds": 8.447839158999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "796285d0-417b-41b5-876a-957c63e11761",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T04:03:52.066Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0193m5AB63jq5MGYvkPBb3XW`</summary>

```json
{
  "query": "Mehrotra perspective-driven inference LLM annotation subjective tasks 2026 arXiv 2603.21404"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "657b9bab-2090-4917-8d7a-a9346892762d",
  "isSidechain": false,
  "requestId": "req_011CbDA5pZAzND7i4caibh21",
  "type": "assistant",
  "uuid": "ddd494f6-4cfb-4ea3-a1e3-93813afa682b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0181XhSgbQbX9cB3Tm3TAARG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 865,
      "cache_read_input_tokens": 27072,
      "output_tokens": 79,
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
          "output_tokens": 79,
          "cache_read_input_tokens": 27072,
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

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "## The LLM Annotation Multiverse: Specification Curve Analysis for Robust Computational Social Science  ### Motivation  LLM-based text annotation has become the default measurement instrument in compu…",
  "leafUuid": "ddd494f6-4cfb-4ea3-a1e3-93813afa682b",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Specification curve analysis for LLM annotation robustness",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d"
}
```

---

### Tool result

_source line 30 · 2026-05-20T04:03:58.633Z_

<details><summary>↩ Tool result · `toolu_0193m5AB63jq5MGYvkPBb3XW`</summary>

```text
Web search results for query: "Mehrotra perspective-driven inference LLM annotation subjective tasks 2026 arXiv 2603.21404"

Links: [{"title":"[2603.21404] Multi-Perspective LLM Annotations for Valid Analyses in Subjective Tasks","url":"https://arxiv.org/abs/2603.21404"},{"title":"Multi-Perspective LLM Annotations for Valid Analyses in Subjective Tasks","url":"https://arxiv.org/html/2603.21404"},{"title":"Multi-Perspective LLM Annotations for Valid Analyses in Subjective Tasks","url":"https://arxiv.org/pdf/2603.21404"},{"title":"Just Put a Human in the Loop? Investigating LLM-Assisted Annotation for Subjective Tasks","url":"https://arxiv.org/pdf/2507.15821"},{"title":"Perspective Transition of Large Language Models for Solving Subjective Tasks","url":"https://arxiv.org/pdf/2501.09265"},{"title":"The Impact of Annotator Personas on LLM Behavior Across the Perspectivism Spectrum","url":"https://arxiv.org/pdf/2508.17164"}]

Based on the search results, I found the paper you're looking for. Here's what the research is about:

The paper is titled "Multi-Perspective LLM Annotations for Valid Analyses in Subjective Tasks" by Navya Mehrotra, Adam Visokay, and Kristina Gligorić.

**Key Contribution:**

The paper introduces Perspective-Driven Inference, a method that treats the distribution of annotations across groups as the quantity of interest, and estimates it using a small human annotation budget.

**The Problem It Addresses:**

Existing methods for correcting LLM annotation error assume a single ground truth. However, this assumption fails in subjective tasks where disagreement across demographic groups is meaningful.

**Technical Approach:**

The method contributes an adaptive sampling strategy that concentrates human annotation effort on groups where LLM proxies are least accurate.

**Evaluation:**

The paper evaluates the approach on politeness and offensiveness rating tasks, showing targeted improvements for harder-to-model demographic groups relative to uniform sampling baselines, while maintaining coverage.

The paper was submitted on March 22, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ddd494f6-4cfb-4ea3-a1e3-93813afa682b",
  "isSidechain": false,
  "promptId": "95a611a0-5f01-4610-9b3e-1c678c101211",
  "type": "user",
  "uuid": "1055bc00-2d53-4160-9fc1-5230e8a2c527",
  "toolUseResult": {
    "query": "Mehrotra perspective-driven inference LLM annotation subjective tasks 2026 arXiv 2603.21404",
    "results": [
      {
        "tool_use_id": "srvtoolu_0134EcPJ3T8m1GGDEnX1d1XK",
        "content": [
          {
            "title": "[2603.21404] Multi-Perspective LLM Annotations for Valid Analyses in Subjective Tasks",
            "url": "https://arxiv.org/abs/2603.21404"
          },
          {
            "title": "Multi-Perspective LLM Annotations for Valid Analyses in Subjective Tasks",
            "url": "https://arxiv.org/html/2603.21404"
          },
          {
            "title": "Multi-Perspective LLM Annotations for Valid Analyses in Subjective Tasks",
            "url": "https://arxiv.org/pdf/2603.21404"
          },
          {
            "title": "Just Put a Human in the Loop? Investigating LLM-Assisted Annotation for Subjective Tasks",
            "url": "https://arxiv.org/pdf/2507.15821"
          },
          {
            "title": "Perspective Transition of Large Language Models for Solving Subjective Tasks",
            "url": "https://arxiv.org/pdf/2501.09265"
          },
          {
            "title": "The Impact of Annotator Personas on LLM Behavior Across the Perspectivism Spectrum",
            "url": "https://arxiv.org/pdf/2508.17164"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's what the research is about:\n\nThe paper is titled \"Multi-Perspective LLM Annotations for Valid Analyses in Subjective Tasks\" by Navya Mehrotra, Adam Visokay, and Kristina Gligorić.\n\n**Key Contribution:**\n\nThe paper introduces Perspective-Driven Inference, a method that treats the distribution of annotations across groups as the quantity of interest, and estimates it using a small human annotation budget.\n\n**The Problem It Addresses:**\n\nExisting methods for correcting LLM annotation error assume a single ground truth. However, this assumption fails in subjective tasks where disagreement across demographic groups is meaningful.\n\n**Technical Approach:**\n\nThe method contributes an adaptive sampling strategy that concentrates human annotation effort on groups where LLM proxies are least accurate.\n\n**Evaluation:**\n\nThe paper evaluates the approach on politeness and offensiveness rating tasks, showing targeted improvements for harder-to-model demographic groups relative to uniform sampling baselines, while maintaining coverage.\n\nThe paper was submitted on March 22, 2026."
    ],
    "durationSeconds": 6.5628609830000055,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ddd494f6-4cfb-4ea3-a1e3-93813afa682b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-20T04:03:58.635Z_

```json
{
  "parentUuid": "1055bc00-2d53-4160-9fc1-5230e8a2c527",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "39eabdcb-31cb-4cb5-bdb0-5f3cc486490a",
  "timestamp": "2026-05-20T04:03:58.635Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 32 · 2026-05-20T04:04:01.702Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JUh8jBGZuNk3rVUdoA3eTQ`</summary>

```json
{
  "query": "Boba specification curve DSL multiverse analysis executable framework Liu CHI 2021 recent applications 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39eabdcb-31cb-4cb5-bdb0-5f3cc486490a",
  "isSidechain": false,
  "requestId": "req_011CbDA6WdBzvroN6pvuddmx",
  "type": "assistant",
  "uuid": "97c6fc8f-f06c-4f2c-a504-5d44e75876bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01184kq2tf6Da4Xo8daDuHgW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 754,
      "cache_read_input_tokens": 27937,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 754,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 27937,
          "cache_creation_input_tokens": 754,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 754
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

_source line 33 · 2026-05-20T04:04:11.003Z_

<details><summary>↩ Tool result · `toolu_01JUh8jBGZuNk3rVUdoA3eTQ`</summary>

```text
Web search results for query: "Boba specification curve DSL multiverse analysis executable framework Liu CHI 2021 recent applications 2025 2026"

Links: [{"title":"Boba: Authoring and Visualizing Multiverse Analyses","url":"https://idl.cs.washington.edu/files/2021-BobaMultiverse-VAST.pdf"},{"title":"Boba: Authoring and Visualizing Multiverse Analyses","url":"https://idl.uw.edu/papers/boba"},{"title":"boba · PyPI","url":"https://pypi.org/project/boba/"},{"title":"GitHub - uwdata/boba: Specifying and executing multiverse analysis · GitHub","url":"https://github.com/uwdata/boba"},{"title":"Boba: Authoring and Visualizing Multiverse Analyses","url":"https://arxiv.org/pdf/2007.05551"},{"title":"Boba: Authoring and Visualizing Multiverse Analyses - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/33027002/"},{"title":"boba - Python Package Health Analysis | Snyk","url":"https://snyk.io/advisor/python/boba"},{"title":"[PDF] Boba: Authoring and Visualizing Multiverse Analyses | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Boba:-Authoring-and-Visualizing-Multiverse-Analyses-Liu-Kale/8498baead9ea8dc2bce5eec95dd357c62ed968d3"},{"title":"[2007.05551] Boba: Authoring and Visualizing Multiverse Analyses","url":"https://arxiv.org/abs/2007.05551"},{"title":"Boba: Authoring and Visualizing Multiverse Analyses | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/9216579/"}]

Now let me search for recent applications in 2025-2026:

Links: [{"title":"Package: multiverse (via r-universe) May 10, 2026 Version 0.6.3 Date 2025-10-22","url":"https://mucollective.r-universe.dev/multiverse/multiverse.pdf"},{"title":"Boba: Authoring and Visualizing Multiverse Analyses | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/9216579/"},{"title":"Boba: Authoring and Visualizing Multiverse Analyses | Request PDF","url":"https://www.researchgate.net/publication/345996760_Boba_Authoring_and_Visualizing_Multiverse_Analyses"},{"title":"Boba: Authoring and Visualizing Multiverse Analyses","url":"https://arxiv.org/pdf/2007.05551"},{"title":"Boba: Authoring and Visualizing Multiverse Analyses","url":"https://idl.uw.edu/papers/boba"},{"title":"Boba: Authoring and Visualizing Multiverse Analyses - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/33027002/"},{"title":"Multiverse Analyses of Fear Acquisition and Extinction Retention in Posttraumatic Stress Disorder - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10330173/"}]

Based on my web search results, here's what I found about Boba and multiverse analysis:

## Overview

Boba is an integrated domain-specific language (DSL) and visual analysis system for authoring and reviewing multiverse analyses. The work was published in IEEE Transactions on Visualization and Computer Graphics (Proc. VAST) in 2021 by Yang Liu, Alex Kale, Tim Althoff, and Jeffrey Heer.

## Core Functionality

Multiverse analysis is an approach to data analysis in which all "reasonable" analytic decisions are evaluated in parallel and interpreted collectively, in order to foster robustness and transparency.

With the Boba DSL, analysts write the shared portion of analysis code only once, alongside local variations defining alternative decisions, from which the compiler generates a multiplex of scripts representing all possible analysis paths. As a meta-language, the Boba DSL is agnostic to the underlying programming language of the analysis script, thereby supporting a wide range of data science use cases.

The Boba Visualizer provides linked views of model results and the multiverse decision space to enable rapid, systematic assessment of consequential decisions and robustness, including sampling uncertainty and model fit.

## Recent Applications

The recently developed Boba Sensitivity Analysis enables quantification of the specific impact of each methodology, and has been applied to the study of fear extinction retention in psychophysiological research.

The search results did not reveal specific large-scale applications exclusively from 2025-2026, though multiverse analysis methods continue to be actively used in recent research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97c6fc8f-f06c-4f2c-a504-5d44e75876bb",
  "isSidechain": false,
  "promptId": "95a611a0-5f01-4610-9b3e-1c678c101211",
  "type": "user",
  "uuid": "cb36d84e-0ea8-4bd8-9c0b-20ae140bdc89",
  "toolUseResult": {
    "query": "Boba specification curve DSL multiverse analysis executable framework Liu CHI 2021 recent applications 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GQe4TSmnEowjrsAoGAhqDc",
        "content": [
          {
            "title": "Boba: Authoring and Visualizing Multiverse Analyses",
            "url": "https://idl.cs.washington.edu/files/2021-BobaMultiverse-VAST.pdf"
          },
          {
            "title": "Boba: Authoring and Visualizing Multiverse Analyses",
            "url": "https://idl.uw.edu/papers/boba"
          },
          {
            "title": "boba · PyPI",
            "url": "https://pypi.org/project/boba/"
          },
          {
            "title": "GitHub - uwdata/boba: Specifying and executing multiverse analysis · GitHub",
            "url": "https://github.com/uwdata/boba"
          },
          {
            "title": "Boba: Authoring and Visualizing Multiverse Analyses",
            "url": "https://arxiv.org/pdf/2007.05551"
          },
          {
            "title": "Boba: Authoring and Visualizing Multiverse Analyses - PubMed",
            "url": "https://pubmed.ncbi.nlm.nih.gov/33027002/"
          },
          {
            "title": "boba - Python Package Health Analysis | Snyk",
            "url": "https://snyk.io/advisor/python/boba"
          },
          {
            "title": "[PDF] Boba: Authoring and Visualizing Multiverse Analyses | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Boba:-Authoring-and-Visualizing-Multiverse-Analyses-Liu-Kale/8498baead9ea8dc2bce5eec95dd357c62ed968d3"
          },
          {
            "title": "[2007.05551] Boba: Authoring and Visualizing Multiverse Analyses",
            "url": "https://arxiv.org/abs/2007.05551"
          },
          {
            "title": "Boba: Authoring and Visualizing Multiverse Analyses | IEEE Journals & Magazine | IEEE Xplore",
            "url": "https://ieeexplore.ieee.org/document/9216579/"
          }
        ]
      },
      "Now let me search for recent applications in 2025-2026:",
      {
        "tool_use_id": "srvtoolu_015HTpjAtoYZR6P1ELTgnJB7",
        "content": [
          {
            "title": "Package: multiverse (via r-universe) May 10, 2026 Version 0.6.3 Date 2025-10-22",
            "url": "https://mucollective.r-universe.dev/multiverse/multiverse.pdf"
          },
          {
            "title": "Boba: Authoring and Visualizing Multiverse Analyses | IEEE Journals & Magazine | IEEE Xplore",
            "url": "https://ieeexplore.ieee.org/document/9216579/"
          },
          {
            "title": "Boba: Authoring and Visualizing Multiverse Analyses | Request PDF",
            "url": "https://www.researchgate.net/publication/345996760_Boba_Authoring_and_Visualizing_Multiverse_Analyses"
          },
          {
            "title": "Boba: Authoring and Visualizing Multiverse Analyses",
            "url": "https://arxiv.org/pdf/2007.05551"
          },
          {
            "title": "Boba: Authoring and Visualizing Multiverse Analyses",
            "url": "https://idl.uw.edu/papers/boba"
          },
          {
            "title": "Boba: Authoring and Visualizing Multiverse Analyses - PubMed",
            "url": "https://pubmed.ncbi.nlm.nih.gov/33027002/"
          },
          {
            "title": "Multiverse Analyses of Fear Acquisition and Extinction Retention in Posttraumatic Stress Disorder - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10330173/"
          }
        ]
      },
      "Based on my web search results, here's what I found about Boba and multiverse analysis:\n\n## Overview\n\nBoba is an integrated domain-specific language (DSL) and visual analysis system for authoring and reviewing multiverse analyses. The work was published in IEEE Transactions on Visualization and Computer Graphics (Proc. VAST) in 2021 by Yang Liu, Alex Kale, Tim Althoff, and Jeffrey Heer.\n\n## Core Functionality\n\nMultiverse analysis is an approach to data analysis in which all \"reasonable\" analytic decisions are evaluated in parallel and interpreted collectively, in order to foster robustness and transparency.\n\nWith the Boba DSL, analysts write the shared portion of analysis code only once, alongside local variations defining alternative decisions, from which the compiler generates a multiplex of scripts representing all possible analysis paths. As a meta-language, the Boba DSL is agnostic to the underlying programming language of the analysis script, thereby supporting a wide range of data science use cases.\n\nThe Boba Visualizer provides linked views of model results and the multiverse decision space to enable rapid, systematic assessment of consequential decisions and robustness, including sampling uncertainty and model fit.\n\n## Recent Applications\n\nThe recently developed Boba Sensitivity Analysis enables quantification of the specific impact of each methodology, and has been applied to the study of fear extinction retention in psychophysiological research.\n\nThe search results did not reveal specific large-scale applications exclusively from 2025-2026, though multiverse analysis methods continue to be actively used in recent research."
    ],
    "durationSeconds": 9.297060897999996,
    "searchCount": 2
  },
  "sourceToolAssistantUUID": "97c6fc8f-f06c-4f2c-a504-5d44e75876bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-20T04:04:13.871Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ttidp42xyex9sGoY2gcJ7Y`</summary>

```json
{
  "query": "LLM annotation robustness sensitivity prompt variation computational social science EMNLP ACL NAACL 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb36d84e-0ea8-4bd8-9c0b-20ae140bdc89",
  "isSidechain": false,
  "requestId": "req_011CbDA7RSvJKa3G26g9nUQx",
  "type": "assistant",
  "uuid": "45f0517f-387a-4ee3-8f39-659f325cbf0d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FP3KxbkwceGVKkX3QRdBvT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1322,
      "cache_read_input_tokens": 28691,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1322,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 28691,
          "cache_creation_input_tokens": 1322,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1322
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

_source line 35 · 2026-05-20T04:04:26.529Z_

<details><summary>↩ Tool result · `toolu_01Ttidp42xyex9sGoY2gcJ7Y`</summary>

```text
Web search results for query: "LLM annotation robustness sensitivity prompt variation computational social science EMNLP ACL NAACL 2025 2026"

Links: [{"title":"Prompt Design Matters for Computational Social Science Tasks but in Unpredictable Ways","url":"https://arxiv.org/pdf/2406.11980"},{"title":"Architectural Vulnerability and Reliability Challenges in AI Text Annotation: A Survey-Inspired Framework with Independent Probability Assessment","url":"https://arxiv.org/pdf/2502.19679"},{"title":"Can Large Language Models Transform Computational Social Science?","url":"https://arxiv.org/pdf/2305.03514"},{"title":"Towards LLMs Robustness to Changes in Prompt Format ...","url":"https://aclanthology.org/2025.naacl-srw.51.pdf"},{"title":"Assessing and Understanding the Prompt Sensitivity of LLMs","url":"https://aclanthology.org/2024.findings-emnlp.108.pdf"},{"title":"What Did I Do Wrong? Quantifying LLMs' Sensitivity and Consistency to Prompt Engineering","url":"https://arxiv.org/pdf/2406.12334"},{"title":"The Effectiveness of LLMs as Annotators: A Comparative Overview and Empirical Analysis of Direct Representation","url":"https://arxiv.org/pdf/2405.01299"}]

Based on the web search results, here are some relevant recent papers and findings on LLM annotation robustness, sensitivity to prompt variation, and computational social science:

## Key Papers Found

1. **"Prompt Design Matters for Computational Social Science Tasks but in Unpredictable Ways"** (2024)
   This work examines how prompt design impacts LLMs' compliance and accuracy, testing model selection and prompt design features (definition inclusion, output type, explanation, and prompt length) on four computational social science tasks: toxicity, sentiment, rumor stance, and news frames. The results show that LLM compliance and accuracy are highly prompt-dependent, with minor prompt changes causing large changes in the distribution of generated labels.

2. **"Towards LLMs Robustness to Changes in Prompt Format"** (NAACL 2025)
   This paper presented at NAACL 2025 addresses LLM robustness to changes in prompt format styles. It proposes Mixture of Formats (MOF) prompts that perform nearly as well as traditional prompts, with MOF prompts generally leading to significant overall mean accuracy improvements.

3. **"ProSA: Assessing and Understanding the Prompt Sensitivity of LLMs"** (EMNLP 2024 Findings)
   This paper presents a framework for assessing prompt sensitivity of LLMs and notes that prompt sensitivity can serve as a proxy for monitoring robustness and stability of LLMs.

4. **"What Did I Do Wrong? Quantifying LLMs' Sensitivity and Consistency to Prompt Engineering"**
   This work emphasizes the importance of having LLMs robust to semantically equivalent variations of prompts, noting that merely syntactic prompt rephrasings can produce very diverse distributions.

5. **LLM Reliability in Social Science Research** (2025)
   A recent framework adapts survey methodology principles to assess LLM text annotation reliability by implementing interventions like option randomization, position randomization, and reverse validation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45f0517f-387a-4ee3-8f39-659f325cbf0d",
  "isSidechain": false,
  "promptId": "95a611a0-5f01-4610-9b3e-1c678c101211",
  "type": "user",
  "uuid": "a39a088a-f043-4288-a21a-2c962ee5ace7",
  "toolUseResult": {
    "query": "LLM annotation robustness sensitivity prompt variation computational social science EMNLP ACL NAACL 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01R1YLe5f8iVvor367Sakp4N",
        "content": [
          {
            "title": "Prompt Design Matters for Computational Social Science Tasks but in Unpredictable Ways",
            "url": "https://arxiv.org/pdf/2406.11980"
          },
          {
            "title": "Architectural Vulnerability and Reliability Challenges in AI Text Annotation: A Survey-Inspired Framework with Independent Probability Assessment",
            "url": "https://arxiv.org/pdf/2502.19679"
          },
          {
            "title": "Can Large Language Models Transform Computational Social Science?",
            "url": "https://arxiv.org/pdf/2305.03514"
          },
          {
            "title": "Towards LLMs Robustness to Changes in Prompt Format ...",
            "url": "https://aclanthology.org/2025.naacl-srw.51.pdf"
          },
          {
            "title": "Assessing and Understanding the Prompt Sensitivity of LLMs",
            "url": "https://aclanthology.org/2024.findings-emnlp.108.pdf"
          },
          {
            "title": "What Did I Do Wrong? Quantifying LLMs' Sensitivity and Consistency to Prompt Engineering",
            "url": "https://arxiv.org/pdf/2406.12334"
          },
          {
            "title": "The Effectiveness of LLMs as Annotators: A Comparative Overview and Empirical Analysis of Direct Representation",
            "url": "https://arxiv.org/pdf/2405.01299"
          }
        ]
      },
      "Based on the web search results, here are some relevant recent papers and findings on LLM annotation robustness, sensitivity to prompt variation, and computational social science:\n\n## Key Papers Found\n\n1. **\"Prompt Design Matters for Computational Social Science Tasks but in Unpredictable Ways\"** (2024)\n   This work examines how prompt design impacts LLMs' compliance and accuracy, testing model selection and prompt design features (definition inclusion, output type, explanation, and prompt length) on four computational social science tasks: toxicity, sentiment, rumor stance, and news frames. The results show that LLM compliance and accuracy are highly prompt-dependent, with minor prompt changes causing large changes in the distribution of generated labels.\n\n2. **\"Towards LLMs Robustness to Changes in Prompt Format\"** (NAACL 2025)\n   This paper presented at NAACL 2025 addresses LLM robustness to changes in prompt format styles. It proposes Mixture of Formats (MOF) prompts that perform nearly as well as traditional prompts, with MOF prompts generally leading to significant overall mean accuracy improvements.\n\n3. **\"ProSA: Assessing and Understanding the Prompt Sensitivity of LLMs\"** (EMNLP 2024 Findings)\n   This paper presents a framework for assessing prompt sensitivity of LLMs and notes that prompt sensitivity can serve as a proxy for monitoring robustness and stability of LLMs.\n\n4. **\"What Did I Do Wrong? Quantifying LLMs' Sensitivity and Consistency to Prompt Engineering\"**\n   This work emphasizes the importance of having LLMs robust to semantically equivalent variations of prompts, noting that merely syntactic prompt rephrasings can produce very diverse distributions.\n\n5. **LLM Reliability in Social Science Research** (2025)\n   A recent framework adapts survey methodology principles to assess LLM text annotation reliability by implementing interventions like option randomization, position randomization, and reverse validation."
    ],
    "durationSeconds": 12.654803394999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "45f0517f-387a-4ee3-8f39-659f325cbf0d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-20T04:04:29.702Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me do one more targeted search to check if anyone has already done something very close to applying multiverse/specification curve analysis specifically to LLM annotation pipelines:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a39a088a-f043-4288-a21a-2c962ee5ace7",
  "isSidechain": false,
  "requestId": "req_011CbDA8ZqUWzNmNFtg7hKKD",
  "type": "assistant",
  "uuid": "c0138866-2bbe-47e0-99da-f99b000fd7a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0144mirDKDNE7f3y21TPY9Sx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 904,
      "cache_read_input_tokens": 30013,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 904,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 30013,
          "cache_creation_input_tokens": 904,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 904
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

_source line 37 · 2026-05-20T04:04:30.117Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013Mu1mHA971rMeqmPsuFiCs`</summary>

```json
{
  "query": "\"multiverse analysis\" OR \"specification curve\" LLM annotation pipeline configuration robustness 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0138866-2bbe-47e0-99da-f99b000fd7a1",
  "isSidechain": false,
  "requestId": "req_011CbDA8ZqUWzNmNFtg7hKKD",
  "type": "assistant",
  "uuid": "25e7493d-f7cb-4aee-9ec8-4c22d407730b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0144mirDKDNE7f3y21TPY9Sx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 904,
      "cache_read_input_tokens": 30013,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 904,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 30013,
          "cache_creation_input_tokens": 904,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 904
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

_source line 38 · 2026-05-20T04:04:37.615Z_

<details><summary>↩ Tool result · `toolu_013Mu1mHA971rMeqmPsuFiCs`</summary>

```text
Web search results for query: ""multiverse analysis" OR "specification curve" LLM annotation pipeline configuration robustness 2025 2026"

Links: [{"title":"42.2 Specification Curve Analysis | A Guide on Data Analysis","url":"https://bookdown.org/mike/data_analysis/specification-curve-analysis.html"},{"title":"Multiverse analysis | FORRT - Framework for Open and Reproducible Research Training","url":"https://forrt.org/glossary/english/multiverse_analysis/"},{"title":"Specification curve analysis and the multiverse | Statistical Modeling, Causal Inference, and Social Science","url":"https://statmodeling.stat.columbia.edu/2024/11/12/specification-curve-analysis-and-the-multiverse/"},{"title":"POST-SELECTION INFERENCE IN MULTIVERSE ANALYSIS (PIMA):","url":"https://arxiv.org/pdf/2210.02794"},{"title":"Into the (Bayesian) Multiverse!","url":"https://pab2163.github.io/amygdala_mpfc_multiverse/into_the_bayesian_multiverse.html"},{"title":"Exploring the multiverse of analysis options for the alcohol Stroop","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11133151/"},{"title":"The Systematic Multiverse Analysis Registration Tool for defining multiverse analyses","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12567067/"},{"title":"AI-Powered Annotation Pipelines for Stabilizing Large Language Models: A Human-AI Synergy Approach","url":"https://arxiv.org/pdf/2512.13714"},{"title":"Visualizing vastness: Graphical methods for multiverse analysis","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12875576/"}]

Based on the search results, I found relevant information about multiverse analysis and specification curves, as well as recent research on LLM annotation pipelines. Here are the key findings:

## Multiverse Analysis and Specification Curves

Specification curve analysis (also known as multiverse analysis or the specification robustness graph) provides a systematic way to examine how results vary across a large set of defensible specifications. Multiverse analyses are based on all potentially equally justifiable data processing and statistical analysis pipelines that can be employed to test a single hypothesis.

Multiverse analysis is increasingly recognized as a systematic framework for assessing the robustness of scientific results across alternative defensible data processing and analysis pipelines. A recent 2025 publication introduced The Systematic Multiverse Analysis Registration Tool for defining multiverse analyses, addressing the challenge that defining the multiverse, by identifying defensible combinations of options across multiple nodes in the analysis workflow, remains a cognitively and logistically demanding and complex task.

## LLM Annotation Pipeline Configuration and Robustness

I found recent research on this topic: An AI-based annotation pipeline systematically identifies, labels, and fixes instability patterns on LLM output, combining automated weak supervision with human validation to guarantee reliability, introducing semantic consistency, factual correctness, and logical coherence categories to enhance model robustness.

The search results show active research in 2025-2026 on both multiverse analysis methodologies and LLM annotation pipeline robustness, though the specific intersection of these topics with configuration analysis appears to be an emerging research area.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25e7493d-f7cb-4aee-9ec8-4c22d407730b",
  "isSidechain": false,
  "promptId": "95a611a0-5f01-4610-9b3e-1c678c101211",
  "type": "user",
  "uuid": "fc98b1aa-7021-450a-a688-89ca0b5a2545",
  "toolUseResult": {
    "query": "\"multiverse analysis\" OR \"specification curve\" LLM annotation pipeline configuration robustness 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WXcmGV9d7tVFx9BYUZgTJT",
        "content": [
          {
            "title": "42.2 Specification Curve Analysis | A Guide on Data Analysis",
            "url": "https://bookdown.org/mike/data_analysis/specification-curve-analysis.html"
          },
          {
            "title": "Multiverse analysis | FORRT - Framework for Open and Reproducible Research Training",
            "url": "https://forrt.org/glossary/english/multiverse_analysis/"
          },
          {
            "title": "Specification curve analysis and the multiverse | Statistical Modeling, Causal Inference, and Social Science",
            "url": "https://statmodeling.stat.columbia.edu/2024/11/12/specification-curve-analysis-and-the-multiverse/"
          },
          {
            "title": "POST-SELECTION INFERENCE IN MULTIVERSE ANALYSIS (PIMA):",
            "url": "https://arxiv.org/pdf/2210.02794"
          },
          {
            "title": "Into the (Bayesian) Multiverse!",
            "url": "https://pab2163.github.io/amygdala_mpfc_multiverse/into_the_bayesian_multiverse.html"
          },
          {
            "title": "Exploring the multiverse of analysis options for the alcohol Stroop",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11133151/"
          },
          {
            "title": "The Systematic Multiverse Analysis Registration Tool for defining multiverse analyses",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12567067/"
          },
          {
            "title": "AI-Powered Annotation Pipelines for Stabilizing Large Language Models: A Human-AI Synergy Approach",
            "url": "https://arxiv.org/pdf/2512.13714"
          },
          {
            "title": "Visualizing vastness: Graphical methods for multiverse analysis",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12875576/"
          }
        ]
      },
      "Based on the search results, I found relevant information about multiverse analysis and specification curves, as well as recent research on LLM annotation pipelines. Here are the key findings:\n\n## Multiverse Analysis and Specification Curves\n\nSpecification curve analysis (also known as multiverse analysis or the specification robustness graph) provides a systematic way to examine how results vary across a large set of defensible specifications. Multiverse analyses are based on all potentially equally justifiable data processing and statistical analysis pipelines that can be employed to test a single hypothesis.\n\nMultiverse analysis is increasingly recognized as a systematic framework for assessing the robustness of scientific results across alternative defensible data processing and analysis pipelines. A recent 2025 publication introduced The Systematic Multiverse Analysis Registration Tool for defining multiverse analyses, addressing the challenge that defining the multiverse, by identifying defensible combinations of options across multiple nodes in the analysis workflow, remains a cognitively and logistically demanding and complex task.\n\n## LLM Annotation Pipeline Configuration and Robustness\n\nI found recent research on this topic: An AI-based annotation pipeline systematically identifies, labels, and fixes instability patterns on LLM output, combining automated weak supervision with human validation to guarantee reliability, introducing semantic consistency, factual correctness, and logical coherence categories to enhance model robustness.\n\nThe search results show active research in 2025-2026 on both multiverse analysis methodologies and LLM annotation pipeline robustness, though the specific intersection of these topics with configuration analysis appears to be an emerging research area."
    ],
    "durationSeconds": 7.494407025999986,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "25e7493d-f7cb-4aee-9ec8-4c22d407730b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "## The LLM Annotation Multiverse: Specification Curve Analysis for Robust Computational Social Science  ### Motivation  LLM-based text annotation has become the default measurement instrument in compu…",
  "leafUuid": "fc98b1aa-7021-450a-a688-89ca0b5a2545",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Specification curve analysis for LLM annotation robustness",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d"
}
```

---

### Assistant

_source line 41 · 2026-05-20T04:05:19.697Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a solid understanding of the landscape. Let me synthesize my findings and provide my assessment as the "发掘 agent."

Key findings from my research:

1. **No one has applied formal multiverse/specification curve analysis to LLM annotation pipelines yet.** My searches confirmed this gap exists. The closest works are:
   - Baumann et al. (2025) - diagnostic study quantifying LLM hacking risk
   - McLaren et al. (2026) - interaction effects in political science annotation
   - Messing (2026) - TEE-corrected standard errors
   - Mehrotra et al. (2026) - perspective-driven inference for subjective tasks
   - Kosch & Feger (CACM 2026) - naming the problem "prompt-hacking"
   - Carlson & Burbano (SMJ 2026) - informal sensitivity analysis

2. **The Auspurg critique and the Ganslmeier & Vlandas reply** represent an active debate in PNAS 2025, where Auspurg contends that brute-force multiverse analysis conflates justified and unjustified specifications, while Ganslmeier & Vlandas counter that restricting to "justified" specifications is the appropriate methodological response.

3. The epistemological case for applying multiverse analysis to LLM annotation—grounded in constant estimands, absence of classical misspecification, and clear E/N/U classification—seems genuinely original and well-reasoned.

4. Boba DSL exists for multiverse authoring but hasn't been adapted to LLM annotation workflows, and the Systematic Multiverse Analysis Registration Tool addresses definition but not the LLM context specifically.

5. Looking at the proposal's strengths: the gap is clearly identified, the epistemological argument directly engages Auspurg's critique as a substantive contribution, the relationship to Messing's TEE is well-positioned as complementary rather than redundant, and there's existing data to work with.

6. The E/N/U framework adapted for LLM pipelines is novel with thoughtfully developed classification criteria, though I'm noticing some potential vulnerabilities: the proposal risks being read as simply transplanting an existing methodology to a new domain rather than making a non-trivial intellectual leap, the epistemological argument—while strong—needs more prominence in the framing, and the "constant estimand" assumption could face pushback if different models operationalize concepts like toxicity or sentiment in fundamentally different ways, which would undermine a key condition for the multiverse approach.

7. Despite these concerns, this is a solid proposal that identifies a genuine methodological gap and engages seriously with the theoretical foundations.

The real pressure point is the constant estimand assumption. Since the paper itself invokes perspectivism through Mehrotra et al., there's a tension: if different LLMs embody different perspectives on subjective tasks, then the estimand arguably shifts across configurations, which would violate the epistemological condition the proposal relies on. Rather than treating this as a fatal flaw, the paper could lean into it—developing a more nuanced argument about when constant estimands hold (objective, factual tasks) versus when they fracture (subjective judgments), which would actually strengthen the contribution.

The novelty framing also needs recalibration. Instead of positioning this as "we applied specification curves to LLM annotation," the deeper claim is that LLM annotation is the first domain where multiverse analysis's theoretical conditions are cleanly satisfied, offering genuine resolution to an open methodological debate. That should be the headline, not a supporting detail.

Finally, there's a gap between robustness and validity that deserves explicit treatment. A finding can be robust across the entire multiverse—all pipelines agree—yet still be systematically wrong if they all share the same bias. The proposal mentions PPI and DSL comparisons but doesn't directly address this "robust but wrong" scenario, which is crucial for understanding what robustness actually guarantees.

The proposal would also benefit from clearly stating what multiverse analysis can and cannot tell you. And the claim that principled multiverse analysis beats ad hoc sensitivity checks (like running 3-5 configurations) needs to be elevated from a supporting argument to a core contribution—ideally with empirical evidence showing where informal approaches miss instabilities that the full multiverse catches.

The real novelty here is that this paper offers the first positive answer to the Auspurg critique, not just that it applies specification curves to LLM annotation—that should be the headline claim. For subjective tasks, there's a genuine tension between assuming a constant estimand and embracing perspectivism, but the E/N/U framework actually handles this well by classifying subjective task parameters as Type U or by integrating with Mehrotra's perspectivism work. And the paper needs to be intellectually honest about what multiverse analysis can deliver: it can show robustness, but that doesn't mean the findings are correct, so I should theorize explicitly about the relationship between multiverse scope and the validity of conclusions.

I should probably dig deeper into the constant estimand problem in multiverse analysis since that's really at the heart of the second point. Let me finalize my thinking on this—the proposal is solid, but there are two or three genuine insights that could strengthen it considerably.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc98b1aa-7021-450a-a688-89ca0b5a2545",
  "isSidechain": false,
  "requestId": "req_011CbDA9PD32Uk18Wq6AhA3E",
  "type": "assistant",
  "uuid": "21aa738b-d346-4a5d-992b-cb14047bed0f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L6FJ3NxH3qS7rBnHgGDNrR",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 955,
      "cache_read_input_tokens": 30917,
      "output_tokens": 5650,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 955,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5650,
          "cache_read_input_tokens": 30917,
          "cache_creation_input_tokens": 955,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 955
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

_source line 42 · 2026-05-20T04:06:43.694Z_

Now I have sufficient research to provide my assessment. Let me compile my analysis.

---

【状态】: 有发掘空间

【前置调研发现】
- [Baumann et al., arXiv:2509.08825](https://arxiv.org/abs/2509.08825) (2025): 最大规模的 LLM 标注不稳定性诊断研究（18 模型 × 37 任务 × 13M 标签），确认 31% 的假设检验可通过更换 pipeline 配置翻转结论。纯诊断性质，无推断框架。
- [McLaren et al., arXiv:2603.26898](https://arxiv.org/abs/2603.26898) (2026): 政治学标注任务中交互效应主导主效应的发现，直接支持本 proposal 关于"pairwise sensitivity check 不够"的论点。6 个开源模型 × 4 个任务的控制实验。
- [Messing, arXiv:2604.11581](https://arxiv.org/abs/2604.11581) (2026): TEE-corrected standard errors，分解 prompt/temperature/judge-model 的方差分量。局限于单一估计的置信区间修正，不遍历配置空间。Proposal 对其定位（互补而非竞争）准确。
- [Mehrotra et al., arXiv:2603.21404](https://arxiv.org/abs/2603.21404) (2026): Perspective-Driven Inference，将主观任务中不同 LLM 的标注分歧视为合法视角而非误差。直接挑战"同一估量对象"假设在主观任务上的成立性。
- [Auspurg, PNAS 2025](https://www.pnas.org/doi/10.1073/pnas.2521917122) vs. [Ganslmeier & Vlandas, PNAS 2025](https://www.pnas.org/doi/10.1073/pnas.2523374122): 关于暴力穷举 multiverse 是否有意义的公开辩论。Auspurg 要求三个条件（constant estimand、无 misspecification、可原则化分类），Ganslmeier 回应"justified model space"本身有争议。
- [Carlson & Burbano, SMJ 2026](https://sms.onlinelibrary.wiley.com/doi/10.1002/smj.70023): 管理学场景下推荐非正式敏感性分析（3-5 组合），代表了当前的"实践智慧"基线。
- [SMART Registration Tool, 2025](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12567067/): 用于定义 multiverse 分析的注册工具，表明该领域正在走向结构化和标准化。
- 经过多次针对性搜索（"specification curve" + "LLM annotation"、"multiverse analysis" + "LLM pipeline" 等），**未找到任何已发表或预印本工作将正式的 specification curve analysis 应用于 LLM 标注 pipeline**。Proposal 声称的 gap 经调研验证为真实存在。
- 调研总结: 当前领域的研究者分为两个阵营——诊断派（量化不稳定性但不提供补救）和修正派（单 pipeline 内去偏但忽略 pipeline 选择本身的影响）。将 multiverse methodology 正式引入 LLM annotation 是一个尚无人占领的交叉点，但其价值取决于能否回应 Auspurg 的理论质疑。

---

【发掘点 1】
- 维度: 核心 claim 强化
- 内容: Proposal 当前的叙事结构将认识论贡献（LLM annotation 满足 Auspurg 三个条件）作为 "Opportunity and Core Argument" 的一个子论点。建议将其提升为**论文的第一主张（headline claim）**，重新组织叙事为："Multiverse analysis 在社会科学中长期受到一个根本性质疑（Auspurg PNAS 2025）；本文证明 LLM 标注是第一个完全满足该质疑所列条件的应用场景，从而为穷举式 multiverse 分析提供首个正面案例（positive case）。" 这一 reframing 将论文从"方法迁移"（applying technique X to domain Y）提升为"方法论争论的解决"（resolving an open debate），后者的 novelty claim 远强于前者。当前写法中，E/N/U 分类适配被定位为 primary methodological contribution，但实际上 E/N/U 分类本身是操作层面的贡献——真正的理论高地是"为什么 LLM annotation 是 multiverse 的理想场景"这个认识论论证。
- 价值: 直接提升 Novelty 和 Significance。审稿人看到"apply X to Y"会本能地问 "so what"；看到"resolve an open methodological debate with the first positive case"则不同——这是对一个领域有影响力的方法论社区（specification curve / multiverse 的使用者和批评者）都有价值的贡献。
- 调研依据: Auspurg (PNAS 2025) 的三条件框架是当前 multiverse 方法论辩论的核心。通过搜索确认，尚无任何已发表工作声称为 Auspurg 三条件提供正面满足案例（positive case），这使得本文如果成功论证，将成为该辩论的关键参照点。

【发掘点 2】
- 维度: 前提假设质疑 + novelty 锐化
- 内容: "Constant estimand"（条件 a）是认识论论证中最脆弱的环节，而 proposal 目前对此处理过于轻描淡写。对于客观/事实性任务（情感极性二分类、NER），不同 pipeline 确实指向同一估量对象。但对于主观任务（toxicity、sentiment intensity、stance），proposal 自身引用的 Mehrotra et al. (2026) 已经论证"不同 LLM 视角是合法的不同视角，不是误差"——这直接暗示不同 pipeline 配置可能在隐性地改变估量对象（例如，GPT-4o 的"toxicity"和 Llama 的"toxicity"是否测量同一构念？）。如果审稿人沿这条线攻击，当前 proposal 缺乏防线。建议：**将此张力正面纳入论文框架**，发展出一个双层论证：(1) 对于客观任务，三条件完全成立，穷举 multiverse 无保留地适用；(2) 对于主观任务，条件 (a) 的成立性取决于我们对"估量对象"的元理论立场——若采取 perspectivism 立场（Mehrotra et al.），pipeline variation 中有一部分是构念层面的变异（construct-level variation），应归类为 Type U 而非 Type E。这意味着 E/N/U 框架不仅是操作工具，而是在理论层面自然地吸收了 objective vs. subjective 任务的区分。这一双层论证将认识论贡献从"LLM annotation 满足条件"深化为"E/N/U 框架提供了一种根据任务性质自适应地处理 constant-estimand 条件的机制"。
- 价值: 同时提升 Novelty（novelty claim 从"应用 multiverse"深化为"在理论层面整合 multiverse + perspectivism"）和 Related Work 差异化（与 Mehrotra et al. 从对立/冲突关系转为互补/整合关系，减少被审稿人用来攻击的面积）。
- 调研依据: 直接参考 Mehrotra et al. (arXiv:2603.21404, 2026) 的 Perspective-Driven Inference 框架，其核心论点——主观任务中标注分歧是视角差异而非误差——直接构成对 constant-estimand 假设的挑战。

【发掘点 3】
- 维度: significance 提升
- 内容: Proposal 当前的 significance 论证集中在"解决 prompt-hacking 问题"和"提供稳健性评估"。但有一个更高阶的 significance 角度未被触及：**multiverse robustness 与 validity 的关系**。一个发现可以在 multiverse 中高度稳健（所有 pipeline 一致）但仍然是错误的（所有 pipeline 共享相同的系统性偏差，例如所有 LLM 在特定人口群体上都偏低估 toxicity）。反之，一个发现可以在 multiverse 中看似脆弱（不同 pipeline 结论不一致）但某些 pipeline 配置实际上比其他更接近真实值。Proposal 提到了与 PPI/DSL 的对比实验（Stage 2 的 Comparative evaluation），但这是实验设计层面的安排——缺失的是**概念层面的清晰界定**：multiverse robustness 告诉我们什么、不告诉我们什么。建议在核心论证中增加一个明确的 scoping claim："Multiverse analysis 提供 robustness to pipeline choice（外部稳健性），PPI/DSL 提供 validity correction（内部准确性）；两者的交叉分类（robust+valid, robust+invalid, fragile+valid, fragile+invalid）构成 LLM 标注可信度的完整评估框架。" 如果能在论文中展示这个 2×2 框架并论证其实践价值，这篇论文的影响力将超越"multiverse 方法论"社区，对所有使用 LLM 标注的 CSS 研究者都有直接指导意义。
- 价值: 提升 Significance。从"提供一种稳健性检验工具"升级为"提出 LLM 标注可信度的完整评估框架"，影响面从方法论专家扩展到所有 CSS 从业者。
- 调研依据: 基于领域整体趋势判断。诊断派（Baumann, McLaren）关注"不稳定性有多严重"，修正派（Messing, PPI/DSL）关注"如何修正偏差"，但尚无工作系统地讨论 robustness 和 validity 的正交关系以及它们的组合含义。Audinet de Pieuchon et al. (EMNLP 2025) 对 DSL vs PPI 的 benchmark 是距离最近的工作，但仍局限于 validity 维度。

【发掘点 4】
- 维度: related work 差异化
- 内容: 当前 proposal 对 Variance-Aware LLM Annotation 框架（arXiv:2601.02370, Kosch & Feger 相关工作）的差异化定位是"protocol guidance rather than statistical inference"。这是准确的，但不够锐利。该框架使用 generalizability theory (G-theory) 分解五个方差源，报告了 12-85pp 的结果波动——这与 proposal 的 Stage 3 (Variance Decomposition) 在表面上高度相似（都是方差分解，都覆盖类似的 pipeline 维度）。审稿人很可能追问："你们的方差分解和他们的 G-theory 分解有什么区别？" 建议在 related work 中明确区分：G-theory 分解的是**标注准确率层面**的方差（annotation-level variance），而本文的 ANOVA 分解的是**下游推断层面**的方差（inference-level variance）——一个 pipeline 维度可能在标注层面引入大量方差但对下游假设检验结论无影响（因为偏差是系统性的、方向一致的），反之亦然。这个区分不是细节——它直接支撑了"诊断不等于推断"的核心论点。
- 价值: 提升 Related Work 差异化，减少审稿人认为"这不就是 G-theory 换了个壳"的风险。
- 调研依据: 直接参考 Variance-Aware LLM Annotation 框架 (arXiv:2601.02370)，其使用 G-theory 分解五个方差源的方法论与 proposal 的 Stage 3 在技术路线上最近似，需要最清晰的差异化。

Sources:
- [Baumann et al. - Large Language Model Hacking](https://arxiv.org/abs/2509.08825)
- [McLaren et al. - Magic Words or Methodical Work](https://arxiv.org/abs/2603.26898)
- [Messing - Hidden Measurement Error in LLM Pipelines](https://arxiv.org/abs/2604.11581)
- [Mehrotra et al. - Multi-Perspective LLM Annotations](https://arxiv.org/abs/2603.21404)
- [Auspurg - Robustness is better assessed with a few thoughtful models](https://www.pnas.org/doi/10.1073/pnas.2521917122)
- [Ganslmeier & Vlandas - Reply to Auspurg](https://www.pnas.org/doi/10.1073/pnas.2523374122)
- [Carlson & Burbano - Use of LLMs to annotate data in management research](https://sms.onlinelibrary.wiley.com/doi/10.1002/smj.70023)
- [Variance-Aware LLM Annotation](https://arxiv.org/pdf/2601.02370)
- [SMART Registration Tool](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12567067/)
- [Boba: Authoring and Visualizing Multiverse Analyses](https://idl.uw.edu/papers/boba)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21aa738b-d346-4a5d-992b-cb14047bed0f",
  "isSidechain": false,
  "requestId": "req_011CbDA9PD32Uk18Wq6AhA3E",
  "type": "assistant",
  "uuid": "dac4b00b-7e86-432f-a6a5-1d67dc78611c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L6FJ3NxH3qS7rBnHgGDNrR",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 955,
      "cache_read_input_tokens": 30917,
      "output_tokens": 5650,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 955,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5650,
          "cache_read_input_tokens": 30917,
          "cache_creation_input_tokens": 955,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 955
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
  "leafUuid": "dac4b00b-7e86-432f-a6a5-1d67dc78611c",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Specification curve analysis for LLM annotation robustness",
  "sessionId": "3976331e-36ff-46c2-b0a6-249940c3361d"
}
```

---
