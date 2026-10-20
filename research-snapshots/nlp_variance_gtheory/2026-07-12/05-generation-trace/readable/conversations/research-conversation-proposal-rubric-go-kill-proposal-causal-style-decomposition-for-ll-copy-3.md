# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Causal Style Decomposition for LL

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-2/7c36a60e-68e4-44f4-9221-decc94c3003a.jsonl`
- **Structured JSON:** [`3c72230dd8c6f6459de0.json`](../../sessions/3c/3c72230dd8c6f6459de0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T04:40:13.275Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T04:40:13.275Z",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Causal Style Decomposition for LLM Judge Debiasing via Doubly-Robust Counterfactual Estimation\n\n## Description\nStyle bias is the dominant systematic bias in LLM-as-a-judge evaluations (effect size 0.76–0.92 across all major models), vastly exceeding position bias (≤0.04), yet no existing method causally isolates and removes style's contribution to black-box judge scores. FairJudge (Feb 2026) addresses style bias by retraining a dedicated judge, but cannot debias commercial APIs like GPT-4o or Claude. We introduce Causal Style Decomposition (CSD), a model-agnostic post-hoc debiasing framework that generates content-preserving binary style counterfactuals along three independent axes (formality, verbosity, formatting) using RATE's double-rewrite protocol, then estimates per-axis causal effects via a Double Machine Learning partially linear model (Chernozhukov et al. 2018) that preserves interpretable style coefficients while allowing arbitrary nonlinear content-quality effects. A legitimacy-aware correction avoids over-debiasing by tuning a conservatism parameter α that distinguishes domain-invariant style bias from legitimate style-quality correlations. Unlike FairJudge (requires retraining), Length-Controlled AlpacaEval (single dimension), or Bias-Bounded Evaluation (non-causal noise injection), CSD provides a principled, multi-dimensional causal decomposition applicable to any black-box judge. We evaluate across five LLM judges on SOS-Bench (objective correctness), LLMBar adversarial (style resistance), RewardBench (domain-specific), and RubricBench (atomic rubric-based), supplemented by a 200-response pilot study with separate human annotations for content and presentation quality. An optional amortized deployment stage trains a lightweight predictor to estimate style effects without generating new counterfactuals, reducing marginal overhead to near-zero. CSD requires no judge retraining, applies to any black-box judge API, and reduces per-response debiasing cost from 25x (naive) to ~7x (full pipeline) or near-zero (amortized).\n\n## Core Problem\nHow can we isolate and remove the causal effect of surface-level style on LLM judge scores while preserving legitimate style-content associations, recovering a score that more faithfully reflects content quality?\n\n## Opportunity\nStyle bias is the dominant bias in LLM judges (effect size 0.76–0.92 across all models per Soumik 2026), vastly exceeding position bias (≤0.04), yet debiasing research overwhelmingly targets position bias. SOS-Bench (ICLR 2025) demonstrated that LLM judges prioritize style over factuality and safety across 152,380 data points. The 'Preference Leakage' paper (ICLR 2026) found judges rely heavily on 'stylistic regularities—tone consistency, sentence cadence, punctuation density.' FairJudge (arXiv Feb 2026) addresses style bias through judge retraining (SFT+DPO+GRPO), but this requires training a new judge model and does not apply to black-box commercial judges. Meanwhile, the CASSE study (Jan 2026) shows style features are 'deeply entangled rather than orthogonal'—prompting for conciseness significantly reduces perceived expertise—highlighting that naive style removal risks destroying legitimate quality signals. This creates a need for a principled causal method that can (a) apply to any black-box judge, (b) quantify per-response style contributions, and (c) distinguish bias from legitimate style-quality correlation. Causal intervention techniques for LLMs now achieve 92.3% style transfer accuracy while preserving content, and the RATE framework (ICML 2025) provides a double-rewrite protocol for unbiased estimation with imperfect counterfactuals, making this technically feasible.\n\n## Landscape\nSOS-Bench (ICLR 2025) is the largest meta-benchmark documenting style-over-substance failure but proposes no fix. FairJudge (arXiv 2602.06625, Feb 2026) is the most directly relevant concurrent work: it trains a dedicated judge via SFT→DPO→GRPO on a curated 16K-instance dataset with contrastive perturbations along five non-semantic dimensions (position, length, format, reasoning style, model provenance), achieving 76.83% agreement on PandaLM and 78.82% on JudgeLM; however, it requires retraining a new judge model (Qwen3-VL 2B/4B/8B backbones) and cannot debias existing black-box commercial judges (GPT-4o, Claude, Gemini). Soumik (April 2026) tests 9 debiasing strategies across 5 judges but focuses on position/verbosity bias without systematic causal style removal. JudgeBiasBench (March 2026) uses Gemini-2.0-Flash for counterfactual bias injection but applies this to construct biased test instances rather than to estimate and remove style effects. RATE (ICML 2025) is the closest methodological precedent—it estimates causal effects of high-level attributes on reward model scores via a double-rewrite correction for imperfect counterfactuals—but targets reward model explainability, not judge debiasing. The ISE framework (Choi et al., NAACL 2024) argues ATE is inapplicable to text treatments due to positivity violations from high dimensionality, but this criticism applies to free-text treatments, not to well-defined binary style interventions where positivity holds by construction (Pryzant et al. 2021; Veitch et al. UAI 2020). Length-Controlled AlpacaEval (ICLR 2025) demonstrates effective post-hoc regression debiasing but only controls for a single dimension (length) at zero additional inference cost. Bias-Bounded Evaluation (arXiv March 2026) injects calibrated Gaussian noise for differential-privacy-inspired debiasing, retaining 61–99% ranking correlation on Arena-Hard-Auto. CyclicJudge (arXiv March 2026) uses round-robin judge assignment to reduce inter-judge variance but is style-agnostic. RBD (NeurIPS 2025) fine-tunes a reasoning-based bias detector achieving 18.5% accuracy improvement but without causal style decomposition. UDA (AAAI 2026) reduces inter-judge Elo divergence by 63.4% via adaptive K-factor calibration. The CASSE dataset (Jan 2026) documents cross-feature stylistic interactions across 12 style features, showing conciseness reduces perceived expertise, supporting our legitimacy-aware correction design. Causal Effect Estimation with Latent Textual Treatments (arXiv Feb 2026) proposes SAE-based causal estimation for latent text features but has not been applied to judge debiasing. Double Machine Learning (Chernozhukov et al. 2018) provides the partially linear model framework and DoubleML Python package we adopt for flexible decomposition. No arXiv preprint or OpenReview submission as of May 2026 proposes content-preserving binary style counterfactuals combined with doubly-robust DML estimation for black-box judge debiasing.\n\n## Approach\nWe propose Causal Style Decomposition (CSD), a model-agnostic post-hoc debiasing framework in four stages.\n\n**Stage 1 — Binary Style Counterfactual Generation.** For each response under evaluation, generate style counterfactuals along three binary axes: (A1) formality (formal ↔ casual), (A2) verbosity (verbose ↔ terse), (A3) formatting (structured/markdown ↔ plain prose). These three axes are chosen for genuine independence: formality concerns register and word choice, verbosity concerns information density, and formatting concerns visual layout. We use Qwen3-32B with axis-specific prompts, applying the RATE double-rewrite protocol: for each axis, generate (i) a counterfactual x' by flipping the axis and (ii) a double-rewrite x'' by flipping x' back. This yields 6 rewrites per response (2 per axis). Content preservation is enforced via a conjunction of BERTScore ≥ 0.92, NLI entailment ≥ 0.95 (DeBERTa-v3-large-MNLI), GPT-4o-mini content-preservation verification, and human spot-checks on a 10% random sample. **Theoretical justification for binary ATE:** Unlike free-text treatments where positivity is structurally violated (Choi et al. NAACL 2024), binary style axes define well-posed interventions satisfying positivity—any text can be made formal or casual, verbose or terse, structured or plain—following the functional intervention framework (Pryzant et al. 2021; Veitch et al. UAI 2020). RATE's Assumption 1 (direction-independent rewrite noise) and Assumption 2 (additive decomposition of reward into attribute and noise components) provide sufficient conditions for unbiased ATE estimation under imperfect counterfactuals.\n\n**Stage 2 — Doubly-Robust Causal Effect Estimation via DML.** Score each original response and its 6 counterfactuals with the target LLM judge (7 scorings per response). Estimate per-axis treatment effects using a Double Machine Learning partially linear model (Chernozhukov et al. 2018): score = β₁·formality + β₂·verbosity + β₃·formatting + g(content_features) + ε, where β coefficients capture interpretable style effects and g(·) is a nonparametric function of content features (estimated via gradient-boosted trees with 5-fold cross-fitting). This replaces the linear additive SCM: the partially linear form preserves interpretable style coefficients while allowing arbitrary nonlinear content-quality effects, and the doubly-robust property ensures consistency if either the outcome model or propensity model is correctly specified. For handling residual axis correlations (e.g., formatting weakly correlating with verbosity), we use the multivariate treatment extension of DoubleML, jointly estimating all three β coefficients rather than decomposing them independently. We include ablations comparing: (i) linear additive, (ii) DML partially linear, and (iii) fully nonparametric (kernel-based) decompositions, plus an ISE-based continuous estimator as a methodological comparison.\n\n**Stage 3 — Legitimacy-Aware Score Adjustment.** Rather than naively subtracting the full estimated style ATE (which risks over-correction when style legitimately signals quality—e.g., well-structured markdown for technical content), we introduce a conservatism parameter α ∈ [0,1]: debiased_score = raw_score − α · Σ β_k · style_k. We determine α by maximizing Spearman correlation with ground-truth quality on a held-out validation set. Additionally, we test domain-conditional α values: for each content domain (coding, reasoning, creative writing, factual QA), we estimate whether style-quality correlations are legitimate by checking if style effects are consistent across domains (bias) vs. domain-specific (potentially legitimate). Style effects that are large and domain-invariant are classified as bias; domain-specific effects are partially retained.\n\n**Stage 4 — Amortized Deployment (optional).** To reduce the ~7x overhead of full CSD for large-scale deployment, we train a lightweight amortized style-effect predictor: a small regression model (e.g., linear probe on text embeddings from a frozen encoder) trained on the counterfactual data from Stage 1–2 to predict per-response style attribution vectors from response features alone. At deployment, this predictor estimates style effects without generating new counterfactuals, reducing marginal cost to near-zero. We validate that the amortized predictor recovers ≥90% of the debiasing improvement of the full pipeline.\n\n**Evaluation.** We evaluate across five LLM judges (GPT-4o, Claude Sonnet 4, Gemini 2.5 Pro, Llama-3.3-70B, Qwen3-32B) on four benchmarks: (1) SOS-Bench—measuring whether debiased scores better correlate with objective correctness on constituent benchmarks (IFEval, MMLU-Pro, GPQA) rather than style; (2) LLMBar adversarial set—measuring whether debiased judges resist choosing wrong-but-polished over correct-but-plain responses; (3) RewardBench—domain-specific analysis across chat-hard, safety, and reasoning subsets; (4) RubricBench—1,147 pairwise comparisons with expert-annotated atomic rubrics targeting misleading surface bias. We additionally conduct a 200-response pilot human annotation study with separate 5-point Likert scales for content quality and presentation quality, providing direct validation that debiased scores correlate with content ratings while discounting presentation ratings. Baselines: FairJudge-8B, Length-Controlled AlpacaEval regression, Bias-Bounded Evaluation, raw (undebiased) judges, and a 'format normalization' baseline that strips all markdown before judging.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '100–140 A100-80GB hours (style counterfactual generation with Qwen3-32B: 6 rewrites/response × ~2K responses ≈ 30h; content verification BERTScore/NLI: 3h; open-source judge inference: 25h; DML estimation and ablations: 5h; amortized model training: 2h; iteration buffer: 35–75h)', 'timeline': '12–14 weeks', 'estimated_gpu_cost': '$250–350 (A100 spot ~$2.50/hr) + $200–350 commercial judge API costs (GPT-4o, Claude Sonnet 4, Gemini 2.5 Pro) + $100–150 GPT-4o-mini content verification + $800–1200 pilot annotation study (200 responses × 3 annotators)'}, 'human_in_loop': {'gpu_hours': '100–140 A100-80GB hours', 'timeline': '9–11 weeks', 'claude_api_cost': '$150–300 (Sonnet 4.6 at $3/$15 per MTok for prompt engineering, counterfactual quality analysis, DML specification, ablation design, and paper drafting)', 'estimated_gpu_cost': '$250–350 + $200–350 commercial judge API + $100–150 GPT-4o-mini + $800–1200 annotation study'}, 'auto_research': {'gpu_hours': '150–220 A100-80GB hours (additional ablations: linear vs. DML vs. nonparametric, ISE comparison, α sensitivity sweeps, domain-conditional analysis, amortized predictor architectures)', 'timeline': '5–7 weeks', 'claude_api_cost': '$500–750 (Sonnet 4.6 for experiment orchestration, automated counterfactual quality filtering, DML cross-fitting, statistical analysis, and full paper drafting)', 'estimated_gpu_cost': '$375–550 + $300–450 commercial judge API + $150–200 GPT-4o-mini + $800–1200 annotation study', 'speed_bottleneck': 'Sequential dependency chain: style counterfactual generation → content-preservation validation (including human spot-checks) → judge scoring → DML estimation; human annotation study runs in parallel but requires ~2 weeks for annotator recruitment and completion'}}\n\n## Inspired By\nField guide finding: 'Style bias is the dominant bias (0.76–0.92) yet has received minimal research attention'; SOS-Bench limitation that it documents but doesn't solve the problem; FairJudge's success at training-based debiasing motivating the question of whether a model-agnostic alternative exists; RATE's double-rewrite correction as a principled solution to imperfect-counterfactual bias; DML/partially-linear models as the standard tool for flexible causal decomposition with interpretable treatment coefficients; CASSE's finding that style features are entangled motivating legitimacy-aware correction.\n\n## Target Venues\n- AAAI 2027 (abstract: July 21, full paper: July 28, 2026 — primary target, 10 weeks)\n- ICLR 2027 (estimated deadline: September 24, 2026 — comfortable 18-week runway)\n- ARR October 2026 cycle (estimated deadline: October 15, 2026 — tertiary option, 21-week runway)\n\n## Key References\n- Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking (ICLR 2025)\n- Preference Leakage: A Contamination Problem in LLM-as-a-judge (ICLR 2026)\n- FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge (arXiv 2602.06625, Feb 2026)\n- Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines (arXiv 2026)\n- Toward Robust LLM-Based Judges: Taxonomic Bias Evaluation and Debiasing Optimization (arXiv 2026)\n- RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals (ICML 2025)\n- Double/Debiased Machine Learning for Treatment and Structural Parameters (Chernozhukov et al., Econometrics Journal 2018)\n- Causal Inference for Human-Language Model Collaboration (Choi et al., NAACL 2024)\n- Adapting Text Embeddings for Causal Inference (Veitch, Sridhar & Blei, UAI 2020)\n- Causal Effects of Linguistic Properties (Pryzant et al., NAACL 2021)\n- A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents (CASSE, arXiv 2601.10809, Jan 2026)\n- Counterfactual LLM-based Framework for Measuring Rhetorical Style (arXiv 2025)\n- Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators (ICLR 2025)\n- Any Large Language Model Can Be a Reliable Judge: Debiasing with a Reasoning-based Bias Detector (NeurIPS 2025)\n- Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation (arXiv 2026)\n- CausalPFN: Amortized Causal Effect Estimation via In-Context Learning (NeurIPS 2025)\n- RubricBench: Aligning Model-Generated Rubrics with Human Standards (arXiv 2603.01562, March 2026)\n- Estimating Causal Effects of Text Interventions Leveraging LLMs (Findings of AACL-IJCNLP 2025)\n- Causal Effect Estimation with Latent Textual Treatments (arXiv 2026)\n- How to Make Causal Inferences Using Texts (Egami et al., Science Advances 2022)\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T04:40:13.278Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T04:40:13.278Z",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a"
}
```

---

## Round 1

47 recorded events

### User

_source line 3 · 2026-05-20T04:40:13.289Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# Causal Style Decomposition for LLM Judge Debiasing via Doubly-Robust Counterfactual Estimation

## Description
Style bias is the dominant systematic bias in LLM-as-a-judge evaluations (effect size 0.76–0.92 across all major models), vastly exceeding position bias (≤0.04), yet no existing method causally isolates and removes style's contribution to black-box judge scores. FairJudge (Feb 2026) addresses style bias by retraining a dedicated judge, but cannot debias commercial APIs like GPT-4o or Claude. We introduce Causal Style Decomposition (CSD), a model-agnostic post-hoc debiasing framework that generates content-preserving binary style counterfactuals along three independent axes (formality, verbosity, formatting) using RATE's double-rewrite protocol, then estimates per-axis causal effects via a Double Machine Learning partially linear model (Chernozhukov et al. 2018) that preserves interpretable style coefficients while allowing arbitrary nonlinear content-quality effects. A legitimacy-aware correction avoids over-debiasing by tuning a conservatism parameter α that distinguishes domain-invariant style bias from legitimate style-quality correlations. Unlike FairJudge (requires retraining), Length-Controlled AlpacaEval (single dimension), or Bias-Bounded Evaluation (non-causal noise injection), CSD provides a principled, multi-dimensional causal decomposition applicable to any black-box judge. We evaluate across five LLM judges on SOS-Bench (objective correctness), LLMBar adversarial (style resistance), RewardBench (domain-specific), and RubricBench (atomic rubric-based), supplemented by a 200-response pilot study with separate human annotations for content and presentation quality. An optional amortized deployment stage trains a lightweight predictor to estimate style effects without generating new counterfactuals, reducing marginal overhead to near-zero. CSD requires no judge retraining, applies to any black-box judge API, and reduces per-response debiasing cost from 25x (naive) to ~7x (full pipeline) or near-zero (amortized).

## Core Problem
How can we isolate and remove the causal effect of surface-level style on LLM judge scores while preserving legitimate style-content associations, recovering a score that more faithfully reflects content quality?

## Opportunity
Style bias is the dominant bias in LLM judges (effect size 0.76–0.92 across all models per Soumik 2026), vastly exceeding position bias (≤0.04), yet debiasing research overwhelmingly targets position bias. SOS-Bench (ICLR 2025) demonstrated that LLM judges prioritize style over factuality and safety across 152,380 data points. The 'Preference Leakage' paper (ICLR 2026) found judges rely heavily on 'stylistic regularities—tone consistency, sentence cadence, punctuation density.' FairJudge (arXiv Feb 2026) addresses style bias through judge retraining (SFT+DPO+GRPO), but this requires training a new judge model and does not apply to black-box commercial judges. Meanwhile, the CASSE study (Jan 2026) shows style features are 'deeply entangled rather than orthogonal'—prompting for conciseness significantly reduces perceived expertise—highlighting that naive style removal risks destroying legitimate quality signals. This creates a need for a principled causal method that can (a) apply to any black-box judge, (b) quantify per-response style contributions, and (c) distinguish bias from legitimate style-quality correlation. Causal intervention techniques for LLMs now achieve 92.3% style transfer accuracy while preserving content, and the RATE framework (ICML 2025) provides a double-rewrite protocol for unbiased estimation with imperfect counterfactuals, making this technically feasible.

## Landscape
SOS-Bench (ICLR 2025) is the largest meta-benchmark documenting style-over-substance failure but proposes no fix. FairJudge (arXiv 2602.06625, Feb 2026) is the most directly relevant concurrent work: it trains a dedicated judge via SFT→DPO→GRPO on a curated 16K-instance dataset with contrastive perturbations along five non-semantic dimensions (position, length, format, reasoning style, model provenance), achieving 76.83% agreement on PandaLM and 78.82% on JudgeLM; however, it requires retraining a new judge model (Qwen3-VL 2B/4B/8B backbones) and cannot debias existing black-box commercial judges (GPT-4o, Claude, Gemini). Soumik (April 2026) tests 9 debiasing strategies across 5 judges but focuses on position/verbosity bias without systematic causal style removal. JudgeBiasBench (March 2026) uses Gemini-2.0-Flash for counterfactual bias injection but applies this to construct biased test instances rather than to estimate and remove style effects. RATE (ICML 2025) is the closest methodological precedent—it estimates causal effects of high-level attributes on reward model scores via a double-rewrite correction for imperfect counterfactuals—but targets reward model explainability, not judge debiasing. The ISE framework (Choi et al., NAACL 2024) argues ATE is inapplicable to text treatments due to positivity violations from high dimensionality, but this criticism applies to free-text treatments, not to well-defined binary style interventions where positivity holds by construction (Pryzant et al. 2021; Veitch et al. UAI 2020). Length-Controlled AlpacaEval (ICLR 2025) demonstrates effective post-hoc regression debiasing but only controls for a single dimension (length) at zero additional inference cost. Bias-Bounded Evaluation (arXiv March 2026) injects calibrated Gaussian noise for differential-privacy-inspired debiasing, retaining 61–99% ranking correlation on Arena-Hard-Auto. CyclicJudge (arXiv March 2026) uses round-robin judge assignment to reduce inter-judge variance but is style-agnostic. RBD (NeurIPS 2025) fine-tunes a reasoning-based bias detector achieving 18.5% accuracy improvement but without causal style decomposition. UDA (AAAI 2026) reduces inter-judge Elo divergence by 63.4% via adaptive K-factor calibration. The CASSE dataset (Jan 2026) documents cross-feature stylistic interactions across 12 style features, showing conciseness reduces perceived expertise, supporting our legitimacy-aware correction design. Causal Effect Estimation with Latent Textual Treatments (arXiv Feb 2026) proposes SAE-based causal estimation for latent text features but has not been applied to judge debiasing. Double Machine Learning (Chernozhukov et al. 2018) provides the partially linear model framework and DoubleML Python package we adopt for flexible decomposition. No arXiv preprint or OpenReview submission as of May 2026 proposes content-preserving binary style counterfactuals combined with doubly-robust DML estimation for black-box judge debiasing.

## Approach
We propose Causal Style Decomposition (CSD), a model-agnostic post-hoc debiasing framework in four stages.

**Stage 1 — Binary Style Counterfactual Generation.** For each response under evaluation, generate style counterfactuals along three binary axes: (A1) formality (formal ↔ casual), (A2) verbosity (verbose ↔ terse), (A3) formatting (structured/markdown ↔ plain prose). These three axes are chosen for genuine independence: formality concerns register and word choice, verbosity concerns information density, and formatting concerns visual layout. We use Qwen3-32B with axis-specific prompts, applying the RATE double-rewrite protocol: for each axis, generate (i) a counterfactual x' by flipping the axis and (ii) a double-rewrite x'' by flipping x' back. This yields 6 rewrites per response (2 per axis). Content preservation is enforced via a conjunction of BERTScore ≥ 0.92, NLI entailment ≥ 0.95 (DeBERTa-v3-large-MNLI), GPT-4o-mini content-preservation verification, and human spot-checks on a 10% random sample. **Theoretical justification for binary ATE:** Unlike free-text treatments where positivity is structurally violated (Choi et al. NAACL 2024), binary style axes define well-posed interventions satisfying positivity—any text can be made formal or casual, verbose or terse, structured or plain—following the functional intervention framework (Pryzant et al. 2021; Veitch et al. UAI 2020). RATE's Assumption 1 (direction-independent rewrite noise) and Assumption 2 (additive decomposition of reward into attribute and noise components) provide sufficient conditions for unbiased ATE estimation under imperfect counterfactuals.

**Stage 2 — Doubly-Robust Causal Effect Estimation via DML.** Score each original response and its 6 counterfactuals with the target LLM judge (7 scorings per response). Estimate per-axis treatment effects using a Double Machine Learning partially linear model (Chernozhukov et al. 2018): score = β₁·formality + β₂·verbosity + β₃·formatting + g(content_features) + ε, where β coefficients capture interpretable style effects and g(·) is a nonparametric function of content features (estimated via gradient-boosted trees with 5-fold cross-fitting). This replaces the linear additive SCM: the partially linear form preserves interpretable style coefficients while allowing arbitrary nonlinear content-quality effects, and the doubly-robust property ensures consistency if either the outcome model or propensity model is correctly specified. For handling residual axis correlations (e.g., formatting weakly correlating with verbosity), we use the multivariate treatment extension of DoubleML, jointly estimating all three β coefficients rather than decomposing them independently. We include ablations comparing: (i) linear additive, (ii) DML partially linear, and (iii) fully nonparametric (kernel-based) decompositions, plus an ISE-based continuous estimator as a methodological comparison.

**Stage 3 — Legitimacy-Aware Score Adjustment.** Rather than naively subtracting the full estimated style ATE (which risks over-correction when style legitimately signals quality—e.g., well-structured markdown for technical content), we introduce a conservatism parameter α ∈ [0,1]: debiased_score = raw_score − α · Σ β_k · style_k. We determine α by maximizing Spearman correlation with ground-truth quality on a held-out validation set. Additionally, we test domain-conditional α values: for each content domain (coding, reasoning, creative writing, factual QA), we estimate whether style-quality correlations are legitimate by checking if style effects are consistent across domains (bias) vs. domain-specific (potentially legitimate). Style effects that are large and domain-invariant are classified as bias; domain-specific effects are partially retained.

**Stage 4 — Amortized Deployment (optional).** To reduce the ~7x overhead of full CSD for large-scale deployment, we train a lightweight amortized style-effect predictor: a small regression model (e.g., linear probe on text embeddings from a frozen encoder) trained on the counterfactual data from Stage 1–2 to predict per-response style attribution vectors from response features alone. At deployment, this predictor estimates style effects without generating new counterfactuals, reducing marginal cost to near-zero. We validate that the amortized predictor recovers ≥90% of the debiasing improvement of the full pipeline.

**Evaluation.** We evaluate across five LLM judges (GPT-4o, Claude Sonnet 4, Gemini 2.5 Pro, Llama-3.3-70B, Qwen3-32B) on four benchmarks: (1) SOS-Bench—measuring whether debiased scores better correlate with objective correctness on constituent benchmarks (IFEval, MMLU-Pro, GPQA) rather than style; (2) LLMBar adversarial set—measuring whether debiased judges resist choosing wrong-but-polished over correct-but-plain responses; (3) RewardBench—domain-specific analysis across chat-hard, safety, and reasoning subsets; (4) RubricBench—1,147 pairwise comparisons with expert-annotated atomic rubrics targeting misleading surface bias. We additionally conduct a 200-response pilot human annotation study with separate 5-point Likert scales for content quality and presentation quality, providing direct validation that debiased scores correlate with content ratings while discounting presentation ratings. Baselines: FairJudge-8B, Length-Controlled AlpacaEval regression, Bias-Bounded Evaluation, raw (undebiased) judges, and a 'format normalization' baseline that strips all markdown before judging.

## Resource Estimate
{'manual': {'gpu_hours': '100–140 A100-80GB hours (style counterfactual generation with Qwen3-32B: 6 rewrites/response × ~2K responses ≈ 30h; content verification BERTScore/NLI: 3h; open-source judge inference: 25h; DML estimation and ablations: 5h; amortized model training: 2h; iteration buffer: 35–75h)', 'timeline': '12–14 weeks', 'estimated_gpu_cost': '$250–350 (A100 spot ~$2.50/hr) + $200–350 commercial judge API costs (GPT-4o, Claude Sonnet 4, Gemini 2.5 Pro) + $100–150 GPT-4o-mini content verification + $800–1200 pilot annotation study (200 responses × 3 annotators)'}, 'human_in_loop': {'gpu_hours': '100–140 A100-80GB hours', 'timeline': '9–11 weeks', 'claude_api_cost': '$150–300 (Sonnet 4.6 at $3/$15 per MTok for prompt engineering, counterfactual quality analysis, DML specification, ablation design, and paper drafting)', 'estimated_gpu_cost': '$250–350 + $200–350 commercial judge API + $100–150 GPT-4o-mini + $800–1200 annotation study'}, 'auto_research': {'gpu_hours': '150–220 A100-80GB hours (additional ablations: linear vs. DML vs. nonparametric, ISE comparison, α sensitivity sweeps, domain-conditional analysis, amortized predictor architectures)', 'timeline': '5–7 weeks', 'claude_api_cost': '$500–750 (Sonnet 4.6 for experiment orchestration, automated counterfactual quality filtering, DML cross-fitting, statistical analysis, and full paper drafting)', 'estimated_gpu_cost': '$375–550 + $300–450 commercial judge API + $150–200 GPT-4o-mini + $800–1200 annotation study', 'speed_bottleneck': 'Sequential dependency chain: style counterfactual generation → content-preservation validation (including human spot-checks) → judge scoring → DML estimation; human annotation study runs in parallel but requires ~2 weeks for annotator recruitment and completion'}}

## Inspired By
Field guide finding: 'Style bias is the dominant bias (0.76–0.92) yet has received minimal research attention'; SOS-Bench limitation that it documents but doesn't solve the problem; FairJudge's success at training-based debiasing motivating the question of whether a model-agnostic alternative exists; RATE's double-rewrite correction as a principled solution to imperfect-counterfactual bias; DML/partially-linear models as the standard tool for flexible causal decomposition with interpretable treatment coefficients; CASSE's finding that style features are entangled motivating legitimacy-aware correction.

## Target Venues
- AAAI 2027 (abstract: July 21, full paper: July 28, 2026 — primary target, 10 weeks)
- ICLR 2027 (estimated deadline: September 24, 2026 — comfortable 18-week runway)
- ARR October 2026 cycle (estimated deadline: October 15, 2026 — tertiary option, 21-week runway)

## Key References
- Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking (ICLR 2025)
- Preference Leakage: A Contamination Problem in LLM-as-a-judge (ICLR 2026)
- FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge (arXiv 2602.06625, Feb 2026)
- Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines (arXiv 2026)
- Toward Robust LLM-Based Judges: Taxonomic Bias Evaluation and Debiasing Optimization (arXiv 2026)
- RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals (ICML 2025)
- Double/Debiased Machine Learning for Treatment and Structural Parameters (Chernozhukov et al., Econometrics Journal 2018)
- Causal Inference for Human-Language Model Collaboration (Choi et al., NAACL 2024)
- Adapting Text Embeddings for Causal Inference (Veitch, Sridhar & Blei, UAI 2020)
- Causal Effects of Linguistic Properties (Pryzant et al., NAACL 2021)
- A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents (CASSE, arXiv 2601.10809, Jan 2026)
- Counterfactual LLM-based Framework for Measuring Rhetorical Style (arXiv 2025)
- Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators (ICLR 2025)
- Any Large Language Model Can Be a Reliable Judge: Debiasing with a Reasoning-based Bias Detector (NeurIPS 2025)
- Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation (arXiv 2026)
- CausalPFN: Amortized Causal Effect Estimation via In-Context Learning (NeurIPS 2025)
- RubricBench: Aligning Model-Generated Rubrics with Human Standards (arXiv 2603.01562, March 2026)
- Estimating Causal Effects of Text Interventions Leveraging LLMs (Findings of AACL-IJCNLP 2025)
- Causal Effect Estimation with Latent Textual Treatments (arXiv 2026)
- How to Make Causal Inferences Using Texts (Egami et al., Science Advances 2022)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "7f63e8fc-85c3-4e6d-bc0e-cacc7b545dea",
  "type": "user",
  "uuid": "b404c421-1cd6-4f24-b8d3-44778a0eb5ad",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T04:40:13.288Z_

```json
{
  "parentUuid": "b404c421-1cd6-4f24-b8d3-44778a0eb5ad",
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
  "uuid": "baad816e-7218-4de7-9faa-1515894d8f4b",
  "timestamp": "2026-05-20T04:40:13.288Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T04:40:13.288Z_

```json
{
  "parentUuid": "baad816e-7218-4de7-9faa-1515894d8f4b",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "356e14ec-780c-468d-87f4-a5f1a48b0b94",
  "timestamp": "2026-05-20T04:40:13.288Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Causal Style Decomposition for LLM Judge Debiasing via Doubly-Robust Counterfactual Estimation  ## Description S…",
  "leafUuid": "356e14ec-780c-468d-87f4-a5f1a48b0b94",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate LLM judge style bias debiasing proposal",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a"
}
```

---

### Assistant

_source line 8 · 2026-05-20T04:40:22.380Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for EMNLP 2026 submission. I need to follow the rubric carefully:

1. First, do 3-5 WebSearches to understand the field
2. Then evaluate on 3 dimensions: Novelty, Significance, Related Work
3. Answer the Trivial Alternative and Premise Assumption checks
4. Give a probability estimate

Let me start by searching for the key topics and papers mentioned in this proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "356e14ec-780c-468d-87f4-a5f1a48b0b94",
  "isSidechain": false,
  "requestId": "req_011CbDCrp96ohhQM4k9TyfJX",
  "type": "assistant",
  "uuid": "2c117104-0815-47cd-b89e-98c21a6fb368",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lp2yqY8Zqh4rH5v5qDwvM3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 20452,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 227,
          "cache_read_input_tokens": 20452,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 9 · 2026-05-20T04:40:22.914Z_

I'll start by conducting thorough field research before making any assessment. Let me search for the key topics and papers mentioned in this proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c117104-0815-47cd-b89e-98c21a6fb368",
  "isSidechain": false,
  "requestId": "req_011CbDCrp96ohhQM4k9TyfJX",
  "type": "assistant",
  "uuid": "2091b7cf-6ad6-422f-bc27-ddf28eeaf61c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lp2yqY8Zqh4rH5v5qDwvM3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 20452,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 227,
          "cache_read_input_tokens": 20452,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 10 · 2026-05-20T04:40:23.486Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01M8ML8zqUjnSYsJHaPeUc85`</summary>

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
  "parentUuid": "2091b7cf-6ad6-422f-bc27-ddf28eeaf61c",
  "isSidechain": false,
  "requestId": "req_011CbDCrp96ohhQM4k9TyfJX",
  "type": "assistant",
  "uuid": "979d6579-e4fe-42e9-adee-25def0fad14f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lp2yqY8Zqh4rH5v5qDwvM3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 20452,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 227,
          "cache_read_input_tokens": 20452,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 11 · 2026-05-20T04:40:23.493Z_

<details><summary>↩ Tool result · `toolu_01M8ML8zqUjnSYsJHaPeUc85`</summary>

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
  "parentUuid": "979d6579-e4fe-42e9-adee-25def0fad14f",
  "isSidechain": false,
  "promptId": "7f63e8fc-85c3-4e6d-bc0e-cacc7b545dea",
  "type": "user",
  "uuid": "3353ef01-789c-4123-99ed-a86396435dc9",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "979d6579-e4fe-42e9-adee-25def0fad14f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-20T04:40:27.593Z_

Now let me conduct the field research with multiple targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3353ef01-789c-4123-99ed-a86396435dc9",
  "isSidechain": false,
  "requestId": "req_011CbDCsZw7dPufvE4LDb9Fn",
  "type": "assistant",
  "uuid": "7344ce4d-3a3d-4d12-9ef0-1e82b9eee198",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DSbzcXZvK6LtrnuPLxsBCy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 752,
      "cache_read_input_tokens": 20452,
      "output_tokens": 297,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 752,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 297,
          "cache_read_input_tokens": 20452,
          "cache_creation_input_tokens": 752,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 752
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

_source line 13 · 2026-05-20T04:40:28.129Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BoneuXka1XvjfsheH6b3aM`</summary>

```json
{
  "query": "LLM judge style bias debiasing causal 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7344ce4d-3a3d-4d12-9ef0-1e82b9eee198",
  "isSidechain": false,
  "requestId": "req_011CbDCsZw7dPufvE4LDb9Fn",
  "type": "assistant",
  "uuid": "6a6c1ff7-9970-45d2-94fb-93c38cf208d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DSbzcXZvK6LtrnuPLxsBCy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 752,
      "cache_read_input_tokens": 20452,
      "output_tokens": 297,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 752,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 297,
          "cache_read_input_tokens": 20452,
          "cache_creation_input_tokens": 752,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 752
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

_source line 14 · 2026-05-20T04:40:29.078Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013JDmhByeHtenGeDvCpFYqc`</summary>

```json
{
  "query": "FairJudge LLM debiasing arXiv 2602.06625 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a6c1ff7-9970-45d2-94fb-93c38cf208d5",
  "isSidechain": false,
  "requestId": "req_011CbDCsZw7dPufvE4LDb9Fn",
  "type": "assistant",
  "uuid": "0e4b3030-15a6-46fb-a444-b0b715790649",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DSbzcXZvK6LtrnuPLxsBCy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 752,
      "cache_read_input_tokens": 20452,
      "output_tokens": 297,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 752,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 297,
          "cache_read_input_tokens": 20452,
          "cache_creation_input_tokens": 752,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 752
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

_source line 15 · 2026-05-20T04:40:30.070Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0129ojd1tBLp89LL1Q8KxSxT`</summary>

```json
{
  "query": "RATE causal explainability reward models imperfect counterfactuals ICML 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e4b3030-15a6-46fb-a444-b0b715790649",
  "isSidechain": false,
  "requestId": "req_011CbDCsZw7dPufvE4LDb9Fn",
  "type": "assistant",
  "uuid": "fddd6009-48ea-43ba-8f16-d99a084e7456",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DSbzcXZvK6LtrnuPLxsBCy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 752,
      "cache_read_input_tokens": 20452,
      "output_tokens": 297,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 752,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 297,
          "cache_read_input_tokens": 20452,
          "cache_creation_input_tokens": 752,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 752
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

_source line 16 · 2026-05-20T04:40:30.602Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Mm7FoziEfKSR8CinRY3igb`</summary>

```json
{
  "query": "SOS-Bench style over substance LLM judges ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fddd6009-48ea-43ba-8f16-d99a084e7456",
  "isSidechain": false,
  "requestId": "req_011CbDCsZw7dPufvE4LDb9Fn",
  "type": "assistant",
  "uuid": "5d57a6d8-0e59-44e5-9567-5958f0b9017d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DSbzcXZvK6LtrnuPLxsBCy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 752,
      "cache_read_input_tokens": 20452,
      "output_tokens": 297,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 752,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 297,
          "cache_read_input_tokens": 20452,
          "cache_creation_input_tokens": 752,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 752
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

_source line 17 · 2026-05-20T04:40:31.292Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CL5uJ17mDpjLSgyYbMK3wD`</summary>

```json
{
  "query": "Double Machine Learning text causal inference style treatment 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d57a6d8-0e59-44e5-9567-5958f0b9017d",
  "isSidechain": false,
  "requestId": "req_011CbDCsZw7dPufvE4LDb9Fn",
  "type": "assistant",
  "uuid": "7a8cb3a5-5d5f-4806-a5e1-0048740ab96d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DSbzcXZvK6LtrnuPLxsBCy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 752,
      "cache_read_input_tokens": 20452,
      "output_tokens": 297,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 752,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 297,
          "cache_read_input_tokens": 20452,
          "cache_creation_input_tokens": 752,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 752
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

_source line 18 · 2026-05-20T04:40:35.102Z_

<details><summary>↩ Tool result · `toolu_0129ojd1tBLp89LL1Q8KxSxT`</summary>

```text
Web search results for query: "RATE causal explainability reward models imperfect counterfactuals ICML 2025"

Links: [{"title":"RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals | OpenReview","url":"https://openreview.net/forum?id=rL3uxe5a0c"},{"title":"[2410.11348] RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals","url":"https://arxiv.org/abs/2410.11348"},{"title":"RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals","url":"https://arxiv.org/pdf/2410.11348"},{"title":"RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals","url":"https://proceedings.mlr.press/v267/reber25a.html"},{"title":"RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals","url":"https://arxiv.org/html/2410.11348"},{"title":"ICML Poster RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals","url":"https://icml.cc/virtual/2025/poster/43898"}]

I found the research paper! Here's what the search reveals about RATE:

## RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals

RATE (Rewrite-based Attribute Treatment Estimator) is an effective method for measuring the sensitivity of a reward model to high-level attributes of responses, such as sentiment, helpfulness, or complexity, and measures the causal effect of an attribute on the reward.

**The Core Problem:**
Reward models are widely used as proxies for human preferences when aligning or evaluating LLMs, however reward models are black boxes, and it is often unclear what they are actually rewarding.

**How RATE Works:**
RATE uses LLMs to rewrite responses to produce imperfect counterfactual examples that can be used to measure causal effects. A key challenge is that these rewrites are imperfect in a manner that can induce substantial bias, and the core idea of RATE is to adjust for this imperfect-rewrite effect by rewriting twice.

**Publication:**
The paper was published in the Proceedings of the 42nd International Conference on Machine Learning (ICML 2025). The authors are David Reber, Sean M. Richardson, Todd Nief, Cristina Garbacea, and Victor Veitch.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fddd6009-48ea-43ba-8f16-d99a084e7456",
  "isSidechain": false,
  "promptId": "7f63e8fc-85c3-4e6d-bc0e-cacc7b545dea",
  "type": "user",
  "uuid": "957d8af5-2ab8-4f0f-94ad-f699a28cfba7",
  "toolUseResult": {
    "query": "RATE causal explainability reward models imperfect counterfactuals ICML 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DQBMgkoGNpvCVLKSCPPwCa",
        "content": [
          {
            "title": "RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals | OpenReview",
            "url": "https://openreview.net/forum?id=rL3uxe5a0c"
          },
          {
            "title": "[2410.11348] RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals",
            "url": "https://arxiv.org/abs/2410.11348"
          },
          {
            "title": "RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals",
            "url": "https://arxiv.org/pdf/2410.11348"
          },
          {
            "title": "RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals",
            "url": "https://proceedings.mlr.press/v267/reber25a.html"
          },
          {
            "title": "RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals",
            "url": "https://arxiv.org/html/2410.11348"
          },
          {
            "title": "ICML Poster RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals",
            "url": "https://icml.cc/virtual/2025/poster/43898"
          }
        ]
      },
      "I found the research paper! Here's what the search reveals about RATE:\n\n## RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals\n\nRATE (Rewrite-based Attribute Treatment Estimator) is an effective method for measuring the sensitivity of a reward model to high-level attributes of responses, such as sentiment, helpfulness, or complexity, and measures the causal effect of an attribute on the reward.\n\n**The Core Problem:**\nReward models are widely used as proxies for human preferences when aligning or evaluating LLMs, however reward models are black boxes, and it is often unclear what they are actually rewarding.\n\n**How RATE Works:**\nRATE uses LLMs to rewrite responses to produce imperfect counterfactual examples that can be used to measure causal effects. A key challenge is that these rewrites are imperfect in a manner that can induce substantial bias, and the core idea of RATE is to adjust for this imperfect-rewrite effect by rewriting twice.\n\n**Publication:**\nThe paper was published in the Proceedings of the 42nd International Conference on Machine Learning (ICML 2025). The authors are David Reber, Sean M. Richardson, Todd Nief, Cristina Garbacea, and Victor Veitch."
    ],
    "durationSeconds": 5.029139076000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fddd6009-48ea-43ba-8f16-d99a084e7456",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T04:40:35.852Z_

<details><summary>↩ Tool result · `toolu_013JDmhByeHtenGeDvCpFYqc`</summary>

```text
Web search results for query: "FairJudge LLM debiasing arXiv 2602.06625 2026"

Links: [{"title":"[2602.06625] FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge","url":"https://arxiv.org/abs/2602.06625"},{"title":"FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge","url":"https://arxiv.org/pdf/2602.06625"},{"title":"FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge","url":"https://arxiv.org/html/2602.06625"},{"title":"FairJudge: MLLM Judging for Social-Attributes and Prompt–Image Alignment","url":"https://arxiv.org/html/2510.22827v1/"},{"title":"Debiasing LLMs by Masking Unfairness-Driving Attention Heads","url":"https://arxiv.org/pdf/2510.10142"}]

I found the paper you're looking for. Here's the information about FairJudge:

FairJudge is an adaptive, debiased, and consistent LLM-as-a-Judge that addresses key limitations in existing LLM-based evaluation systems. Existing LLM-as-a-Judge systems suffer from limited adaptivity to task- and domain-specific evaluation criteria, systematic biases driven by non-semantic cues such as position, length, format, and model provenance, and evaluation inconsistency that leads to contradictory judgments across different evaluation modes.

Unlike prior approaches that treat the judge as a static evaluator, FairJudge models judging behavior itself as a learnable and regularized policy. The approach constructs a high-information-density judging dataset that explicitly injects supervision signals aligned with evaluation behavior, and adopts a curriculum-style SFT-DPO-GRPO training paradigm that progressively aligns rubric adherence, bias mitigation, and cross-mode consistency.

Experimental results on multiple internal and public benchmarks show that FairJudge consistently improves agreement and F1, reduces non-semantic biases, and outperforms substantially larger instruction-tuned LLMs.

The paper was published on February 6, 2026, and is available at arXiv:2602.06625.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e4b3030-15a6-46fb-a444-b0b715790649",
  "isSidechain": false,
  "promptId": "7f63e8fc-85c3-4e6d-bc0e-cacc7b545dea",
  "type": "user",
  "uuid": "2d073d9a-90dc-4dac-a92e-74b2a40649e7",
  "toolUseResult": {
    "query": "FairJudge LLM debiasing arXiv 2602.06625 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01E6M5SeSXoMNfQw91XE4fMc",
        "content": [
          {
            "title": "[2602.06625] FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge",
            "url": "https://arxiv.org/abs/2602.06625"
          },
          {
            "title": "FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge",
            "url": "https://arxiv.org/pdf/2602.06625"
          },
          {
            "title": "FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge",
            "url": "https://arxiv.org/html/2602.06625"
          },
          {
            "title": "FairJudge: MLLM Judging for Social-Attributes and Prompt–Image Alignment",
            "url": "https://arxiv.org/html/2510.22827v1/"
          },
          {
            "title": "Debiasing LLMs by Masking Unfairness-Driving Attention Heads",
            "url": "https://arxiv.org/pdf/2510.10142"
          }
        ]
      },
      "I found the paper you're looking for. Here's the information about FairJudge:\n\nFairJudge is an adaptive, debiased, and consistent LLM-as-a-Judge that addresses key limitations in existing LLM-based evaluation systems. Existing LLM-as-a-Judge systems suffer from limited adaptivity to task- and domain-specific evaluation criteria, systematic biases driven by non-semantic cues such as position, length, format, and model provenance, and evaluation inconsistency that leads to contradictory judgments across different evaluation modes.\n\nUnlike prior approaches that treat the judge as a static evaluator, FairJudge models judging behavior itself as a learnable and regularized policy. The approach constructs a high-information-density judging dataset that explicitly injects supervision signals aligned with evaluation behavior, and adopts a curriculum-style SFT-DPO-GRPO training paradigm that progressively aligns rubric adherence, bias mitigation, and cross-mode consistency.\n\nExperimental results on multiple internal and public benchmarks show that FairJudge consistently improves agreement and F1, reduces non-semantic biases, and outperforms substantially larger instruction-tuned LLMs.\n\nThe paper was published on February 6, 2026, and is available at arXiv:2602.06625."
    ],
    "durationSeconds": 6.771890173,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0e4b3030-15a6-46fb-a444-b0b715790649",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T04:40:36.884Z_

<details><summary>↩ Tool result · `toolu_01BoneuXka1XvjfsheH6b3aM`</summary>

```text
Web search results for query: "LLM judge style bias debiasing causal 2025 2026"

Links: [{"title":"Any Large Language Model Can Be a Reliable Judge: Debiasing with a Reasoning-based Bias Detector | OpenReview","url":"https://openreview.net/forum?id=sLNz60fJFF"},{"title":"[2604.23178] Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines","url":"https://arxiv.org/abs/2604.23178"},{"title":"LLM-as-a-Judge: Why Frontier Models Fail 50%+ Bias Tests | Adaline","url":"https://www.adaline.ai/blog/llm-as-a-judge-reliability-bias"},{"title":"The Silent Judge: Unacknowledged Shortcut Bias in LLM-as-a-Judge","url":"https://arxiv.org/pdf/2509.26072"},{"title":"LLM-Based Judge Model","url":"https://www.emergentmind.com/topics/llm-based-judge-model"},{"title":"Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines","url":"https://arxiv.org/html/2604.23178v1"},{"title":"Mitigating the Bias of Large Language Model Evaluation","url":"https://arxiv.org/pdf/2409.16788"},{"title":"Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge","url":"https://arxiv.org/html/2406.07791v9"},{"title":"Causal-Guided Active Learning for Debiasing Large Language Models","url":"https://arxiv.org/pdf/2408.12942"}]

Based on the search results, here's what recent research reveals about LLM judge bias, debiasing strategies, and causal approaches in 2025-2026:

## Key Findings on LLM Judge Bias

LLM-as-a-Judge has become the dominant paradigm for evaluating language model outputs, yet LLM judges exhibit systematic biases that compromise evaluation reliability. Studies published in 2025 and early 2026 have systematically documented where LLM judges fail, why they fail, and how often.

**Style Bias Dominates:** Style bias is the dominant bias (0.76–0.92 across all models), far exceeding position bias, yet has received minimal research attention. Models exhibit a strong recency bias, systematically favoring "new" responses over "old", as well as a clear provenance hierarchy (EXPERT > HUMAN > LLM > UNKNOWN).

## Debiasing Strategies

Recent research explores multiple mitigation approaches. RBD is a plug-in module that detects and corrects biased LLM evaluations through structured reasoning, significantly improving accuracy, consistency, and scalability across multiple bias types and evaluator models. Comprehensive studies compare nine debiasing strategies across five judge models from four provider families (Google, Anthropic, OpenAI, Meta) across three benchmarks and four bias types.

Current debiasing strategies (prompt augmentation, ensembling, counterfactual audits) are necessary but insufficient, particularly for domain- and language-general evaluation.

## Causal and Mechanistic Approaches

Mechanistic approaches have been explored to address position bias by modifying model internals like positional embeddings and causal attention mechanisms. Additionally, causal origins of scoring bias remain an open problem.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a6c1ff7-9970-45d2-94fb-93c38cf208d5",
  "isSidechain": false,
  "promptId": "7f63e8fc-85c3-4e6d-bc0e-cacc7b545dea",
  "type": "user",
  "uuid": "feb26a7f-e226-49c3-bb51-070af712a5e9",
  "toolUseResult": {
    "query": "LLM judge style bias debiasing causal 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BZmcFxX896sgDcpUJjdZw5",
        "content": [
          {
            "title": "Any Large Language Model Can Be a Reliable Judge: Debiasing with a Reasoning-based Bias Detector | OpenReview",
            "url": "https://openreview.net/forum?id=sLNz60fJFF"
          },
          {
            "title": "[2604.23178] Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines",
            "url": "https://arxiv.org/abs/2604.23178"
          },
          {
            "title": "LLM-as-a-Judge: Why Frontier Models Fail 50%+ Bias Tests | Adaline",
            "url": "https://www.adaline.ai/blog/llm-as-a-judge-reliability-bias"
          },
          {
            "title": "The Silent Judge: Unacknowledged Shortcut Bias in LLM-as-a-Judge",
            "url": "https://arxiv.org/pdf/2509.26072"
          },
          {
            "title": "LLM-Based Judge Model",
            "url": "https://www.emergentmind.com/topics/llm-based-judge-model"
          },
          {
            "title": "Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines",
            "url": "https://arxiv.org/html/2604.23178v1"
          },
          {
            "title": "Mitigating the Bias of Large Language Model Evaluation",
            "url": "https://arxiv.org/pdf/2409.16788"
          },
          {
            "title": "Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge",
            "url": "https://arxiv.org/html/2406.07791v9"
          },
          {
            "title": "Causal-Guided Active Learning for Debiasing Large Language Models",
            "url": "https://arxiv.org/pdf/2408.12942"
          }
        ]
      },
      "Based on the search results, here's what recent research reveals about LLM judge bias, debiasing strategies, and causal approaches in 2025-2026:\n\n## Key Findings on LLM Judge Bias\n\nLLM-as-a-Judge has become the dominant paradigm for evaluating language model outputs, yet LLM judges exhibit systematic biases that compromise evaluation reliability. Studies published in 2025 and early 2026 have systematically documented where LLM judges fail, why they fail, and how often.\n\n**Style Bias Dominates:** Style bias is the dominant bias (0.76–0.92 across all models), far exceeding position bias, yet has received minimal research attention. Models exhibit a strong recency bias, systematically favoring \"new\" responses over \"old\", as well as a clear provenance hierarchy (EXPERT > HUMAN > LLM > UNKNOWN).\n\n## Debiasing Strategies\n\nRecent research explores multiple mitigation approaches. RBD is a plug-in module that detects and corrects biased LLM evaluations through structured reasoning, significantly improving accuracy, consistency, and scalability across multiple bias types and evaluator models. Comprehensive studies compare nine debiasing strategies across five judge models from four provider families (Google, Anthropic, OpenAI, Meta) across three benchmarks and four bias types.\n\nCurrent debiasing strategies (prompt augmentation, ensembling, counterfactual audits) are necessary but insufficient, particularly for domain- and language-general evaluation.\n\n## Causal and Mechanistic Approaches\n\nMechanistic approaches have been explored to address position bias by modifying model internals like positional embeddings and causal attention mechanisms. Additionally, causal origins of scoring bias remain an open problem."
    ],
    "durationSeconds": 8.750668777000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6a6c1ff7-9970-45d2-94fb-93c38cf208d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-20T04:40:38.122Z_

<details><summary>↩ Tool result · `toolu_01Mm7FoziEfKSR8CinRY3igb`</summary>

```text
Web search results for query: "SOS-Bench style over substance LLM judges ICLR 2025"

Links: [{"title":"[Literature Review] Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking","url":"https://www.themoonlight.io/en/review/style-outweighs-substance-failure-modes-of-llm-judges-in-alignment-benchmarking"},{"title":"(PDF) Style over Substance: Failure Modes of LLM Judges in Alignment Benchmarking","url":"https://www.researchgate.net/publication/384288829_Style_over_Substance_Failure_Modes_of_LLM_Judges_in_Alignment_Benchmarking"},{"title":"ICLR Poster Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking","url":"https://iclr.cc/virtual/2025/poster/29906"},{"title":"[Quick Review] Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking","url":"https://liner.com/review/style-outweighs-substance-failure-modes-of-llm-judges-in-alignment"},{"title":"Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking | OpenReview","url":"https://openreview.net/forum?id=MzHNftnAM1"},{"title":"Style Outweighs Substance: Failure Modes of LLM Judges in Alignment   Benchmarking","url":"https://arxiv.org/pdf/2409.15268"},{"title":"Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking","url":"https://arxiv.org/html/2409.15268v3"},{"title":"[2409.15268] Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking","url":"https://arxiv.org/abs/2409.15268"},{"title":"Style over Substance: Failure Modes of LLM Judges in Alignment Benchmarking","url":"https://arxiv.org/html/2409.15268v1"},{"title":"Paper page - Style over Substance: Failure Modes of LLM Judges in Alignment Benchmarking","url":"https://huggingface.co/papers/2409.15268"}]

Based on the search results, here's what I found about the SOS-Bench paper:

## Overview

The paper "Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking" was presented at ICLR 2025, and was written by Benjamin Feuer et al.

## Key Findings

The research found that (1) LLM-judge preferences do not correlate with concrete measures of safety, world knowledge, and instruction following; (2) LLM-judges have powerful implicit biases, prioritizing style over factuality and safety; and (3) the supervised fine-tuning (SFT) stage of post-training has a large impact on alignment, with data scaling and prompt diversity as the driving factors.

## The SOS-Bench Benchmark

SOS-Bench (Substance Outweighs Style Benchmark) is the largest standardized, reproducible LLM meta-benchmark to date. SOS-Bench combines 19 existing world knowledge, instruction following, and safety benchmarks for a holistic view of model performance. The benchmark tests models on 152,380 data points, which is almost 7x larger than the largest previous open source LLM benchmark.

## Implications

Sarcasm, a minor violation of helpfulness, resulted in a 96% loss, while incorrect answers, a strong violation of honesty, only caused a 13% loss, suggesting that LLM judges' implicit biases do not accurately reflect priorities in model alignment.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d57a6d8-0e59-44e5-9567-5958f0b9017d",
  "isSidechain": false,
  "promptId": "7f63e8fc-85c3-4e6d-bc0e-cacc7b545dea",
  "type": "user",
  "uuid": "dca68cc7-20d9-4ba4-aac2-3c7195e7f5dc",
  "toolUseResult": {
    "query": "SOS-Bench style over substance LLM judges ICLR 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_015mzSTKmZXhe8EFxgbeLfr6",
        "content": [
          {
            "title": "[Literature Review] Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking",
            "url": "https://www.themoonlight.io/en/review/style-outweighs-substance-failure-modes-of-llm-judges-in-alignment-benchmarking"
          },
          {
            "title": "(PDF) Style over Substance: Failure Modes of LLM Judges in Alignment Benchmarking",
            "url": "https://www.researchgate.net/publication/384288829_Style_over_Substance_Failure_Modes_of_LLM_Judges_in_Alignment_Benchmarking"
          },
          {
            "title": "ICLR Poster Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking",
            "url": "https://iclr.cc/virtual/2025/poster/29906"
          },
          {
            "title": "[Quick Review] Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking",
            "url": "https://liner.com/review/style-outweighs-substance-failure-modes-of-llm-judges-in-alignment"
          },
          {
            "title": "Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking | OpenReview",
            "url": "https://openreview.net/forum?id=MzHNftnAM1"
          },
          {
            "title": "Style Outweighs Substance: Failure Modes of LLM Judges in Alignment   Benchmarking",
            "url": "https://arxiv.org/pdf/2409.15268"
          },
          {
            "title": "Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking",
            "url": "https://arxiv.org/html/2409.15268v3"
          },
          {
            "title": "[2409.15268] Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking",
            "url": "https://arxiv.org/abs/2409.15268"
          },
          {
            "title": "Style over Substance: Failure Modes of LLM Judges in Alignment Benchmarking",
            "url": "https://arxiv.org/html/2409.15268v1"
          },
          {
            "title": "Paper page - Style over Substance: Failure Modes of LLM Judges in Alignment Benchmarking",
            "url": "https://huggingface.co/papers/2409.15268"
          }
        ]
      },
      "Based on the search results, here's what I found about the SOS-Bench paper:\n\n## Overview\n\nThe paper \"Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking\" was presented at ICLR 2025, and was written by Benjamin Feuer et al.\n\n## Key Findings\n\nThe research found that (1) LLM-judge preferences do not correlate with concrete measures of safety, world knowledge, and instruction following; (2) LLM-judges have powerful implicit biases, prioritizing style over factuality and safety; and (3) the supervised fine-tuning (SFT) stage of post-training has a large impact on alignment, with data scaling and prompt diversity as the driving factors.\n\n## The SOS-Bench Benchmark\n\nSOS-Bench (Substance Outweighs Style Benchmark) is the largest standardized, reproducible LLM meta-benchmark to date. SOS-Bench combines 19 existing world knowledge, instruction following, and safety benchmarks for a holistic view of model performance. The benchmark tests models on 152,380 data points, which is almost 7x larger than the largest previous open source LLM benchmark.\n\n## Implications\n\nSarcasm, a minor violation of helpfulness, resulted in a 96% loss, while incorrect answers, a strong violation of honesty, only caused a 13% loss, suggesting that LLM judges' implicit biases do not accurately reflect priorities in model alignment."
    ],
    "durationSeconds": 7.518054183,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5d57a6d8-0e59-44e5-9567-5958f0b9017d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Causal Style Decomposition for LLM Judge Debiasing via Doubly-Robust Counterfactual Estimation  ## Description S…",
  "leafUuid": "dca68cc7-20d9-4ba4-aac2-3c7195e7f5dc",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate LLM judge style bias debiasing proposal",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a"
}
```

---

### Tool result

_source line 24 · 2026-05-20T04:40:38.383Z_

<details><summary>↩ Tool result · `toolu_01CL5uJ17mDpjLSgyYbMK3wD`</summary>

```text
Web search results for query: "Double Machine Learning text causal inference style treatment 2025 2026"

Links: [{"title":"Introduction to Causal Inference: Double Machine Learning | Carlos Mendez","url":"https://carlos-mendez.org/post/python_doubleml/"},{"title":"[2511.12640] Double machine learning for causal inference in a multivariate sample selection model","url":"https://arxiv.org/abs/2511.12640"},{"title":"Double machine learning for static panel models with fixed effects | The Econometrics Journal | Oxford Academic","url":"https://academic.oup.com/ectj/article/29/1/69/8120202"},{"title":"[2505.12617] Double machine learning to estimate the effects of multiple treatments and their interactions","url":"https://arxiv.org/abs/2505.12617"},{"title":"Double machine learning for causal inference in a multivariate sample selection model","url":"https://arxiv.org/pdf/2511.12640"},{"title":"Full article: Double Debiased Machine Learning Nonparametric Inference with Continuous Treatments","url":"https://www.tandfonline.com/doi/full/10.1080/07350015.2025.2505487"},{"title":"(PDF) Double machine learning for causal inference in a multivariate sample selection model","url":"https://www.researchgate.net/publication/397700429_Double_machine_learning_for_causal_inference_in_a_multivariate_sample_selection_model"},{"title":"Double Machine Learning for Causal Inference under Shared-State   Interference","url":"https://arxiv.org/pdf/2504.08836"},{"title":"“Double Machine Learning for Causal Inference in High-Dimensional Electronic Health Records” | medRxiv","url":"https://www.medrxiv.org/content/10.1101/2025.07.21.25331944v1"}]

Based on the search results, here's what I found about Double Machine Learning (DML) for causal inference and treatment effects in 2025-2026:

## Overview

Double Machine Learning (DML) addresses causal inference by using flexible machine learning models to partial out the confounding variation, then estimating the causal effect on the cleaned residuals.

## Recent Applications and Extensions (2025-2026)

Several recent papers demonstrate active development in this area:

1. **Panel Data with Fixed Effects**: Novel double machine learning procedures for panel data have been developed in which algorithms are used to approximate high-dimensional and non-linear nuisance functions of the covariates.

2. **Multiple Treatments**: Methods have been applied to study the effect of three treatments on HIV-associated kidney disease in an adult HIV cohort of 2455 participants in Nigeria.

3. **Sample Selection Models**: DML estimators of average treatment effect (ATE), average treatment effect on the treated (ATET) and local average treatment effect (LATE) have been proposed in the multivariate sample selection model with ordinal selection equations.

4. **Continuous Treatments**: Nonparametric inference methods for continuous treatment effects have been proposed using double debiased ML approaches that combine doubly robust moment functions and cross-fitting.

5. **Health Data Applications**: Double machine learning based methods consistently outperform IPTW regarding bias and empirical standard error, particularly in large sample sizes and sparse-data scenarios.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a8cb3a5-5d5f-4806-a5e1-0048740ab96d",
  "isSidechain": false,
  "promptId": "7f63e8fc-85c3-4e6d-bc0e-cacc7b545dea",
  "type": "user",
  "uuid": "135e4c3e-4379-4682-954e-1f4075ba6a9a",
  "toolUseResult": {
    "query": "Double Machine Learning text causal inference style treatment 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01T99m5zSxGBvyCTMsMVnf1v",
        "content": [
          {
            "title": "Introduction to Causal Inference: Double Machine Learning | Carlos Mendez",
            "url": "https://carlos-mendez.org/post/python_doubleml/"
          },
          {
            "title": "[2511.12640] Double machine learning for causal inference in a multivariate sample selection model",
            "url": "https://arxiv.org/abs/2511.12640"
          },
          {
            "title": "Double machine learning for static panel models with fixed effects | The Econometrics Journal | Oxford Academic",
            "url": "https://academic.oup.com/ectj/article/29/1/69/8120202"
          },
          {
            "title": "[2505.12617] Double machine learning to estimate the effects of multiple treatments and their interactions",
            "url": "https://arxiv.org/abs/2505.12617"
          },
          {
            "title": "Double machine learning for causal inference in a multivariate sample selection model",
            "url": "https://arxiv.org/pdf/2511.12640"
          },
          {
            "title": "Full article: Double Debiased Machine Learning Nonparametric Inference with Continuous Treatments",
            "url": "https://www.tandfonline.com/doi/full/10.1080/07350015.2025.2505487"
          },
          {
            "title": "(PDF) Double machine learning for causal inference in a multivariate sample selection model",
            "url": "https://www.researchgate.net/publication/397700429_Double_machine_learning_for_causal_inference_in_a_multivariate_sample_selection_model"
          },
          {
            "title": "Double Machine Learning for Causal Inference under Shared-State   Interference",
            "url": "https://arxiv.org/pdf/2504.08836"
          },
          {
            "title": "“Double Machine Learning for Causal Inference in High-Dimensional Electronic Health Records” | medRxiv",
            "url": "https://www.medrxiv.org/content/10.1101/2025.07.21.25331944v1"
          }
        ]
      },
      "Based on the search results, here's what I found about Double Machine Learning (DML) for causal inference and treatment effects in 2025-2026:\n\n## Overview\n\nDouble Machine Learning (DML) addresses causal inference by using flexible machine learning models to partial out the confounding variation, then estimating the causal effect on the cleaned residuals.\n\n## Recent Applications and Extensions (2025-2026)\n\nSeveral recent papers demonstrate active development in this area:\n\n1. **Panel Data with Fixed Effects**: Novel double machine learning procedures for panel data have been developed in which algorithms are used to approximate high-dimensional and non-linear nuisance functions of the covariates.\n\n2. **Multiple Treatments**: Methods have been applied to study the effect of three treatments on HIV-associated kidney disease in an adult HIV cohort of 2455 participants in Nigeria.\n\n3. **Sample Selection Models**: DML estimators of average treatment effect (ATE), average treatment effect on the treated (ATET) and local average treatment effect (LATE) have been proposed in the multivariate sample selection model with ordinal selection equations.\n\n4. **Continuous Treatments**: Nonparametric inference methods for continuous treatment effects have been proposed using double debiased ML approaches that combine doubly robust moment functions and cross-fitting.\n\n5. **Health Data Applications**: Double machine learning based methods consistently outperform IPTW regarding bias and empirical standard error, particularly in large sample sizes and sparse-data scenarios."
    ],
    "durationSeconds": 7.0886974449999975,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7a8cb3a5-5d5f-4806-a5e1-0048740ab96d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T04:40:44.562Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HRngFe5p9MzfaVp1KSv9kb`</summary>

```json
{
  "query": "Length-Controlled AlpacaEval post-hoc debiasing regression ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "135e4c3e-4379-4682-954e-1f4075ba6a9a",
  "isSidechain": false,
  "requestId": "req_011CbDCtqfgyJvcz7KmRnTiF",
  "type": "assistant",
  "uuid": "3dfd176d-b84d-45a5-9324-c4dd03b2c809",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KAX2QCQxur1GeePVTW9bZB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4344,
      "cache_read_input_tokens": 21204,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4344,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 182,
          "cache_read_input_tokens": 21204,
          "cache_creation_input_tokens": 4344,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4344
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

_source line 26 · 2026-05-20T04:40:45.498Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FducNKmDDsc7SXoFFZBdue`</summary>

```json
{
  "query": "Bias-Bounded Evaluation LLM judge differential privacy debiasing 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3dfd176d-b84d-45a5-9324-c4dd03b2c809",
  "isSidechain": false,
  "requestId": "req_011CbDCtqfgyJvcz7KmRnTiF",
  "type": "assistant",
  "uuid": "9d24dab4-b2c8-42b9-820b-96bd727f8fc4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KAX2QCQxur1GeePVTW9bZB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4344,
      "cache_read_input_tokens": 21204,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4344,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 182,
          "cache_read_input_tokens": 21204,
          "cache_creation_input_tokens": 4344,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4344
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

_source line 27 · 2026-05-20T04:40:46.349Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XDhd2eVpbFPCnLSAvT6PZV`</summary>

```json
{
  "query": "CASSE concise agent style features side effects 2601.10809 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d24dab4-b2c8-42b9-820b-96bd727f8fc4",
  "isSidechain": false,
  "requestId": "req_011CbDCtqfgyJvcz7KmRnTiF",
  "type": "assistant",
  "uuid": "dd97e029-6ab7-45c0-8cf3-cfd5371f4d26",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KAX2QCQxur1GeePVTW9bZB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4344,
      "cache_read_input_tokens": 21204,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4344,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 182,
          "cache_read_input_tokens": 21204,
          "cache_creation_input_tokens": 4344,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4344
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

_source line 28 · 2026-05-20T04:40:51.349Z_

<details><summary>↩ Tool result · `toolu_01HRngFe5p9MzfaVp1KSv9kb`</summary>

```text
Web search results for query: "Length-Controlled AlpacaEval post-hoc debiasing regression ICLR 2025"

Links: [{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2410.04203"},{"title":"Length-Controlled AlpacaEval: A Simple Way to Debias Automatic   Evaluators","url":"https://arxiv.org/pdf/2404.04475"},{"title":"Post-Hoc Reward Calibration: A Case Study on Length Bias","url":"https://iclr.cc/media/iclr-2025/Slides/30144.pdf"},{"title":"Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators","url":"https://arxiv.org/html/2404.04475v2"},{"title":"Length-Controlled AlpacaEval: A Simple Debiasing of Automatic Evaluators | OpenReview","url":"https://openreview.net/forum?id=CybBmzWBX0"},{"title":"[2404.04475] Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators","url":"https://arxiv.org/abs/2404.04475"},{"title":"Published as a conference paper at ICLR 2025","url":"https://openreview.net/pdf?id=BPgK5XW1Nb"},{"title":"AlpacaEval 2.0: Scalable LLM Evaluation","url":"https://www.emergentmind.com/topics/alpacaeval-2-0"}]

Based on the search results, here's what I found about Length-Controlled AlpacaEval post-hoc debiasing regression at ICLR 2025:

## Overview

The approach proposes a simple, interpretable debiasing strategy for automated evaluation metrics based on regression-based adjustments for observational causal inference, viewing spurious correlates such as length as undesirable mediators in a causal graph.

## The Problem Being Addressed

One of the major issues of AlpacaEval is that one can increase the win-rate by increasing the length of outputs.

## Technical Approach

For each model, AlpacaEval2 fits a logistic regression to predict the preference of the autoannotator given the instruction, the model, and the difference of length between the baseline and model output. This regression can then predict the counterfactual "what would the preference be if the model's output had the same length as the baseline" by setting the length difference to 0, and by averaging over this length-controlled preference, AlpacaEval2 obtains the LC win rates.

## Results

Length controlled win-rates increase the correlation between AlpacaEval's leaderboard and Chat Arena from 0.93 to 0.98 Spearman correlation, while significantly decreasing the length gameability.

The work was published as a conference paper at ICLR 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3dfd176d-b84d-45a5-9324-c4dd03b2c809",
  "isSidechain": false,
  "promptId": "7f63e8fc-85c3-4e6d-bc0e-cacc7b545dea",
  "type": "user",
  "uuid": "da422514-7a9c-45d1-995b-756764a1a2dd",
  "toolUseResult": {
    "query": "Length-Controlled AlpacaEval post-hoc debiasing regression ICLR 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_017cUfiHwLetoZ2rgjdHcsT6",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://arxiv.org/pdf/2410.04203"
          },
          {
            "title": "Length-Controlled AlpacaEval: A Simple Way to Debias Automatic   Evaluators",
            "url": "https://arxiv.org/pdf/2404.04475"
          },
          {
            "title": "Post-Hoc Reward Calibration: A Case Study on Length Bias",
            "url": "https://iclr.cc/media/iclr-2025/Slides/30144.pdf"
          },
          {
            "title": "Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators",
            "url": "https://arxiv.org/html/2404.04475v2"
          },
          {
            "title": "Length-Controlled AlpacaEval: A Simple Debiasing of Automatic Evaluators | OpenReview",
            "url": "https://openreview.net/forum?id=CybBmzWBX0"
          },
          {
            "title": "[2404.04475] Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators",
            "url": "https://arxiv.org/abs/2404.04475"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://openreview.net/pdf?id=BPgK5XW1Nb"
          },
          {
            "title": "AlpacaEval 2.0: Scalable LLM Evaluation",
            "url": "https://www.emergentmind.com/topics/alpacaeval-2-0"
          }
        ]
      },
      "Based on the search results, here's what I found about Length-Controlled AlpacaEval post-hoc debiasing regression at ICLR 2025:\n\n## Overview\n\nThe approach proposes a simple, interpretable debiasing strategy for automated evaluation metrics based on regression-based adjustments for observational causal inference, viewing spurious correlates such as length as undesirable mediators in a causal graph.\n\n## The Problem Being Addressed\n\nOne of the major issues of AlpacaEval is that one can increase the win-rate by increasing the length of outputs.\n\n## Technical Approach\n\nFor each model, AlpacaEval2 fits a logistic regression to predict the preference of the autoannotator given the instruction, the model, and the difference of length between the baseline and model output. This regression can then predict the counterfactual \"what would the preference be if the model's output had the same length as the baseline\" by setting the length difference to 0, and by averaging over this length-controlled preference, AlpacaEval2 obtains the LC win rates.\n\n## Results\n\nLength controlled win-rates increase the correlation between AlpacaEval's leaderboard and Chat Arena from 0.93 to 0.98 Spearman correlation, while significantly decreasing the length gameability.\n\nThe work was published as a conference paper at ICLR 2025."
    ],
    "durationSeconds": 6.782455766999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3dfd176d-b84d-45a5-9324-c4dd03b2c809",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-20T04:40:52.528Z_

<details><summary>↩ Tool result · `toolu_01XDhd2eVpbFPCnLSAvT6PZV`</summary>

```text
Web search results for query: "CASSE concise agent style features side effects 2601.10809 2026"

Links: [{"title":"[2601.10809] A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents","url":"https://arxiv.org/abs/2601.10809"},{"title":"A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents","url":"https://www.catalyzex.com/paper/a-concise-agent-is-less-expert-revealing-side"},{"title":"A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents","url":"https://arxiv.org/html/2601.10809"},{"title":"Mitigating Side Effects in Multi-Agent Systems Using Blame Assignment","url":"https://arxiv.org/pdf/2405.04702"},{"title":"Actin Dysregulation Mediates Nephrotoxicity of Cassiae Semen Aqueous Extracts","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11360101/"}]

Based on the search results, I found relevant information about the paper you're looking for:

CASSE (Conversational Agent Stylistic Side Effects) is a dataset capturing complex interactions of style features in conversational agents. The paper is titled "A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents".

The research studies how style features such as friendly, helpful, or concise—which are widely used in prompts to steer conversational agents—have unintended side effects. The researchers conducted a comprehensive survey of 127 conversational agent papers and identified 12 frequently used style features.

Key findings include: Prompting for conciseness significantly reduces perceived expertise, and style features are deeply entangled rather than orthogonal. The researchers evaluated prompt-based and activation steering mitigation strategies, finding that while they can partially restore suppressed traits, they often degrade the primary intended style.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd97e029-6ab7-45c0-8cf3-cfd5371f4d26",
  "isSidechain": false,
  "promptId": "7f63e8fc-85c3-4e6d-bc0e-cacc7b545dea",
  "type": "user",
  "uuid": "ebb52451-48a6-4f24-8ac1-3bd7597ea2d7",
  "toolUseResult": {
    "query": "CASSE concise agent style features side effects 2601.10809 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TEjKSKKuLBsAX8gfBshedN",
        "content": [
          {
            "title": "[2601.10809] A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents",
            "url": "https://arxiv.org/abs/2601.10809"
          },
          {
            "title": "A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents",
            "url": "https://www.catalyzex.com/paper/a-concise-agent-is-less-expert-revealing-side"
          },
          {
            "title": "A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents",
            "url": "https://arxiv.org/html/2601.10809"
          },
          {
            "title": "Mitigating Side Effects in Multi-Agent Systems Using Blame Assignment",
            "url": "https://arxiv.org/pdf/2405.04702"
          },
          {
            "title": "Actin Dysregulation Mediates Nephrotoxicity of Cassiae Semen Aqueous Extracts",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11360101/"
          }
        ]
      },
      "Based on the search results, I found relevant information about the paper you're looking for:\n\nCASSE (Conversational Agent Stylistic Side Effects) is a dataset capturing complex interactions of style features in conversational agents. The paper is titled \"A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents\".\n\nThe research studies how style features such as friendly, helpful, or concise—which are widely used in prompts to steer conversational agents—have unintended side effects. The researchers conducted a comprehensive survey of 127 conversational agent papers and identified 12 frequently used style features.\n\nKey findings include: Prompting for conciseness significantly reduces perceived expertise, and style features are deeply entangled rather than orthogonal. The researchers evaluated prompt-based and activation steering mitigation strategies, finding that while they can partially restore suppressed traits, they often degrade the primary intended style."
    ],
    "durationSeconds": 6.177173140999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "dd97e029-6ab7-45c0-8cf3-cfd5371f4d26",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T04:40:53.527Z_

<details><summary>↩ Tool result · `toolu_01FducNKmDDsc7SXoFFZBdue`</summary>

```text
Web search results for query: "Bias-Bounded Evaluation LLM judge differential privacy debiasing 2026"

Links: [{"title":"LLM Judges: A Bias-Bounded Evaluation Framework (CS 2026) - Studocu","url":"https://www.studocu.com/in/document/chirec-international-school/mathematics-applications-and-interpretation-sl/llm-judges-a-bias-bounded-evaluation-framework-cs-2026/155334241"},{"title":"Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation","url":"https://arxiv.org/html/2603.05485"},{"title":"GitHub - penfever/bias-bounded-evaluation: A Python implementation of differential privacy-inspired techniques for reducing implicit bias in LLM judge evaluations while providing formal guarantees. · GitHub","url":"https://github.com/penfever/bias-bounded-evaluation"},{"title":"[2603.05485] Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation","url":"https://arxiv.org/abs/2603.05485"},{"title":"Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation","url":"https://arxiv.org/pdf/2603.05485"},{"title":"Toward robust LLM-based judges: taxonomic bias evaluation and debiasing optimization","url":"https://arxiv.org/html/2603.08091"}]

Based on the search results, here's what I found about Bias-Bounded Evaluation for LLM judges with differential privacy-inspired debiasing:

## Overview

Bias-bounded evaluation (BBE) is a novel framework that measures how sensitive an LLM judge is to biases and then renders that sensitivity in the judgment scores.

## How It Works

Bias-bounded evaluation measures how sensitive a judge is to contextual perturbations, and then injects calibrated Gaussian noise to mitigate the effects of the bias. BBE injects calibrated Gaussian noise to the judge's scores to mitigate the effects of the bias, using a novel mechanism called average bias-boundedness (A-BB).

## Scope of Biases

Biases can be very simple (e.g. varying presentation order or format) or arbitrarily complex; the only limitation in this framework is that a bias must be subject to a valid and reliable measure, in the units of judgment, in order to be targeted.

## Research Context

The 2026 AAAI Conference added an LLM judge (AI-Powered Peer Review System) to the panel of reviewers for its scientific submissions. The approach uses differential privacy-inspired techniques for reducing implicit bias in LLM judge evaluations while providing formal guarantees.

## Implementation

The reference implementation of the bias-bounded evaluation pipeline combines classical differential-privacy style guarantees with practical tooling for measuring judge sensitivity, applying calibrated noise, and visualizing downstream impact.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d24dab4-b2c8-42b9-820b-96bd727f8fc4",
  "isSidechain": false,
  "promptId": "7f63e8fc-85c3-4e6d-bc0e-cacc7b545dea",
  "type": "user",
  "uuid": "e267d01b-ace3-4975-a50e-6e2d30bbf89b",
  "toolUseResult": {
    "query": "Bias-Bounded Evaluation LLM judge differential privacy debiasing 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KmYpXYaRXevppB63u6keqz",
        "content": [
          {
            "title": "LLM Judges: A Bias-Bounded Evaluation Framework (CS 2026) - Studocu",
            "url": "https://www.studocu.com/in/document/chirec-international-school/mathematics-applications-and-interpretation-sl/llm-judges-a-bias-bounded-evaluation-framework-cs-2026/155334241"
          },
          {
            "title": "Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation",
            "url": "https://arxiv.org/html/2603.05485"
          },
          {
            "title": "GitHub - penfever/bias-bounded-evaluation: A Python implementation of differential privacy-inspired techniques for reducing implicit bias in LLM judge evaluations while providing formal guarantees. · GitHub",
            "url": "https://github.com/penfever/bias-bounded-evaluation"
          },
          {
            "title": "[2603.05485] Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation",
            "url": "https://arxiv.org/abs/2603.05485"
          },
          {
            "title": "Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation",
            "url": "https://arxiv.org/pdf/2603.05485"
          },
          {
            "title": "Toward robust LLM-based judges: taxonomic bias evaluation and debiasing optimization",
            "url": "https://arxiv.org/html/2603.08091"
          }
        ]
      },
      "Based on the search results, here's what I found about Bias-Bounded Evaluation for LLM judges with differential privacy-inspired debiasing:\n\n## Overview\n\nBias-bounded evaluation (BBE) is a novel framework that measures how sensitive an LLM judge is to biases and then renders that sensitivity in the judgment scores.\n\n## How It Works\n\nBias-bounded evaluation measures how sensitive a judge is to contextual perturbations, and then injects calibrated Gaussian noise to mitigate the effects of the bias. BBE injects calibrated Gaussian noise to the judge's scores to mitigate the effects of the bias, using a novel mechanism called average bias-boundedness (A-BB).\n\n## Scope of Biases\n\nBiases can be very simple (e.g. varying presentation order or format) or arbitrarily complex; the only limitation in this framework is that a bias must be subject to a valid and reliable measure, in the units of judgment, in order to be targeted.\n\n## Research Context\n\nThe 2026 AAAI Conference added an LLM judge (AI-Powered Peer Review System) to the panel of reviewers for its scientific submissions. The approach uses differential privacy-inspired techniques for reducing implicit bias in LLM judge evaluations while providing formal guarantees.\n\n## Implementation\n\nThe reference implementation of the bias-bounded evaluation pipeline combines classical differential-privacy style guarantees with practical tooling for measuring judge sensitivity, applying calibrated noise, and visualizing downstream impact."
    ],
    "durationSeconds": 8.026143181,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9d24dab4-b2c8-42b9-820b-96bd727f8fc4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-20T04:40:53.532Z_

```json
{
  "parentUuid": "e267d01b-ace3-4975-a50e-6e2d30bbf89b",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "7d9d482b-f9d0-4390-953e-69fdc6a91fd3",
  "timestamp": "2026-05-20T04:40:53.532Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 32 · 2026-05-20T04:41:03.307Z_

<details><summary>Logged reasoning block</summary>

```text
Let me do a couple more searches to be thorough - particularly about whether anyone has already done causal style decomposition for LLM judge debiasing, and about the "Preference Leakage" paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d9d482b-f9d0-4390-953e-69fdc6a91fd3",
  "isSidechain": false,
  "requestId": "req_011CbDCuneQ2QATSLqnhyhTQ",
  "type": "assistant",
  "uuid": "c96009cf-1055-4680-875e-a31e49e3154c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J8aZtwrUnocXaQsykH7w8s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 537,
      "cache_creation_input_tokens": 1789,
      "cache_read_input_tokens": 25548,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1789,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 537,
          "output_tokens": 196,
          "cache_read_input_tokens": 25548,
          "cache_creation_input_tokens": 1789,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1789
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

_source line 33 · 2026-05-20T04:41:04.255Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AeuuJErqyyq3qqQ64btMfY`</summary>

```json
{
  "query": "counterfactual style rewriting LLM judge debiasing post-hoc model-agnostic 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c96009cf-1055-4680-875e-a31e49e3154c",
  "isSidechain": false,
  "requestId": "req_011CbDCuneQ2QATSLqnhyhTQ",
  "type": "assistant",
  "uuid": "88670fc5-971e-46bf-9c87-5a687f846505",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J8aZtwrUnocXaQsykH7w8s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 537,
      "cache_creation_input_tokens": 1789,
      "cache_read_input_tokens": 25548,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1789,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 537,
          "output_tokens": 196,
          "cache_read_input_tokens": 25548,
          "cache_creation_input_tokens": 1789,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1789
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

_source line 34 · 2026-05-20T04:41:04.448Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MgHAfuDhQ9mAGJhDdPQMpR`</summary>

```json
{
  "query": "\"Preference Leakage\" contamination LLM judge ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88670fc5-971e-46bf-9c87-5a687f846505",
  "isSidechain": false,
  "requestId": "req_011CbDCuneQ2QATSLqnhyhTQ",
  "type": "assistant",
  "uuid": "f76d4391-c65d-4ad2-8ebf-ec6f4a82a777",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J8aZtwrUnocXaQsykH7w8s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 537,
      "cache_creation_input_tokens": 1789,
      "cache_read_input_tokens": 25548,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1789,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 537,
          "output_tokens": 196,
          "cache_read_input_tokens": 25548,
          "cache_creation_input_tokens": 1789,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1789
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

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Causal Style Decomposition for LLM Judge Debiasing via Doubly-Robust Counterfactual Estimation  ## Description S…",
  "leafUuid": "f76d4391-c65d-4ad2-8ebf-ec6f4a82a777",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate LLM judge style bias debiasing proposal",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a"
}
```

---

### Tool result

_source line 37 · 2026-05-20T04:41:09.775Z_

<details><summary>↩ Tool result · `toolu_01MgHAfuDhQ9mAGJhDdPQMpR`</summary>

```text
Web search results for query: ""Preference Leakage" contamination LLM judge ICLR 2026"

Links: [{"title":"Preference Leakage: A Contamination Problem in LLM-as-a-judge | OpenReview","url":"https://openreview.net/forum?id=grIvSXVJ65"},{"title":"Preference Leakage: A Contamination Problem in LLM-as-a-judge [Quick Review]","url":"https://liner.com/review/preference-leakage-a-contamination-problem-in-llmasajudge"},{"title":"[Paper Note] Preference Leakage: A Contamination Problem in LLM-as-a-judge - 📚 AI Paper Notes","url":"https://en.papernotes.org/ICLR2026/llm_evaluation/preference_leakage_a_contamination_problem_in_llm-as-a-judge/"},{"title":"ICLR Poster Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://iclr.cc/virtual/2026/poster/10008112"},{"title":"LLM-as-a-judge","url":"https://llm-as-a-judge.github.io/"},{"title":"Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://arxiv.org/html/2502.01534v3"},{"title":"[2502.01534] Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://arxiv.org/abs/2502.01534"},{"title":"Preference Leakage: A Contamination Problem in LLM-as- ...","url":"https://arxiv.org/pdf/2502.01534"},{"title":"Paper page - Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://huggingface.co/papers/2502.01534"}]

Based on the search results, I found relevant information about this paper:

## Preference Leakage: A Contamination Problem in LLM-as-a-Judge

Preference leakage is a contamination problem in LLM-as-a-judge caused by the relatedness between the synthetic data generators and LLM-based evaluators.

**Key Context:**
Large Language Models (LLMs) as judges and LLM-based data synthesis have emerged as two fundamental LLM-driven data annotation methods in model development. However, while their combination significantly enhances the efficiency of model training and evaluation, little attention has been given to the potential contamination brought by this new model development paradigm.

**Types of Relatedness:**
Three common relatednesses between the data generator LLM and the judge LLM are: being the same model, having an inheritance relationship, and belonging to the same model family.

**Key Findings:**
Through extensive experiments, the researchers empirically confirm the bias of judges towards their related student models caused by preference leakage across multiple LLM baselines and benchmarks. Preference leakage is a pervasive and real-world problem that is harder to detect compared to previously identified biases in LLM-as-a-judge scenarios.

This paper was accepted at ICLR 2026 and is authored by Dawei Li and colleagues.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f76d4391-c65d-4ad2-8ebf-ec6f4a82a777",
  "isSidechain": false,
  "promptId": "7f63e8fc-85c3-4e6d-bc0e-cacc7b545dea",
  "type": "user",
  "uuid": "af6c740b-11e7-44ce-bfad-79ade66a03a3",
  "toolUseResult": {
    "query": "\"Preference Leakage\" contamination LLM judge ICLR 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_012YQYs4mTA8UuuC33wR9FAa",
        "content": [
          {
            "title": "Preference Leakage: A Contamination Problem in LLM-as-a-judge | OpenReview",
            "url": "https://openreview.net/forum?id=grIvSXVJ65"
          },
          {
            "title": "Preference Leakage: A Contamination Problem in LLM-as-a-judge [Quick Review]",
            "url": "https://liner.com/review/preference-leakage-a-contamination-problem-in-llmasajudge"
          },
          {
            "title": "[Paper Note] Preference Leakage: A Contamination Problem in LLM-as-a-judge - 📚 AI Paper Notes",
            "url": "https://en.papernotes.org/ICLR2026/llm_evaluation/preference_leakage_a_contamination_problem_in_llm-as-a-judge/"
          },
          {
            "title": "ICLR Poster Preference Leakage: A Contamination Problem in LLM-as-a-judge",
            "url": "https://iclr.cc/virtual/2026/poster/10008112"
          },
          {
            "title": "LLM-as-a-judge",
            "url": "https://llm-as-a-judge.github.io/"
          },
          {
            "title": "Preference Leakage: A Contamination Problem in LLM-as-a-judge",
            "url": "https://arxiv.org/html/2502.01534v3"
          },
          {
            "title": "[2502.01534] Preference Leakage: A Contamination Problem in LLM-as-a-judge",
            "url": "https://arxiv.org/abs/2502.01534"
          },
          {
            "title": "Preference Leakage: A Contamination Problem in LLM-as- ...",
            "url": "https://arxiv.org/pdf/2502.01534"
          },
          {
            "title": "Paper page - Preference Leakage: A Contamination Problem in LLM-as-a-judge",
            "url": "https://huggingface.co/papers/2502.01534"
          }
        ]
      },
      "Based on the search results, I found relevant information about this paper:\n\n## Preference Leakage: A Contamination Problem in LLM-as-a-Judge\n\nPreference leakage is a contamination problem in LLM-as-a-judge caused by the relatedness between the synthetic data generators and LLM-based evaluators.\n\n**Key Context:**\nLarge Language Models (LLMs) as judges and LLM-based data synthesis have emerged as two fundamental LLM-driven data annotation methods in model development. However, while their combination significantly enhances the efficiency of model training and evaluation, little attention has been given to the potential contamination brought by this new model development paradigm.\n\n**Types of Relatedness:**\nThree common relatednesses between the data generator LLM and the judge LLM are: being the same model, having an inheritance relationship, and belonging to the same model family.\n\n**Key Findings:**\nThrough extensive experiments, the researchers empirically confirm the bias of judges towards their related student models caused by preference leakage across multiple LLM baselines and benchmarks. Preference leakage is a pervasive and real-world problem that is harder to detect compared to previously identified biases in LLM-as-a-judge scenarios.\n\nThis paper was accepted at ICLR 2026 and is authored by Dawei Li and colleagues."
    ],
    "durationSeconds": 5.323963545999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f76d4391-c65d-4ad2-8ebf-ec6f4a82a777",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T04:41:12.857Z_

<details><summary>↩ Tool result · `toolu_01AeuuJErqyyq3qqQ64btMfY`</summary>

```text
Web search results for query: "counterfactual style rewriting LLM judge debiasing post-hoc model-agnostic 2025 2026"

Links: [{"title":"LLM-Based Judge Model","url":"https://www.emergentmind.com/topics/llm-based-judge-model"},{"title":"CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models","url":"https://arxiv.org/html/2507.15698v1"},{"title":"Counterfactual LLM-based Framework for Measuring Rhetorical Style","url":"https://www.researchgate.net/publication/399026376_Counterfactual_LLM-based_Framework_for_Measuring_Rhetorical_Style"},{"title":"[2512.19908] Counterfactual LLM-based Framework for Measuring Rhetorical Style","url":"https://arxiv.org/abs/2512.19908"},{"title":"Debiasing Text Safety Classifiers through a Fairness-Aware Ensemble","url":"https://arxiv.org/pdf/2409.13705"},{"title":"Rubric-Based Evaluations & LLM-as-a-Judge — Methodologies, Biases, and Empirical Validation in Domain-Specific Contexts. | by Adnan Masood, PhD. | Apr, 2026 | Medium","url":"https://medium.com/@adnanmasood/rubric-based-evals-llm-as-a-judge-methodologies-and-empirical-validation-in-domain-context-71936b989e80"},{"title":"FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge","url":"https://arxiv.org/pdf/2602.06625"}]

I found several relevant results about counterfactual approaches for LLM evaluation and debiasing. Here are the key findings:

## Counterfactual Style Rewriting Framework

A counterfactual LLM-based framework has been introduced where multiple LLM rhetorical personas generate counterfactual writings from the same substantive content, an LLM judge compares them through pairwise evaluations, and the outcomes are aggregated using a Bradley-Terry model. This method has been applied to 8,485 ICLR submissions sampled from 2017 to 2025, generating more than 250,000 counterfactual writings to quantify rhetorical style in ML papers.

## Post-hoc Debiasing Strategies

For calibration to human annotation, post-hoc statistical models are recommended, such as quantitative/GLM, jury-based, or regression methods. Current debiasing strategies including prompt augmentation, ensembling, and counterfactual audits are necessary but insufficient, particularly for domain- and language-general evaluation.

## Fairness and Auditing

Group fairness cannot be achieved by size, release date, or country of origin; explicit debiasing and counterfactual auditing are necessary. Regular audits of model outputs across all dimensions—accuracy, agreement, bias, robustness, and fairness—using comprehensive, ideally counterfactually-augmented, benchmarks are recommended.

## LLM Judge Debiasing Approaches

The FairJudge method treats judging behavior as a learning objective, aiming to systematically improve LLM-as-a-Judge systems in terms of adaptivity, debiasing, and consistency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "88670fc5-971e-46bf-9c87-5a687f846505",
  "isSidechain": false,
  "promptId": "7f63e8fc-85c3-4e6d-bc0e-cacc7b545dea",
  "type": "user",
  "uuid": "68705599-650a-4804-8509-bc782261583a",
  "toolUseResult": {
    "query": "counterfactual style rewriting LLM judge debiasing post-hoc model-agnostic 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_014XShD64cHMKH4UcX4dMeyq",
        "content": [
          {
            "title": "LLM-Based Judge Model",
            "url": "https://www.emergentmind.com/topics/llm-based-judge-model"
          },
          {
            "title": "CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models",
            "url": "https://arxiv.org/html/2507.15698v1"
          },
          {
            "title": "Counterfactual LLM-based Framework for Measuring Rhetorical Style",
            "url": "https://www.researchgate.net/publication/399026376_Counterfactual_LLM-based_Framework_for_Measuring_Rhetorical_Style"
          },
          {
            "title": "[2512.19908] Counterfactual LLM-based Framework for Measuring Rhetorical Style",
            "url": "https://arxiv.org/abs/2512.19908"
          },
          {
            "title": "Debiasing Text Safety Classifiers through a Fairness-Aware Ensemble",
            "url": "https://arxiv.org/pdf/2409.13705"
          },
          {
            "title": "Rubric-Based Evaluations & LLM-as-a-Judge — Methodologies, Biases, and Empirical Validation in Domain-Specific Contexts. | by Adnan Masood, PhD. | Apr, 2026 | Medium",
            "url": "https://medium.com/@adnanmasood/rubric-based-evals-llm-as-a-judge-methodologies-and-empirical-validation-in-domain-context-71936b989e80"
          },
          {
            "title": "FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge",
            "url": "https://arxiv.org/pdf/2602.06625"
          }
        ]
      },
      "I found several relevant results about counterfactual approaches for LLM evaluation and debiasing. Here are the key findings:\n\n## Counterfactual Style Rewriting Framework\n\nA counterfactual LLM-based framework has been introduced where multiple LLM rhetorical personas generate counterfactual writings from the same substantive content, an LLM judge compares them through pairwise evaluations, and the outcomes are aggregated using a Bradley-Terry model. This method has been applied to 8,485 ICLR submissions sampled from 2017 to 2025, generating more than 250,000 counterfactual writings to quantify rhetorical style in ML papers.\n\n## Post-hoc Debiasing Strategies\n\nFor calibration to human annotation, post-hoc statistical models are recommended, such as quantitative/GLM, jury-based, or regression methods. Current debiasing strategies including prompt augmentation, ensembling, and counterfactual audits are necessary but insufficient, particularly for domain- and language-general evaluation.\n\n## Fairness and Auditing\n\nGroup fairness cannot be achieved by size, release date, or country of origin; explicit debiasing and counterfactual auditing are necessary. Regular audits of model outputs across all dimensions—accuracy, agreement, bias, robustness, and fairness—using comprehensive, ideally counterfactually-augmented, benchmarks are recommended.\n\n## LLM Judge Debiasing Approaches\n\nThe FairJudge method treats judging behavior as a learning objective, aiming to systematically improve LLM-as-a-Judge systems in terms of adaptivity, debiasing, and consistency."
    ],
    "durationSeconds": 8.598036896000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "88670fc5-971e-46bf-9c87-5a687f846505",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-20T04:41:16.955Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me search for the most critical comparison - the "Counterfactual LLM-based Framework for Measuring Rhetorical Style" paper, which seems very closely related to this proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68705599-650a-4804-8509-bc782261583a",
  "isSidechain": false,
  "requestId": "req_011CbDCwCuSBV5zHA3d24jCu",
  "type": "assistant",
  "uuid": "f48dcb34-6c25-4a29-b17e-527c78b6d81b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JU8xs9drqdBR94CvZ1FVu8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 861,
      "cache_creation_input_tokens": 1604,
      "cache_read_input_tokens": 27337,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1604,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 861,
          "output_tokens": 187,
          "cache_read_input_tokens": 27337,
          "cache_creation_input_tokens": 1604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1604
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

_source line 40 · 2026-05-20T04:41:17.443Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H3QjBZWKtNjqi89zH9WJDP`</summary>

```json
{
  "query": "arXiv 2512.19908 counterfactual LLM rhetorical style Bradley-Terry measurement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f48dcb34-6c25-4a29-b17e-527c78b6d81b",
  "isSidechain": false,
  "requestId": "req_011CbDCwCuSBV5zHA3d24jCu",
  "type": "assistant",
  "uuid": "3c2a600f-42d9-45a4-86fc-8b9bfe4cf528",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JU8xs9drqdBR94CvZ1FVu8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 861,
      "cache_creation_input_tokens": 1604,
      "cache_read_input_tokens": 27337,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1604,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 861,
          "output_tokens": 187,
          "cache_read_input_tokens": 27337,
          "cache_creation_input_tokens": 1604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1604
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

_source line 41 · 2026-05-20T04:41:17.945Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Voew42aZHYJ8BepRry2W43`</summary>

```json
{
  "query": "JudgeBiasBench counterfactual bias injection Gemini 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c2a600f-42d9-45a4-86fc-8b9bfe4cf528",
  "isSidechain": false,
  "requestId": "req_011CbDCwCuSBV5zHA3d24jCu",
  "type": "assistant",
  "uuid": "5fe87ee3-fe7d-4896-8d6e-bd89b3d9f5b4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JU8xs9drqdBR94CvZ1FVu8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 861,
      "cache_creation_input_tokens": 1604,
      "cache_read_input_tokens": 27337,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1604,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 861,
          "output_tokens": 187,
          "cache_read_input_tokens": 27337,
          "cache_creation_input_tokens": 1604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1604
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

_source line 42 · 2026-05-20T04:41:24.478Z_

<details><summary>↩ Tool result · `toolu_01Voew42aZHYJ8BepRry2W43`</summary>

```text
Web search results for query: "JudgeBiasBench counterfactual bias injection Gemini 2026"

Links: [{"title":"Toward Robust LLM-Based Judges: Taxonomic Bias Evaluation and Debiasing Optimization","url":"https://arxiv.org/pdf/2603.08091"},{"title":"Is Your LLM-as-a-Recommender Agent Trustable? LLMs' Recommendation is Easily Hacked by Biases (Preferences)","url":"https://arxiv.org/pdf/2603.17417"},{"title":"The Silent Judge: Unacknowledged Shortcut Bias in LLM-as-a-Judge","url":"https://arxiv.org/pdf/2509.26072"},{"title":"OffsetBias: Leveraging Debiased Data for Tuning Evaluators","url":"https://arxiv.org/pdf/2407.06551"},{"title":"Algorithmic Bias: Google Gemini Faces Intensifying Scrutiny - AI CERTs News","url":"https://www.aicerts.ai/news/algorithmic-bias-google-gemini-faces-intensifying-scrutiny/"},{"title":"The Judge Who Never Admits: Hidden Shortcuts in LLM-based Evaluation","url":"https://arxiv.org/pdf/2602.07996"},{"title":"AI Bias and Fairness: From Detection to Mitigation in 2026 | Zylos Research","url":"https://zylos.ai/research/2026-02-05-ai-bias-fairness"},{"title":"Strategies for Mitigating Algorithmic Bias in Gemini | by Raffaello Palandri | Medium","url":"https://raffaellopalandri.medium.com/strategies-for-mitigating-algorithmic-bias-in-gemini-318e27ff3b74"},{"title":"Google Gemini Prompt Injection Flaw Exposed Private Calendar Data via Malicious Invites","url":"https://thehackernews.com/2026/01/google-gemini-prompt-injection-flaw.html"}]

Based on the search results, I found relevant information about JudgeBiasBench:

JudgeBiasBench is a benchmark for systematically quantifying biases in LLM-based judges, defining a taxonomy of judgment biases across 4 dimensions and constructing bias-augmented evaluation instances through a controlled bias injection pipeline, covering 12 representative bias types.

The benchmark encompasses 12 representative judgment bias types, each instantiated through carefully controlled perturbations that isolate task-irrelevant factors while preserving task-relevant correctness.

Extensive experiments across both generative and discriminative judges reveal that current judges exhibit significant and diverse bias patterns that often compromise the reliability of automated evaluation.

To mitigate judgment bias, the research proposes bias-aware training that explicitly incorporates bias-related attributes into the training process, encouraging judges to disentangle task-relevant quality from bias-correlated cues, using reinforcement learning for generative judges and contrastive learning for discriminative judges.

The search results show this is recent research (from an arxiv paper with identifier 2603.08091), representing current work in evaluating and mitigating biases in LLM-based judge systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5fe87ee3-fe7d-4896-8d6e-bd89b3d9f5b4",
  "isSidechain": false,
  "promptId": "7f63e8fc-85c3-4e6d-bc0e-cacc7b545dea",
  "type": "user",
  "uuid": "5dd1cfa9-4075-4a30-87ce-c01890b1131a",
  "toolUseResult": {
    "query": "JudgeBiasBench counterfactual bias injection Gemini 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XFskqnwhbDGfKi9dsrV9vp",
        "content": [
          {
            "title": "Toward Robust LLM-Based Judges: Taxonomic Bias Evaluation and Debiasing Optimization",
            "url": "https://arxiv.org/pdf/2603.08091"
          },
          {
            "title": "Is Your LLM-as-a-Recommender Agent Trustable? LLMs' Recommendation is Easily Hacked by Biases (Preferences)",
            "url": "https://arxiv.org/pdf/2603.17417"
          },
          {
            "title": "The Silent Judge: Unacknowledged Shortcut Bias in LLM-as-a-Judge",
            "url": "https://arxiv.org/pdf/2509.26072"
          },
          {
            "title": "OffsetBias: Leveraging Debiased Data for Tuning Evaluators",
            "url": "https://arxiv.org/pdf/2407.06551"
          },
          {
            "title": "Algorithmic Bias: Google Gemini Faces Intensifying Scrutiny - AI CERTs News",
            "url": "https://www.aicerts.ai/news/algorithmic-bias-google-gemini-faces-intensifying-scrutiny/"
          },
          {
            "title": "The Judge Who Never Admits: Hidden Shortcuts in LLM-based Evaluation",
            "url": "https://arxiv.org/pdf/2602.07996"
          },
          {
            "title": "AI Bias and Fairness: From Detection to Mitigation in 2026 | Zylos Research",
            "url": "https://zylos.ai/research/2026-02-05-ai-bias-fairness"
          },
          {
            "title": "Strategies for Mitigating Algorithmic Bias in Gemini | by Raffaello Palandri | Medium",
            "url": "https://raffaellopalandri.medium.com/strategies-for-mitigating-algorithmic-bias-in-gemini-318e27ff3b74"
          },
          {
            "title": "Google Gemini Prompt Injection Flaw Exposed Private Calendar Data via Malicious Invites",
            "url": "https://thehackernews.com/2026/01/google-gemini-prompt-injection-flaw.html"
          }
        ]
      },
      "Based on the search results, I found relevant information about JudgeBiasBench:\n\nJudgeBiasBench is a benchmark for systematically quantifying biases in LLM-based judges, defining a taxonomy of judgment biases across 4 dimensions and constructing bias-augmented evaluation instances through a controlled bias injection pipeline, covering 12 representative bias types.\n\nThe benchmark encompasses 12 representative judgment bias types, each instantiated through carefully controlled perturbations that isolate task-irrelevant factors while preserving task-relevant correctness.\n\nExtensive experiments across both generative and discriminative judges reveal that current judges exhibit significant and diverse bias patterns that often compromise the reliability of automated evaluation.\n\nTo mitigate judgment bias, the research proposes bias-aware training that explicitly incorporates bias-related attributes into the training process, encouraging judges to disentangle task-relevant quality from bias-correlated cues, using reinforcement learning for generative judges and contrastive learning for discriminative judges.\n\nThe search results show this is recent research (from an arxiv paper with identifier 2603.08091), representing current work in evaluating and mitigating biases in LLM-based judge systems."
    ],
    "durationSeconds": 6.528794105999994,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5fe87ee3-fe7d-4896-8d6e-bd89b3d9f5b4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-20T04:41:25.115Z_

<details><summary>↩ Tool result · `toolu_01H3QjBZWKtNjqi89zH9WJDP`</summary>

```text
Web search results for query: "arXiv 2512.19908 counterfactual LLM rhetorical style Bradley-Terry measurement"

Links: [{"title":"[2512.19908] Counterfactual LLM-based Framework for Measuring Rhetorical Style","url":"https://arxiv.org/abs/2512.19908"},{"title":"Counterfactual LLM-based Framework for Measuring Rhetorical Style","url":"https://arxiv.org/html/2512.19908v1"},{"title":"Counterfactual LLM-based Framework for Measuring Rhetorical Style","url":"https://arxiv.org/pdf/2512.19908"},{"title":"COUNTERFACTUAL LLM-BASED FRAMEWORK FOR ...","url":"https://openreview.net/pdf/d3ec7b4b810a4d77348ff7a47f8e49cd19606c7e.pdf"},{"title":"[Literature Review] Counterfactual LLM-based Framework for Measuring Rhetorical Style","url":"https://www.themoonlight.io/en/review/counterfactual-llm-based-framework-for-measuring-rhetorical-style"},{"title":"Counterfactual LLM-based Framework for Measuring Rhetorical Style | OpenReview","url":"https://openreview.net/forum?id=fiohEI16sf"},{"title":"Counterfactual LLM-based Framework for Measuring Rhetorical Style","url":"https://www.researchgate.net/publication/399026376_Counterfactual_LLM-based_Framework_for_Measuring_Rhetorical_Style"}]

I found the paper you're looking for! Here's information about arXiv paper 2512.19908:

**Title:** Counterfactual LLM-based Framework for Measuring Rhetorical Style

**Authors:** Jingyi Qiu (University of Michigan), Hong Chen (University of Michigan), and Zongyi Li (MIT)

**Overview:** The paper addresses the challenge of distinguishing rhetorical style from substantive content in academic papers, proposing that multiple LLM rhetorical personas generate counterfactual writings from the same substantive content, an LLM judge compares them through pairwise evaluations, and the outcomes are aggregated using a Bradley-Terry model.

**Key Findings:**
- The study analyzed 8,485 ICLR submissions from 2017 to 2025, generating more than 250,000 counterfactual writings
- Visionary framing significantly predicts downstream attention, including citations and media attention, even after controlling for peer-review evaluations
- There is a sharp rise in rhetorical strength after 2023, largely driven by the adoption of LLM-based writing assistance

**Validation:** The framework's reliability is validated by its robustness to the choice of personas and the high correlation between LLM judgments and human annotations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c2a600f-42d9-45a4-86fc-8b9bfe4cf528",
  "isSidechain": false,
  "promptId": "7f63e8fc-85c3-4e6d-bc0e-cacc7b545dea",
  "type": "user",
  "uuid": "33df25dd-31e9-4eed-9a77-f4e22f7d7391",
  "toolUseResult": {
    "query": "arXiv 2512.19908 counterfactual LLM rhetorical style Bradley-Terry measurement",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MRiEUotLQ2mdpVamSDYWSa",
        "content": [
          {
            "title": "[2512.19908] Counterfactual LLM-based Framework for Measuring Rhetorical Style",
            "url": "https://arxiv.org/abs/2512.19908"
          },
          {
            "title": "Counterfactual LLM-based Framework for Measuring Rhetorical Style",
            "url": "https://arxiv.org/html/2512.19908v1"
          },
          {
            "title": "Counterfactual LLM-based Framework for Measuring Rhetorical Style",
            "url": "https://arxiv.org/pdf/2512.19908"
          },
          {
            "title": "COUNTERFACTUAL LLM-BASED FRAMEWORK FOR ...",
            "url": "https://openreview.net/pdf/d3ec7b4b810a4d77348ff7a47f8e49cd19606c7e.pdf"
          },
          {
            "title": "[Literature Review] Counterfactual LLM-based Framework for Measuring Rhetorical Style",
            "url": "https://www.themoonlight.io/en/review/counterfactual-llm-based-framework-for-measuring-rhetorical-style"
          },
          {
            "title": "Counterfactual LLM-based Framework for Measuring Rhetorical Style | OpenReview",
            "url": "https://openreview.net/forum?id=fiohEI16sf"
          },
          {
            "title": "Counterfactual LLM-based Framework for Measuring Rhetorical Style",
            "url": "https://www.researchgate.net/publication/399026376_Counterfactual_LLM-based_Framework_for_Measuring_Rhetorical_Style"
          }
        ]
      },
      "I found the paper you're looking for! Here's information about arXiv paper 2512.19908:\n\n**Title:** Counterfactual LLM-based Framework for Measuring Rhetorical Style\n\n**Authors:** Jingyi Qiu (University of Michigan), Hong Chen (University of Michigan), and Zongyi Li (MIT)\n\n**Overview:** The paper addresses the challenge of distinguishing rhetorical style from substantive content in academic papers, proposing that multiple LLM rhetorical personas generate counterfactual writings from the same substantive content, an LLM judge compares them through pairwise evaluations, and the outcomes are aggregated using a Bradley-Terry model.\n\n**Key Findings:**\n- The study analyzed 8,485 ICLR submissions from 2017 to 2025, generating more than 250,000 counterfactual writings\n- Visionary framing significantly predicts downstream attention, including citations and media attention, even after controlling for peer-review evaluations\n- There is a sharp rise in rhetorical strength after 2023, largely driven by the adoption of LLM-based writing assistance\n\n**Validation:** The framework's reliability is validated by its robustness to the choice of personas and the high correlation between LLM judgments and human annotations."
    ],
    "durationSeconds": 7.667575065999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3c2a600f-42d9-45a4-86fc-8b9bfe4cf528",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-20T04:42:27.579Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture of the field. Let me analyze this proposal carefully.

## Summary of what I've found:

### Key Related Works:
1. **SOS-Bench (ICLR 2025)**: Documents the style-over-substance problem in LLM judges with 152K data points. Shows style bias is dominant but proposes no fix.

2. **FairJudge (arXiv Feb 2026)**: Trains a dedicated debiased judge via SFT→DPO→GRPO. Requires retraining; cannot debias black-box APIs. This is the most directly competitive work.
   
3. **RATE (ICML 2025)**: A double-rewrite protocol for causal effect estimation on reward models that handles imperfect counterfactuals—this is the methodological foundation the proposal builds directly on.

4. **Length-Controlled AlpacaEval (ICLR 2025)**: Uses post-hoc regression debiasing but only for length, making it a successful single-dimension predecessor in the post-hoc debiasing space.

5. **Preference Leakage (ICLR 2026)**: Identifies contamination from model relatedness rather than style bias specifically.

6. **CASSE (Jan 2026)**: Demonstrates that style features are...

Examining related work on style bias measurement and debiasing approaches. CASSE shows style features are deeply entangled, which supports the legitimacy-aware correction approach. There's also work using counterfactual style rewrites with Bradley-Terry models to measure rhetorical style in academic papers, though that focuses on measurement rather than debiasing judge scores. Other recent work tests multiple debiasing strategies across different judges but concentrates on position and verbosity without causal style removal, and there's bias injection work for constructing test sets.

The core novelty here is combining content-preserving binary style counterfactuals with doubly-robust DML estimation for black-box judge debiasing. While counterfactual style rewriting isn't entirely new—there's existing work using it for measurement purposes—applying it specifically to debiasing through causal estimation appears to be the distinguishing contribution. causal effect estimation on reward models.

2. **DML for text causal inference** — DML is well-established in econometrics. Applying it to text treatments has been explored in causal text analysis literature.

3. **Post-hoc debiasing of black-box judges** — Length-Controlled AlpacaEval does this for length. BBE does this with noise injection.

The key novelty is the **combination**: binary style counterfactuals + RATE double-rewrite + DML partially linear model + multi-dimensional style decomposition + legitimacy-aware correction, all applied to black-box judge debiasing. This is a genuine systems contribution with an original combination, but the individual components are not new.

The most novel element is probably the **legitimacy-aware correction** with the α parameter and domain-conditional analysis. The insight that some style effects are legitimate (e.g., well-structured markdown for code) and distinguishing bias from legitimate style-quality correlation is genuinely interesting.

The problem itself is clearly important—style bias in LLM judges is well-documented and a major practical concern, and no existing method handles post-hoc causal style debiasing for black-box judges. But I'm wondering whether the practical impact justifies the 7x inference cost, especially since the amortized version requires training and somewhat contradicts the "no training needed" premise. I should also check whether a simple format normalization baseline might already handle much of this. are deeply entangled with each other, so the independence assumption is questionable. The multivariate DML approach helps, but the counterfactual generation still assumes I can manipulate each axis separately. I'm also concerned about content preservation—claiming BERTScore and NLI thresholds validate that formality and verbosity changes don't shift meaning seems optimistic, especially for technical domains where precision matters. And there's a bigger question: do RATE's assumptions about decomposability and direction-independent noise actually transfer from reward models to diverse LLM judges like GPT-4o and Claude?

The linear specification for style effects is also a convenience assumption—why would style only interact additively with content when nonlinear interactions seem plausible? Despite these concerns, this is a solid proposal that addresses a genuine gap in post-hoc causal debiasing for black-box judges. The combination of RATE and DML is principled, the problem is well-motivated by empirical work like SOS-Bench and CASSE, and the evaluation plan is thorough. The novelty lies mainly in bringing these tools together for this specific application rather than in any single methodological innovation.

The main limitations are that the core finding—removing style effects improves judge accuracy—wouldn't surprise reviewers, the 7x cost overhead is significant, and a simpler multi-dimensional regression baseline might achieve similar results at much lower cost. The amortized version also requires training, which partially undermines the claimed advantage over FairJudge. Still, the work is methodologically sound and addresses a real problem, even if the insight itself feels somewhat expected.

For EMNLP 2026, I'm settling on around 25-35% acceptance probability, with 30% as my median estimate. The novelty is moderate—the combination is new but the pieces already exist—and while the significance is solid and the related work coverage is excellent, the trivial alternative threat of simpler debiasing methods is a genuine concern that could sway reviewers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33df25dd-31e9-4eed-9a77-f4e22f7d7391",
  "isSidechain": false,
  "requestId": "req_011CbDCx7Bv5f4aCDXi2Y1Vv",
  "type": "assistant",
  "uuid": "6030fd32-b2ba-4efe-abe6-3e5286b2c7ca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WtCa6b3z6DvqDVmHcpiy3i",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 826,
      "cache_creation_input_tokens": 1800,
      "cache_read_input_tokens": 28941,
      "output_tokens": 7136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1800,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 826,
          "output_tokens": 7136,
          "cache_read_input_tokens": 28941,
          "cache_creation_input_tokens": 1800,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1800
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

_source line 45 · 2026-05-20T04:44:14.108Z_

Now I have enough research context to make an informed assessment. Let me compile the evaluation.

---

```
【阶段】: Triage

【领域调研】:
- **SOS-Bench / "Style Outweighs Substance" (ICLR 2025, arXiv 2409.15268)**: 最大规模的 LLM judge 偏差元基准（152K 数据点），证实 style bias 在所有主流 judge 中占主导地位（sarcasm 导致 96% 偏好损失，而错误答案仅 13%）。该工作只诊断不治疗——没有提出任何 debiasing 方案。Proposal 正确识别了这个"诊断无方案"的空白。
- **FairJudge (arXiv 2602.06625, Feb 2026)**: 最直接的竞争者。通过 SFT→DPO→GRPO 课程式训练（Qwen3-VL 2B/4B/8B backbone）构建去偏 judge，在 PandaLM 76.83%、JudgeLM 78.82% agreement。**核心局限**：需要重新训练 judge 模型，无法适用于 GPT-4o/Claude/Gemini 等黑盒 API。Proposal 的 model-agnostic 定位与之差异化合理。
- **RATE (ICML 2025, arXiv 2410.11348)**: 本 proposal 最核心的方法论前身。使用 double-rewrite protocol 校正不完美反事实，估计 reward model 对高层属性的因果效应。**关键区别**：RATE 的目标是 reward model explainability，而非 judge debiasing。CSD 本质上是将 RATE 的 rewrite protocol 嫁接到 DML 框架并应用于 judge 去偏——这是一个 application pivot 而非方法论创新。
- **Length-Controlled AlpacaEval (ICLR 2025, arXiv 2404.04475)**: 通过 logistic regression 控制 length 的 post-hoc debiasing 方案，将与 ChatBot Arena 的 Spearman 相关性从 0.93 提升到 0.98。**这是最重要的 trivial alternative 参照物**：该方法成本为零，单维度回归即取得巨大效果。Proposal 需要令人信服地证明多维因果分解（7x 成本开销）相对于"多维回归控制"的增量价值。
- **Counterfactual LLM-based Framework for Measuring Rhetorical Style (arXiv 2512.19908, Dec 2025)**: 使用 LLM 生成反事实风格重写 + Bradley-Terry 模型量化学术论文的修辞风格。在 8,485 篇 ICLR 投稿上生成 250K+ 反事实文本。该工作与 CSD 共享"反事实风格重写"的核心技术思路，但目标是 style measurement 而非 judge debiasing。
- **Bias-Bounded Evaluation (arXiv 2603.05485, March 2026)**: 差分隐私启发的校准高斯噪声注入，在 Arena-Hard-Auto 上保留 61-99% 排名相关性。非因果方法，提供形式化偏差上界保证。
- **Preference Leakage (ICLR 2026, arXiv 2502.01534)**: 发现 judge 与生成模型的"亲缘关系"导致评估偏差，属于 contamination bias 而非 style bias，与本 proposal 正交但同属 judge bias 生态。
- **CASSE (arXiv 2601.10809, Jan 2026)**: 研究 12 种 style feature 的交互效应，核心发现 style features "deeply entangled rather than orthogonal"。这同时支持了 proposal 的 legitimacy-aware correction 设计，但也威胁了其"三轴独立"假设。
- **Choi et al. ISE (NAACL 2024)**: 论证 ATE 在自由文本 treatment 上因 positivity violation 不可行。Proposal 通过限制 binary style intervention 来规避此批评，这个应对策略在方法论上是合理的。
- **Judging the Judges / Soumik (arXiv 2604.23178, April 2026)**: 系统测试 9 种 debiasing 策略 × 5 种 judge，但聚焦 position/verbosity bias，没有系统性因果 style removal。
- **调研总结**: Style bias in LLM judges 是一个已被充分诊断但 debiasing 方案稀缺的领域。现有方案要么需要训练（FairJudge），要么只控单维度（LC-AlpacaEval），要么非因果（BBE）。Post-hoc + model-agnostic + 多维因果的组合确实存在空白。但 RATE 的 double-rewrite + 反事实风格重写 的技术路线已在邻近工作中被探索，CSD 的核心创新更多在于"组合与应用场景"而非"方法论突破"。


【Trivial Alternative 检验】:

**存在两个严重的 trivial alternative 威胁：**

1. **多维回归控制（Multi-dimensional LC-AlpacaEval 扩展）**: LC-AlpacaEval 仅用单维度 logistic regression 控制 length 就将相关性从 0.93→0.98，零额外推理成本。一个自然的扩展是：提取多个 surface features（token count、markdown 标记密度、平均句长、正式词占比等），用多维回归做 post-hoc 控制。这个方法：无需反事实生成（省去 7x 成本）、无需 DML 框架、无需 content preservation 验证。如果这个 trivial baseline 能达到 CSD 80%+ 的去偏效果，CSD 的增量价值将严重受损。Proposal 确实包含了 LC-AlpacaEval 作为 baseline，但仅作为"单维度"对比——真正的威胁是多维度扩展版，proposal 未直接面对这个问题。

2. **Format normalization + 简单 prompt engineering**: Proposal 自己也列了 "strip all markdown before judging" 作为 baseline，加上 "请忽略风格只关注内容" 的 prompt，这组合的成本几乎为零。如果格式化是 style bias 的主要来源（markdown/列表视觉效果），这个 trivial 方法可能已覆盖大部分效应。

**增量价值声称**：CSD 的增量价值需建立在以下论证上：(a) 多维回归无法捕捉 style 与 content 之间的非线性交互，而 DML 可以；(b) 因果估计提供了 per-response 的风格归因（而非群体平均），对个案审查有价值；(c) legitimacy-aware correction 需要因果框架才能区分 bias 与合法相关性。论证 (c) 最具说服力，但也最难验证。


【前提假设检验】:

**核心 claim 的逻辑链中，有以下关键未验证假设：**

1. **"三轴独立"假设**：Proposal 声称 formality、verbosity、formatting "genuinely independent"，但 CASSE (Jan 2026) 的核心发现恰恰是 style features "deeply entangled"。例如：formal 文本通常更 verbose、更倾向使用 structured formatting。虽然 proposal 提到用 multivariate DML 处理残余相关，但反事实生成阶段仍假定可以独立翻转单个轴而不影响其他轴。如果 flip formality 的同时系统性地改变了 verbosity（因为 casual 文本天然更短），整个因果估计框架的有效性就受到威胁。

2. **Content preservation under style rewriting**: BERTScore ≥ 0.92 和 NLI ≥ 0.95 是否足以保证"内容等价"？一篇高度技术性的 formal 文本被重写为 casual 版本时，术语精确度和推理严谨度可能系统性降低——这种降低不会被 BERTScore（表面语义相似度）或 NLI（单向蕴含）捕捉到。如果 content quality 在 style flip 过程中被系统性地改变，那估计的"style effect"实际上混杂了 content degradation effect。

3. **RATE 的 Assumption 1 & 2 跨 judge 迁移**：RATE 的双重重写校正依赖两个假设——方向无关的重写噪声和加性分解。这些假设在 RATE 原论文中只在特定 reward model 上验证。不同的 LLM judge（GPT-4o vs. Claude vs. Llama）可能有非常不同的评分机制，假设的跨 judge 一致性缺乏理论支撑。

4. **Style 效应线性可加性**：DML partially linear model 假定 score = β₁·formality + β₂·verbosity + β₃·formatting + g(content) + ε。但 style 效应很可能与 content domain 存在交互作用（coding 场景下 formatting 的效应远大于 creative writing 场景）。虽然 Stage 3 的 domain-conditional α 部分缓解了这个问题，但 Stage 2 的估计阶段仍假定全局线性可加性。

5. **α 的可识别性**: legitimacy-aware correction 的 α 通过"最大化与 ground-truth quality 的 Spearman 相关性"来确定。但如果 ground-truth 本身有限（200-response pilot study），α 可能过拟合这个小样本。而且如果不同 benchmark 的最优 α 差异很大，"legitimacy"本身就成了一个 benchmark-dependent 的概念而非通用原则。


【3 维度打分】:

1. **Novelty: 中** — CSD 的核心技术组件（反事实风格重写、double-rewrite 校正、DML partially linear model）均已在各自领域存在成熟先例。RATE (ICML 2025) 提供了 double-rewrite protocol，LC-AlpacaEval (ICLR 2025) 示范了 post-hoc regression debiasing，DML (Chernozhukov 2018) 是标准因果推断工具。Counterfactual LLM-based Framework (arXiv 2512.19908) 已经在使用反事实风格重写。CSD 的新颖性主要在于这些组件的**组合应用**——将 RATE 的 rewrite protocol 嫁接到 DML 框架、增加 legitimacy-aware correction、面向黑盒 judge debiasing。这是一个合理的 application novelty，但不是方法论突破。Legitimacy-aware correction (α parameter + domain-conditional analysis) 是最具原创性的贡献，但本质上是一个调参策略。如果核心结果是 "CSD 比 raw judge 提高了 correlation"，审稿人会说 "I would have guessed this works"。

2. **Significance: 中偏强** — 问题本身非常重要。SOS-Bench (ICLR 2025) 以 152K 数据点证实 style bias 是 dominant bias，CASSE 进一步揭示 style 效应的 entanglement，Preference Leakage (ICLR 2026) 揭示 judge bias 的更多维度。LLM-as-a-judge 已成为 NLP 评估基础设施的核心组件，其去偏是一个有广泛影响力的实用问题。Model-agnostic 的 post-hoc 方案填补了 FairJudge（需训练）和 LC-AlpacaEval（单维度）之间的空白。然而，7x 推理成本开销限制了实际采用场景（大规模 leaderboard 可能不愿支付这个成本），amortized 版本虽降低成本但需要训练，与 "no training needed" 的主打优势有内在张力。

3. **Related Work: 强** — 覆盖非常全面。FairJudge、RATE、LC-AlpacaEval、SOS-Bench、CASSE、BBE、Preference Leakage、ISE (Choi et al.)、DML、RBD、UDA、CyclicJudge 等均有讨论。对 ISE (NAACL 2024) 关于 positivity violation 的批评有直接回应（binary intervention 规避），与 LC-AlpacaEval 的差异化定位清晰。Landscape section 几乎覆盖了 2024-2026 的所有相关工作。唯一缺漏是 Counterfactual LLM-based Framework (arXiv 2512.19908) 虽在引用列表中但 landscape 段没有深入对比。


【概率估计】: [23% - 33%] 中位 28%

【估计理由】: 
- **Significance 是最强维度**（中偏强），问题重要且空白真实，这撑住了下界不至于太低。
- **Novelty 是主要限制维度**（中），组合应用型创新在顶会审稿中通常被视为 incremental。审稿人会认出 RATE + DML 的组合，并质疑 "what is the fundamental new insight beyond combining existing tools?"。核心发现若 positive（"去偏后 correlation 更高"），审稿人不会感到 surprising。
- **Trivial alternative 威胁真实**：多维回归控制（零成本）vs. CSD（7x 成本）的性价比对比，如果 CSD 不能在实验中碾压 trivial baseline，论文说服力大打折扣。这个风险拉低了上界。
- 上界 33% 反映了"如果 trivial baseline 被有效击败 + legitimacy-aware correction 展示出意想不到的效果"的最佳情景。下界 23% 反映了"novelty 被判 incremental + trivial baseline 表现相近"的情景。

【主要风险】: 
1. **Novelty 被判为 incremental（"RATE + DML = CSD"）**: 审稿人可能认为这是将两个已知工具组合应用到一个新场景，缺乏方法论深度。尤其当 RATE 已经做了 double-rewrite 因果效应估计、LC-AlpacaEval 已经做了 post-hoc regression debiasing 时，"把它们合在一起做 multi-dimensional causal debiasing" 的 novelty increment 可能不足以支撑一篇顶会论文。
2. **Trivial alternative 表现出人意料地好**: 如果 "多维 surface feature 回归 + format stripping" 这个零成本方案已经能消除大部分 style bias，CSD 的 7x 推理成本开销就变得不可辩护。这是一个实验才能回答的问题，但它是 idea 层面的结构性风险——如果 trivial baseline 表现好，说明问题本身不需要因果框架来解决。
```

Sources:
- [Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking (ICLR 2025)](https://arxiv.org/abs/2409.15268)
- [FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge (arXiv 2602.06625)](https://arxiv.org/abs/2602.06625)
- [RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals (ICML 2025)](https://arxiv.org/abs/2410.11348)
- [Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators (ICLR 2025)](https://arxiv.org/abs/2404.04475)
- [Counterfactual LLM-based Framework for Measuring Rhetorical Style (arXiv 2512.19908)](https://arxiv.org/abs/2512.19908)
- [Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation (arXiv 2603.05485)](https://arxiv.org/abs/2603.05485)
- [Preference Leakage: A Contamination Problem in LLM-as-a-judge (ICLR 2026)](https://arxiv.org/abs/2502.01534)
- [A Concise Agent is Less Expert: CASSE (arXiv 2601.10809)](https://arxiv.org/abs/2601.10809)
- [Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies (arXiv 2604.23178)](https://arxiv.org/abs/2604.23178)
- [Toward Robust LLM-Based Judges: Taxonomic Bias Evaluation (arXiv 2603.08091)](https://arxiv.org/abs/2603.08091)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6030fd32-b2ba-4efe-abe6-3e5286b2c7ca",
  "isSidechain": false,
  "requestId": "req_011CbDCx7Bv5f4aCDXi2Y1Vv",
  "type": "assistant",
  "uuid": "f4adf58e-ca62-4c52-aead-40c1d72c897d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WtCa6b3z6DvqDVmHcpiy3i",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 826,
      "cache_creation_input_tokens": 1800,
      "cache_read_input_tokens": 28941,
      "output_tokens": 7136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1800,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 826,
          "output_tokens": 7136,
          "cache_read_input_tokens": 28941,
          "cache_creation_input_tokens": 1800,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1800
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

_source line 46_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Causal Style Decomposition for LLM Judge Debiasing via Doubly-Robust Counterfactual Estimation  ## Description S…",
  "leafUuid": "f4adf58e-ca62-4c52-aead-40c1d72c897d",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate LLM judge style bias debiasing proposal",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Causal Style Decomposition for LLM Judge Debiasing via Doubly-Robust Counterfactual Estimation  ## Description S…",
  "leafUuid": "f4adf58e-ca62-4c52-aead-40c1d72c897d",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a"
}
```

---

### Runtime record

_source line 49_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate LLM judge style bias debiasing proposal",
  "sessionId": "7c36a60e-68e4-44f4-9221-decc94c3003a"
}
```

---
