# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Causal Style Decomposition for LL

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-2/45668d56-1de2-4a3a-82b3-f65cc49f0197.jsonl`
- **Structured JSON:** [`68d9d337111745b40ff3.json`](../../sessions/68/68d9d337111745b40ff3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:32:22.434Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:32:22.434Z",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Causal Style Decomposition for LLM Judge Debiasing via Doubly-Robust Counterfactual Estimation\n\n## Description\nStyle bias is the dominant systematic bias in LLM-as-a-judge evaluations (effect size 0.76–0.92 across all major models), vastly exceeding position bias (≤0.04), yet no existing method causally isolates and removes style's contribution to black-box judge scores. FairJudge (Feb 2026) addresses style bias by retraining a dedicated judge, but cannot debias commercial APIs like GPT-4o or Claude. We introduce Causal Style Decomposition (CSD), a model-agnostic post-hoc debiasing framework that generates content-preserving binary style counterfactuals along three independent axes (formality, verbosity, formatting) using RATE's double-rewrite protocol, then estimates per-axis causal effects via a Double Machine Learning partially linear model (Chernozhukov et al. 2018) that preserves interpretable style coefficients while allowing arbitrary nonlinear content-quality effects. A legitimacy-aware correction avoids over-debiasing by tuning a conservatism parameter α that distinguishes domain-invariant style bias from legitimate style-quality correlations. Unlike FairJudge (requires retraining), Length-Controlled AlpacaEval (single dimension), or Bias-Bounded Evaluation (non-causal noise injection), CSD provides a principled, multi-dimensional causal decomposition applicable to any black-box judge. We evaluate across five LLM judges on SOS-Bench (objective correctness), LLMBar adversarial (style resistance), RewardBench (domain-specific), and RubricBench (atomic rubric-based), supplemented by a 200-response pilot study with separate human annotations for content and presentation quality. An optional amortized deployment stage trains a lightweight predictor to estimate style effects without generating new counterfactuals, reducing marginal overhead to near-zero. CSD requires no judge retraining, applies to any black-box judge API, and reduces per-response debiasing cost from 25x (naive) to ~7x (full pipeline) or near-zero (amortized).\n\n## Core Problem\nHow can we isolate and remove the causal effect of surface-level style on LLM judge scores while preserving legitimate style-content associations, recovering a score that more faithfully reflects content quality?\n\n## Opportunity\nStyle bias is the dominant bias in LLM judges (effect size 0.76–0.92 across all models per Soumik 2026), vastly exceeding position bias (≤0.04), yet debiasing research overwhelmingly targets position bias. SOS-Bench (ICLR 2025) demonstrated that LLM judges prioritize style over factuality and safety across 152,380 data points. The 'Preference Leakage' paper (ICLR 2026) found judges rely heavily on 'stylistic regularities—tone consistency, sentence cadence, punctuation density.' FairJudge (arXiv Feb 2026) addresses style bias through judge retraining (SFT+DPO+GRPO), but this requires training a new judge model and does not apply to black-box commercial judges. Meanwhile, the CASSE study (Jan 2026) shows style features are 'deeply entangled rather than orthogonal'—prompting for conciseness significantly reduces perceived expertise—highlighting that naive style removal risks destroying legitimate quality signals. This creates a need for a principled causal method that can (a) apply to any black-box judge, (b) quantify per-response style contributions, and (c) distinguish bias from legitimate style-quality correlation. Causal intervention techniques for LLMs now achieve 92.3% style transfer accuracy while preserving content, and the RATE framework (ICML 2025) provides a double-rewrite protocol for unbiased estimation with imperfect counterfactuals, making this technically feasible.\n\n## Landscape\nSOS-Bench (ICLR 2025) is the largest meta-benchmark documenting style-over-substance failure but proposes no fix. FairJudge (arXiv 2602.06625, Feb 2026) is the most directly relevant concurrent work: it trains a dedicated judge via SFT→DPO→GRPO on a curated 16K-instance dataset with contrastive perturbations along five non-semantic dimensions (position, length, format, reasoning style, model provenance), achieving 76.83% agreement on PandaLM and 78.82% on JudgeLM; however, it requires retraining a new judge model (Qwen3-VL 2B/4B/8B backbones) and cannot debias existing black-box commercial judges (GPT-4o, Claude, Gemini). Soumik (April 2026) tests 9 debiasing strategies across 5 judges but focuses on position/verbosity bias without systematic causal style removal. JudgeBiasBench (March 2026) uses Gemini-2.0-Flash for counterfactual bias injection but applies this to construct biased test instances rather than to estimate and remove style effects. RATE (ICML 2025) is the closest methodological precedent—it estimates causal effects of high-level attributes on reward model scores via a double-rewrite correction for imperfect counterfactuals—but targets reward model explainability, not judge debiasing. The ISE framework (Choi et al., NAACL 2024) argues ATE is inapplicable to text treatments due to positivity violations from high dimensionality, but this criticism applies to free-text treatments, not to well-defined binary style interventions where positivity holds by construction (Pryzant et al. 2021; Veitch et al. UAI 2020). Length-Controlled AlpacaEval (ICLR 2025) demonstrates effective post-hoc regression debiasing but only controls for a single dimension (length) at zero additional inference cost. Bias-Bounded Evaluation (arXiv March 2026) injects calibrated Gaussian noise for differential-privacy-inspired debiasing, retaining 61–99% ranking correlation on Arena-Hard-Auto. CyclicJudge (arXiv March 2026) uses round-robin judge assignment to reduce inter-judge variance but is style-agnostic. RBD (NeurIPS 2025) fine-tunes a reasoning-based bias detector achieving 18.5% accuracy improvement but without causal style decomposition. UDA (AAAI 2026) reduces inter-judge Elo divergence by 63.4% via adaptive K-factor calibration. The CASSE dataset (Jan 2026) documents cross-feature stylistic interactions across 12 style features, showing conciseness reduces perceived expertise, supporting our legitimacy-aware correction design. Causal Effect Estimation with Latent Textual Treatments (arXiv Feb 2026) proposes SAE-based causal estimation for latent text features but has not been applied to judge debiasing. Double Machine Learning (Chernozhukov et al. 2018) provides the partially linear model framework and DoubleML Python package we adopt for flexible decomposition. No arXiv preprint or OpenReview submission as of May 2026 proposes content-preserving binary style counterfactuals combined with doubly-robust DML estimation for black-box judge debiasing.\n\n## Approach\nWe propose Causal Style Decomposition (CSD), a model-agnostic post-hoc debiasing framework in four stages.\n\n**Stage 1 — Binary Style Counterfactual Generation.** For each response under evaluation, generate style counterfactuals along three binary axes: (A1) formality (formal ↔ casual), (A2) verbosity (verbose ↔ terse), (A3) formatting (structured/markdown ↔ plain prose). These three axes are chosen for genuine independence: formality concerns register and word choice, verbosity concerns information density, and formatting concerns visual layout. We use Qwen3-32B with axis-specific prompts, applying the RATE double-rewrite protocol: for each axis, generate (i) a counterfactual x' by flipping the axis and (ii) a double-rewrite x'' by flipping x' back. This yields 6 rewrites per response (2 per axis). Content preservation is enforced via a conjunction of BERTScore ≥ 0.92, NLI entailment ≥ 0.95 (DeBERTa-v3-large-MNLI), GPT-4o-mini content-preservation verification, and human spot-checks on a 10% random sample. **Theoretical justification for binary ATE:** Unlike free-text treatments where positivity is structurally violated (Choi et al. NAACL 2024), binary style axes define well-posed interventions satisfying positivity—any text can be made formal or casual, verbose or terse, structured or plain—following the functional intervention framework (Pryzant et al. 2021; Veitch et al. UAI 2020). RATE's Assumption 1 (direction-independent rewrite noise) and Assumption 2 (additive decomposition of reward into attribute and noise components) provide sufficient conditions for unbiased ATE estimation under imperfect counterfactuals.\n\n**Stage 2 — Doubly-Robust Causal Effect Estimation via DML.** Score each original response and its 6 counterfactuals with the target LLM judge (7 scorings per response). Estimate per-axis treatment effects using a Double Machine Learning partially linear model (Chernozhukov et al. 2018): score = β₁·formality + β₂·verbosity + β₃·formatting + g(content_features) + ε, where β coefficients capture interpretable style effects and g(·) is a nonparametric function of content features (estimated via gradient-boosted trees with 5-fold cross-fitting). This replaces the linear additive SCM: the partially linear form preserves interpretable style coefficients while allowing arbitrary nonlinear content-quality effects, and the doubly-robust property ensures consistency if either the outcome model or propensity model is correctly specified. For handling residual axis correlations (e.g., formatting weakly correlating with verbosity), we use the multivariate treatment extension of DoubleML, jointly estimating all three β coefficients rather than decomposing them independently. We include ablations comparing: (i) linear additive, (ii) DML partially linear, and (iii) fully nonparametric (kernel-based) decompositions, plus an ISE-based continuous estimator as a methodological comparison.\n\n**Stage 3 — Legitimacy-Aware Score Adjustment.** Rather than naively subtracting the full estimated style ATE (which risks over-correction when style legitimately signals quality—e.g., well-structured markdown for technical content), we introduce a conservatism parameter α ∈ [0,1]: debiased_score = raw_score − α · Σ β_k · style_k. We determine α by maximizing Spearman correlation with ground-truth quality on a held-out validation set. Additionally, we test domain-conditional α values: for each content domain (coding, reasoning, creative writing, factual QA), we estimate whether style-quality correlations are legitimate by checking if style effects are consistent across domains (bias) vs. domain-specific (potentially legitimate). Style effects that are large and domain-invariant are classified as bias; domain-specific effects are partially retained.\n\n**Stage 4 — Amortized Deployment (optional).** To reduce the ~7x overhead of full CSD for large-scale deployment, we train a lightweight amortized style-effect predictor: a small regression model (e.g., linear probe on text embeddings from a frozen encoder) trained on the counterfactual data from Stage 1–2 to predict per-response style attribution vectors from response features alone. At deployment, this predictor estimates style effects without generating new counterfactuals, reducing marginal cost to near-zero. We validate that the amortized predictor recovers ≥90% of the debiasing improvement of the full pipeline.\n\n**Evaluation.** We evaluate across five LLM judges (GPT-4o, Claude Sonnet 4, Gemini 2.5 Pro, Llama-3.3-70B, Qwen3-32B) on four benchmarks: (1) SOS-Bench—measuring whether debiased scores better correlate with objective correctness on constituent benchmarks (IFEval, MMLU-Pro, GPQA) rather than style; (2) LLMBar adversarial set—measuring whether debiased judges resist choosing wrong-but-polished over correct-but-plain responses; (3) RewardBench—domain-specific analysis across chat-hard, safety, and reasoning subsets; (4) RubricBench—1,147 pairwise comparisons with expert-annotated atomic rubrics targeting misleading surface bias. We additionally conduct a 200-response pilot human annotation study with separate 5-point Likert scales for content quality and presentation quality, providing direct validation that debiased scores correlate with content ratings while discounting presentation ratings. Baselines: FairJudge-8B, Length-Controlled AlpacaEval regression, Bias-Bounded Evaluation, raw (undebiased) judges, and a 'format normalization' baseline that strips all markdown before judging.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '100–140 A100-80GB hours (style counterfactual generation with Qwen3-32B: 6 rewrites/response × ~2K responses ≈ 30h; content verification BERTScore/NLI: 3h; open-source judge inference: 25h; DML estimation and ablations: 5h; amortized model training: 2h; iteration buffer: 35–75h)', 'timeline': '12–14 weeks', 'estimated_gpu_cost': '$250–350 (A100 spot ~$2.50/hr) + $200–350 commercial judge API costs (GPT-4o, Claude Sonnet 4, Gemini 2.5 Pro) + $100–150 GPT-4o-mini content verification + $800–1200 pilot annotation study (200 responses × 3 annotators)'}, 'human_in_loop': {'gpu_hours': '100–140 A100-80GB hours', 'timeline': '9–11 weeks', 'claude_api_cost': '$150–300 (Sonnet 4.6 at $3/$15 per MTok for prompt engineering, counterfactual quality analysis, DML specification, ablation design, and paper drafting)', 'estimated_gpu_cost': '$250–350 + $200–350 commercial judge API + $100–150 GPT-4o-mini + $800–1200 annotation study'}, 'auto_research': {'gpu_hours': '150–220 A100-80GB hours (additional ablations: linear vs. DML vs. nonparametric, ISE comparison, α sensitivity sweeps, domain-conditional analysis, amortized predictor architectures)', 'timeline': '5–7 weeks', 'claude_api_cost': '$500–750 (Sonnet 4.6 for experiment orchestration, automated counterfactual quality filtering, DML cross-fitting, statistical analysis, and full paper drafting)', 'estimated_gpu_cost': '$375–550 + $300–450 commercial judge API + $150–200 GPT-4o-mini + $800–1200 annotation study', 'speed_bottleneck': 'Sequential dependency chain: style counterfactual generation → content-preservation validation (including human spot-checks) → judge scoring → DML estimation; human annotation study runs in parallel but requires ~2 weeks for annotator recruitment and completion'}}\n\n## Inspired By\nField guide finding: 'Style bias is the dominant bias (0.76–0.92) yet has received minimal research attention'; SOS-Bench limitation that it documents but doesn't solve the problem; FairJudge's success at training-based debiasing motivating the question of whether a model-agnostic alternative exists; RATE's double-rewrite correction as a principled solution to imperfect-counterfactual bias; DML/partially-linear models as the standard tool for flexible causal decomposition with interpretable treatment coefficients; CASSE's finding that style features are entangled motivating legitimacy-aware correction.\n\n## Target Venues\n- AAAI 2027 (abstract: July 21, full paper: July 28, 2026 — primary target, 10 weeks)\n- ICLR 2027 (estimated deadline: September 24, 2026 — comfortable 18-week runway)\n- ARR October 2026 cycle (estimated deadline: October 15, 2026 — tertiary option, 21-week runway)\n\n## Key References\n- Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking (ICLR 2025)\n- Preference Leakage: A Contamination Problem in LLM-as-a-judge (ICLR 2026)\n- FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge (arXiv 2602.06625, Feb 2026)\n- Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines (arXiv 2026)\n- Toward Robust LLM-Based Judges: Taxonomic Bias Evaluation and Debiasing Optimization (arXiv 2026)\n- RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals (ICML 2025)\n- Double/Debiased Machine Learning for Treatment and Structural Parameters (Chernozhukov et al., Econometrics Journal 2018)\n- Causal Inference for Human-Language Model Collaboration (Choi et al., NAACL 2024)\n- Adapting Text Embeddings for Causal Inference (Veitch, Sridhar & Blei, UAI 2020)\n- Causal Effects of Linguistic Properties (Pryzant et al., NAACL 2021)\n- A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents (CASSE, arXiv 2601.10809, Jan 2026)\n- Counterfactual LLM-based Framework for Measuring Rhetorical Style (arXiv 2025)\n- Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators (ICLR 2025)\n- Any Large Language Model Can Be a Reliable Judge: Debiasing with a Reasoning-based Bias Detector (NeurIPS 2025)\n- Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation (arXiv 2026)\n- CausalPFN: Amortized Causal Effect Estimation via In-Context Learning (NeurIPS 2025)\n- RubricBench: Aligning Model-Generated Rubrics with Human Standards (arXiv 2603.01562, March 2026)\n- Estimating Causal Effects of Text Interventions Leveraging LLMs (Findings of AACL-IJCNLP 2025)\n- Causal Effect Estimation with Latent Textual Treatments (arXiv 2026)\n- How to Make Causal Inferences Using Texts (Egami et al., Science Advances 2022)\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T03:32:22.448Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:32:22.448Z",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197"
}
```

---

## Round 1

43 recorded events

### User

_source line 3 · 2026-05-20T03:32:22.466Z_

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
  "promptId": "e0ade265-184d-408b-8e8a-4a4a7a9fb81f",
  "type": "user",
  "uuid": "ffe9c1db-9fc0-4e04-a639-620cd3e0800b",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:32:22.465Z_

```json
{
  "parentUuid": "ffe9c1db-9fc0-4e04-a639-620cd3e0800b",
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
  "uuid": "8d640ba9-6d66-489c-bc48-9c6c70540d5e",
  "timestamp": "2026-05-20T03:32:22.465Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:32:22.465Z_

```json
{
  "parentUuid": "8d640ba9-6d66-489c-bc48-9c6c70540d5e",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7bb73ad0-de51-49f1-9be9-069ec9bc5a9c",
  "timestamp": "2026-05-20T03:32:22.465Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197",
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
  "leafUuid": "7bb73ad0-de51-49f1-9be9-069ec9bc5a9c",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate causal style decomposition for LLM judge debiasing",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197"
}
```

---

### Assistant

_source line 8 · 2026-05-20T03:32:26.994Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for its idea quality, following a specific rubric. Before I can do any evaluation, I need to do thorough web research on the field. Let me search for the key topics and papers mentioned in this proposal.

Let me first load the WebSearch tool, then conduct several searches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bb73ad0-de51-49f1-9be9-069ec9bc5a9c",
  "isSidechain": false,
  "requestId": "req_011CbD7gje8FirZvncmo9XHV",
  "type": "assistant",
  "uuid": "f6c18c65-0450-471e-92f4-b7b1aca56b12",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016kn4FgXQp6r9hqvQ13XFbr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6119,
      "cache_read_input_tokens": 13985,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6119,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 159,
          "cache_read_input_tokens": 13985,
          "cache_creation_input_tokens": 6119,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6119
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

_source line 9 · 2026-05-20T03:32:27.339Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012AQu9qzFmfMf9UL45KQTPq`</summary>

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
  "parentUuid": "f6c18c65-0450-471e-92f4-b7b1aca56b12",
  "isSidechain": false,
  "requestId": "req_011CbD7gje8FirZvncmo9XHV",
  "type": "assistant",
  "uuid": "14128629-978b-407b-9ac3-1119918bdb7e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016kn4FgXQp6r9hqvQ13XFbr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6119,
      "cache_read_input_tokens": 13985,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6119,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 159,
          "cache_read_input_tokens": 13985,
          "cache_creation_input_tokens": 6119,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6119
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

_source line 10 · 2026-05-20T03:32:27.347Z_

<details><summary>↩ Tool result · `toolu_012AQu9qzFmfMf9UL45KQTPq`</summary>

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
  "parentUuid": "14128629-978b-407b-9ac3-1119918bdb7e",
  "isSidechain": false,
  "promptId": "e0ade265-184d-408b-8e8a-4a4a7a9fb81f",
  "type": "user",
  "uuid": "5b8b6706-179e-45f8-b1ce-ee291180a9e8",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "14128629-978b-407b-9ac3-1119918bdb7e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-20T03:32:30.444Z_

Now let me conduct the required field research. I'll run multiple searches in parallel to cover the key areas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b8b6706-179e-45f8-b1ce-ee291180a9e8",
  "isSidechain": false,
  "requestId": "req_011CbD7h6fR6TLuVyNizG4XM",
  "type": "assistant",
  "uuid": "09650f98-f471-4b4e-bd73-5882d3f5f0b9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015bbbvns2C3UFVo6NrB95Pw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 686,
      "cache_read_input_tokens": 20104,
      "output_tokens": 310,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 686,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 310,
          "cache_read_input_tokens": 20104,
          "cache_creation_input_tokens": 686,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 686
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

_source line 12 · 2026-05-20T03:32:30.683Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MePvPeb7mT4oxAf83kGpRT`</summary>

```json
{
  "query": "LLM judge style bias debiasing 2025 2026 survey"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09650f98-f471-4b4e-bd73-5882d3f5f0b9",
  "isSidechain": false,
  "requestId": "req_011CbD7h6fR6TLuVyNizG4XM",
  "type": "assistant",
  "uuid": "104db327-628b-48ff-bc7b-761d851c2957",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015bbbvns2C3UFVo6NrB95Pw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 686,
      "cache_read_input_tokens": 20104,
      "output_tokens": 310,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 686,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 310,
          "cache_read_input_tokens": 20104,
          "cache_creation_input_tokens": 686,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 686
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

_source line 13 · 2026-05-20T03:32:31.157Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01529uQZzWVRH3YXAycstV15`</summary>

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
  "parentUuid": "104db327-628b-48ff-bc7b-761d851c2957",
  "isSidechain": false,
  "requestId": "req_011CbD7h6fR6TLuVyNizG4XM",
  "type": "assistant",
  "uuid": "5dd1bd49-5d9c-4cca-a6b4-d2e09107ba7d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015bbbvns2C3UFVo6NrB95Pw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 686,
      "cache_read_input_tokens": 20104,
      "output_tokens": 310,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 686,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 310,
          "cache_read_input_tokens": 20104,
          "cache_creation_input_tokens": 686,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 686
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

_source line 14 · 2026-05-20T03:32:31.929Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LWy7EsQFuwXPC1bAHazvqD`</summary>

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
  "parentUuid": "5dd1bd49-5d9c-4cca-a6b4-d2e09107ba7d",
  "isSidechain": false,
  "requestId": "req_011CbD7h6fR6TLuVyNizG4XM",
  "type": "assistant",
  "uuid": "b2b2e5fe-68e0-4871-b3da-5e5126a54c61",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015bbbvns2C3UFVo6NrB95Pw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 686,
      "cache_read_input_tokens": 20104,
      "output_tokens": 310,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 686,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 310,
          "cache_read_input_tokens": 20104,
          "cache_creation_input_tokens": 686,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 686
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

_source line 15 · 2026-05-20T03:32:32.098Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HeXA9Mpuivb5UHoDpbQYwL`</summary>

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
  "parentUuid": "b2b2e5fe-68e0-4871-b3da-5e5126a54c61",
  "isSidechain": false,
  "requestId": "req_011CbD7h6fR6TLuVyNizG4XM",
  "type": "assistant",
  "uuid": "dee21660-0ce8-41ec-9f93-088e46df3189",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015bbbvns2C3UFVo6NrB95Pw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 686,
      "cache_read_input_tokens": 20104,
      "output_tokens": 310,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 686,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 310,
          "cache_read_input_tokens": 20104,
          "cache_creation_input_tokens": 686,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 686
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

_source line 16 · 2026-05-20T03:32:32.756Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LcJjqSNXMk9SzLaxFPhwSG`</summary>

```json
{
  "query": "Double Machine Learning causal inference text NLP debiasing 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dee21660-0ce8-41ec-9f93-088e46df3189",
  "isSidechain": false,
  "requestId": "req_011CbD7h6fR6TLuVyNizG4XM",
  "type": "assistant",
  "uuid": "2fb3f6f4-cc98-4771-a53e-a979f5cd0877",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015bbbvns2C3UFVo6NrB95Pw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 686,
      "cache_read_input_tokens": 20104,
      "output_tokens": 310,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 686,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 310,
          "cache_read_input_tokens": 20104,
          "cache_creation_input_tokens": 686,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 686
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

_source line 17 · 2026-05-20T03:32:37.883Z_

<details><summary>↩ Tool result · `toolu_01LWy7EsQFuwXPC1bAHazvqD`</summary>

```text
Web search results for query: "RATE causal explainability reward models imperfect counterfactuals ICML 2025"

Links: [{"title":"RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals | OpenReview","url":"https://openreview.net/forum?id=rL3uxe5a0c"},{"title":"[2410.11348] RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals","url":"https://arxiv.org/abs/2410.11348"},{"title":"RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals","url":"https://arxiv.org/pdf/2410.11348"},{"title":"RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals","url":"https://proceedings.mlr.press/v267/reber25a.html"},{"title":"ICML Poster RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals","url":"https://icml.cc/virtual/2025/poster/43898"},{"title":"RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals","url":"https://arxiv.org/html/2410.11348"}]

I found the paper! Here are the key details about RATE:

## Overview

RATE (Rewrite-based Attribute Treatment Estimator) is an effective method for measuring the sensitivity of a reward model to high-level attributes of responses, such as sentiment, helpfulness, or complexity. RATE measures the causal effect of an attribute on the reward.

## Methodology

RATE uses LLMs to rewrite responses to produce imperfect counterfactuals examples that can be used to measure causal effects. However, these rewrites are imperfect in a manner that can induce substantial bias in the estimated sensitivity of the reward model to the attribute.

The core idea of RATE is to adjust for this imperfect-rewrite effect by rewriting twice.

## Motivation

Reward models are widely used as proxies for human preferences when aligning or evaluating LLMs. However, reward models are black boxes, and it is often unclear what, exactly, they are actually rewarding.

## Publication

The paper was published in the Proceedings of the 42nd International Conference on Machine Learning (ICML 2025), PMLR 267:51341-51368.

The paper is authored by David Reber, Sean M. Richardson, Todd Nief, Cristina Garbacea, and Victor Veitch.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b2b2e5fe-68e0-4871-b3da-5e5126a54c61",
  "isSidechain": false,
  "promptId": "e0ade265-184d-408b-8e8a-4a4a7a9fb81f",
  "type": "user",
  "uuid": "c80ac161-07f8-4991-9394-57bd5b819ab6",
  "toolUseResult": {
    "query": "RATE causal explainability reward models imperfect counterfactuals ICML 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01K664oyySQZxbPnJ6Zt6Qk3",
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
            "title": "ICML Poster RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals",
            "url": "https://icml.cc/virtual/2025/poster/43898"
          },
          {
            "title": "RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals",
            "url": "https://arxiv.org/html/2410.11348"
          }
        ]
      },
      "I found the paper! Here are the key details about RATE:\n\n## Overview\n\nRATE (Rewrite-based Attribute Treatment Estimator) is an effective method for measuring the sensitivity of a reward model to high-level attributes of responses, such as sentiment, helpfulness, or complexity. RATE measures the causal effect of an attribute on the reward.\n\n## Methodology\n\nRATE uses LLMs to rewrite responses to produce imperfect counterfactuals examples that can be used to measure causal effects. However, these rewrites are imperfect in a manner that can induce substantial bias in the estimated sensitivity of the reward model to the attribute.\n\nThe core idea of RATE is to adjust for this imperfect-rewrite effect by rewriting twice.\n\n## Motivation\n\nReward models are widely used as proxies for human preferences when aligning or evaluating LLMs. However, reward models are black boxes, and it is often unclear what, exactly, they are actually rewarding.\n\n## Publication\n\nThe paper was published in the Proceedings of the 42nd International Conference on Machine Learning (ICML 2025), PMLR 267:51341-51368.\n\nThe paper is authored by David Reber, Sean M. Richardson, Todd Nief, Cristina Garbacea, and Victor Veitch."
    ],
    "durationSeconds": 5.948403450000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b2b2e5fe-68e0-4871-b3da-5e5126a54c61",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T03:32:37.942Z_

<details><summary>↩ Tool result · `toolu_01529uQZzWVRH3YXAycstV15`</summary>

```text
Web search results for query: "FairJudge LLM debiasing arXiv 2602.06625 2026"

Links: [{"title":"[2602.06625] FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge","url":"https://arxiv.org/abs/2602.06625"},{"title":"FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge","url":"https://arxiv.org/pdf/2602.06625"},{"title":"FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge","url":"https://arxiv.org/html/2602.06625"},{"title":"FairJudge: MLLM Judging for Social-Attributes and Prompt–Image Alignment","url":"https://arxiv.org/html/2510.22827v1/"},{"title":"Debiasing LLMs by Masking Unfairness-Driving Attention Heads","url":"https://arxiv.org/pdf/2510.10142"}]

Based on the search results, I found the paper you're looking for:

FairJudge is an adaptive, debiased, and consistent LLM-as-a-Judge. The paper addresses three fundamental limitations in existing LLM-as-a-Judge systems: limited adaptivity to task and domain-specific evaluation criteria, systematic biases driven by non-semantic cues such as position, length, format, and model provenance, and evaluation inconsistency that leads to contradictory judgments across different evaluation modes (e.g., pointwise versus pairwise).

Unlike prior approaches that treat the judge as a static evaluator, FairJudge models judging behavior itself as a learnable and regularized policy. The approach uses a curriculum-style SFT-DPO-GRPO training paradigm that progressively aligns rubric adherence, bias mitigation, and cross-mode consistency, while avoiding catastrophic forgetting. Experimental results on multiple internal and public benchmarks show that FairJudge consistently improves agreement and F1, reduces non-semantic biases, and outperforms substantially larger instruction-tuned LLMs.

The paper was published on February 6, 2026, and you can access it directly at https://arxiv.org/abs/2602.06625.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5dd1bd49-5d9c-4cca-a6b4-d2e09107ba7d",
  "isSidechain": false,
  "promptId": "e0ade265-184d-408b-8e8a-4a4a7a9fb81f",
  "type": "user",
  "uuid": "91cb95aa-99d4-4e1d-ba96-2c367e958c58",
  "toolUseResult": {
    "query": "FairJudge LLM debiasing arXiv 2602.06625 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UbTaqTysbKMYF2EmSfn2Ek",
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
      "Based on the search results, I found the paper you're looking for:\n\nFairJudge is an adaptive, debiased, and consistent LLM-as-a-Judge. The paper addresses three fundamental limitations in existing LLM-as-a-Judge systems: limited adaptivity to task and domain-specific evaluation criteria, systematic biases driven by non-semantic cues such as position, length, format, and model provenance, and evaluation inconsistency that leads to contradictory judgments across different evaluation modes (e.g., pointwise versus pairwise).\n\nUnlike prior approaches that treat the judge as a static evaluator, FairJudge models judging behavior itself as a learnable and regularized policy. The approach uses a curriculum-style SFT-DPO-GRPO training paradigm that progressively aligns rubric adherence, bias mitigation, and cross-mode consistency, while avoiding catastrophic forgetting. Experimental results on multiple internal and public benchmarks show that FairJudge consistently improves agreement and F1, reduces non-semantic biases, and outperforms substantially larger instruction-tuned LLMs.\n\nThe paper was published on February 6, 2026, and you can access it directly at https://arxiv.org/abs/2602.06625."
    ],
    "durationSeconds": 6.7829770819999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5dd1bd49-5d9c-4cca-a6b4-d2e09107ba7d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T03:32:38.669Z_

<details><summary>↩ Tool result · `toolu_01HeXA9Mpuivb5UHoDpbQYwL`</summary>

```text
Web search results for query: "SOS-Bench style over substance LLM judges ICLR 2025"

Links: [{"title":"[Literature Review] Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking","url":"https://www.themoonlight.io/en/review/style-outweighs-substance-failure-modes-of-llm-judges-in-alignment-benchmarking"},{"title":"(PDF) Style over Substance: Failure Modes of LLM Judges in Alignment Benchmarking","url":"https://www.researchgate.net/publication/384288829_Style_over_Substance_Failure_Modes_of_LLM_Judges_in_Alignment_Benchmarking"},{"title":"ICLR Poster Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking","url":"https://iclr.cc/virtual/2025/poster/29906"},{"title":"[Quick Review] Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking","url":"https://liner.com/review/style-outweighs-substance-failure-modes-of-llm-judges-in-alignment"},{"title":"Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking | OpenReview","url":"https://openreview.net/forum?id=MzHNftnAM1"},{"title":"Style Outweighs Substance: Failure Modes of LLM Judges in Alignment   Benchmarking","url":"https://arxiv.org/pdf/2409.15268"},{"title":"Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking","url":"https://arxiv.org/html/2409.15268v3"},{"title":"[2409.15268] Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking","url":"https://arxiv.org/abs/2409.15268"},{"title":"Style over Substance: Failure Modes of LLM Judges in Alignment Benchmarking","url":"https://arxiv.org/html/2409.15268v1"},{"title":"Paper page - Style over Substance: Failure Modes of LLM Judges in Alignment Benchmarking","url":"https://huggingface.co/papers/2409.15268"}]

Based on the search results, here's information about the SOS-Bench paper:

## Overview

The paper "Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking" was presented at the International Conference on Learning Representations (ICLR) in 2025. It was written by Benjamin Feuer et al.

## Key Findings

The research finds that (1) LLM-judge preferences do not correlate with concrete measures of safety, world knowledge, and instruction following; (2) LLM-judges have powerful implicit biases, prioritizing style over factuality and safety; and (3) the supervised fine-tuning (SFT) stage of post-training has a large impact on alignment, with data scaling and prompt diversity as the driving factors.

## The SOS-Bench Benchmark

The authors introduce a meta-benchmark, SOS-BENCH, which serves as a standardized framework for measuring LLM alignment based on established ground truths. SOS-Bench combines 19 existing world knowledge, instruction following, and safety benchmarks for a holistic view of model performance. The benchmark tests models on 152,380 data points; to the best of their knowledge, this is almost 7x larger than the largest previous open source LLM benchmark which end users can run themselves.

## Specific Bias Examples

Sarcasm, a minor violation of helpfulness, resulted in a 96% loss, while incorrect answers, a strong violation of honesty, only caused a 13% loss.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dee21660-0ce8-41ec-9f93-088e46df3189",
  "isSidechain": false,
  "promptId": "e0ade265-184d-408b-8e8a-4a4a7a9fb81f",
  "type": "user",
  "uuid": "c04c66ba-3380-466d-a931-20f56d6dc1ab",
  "toolUseResult": {
    "query": "SOS-Bench style over substance LLM judges ICLR 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_018p3yrW7cf56WDt5Z8MLBaJ",
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
      "Based on the search results, here's information about the SOS-Bench paper:\n\n## Overview\n\nThe paper \"Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking\" was presented at the International Conference on Learning Representations (ICLR) in 2025. It was written by Benjamin Feuer et al.\n\n## Key Findings\n\nThe research finds that (1) LLM-judge preferences do not correlate with concrete measures of safety, world knowledge, and instruction following; (2) LLM-judges have powerful implicit biases, prioritizing style over factuality and safety; and (3) the supervised fine-tuning (SFT) stage of post-training has a large impact on alignment, with data scaling and prompt diversity as the driving factors.\n\n## The SOS-Bench Benchmark\n\nThe authors introduce a meta-benchmark, SOS-BENCH, which serves as a standardized framework for measuring LLM alignment based on established ground truths. SOS-Bench combines 19 existing world knowledge, instruction following, and safety benchmarks for a holistic view of model performance. The benchmark tests models on 152,380 data points; to the best of their knowledge, this is almost 7x larger than the largest previous open source LLM benchmark which end users can run themselves.\n\n## Specific Bias Examples\n\nSarcasm, a minor violation of helpfulness, resulted in a 96% loss, while incorrect answers, a strong violation of honesty, only caused a 13% loss."
    ],
    "durationSeconds": 6.567777401000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "dee21660-0ce8-41ec-9f93-088e46df3189",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T03:32:38.733Z_

<details><summary>↩ Tool result · `toolu_01MePvPeb7mT4oxAf83kGpRT`</summary>

```text
Web search results for query: "LLM judge style bias debiasing 2025 2026 survey"

Links: [{"title":"Any Large Language Model Can Be a Reliable Judge: Debiasing with a Reasoning-based Bias Detector | OpenReview","url":"https://openreview.net/forum?id=sLNz60fJFF"},{"title":"LLM-as-a-Judge: Why Frontier Models Fail 50%+ Bias Tests | Adaline","url":"https://www.adaline.ai/blog/llm-as-a-judge-reliability-bias"},{"title":"[2604.23178] Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines","url":"https://arxiv.org/abs/2604.23178"},{"title":"A survey on LLM-as-a-judge - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2666675825004564"},{"title":"Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines","url":"https://arxiv.org/html/2604.23178v1"},{"title":"Rubric-Based Evaluations & LLM-as-a-Judge — Methodologies, Biases, and Empirical Validation in Domain-Specific Contexts. | by Adnan Masood, PhD. | Apr, 2026 | Medium","url":"https://medium.com/@adnanmasood/rubric-based-evals-llm-as-a-judge-methodologies-and-empirical-validation-in-domain-context-71936b989e80"},{"title":"The Silent Judge: Unacknowledged Shortcut Bias in LLM-as-a-Judge","url":"https://arxiv.org/pdf/2509.26072"},{"title":"Evaluating Scoring Bias in LLM-as-a-Judge","url":"https://arxiv.org/html/2506.22316v1"},{"title":"Mitigating the Bias of Large Language Model Evaluation","url":"https://arxiv.org/pdf/2409.16788"}]

Based on the search results, here's what recent research shows about LLM judge style bias and debiasing:

## Key Findings on Style Bias

Style bias is the dominant bias (0.76–0.92 across all models), far exceeding position bias (≤0.04), yet has received minimal research attention. This represents a significant shift in understanding LLM judge limitations, as position bias is now negligible across all tested models.

## Recent Survey Work

A comprehensive survey available online in January 2026 provides a systematic framework for building reliable LLM-as-a-judge systems, addressing how ensuring reliability and reducing biases remain significant challenges for practical deployment.

## Debiasing Strategies and Results

Recent comprehensive empirical studies compare nine debiasing strategies across five judge models from four provider families (Google, Anthropic, OpenAI, Meta) and four bias types. Debiasing strategies show model-dependent benefits, with the combined budget strategy significantly improving Claude Sonnet 4 by +11.2 percentage points (p < 0.0001).

Additional debiasing approaches include: chain-of-thought prompting to improve evaluation quality, debiased training data to reduce bias in fine-tuned evaluators, and wider/deeper model panels to produce fairer evaluations.

## Emerging Methodological Frontiers

Two 2025–2026 lines of work focus on calibration-based bias correction with confidence intervals accounting for imperfect judge sensitivity and specificity, and applying item response theory to frame reliability as a property of the measurement instrument.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "104db327-628b-48ff-bc7b-761d851c2957",
  "isSidechain": false,
  "promptId": "e0ade265-184d-408b-8e8a-4a4a7a9fb81f",
  "type": "user",
  "uuid": "6cba611f-ba4f-46bf-ba3d-8d290b375669",
  "toolUseResult": {
    "query": "LLM judge style bias debiasing 2025 2026 survey",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WkuW8ZtoTzEeFvotikuZVP",
        "content": [
          {
            "title": "Any Large Language Model Can Be a Reliable Judge: Debiasing with a Reasoning-based Bias Detector | OpenReview",
            "url": "https://openreview.net/forum?id=sLNz60fJFF"
          },
          {
            "title": "LLM-as-a-Judge: Why Frontier Models Fail 50%+ Bias Tests | Adaline",
            "url": "https://www.adaline.ai/blog/llm-as-a-judge-reliability-bias"
          },
          {
            "title": "[2604.23178] Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines",
            "url": "https://arxiv.org/abs/2604.23178"
          },
          {
            "title": "A survey on LLM-as-a-judge - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S2666675825004564"
          },
          {
            "title": "Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines",
            "url": "https://arxiv.org/html/2604.23178v1"
          },
          {
            "title": "Rubric-Based Evaluations & LLM-as-a-Judge — Methodologies, Biases, and Empirical Validation in Domain-Specific Contexts. | by Adnan Masood, PhD. | Apr, 2026 | Medium",
            "url": "https://medium.com/@adnanmasood/rubric-based-evals-llm-as-a-judge-methodologies-and-empirical-validation-in-domain-context-71936b989e80"
          },
          {
            "title": "The Silent Judge: Unacknowledged Shortcut Bias in LLM-as-a-Judge",
            "url": "https://arxiv.org/pdf/2509.26072"
          },
          {
            "title": "Evaluating Scoring Bias in LLM-as-a-Judge",
            "url": "https://arxiv.org/html/2506.22316v1"
          },
          {
            "title": "Mitigating the Bias of Large Language Model Evaluation",
            "url": "https://arxiv.org/pdf/2409.16788"
          }
        ]
      },
      "Based on the search results, here's what recent research shows about LLM judge style bias and debiasing:\n\n## Key Findings on Style Bias\n\nStyle bias is the dominant bias (0.76–0.92 across all models), far exceeding position bias (≤0.04), yet has received minimal research attention. This represents a significant shift in understanding LLM judge limitations, as position bias is now negligible across all tested models.\n\n## Recent Survey Work\n\nA comprehensive survey available online in January 2026 provides a systematic framework for building reliable LLM-as-a-judge systems, addressing how ensuring reliability and reducing biases remain significant challenges for practical deployment.\n\n## Debiasing Strategies and Results\n\nRecent comprehensive empirical studies compare nine debiasing strategies across five judge models from four provider families (Google, Anthropic, OpenAI, Meta) and four bias types. Debiasing strategies show model-dependent benefits, with the combined budget strategy significantly improving Claude Sonnet 4 by +11.2 percentage points (p < 0.0001).\n\nAdditional debiasing approaches include: chain-of-thought prompting to improve evaluation quality, debiased training data to reduce bias in fine-tuned evaluators, and wider/deeper model panels to produce fairer evaluations.\n\n## Emerging Methodological Frontiers\n\nTwo 2025–2026 lines of work focus on calibration-based bias correction with confidence intervals accounting for imperfect judge sensitivity and specificity, and applying item response theory to frame reliability as a property of the measurement instrument."
    ],
    "durationSeconds": 8.045906361,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "104db327-628b-48ff-bc7b-761d851c2957",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Causal Style Decomposition for LLM Judge Debiasing via Doubly-Robust Counterfactual Estimation  ## Description S…",
  "leafUuid": "6cba611f-ba4f-46bf-ba3d-8d290b375669",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate causal style decomposition for LLM judge debiasing",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197"
}
```

---

### Tool result

_source line 23 · 2026-05-20T03:32:39.889Z_

<details><summary>↩ Tool result · `toolu_01LcJjqSNXMk9SzLaxFPhwSG`</summary>

```text
Web search results for query: "Double Machine Learning causal inference text NLP debiasing 2025 2026"

Links: [{"title":"Introduction to Causal Inference: Double Machine Learning | Carlos Mendez","url":"https://carlos-mendez.org/post/python_doubleml/"},{"title":"Bayesian Double Machine Learning for Causal Inference","url":"https://www.researchgate.net/publication/394540063_Bayesian_Double_Machine_Learning_for_Causal_Inference"},{"title":"Double Machine Learning for Causal Inference under Shared-State Interference","url":"https://ideas.repec.org/p/arx/papers/2504.08836.html"},{"title":"Anytime-Valid Inference for Double/Debiased Machine Learning of Causal   Parameters","url":"https://arxiv.org/pdf/2408.09598"},{"title":"Reading Between the Lines: Deconfounding Causal Estimates using Text Embeddings and Deep Learning","url":"https://arxiv.org/pdf/2601.01511"},{"title":"Full article: Double Debiased Machine Learning Nonparametric Inference with Continuous Treatments","url":"https://www.tandfonline.com/doi/full/10.1080/07350015.2025.2505487"},{"title":"1. The basics of double/debiased machine learning — DoubleML documentation","url":"https://docs.doubleml.org/stable/guide/basics.html"},{"title":"DoubleML -- An Object-Oriented Implementation of Double Machine Learning   in R","url":"https://arxiv.org/pdf/2103.09603"},{"title":"Bayesian Double Machine Learning for Causal InferenceWe thank Otilia Boldea, Neal Shephard, and seminar participants at York and the Frank Diebold 65+35 Conference for helpful comments and suggestions. We thank Lasse von der Heydt for excellent research assistance.","url":"https://arxiv.org/html/2508.12688v1"}]

Based on the search results, I found several relevant recent works on Double Machine Learning (DML), causal inference, NLP, and debiasing from 2025-2026:

## Key Recent Developments:

**Text-Based Deconfounding with Neural Networks:**
A Neural Network-Enhanced Double Machine Learning framework has been proposed to leverage text embeddings for causal identification, addressing a critical gap in causal inference. High-dimensional unstructured text often contains rich proxies for latent confounding variables when traditional econometric methods struggle.

**Bayesian Approaches to DML:**
A fully-Bayesian approach for causal inference in partially linear models with high-dimensional control variables has been developed. By orthogonalizing the moment condition with respect to the nuisance parameter, DML inoculates against regularization bias to first order.

**Extending DML Methodologies:**
Recent work on Double Machine Learning for Causal Inference under Shared-State Interference has been published in 2025, expanding the framework's applicability. Additionally, anytime-valid inference for Double/Debiased Machine Learning addresses the limitation that the classic framework is only valid asymptotically for predetermined sample sizes.

**Continuous Treatment Effects:**
A doubly robust inference method for causal effects of continuous treatment variables has been proposed, under unconfoundedness and with nonparametric or high-dimensional nuisance functions.

These developments represent significant advances in combining DML with NLP, neural network approaches, and Bayesian methods for improved causal inference and debiasing.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2fb3f6f4-cc98-4771-a53e-a979f5cd0877",
  "isSidechain": false,
  "promptId": "e0ade265-184d-408b-8e8a-4a4a7a9fb81f",
  "type": "user",
  "uuid": "cb8abe49-2e6a-40a6-b1e0-267751c72745",
  "toolUseResult": {
    "query": "Double Machine Learning causal inference text NLP debiasing 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LXM1uCk1o4tPsaTnGQVdiq",
        "content": [
          {
            "title": "Introduction to Causal Inference: Double Machine Learning | Carlos Mendez",
            "url": "https://carlos-mendez.org/post/python_doubleml/"
          },
          {
            "title": "Bayesian Double Machine Learning for Causal Inference",
            "url": "https://www.researchgate.net/publication/394540063_Bayesian_Double_Machine_Learning_for_Causal_Inference"
          },
          {
            "title": "Double Machine Learning for Causal Inference under Shared-State Interference",
            "url": "https://ideas.repec.org/p/arx/papers/2504.08836.html"
          },
          {
            "title": "Anytime-Valid Inference for Double/Debiased Machine Learning of Causal   Parameters",
            "url": "https://arxiv.org/pdf/2408.09598"
          },
          {
            "title": "Reading Between the Lines: Deconfounding Causal Estimates using Text Embeddings and Deep Learning",
            "url": "https://arxiv.org/pdf/2601.01511"
          },
          {
            "title": "Full article: Double Debiased Machine Learning Nonparametric Inference with Continuous Treatments",
            "url": "https://www.tandfonline.com/doi/full/10.1080/07350015.2025.2505487"
          },
          {
            "title": "1. The basics of double/debiased machine learning — DoubleML documentation",
            "url": "https://docs.doubleml.org/stable/guide/basics.html"
          },
          {
            "title": "DoubleML -- An Object-Oriented Implementation of Double Machine Learning   in R",
            "url": "https://arxiv.org/pdf/2103.09603"
          },
          {
            "title": "Bayesian Double Machine Learning for Causal InferenceWe thank Otilia Boldea, Neal Shephard, and seminar participants at York and the Frank Diebold 65+35 Conference for helpful comments and suggestions. We thank Lasse von der Heydt for excellent research assistance.",
            "url": "https://arxiv.org/html/2508.12688v1"
          }
        ]
      },
      "Based on the search results, I found several relevant recent works on Double Machine Learning (DML), causal inference, NLP, and debiasing from 2025-2026:\n\n## Key Recent Developments:\n\n**Text-Based Deconfounding with Neural Networks:**\nA Neural Network-Enhanced Double Machine Learning framework has been proposed to leverage text embeddings for causal identification, addressing a critical gap in causal inference. High-dimensional unstructured text often contains rich proxies for latent confounding variables when traditional econometric methods struggle.\n\n**Bayesian Approaches to DML:**\nA fully-Bayesian approach for causal inference in partially linear models with high-dimensional control variables has been developed. By orthogonalizing the moment condition with respect to the nuisance parameter, DML inoculates against regularization bias to first order.\n\n**Extending DML Methodologies:**\nRecent work on Double Machine Learning for Causal Inference under Shared-State Interference has been published in 2025, expanding the framework's applicability. Additionally, anytime-valid inference for Double/Debiased Machine Learning addresses the limitation that the classic framework is only valid asymptotically for predetermined sample sizes.\n\n**Continuous Treatment Effects:**\nA doubly robust inference method for causal effects of continuous treatment variables has been proposed, under unconfoundedness and with nonparametric or high-dimensional nuisance functions.\n\nThese developments represent significant advances in combining DML with NLP, neural network approaches, and Bayesian methods for improved causal inference and debiasing."
    ],
    "durationSeconds": 7.131202362000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2fb3f6f4-cc98-4771-a53e-a979f5cd0877",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T03:32:42.436Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LBqRY2YYn7cAgW9fWNWeFn`</summary>

```json
{
  "query": "Length-Controlled AlpacaEval debiasing ICLR 2025 post-hoc regression"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb8abe49-2e6a-40a6-b1e0-267751c72745",
  "isSidechain": false,
  "requestId": "req_011CbD7i248ZDUogy5zYed16",
  "type": "assistant",
  "uuid": "f79ec9ad-f76d-445f-a13b-9b1949e6ae2e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J7aDgx8JKhxCoy1263eouW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4434,
      "cache_read_input_tokens": 20790,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4434,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 20790,
          "cache_creation_input_tokens": 4434,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4434
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

_source line 25 · 2026-05-20T03:32:43.373Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AAZ7ixmt3q2rFK98GxC9ia`</summary>

```json
{
  "query": "Bias-Bounded Evaluation LLM judge differential privacy 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f79ec9ad-f76d-445f-a13b-9b1949e6ae2e",
  "isSidechain": false,
  "requestId": "req_011CbD7i248ZDUogy5zYed16",
  "type": "assistant",
  "uuid": "f0e1ed33-8c3f-491f-9b23-e96380c5117b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J7aDgx8JKhxCoy1263eouW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4434,
      "cache_read_input_tokens": 20790,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4434,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 20790,
          "cache_creation_input_tokens": 4434,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4434
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

_source line 26 · 2026-05-20T03:32:44.626Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017ogyd4CrxmcBJwkieBq8hV`</summary>

```json
{
  "query": "causal counterfactual style transfer text rewriting debiasing LLM evaluation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0e1ed33-8c3f-491f-9b23-e96380c5117b",
  "isSidechain": false,
  "requestId": "req_011CbD7i248ZDUogy5zYed16",
  "type": "assistant",
  "uuid": "34b84652-2848-49dc-aa3e-81c129053698",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J7aDgx8JKhxCoy1263eouW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4434,
      "cache_read_input_tokens": 20790,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4434,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 20790,
          "cache_creation_input_tokens": 4434,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4434
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

_source line 27 · 2026-05-20T03:32:49.261Z_

<details><summary>↩ Tool result · `toolu_01LBqRY2YYn7cAgW9fWNWeFn`</summary>

```text
Web search results for query: "Length-Controlled AlpacaEval debiasing ICLR 2025 post-hoc regression"

Links: [{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2410.04203"},{"title":"Post-Hoc Reward Calibration: A Case Study on Length Bias","url":"https://iclr.cc/media/iclr-2025/Slides/30144.pdf"},{"title":"Length-Controlled AlpacaEval: A Simple Way to Debias Automatic   Evaluators","url":"https://arxiv.org/pdf/2404.04475"},{"title":"Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators","url":"https://arxiv.org/html/2404.04475v2"},{"title":"[2404.04475] Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators","url":"https://arxiv.org/abs/2404.04475"},{"title":"Length-Controlled AlpacaEval - A Simple Way to Debias Automatic Evaluators","url":"https://hyunyoung2.github.io/2024/07/20/alpacaEval2/"},{"title":"Published as a conference paper at COLM 2024 Length-Controlled AlpacaEval:","url":"https://openreview.net/pdf/76a4afefba676b543f4c4ca61529f92e828e171f.pdf"}]

I found relevant information about Length-Controlled AlpacaEval and debiasing. Here's what the search results reveal:

## Length-Controlled AlpacaEval

Length Controlled (LC) Win Rate is a debiased version of the AlpacaEval Win Rate that controls for the length of outputs and increases correlation to Chat Arena.

## The Problem Being Addressed

One of the major issues of AlpacaEval is that one can increase the win-rate by increasing the length of outputs.

## Methodology: Post-Hoc Regression

The main idea of Length Controlled Win Rate is that for each model, AlpacaEval2 fits a logistic regression to predict the preference of the autoannotator given: (1) the instruction, (2) the model, and (3) the difference of length between the baseline and model output. AlpacaEval2 can then predict the counterfactual "what would the preference be if the model's output had the same length as the baseline" by setting the length difference to 0.

## Results

Length controlled win-rates increase the correlation between AlpacaEval's leaderboard and Chat Arena from 0.93 to 0.98 Spearman correlation, while significantly decreasing the length gameability.

## ICLR 2025 Connection

Testing with four LLM-RM configurations, there are consistent improvements in AlpacaEval2 Length-controlled win rates, with this approach being presented at ICLR 2025 in the context of post-hoc reward calibration for addressing length bias.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f79ec9ad-f76d-445f-a13b-9b1949e6ae2e",
  "isSidechain": false,
  "promptId": "e0ade265-184d-408b-8e8a-4a4a7a9fb81f",
  "type": "user",
  "uuid": "569561c4-5364-45de-9bbb-10ff819f01b7",
  "toolUseResult": {
    "query": "Length-Controlled AlpacaEval debiasing ICLR 2025 post-hoc regression",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KTVMGEPQSy7XindzzcrcC1",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://arxiv.org/pdf/2410.04203"
          },
          {
            "title": "Post-Hoc Reward Calibration: A Case Study on Length Bias",
            "url": "https://iclr.cc/media/iclr-2025/Slides/30144.pdf"
          },
          {
            "title": "Length-Controlled AlpacaEval: A Simple Way to Debias Automatic   Evaluators",
            "url": "https://arxiv.org/pdf/2404.04475"
          },
          {
            "title": "Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators",
            "url": "https://arxiv.org/html/2404.04475v2"
          },
          {
            "title": "[2404.04475] Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators",
            "url": "https://arxiv.org/abs/2404.04475"
          },
          {
            "title": "Length-Controlled AlpacaEval - A Simple Way to Debias Automatic Evaluators",
            "url": "https://hyunyoung2.github.io/2024/07/20/alpacaEval2/"
          },
          {
            "title": "Published as a conference paper at COLM 2024 Length-Controlled AlpacaEval:",
            "url": "https://openreview.net/pdf/76a4afefba676b543f4c4ca61529f92e828e171f.pdf"
          }
        ]
      },
      "I found relevant information about Length-Controlled AlpacaEval and debiasing. Here's what the search results reveal:\n\n## Length-Controlled AlpacaEval\n\nLength Controlled (LC) Win Rate is a debiased version of the AlpacaEval Win Rate that controls for the length of outputs and increases correlation to Chat Arena.\n\n## The Problem Being Addressed\n\nOne of the major issues of AlpacaEval is that one can increase the win-rate by increasing the length of outputs.\n\n## Methodology: Post-Hoc Regression\n\nThe main idea of Length Controlled Win Rate is that for each model, AlpacaEval2 fits a logistic regression to predict the preference of the autoannotator given: (1) the instruction, (2) the model, and (3) the difference of length between the baseline and model output. AlpacaEval2 can then predict the counterfactual \"what would the preference be if the model's output had the same length as the baseline\" by setting the length difference to 0.\n\n## Results\n\nLength controlled win-rates increase the correlation between AlpacaEval's leaderboard and Chat Arena from 0.93 to 0.98 Spearman correlation, while significantly decreasing the length gameability.\n\n## ICLR 2025 Connection\n\nTesting with four LLM-RM configurations, there are consistent improvements in AlpacaEval2 Length-controlled win rates, with this approach being presented at ICLR 2025 in the context of post-hoc reward calibration for addressing length bias."
    ],
    "durationSeconds": 6.8207627409999985,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f79ec9ad-f76d-445f-a13b-9b1949e6ae2e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T03:32:50.664Z_

<details><summary>↩ Tool result · `toolu_01AAZ7ixmt3q2rFK98GxC9ia`</summary>

```text
Web search results for query: "Bias-Bounded Evaluation LLM judge differential privacy 2026 arXiv"

Links: [{"title":"[2603.05485] Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation","url":"https://arxiv.org/abs/2603.05485"},{"title":"Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation","url":"https://arxiv.org/html/2603.05485"},{"title":"Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation","url":"https://arxiv.org/pdf/2603.05485"},{"title":"[2506.22316] Evaluating Scoring Bias in LLM-as-a-Judge","url":"https://arxiv.org/abs/2506.22316"},{"title":"[2604.23178] Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines","url":"https://arxiv.org/abs/2604.23178"},{"title":"[2603.08091] Toward Robust LLM-Based Judges: Taxonomic Bias Evaluation and Debiasing Optimization","url":"https://arxiv.org/abs/2603.08091"},{"title":"[2603.08091v1] Toward Robust LLM-Based Judges: Taxonomic Bias Evaluation and Debiasing Optimization","url":"https://arxiv.org/abs/2603.08091v1"}]

I found research on your topic! Here are the key results:

## Primary Result: Bias-Bounded Evaluation

The main paper is "Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation" (arXiv 2603.05485), posted March 5, 2026.

**Core Contribution:**
The paper proposes average bias-boundedness (A-BB), an algorithmic framework which formally guarantees reductions of harm/impact as a result of any measurable bias in an LLM judge. BBE injects calibrated Gaussian noise to the judge's scores to mitigate the effects of the bias, using the A-BB mechanism.

**Connection to Differential Privacy:**
The mechanism takes inspiration from techniques in differential privacy, though the analysis differs substantially, as does the goal.

**Results:**
Evaluating on Arena-Hard-Auto with four LLM judges, the work achieves (τ=0.5, δ=0.01)-bias-bounded guarantees while retaining 61–99% correlation with original rankings across formatting and schematic bias settings.

## Related Papers

The search also found several related 2026 arXiv papers on LLM judge bias mitigation that may be of interest, including work on taxonomic bias evaluation and systematic evaluation of debiasing strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0e1ed33-8c3f-491f-9b23-e96380c5117b",
  "isSidechain": false,
  "promptId": "e0ade265-184d-408b-8e8a-4a4a7a9fb81f",
  "type": "user",
  "uuid": "7621232b-220c-4232-8c93-537a9f636175",
  "toolUseResult": {
    "query": "Bias-Bounded Evaluation LLM judge differential privacy 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EcQREUgotr9tpVKzu2PWCJ",
        "content": [
          {
            "title": "[2603.05485] Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation",
            "url": "https://arxiv.org/abs/2603.05485"
          },
          {
            "title": "Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation",
            "url": "https://arxiv.org/html/2603.05485"
          },
          {
            "title": "Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation",
            "url": "https://arxiv.org/pdf/2603.05485"
          },
          {
            "title": "[2506.22316] Evaluating Scoring Bias in LLM-as-a-Judge",
            "url": "https://arxiv.org/abs/2506.22316"
          },
          {
            "title": "[2604.23178] Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines",
            "url": "https://arxiv.org/abs/2604.23178"
          },
          {
            "title": "[2603.08091] Toward Robust LLM-Based Judges: Taxonomic Bias Evaluation and Debiasing Optimization",
            "url": "https://arxiv.org/abs/2603.08091"
          },
          {
            "title": "[2603.08091v1] Toward Robust LLM-Based Judges: Taxonomic Bias Evaluation and Debiasing Optimization",
            "url": "https://arxiv.org/abs/2603.08091v1"
          }
        ]
      },
      "I found research on your topic! Here are the key results:\n\n## Primary Result: Bias-Bounded Evaluation\n\nThe main paper is \"Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation\" (arXiv 2603.05485), posted March 5, 2026.\n\n**Core Contribution:**\nThe paper proposes average bias-boundedness (A-BB), an algorithmic framework which formally guarantees reductions of harm/impact as a result of any measurable bias in an LLM judge. BBE injects calibrated Gaussian noise to the judge's scores to mitigate the effects of the bias, using the A-BB mechanism.\n\n**Connection to Differential Privacy:**\nThe mechanism takes inspiration from techniques in differential privacy, though the analysis differs substantially, as does the goal.\n\n**Results:**\nEvaluating on Arena-Hard-Auto with four LLM judges, the work achieves (τ=0.5, δ=0.01)-bias-bounded guarantees while retaining 61–99% correlation with original rankings across formatting and schematic bias settings.\n\n## Related Papers\n\nThe search also found several related 2026 arXiv papers on LLM judge bias mitigation that may be of interest, including work on taxonomic bias evaluation and systematic evaluation of debiasing strategies."
    ],
    "durationSeconds": 7.286576779999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f0e1ed33-8c3f-491f-9b23-e96380c5117b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-20T03:32:52.852Z_

<details><summary>↩ Tool result · `toolu_017ogyd4CrxmcBJwkieBq8hV`</summary>

```text
Web search results for query: "causal counterfactual style transfer text rewriting debiasing LLM evaluation 2025 2026"

Links: [{"title":"Towards Controllable and Explainable Text Generation via Causal Intervention in LLMs","url":"https://www.mdpi.com/2079-9292/14/16/3279"},{"title":"Counterfactual LLM-based Framework for Measuring Rhetorical Style","url":"https://arxiv.org/html/2512.19908v1"},{"title":"On the Eligibility of LLMs for Counterfactual Reasoning","url":"https://arxiv.org/pdf/2505.11839"},{"title":"Estimating Causal Effects of Text Interventions Leveraging LLMs","url":"https://arxiv.org/pdf/2410.21474"},{"title":"RAZOR: Sharpening Knowledge by Cutting Bias with Unsupervised Text   Rewriting","url":"https://arxiv.org/pdf/2412.07675"},{"title":"Causal-Guided Active Learning for Debiasing Large Language Models","url":"https://arxiv.org/pdf/2408.12942"},{"title":"Benchmarking and Pushing the Multi-Bias Elimination Boundary of LLMs via Causal Effect Estimation-guided Debiasing","url":"https://arxiv.org/pdf/2505.16522"},{"title":"Information Gain-Guided Causal Intervention for Autonomous Debiasing Large Language Models","url":"https://arxiv.org/pdf/2504.12898"}]

I found several relevant research papers on these interconnected topics from 2025-2026. Here are the key findings:

## Controllable Text Generation with Causal Intervention

A structural causal intervention framework models input-hidden-output dependencies through a structural causal model and performs targeted interventions on hidden representations, combining counterfactual sample construction with contrastive training to enable precise control of style, sentiment, and factual consistency. This approach achieves style transfer accuracy of 92.3% (+7–14 percentage points over strong baselines) and sentiment-controlled generation accuracy of 90.1%.

## Counterfactual LLM-based Measurement Framework

A counterfactual LLM-based framework uses multiple LLM rhetorical personas to generate counterfactual writings from the same substantive content, with an LLM judge comparing them through pairwise evaluations, applied to 8,485 ICLR submissions sampled from 2017 to 2025, generating more than 250,000 counterfactual writings.

## LLM Counterfactual Reasoning Evaluation

Counterfactual reasoning refers to the ability to adjust responses when presented with modified premises, and investigating this capability of LLMs provides an interpretable step to understand their adaptability under hypothetical alterations to input conditions.

## Debiasing through Text Rewriting

CLEVER leverages counterfactual inference for debiasing in fact-checking tasks by training two models—a claim-evidence fusion model and a claim-only model—and then subtracting the output of the claim-only model from the fusion model to isolate and remove biases.

## Multi-Bias Elimination and Causal Effects

LLMs learn bias during training leading to poor generalizability, making it crucial to assess LLMs' generalizability with respect to biases and explore effective debiasing solutions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34b84652-2848-49dc-aa3e-81c129053698",
  "isSidechain": false,
  "promptId": "e0ade265-184d-408b-8e8a-4a4a7a9fb81f",
  "type": "user",
  "uuid": "fa1ad234-8c5a-4f53-a6bf-05c7008e0311",
  "toolUseResult": {
    "query": "causal counterfactual style transfer text rewriting debiasing LLM evaluation 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JofoJAqo6RqMEjNPgZTUs6",
        "content": [
          {
            "title": "Towards Controllable and Explainable Text Generation via Causal Intervention in LLMs",
            "url": "https://www.mdpi.com/2079-9292/14/16/3279"
          },
          {
            "title": "Counterfactual LLM-based Framework for Measuring Rhetorical Style",
            "url": "https://arxiv.org/html/2512.19908v1"
          },
          {
            "title": "On the Eligibility of LLMs for Counterfactual Reasoning",
            "url": "https://arxiv.org/pdf/2505.11839"
          },
          {
            "title": "Estimating Causal Effects of Text Interventions Leveraging LLMs",
            "url": "https://arxiv.org/pdf/2410.21474"
          },
          {
            "title": "RAZOR: Sharpening Knowledge by Cutting Bias with Unsupervised Text   Rewriting",
            "url": "https://arxiv.org/pdf/2412.07675"
          },
          {
            "title": "Causal-Guided Active Learning for Debiasing Large Language Models",
            "url": "https://arxiv.org/pdf/2408.12942"
          },
          {
            "title": "Benchmarking and Pushing the Multi-Bias Elimination Boundary of LLMs via Causal Effect Estimation-guided Debiasing",
            "url": "https://arxiv.org/pdf/2505.16522"
          },
          {
            "title": "Information Gain-Guided Causal Intervention for Autonomous Debiasing Large Language Models",
            "url": "https://arxiv.org/pdf/2504.12898"
          }
        ]
      },
      "I found several relevant research papers on these interconnected topics from 2025-2026. Here are the key findings:\n\n## Controllable Text Generation with Causal Intervention\n\nA structural causal intervention framework models input-hidden-output dependencies through a structural causal model and performs targeted interventions on hidden representations, combining counterfactual sample construction with contrastive training to enable precise control of style, sentiment, and factual consistency. This approach achieves style transfer accuracy of 92.3% (+7–14 percentage points over strong baselines) and sentiment-controlled generation accuracy of 90.1%.\n\n## Counterfactual LLM-based Measurement Framework\n\nA counterfactual LLM-based framework uses multiple LLM rhetorical personas to generate counterfactual writings from the same substantive content, with an LLM judge comparing them through pairwise evaluations, applied to 8,485 ICLR submissions sampled from 2017 to 2025, generating more than 250,000 counterfactual writings.\n\n## LLM Counterfactual Reasoning Evaluation\n\nCounterfactual reasoning refers to the ability to adjust responses when presented with modified premises, and investigating this capability of LLMs provides an interpretable step to understand their adaptability under hypothetical alterations to input conditions.\n\n## Debiasing through Text Rewriting\n\nCLEVER leverages counterfactual inference for debiasing in fact-checking tasks by training two models—a claim-evidence fusion model and a claim-only model—and then subtracting the output of the claim-only model from the fusion model to isolate and remove biases.\n\n## Multi-Bias Elimination and Causal Effects\n\nLLMs learn bias during training leading to poor generalizability, making it crucial to assess LLMs' generalizability with respect to biases and explore effective debiasing solutions."
    ],
    "durationSeconds": 8.223745374000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "34b84652-2848-49dc-aa3e-81c129053698",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-20T03:32:52.857Z_

```json
{
  "parentUuid": "fa1ad234-8c5a-4f53-a6bf-05c7008e0311",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "1d2dcb61-55a1-43e1-9724-0be080027abb",
  "timestamp": "2026-05-20T03:32:52.857Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 31 · 2026-05-20T03:32:57.057Z_

<details><summary>Logged reasoning block</summary>

```text
Let me do a couple more targeted searches to understand the competitive landscape better, particularly around: (1) whether anyone has already proposed using causal methods specifically for LLM judge debiasing in a black-box setting, (2) the CASSE paper, and (3) any very recent works that might overlap with this proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d2dcb61-55a1-43e1-9724-0be080027abb",
  "isSidechain": false,
  "requestId": "req_011CbD7iyUNpfnwj5gEe2ySC",
  "type": "assistant",
  "uuid": "9ca1ca2e-6f09-4e22-b024-4b9b9ed5dd23",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FVwfD4twFTk4S9zkNxYZNR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2680,
      "cache_read_input_tokens": 25224,
      "output_tokens": 265,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2680,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 265,
          "cache_read_input_tokens": 25224,
          "cache_creation_input_tokens": 2680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2680
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

_source line 32 · 2026-05-20T03:32:58.493Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015uFkc2wXU8AQVHQZt7f4qC`</summary>

```json
{
  "query": "CASSE \"concise agent less expert\" style features conversational agents arXiv 2601.10809"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ca1ca2e-6f09-4e22-b024-4b9b9ed5dd23",
  "isSidechain": false,
  "requestId": "req_011CbD7iyUNpfnwj5gEe2ySC",
  "type": "assistant",
  "uuid": "27659b56-9da5-4f57-b8d3-237d59d22074",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FVwfD4twFTk4S9zkNxYZNR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2680,
      "cache_read_input_tokens": 25224,
      "output_tokens": 265,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2680,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 265,
          "cache_read_input_tokens": 25224,
          "cache_creation_input_tokens": 2680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2680
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

_source line 33 · 2026-05-20T03:32:59.130Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ag1vcBSQZNuGA3maJwXAN4`</summary>

```json
{
  "query": "\"Preference Leakage\" LLM judge contamination ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27659b56-9da5-4f57-b8d3-237d59d22074",
  "isSidechain": false,
  "requestId": "req_011CbD7iyUNpfnwj5gEe2ySC",
  "type": "assistant",
  "uuid": "1fc23366-287e-4f09-81b4-b36a655899eb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FVwfD4twFTk4S9zkNxYZNR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2680,
      "cache_read_input_tokens": 25224,
      "output_tokens": 265,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2680,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 265,
          "cache_read_input_tokens": 25224,
          "cache_creation_input_tokens": 2680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2680
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

_source line 34 · 2026-05-20T03:32:59.836Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A741s5pSYbH8zCUp75bvBS`</summary>

```json
{
  "query": "CoRL 2026 2027 robot learning conference call for papers deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1fc23366-287e-4f09-81b4-b36a655899eb",
  "isSidechain": false,
  "requestId": "req_011CbD7iyUNpfnwj5gEe2ySC",
  "type": "assistant",
  "uuid": "d4f1bf5d-a06d-4b61-9725-e9ff6fae9f32",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FVwfD4twFTk4S9zkNxYZNR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2680,
      "cache_read_input_tokens": 25224,
      "output_tokens": 265,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2680,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 265,
          "cache_read_input_tokens": 25224,
          "cache_creation_input_tokens": 2680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2680
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
  "leafUuid": "d4f1bf5d-a06d-4b61-9725-e9ff6fae9f32",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate causal style decomposition for LLM judge debiasing",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197"
}
```

---

### Tool result

_source line 37 · 2026-05-20T03:33:04.045Z_

<details><summary>↩ Tool result · `toolu_015uFkc2wXU8AQVHQZt7f4qC`</summary>

```text
Web search results for query: "CASSE "concise agent less expert" style features conversational agents arXiv 2601.10809"

Links: [{"title":"[2601.10809] A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents","url":"https://arxiv.org/abs/2601.10809"},{"title":"A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents","url":"https://arxiv.org/html/2601.10809"},{"title":"A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents","url":"https://arxiv.org/pdf/2601.10809"},{"title":"Responses of Conversational Agents to Health and Lifestyle Prompts: Investigation of Appropriateness and Presentation Structures","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7055771/"},{"title":"Synthesis of personalized conversational automation agents","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12555571"}]

Perfect! I found the paper you're looking for. Here are the key details:

**Paper Title:** "A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents"

**What is CASSE?** CASSE (Conversational Agent Stylistic Side Effects) is a dataset capturing complex interactions between style features. More specifically, the dataset includes 12,200 synthetically generated messages annotated with 12 style features.

**Main Research Focus:** The work presents the first systematic study of cross-feature stylistic side effects, conducting a comprehensive survey of 127 conversational agent papers from ACL Anthology and identifying 12 frequently used style features.

**Key Findings:** The results reveal consistent and structured side effects, such as prompting for conciseness significantly reducing perceived expertise, and demonstrate that style features are deeply entangled rather than orthogonal.

The paper was published on January 15, 2026, and is available on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27659b56-9da5-4f57-b8d3-237d59d22074",
  "isSidechain": false,
  "promptId": "e0ade265-184d-408b-8e8a-4a4a7a9fb81f",
  "type": "user",
  "uuid": "e000f5d1-8bbe-4c44-a243-7b344b313237",
  "toolUseResult": {
    "query": "CASSE \"concise agent less expert\" style features conversational agents arXiv 2601.10809",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RChHzzi61i8KbYfrio99Fh",
        "content": [
          {
            "title": "[2601.10809] A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents",
            "url": "https://arxiv.org/abs/2601.10809"
          },
          {
            "title": "A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents",
            "url": "https://arxiv.org/html/2601.10809"
          },
          {
            "title": "A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents",
            "url": "https://arxiv.org/pdf/2601.10809"
          },
          {
            "title": "Responses of Conversational Agents to Health and Lifestyle Prompts: Investigation of Appropriateness and Presentation Structures",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7055771/"
          },
          {
            "title": "Synthesis of personalized conversational automation agents",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12555571"
          }
        ]
      },
      "Perfect! I found the paper you're looking for. Here are the key details:\n\n**Paper Title:** \"A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents\"\n\n**What is CASSE?** CASSE (Conversational Agent Stylistic Side Effects) is a dataset capturing complex interactions between style features. More specifically, the dataset includes 12,200 synthetically generated messages annotated with 12 style features.\n\n**Main Research Focus:** The work presents the first systematic study of cross-feature stylistic side effects, conducting a comprehensive survey of 127 conversational agent papers from ACL Anthology and identifying 12 frequently used style features.\n\n**Key Findings:** The results reveal consistent and structured side effects, such as prompting for conciseness significantly reducing perceived expertise, and demonstrate that style features are deeply entangled rather than orthogonal.\n\nThe paper was published on January 15, 2026, and is available on arXiv."
    ],
    "durationSeconds": 5.547432158999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "27659b56-9da5-4f57-b8d3-237d59d22074",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T03:33:04.686Z_

<details><summary>↩ Tool result · `toolu_01A741s5pSYbH8zCUp75bvBS`</summary>

```text
Web search results for query: "CoRL 2026 2027 robot learning conference call for papers deadline"

Links: [{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 - Call for Workshops","url":"https://www.corl.org/contributions/call-for-workshops"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"2025 Conference on Robot Learning - CoRL","url":"https://www.corl.org/home"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"}]

Based on the search results, here is the information about CoRL 2026's call for papers deadline:

## CoRL 2026 Paper Submission Deadlines

The abstract submission deadline is May 26, 2026 at 11:59 UTC, and the paper submission deadline is May 29, 2026 at 11:59 UTC.

## Conference Details

CoRL 2026 will be held in Austin, Texas, US, and workshops and tutorials will be held on November 9th, 2026, the day before the main conference (November 10–12, 2026).

## Paper Specifications

Papers are limited to 8 pages of content plus unlimited references. CoRL welcomes submissions of high-quality research papers that offer novel contributions to robot learning.

Papers may be submitted through OpenReview, and the deadlines are final, and accommodations cannot be made for missing the abstract deadline or paper deadline.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4f1bf5d-a06d-4b61-9725-e9ff6fae9f32",
  "isSidechain": false,
  "promptId": "e0ade265-184d-408b-8e8a-4a4a7a9fb81f",
  "type": "user",
  "uuid": "af78c2fb-167d-4551-89cd-4138912b586b",
  "toolUseResult": {
    "query": "CoRL 2026 2027 robot learning conference call for papers deadline",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GfMUNKTqfAgm6HMucJbiaG",
        "content": [
          {
            "title": "CoRL 2026 - Call for Papers",
            "url": "https://www.corl.org/contributions/call-for-papers"
          },
          {
            "title": "CoRL 2026",
            "url": "https://www.corl.org/"
          },
          {
            "title": "Robot Learning Foundation",
            "url": "https://www.robot-learning.org/"
          },
          {
            "title": "Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"
          },
          {
            "title": "CoRL 2026 - Call for Workshops",
            "url": "https://www.corl.org/contributions/call-for-workshops"
          },
          {
            "title": "AI & ML Conference Deadlines 2026–2027",
            "url": "https://trybibby.com/conference-deadlines"
          },
          {
            "title": "CoRL LaTeX Template | Robot Learning Conference Format | Underleaf",
            "url": "https://www.underleaf.ai/templates/corl"
          },
          {
            "title": "CoRL 2026 - Instruction for Authors",
            "url": "https://www.corl.org/contributions/instruction-for-authors"
          },
          {
            "title": "2025 Conference on Robot Learning - CoRL",
            "url": "https://www.corl.org/home"
          },
          {
            "title": "CoRL 2026 - Contributions",
            "url": "https://www.corl.org/contributions"
          }
        ]
      },
      "Based on the search results, here is the information about CoRL 2026's call for papers deadline:\n\n## CoRL 2026 Paper Submission Deadlines\n\nThe abstract submission deadline is May 26, 2026 at 11:59 UTC, and the paper submission deadline is May 29, 2026 at 11:59 UTC.\n\n## Conference Details\n\nCoRL 2026 will be held in Austin, Texas, US, and workshops and tutorials will be held on November 9th, 2026, the day before the main conference (November 10–12, 2026).\n\n## Paper Specifications\n\nPapers are limited to 8 pages of content plus unlimited references. CoRL welcomes submissions of high-quality research papers that offer novel contributions to robot learning.\n\nPapers may be submitted through OpenReview, and the deadlines are final, and accommodations cannot be made for missing the abstract deadline or paper deadline."
    ],
    "durationSeconds": 4.847783247,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d4f1bf5d-a06d-4b61-9725-e9ff6fae9f32",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-20T03:33:05.914Z_

<details><summary>↩ Tool result · `toolu_01Ag1vcBSQZNuGA3maJwXAN4`</summary>

```text
Web search results for query: ""Preference Leakage" LLM judge contamination ICLR 2026"

Links: [{"title":"Preference Leakage: A Contamination Problem in LLM-as-a-judge | OpenReview","url":"https://openreview.net/forum?id=grIvSXVJ65"},{"title":"Preference Leakage: A Contamination Problem in LLM-as-a-judge [Quick Review]","url":"https://liner.com/review/preference-leakage-a-contamination-problem-in-llmasajudge"},{"title":"[Paper Note] Preference Leakage: A Contamination Problem in LLM-as-a-judge - 📚 AI Paper Notes","url":"https://en.papernotes.org/ICLR2026/llm_evaluation/preference_leakage_a_contamination_problem_in_llm-as-a-judge/"},{"title":"Preference Leakage:ACONTAMINATION PROBLEM IN","url":"https://openreview.net/pdf/f82d578df50174f72931047a5cc1be666424a379.pdf"},{"title":"ICLR Poster Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://iclr.cc/virtual/2026/poster/10008112"},{"title":"Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://arxiv.org/html/2502.01534v3"},{"title":"[2502.01534] Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://arxiv.org/abs/2502.01534"},{"title":"Paper page - Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://huggingface.co/papers/2502.01534"},{"title":"Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://openreview.net/pdf?id=gW6NT2IuME"}]

I found relevant results for your search query. Here's what I found:

**Preference Leakage** is a contamination problem in LLM-as-a-judge caused by the relatedness between the synthetic data generators and LLM-based evaluators. Large Language Models as judges and LLM-based data synthesis have emerged as two fundamental LLM-driven data annotation methods in model development. While their combination significantly enhances the efficiency of model training and evaluation, little attention has been given to the potential contamination brought by this new model development paradigm.

To study this issue, the research defines three common relatednesses between the data generator LLM and the judge LLM: being the same model, having an inheritance relationship, and belonging to the same model family.

This issue arises when the LLMs used for data generation and evaluation are closely related, causing the preference of the LLM evaluators to leak to the student models through synthetic data and thus inflating the evaluation score.

Through extensive experiments, the research empirically confirms the bias of judges towards their related student models caused by preference leakage across multiple LLM baselines and benchmarks. Further analysis suggests that preference leakage is a pervasive issue that is harder to detect compared to previously identified biases in LLM-as-a-judge scenarios.

This paper was presented at ICLR 2026 as a poster presentation and is authored by Dawei Li and colleagues.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1fc23366-287e-4f09-81b4-b36a655899eb",
  "isSidechain": false,
  "promptId": "e0ade265-184d-408b-8e8a-4a4a7a9fb81f",
  "type": "user",
  "uuid": "0f0f3114-9410-4168-9ea4-ed6bf006a109",
  "toolUseResult": {
    "query": "\"Preference Leakage\" LLM judge contamination ICLR 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FkWkyUk5ReW6xPPZF9hPpo",
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
            "title": "Preference Leakage:ACONTAMINATION PROBLEM IN",
            "url": "https://openreview.net/pdf/f82d578df50174f72931047a5cc1be666424a379.pdf"
          },
          {
            "title": "ICLR Poster Preference Leakage: A Contamination Problem in LLM-as-a-judge",
            "url": "https://iclr.cc/virtual/2026/poster/10008112"
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
            "title": "Paper page - Preference Leakage: A Contamination Problem in LLM-as-a-judge",
            "url": "https://huggingface.co/papers/2502.01534"
          },
          {
            "title": "Preference Leakage: A Contamination Problem in LLM-as-a-judge",
            "url": "https://openreview.net/pdf?id=gW6NT2IuME"
          }
        ]
      },
      "I found relevant results for your search query. Here's what I found:\n\n**Preference Leakage** is a contamination problem in LLM-as-a-judge caused by the relatedness between the synthetic data generators and LLM-based evaluators. Large Language Models as judges and LLM-based data synthesis have emerged as two fundamental LLM-driven data annotation methods in model development. While their combination significantly enhances the efficiency of model training and evaluation, little attention has been given to the potential contamination brought by this new model development paradigm.\n\nTo study this issue, the research defines three common relatednesses between the data generator LLM and the judge LLM: being the same model, having an inheritance relationship, and belonging to the same model family.\n\nThis issue arises when the LLMs used for data generation and evaluation are closely related, causing the preference of the LLM evaluators to leak to the student models through synthetic data and thus inflating the evaluation score.\n\nThrough extensive experiments, the research empirically confirms the bias of judges towards their related student models caused by preference leakage across multiple LLM baselines and benchmarks. Further analysis suggests that preference leakage is a pervasive issue that is harder to detect compared to previously identified biases in LLM-as-a-judge scenarios.\n\nThis paper was presented at ICLR 2026 as a poster presentation and is authored by Dawei Li and colleagues."
    ],
    "durationSeconds": 6.781277480000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1fc23366-287e-4f09-81b4-b36a655899eb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-20T03:33:45.036Z_

<details><summary>Logged reasoning block</summary>

```text
Wait - the user said this is for "CoRL 2026 主会" (CoRL 2026 main conference). CoRL is the Conference on Robot Learning. This proposal is about LLM-as-a-judge debiasing, which is an NLP/evaluation topic, NOT a robot learning topic. This is a critical mismatch.

Let me re-read the proposal carefully... Yes, the proposal is about "Causal Style Decomposition for LLM Judge Debiasing via Doubly-Robust Counterfactual Estimation." This is squarely an NLP/AI evaluation methodology paper. The target venues listed in the proposal itself are AAAI 2027, ICLR 2027, and ARR October 2026 - none of which are CoRL.
 
CoRL is fundamentally about robot learning - perception, planning, manipulation, locomotion - so an LLM judge debiasing paper would be completely out of scope. The proposal doesn't even list CoRL as a target venue, which is a major red flag. Before I assess the idea itself, I need to flag this venue mismatch clearly. Now let me evaluate the core contribution: using causal counterfactuals through style rewrites combined with doubly-robust estimation to reduce bias in LLM judges.

Looking at the novelty landscape, there's Length-Controlled AlpacaEval that does post-hoc regression debiasing but only for length as a single dimension, whereas this extends to multiple style axes with proper causal identification. RATE uses double-rewrite for causal estimation on reward models but focuses on explainability rather than debiasing. FairJudge tackles style bias through retraining instead of post-hoc methods for black-box judges. Bias-Bounded Evaluation does post-hoc debiasing via noise injection but takes a different approach.

The core contribution here is combining RATE's double-rewrite protocol with debiased machine learning to handle multi-dimensional causal style debiasing of black-box judges. It's a meaningful assembly of existing pieces—the double-rewrite mechanism, the partially linear model from econometrics, binary style counterfactual axes, and a legitimacy-aware tuning parameter—but the genuine novelty lies in how these components work together for this specific application rather than in any single methodological breakthrough. The shift from using double-rewrite for reward model explainability to judge debiasing is a relatively straightforward extension.

The problem itself matters significantly. Style bias is well-documented in the literature, and FairJudge's adoption demonstrates real community interest in solving this.

However, I'm noticing some practical constraints that could limit impact. The 7x cost overhead for the full approach is substantial, and whether the amortized version actually delivers comparable results remains unclear. I should also consider whether simpler alternatives might capture most of the value—just normalizing formatting and length could plausibly get 80% of the way there, which would undercut the incremental value of the full causal machinery. Multi-prompt ensembling with style-neutralizing instructions is another cheap alternative that might work surprisingly well. Even extending length-controlled regression approaches to multiple style features could be a competitive baseline.

Looking at the core assumptions, I'm skeptical about a few things. The proposal claims the three style axes are genuinely independent, but CASSE shows features are actually entangled—that's a real tension. There's also the question of whether style rewrites preserve content faithfully enough; even with high BERTScore and NLI checks, subtle content shifts could confound the causal estimates. And the DML partially linear model assumes we can cleanly separate "content features" from style, but what actually constitutes content quality independent of presentation isn't well-defined.

Now, regarding CoRL specifically—this is a fundamental venue mismatch. CoRL focuses on robot learning, and this paper has no connection to robotics whatsoever. Even if the core idea were strong, it would face desk rejection for being out of scope. The user's own target venues (AAAI 2027, ICLR 2027, ARR) are all appropriate fits. I need to flag this clearly while still evaluating the idea on its merits, though the user did explicitly ask about CoRL 2026 acceptance probability, so I should address that directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f0f3114-9410-4168-9ea4-ed6bf006a109",
  "isSidechain": false,
  "requestId": "req_011CbD7jwSNSaUkjPcGrbtQN",
  "type": "assistant",
  "uuid": "800b3e17-46d5-4c15-a280-1866f6554160",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q6zFMRGGvGvVoMBahAXL6Q",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 631,
      "cache_creation_input_tokens": 1711,
      "cache_read_input_tokens": 27904,
      "output_tokens": 6316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1711,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 631,
          "output_tokens": 6316,
          "cache_read_input_tokens": 27904,
          "cache_creation_input_tokens": 1711,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1711
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

_source line 41 · 2026-05-20T03:35:24.113Z_

Now I have enough information to conduct a thorough evaluation. Let me note a critical issue before proceeding to the formal rubric.

---

```
【阶段】: Triage

⚠️ 关键前置问题：严重的 venue mismatch

本 proposal 投稿目标是 CoRL 2026（Conference on Robot Learning），但 proposal 的主题是 "LLM-as-a-Judge 评估中的风格偏差因果去偏"——这是一个纯 NLP/AI evaluation methodology 问题，与机器人学习（感知、操控、运动规划、robot policy learning 等）完全无关。

CoRL 2026 CFP 明确征集 "high-quality research papers that offer novel contributions to robot learning"。本 proposal 不涉及任何机器人学习内容，极大概率会被 desk reject（领域不匹配）。

值得注意的是，proposal 自身列出的 target venues 是 AAAI 2027、ICLR 2027、ARR October 2026——均未包含 CoRL。这些 NLP/ML 通用会议才是合理的投稿目标。

以下评估仍然按照 idea 质量客观打分，但概率估计将反映 CoRL 这一特定 venue 的匹配度。


【领域调研】:

1. [Style Outweighs Substance / SOS-Bench](https://arxiv.org/abs/2409.15268) (ICLR 2025): 
   最大规模 meta-benchmark（152,380 数据点），证明 LLM judges 严重偏好 style 而非 factuality/safety。诊断了问题但未提出解决方案。本 proposal 将其作为问题动机，定位准确。

2. [FairJudge](https://arxiv.org/abs/2602.06625) (arXiv Feb 2026): 
   最直接的竞争工作。通过 SFT→DPO→GRPO 课程式训练专门的 judge 模型（Qwen3-VL 2B/4B/8B），针对 position、length、format、reasoning style、model provenance 五维非语义偏差进行去偏。核心限制：需要重新训练 judge，不适用于黑盒商业 API。本 proposal 的核心差异化定位——model-agnostic post-hoc——确实成立。

3. [RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals](https://arxiv.org/abs/2410.11348) (ICML 2025): 
   本 proposal 的方法论核心来源。RATE 提出 double-rewrite protocol 来纠正不完美反事实偏差，用于估计 reward model 对高级属性的因果敏感度。RATE 目标是 reward model 可解释性，非 judge 去偏。本 proposal 本质上是将 RATE 的方法适配到 judge debiasing 场景。

4. [Length-Controlled AlpacaEval](https://arxiv.org/abs/2404.04475) (COLM 2024 / ICLR 2025 context): 
   通过 post-hoc logistic regression 控制 length 偏差，将 AlpacaEval 与 Chatbot Arena 的 Spearman 相关从 0.93 提升到 0.98。仅控制单一维度（length），成本为零。这是最重要的 trivial alternative baseline——如果简单地将其扩展为多维回归（加入 formatting、formality 特征），是否就够了？

5. [Bias-Bounded Evaluation](https://arxiv.org/abs/2603.05485) (arXiv March 2026): 
   通过注入校准高斯噪声实现 differential-privacy 风格的去偏，保持 61–99% ranking correlation。非因果方法，不区分 bias vs. legitimate style-quality association。

6. [Preference Leakage](https://arxiv.org/abs/2502.01534) (ICLR 2026): 
   揭示 judge 与数据生成 LLM 之间的 preference 泄漏问题，提到 judges 依赖 "stylistic regularities"。印证了 style bias 的普遍性。

7. [CASSE: A Concise Agent is Less Expert](https://arxiv.org/abs/2601.10809) (arXiv Jan 2026): 
   12 种 style features 之间存在 deep entanglement（如 conciseness 降低 perceived expertise）。直接挑战了 proposal 中 "三个 style axis 独立" 的假设。

8. [Judging the Judges](https://arxiv.org/abs/2604.23178) (arXiv April 2026): 
   系统评估 9 种 debiasing 策略在 5 个 judge 上的效果。发现 debiasing 效果高度 model-dependent。

9. [Counterfactual LLM-based Framework for Measuring Rhetorical Style](https://arxiv.org/html/2512.19908v1) (arXiv 2025): 
   使用 LLM rhetorical personas 生成反事实写作，通过 pairwise 评估测量修辞风格影响。方法论思路与本 proposal 有相似性（counterfactual rewriting + 评估），但目标不同（测量而非去偏）。

- **调研总结**: LLM judge style bias 是 2025-2026 年的热门研究问题，已有大量工作从诊断（SOS-Bench）、训练去偏（FairJudge）、单维度后处理（LC-AlpacaEval）、噪声注入（BBE）等角度切入。本 proposal 的定位——多维因果分解 + 黑盒适用——在现有工作中确实是一个空白点，但其核心方法论（RATE double-rewrite + DML）是对已有组件的组合应用而非原创方法。


【Trivial Alternative 检验】:

存在多个成本显著更低的替代方案，构成实质威胁：

1. **多维 Length-Controlled AlpacaEval 扩展**：LC-AlpacaEval 已证明 post-hoc regression 在 length 维度上极其有效（Spearman 0.93→0.98），且成本为零。将其自然扩展为多维回归——加入 formatting indicator（是否有 markdown）、formality score、verbosity ratio 作为额外 covariates——不需要生成任何反事实，不需要 7x 推理成本，可能就能捕获大部分 style bias。Proposal 需要论证为什么简单的多维 observational regression 不够，必须做因果 counterfactual estimation，但目前这一论证是缺失的。

2. **Format normalization baseline**：proposal 自己也提到了 "strip all markdown before judging" 这个 baseline。如果 formatting 是 style bias 的主导来源，这个零成本方法可能已经解决了大部分问题。

3. **Style-neutralizing prompt engineering**：在 judge prompt 中加入 "Ignore formatting, length, and writing style; focus solely on content accuracy and completeness" 等指令。[Judging the Judges] 已评估了类似策略，部分场景下效果显著。

**增量价值的关键取决于**：简单回归 / prompt engineering 是否已经 "够好"。如果它们能消除 80% 的 style bias，那 CSD 的 7x 成本换取的额外 20% 改善在实践中可能不值得。Proposal 的因果框架的理论优势（identifiability、unbiasedness）在审稿人眼中是否足以弥补实用性劣势，是一个开放问题。


【前提假设检验】:

核心 claim 的逻辑链中有以下未经验证的关键假设：

1. **三个 binary axis 独立且充分**：Proposal 声称 formality、verbosity、formatting "genuinely independent"，但 CASSE (2601.10809) 明确发现 style features 是 "deeply entangled rather than orthogonal"。Formality 和 verbosity 在实际文本中很可能高度相关（casual text 倾向于 terse）。更关键的是，三个 axis 是否覆盖了 style bias 的主要来源？如果 judge 偏好的 style 特征还包括 tone warmth、sentence complexity、hedging 等，三个 axis 的去偏只能部分解决问题。

2. **LLM rewrite 保持 content 不变的假设**：即使 BERTScore ≥ 0.92 和 NLI ≥ 0.95，rewrites 仍可能引入微妙的 content 变化（如改写 formal→casual 时简化了技术术语、丢失了 nuance）。这种残留 confounding 会直接污染因果估计。RATE 的 double-rewrite 可以纠正 systematic 偏差，但前提是 rewrite noise 是 direction-independent（RATE Assumption 1）——这一假设在 style rewriting 中是否成立未经验证。

3. **DML 中 "content features" 的操作化**：DML partially linear model 中 g(content_features) 需要一组代表 "content quality" 的特征作为控制变量。Proposal 没有说明这些特征是什么、如何提取。如果 content features 与 style features 存在 overlap（例如 text embeddings 同时编码 content 和 style），DML 的识别条件可能被违反。

4. **α parameter 的可泛化性**：legitimacy-aware correction 的 α 在 held-out validation set 上通过最大化 Spearman 相关来调优。但不同 judge、不同 domain 的 α 可能差异很大，且 α 的最优值依赖于 ground-truth quality labels 的可获得性——而 ground-truth 标注恰恰是 LLM judge 试图替代的。这产生了循环依赖。


【3 维度打分】:

1. **Novelty: 弱-中（偏弱）**
   
   核心方法论是对现有组件的组合：RATE 的 double-rewrite protocol（ICML 2025）+ DML partially linear model（Chernozhukov et al. 2018, 标准计量工具）+ binary style counterfactuals（Pryzant et al. 2021 的 functional intervention 思路）。每个组件单独来看都不是新的；组合的 novelty 在于 application to judge debiasing。
   
   与最相关工作的 delta：
   - vs. RATE：从 reward model explainability 到 judge debiasing，核心 estimation 方法不变，只是下游应用不同。
   - vs. LC-AlpacaEval：从单维度回归扩展到多维因果估计，这是一个有意义的升级，但 "多维回归" 这个 trivial alternative 严重削弱了因果框架的 marginal novelty。
   - vs. FairJudge：model-agnostic 是真实差异化，但方法论方向完全不同（post-hoc estimation vs. training-based），不构成直接方法论竞争。
   
   如果审稿人问 "这和把 LC-AlpacaEval 扩展到多维有什么本质区别"，proposal 目前没有令人信服的回答。

2. **Significance: 中**
   
   问题本身重要且 timely——style bias 是 documented 的 dominant bias（SOS-Bench, ICLR 2025），model-agnostic debiasing for black-box judges 填补真实空白（FairJudge 不能用于 GPT-4o/Claude）。这个 gap 是真实的。
   
   但 significance 受限于：(a) 7x 推理成本在实际部署中很可能不被接受，amortized 版本的有效性未经验证；(b) 如果核心发现是 "CSD 提升了 correlation with ground truth by X points"，审稿人很可能觉得 "I would have guessed this"——因为因果方法 by construction 应该比 observational regression 更准确，这不 surprising；(c) 真正 surprising 的发现需要是 "哪些 style effects 在哪些 domain 是 legitimate 的"——但这更像一个 empirical finding 而非方法论贡献。
   
   **注意：这里的 Significance 评估是针对 NLP/ML 会议的。对于 CoRL（机器人学习），significance 为致命级别的零——该问题与机器人学习完全不相关。**

3. **Related Work: 强**
   
   这是本 proposal 做得最好的部分。Related work 覆盖全面且准确：SOS-Bench (ICLR 2025)、FairJudge (arXiv Feb 2026)、RATE (ICML 2025)、LC-AlpacaEval (COLM 2024)、BBE (arXiv March 2026)、CASSE (Jan 2026)、Preference Leakage (ICLR 2026)、DML (Chernozhukov 2018)、ISE (Choi et al. NAACL 2024) 等均已覆盖并正确描述。差异化定位清晰——每个竞争工作都被准确地说明了其局限性以及 CSD 如何填补空白。调研中验证的所有引用均真实存在且描述准确。
   
   唯一可补充的是 [Counterfactual LLM-based Framework for Measuring Rhetorical Style] (arXiv 2025)，它使用类似的 counterfactual rewriting + evaluation 思路来测量修辞风格影响，虽然目标不同但方法论有重叠。


【概率估计】: 0% - 3%，中位 1%

【估计理由】: 
**概率估计的主导因素是 venue mismatch，而非 idea 质量。** CoRL 2026 是 Conference on Robot Learning，征集的是机器人学习领域的高质量论文。本 proposal 是纯 NLP/AI evaluation methodology 工作，与机器人学习无任何关联，极大概率在 desk review 阶段就会被拒绝（out of scope）。Proposal 自身都未将 CoRL 列为 target venue（列出的是 AAAI、ICLR、ARR）。

如果改投至 proposal 自列的目标 venue（AAAI 2027 / ICLR 2027 / ARR），仅基于 idea 质量的估计为：**20% - 30%，中位 25%**。理由：
- Related Work 覆盖扎实（强），问题定位准确，gap 真实存在
- 但 Novelty 偏弱：核心是已有组件（RATE + DML + binary interventions）的组合应用，存在 "多维 LC-AlpacaEval 回归" 这一强 trivial alternative 威胁
- Significance 中等：问题重要但核心发现 if positive 不太 surprising；7x 成本是实用性障碍
- 上界被 Novelty 限制：如果审稿人认为这主要是 RATE 的 straightforward application to a new domain，得分会被压低

【主要风险】:
1. **致命风险——Venue Mismatch**: 投稿 CoRL 将几乎确定被 desk reject。这是一个 NLP evaluation methodology 的工作，不属于机器人学习范畴。
2. **Idea 层面风险——Trivial Alternative 威胁**: 多维 observational regression（LC-AlpacaEval 的自然扩展）可能以接近零的成本达到 CSD 大部分效果，使得因果框架的 7x 开销难以 justify。Proposal 必须在实验中明确展示简单回归方法的不足之处，以论证因果估计的必要性。
```

Sources:
- [SOS-Bench: Style Outweighs Substance](https://arxiv.org/abs/2409.15268)
- [FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge](https://arxiv.org/abs/2602.06625)
- [RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals](https://arxiv.org/abs/2410.11348)
- [Length-Controlled AlpacaEval](https://arxiv.org/abs/2404.04475)
- [Bias-Bounded Evaluation](https://arxiv.org/abs/2603.05485)
- [Preference Leakage](https://arxiv.org/abs/2502.01534)
- [CASSE: A Concise Agent is Less Expert](https://arxiv.org/abs/2601.10809)
- [Judging the Judges: Systematic Evaluation of Bias Mitigation](https://arxiv.org/abs/2604.23178)
- [Counterfactual LLM-based Framework for Measuring Rhetorical Style](https://arxiv.org/html/2512.19908v1)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "800b3e17-46d5-4c15-a280-1866f6554160",
  "isSidechain": false,
  "requestId": "req_011CbD7jwSNSaUkjPcGrbtQN",
  "type": "assistant",
  "uuid": "e4ead3b3-8a62-47cf-95e9-d33b0821502a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q6zFMRGGvGvVoMBahAXL6Q",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 631,
      "cache_creation_input_tokens": 1711,
      "cache_read_input_tokens": 27904,
      "output_tokens": 6316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1711,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 631,
          "output_tokens": 6316,
          "cache_read_input_tokens": 27904,
          "cache_creation_input_tokens": 1711,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1711
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

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Causal Style Decomposition for LLM Judge Debiasing via Doubly-Robust Counterfactual Estimation  ## Description S…",
  "leafUuid": "e4ead3b3-8a62-47cf-95e9-d33b0821502a",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate causal style decomposition for LLM judge debiasing",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Causal Style Decomposition for LLM Judge Debiasing via Doubly-Robust Counterfactual Estimation  ## Description S…",
  "leafUuid": "e4ead3b3-8a62-47cf-95e9-d33b0821502a",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate causal style decomposition for LLM judge debiasing",
  "sessionId": "45668d56-1de2-4a3a-82b3-f65cc49f0197"
}
```

---
