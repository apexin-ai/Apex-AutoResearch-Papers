# 4. Experiments

## 4.1 Experimental Setup

**Claim**: We evaluate BCP and DPO+BCP calibration on Qwen2.5-7B-Instruct in the $\tau$-bench retail domain, with auxiliary cross-model and cross-scale evidence.

**Primary model.** Qwen2.5-7B-Instruct, served via vLLM with `gpu_memory_utilization=0.9`, `max_model_len=32768`, `trust_remote_code=True`. For DPO experiments, the DPO-003 adapter is merged into base weights and served as a standalone model.

**Excluded models.**
- *Llama-3-8B-Instruct* [llama-bcp-001]: Completion floor at 5% (1/20 tasks). Tool-calling capability insufficient for $\tau$-bench's 16-tool environment. Cannot isolate BCP effect from tool-calling failure.
- *Mistral-7B-Instruct-v0.3* [mistral-bcp-001]: Completion 0% (0/3 tasks). Model cannot generate structured `tool_calls` with 16 tools --- embeds JSON in text content instead. Single-tool calling works; 16-tool calling fails. Attempted `--tool-call-parser mistral` + `--tokenizer-mode mistral` without success.

**Cross-scale validation.** [PENDING: Qwen2.5-14B-Instruct-AWQ, qwen14b-bcp-001]

## 4.2 BCP Failure Mechanisms (C1)

**Claim**: BCP produces three systematic failure mechanisms --- global behavior suppression, cross-dimension interference, and overcorrection rebound --- that collectively explain why prompt-based calibration fails.

### Table 1: BCP Results (Qwen2.5-7B-Instruct, $n=19$--$20$ per variant) [mvp-004]

| Variant | Politeness | $\Delta$ Pol | Completion | $\Delta$ Comp | Question Rate | $\Delta$ QR |
|---------|------------|-------------|------------|--------------|---------------|-------------|
| `baseline` | 0.559 | --- | 0.368 | --- | 0.044 | --- |
| `aave_target` | 0.468 | $-16.3\%$ | 0.100 | $-72.8\%$ | 0.015 | $-65.9\%$ |
| `indian_english` | 0.460 | $-17.7\%$ | 0.150 | $-59.2\%$ | 0.014 | $-68.2\%$ |
| `overcorrected` | 0.605 | $+8.2\%$ | 0.263 | $-28.5\%$ | 0.018 | $-59.1\%$ |
| `single_dim_question` | 0.416 | $-25.6\%$ | 0.250 | $-32.1\%$ | 0.065 | $+47.7\%$ |
| `single_dim_politeness` | 0.634 | $+13.4\%$ | 0.200 | $-45.7\%$ | 0.021 | $-52.3\%$ |

### FM1: Global Behavior Suppression

BCP injection collapses task completion regardless of the targeted behavioral dimension. Mean calibrated completion across all five BCP variants is $0.193$ ($52.3\%$ retention of baseline $0.368$), far below the $\geq 80\%$ threshold required by H3. Even the best-performing variant (`overcorrected`, $0.263$) retains only $71.5\%$ of baseline completion.

This parallels the persona-accuracy trade-off documented in classification settings: persona prompting degrades MMLU accuracy from $71.6\%$ to $66.3\%$ \cite{basil2025playing_pretend}, and expert personas cause up to 30pp accuracy drops with instruction-tuned models being most susceptible \cite{hu2026expert_persona}. BCP represents a more severe instance of this trade-off in agentic settings, where the model must simultaneously maintain persona compliance and multi-step tool-calling capability.

### FM2: Cross-Dimension Interference

Targeting a single behavioral dimension perturbs non-targeted dimensions:

- `single_dim_question` (targets question rate only): politeness drops $25.6\%$ ($0.559 \to 0.416$), despite no politeness constraint.
- `single_dim_politeness` (targets politeness only): question rate drops $52.3\%$ ($0.044 \to 0.021$), despite no question rate constraint.

**Base rate caveat.** The baseline question rate is low ($0.044$, approximately 0.8 questions per multi-turn task episode). The $52.3\%$ relative drop corresponds to an absolute change from $\sim 0.044$ to $\sim 0.021$. We report both relative and absolute values throughout; readers should weight the absolute magnitudes when assessing practical significance.

This cross-dimension coupling aligns with the bias spillover effect documented in targeted LLM alignment \cite{gupta2026intra_fairness}, where debiasing one social axis produces unintended effects on others. In our setting, the coupling suggests behavioral dimensions share representational capacity that cannot be independently modulated via prompting alone.

### FM3: Overcorrection Rebound

Requesting extreme behavioral shifts causes the model to rebound in the opposite direction. The `overcorrected` variant targets very low politeness ($\sim 5\%$) but produces *higher* politeness than baseline.

**Primary evidence** [hgate-dpo003-merged, 4 runs]:

| Run | Baseline Pol | Overcorrected Pol | $\Delta$ (pp) |
|-----|-------------|-------------------|---------------|
| 1 | 0.4748 | 0.5693 | $+9.45$ |
| 2 | 0.4657 | 0.5080 | $+4.23$ |
| 3 | 0.5321 | 0.5810 | $+4.89$ |
| 4 | 0.5336 | 0.6371 | $+10.35$ |
| **Mean** | **0.5016** | **0.5739** | **$+7.23$** |

The rebound is consistent across all 4 runs (4/4), with magnitude ranging from $+4.2$pp to $+10.4$pp ($+8.2\%$ to $+19.4\%$ relative). Auxiliary evidence from the single-run BCP experiment [mvp-004] shows the same direction: overcorrected politeness $0.605$ vs. baseline $0.559$ ($+4.6$pp, $+8.2\%$ relative).

This suggests an "attractor basin" for default behavioral rates: the model resists large perturbations and snaps back toward (or beyond) its baseline distribution. No direct external parallel exists for this specific mechanism, making FM3 a novel contribution.

## 4.3 DPO+BCP Interaction Reversal (C2)

**Claim**: DPO training, despite effective learning (accuracy $0.75$--$1.0$), reverses the direction of BCP calibration when combined, expanding rather than closing dialect-dependent behavioral gaps.

### Table 2: DPO+BCP Aggregate Results [hgate-dpo003-merged, 4 runs $\times$ 20 tasks]

| Variant | Mean Pol ($\pm$ SD) | Mean Comp ($\pm$ SD) | H2 Gap Change |
|---------|---------------------|----------------------|---------------|
| `baseline` | $0.502 \pm 0.035$ | $0.294 \pm 0.107$ | --- |
| `aave_target` | $0.566 \pm 0.039$ | $0.249 \pm 0.157$ | $-23.3 \pm 23.4$ |
| `indian_english` | $0.565 \pm 0.054$ | $0.166 \pm 0.059$ | $-21.9 \pm 19.3$ |
| `overcorrected` | $0.574 \pm 0.054$ | $0.209 \pm 0.057$ | $-18.0 \pm 7.5$ |
| `single_dim_question` | $0.475 \pm 0.059$ | $0.220 \pm 0.090$ | --- |
| `single_dim_politeness` | $0.609 \pm 0.043$ | $0.279 \pm 0.082$ | --- |

*H2 Gap Change reported as mean $\pm$ SD across 4 runs (negative = gap expanded). See Appendix for per-run breakdown.*

**H-gate results**: H1 PASS (4/4), H2 FAIL (0/4), H3 FAIL (3/4). Overall: **FAIL**.

### Direction Reversal

The critical finding is that DPO+BCP *reverses* the calibration direction compared to BCP alone:

| Comparison | AAVE Pol Gap | Indian Pol Gap |
|------------|-------------|----------------|
| BCP alone (baseline $-$ variant) [mvp-004] | $-0.091$ (correct: variant lower) | $-0.099$ (correct: variant lower) |
| DPO+BCP (baseline $-$ variant) [hgate-dpo003-merged] | $+0.064$ (**reversed**: variant higher) | $+0.063$ (**reversed**: variant higher) |

Under BCP alone, dialect-targeted variants show lower politeness than baseline (the intended calibration direction). Under DPO+BCP, the same variants show *higher* politeness than baseline --- the gap has flipped sign.

**Gap expansion.** Across 4 runs $\times$ 3 dialect-targeted variants (aave, indian, overcorrected) = 12 variant$\times$run checks, 10/12 show gap expansion (politeness gap increased rather than decreased). Mean H2 gap reduction = $-10.3\%$ (negative = wrong direction; threshold $\geq +30\%$).

### DPO Training Was Effective

The reversal is not attributable to DPO training failure. DPO-003 metrics show strong learning:

- Rewards accuracy: $0.75$--$1.0$ (vs. $0.50$ for DPO-001 with mismatched data)
- Rewards margin: $0.05$--$0.17$ (vs. $-0.00015$ for DPO-001)
- Merged model completion: $60\%$ vs. base model $40\%$ [diag-lora-merge]

DPO improved the model's tool-calling ability. The reversal arises from an **interaction effect** between DPO alignment and BCP prompting. This aligns with findings that DPO bypasses rather than removes pre-training capabilities \cite{lee2024dpo_toxicity}: the DPO-aligned model has a shifted behavioral baseline that interacts adversarially with BCP rate targets.

### Overcorrection Amplification

DPO amplifies the overcorrection rebound (FM3):

| Setting | Overcorrected Pol $-$ Baseline Pol | Relative |
|---------|-------------------------------------|----------|
| BCP alone [mvp-004] | $+4.6$pp ($0.605$ vs. $0.559$) | $+8.2\%$ |
| DPO+BCP [hgate-dpo003-merged, mean] | $+7.2$pp ($0.574$ vs. $0.502$) | $+14.3\%$ |

The rebound magnitude approximately doubles under DPO, suggesting that alignment strengthens the attractor basin that resists extreme calibration targets.

## 4.4 Cross-Scale Validation (C3)

[PENDING: qwen14b-bcp-001]

### Table 3: Cross-Scale BCP Comparison (placeholder)

| Metric | Qwen2.5-7B [mvp-004] | Qwen2.5-14B [PENDING] |
|--------|-----------------------|-----------------------|
| Baseline completion | 0.368 | [PENDING] |
| Baseline politeness | 0.559 | [PENDING] |
| FM1: mean calibrated completion retention | 52.3% | [PENDING] |
| FM2: cross-dim politeness shift (single_dim_question) | $-25.6\%$ | [PENDING] |
| FM3: overcorrection rebound | $+8.2\%$ | [PENDING] |

**Auxiliary cross-model evidence.**
- Llama-3-8B-Instruct [llama-bcp-001]: Completion floor ($5\%$) prevents meaningful BCP analysis. All three tested variants achieve identical completion (1/20 on the same task), so BCP has zero observable completion effect. Politeness shifts are observable but occur in $95\%$-failed dialogues, supporting only a weak claim that "low-capability models also exhibit behavioral shifts under BCP."
- Mistral-7B-Instruct-v0.3 [mistral-bcp-001]: Zero tool-calling capability in 16-tool setting. No usable data.

**Hedging strategy.** If Qwen-14B replicates FM1--FM3: "failure modes persist across model scales (7B, 14B)." If not: "documented on Qwen2.5-7B; generalizability requires further investigation."

## 4.5 Analysis

### Baseline Completion Variance

Baseline task completion exhibits high variance across runs in the DPO+BCP evaluation [hgate-dpo003-merged]:

| Run | Baseline Completion |
|-----|---------------------|
| 1 | 0.278 |
| 2 | 0.150 |
| 3 | 0.400 |
| 4 | 0.350 |
| **Mean $\pm$ SD** | **$0.294 \pm 0.107$** |

The $\sigma = 10.7$pp across 4 runs (range: $15.0\%$--$40.0\%$) reflects inherent stochasticity in multi-turn tool-calling dialogues. This variance is a confound for completion-based claims and motivates our focus on *directional consistency* (e.g., overcorrection rebound in 4/4 runs, gap expansion in 10/12 checks) rather than precise magnitude estimates.

### DPO Training Quality Progression

The three DPO iterations demonstrate how data quality dominates training outcomes:

| Version | Mismatch | Accuracy | Loss | Margin | exp_id |
|---------|----------|----------|------|--------|--------|
| DPO-001 | 48% | 0.50 | 0.6814 | $-0.00015$ | dpo-001 |
| DPO-002 | Partial | 0.667 | 0.6614 | $0.026$ | dpo-002 |
| DPO-003 | 0% | 0.75--1.0 | 0.653 | $0.05$--$0.17$ | dpo-003 |

DPO-001 trained on v1 data with $48\%$ tokenizer mismatch, producing random-level accuracy and near-zero rewards margin. Fix B (apply_chat_template $\to$ plain text) in DPO-003 eliminated mismatch entirely, yielding strong learning signal. Despite this effective training, DPO-003 still failed to produce positive calibration outcomes when combined with BCP --- the failure is in the calibration interaction, not in DPO learning.

### vLLM LoRA Serving Bug

Diagnostic experiment [diag-lora-merge] revealed a critical evaluation artifact: vLLM's dynamic LoRA loading produces severely degraded completion compared to merged-model serving.

| Serving Mode | Completion | Source |
|-------------|------------|--------|
| vLLM LoRA dynamic loading | 15% | hgate-dpo003 (killed) |
| Merged model (PEFT `merge_and_unload`) | 60% | diag-lora-merge |
| Base model (no DPO) | 40% | diag-lora-merge |

The $4\times$ gap between LoRA serving ($15\%$) and merged serving ($60\%$) invalidates all LoRA-served evaluation data (hgate-dpo001, hgate-dpo002, hgate-dpo003). All final results in this paper use the merged model [hgate-dpo003-merged]. This finding has practical implications: researchers using vLLM for LoRA-based evaluation should validate against merged-model baselines.

### Statistical Limitations

- BCP-only results (Table 1) are from a single run ($n = 19$--$20$ per variant). While effect sizes are large (completion drops $>28\%$), statistical power for precise magnitude estimates is limited.
- DPO+BCP results (Table 2) benefit from 4 independent runs, enabling consistency analysis. We focus on directional consistency (10/12 gap expansion, 4/4 overcorrection rebound) rather than point estimates.
- [PENDING: Bootstrap confidence intervals for key comparisons (FM3 rebound magnitude, C2 reversal direction)]
