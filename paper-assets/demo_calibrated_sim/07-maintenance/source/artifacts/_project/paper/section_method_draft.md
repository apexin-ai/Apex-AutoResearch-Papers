# 3. Method

## 3.1 Task Environment

We ground our study in the $\tau$-bench retail domain \cite{yao2024taubench}, a multi-turn tool-calling benchmark for evaluating customer service agents. The environment consists of a user simulator $\mathcal{U}$, a customer service agent $\mathcal{A}$, and 16 retail-domain tools (e.g., `get_order_details`, `cancel_order`, `modify_pending_order`). Each episode proceeds as a multi-turn dialogue where $\mathcal{U}$ presents a task request and $\mathcal{A}$ must resolve it through tool-calling and natural language interaction.

**Task completion.** Following \cite{yao2024taubench}, we define task success as a binary reward $r \in \{0, 1\}$ computed by comparing the final database state against the ground-truth target state. We report task completion rate as $\bar{r} = \frac{1}{N}\sum_{i=1}^{N} r_i$ over $N$ episodes.

**Why $\tau$-bench.** $\tau$-bench provides (1) a standardized user simulator that is amenable to behavioral modification via system prompt injection, (2) a deterministic reward signal that does not require human judgment, and (3) a multi-turn setting where behavioral calibration effects accumulate across turns. Recent work \cite{sim2real2026gap} demonstrates that LLM user simulators in $\tau$-bench are excessively cooperative and stylistically uniform compared to real users, directly motivating calibration interventions.

## 3.2 Behavioral Calibration Prompting (BCP)

**Motivation.** LLM user simulators exhibit dialect-dependent behavioral biases: AAVE and Indian English speakers receive systematically different politeness and question-asking patterns compared to Standard American English \cite{seshadri2026lost, haq2026dialect}. BCP aims to close these gaps by injecting explicit behavioral rate targets into the user simulator's system prompt.

**Design.** A BCP prompt $p_v$ for variant $v$ specifies target rates for one or more behavioral dimensions. The modified user simulator $\mathcal{U}_{v}$ receives $p_v$ prepended to its standard instructions. We design six variants to cover three axes of variation:

| Variant | Target | Motivation |
|---------|--------|------------|
| `baseline` | No BCP injection | Control condition; uncalibrated simulator |
| `aave_target` | Politeness $\approx 20\%$, question rate $\approx 10\%$ | Calibrate toward AAVE behavioral norms \cite{rickford1999aave} |
| `indian_english` | Politeness $\approx 35\%$, question rate $\approx 8\%$ | Calibrate toward Indian English norms \cite{kachru2008cultures} |
| `overcorrected` | Politeness $\approx 5\%$, question rate $\approx 2\%$ | Extreme target to probe overcorrection dynamics |
| `single_dim_question` | Question rate $\approx 10\%$; politeness unconstrained | Isolate single-dimension calibration effect |
| `single_dim_politeness` | Politeness $\approx 20\%$; question rate unconstrained | Isolate single-dimension calibration effect |

**Variant selection rationale.** The six variants span three critical dimensions: (1) cross-dialect calibration (`aave_target`, `indian_english`) tests whether BCP can correct real demographic gaps; (2) single-dimension controls (`single_dim_question`, `single_dim_politeness`) isolate whether cross-dimension interference is inherent; (3) the `overcorrected` variant probes model behavior under extreme calibration pressure, revealing overcorrection rebound effects.

## 3.3 DPO Training Protocol

**Data construction.** We generate preference pairs from $\tau$-bench retail episodes. Each pair $(x, y_w, y_l)$ consists of a dialogue context $x$, a preferred response $y_w$ exhibiting target behavioral rates (lower politeness, appropriate question frequency), and a dispreferred response $y_l$ exhibiting baseline behavioral rates.

- **Source data**: 137 baseline traces + 32 AAVE-calibrated traces from Qwen2.5-7B-Instruct [aave-corpus-gen]
- **Pair construction**: 1,563 DPO preference pairs from user-turn behavioral rate contrasts [aave-corpus-gen]

**Critical implementation detail: Fix B.** TRL's `DPOTrainer` (v1.4.0) hard-codes `add_generation_prompt=True` for conversational-format data, appending `<|im_start|>assistant\n` to prompt tokens. When chosen/rejected responses are user-role turns, this causes systematic tokenizer mismatch (TRL issue #5213). We resolve this by applying `tokenizer.apply_chat_template()` during preprocessing to convert conversations to plain text, forcing `DPOTrainer` to use the text-format code path with zero mismatch. We additionally set `padding_side="right"` to prevent padding-induced attention artifacts.

**Training configuration.** We fine-tune Qwen2.5-7B-Instruct using LoRA \cite{hu2021lora}:

| Parameter | Value |
|-----------|-------|
| LoRA rank $r$ | 16 |
| LoRA $\alpha$ | 32 (scaling factor $\alpha/r = 2$) |
| Target modules | `q_proj`, `v_proj` |
| LoRA dropout | 0.05 |
| Learning rate | $5 \times 10^{-7}$ |
| DPO $\beta$ | 0.1 |
| Batch size | 1 (gradient accumulation 4, effective batch 4) |
| Epochs | 3 |
| Total steps | 1,173 |

**DPO version evolution.** The final training protocol (DPO-003) emerged through iterative debugging:

| Version | Data Format | Mismatch Rate | Final Accuracy | Final Loss | exp_id |
|---------|-------------|---------------|----------------|------------|--------|
| DPO-001 | Raw text (v1) | 48% | 0.50 (random) | 0.6814 | dpo-001 |
| DPO-002 | Chat template (v2) | Partial (TRL bug) | 0.667 | 0.6614 | dpo-002 |
| DPO-003 | Plain text via Fix B (v3) | 0% | 0.75--1.0 | 0.653 | dpo-003 |

DPO-001's 48% mismatch rate rendered training ineffective (accuracy at chance level, rewards margin $-0.00015$). DPO-003 achieved strong learning signal with rewards margin $0.05$--$0.17$, confirming that Fix B resolved the data-model alignment issue.

## 3.4 Evaluation Protocol

**Hypothesis-gated evaluation (H-gate).** We evaluate calibration success through three sequential hypotheses:

- **H1 (Baseline quality)**: Uncalibrated baseline politeness rate $\geq 0.30$, confirming the model exhibits measurable behavioral rates worth calibrating.
- **H2 (Calibration effect)**: Calibrated variants reduce the politeness gap between dialect-targeted variants and baseline by $\geq 30\%$ relative.
- **H3 (Completion retention)**: Calibrated variant task completion $\geq 80\%$ of baseline completion rate, ensuring calibration does not destroy task-solving capability.

**Evaluation scale.** For BCP-only evaluation [mvp-004]: 1 run $\times$ 20 tasks $\times$ 6 variants = 120 episodes ($n = 19$--$20$ per variant after filtering). For DPO+BCP evaluation [hgate-dpo003-merged]: 4 runs $\times$ 20 tasks $\times$ 6 variants = 480 episodes, enabling cross-run consistency analysis.

**Behavioral metrics.** We measure three dimensions per episode:

- **Politeness rate**: Fraction of user turns containing politeness markers (greetings, thanks, hedging, apologies), computed via keyword-based classifier.
- **Task completion**: Binary reward $r \in \{0, 1\}$ from $\tau$-bench database state comparison.
- **Question rate**: Fraction of user turns containing interrogative sentences, computed via `QuestionDetector` (rule-based, precision-validated on a held-out annotation set).

**Model serving.** For DPO-003 evaluation, we serve the merged model (LoRA weights merged via PEFT `merge_and_unload`) rather than vLLM dynamic LoRA loading. Diagnostic experiment [diag-lora-merge] revealed that vLLM LoRA dynamic loading produces severely degraded completion (15% vs. 60% for merged model vs. 40% for base model), likely due to weight scaling inconsistencies in the LoRA serving path. All reported DPO results use the merged model.

[PENDING: Qwen2.5-14B-Instruct-AWQ deployment details for cross-scale validation, qwen14b-bcp-001]
