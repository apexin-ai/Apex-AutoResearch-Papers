# Research conversation: <project_context> # 项目: distill_sparse_swiglu ## 运行环境 - 服务器名: westd-34887 - SSH 账户: root（调用 ssh_execute / submit_trainin — Part 2 of 2

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../research-conversation-project-context-distill-sparse-swiglu-westd-34887-ssh-root-ssh-execute-submit-copy-585.md) · [Structured JSON](../../../sessions/bb/bb1dce603b140fac75d4.json)

## Round 1

### Tool result

_source line 61 · 2026-05-24T01:19:44.597Z_

<details><summary>↩ Tool result · `toolu_01AfEt1m2xwHJYb8DrDiwKup`</summary>

````text
Now I have all the data needed to produce the full verification report.

---

## Cross-Verification Report

---

### TABLE A: Qwen-2.5-14B (tab:14b)

**Dense Baseline** (qwen14b_dense_baseline + qwen14b_dense_hspiqa)

```
[A][Dense] PPL    paper=5.19    registry=5.1854 (qwen14b_dense_baseline) ✅
[A][Dense] ARC-c  paper=67.58   registry=67.58  (qwen14b_dense_baseline) ✅
[A][Dense] WG     paper=81.06   registry=81.06  (qwen14b_dense_baseline) ✅
[A][Dense] MMLU   paper=79.77   registry=79.77  (qwen14b_dense_baseline) ✅
[A][Dense] GSM8K  paper=87.57   registry=87.57  (qwen14b_dense_baseline) ✅
[A][Dense] HS     paper=84.20   registry=84.21  (qwen14b_dense_hspiqa)   ✅
[A][Dense] PIQA   paper=81.94   registry=81.94  (qwen14b_dense_hspiqa)   ✅
```

**Global KL (qwen14b_kl30_s42_eval + qwen14b_kl30_global_hspiqa)**

```
[A][KL-Global] PPL    paper=7.62    registry=7.6232  (qwen14b_kl30_s42_eval) ✅
[A][KL-Global] ARC-c  paper=57.17   registry=57.17   (qwen14b_kl30_s42_eval) ✅
[A][KL-Global] WG     paper=72.06   registry=72.06   (qwen14b_kl30_s42_eval) ✅
[A][KL-Global] MMLU   paper=63.72   registry=63.72   (qwen14b_kl30_s42_eval) ✅
[A][KL-Global] GSM8K  paper=48.82   registry=48.82   (qwen14b_kl30_s42_eval) ✅
[A][KL-Global] HS     paper=75.01   registry=75.01   (qwen14b_kl30_global_hspiqa) ✅
[A][KL-Global] PIQA   paper=77.37   registry=77.37   (qwen14b_kl30_global_hspiqa) ✅
```

**Global TEAL (qwen14b_teal30_eval + qwen14b_teal30_global_hspiqa)**

```
[A][TEAL-Global] PPL    paper=8.73    registry=8.7332  (qwen14b_teal30_eval) ✅
[A][TEAL-Global] ARC-c  paper=56.83   registry=56.83   (qwen14b_teal30_eval) ✅
[A][TEAL-Global] WG     paper=72.69   registry=72.69   (qwen14b_teal30_eval) ✅
[A][TEAL-Global] MMLU   paper=71.83   registry=71.83   (qwen14b_teal30_eval) ✅
[A][TEAL-Global] GSM8K  paper=49.51   registry=49.51   (qwen14b_teal30_eval) ✅
[A][TEAL-Global] HS     paper=70.51   registry=70.51   (qwen14b_teal30_global_hspiqa) ✅
[A][TEAL-Global] PIQA   paper=74.70   registry=74.70   (qwen14b_teal30_global_hspiqa) ✅
```

**Global BCE (qwen14b_bce30_s42 for PPL; qwen14b_bce30_global_hspiqa for HS/PIQA; exp_id qwen14b_bce30_s42_eval NOT IN REGISTRY for ARC-c/WG/MMLU/GSM8K)**

```
[A][BCE-Global] PPL    paper=8.76    registry=8.76  (qwen14b_bce30_s42, teal_global_ppl) ✅
[A][BCE-Global] ARC-c  paper=57.59   registry=NOT FOUND (qwen14b_bce30_s42_eval missing) ⚠️
[A][BCE-Global] WG     paper=72.61   registry=NOT FOUND ⚠️
[A][BCE-Global] MMLU   paper=71.67   registry=NOT FOUND ⚠️
[A][BCE-Global] GSM8K  paper=53.07   registry=NOT FOUND ⚠️
[A][BCE-Global] HS     paper=53.43   registry=53.43  (qwen14b_bce30_global_hspiqa) ✅
[A][BCE-Global] PIQA   paper=68.28   registry=68.28  (qwen14b_bce30_global_hspiqa) ✅
```

**Uniform KL (3-seed s42/s123/s456: qwen14b_kl30_s42_eval_uniform_v3, qwen14b_kl30_s123_eval_v5, qwen14b_kl30_s456_eval_v3)**

```
[A][KL-Uniform] PPL    paper=7.90        registry=7.90±0.03  (3-seed mean) ✅
[A][KL-Uniform] ARC-c  paper=53.50       registry=53.50±1.83 (3-seed mean) ✅
[A][KL-Uniform] WG     paper=72.82       registry=72.82±1.41 (3-seed mean) ✅
[A][KL-Uniform] MMLU   paper=63.55       registry=63.55±1.23 (3-seed mean) ✅
[A][KL-Uniform] GSM8K  paper=30.9±6.8*  registry=30.8±6.6 (s42=35.5, s456=26.1, n=2) ✅
[A][KL-Uniform] HS     paper=72.68±0.2   registry=72.68±0.19 (3-seed) ✅
[A][KL-Uniform] PIQA   paper=76.01±1.1   registry=76.01±1.09 (3-seed) ✅
```

*Note: GSM8K n=2 because s123 incomplete; paper footnote acknowledges this. Registry gives mean=30.8 vs paper 30.9 (0.1pp rounding), std=6.6 vs 6.8 (0.2pp rounding). Both within rounding.*

**Uniform TEAL (qwen14b_teal30_uniform_gsm8k + qwen14b_teal30_uniform_hspiqa; ARC-c/WG/MMLU/PPL NOT IN REGISTRY)**

```
[A][TEAL-Uniform] PPL    paper=8.01    registry=NOT FOUND ⚠️
[A][TEAL-Uniform] ARC-c  paper=55.29   registry=NOT FOUND ⚠️
[A][TEAL-Uniform] WG     paper=69.85   registry=NOT FOUND ⚠️
[A][TEAL-Uniform] MMLU   paper=66.34   registry=NOT FOUND ⚠️
[A][TEAL-Uniform] GSM8K  paper=52.1    registry=52.1  (qwen14b_teal30_uniform_gsm8k) ✅
[A][TEAL-Uniform] HS     paper=67.72   registry=67.72 (qwen14b_teal30_uniform_hspiqa) ✅
[A][TEAL-Uniform] PIQA   paper=74.70   registry=74.70 (qwen14b_teal30_uniform_hspiqa) ✅
```

---

### TABLE B: Extended Downstream (tab:downstream)

```
[B][Dense]         HS   paper=82.35   registry=82.35  (dense_baseline_hellaswag_piqa) ✅
[B][Dense]         PIQA paper=80.90   registry=80.90  (dense_baseline_hellaswag_piqa) ✅
[B][KL-30%-unif]   HS   paper=71.07±0.54  registry=70.85 (s42 only; kl30_uniform_hellaswag_piqa_v2) ⚠️
[B][KL-30%-unif]   PIQA paper=74.95±0.25  registry=74.81 (s42 only) ⚠️
[B][TEAL-30%-unif] HS   paper=63.31   registry=63.31  (teal_30pct_uniform_multiseed_eval) ✅
[B][TEAL-30%-unif] PIQA paper=72.80   registry=71.98  (teal_30pct_uniform_multiseed_eval) ❌
[B][BCE-30%-iso]   HS   paper=62.81   registry=62.81  (bce_isocompute_hellaswag_piqa_v2) ✅
[B][BCE-30%-iso]   PIQA paper=74.21   registry=74.21  (bce_isocompute_hellaswag_piqa_v2) ✅
[B][KL-50%-global] HS   paper=58.95   registry=58.95  (kl50_global_hellaswag_piqa_v2) ✅
[B][KL-50%-global] PIQA paper=69.48   registry=69.48  (kl50_global_hellaswag_piqa_v2) ✅
[B][KL-50%-unif]   HS   paper=56.66   registry=56.66  (kl50_uniform_hellaswag_piqa) ✅
[B][KL-50%-unif]   PIQA paper=69.10   registry=69.10  (kl50_uniform_hellaswag_piqa) ✅
[B][TEAL-50%-unif] HS   paper=39.35   registry=NOT FOUND (bench_teal50_uniform_6task missing) ⚠️
[B][TEAL-50%-unif] PIQA paper=63.66   registry=NOT FOUND ⚠️
```

**Table B flags:**
- `[B][KL-30%-unif]`: Only seed 42 (s42=70.85 HS, 74.81 PIQA) is registered individually. The paper reports a 3-seed mean (71.07/74.95). The s123 and s456 HS/PIQA runs for LLaMA KL30 uniform are not registered under any exp_id. The paper values are not individually verifiable from registry alone; they are plausible given s42 is within 0.2pp of the mean.
- `[B][TEAL-30%-unif] PIQA`: Registry shows 71.98; paper shows 72.80. This is a **0.82pp discrepancy**. The registry entry `teal_30pct_uniform_multiseed_eval` stores `piqa` (=71.98) not `piqa_acc_norm`. It is likely both refer to acc_norm but there is a genuine numerical mismatch.
- `[B][TEAL-50%-unif]`: The exp_id `bench_teal50_uniform_6task` does not exist in the registry; only bench_teal50 (global, no HS/PIQA) is present.

---

### TABLE C: OOD Evaluation (tab:ood)

```
[C][Dense]        C4-PPL paper=9.21     registry=9.2075 (c4_ood_dense_baseline_v2) ✅
[C][KL-30%-pred]  C4-PPL paper=16.03±0.01  registry=16.033±0.010 (c4_ood_kl30_s42_v2=16.040, c4_ood_kl30_s123_v2=16.026) ✅
[C][KL-50%-pred]  C4-PPL paper=18.40    registry=18.401 (eval_c4_ood_kl50) ✅
[C][TEAL-50%-van] C4-PPL paper=38.75    registry=38.750 (eval_c4_ood_kl50) ✅
```

*Appendix paragraph on uniform allocation: paper says 18.22/16.37/16.36 → mean 16.98±1.07. Registry: c4_ood_kl30_uniform_s42=18.22, s123=16.37, s456=16.36, computed mean=16.98±1.07. ✅ (perfect match)*

---

### TABLE D: C4 Training Data Control (tab:c4_control)

```
[D][WikiText] PPL    paper=8.82    registry=8.8157  (bench_kl30_uniform) ✅
[D][WikiText] ARC-c  paper=40.78   registry=40.78   (bench_kl30_uniform) ✅
[D][WikiText] WG     paper=68.59   registry=68.59   (bench_kl30_uniform) ✅
[D][WikiText] MMLU   paper=40.6    registry=40.61   (bench_kl30_uniform) ✅
[D][WikiText] GSM8K  paper=7.35    registry=7.35    (bench_kl30_uniform) ✅
[D][WikiText] HS     paper=69.4    registry=NOT MATCHED ❌
[D][WikiText] PIQA   paper=75.5    registry=NOT MATCHED ❌
[D][C4]       PPL    paper=11.55   registry=11.554  (c4_kl30_s42_eval) ✅
[D][C4]       ARC-c  paper=43.09   registry=43.09   (c4_kl30_s42_eval) ✅
[D][C4]       WG     paper=68.67   registry=68.67   (c4_kl30_s42_eval) ✅
[D][C4]       MMLU   paper=39.95   registry=39.95   (c4_kl30_s42_eval) ✅
[D][C4]       GSM8K  paper=4.09    registry=4.09    (c4_kl30_s42_eval) ✅
[D][C4]       HS     paper=69.24   registry=69.24   (c4_kl30_s42_eval) ✅
[D][C4]       PIQA   paper=74.86   registry=75.03   (c4_kl30_s42_eval) ❌
```

**Table D flags:**
- `[D][WikiText] HS/PIQA`: The paper reports 69.4/75.5 for the WikiText-trained predictor. The only LLaMA KL30 uniform HS/PIQA registry entry (`kl30_uniform_hellaswag_piqa_v2`) gives 70.85/74.81, which does not match. No other registry entry contains 69.4% HellaSwag for KL30 uniform. Source of these specific values is untraced in the registry.
- `[D][C4] PIQA`: Paper says 74.86; registry (`c4_kl30_s42_eval`) gives 75.03. Discrepancy of **0.17pp**.

---

### TABLE E: Latency (tab:latency)

```
[E][Dense]        ms/fwd paper=119.11±0.57  registry=119.11±0.57  (latency_benchmark) ✅
[E][Dense]        tok/s  paper=17195         registry=17194.5      (latency_benchmark) ✅
[E][KL-pred-30%]  ms/fwd paper=126.64±0.70  registry=126.64±0.70  (latency_benchmark) ✅
[E][KL-pred-30%]  tok/s  paper=16172         registry=16171.8      (latency_benchmark) ✅
[E][KL-pred-50%]  ms/fwd paper=126.78±0.31  registry=126.78±0.31  (latency_benchmark) ✅
[E][KL-pred-50%]  tok/s  paper=16154         registry=16154.2      (latency_benchmark) ✅
[E][Pred+comp-30%] ms/fwd paper=129.94±0.75 registry=129.94±0.75  (latency_benchmark) ✅
[E][Pred+comp-30%] tok/s  paper=15761        registry=15761.4      (latency_benchmark) ✅
[E][Pred+comp-50%] ms/fwd paper=129.71±0.53 registry=129.71±0.53  (latency_benchmark) ✅
[E][Pred+comp-50%] tok/s  paper=15789        registry=15788.8      (latency_benchmark) ✅
```

---

## Summary

| Category | Count |
|---|---|
| **Total checks** | 77 |
| **Matches (✅)** | 62 |
| **Mismatches (❌)** | 3 |
| **Not found / unverifiable (⚠️)** | 12 |

### Mismatches (❌) — require correction

1. **[B][TEAL-30%-unif] PIQA**: Paper=72.80, registry (`teal_30pct_uniform_multiseed_eval`)=71.98. Discrepancy of 0.82pp. The registry stores `piqa` (not `piqa_acc_norm`); if both are acc_norm this is a real error. Needs recheck of whether paper used a different eval run.

2. **[D][WikiText] HS**: Paper=69.4, registry best match for LLaMA KL30 uniform is 70.85 (`kl30_uniform_hellaswag_piqa_v2`). No registry entry traces to 69.4. Discrepancy of 1.45pp.

3. **[D][C4] PIQA**: Paper=74.86, registry (`c4_kl30_s42_eval`)=75.03. Discrepancy of 0.17pp (possible rounding in earlier version of run).

### Not found / partially verifiable (⚠️)

- **Table A BCE Global** (ARC-c/WG/MMLU/GSM8K): `qwen14b_bce30_s42_eval` not in registry. PPL/HS/PIQA are verifiable; 4 downstream metrics are not.
- **Table A TEAL Uniform** (PPL/ARC-c/WG/MMLU): No Qwen14B TEAL 30% uniform 4-task eval registered. GSM8K/HS/PIQA are verifiable.
- **Table B KL-30%-uniform** (HS/PIQA ±std): Only seed 42 is individually registered. The 3-seed mean (71.07/74.95) cannot be fully reconstructed from registry; s123 and s456 HS/PIQA for LLaMA KL30 uniform are absent.
- **Table B TEAL-50%-uniform** (HS/PIQA): `bench_teal50_uniform_6task` not in registry.
- **Table D WikiText PIQA** (75.5): No registry match; the value 74.81 from `kl30_uniform_hellaswag_piqa_v2` differs by 0.69pp.

agentId: a3dc6f65833ecaedb (use SendMessage with to: 'a3dc6f65833ecaedb' to continue this agent)
&lt;usage>total_tokens: 86961
tool_uses: 30
duration_ms: 386627&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "1f1205d8-8c8b-43cc-a9a5-b52c0f08b07b",
  "isSidechain": false,
  "promptId": "de60ee45-84fe-40c7-ad5a-52baa3f09b49",
  "type": "user",
  "uuid": "f12609ad-b9e6-4750-a4a1-c558664d3560",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are cross-verifying paper data against a registry of experiment results. The registry metrics are in `/tmp/registry_metrics.json` (JSON dict: exp_id -> {metrics, spec, conclusion, status}).\n\nYour task: verify numbers in the following paper tables against the registry:\n\n## Table A: Qwen-2.5-14B (tab:14b in appendix.tex)\n\n```\nMethod & PPL↓ & ARC-c & WG & MMLU & GSM8K & HS & PIQA\nDense & 5.19 & 67.58 & 81.06 & 79.77 & 87.57 & 84.20 & 81.94\nGlobal KL (Ours) & 7.62 & 57.17 & 72.06 & 63.72 & 48.82 & 75.01 & 77.37  % exp_id: qwen14b_kl30_s42\nGlobal TEAL & 8.73 & 56.83 & 72.69 & 71.83 & 49.51 & 70.51 & 74.70      % exp_id: qwen14b_teal30_eval\nGlobal BCE & 8.76 & 57.59 & 72.61 & 71.67 & 53.07 & 53.43 & 68.28       % exp_id: qwen14b_bce30_s42_eval\nUniform KL (Ours) & 7.90 & 53.50 & 72.82 & 63.55 & 32.0±5.2 & 72.68±0.2 & 76.01±1.1  % exp_id: qwen14b_kl30_uniform\nUniform TEAL & 8.01 & 55.29 & 69.85 & 66.34 & 52.1 & 67.72 & 74.70       % exp_id: qwen14b_teal30_uniform\n```\n\nFor the Qwen dense baseline, look for `qwen14b_dense_baseline`, `qwen14b_dense_4task_v2`, `qwen14b_dense_hspiqa`.\nFor uniform KL with ±std (GSM8K, HS, PIQA), look for `qwen14b_kl30_s42_eval_uniform_v3`, `qwen14b_kl30_s123_eval_v5`, `qwen14b_kl30_s456_eval_v2` or similar. Also `qwen14b_kl30_s42_gsm8k_uniform`, `qwen14b_kl30_s456_gsm8k`, `qwen14b_kl30_uniform_hspiqa`.\nFor TEAL uniform, try `qwen14b_teal30_uniform_hspiqa`, `qwen14b_teal30_uniform_gsm8k`.\n\n## Table B: Extended Downstream (tab:downstream in appendix)\n\n```\nSparsity & Method & HellaSwag & PIQA\n0% Dense & 82.35 & 80.90\n30% KL uniform & 71.07±0.54 & 74.95±0.25   % exp_id: hellaswag_piqa_kl30_uniform (3-seed)\n30% TEAL uniform & 63.31 & 72.80            % exp_id: bench_teal30_uniform_6task\n30% BCE isocompute & 62.81 & 74.21          % exp_id: bce_isocompute_30u_hellaswag_piqa\n50% KL global & 58.95 & 69.48               % exp_id: hellaswag_piqa_kl50_global\n50% KL uniform & 56.66 & 69.10              % exp_id: hellaswag_piqa_kl50_uniform\n50% TEAL uniform & 39.35 & 63.66            % exp_id: bench_teal50_uniform_6task\n```\n\nLook for experiments with these exp_ids or variants like `kl30_uniform_hellaswag_piqa_v2`, `kl50_global_hellaswag_piqa_v2`, `dense_baseline_hellaswag_piqa`, `bce_isocompute_hellaswag_piqa_v2`.\n\n## Table C: OOD Evaluation (tab:ood in appendix)\n\n```\nMethod & C4 PPL↓\nDense & 9.21\n30% KL predictor & 16.03±0.01   % exp_id: c4_ood_kl30_s42, c4_ood_kl30_s123\n50% KL predictor & 18.40         % exp_id: eval_c4_ood_kl50\n50% TEAL vanilla & 38.75\n```\n\nLook for `c4_ood_kl30_s42_v2`, `c4_ood_kl30_s123_v2`, `eval_c4_ood_kl50`, `c4_ood_dense_baseline_v2`. Also check OOD uniform table: `c4_ood_kl30_uniform_s42/s123/s456`.\n\n## Table D: C4 Control (tab:c4_control in appendix)\n\n```\nTraining Data & PPL↓ & ARC-c & WG & MMLU & GSM8K & HS / PIQA\nWikiText-103 & 8.82 & 40.78 & 68.59 & 40.6 & 7.35 & 69.4 / 75.5\nC4 & 11.55 & 43.09 & 68.67 & 39.95 & 4.09 & 69.24 / 74.86\n```\n\nLook for `c4_kl30_s42_eval`, `c4_kl30_s42`, `c4_control_eval` etc. The WikiText row should match bench_kl30_uniform.\n\n## Table E: Latency (tab:latency in appendix)\n\n```\nDense: 119.11±0.57 ms/fwd, 17195 tok/s\nKL pred 30%: 126.64±0.70, 16172\nKL pred 50%: 126.78±0.31, 16154\nPred+comp 30%: 129.94±0.75, 15761\nPred+comp 50%: 129.71±0.53, 15789\n```\n\nLook for `latency_benchmark` or `latency_bench`.\n\nFor each data point, output:\n```\n[TABLE][ROW] [METRIC] paper=[value] registry=[value] (exp_id) ✅/❌/⚠️\n```\n\nAt the end, provide a summary of total checks, matches, mismatches, not found.",
    "agentId": "a3dc6f65833ecaedb",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the data needed to produce the full verification report.\n\n---\n\n## Cross-Verification Report\n\n---\n\n### TABLE A: Qwen-2.5-14B (tab:14b)\n\n**Dense Baseline** (qwen14b_dense_baseline + qwen14b_dense_hspiqa)\n\n```\n[A][Dense] PPL    paper=5.19    registry=5.1854 (qwen14b_dense_baseline) ✅\n[A][Dense] ARC-c  paper=67.58   registry=67.58  (qwen14b_dense_baseline) ✅\n[A][Dense] WG     paper=81.06   registry=81.06  (qwen14b_dense_baseline) ✅\n[A][Dense] MMLU   paper=79.77   registry=79.77  (qwen14b_dense_baseline) ✅\n[A][Dense] GSM8K  paper=87.57   registry=87.57  (qwen14b_dense_baseline) ✅\n[A][Dense] HS     paper=84.20   registry=84.21  (qwen14b_dense_hspiqa)   ✅\n[A][Dense] PIQA   paper=81.94   registry=81.94  (qwen14b_dense_hspiqa)   ✅\n```\n\n**Global KL (qwen14b_kl30_s42_eval + qwen14b_kl30_global_hspiqa)**\n\n```\n[A][KL-Global] PPL    paper=7.62    registry=7.6232  (qwen14b_kl30_s42_eval) ✅\n[A][KL-Global] ARC-c  paper=57.17   registry=57.17   (qwen14b_kl30_s42_eval) ✅\n[A][KL-Global] WG     paper=72.06   registry=72.06   (qwen14b_kl30_s42_eval) ✅\n[A][KL-Global] MMLU   paper=63.72   registry=63.72   (qwen14b_kl30_s42_eval) ✅\n[A][KL-Global] GSM8K  paper=48.82   registry=48.82   (qwen14b_kl30_s42_eval) ✅\n[A][KL-Global] HS     paper=75.01   registry=75.01   (qwen14b_kl30_global_hspiqa) ✅\n[A][KL-Global] PIQA   paper=77.37   registry=77.37   (qwen14b_kl30_global_hspiqa) ✅\n```\n\n**Global TEAL (qwen14b_teal30_eval + qwen14b_teal30_global_hspiqa)**\n\n```\n[A][TEAL-Global] PPL    paper=8.73    registry=8.7332  (qwen14b_teal30_eval) ✅\n[A][TEAL-Global] ARC-c  paper=56.83   registry=56.83   (qwen14b_teal30_eval) ✅\n[A][TEAL-Global] WG     paper=72.69   registry=72.69   (qwen14b_teal30_eval) ✅\n[A][TEAL-Global] MMLU   paper=71.83   registry=71.83   (qwen14b_teal30_eval) ✅\n[A][TEAL-Global] GSM8K  paper=49.51   registry=49.51   (qwen14b_teal30_eval) ✅\n[A][TEAL-Global] HS     paper=70.51   registry=70.51   (qwen14b_teal30_global_hspiqa) ✅\n[A][TEAL-Global] PIQA   paper=74.70   registry=74.70   (qwen14b_teal30_global_hspiqa) ✅\n```\n\n**Global BCE (qwen14b_bce30_s42 for PPL; qwen14b_bce30_global_hspiqa for HS/PIQA; exp_id qwen14b_bce30_s42_eval NOT IN REGISTRY for ARC-c/WG/MMLU/GSM8K)**\n\n```\n[A][BCE-Global] PPL    paper=8.76    registry=8.76  (qwen14b_bce30_s42, teal_global_ppl) ✅\n[A][BCE-Global] ARC-c  paper=57.59   registry=NOT FOUND (qwen14b_bce30_s42_eval missing) ⚠️\n[A][BCE-Global] WG     paper=72.61   registry=NOT FOUND ⚠️\n[A][BCE-Global] MMLU   paper=71.67   registry=NOT FOUND ⚠️\n[A][BCE-Global] GSM8K  paper=53.07   registry=NOT FOUND ⚠️\n[A][BCE-Global] HS     paper=53.43   registry=53.43  (qwen14b_bce30_global_hspiqa) ✅\n[A][BCE-Global] PIQA   paper=68.28   registry=68.28  (qwen14b_bce30_global_hspiqa) ✅\n```\n\n**Uniform KL (3-seed s42/s123/s456: qwen14b_kl30_s42_eval_uniform_v3, qwen14b_kl30_s123_eval_v5, qwen14b_kl30_s456_eval_v3)**\n\n```\n[A][KL-Uniform] PPL    paper=7.90        registry=7.90±0.03  (3-seed mean) ✅\n[A][KL-Uniform] ARC-c  paper=53.50       registry=53.50±1.83 (3-seed mean) ✅\n[A][KL-Uniform] WG     paper=72.82       registry=72.82±1.41 (3-seed mean) ✅\n[A][KL-Uniform] MMLU   paper=63.55       registry=63.55±1.23 (3-seed mean) ✅\n[A][KL-Uniform] GSM8K  paper=30.9±6.8*  registry=30.8±6.6 (s42=35.5, s456=26.1, n=2) ✅\n[A][KL-Uniform] HS     paper=72.68±0.2   registry=72.68±0.19 (3-seed) ✅\n[A][KL-Uniform] PIQA   paper=76.01±1.1   registry=76.01±1.09 (3-seed) ✅\n```\n\n*Note: GSM8K n=2 because s123 incomplete; paper footnote acknowledges this. Registry gives mean=30.8 vs paper 30.9 (0.1pp rounding), std=6.6 vs 6.8 (0.2pp rounding). Both within rounding.*\n\n**Uniform TEAL (qwen14b_teal30_uniform_gsm8k + qwen14b_teal30_uniform_hspiqa; ARC-c/WG/MMLU/PPL NOT IN REGISTRY)**\n\n```\n[A][TEAL-Uniform] PPL    paper=8.01    registry=NOT FOUND ⚠️\n[A][TEAL-Uniform] ARC-c  paper=55.29   registry=NOT FOUND ⚠️\n[A][TEAL-Uniform] WG     paper=69.85   registry=NOT FOUND ⚠️\n[A][TEAL-Uniform] MMLU   paper=66.34   registry=NOT FOUND ⚠️\n[A][TEAL-Uniform] GSM8K  paper=52.1    registry=52.1  (qwen14b_teal30_uniform_gsm8k) ✅\n[A][TEAL-Uniform] HS     paper=67.72   registry=67.72 (qwen14b_teal30_uniform_hspiqa) ✅\n[A][TEAL-Uniform] PIQA   paper=74.70   registry=74.70 (qwen14b_teal30_uniform_hspiqa) ✅\n```\n\n---\n\n### TABLE B: Extended Downstream (tab:downstream)\n\n```\n[B][Dense]         HS   paper=82.35   registry=82.35  (dense_baseline_hellaswag_piqa) ✅\n[B][Dense]         PIQA paper=80.90   registry=80.90  (dense_baseline_hellaswag_piqa) ✅\n[B][KL-30%-unif]   HS   paper=71.07±0.54  registry=70.85 (s42 only; kl30_uniform_hellaswag_piqa_v2) ⚠️\n[B][KL-30%-unif]   PIQA paper=74.95±0.25  registry=74.81 (s42 only) ⚠️\n[B][TEAL-30%-unif] HS   paper=63.31   registry=63.31  (teal_30pct_uniform_multiseed_eval) ✅\n[B][TEAL-30%-unif] PIQA paper=72.80   registry=71.98  (teal_30pct_uniform_multiseed_eval) ❌\n[B][BCE-30%-iso]   HS   paper=62.81   registry=62.81  (bce_isocompute_hellaswag_piqa_v2) ✅\n[B][BCE-30%-iso]   PIQA paper=74.21   registry=74.21  (bce_isocompute_hellaswag_piqa_v2) ✅\n[B][KL-50%-global] HS   paper=58.95   registry=58.95  (kl50_global_hellaswag_piqa_v2) ✅\n[B][KL-50%-global] PIQA paper=69.48   registry=69.48  (kl50_global_hellaswag_piqa_v2) ✅\n[B][KL-50%-unif]   HS   paper=56.66   registry=56.66  (kl50_uniform_hellaswag_piqa) ✅\n[B][KL-50%-unif]   PIQA paper=69.10   registry=69.10  (kl50_uniform_hellaswag_piqa) ✅\n[B][TEAL-50%-unif] HS   paper=39.35   registry=NOT FOUND (bench_teal50_uniform_6task missing) ⚠️\n[B][TEAL-50%-unif] PIQA paper=63.66   registry=NOT FOUND ⚠️\n```\n\n**Table B flags:**\n- `[B][KL-30%-unif]`: Only seed 42 (s42=70.85 HS, 74.81 PIQA) is registered individually. The paper reports a 3-seed mean (71.07/74.95). The s123 and s456 HS/PIQA runs for LLaMA KL30 uniform are not registered under any exp_id. The paper values are not individually verifiable from registry alone; they are plausible given s42 is within 0.2pp of the mean.\n- `[B][TEAL-30%-unif] PIQA`: Registry shows 71.98; paper shows 72.80. This is a **0.82pp discrepancy**. The registry entry `teal_30pct_uniform_multiseed_eval` stores `piqa` (=71.98) not `piqa_acc_norm`. It is likely both refer to acc_norm but there is a genuine numerical mismatch.\n- `[B][TEAL-50%-unif]`: The exp_id `bench_teal50_uniform_6task` does not exist in the registry; only bench_teal50 (global, no HS/PIQA) is present.\n\n---\n\n### TABLE C: OOD Evaluation (tab:ood)\n\n```\n[C][Dense]        C4-PPL paper=9.21     registry=9.2075 (c4_ood_dense_baseline_v2) ✅\n[C][KL-30%-pred]  C4-PPL paper=16.03±0.01  registry=16.033±0.010 (c4_ood_kl30_s42_v2=16.040, c4_ood_kl30_s123_v2=16.026) ✅\n[C][KL-50%-pred]  C4-PPL paper=18.40    registry=18.401 (eval_c4_ood_kl50) ✅\n[C][TEAL-50%-van] C4-PPL paper=38.75    registry=38.750 (eval_c4_ood_kl50) ✅\n```\n\n*Appendix paragraph on uniform allocation: paper says 18.22/16.37/16.36 → mean 16.98±1.07. Registry: c4_ood_kl30_uniform_s42=18.22, s123=16.37, s456=16.36, computed mean=16.98±1.07. ✅ (perfect match)*\n\n---\n\n### TABLE D: C4 Training Data Control (tab:c4_control)\n\n```\n[D][WikiText] PPL    paper=8.82    registry=8.8157  (bench_kl30_uniform) ✅\n[D][WikiText] ARC-c  paper=40.78   registry=40.78   (bench_kl30_uniform) ✅\n[D][WikiText] WG     paper=68.59   registry=68.59   (bench_kl30_uniform) ✅\n[D][WikiText] MMLU   paper=40.6    registry=40.61   (bench_kl30_uniform) ✅\n[D][WikiText] GSM8K  paper=7.35    registry=7.35    (bench_kl30_uniform) ✅\n[D][WikiText] HS     paper=69.4    registry=NOT MATCHED ❌\n[D][WikiText] PIQA   paper=75.5    registry=NOT MATCHED ❌\n[D][C4]       PPL    paper=11.55   registry=11.554  (c4_kl30_s42_eval) ✅\n[D][C4]       ARC-c  paper=43.09   registry=43.09   (c4_kl30_s42_eval) ✅\n[D][C4]       WG     paper=68.67   registry=68.67   (c4_kl30_s42_eval) ✅\n[D][C4]       MMLU   paper=39.95   registry=39.95   (c4_kl30_s42_eval) ✅\n[D][C4]       GSM8K  paper=4.09    registry=4.09    (c4_kl30_s42_eval) ✅\n[D][C4]       HS     paper=69.24   registry=69.24   (c4_kl30_s42_eval) ✅\n[D][C4]       PIQA   paper=74.86   registry=75.03   (c4_kl30_s42_eval) ❌\n```\n\n**Table D flags:**\n- `[D][WikiText] HS/PIQA`: The paper reports 69.4/75.5 for the WikiText-trained predictor. The only LLaMA KL30 uniform HS/PIQA registry entry (`kl30_uniform_hellaswag_piqa_v2`) gives 70.85/74.81, which does not match. No other registry entry contains 69.4% HellaSwag for KL30 uniform. Source of these specific values is untraced in the registry.\n- `[D][C4] PIQA`: Paper says 74.86; registry (`c4_kl30_s42_eval`) gives 75.03. Discrepancy of **0.17pp**.\n\n---\n\n### TABLE E: Latency (tab:latency)\n\n```\n[E][Dense]        ms/fwd paper=119.11±0.57  registry=119.11±0.57  (latency_benchmark) ✅\n[E][Dense]        tok/s  paper=17195         registry=17194.5      (latency_benchmark) ✅\n[E][KL-pred-30%]  ms/fwd paper=126.64±0.70  registry=126.64±0.70  (latency_benchmark) ✅\n[E][KL-pred-30%]  tok/s  paper=16172         registry=16171.8      (latency_benchmark) ✅\n[E][KL-pred-50%]  ms/fwd paper=126.78±0.31  registry=126.78±0.31  (latency_benchmark) ✅\n[E][KL-pred-50%]  tok/s  paper=16154         registry=16154.2      (latency_benchmark) ✅\n[E][Pred+comp-30%] ms/fwd paper=129.94±0.75 registry=129.94±0.75  (latency_benchmark) ✅\n[E][Pred+comp-30%] tok/s  paper=15761        registry=15761.4      (latency_benchmark) ✅\n[E][Pred+comp-50%] ms/fwd paper=129.71±0.53 registry=129.71±0.53  (latency_benchmark) ✅\n[E][Pred+comp-50%] tok/s  paper=15789        registry=15788.8      (latency_benchmark) ✅\n```\n\n---\n\n## Summary\n\n| Category | Count |\n|---|---|\n| **Total checks** | 77 |\n| **Matches (✅)** | 62 |\n| **Mismatches (❌)** | 3 |\n| **Not found / unverifiable (⚠️)** | 12 |\n\n### Mismatches (❌) — require correction\n\n1. **[B][TEAL-30%-unif] PIQA**: Paper=72.80, registry (`teal_30pct_uniform_multiseed_eval`)=71.98. Discrepancy of 0.82pp. The registry stores `piqa` (not `piqa_acc_norm`); if both are acc_norm this is a real error. Needs recheck of whether paper used a different eval run.\n\n2. **[D][WikiText] HS**: Paper=69.4, registry best match for LLaMA KL30 uniform is 70.85 (`kl30_uniform_hellaswag_piqa_v2`). No registry entry traces to 69.4. Discrepancy of 1.45pp.\n\n3. **[D][C4] PIQA**: Paper=74.86, registry (`c4_kl30_s42_eval`)=75.03. Discrepancy of 0.17pp (possible rounding in earlier version of run).\n\n### Not found / partially verifiable (⚠️)\n\n- **Table A BCE Global** (ARC-c/WG/MMLU/GSM8K): `qwen14b_bce30_s42_eval` not in registry. PPL/HS/PIQA are verifiable; 4 downstream metrics are not.\n- **Table A TEAL Uniform** (PPL/ARC-c/WG/MMLU): No Qwen14B TEAL 30% uniform 4-task eval registered. GSM8K/HS/PIQA are verifiable.\n- **Table B KL-30%-uniform** (HS/PIQA ±std): Only seed 42 is individually registered. The 3-seed mean (71.07/74.95) cannot be fully reconstructed from registry; s123 and s456 HS/PIQA for LLaMA KL30 uniform are absent.\n- **Table B TEAL-50%-uniform** (HS/PIQA): `bench_teal50_uniform_6task` not in registry.\n- **Table D WikiText PIQA** (75.5): No registry match; the value 74.81 from `kl30_uniform_hellaswag_piqa_v2` differs by 0.69pp."
      }
    ],
    "totalDurationMs": 386627,
    "totalTokens": 86961,
    "totalToolUseCount": 30,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1355,
      "cache_read_input_tokens": 80430,
      "output_tokens": 5175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1355
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5175,
          "cache_read_input_tokens": 80430,
          "cache_creation_input_tokens": 1355,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1355,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 1,
      "searchCount": 0,
      "bashCount": 29,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "1f1205d8-8c8b-43cc-a9a5-b52c0f08b07b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01",
  "version": "2.1.126",
  "gitBranch": "master"
}
````

</details>

---


### Runtime record

_source line 62_

```json
{
  "type": "last-prompt",
  "leafUuid": "f12609ad-b9e6-4750-a4a1-c558664d3560",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01"
}
```

---


### Runtime record

_source line 63_

```json
{
  "type": "ai-title",
  "aiTitle": "Final data consistency audit registry vs paper",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01"
}
```

---


### Assistant

_source line 64 · 2026-05-24T01:19:48.558Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me also verify the inline numbers in the prose (abstract, introduction, experiments body text, conclusion). Let me launch one more agent for that.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f12609ad-b9e6-4750-a4a1-c558664d3560",
  "isSidechain": false,
  "requestId": "req_011CbLWonk48aqbAdxUYKAko",
  "type": "assistant",
  "uuid": "6c482b87-6771-4c1c-8902-3495ac3437f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EoV3cC4EvojmHj9WNLTqM7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7125,
      "cache_read_input_tokens": 82961,
      "output_tokens": 1993,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7125,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1993,
          "cache_read_input_tokens": 82961,
          "cache_creation_input_tokens": 7125,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7125
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

_source line 65 · 2026-05-24T01:19:49.096Z_

Now let me verify the inline prose numbers (abstract, introduction, experiments body text, conclusion).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c482b87-6771-4c1c-8902-3495ac3437f7",
  "isSidechain": false,
  "requestId": "req_011CbLWonk48aqbAdxUYKAko",
  "type": "assistant",
  "uuid": "18b5be64-8b04-45ca-b5c3-0e824dc6a0d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EoV3cC4EvojmHj9WNLTqM7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7125,
      "cache_read_input_tokens": 82961,
      "output_tokens": 1993,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7125,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1993,
          "cache_read_input_tokens": 82961,
          "cache_creation_input_tokens": 7125,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7125
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

_source line 66 · 2026-05-24T01:20:34.747Z_

<details open><summary>🔧 Tool call — Agent · `toolu_014Hxk77M4CwKNx9EagMdPbj`</summary>

````json
{
  "description": "Verify inline prose numbers",
  "prompt": "You are cross-verifying paper inline numbers against a registry of experiment results. The registry metrics are in `/tmp/registry_metrics.json` (JSON dict: exp_id -> {metrics, spec, conclusion, status}).\n\nYour task: verify ALL quantitative claims made in the **prose text** (not table cells, which are verified separately) of these paper sections. For each numeric claim, find the registry source and check correctness.\n\n## Claims to verify:\n\n### Abstract (abstract.tex)\n1. \"14.5% over TEAL at matched sparsity\" — check: (TEAL_PPL - KL_PPL) / TEAL_PPL. Need TEAL PPL at matched sparsity (28.5% actual). Look for `teal_28.5pct_sanity` or compute from TEAL at 28.5%.\n2. \"MMLU −5.2pp on 8B\" — check: KL_MMLU - Dense_MMLU or KL_MMLU - TEAL_MMLU?  Paper says \"knowledge-intensive regression (MMLU −5.2pp on 8B)\". Context: probably TEAL_MMLU - KL_MMLU = 45.86 - 40.7 = 5.16 ≈ 5.2pp\n3. \"GSM8K −20.1pp on 14B\" — check: probably TEAL_GSM8K - KL_GSM8K for Qwen14B uniform. TEAL=52.1, KL=32.0. Diff=20.1pp\n4. \"+67.2M params\" — architecture claim, not registry\n5. \"PPL gap ≤0.65pp\" — C1 ablation claim. Check: max PPL gap between C1 and KL across seeds at 30%. From Table 3: s42 gap = 9.45-8.82=0.63, s123 gap=8.84-8.83=0.01, s456 gap=8.82-8.79=0.03. Max=0.63pp. Paper says ≤0.65pp. But caption says \"max Δ≤1.70pp at 30%\". Verify.\n6. \"46--68% from magnitude-based targets\" — Jaccard distance range. Look for `c1_mask_overlap` or mask divergence experiments.\n7. \"75.9M params, <1% of base\" — architecture constant\n\n### Introduction (introduction.tex)\n8. \"14.5% at matched sparsity (8.81 vs. 10.30, both at 28.5%)\" — need TEAL PPL at 28.5% actual sparsity. Look for `teal_28.5pct_sanity`.\n9. \"MMLU 40.7±1.3% vs. 65.3% dense\" — KL MMLU from 3-seed (matches Table 2) vs dense. Dense MMLU = 65.27, paper says 65.3%.\n10. \"7.3× MMLU σ\" — global MMLU std / uniform MMLU std. Global: 9.5, Uniform: 1.3. 9.5/1.3 = 7.31 ≈ 7.3×\n11. \"−17.3% PPL on Mistral\" — (TEAL_PPL - KL_PPL) / TEAL_PPL for Mistral 30%. TEAL=8.38, KL=6.93. (8.38-6.93)/8.38 = 17.3%\n12. \"GSM8K −20.1pp, σ=5.2pp\" for Qwen14B\n13. \"MMLU −2.8pp\" for Qwen14B — TEAL_MMLU - KL_MMLU for 14B uniform. TEAL=66.34, KL=63.55. Diff=2.79≈2.8pp\n14. \"6.4% latency overhead\" — from latency table\n\n### Experiments prose (experiments.tex body text, not table cells)\n15. \"PPL 8.81±0.02 (3-seed), a 14.5% reduction over TEAL at matched actual sparsity (8.81 vs. 10.30, both at 28.5%)\" — verify TEAL at 28.5% = 10.30\n16. \"MMLU 40.7±1.3%, 3-seed\" — matches Table 2\n17. \"35.7±9.5%\" for global MMLU — matches Table 2  \n18. \"L31 retention 28.4%\" — look for perlayer_sparsity_analysis\n19. \"11.92 vs. 23.90, 50% reduction\" — (23.90-11.92)/23.90 = 50.1%\n20. \"28.13±0.20\" for BCE at 2700 steps — matches Table 2\n21. \"2.39× worse than KL (11.79)\" — 28.13/11.79 = 2.386 ≈ 2.39×. But wait, text says \"KL (11.79)\" at 50% — this should be from bench_kl50_global\n22. \"F1 (0.613 vs. 0.540)\" — look for `kl_bce_f1_oracle` or `f1_oracle_analysis`\n23. \"139% worse PPL\" — (28.13-11.79)/11.79 = 138.7% ≈ 139%\n24. \"Jaccard distance averages 68% at 50%\" — from mask overlap analysis\n25. \"cross-seed variation (36.3%)\" — cross-seed Jaccard\n26. \"Gumbel-Sigmoid outperforms STE by 33.8% (11.79 vs. 15.77)\" — (15.77-11.79)/11.79 = 33.8%\n27. \"forward KL outperforms JSD (+6.4%) and reverse KL (+8.6%)\" — (12.54-11.79)/11.79=6.4%, (12.80-11.79)/11.79=8.6%\n28. \"$K=16$ achieves the lowest PPL (8.67±0.02 vs. E2E 8.81±0.02)\" — from K-curve\n29. \"the full coupling range (2.08 PPL)\" — K=2 worst (10.75) - K=16 best (8.67) = 2.08\n30. \"signal type gap (9.47 PPL)\" — MSE PPL(18.52) - K=1 KL PPL(9.05) = 9.47\n31. \"$-$17.3\\%, 3-seed\" for Mistral\n32. \"GSM8K 32.0±5.2 vs. 52.1\" for Qwen14B\n33. \"$148×$ vs. $112×$ compression\" — d_model/d_b ratios. For Qwen-14B: d_model=5120(?)/d_b=128 or d_ff/d_b? Need to check architecture.\n\n### Conclusion (conclusion.tex)\n34. \"14.5%\" — same claim as above\n\nFor each claim, output:\n```\n[SECTION] Claim: \"[text]\" → computed=[value] paper=[value] ✅/❌\n```\n\nFocus on numerical accuracy. Tolerance ≤0.1pp for derived calculations.",
  "model": "sonnet"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18b5be64-8b04-45ca-b5c3-0e824dc6a0d9",
  "isSidechain": false,
  "requestId": "req_011CbLWonk48aqbAdxUYKAko",
  "type": "assistant",
  "uuid": "a5b4b084-c25b-4756-bab6-1fd4be61c515",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EoV3cC4EvojmHj9WNLTqM7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7125,
      "cache_read_input_tokens": 82961,
      "output_tokens": 1993,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7125,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1993,
          "cache_read_input_tokens": 82961,
          "cache_creation_input_tokens": 7125,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7125
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

_source line 67 · 2026-05-24T01:34:47.351Z_

<details><summary>↩ Tool result · `toolu_014Hxk77M4CwKNx9EagMdPbj`</summary>

```text
Here is the complete verification report for all quantitative prose claims:

---

## Verification Results

### Abstract (`abstract.tex`)

**[ABSTRACT] Claim 1:** "14.5% over TEAL at matched sparsity" → computed=(10.30−8.81)/10.30×100=**14.5%** (using rounded 3-seed mean 8.81 and TEAL-28.5%=10.30 from `teal_28.5pct_sanity`). Raw 3-seed mean is 8.8137; exact reduction is 14.43%, which rounds to 14.4% but paper consistently uses the 2dp rounded PPLs. paper=14.5% **✅** (borderline; within rounding tolerance)

**[ABSTRACT] Claim 2:** "MMLU −5.2pp on 8B" → TEAL uniform MMLU=45.86% (`teal_30pct_uniform_multiseed_eval`), KL 3-seed MMLU=40.7%, diff=5.16pp≈**5.2pp** ✅

**[ABSTRACT] Claim 3:** "GSM8K −21.2pp on 14B" → TEAL GSM8K=52.08% (`qwen14b_teal30_uniform_gsm8k`), KL 2-seed mean=(35.71+26.08)/2=30.9%, diff=**21.2pp** ✅

**[ABSTRACT] Claim 4:** "+67.2M params" — architectural constant, not directly in registry. Cited from `latency_benchmark` appendix prose.

**[ABSTRACT] Claim 5:** "PPL gap ≤0.65pp" → actual max PPL gap across seeds: s42=9.4463−8.8157=**0.6306pp**, s123=0.01pp, s456=0.03pp. All ≤0.65 ✅. However, the Table 3 footnote says "(gap 0.65pp)" for s42, but registry gives 0.63pp. The "≤0.65pp" upper bound holds, but the footnote value is slightly imprecise — the actual is **0.63pp**, not 0.65pp. ⚠️

**[ABSTRACT] Claim 6:** "46--68% from magnitude-based targets" → 30% sparsity: mean Jaccard distance=**46.3%** (`mask_stats_30pct_64samples.json`); 50% sparsity: mean Jaccard distance=**68.2%** (`mask_stats_50pct_64samples.json`). Range=46–68% ✅

**[ABSTRACT] Claim 7:** "75.9M params, <1% of base" — architecture constant. 32 layers × 2.37M params/layer = 75.84M ≈ 75.9M. <1% of LLaMA-8B (7.98B active params). ✅

---

### Introduction (`introduction.tex`)

**[INTRO] Claim 8:** "14.5% at matched sparsity (8.81 vs. 10.30, both at 28.5%)" → same as Abstract claim 1. KL 3-seed mean=8.8137≈8.81, TEAL-28.5%=10.30, (10.30−8.81)/10.30=14.47%≈**14.5%** ✅

**[INTRO] Claim 9:** "MMLU 40.7±1.3% vs. 65.3% dense" → s42=0.4061, s123=0.3944, s456=0.4198; mean=40.68%≈**40.7%**, std(ddof=1)=1.3% ✅. Dense=65.27%≈**65.3%** (`bench_dense`) ✅

**[INTRO] Claim 10:** "7.3× MMLU σ" → global MMLU std=9.5pp, uniform MMLU std=1.3pp; 9.5/1.3=**7.31×**≈7.3× ✅

**[INTRO] Claim 11:** "−17.3% PPL on Mistral" → s42=6.7733 (`mistral_kl30_teal_global`), s123=7.1491, s456=6.8752; mean=6.9325; TEAL=8.3807 (`mistral_teal30_baseline`). (8.3807−6.9325)/8.3807=**17.3%** ✅

**[INTRO] Claim 12:** "GSM8K −21.2pp, σ=6.8pp" for Qwen14B → 2-seed (s42=35.71%, s456=26.08%); mean=30.9%, std(ddof=1)=**6.8pp**; TEAL=52.1%; diff=**21.2pp** ✅

**[INTRO] Claim 13:** "MMLU −2.8pp" for Qwen14B → Appendix Table 14b reports KL uniform MMLU=63.55%, TEAL uniform MMLU=66.34%, diff=2.79pp≈**2.8pp** ✅ in context. However, **TEAL uniform MMLU=66.34% is not directly in the registry** (nearest entry is `qwen14b_teal275_uniform_eval_v3` at 67.38%). The table value 66.34 cannot be independently verified from registry alone. ⚠️

**[INTRO] Claim 14:** "6.4% latency overhead" → `latency_benchmark`: KL-50%=126.78ms, dense=119.11ms; (126.78−119.11)/119.11=**6.44%**≈6.4% ✅. At 30%: 6.32%; the 6.4% specifically refers to the 50% sparsity row (per appendix).

---

### Experiments prose (`experiments.tex`)

**[EXP] Claim 15:** "PPL 8.81±0.02 (3-seed), a 14.5% reduction over TEAL at matched actual sparsity (8.81 vs. 10.30, both at 28.5%)" → mean=8.8137≈**8.81**, std(ddof=1)=0.018≈**0.02**; TEAL-28.5%=**10.30** ✅

**[EXP] Claim 16:** "MMLU 40.7±1.3%, 3-seed" → confirmed ✅ (same as claim 9)

**[EXP] Claim 17:** "35.7±9.5%" for global MMLU → s42=25.27%, s123=38.07%, s456=43.82%; mean=**35.72%**, std(ddof=1)=**9.5%** ✅

**[EXP] Claim 18:** "L31 retention 28.4%" → from figure caption (Appendix, `app:retention`): "retention dropping to 28.4% (L31) even at 30% sparsity." No registry exp_id `perlayer_sparsity_analysis` found; value comes from figure data not directly registered. **Cannot verify from registry** ⚠️

**[EXP] Claim 19:** "11.92 vs. 23.90, 50% reduction" → KL 3-seed uniform 50%: mean=(11.963+11.83+11.9604)/3=**11.918**≈11.92, std=0.076≈0.07 ✅; TEAL uniform 50%=**23.90** (`training_free_baselines.uniform_50pct_ppl`) ✅; (23.90−11.92)/23.90=**50.1%** ✅

**[EXP] Claim 20:** "28.13±0.20" BCE at 2700 steps → s42=27.9696, s123=28.0627, s456=28.3503; mean=28.1275→**28.13**, std(ddof=1)=0.1985→**0.20** (0.1985 at 2dp rounds up to 0.20) ✅

**[EXP] Claim 21:** "2.39× worse than KL (11.79)" → 28.13/11.79=**2.386×**≈2.39× ✅ (KL=`bench_kl50_global` s42=11.7933≈11.79)

**[EXP] Claim 22:** "F1 (0.613 vs. 0.540)" → `kl_bce_f1_oracle`: BCE_F1=**0.6128**≈0.613, KL_F1=**0.5397**≈0.540 ✅

**[EXP] Claim 23:** "139% worse PPL" → (28.13−11.79)/11.79×100=**138.6%**≈139% ✅

**[EXP] Claim 24:** "Jaccard distance averages 68% at 50%" → `mask_stats_50pct_64samples.json`: jaccard_distance_mean=**0.6824=68.24%** ✅

**[EXP] Claim 25:** "cross-seed variation (36.3%)" → appendix §Cross-Seed Mask Consistency: "mean cross-seed Jaccard distance is 0.363 (IoU=0.637)". Source exp_id `cross_seed_jaccard_kl30` not in registry, but value consistent with appendix text and independently stated. ✅

**[EXP] Claim 26:** "Gumbel-Sigmoid outperforms STE by 33.8% (11.79 vs. 15.77)" → (15.77−11.79)/11.79×100=**33.8%** ✅ (`ste_baseline_s42`: teal_sparse_ppl=15.77)

**[EXP] Claim 27:** "forward KL outperforms JSD (+6.4%) and reverse KL (+8.6%)" → JSD_50%=12.54: (12.54−11.79)/11.79×100=**6.4%** ✅; RevKL_50%=12.80: (12.80−11.79)/11.79×100=**8.6%** ✅. Note: JSD/RevKL 50% values (12.54, 12.80) appear only in the ablation table, with no dedicated registry exp_ids; the computation is internally consistent.

**[EXP] Claim 28:** "K=16 achieves the lowest PPL (8.67±0.02 vs. E2E 8.81±0.02)" → K=16 3-seed: s42=8.6737 (`perlayer_kl_k16_eval_final2`), s123=8.6939, s456=8.655; mean=**8.6742**≈8.67, std(ddof=1)=0.0195≈**0.02** ✅

**[EXP] Claim 29:** "the full coupling range (2.08 PPL)" → K=2 3-seed mean=10.754, K=16 3-seed mean=8.674; range=**2.080** ✅

**[EXP] Claim 30:** "signal type gap (9.47 PPL)" → MSE=18.52, K=1 per-layer KL=9.05; gap=**9.47** ✅

**[EXP] Claim 31:** "−17.3%, 3-seed" for Mistral → confirmed same as claim 11 ✅

**[EXP] Claim 32:** "GSM8K 32.0±5.2 vs. 52.1 for Qwen14B" — The actual paper text (`experiments.tex` line 195) reads **"30.9±6.8 vs. 52.1, n=2"**, not "32.0±5.2" as stated in the task. Registry confirms: 2-seed mean=30.9%, std(ddof=1)=6.8%, TEAL=52.1% ✅. The verification task prompt had an outdated version of this number; the current paper text is correct.

**[EXP] Claim 33:** "148× vs. 112× compression" → LLaMA-8B: d_ff=14336, d_b=128, ratio=**112** ✅. Qwen-14B claim of **148×** is **inconsistent with registry**: `qwen14b_kl30_s123` reports `trainable_params='117M (0.793%)'`; 117M/48 layers ≈ 2.44M per layer; with d_model=5120, d_b=128: implied d_ff≈13,923, ratio≈**109×**, not 148×. A ratio of 148 would require d_ff=18,944 and ~148M total trainable params, contradicting the 117M figure. **❌**

---

### Conclusion (`conclusion.tex`)

**[CONCLUSION] Claim 34:** "14.5%" → same basis as all prior 14.5% claims ✅

---

## Summary of Issues Found

| # | Claim | Status | Issue |
|---|-------|--------|-------|
| 5 | "PPL gap ≤0.65pp" / footnote "(gap 0.65pp)" | ⚠️ | Actual s42 gap = 0.63pp (registry: 9.4463−8.8157=0.6306). The ≤0.65pp bound holds, but the footnote's stated value 0.65pp is imprecise. |
| 13 | "MMLU −2.8pp" Qwen14B | ⚠️ | TEAL uniform MMLU=66.34% not in registry (nearest: TEAL 27.5% =67.38%). The diff itself (2.79pp≈2.8pp) is plausible given the table. |
| 18 | "L31 retention 28.4%" | ⚠️ | Not directly in registry; comes from per-layer sparsity figure data not registered. |
| 20 | BCE std "±0.20" | ⚠️ Minor | Exact std(ddof=1)=0.1985 does round to 0.20 (correct under standard rounding), but exact value is 0.1985. ✅ on closer examination. |
| 33 | "148× vs. 112× compression" | ❌ | 112× for LLaMA is correct (14336/128). But 148× for Qwen-14B is inconsistent with the 117M trainable-params figure in the registry, which implies ratio≈109× (d_ff≈13,923). If d_ff were 18,944 (as needed for 148×), total params would be ~148M, not 117M. |

agentId: a31d3bedb296fdf29 (use SendMessage with to: 'a31d3bedb296fdf29' to continue this agent)
&lt;usage>total_tokens: 135485
tool_uses: 40
duration_ms: 852600&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "a5b4b084-c25b-4756-bab6-1fd4be61c515",
  "isSidechain": false,
  "promptId": "de60ee45-84fe-40c7-ad5a-52baa3f09b49",
  "type": "user",
  "uuid": "de04a4d6-5f36-43ae-ba41-07cbcaf1e0f3",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are cross-verifying paper inline numbers against a registry of experiment results. The registry metrics are in `/tmp/registry_metrics.json` (JSON dict: exp_id -> {metrics, spec, conclusion, status}).\n\nYour task: verify ALL quantitative claims made in the **prose text** (not table cells, which are verified separately) of these paper sections. For each numeric claim, find the registry source and check correctness.\n\n## Claims to verify:\n\n### Abstract (abstract.tex)\n1. \"14.5% over TEAL at matched sparsity\" — check: (TEAL_PPL - KL_PPL) / TEAL_PPL. Need TEAL PPL at matched sparsity (28.5% actual). Look for `teal_28.5pct_sanity` or compute from TEAL at 28.5%.\n2. \"MMLU −5.2pp on 8B\" — check: KL_MMLU - Dense_MMLU or KL_MMLU - TEAL_MMLU?  Paper says \"knowledge-intensive regression (MMLU −5.2pp on 8B)\". Context: probably TEAL_MMLU - KL_MMLU = 45.86 - 40.7 = 5.16 ≈ 5.2pp\n3. \"GSM8K −20.1pp on 14B\" — check: probably TEAL_GSM8K - KL_GSM8K for Qwen14B uniform. TEAL=52.1, KL=32.0. Diff=20.1pp\n4. \"+67.2M params\" — architecture claim, not registry\n5. \"PPL gap ≤0.65pp\" — C1 ablation claim. Check: max PPL gap between C1 and KL across seeds at 30%. From Table 3: s42 gap = 9.45-8.82=0.63, s123 gap=8.84-8.83=0.01, s456 gap=8.82-8.79=0.03. Max=0.63pp. Paper says ≤0.65pp. But caption says \"max Δ≤1.70pp at 30%\". Verify.\n6. \"46--68% from magnitude-based targets\" — Jaccard distance range. Look for `c1_mask_overlap` or mask divergence experiments.\n7. \"75.9M params, <1% of base\" — architecture constant\n\n### Introduction (introduction.tex)\n8. \"14.5% at matched sparsity (8.81 vs. 10.30, both at 28.5%)\" — need TEAL PPL at 28.5% actual sparsity. Look for `teal_28.5pct_sanity`.\n9. \"MMLU 40.7±1.3% vs. 65.3% dense\" — KL MMLU from 3-seed (matches Table 2) vs dense. Dense MMLU = 65.27, paper says 65.3%.\n10. \"7.3× MMLU σ\" — global MMLU std / uniform MMLU std. Global: 9.5, Uniform: 1.3. 9.5/1.3 = 7.31 ≈ 7.3×\n11. \"−17.3% PPL on Mistral\" — (TEAL_PPL - KL_PPL) / TEAL_PPL for Mistral 30%. TEAL=8.38, KL=6.93. (8.38-6.93)/8.38 = 17.3%\n12. \"GSM8K −20.1pp, σ=5.2pp\" for Qwen14B\n13. \"MMLU −2.8pp\" for Qwen14B — TEAL_MMLU - KL_MMLU for 14B uniform. TEAL=66.34, KL=63.55. Diff=2.79≈2.8pp\n14. \"6.4% latency overhead\" — from latency table\n\n### Experiments prose (experiments.tex body text, not table cells)\n15. \"PPL 8.81±0.02 (3-seed), a 14.5% reduction over TEAL at matched actual sparsity (8.81 vs. 10.30, both at 28.5%)\" — verify TEAL at 28.5% = 10.30\n16. \"MMLU 40.7±1.3%, 3-seed\" — matches Table 2\n17. \"35.7±9.5%\" for global MMLU — matches Table 2  \n18. \"L31 retention 28.4%\" — look for perlayer_sparsity_analysis\n19. \"11.92 vs. 23.90, 50% reduction\" — (23.90-11.92)/23.90 = 50.1%\n20. \"28.13±0.20\" for BCE at 2700 steps — matches Table 2\n21. \"2.39× worse than KL (11.79)\" — 28.13/11.79 = 2.386 ≈ 2.39×. But wait, text says \"KL (11.79)\" at 50% — this should be from bench_kl50_global\n22. \"F1 (0.613 vs. 0.540)\" — look for `kl_bce_f1_oracle` or `f1_oracle_analysis`\n23. \"139% worse PPL\" — (28.13-11.79)/11.79 = 138.7% ≈ 139%\n24. \"Jaccard distance averages 68% at 50%\" — from mask overlap analysis\n25. \"cross-seed variation (36.3%)\" — cross-seed Jaccard\n26. \"Gumbel-Sigmoid outperforms STE by 33.8% (11.79 vs. 15.77)\" — (15.77-11.79)/11.79 = 33.8%\n27. \"forward KL outperforms JSD (+6.4%) and reverse KL (+8.6%)\" — (12.54-11.79)/11.79=6.4%, (12.80-11.79)/11.79=8.6%\n28. \"$K=16$ achieves the lowest PPL (8.67±0.02 vs. E2E 8.81±0.02)\" — from K-curve\n29. \"the full coupling range (2.08 PPL)\" — K=2 worst (10.75) - K=16 best (8.67) = 2.08\n30. \"signal type gap (9.47 PPL)\" — MSE PPL(18.52) - K=1 KL PPL(9.05) = 9.47\n31. \"$-$17.3\\%, 3-seed\" for Mistral\n32. \"GSM8K 32.0±5.2 vs. 52.1\" for Qwen14B\n33. \"$148×$ vs. $112×$ compression\" — d_model/d_b ratios. For Qwen-14B: d_model=5120(?)/d_b=128 or d_ff/d_b? Need to check architecture.\n\n### Conclusion (conclusion.tex)\n34. \"14.5%\" — same claim as above\n\nFor each claim, output:\n```\n[SECTION] Claim: \"[text]\" → computed=[value] paper=[value] ✅/❌\n```\n\nFocus on numerical accuracy. Tolerance ≤0.1pp for derived calculations.",
    "agentId": "a31d3bedb296fdf29",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the complete verification report for all quantitative prose claims:\n\n---\n\n## Verification Results\n\n### Abstract (`abstract.tex`)\n\n**[ABSTRACT] Claim 1:** \"14.5% over TEAL at matched sparsity\" → computed=(10.30−8.81)/10.30×100=**14.5%** (using rounded 3-seed mean 8.81 and TEAL-28.5%=10.30 from `teal_28.5pct_sanity`). Raw 3-seed mean is 8.8137; exact reduction is 14.43%, which rounds to 14.4% but paper consistently uses the 2dp rounded PPLs. paper=14.5% **✅** (borderline; within rounding tolerance)\n\n**[ABSTRACT] Claim 2:** \"MMLU −5.2pp on 8B\" → TEAL uniform MMLU=45.86% (`teal_30pct_uniform_multiseed_eval`), KL 3-seed MMLU=40.7%, diff=5.16pp≈**5.2pp** ✅\n\n**[ABSTRACT] Claim 3:** \"GSM8K −21.2pp on 14B\" → TEAL GSM8K=52.08% (`qwen14b_teal30_uniform_gsm8k`), KL 2-seed mean=(35.71+26.08)/2=30.9%, diff=**21.2pp** ✅\n\n**[ABSTRACT] Claim 4:** \"+67.2M params\" — architectural constant, not directly in registry. Cited from `latency_benchmark` appendix prose.\n\n**[ABSTRACT] Claim 5:** \"PPL gap ≤0.65pp\" → actual max PPL gap across seeds: s42=9.4463−8.8157=**0.6306pp**, s123=0.01pp, s456=0.03pp. All ≤0.65 ✅. However, the Table 3 footnote says \"(gap 0.65pp)\" for s42, but registry gives 0.63pp. The \"≤0.65pp\" upper bound holds, but the footnote value is slightly imprecise — the actual is **0.63pp**, not 0.65pp. ⚠️\n\n**[ABSTRACT] Claim 6:** \"46--68% from magnitude-based targets\" → 30% sparsity: mean Jaccard distance=**46.3%** (`mask_stats_30pct_64samples.json`); 50% sparsity: mean Jaccard distance=**68.2%** (`mask_stats_50pct_64samples.json`). Range=46–68% ✅\n\n**[ABSTRACT] Claim 7:** \"75.9M params, <1% of base\" — architecture constant. 32 layers × 2.37M params/layer = 75.84M ≈ 75.9M. <1% of LLaMA-8B (7.98B active params). ✅\n\n---\n\n### Introduction (`introduction.tex`)\n\n**[INTRO] Claim 8:** \"14.5% at matched sparsity (8.81 vs. 10.30, both at 28.5%)\" → same as Abstract claim 1. KL 3-seed mean=8.8137≈8.81, TEAL-28.5%=10.30, (10.30−8.81)/10.30=14.47%≈**14.5%** ✅\n\n**[INTRO] Claim 9:** \"MMLU 40.7±1.3% vs. 65.3% dense\" → s42=0.4061, s123=0.3944, s456=0.4198; mean=40.68%≈**40.7%**, std(ddof=1)=1.3% ✅. Dense=65.27%≈**65.3%** (`bench_dense`) ✅\n\n**[INTRO] Claim 10:** \"7.3× MMLU σ\" → global MMLU std=9.5pp, uniform MMLU std=1.3pp; 9.5/1.3=**7.31×**≈7.3× ✅\n\n**[INTRO] Claim 11:** \"−17.3% PPL on Mistral\" → s42=6.7733 (`mistral_kl30_teal_global`), s123=7.1491, s456=6.8752; mean=6.9325; TEAL=8.3807 (`mistral_teal30_baseline`). (8.3807−6.9325)/8.3807=**17.3%** ✅\n\n**[INTRO] Claim 12:** \"GSM8K −21.2pp, σ=6.8pp\" for Qwen14B → 2-seed (s42=35.71%, s456=26.08%); mean=30.9%, std(ddof=1)=**6.8pp**; TEAL=52.1%; diff=**21.2pp** ✅\n\n**[INTRO] Claim 13:** \"MMLU −2.8pp\" for Qwen14B → Appendix Table 14b reports KL uniform MMLU=63.55%, TEAL uniform MMLU=66.34%, diff=2.79pp≈**2.8pp** ✅ in context. However, **TEAL uniform MMLU=66.34% is not directly in the registry** (nearest entry is `qwen14b_teal275_uniform_eval_v3` at 67.38%). The table value 66.34 cannot be independently verified from registry alone. ⚠️\n\n**[INTRO] Claim 14:** \"6.4% latency overhead\" → `latency_benchmark`: KL-50%=126.78ms, dense=119.11ms; (126.78−119.11)/119.11=**6.44%**≈6.4% ✅. At 30%: 6.32%; the 6.4% specifically refers to the 50% sparsity row (per appendix).\n\n---\n\n### Experiments prose (`experiments.tex`)\n\n**[EXP] Claim 15:** \"PPL 8.81±0.02 (3-seed), a 14.5% reduction over TEAL at matched actual sparsity (8.81 vs. 10.30, both at 28.5%)\" → mean=8.8137≈**8.81**, std(ddof=1)=0.018≈**0.02**; TEAL-28.5%=**10.30** ✅\n\n**[EXP] Claim 16:** \"MMLU 40.7±1.3%, 3-seed\" → confirmed ✅ (same as claim 9)\n\n**[EXP] Claim 17:** \"35.7±9.5%\" for global MMLU → s42=25.27%, s123=38.07%, s456=43.82%; mean=**35.72%**, std(ddof=1)=**9.5%** ✅\n\n**[EXP] Claim 18:** \"L31 retention 28.4%\" → from figure caption (Appendix, `app:retention`): \"retention dropping to 28.4% (L31) even at 30% sparsity.\" No registry exp_id `perlayer_sparsity_analysis` found; value comes from figure data not directly registered. **Cannot verify from registry** ⚠️\n\n**[EXP] Claim 19:** \"11.92 vs. 23.90, 50% reduction\" → KL 3-seed uniform 50%: mean=(11.963+11.83+11.9604)/3=**11.918**≈11.92, std=0.076≈0.07 ✅; TEAL uniform 50%=**23.90** (`training_free_baselines.uniform_50pct_ppl`) ✅; (23.90−11.92)/23.90=**50.1%** ✅\n\n**[EXP] Claim 20:** \"28.13±0.20\" BCE at 2700 steps → s42=27.9696, s123=28.0627, s456=28.3503; mean=28.1275→**28.13**, std(ddof=1)=0.1985→**0.20** (0.1985 at 2dp rounds up to 0.20) ✅\n\n**[EXP] Claim 21:** \"2.39× worse than KL (11.79)\" → 28.13/11.79=**2.386×**≈2.39× ✅ (KL=`bench_kl50_global` s42=11.7933≈11.79)\n\n**[EXP] Claim 22:** \"F1 (0.613 vs. 0.540)\" → `kl_bce_f1_oracle`: BCE_F1=**0.6128**≈0.613, KL_F1=**0.5397**≈0.540 ✅\n\n**[EXP] Claim 23:** \"139% worse PPL\" → (28.13−11.79)/11.79×100=**138.6%**≈139% ✅\n\n**[EXP] Claim 24:** \"Jaccard distance averages 68% at 50%\" → `mask_stats_50pct_64samples.json`: jaccard_distance_mean=**0.6824=68.24%** ✅\n\n**[EXP] Claim 25:** \"cross-seed variation (36.3%)\" → appendix §Cross-Seed Mask Consistency: \"mean cross-seed Jaccard distance is 0.363 (IoU=0.637)\". Source exp_id `cross_seed_jaccard_kl30` not in registry, but value consistent with appendix text and independently stated. ✅\n\n**[EXP] Claim 26:** \"Gumbel-Sigmoid outperforms STE by 33.8% (11.79 vs. 15.77)\" → (15.77−11.79)/11.79×100=**33.8%** ✅ (`ste_baseline_s42`: teal_sparse_ppl=15.77)\n\n**[EXP] Claim 27:** \"forward KL outperforms JSD (+6.4%) and reverse KL (+8.6%)\" → JSD_50%=12.54: (12.54−11.79)/11.79×100=**6.4%** ✅; RevKL_50%=12.80: (12.80−11.79)/11.79×100=**8.6%** ✅. Note: JSD/RevKL 50% values (12.54, 12.80) appear only in the ablation table, with no dedicated registry exp_ids; the computation is internally consistent.\n\n**[EXP] Claim 28:** \"K=16 achieves the lowest PPL (8.67±0.02 vs. E2E 8.81±0.02)\" → K=16 3-seed: s42=8.6737 (`perlayer_kl_k16_eval_final2`), s123=8.6939, s456=8.655; mean=**8.6742**≈8.67, std(ddof=1)=0.0195≈**0.02** ✅\n\n**[EXP] Claim 29:** \"the full coupling range (2.08 PPL)\" → K=2 3-seed mean=10.754, K=16 3-seed mean=8.674; range=**2.080** ✅\n\n**[EXP] Claim 30:** \"signal type gap (9.47 PPL)\" → MSE=18.52, K=1 per-layer KL=9.05; gap=**9.47** ✅\n\n**[EXP] Claim 31:** \"−17.3%, 3-seed\" for Mistral → confirmed same as claim 11 ✅\n\n**[EXP] Claim 32:** \"GSM8K 32.0±5.2 vs. 52.1 for Qwen14B\" — The actual paper text (`experiments.tex` line 195) reads **\"30.9±6.8 vs. 52.1, n=2\"**, not \"32.0±5.2\" as stated in the task. Registry confirms: 2-seed mean=30.9%, std(ddof=1)=6.8%, TEAL=52.1% ✅. The verification task prompt had an outdated version of this number; the current paper text is correct.\n\n**[EXP] Claim 33:** \"148× vs. 112× compression\" → LLaMA-8B: d_ff=14336, d_b=128, ratio=**112** ✅. Qwen-14B claim of **148×** is **inconsistent with registry**: `qwen14b_kl30_s123` reports `trainable_params='117M (0.793%)'`; 117M/48 layers ≈ 2.44M per layer; with d_model=5120, d_b=128: implied d_ff≈13,923, ratio≈**109×**, not 148×. A ratio of 148 would require d_ff=18,944 and ~148M total trainable params, contradicting the 117M figure. **❌**\n\n---\n\n### Conclusion (`conclusion.tex`)\n\n**[CONCLUSION] Claim 34:** \"14.5%\" → same basis as all prior 14.5% claims ✅\n\n---\n\n## Summary of Issues Found\n\n| # | Claim | Status | Issue |\n|---|-------|--------|-------|\n| 5 | \"PPL gap ≤0.65pp\" / footnote \"(gap 0.65pp)\" | ⚠️ | Actual s42 gap = 0.63pp (registry: 9.4463−8.8157=0.6306). The ≤0.65pp bound holds, but the footnote's stated value 0.65pp is imprecise. |\n| 13 | \"MMLU −2.8pp\" Qwen14B | ⚠️ | TEAL uniform MMLU=66.34% not in registry (nearest: TEAL 27.5% =67.38%). The diff itself (2.79pp≈2.8pp) is plausible given the table. |\n| 18 | \"L31 retention 28.4%\" | ⚠️ | Not directly in registry; comes from per-layer sparsity figure data not registered. |\n| 20 | BCE std \"±0.20\" | ⚠️ Minor | Exact std(ddof=1)=0.1985 does round to 0.20 (correct under standard rounding), but exact value is 0.1985. ✅ on closer examination. |\n| 33 | \"148× vs. 112× compression\" | ❌ | 112× for LLaMA is correct (14336/128). But 148× for Qwen-14B is inconsistent with the 117M trainable-params figure in the registry, which implies ratio≈109× (d_ff≈13,923). If d_ff were 18,944 (as needed for 148×), total params would be ~148M, not 117M. |"
      }
    ],
    "totalDurationMs": 852600,
    "totalTokens": 135485,
    "totalToolUseCount": 40,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2034,
      "cache_read_input_tokens": 129651,
      "output_tokens": 3799,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2034
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3799,
          "cache_read_input_tokens": 129651,
          "cache_creation_input_tokens": 2034,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2034,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 7,
      "searchCount": 0,
      "bashCount": 33,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "a5b4b084-c25b-4756-bab6-1fd4be61c515",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01",
  "version": "2.1.126",
  "gitBranch": "master"
}
````

</details>

---


### Assistant

_source line 68 · 2026-05-24T01:35:44.566Z_

<details><summary>Logged reasoning block</summary>

```text
Let me also verify some of the claims that need quick checking - the Qwen 14B compression ratio claim and the abstract GSM8K number. Let me also quickly verify the TEAL 28.5% PPL = 10.30 claim.

Let me also check for the introduction claim about "GSM8K −20.1pp" vs what the agent found ("−21.2pp"). Let me re-read the abstract and intro more carefully.

From abstract.tex line 3: "knowledge-intensive regression (MMLU $-$5.2pp on 8B; GSM8K $-$20.1pp on 14B)"


From intro line 17: "GSM8K $-$20.1pp, $\sigma$=5.2pp"

Now I'm checking the experiments.tex file to verify the actual GSM8K numbers - the agent claimed to find "30.9±6.8 vs. 52.1, n=2" but I need to see what's actually written there around line 195. I'm cross-referencing the paper's actual text against what the verification agent reported. The experiments.tex clearly states GSM8K 32.0±5.2 for Qwen14B uniform KL, which aligns with the abstract's 20.1pp regression (52.1 baseline minus 32.0 result). But the agent claimed the paper shows 30.9±6.8 instead, so there's a discrepancy I need to resolve by checking the source directly. I'm seeing a discrepancy between what the agent reported and what's actually in the paper. The agent found GSM8K values of 35.5 and 26.1 (averaging to 30.8), but the paper clearly states 32.0±5.2 in both the table and the inline text. Either the agent misread the paper or there's a genuine mismatch in the reported numbers.

The agent marked n=2 because seed 123 was incomplete, but I should check if including that third seed would change the computed mean and standard deviation. Let me trace through the actual experiment IDs to see what data's available across all three seeds. I'm calculating the per-layer parameter count for Qwen-2.5-14B with its actual dimensions, and the math shows around 3.08M parameters per layer across 48 layers, which doesn't match up with the 117M trainable parameters the agent reported. 123.2M, which still doesn't match the 117M from the registry. Let me recalculate assuming Qwen2.5-14B uses SwiGLU with an intermediate_size of 13696 instead—that would give me about 2.41M per layer, and with 48 layers I'd get roughly 115.6M, which is much closer to 117M. I need to verify the exact intermediate size for this model since SwiGLU changes how the config is interpreted. I need to verify these specific claims against the actual registry data before finalizing my report. Let me pull the exact entries for the KL 50% global row, the Qwen14B GSM8K results, the compression ratio calculation, and the other flagged discrepancies so I can document what matches and what doesn't.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de04a4d6-5f36-43ae-ba41-07cbcaf1e0f3",
  "isSidechain": false,
  "requestId": "req_011CbLXxLR95Gvjr9vrTMPGW",
  "type": "assistant",
  "uuid": "789cf813-2d99-4673-a38d-eb75fa682cb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RS1BHnAK2Afepx6o9vHDS6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5869,
      "cache_read_input_tokens": 90086,
      "output_tokens": 4664,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5869,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4664,
          "cache_read_input_tokens": 90086,
          "cache_creation_input_tokens": 5869,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5869
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

_source line 69 · 2026-05-24T01:35:44.717Z_

All four agents returned. Let me verify a few critical discrepancies they flagged.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "789cf813-2d99-4673-a38d-eb75fa682cb9",
  "isSidechain": false,
  "requestId": "req_011CbLXxLR95Gvjr9vrTMPGW",
  "type": "assistant",
  "uuid": "a0659779-9b89-4af8-94c3-5a8c021987ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RS1BHnAK2Afepx6o9vHDS6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5869,
      "cache_read_input_tokens": 90086,
      "output_tokens": 4664,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5869,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4664,
          "cache_read_input_tokens": 90086,
          "cache_creation_input_tokens": 5869,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5869
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

_source line 70 · 2026-05-24T01:35:53.158Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01HxKMBoeUYdta6VHHFSMEx5`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/tmp/registry_metrics.json') as f:\n    reg = json.load(f)\n\n# 1. KL 50% global 3-seed: check bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval, kl50_s456_global_eval, mvp_kl_norm_v2_s42/s123/s456\nprint(\"=== KL 50% global seed experiments ===\")\nfor eid in ['bench_kl50_global', 'kl50_global_s123_downstream_v2', 'kl50_global_s456_eval', 'kl50_s456_global_eval', 'kl50_global_s123_reeval', 'kl50_s123_eval', 'kl50_s456_eval', 'mvp_kl_norm_v2_s42', 'mvp_kl_norm_v2_s123', 'mvp_kl_norm_v2_s456']:\n    if eid in reg:\n        m = reg[eid]['metrics']\n        ppl_keys = [k for k in m.keys() if 'ppl' in k.lower()]\n        arc_keys = [k for k in m.keys() if 'arc' in k.lower()]\n        wg_keys = [k for k in m.keys() if 'winogrande' in k.lower() or 'wg' in k.lower()]\n        mmlu_keys = [k for k in m.keys() if 'mmlu' in k.lower()]\n        gsm_keys = [k for k in m.keys() if 'gsm' in k.lower()]\n        print(f\"\\n{eid}:\")\n        for k in ppl_keys: print(f\"  {k}: {m[k]}\")\n        for k in arc_keys: print(f\"  {k}: {m[k]}\")\n        for k in wg_keys: print(f\"  {k}: {m[k]}\")\n        for k in mmlu_keys: print(f\"  {k}: {m[k]}\")\n        for k in gsm_keys: print(f\"  {k}: {m[k]}\")\n    else:\n        print(f\"{eid}: NOT FOUND\")\n\nPYEOF\n",
  "description": "Check KL 50% global 3-seed raw metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0659779-9b89-4af8-94c3-5a8c021987ae",
  "isSidechain": false,
  "requestId": "req_011CbLXxLR95Gvjr9vrTMPGW",
  "type": "assistant",
  "uuid": "413b0831-da1e-4d8b-a29e-d9f1826722c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RS1BHnAK2Afepx6o9vHDS6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5869,
      "cache_read_input_tokens": 90086,
      "output_tokens": 4664,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5869,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4664,
          "cache_read_input_tokens": 90086,
          "cache_creation_input_tokens": 5869,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5869
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

_source line 71 · 2026-05-24T01:35:53.263Z_

<details><summary>↩ Tool result · `toolu_01HxKMBoeUYdta6VHHFSMEx5`</summary>

```text
=== KL 50% global seed experiments ===

bench_kl50_global:
  wikitext2_ppl: 11.7933
  arc_challenge_acc_norm: 0.3285
  winogrande_acc: 0.6346
  mmlu_acc: 0.2789
  gsm8k_exact_match: 0.0129

kl50_global_s123_downstream_v2:
  arc_challenge_acc_norm: 0.3916
  winogrande_acc: 0.6401
  mmlu_acc: 0.2908
  gsm8k_exact_match: 0.0341
kl50_global_s456_eval: NOT FOUND

kl50_s456_global_eval:
  ppl_wikitext2: 11.8057
  arc_challenge: 0.3319
  winogrande: 0.6488
  mmlu: 0.2794
  gsm8k: 0.0212

kl50_global_s123_reeval:
  wikitext2_ppl: 11.7184
  arc_challenge_acc_norm: 0.3635
  winogrande_acc: 0.6109
  mmlu_acc: 0.2834
  gsm8k_exact_match: 0.0258

kl50_s123_eval:
  wikitext2_ppl: 11.745
  arc_challenge: 0.3814
  winogrande: 0.6125
  mmlu: 0.2752
  gsm8k: 0.0281

kl50_s456_eval:
  wikitext2_ppl: 11.8614
  arc_challenge_acc_norm: 0.3754
  winogrande_acc: 0.6417
  mmlu_acc: 0.2784
  gsm8k_exact_match: 0.0212

mvp_kl_norm_v2_s42:
  true_dense_ppl: 6.1173
  predictor_hard_mask_ppl: 9.2142
  teal_sparse_ppl: 12.0776
  ppl_increase_vs_true_dense_pct: 97.4
  vanilla_teal_sparse_ppl_INVALID: 66036.4062

mvp_kl_norm_v2_s123:
  true_dense_ppl: 6.1173
  predictor_hard_mask_ppl: 9.2474
  teal_sparse_ppl: 11.9128
  ppl_increase_vs_true_dense_pct: 94.7
  vanilla_teal_sparse_ppl_INVALID: 66036.4062

mvp_kl_norm_v2_s456:
  true_dense_ppl: 6.1173
  predictor_hard_mask_ppl: 9.14
  teal_sparse_ppl: 13.58
  ppl_increase_vs_true_dense_pct: 121.9
  vanilla_teal_sparse_ppl_INVALID: 66036.4062
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "413b0831-da1e-4d8b-a29e-d9f1826722c7",
  "isSidechain": false,
  "promptId": "de60ee45-84fe-40c7-ad5a-52baa3f09b49",
  "type": "user",
  "uuid": "d0786508-9ba8-4a93-8a88-fe42faa149f6",
  "toolUseResult": {
    "stdout": "=== KL 50% global seed experiments ===\n\nbench_kl50_global:\n  wikitext2_ppl: 11.7933\n  arc_challenge_acc_norm: 0.3285\n  winogrande_acc: 0.6346\n  mmlu_acc: 0.2789\n  gsm8k_exact_match: 0.0129\n\nkl50_global_s123_downstream_v2:\n  arc_challenge_acc_norm: 0.3916\n  winogrande_acc: 0.6401\n  mmlu_acc: 0.2908\n  gsm8k_exact_match: 0.0341\nkl50_global_s456_eval: NOT FOUND\n\nkl50_s456_global_eval:\n  ppl_wikitext2: 11.8057\n  arc_challenge: 0.3319\n  winogrande: 0.6488\n  mmlu: 0.2794\n  gsm8k: 0.0212\n\nkl50_global_s123_reeval:\n  wikitext2_ppl: 11.7184\n  arc_challenge_acc_norm: 0.3635\n  winogrande_acc: 0.6109\n  mmlu_acc: 0.2834\n  gsm8k_exact_match: 0.0258\n\nkl50_s123_eval:\n  wikitext2_ppl: 11.745\n  arc_challenge: 0.3814\n  winogrande: 0.6125\n  mmlu: 0.2752\n  gsm8k: 0.0281\n\nkl50_s456_eval:\n  wikitext2_ppl: 11.8614\n  arc_challenge_acc_norm: 0.3754\n  winogrande_acc: 0.6417\n  mmlu_acc: 0.2784\n  gsm8k_exact_match: 0.0212\n\nmvp_kl_norm_v2_s42:\n  true_dense_ppl: 6.1173\n  predictor_hard_mask_ppl: 9.2142\n  teal_sparse_ppl: 12.0776\n  ppl_increase_vs_true_dense_pct: 97.4\n  vanilla_teal_sparse_ppl_INVALID: 66036.4062\n\nmvp_kl_norm_v2_s123:\n  true_dense_ppl: 6.1173\n  predictor_hard_mask_ppl: 9.2474\n  teal_sparse_ppl: 11.9128\n  ppl_increase_vs_true_dense_pct: 94.7\n  vanilla_teal_sparse_ppl_INVALID: 66036.4062\n\nmvp_kl_norm_v2_s456:\n  true_dense_ppl: 6.1173\n  predictor_hard_mask_ppl: 9.14\n  teal_sparse_ppl: 13.58\n  ppl_increase_vs_true_dense_pct: 121.9\n  vanilla_teal_sparse_ppl_INVALID: 66036.4062",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "413b0831-da1e-4d8b-a29e-d9f1826722c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 72 · 2026-05-24T01:35:58.588Z_

<details open><summary>🔧 Tool call — Bash · `toolu_018udhycEegcwc23JRXiWFBa`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/tmp/registry_metrics.json') as f:\n    reg = json.load(f)\n\n# 2. Qwen14B GSM8K values\nprint(\"=== Qwen14B GSM8K experiments ===\")\nfor eid in ['qwen14b_kl30_s42_gsm8k_uniform', 'qwen14b_kl30_s42_gsm8k_v2', 'qwen14b_kl30_s456_gsm8k', 'qwen14b_kl30_s123_eval_v5', 'qwen14b_kl30_s456_eval_v2', 'qwen14b_kl30_s456_eval_v3', 'qwen14b_kl30_s42_eval_uniform_v3', 'qwen14b_kl30_s123']:\n    if eid in reg:\n        m = reg[eid]['metrics']\n        gsm_keys = [k for k in m.keys() if 'gsm' in k.lower()]\n        print(f\"\\n{eid}:\")\n        for k in gsm_keys: print(f\"  {k}: {m[k]}\")\n        if not gsm_keys:\n            print(f\"  (no gsm keys; all keys: {list(m.keys())[:10]})\")\n    else:\n        print(f\"{eid}: NOT FOUND\")\n\n# 3. Qwen14B architecture: check spec for d_ff\nprint(\"\\n=== Qwen14B spec ===\")\nfor eid in ['qwen14b_kl30_s42', 'qwen14b_kl30_s123']:\n    if eid in reg:\n        s = reg[eid].get('spec', {})\n        print(f\"\\n{eid} spec:\")\n        for k, v in s.items():\n            print(f\"  {k}: {v}\")\n\nPYEOF\n",
  "description": "Check Qwen14B GSM8K and architecture spec"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0786508-9ba8-4a93-8a88-fe42faa149f6",
  "isSidechain": false,
  "requestId": "req_011CbLXxLR95Gvjr9vrTMPGW",
  "type": "assistant",
  "uuid": "eaa505bf-7d75-4fea-96d7-6788fe8afa78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RS1BHnAK2Afepx6o9vHDS6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5869,
      "cache_read_input_tokens": 90086,
      "output_tokens": 4664,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5869,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4664,
          "cache_read_input_tokens": 90086,
          "cache_creation_input_tokens": 5869,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5869
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

_source line 73 · 2026-05-24T01:35:58.660Z_

<details><summary>↩ Tool result · `toolu_018udhycEegcwc23JRXiWFBa`</summary>

```text
=== Qwen14B GSM8K experiments ===

qwen14b_kl30_s42_gsm8k_uniform:
  gsm8k_exact_match: 0.3548

qwen14b_kl30_s42_gsm8k_v2:
  gsm8k_exact_match: 0.3571
  gsm8k_exact_match_strict: 0.3541
  gsm8k_exact_match_stderr: 0.0132

qwen14b_kl30_s456_gsm8k:
  gsm8k_exact_match: 0.2608
  gsm8k_exact_match_stderr: 0.01209
  gsm8k_exact_match_strict: 0.2547
  gsm8k_exact_match_strict_stderr: 0.012

qwen14b_kl30_s123_eval_v5:
  (no gsm keys; all keys: ['wikitext2_ppl', 'arc_challenge_acc_norm', 'winogrande_acc', 'hellaswag_acc_norm', 'piqa_acc_norm', 'mmlu_acc', 'actual_sparsity'])

qwen14b_kl30_s456_eval_v2:
  (no gsm keys; all keys: ['wikitext2_ppl', 'arc_challenge_acc', 'arc_challenge_acc_norm', 'winogrande_acc', 'mmlu_acc', 'hellaswag_acc', 'hellaswag_acc_norm', 'piqa_acc', 'piqa_acc_norm', 'model_sparsity'])

qwen14b_kl30_s456_eval_v3:
  (no gsm keys; all keys: ['wikitext2_ppl', 'arc_challenge_acc_norm', 'winogrande_acc', 'hellaswag_acc_norm', 'piqa_acc_norm', 'mmlu_acc', 'actual_sparsity'])

qwen14b_kl30_s42_eval_uniform_v3:
  (no gsm keys; all keys: ['wikitext2_ppl', 'arc_challenge_acc', 'arc_challenge_acc_norm', 'winogrande_acc', 'mmlu_acc', 'hellaswag_acc_norm', 'piqa_acc_norm', 'actual_sparsity'])

qwen14b_kl30_s123:
  (no gsm keys; all keys: ['final_loss_kl_norm', 'final_kl_raw', 'final_sparsity', 'final_constraint', 'final_lambda', 'final_tau', 'steps', 'trainable_params'])

=== Qwen14B spec ===

qwen14b_kl30_s42 spec:
  command: cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_HUB_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/train.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --loss_type kl_normalized --num_steps 1000 --batch_size 1 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.3 --lambda_max 5000 --gradient_checkpointing --dataset wikitext-103 --log_every 10 --output_dir checkpoints/qwen14b_kl30_s42 --wandb_run_name qwen14b_kl30_s42 --gpu 0
  server: westd-34887
  gpu: ['cuda:1']
  pid: 50349
  log_path: ~/runs/distill_sparse_swiglu/qwen14b_kl30_s42.log
  submitted_at: 2026-05-17T14:28:58.095Z
  submitted_via: submit_training_job
  backend: tmux
  account: root
  wall_clock_seconds: 1278.3
  gpu_hours: 0.36

qwen14b_kl30_s123 spec:
  command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export WANDB_MODE=disabled && export PYTHONUNBUFFERED=1 && python -u src/train.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --loss_type kl_normalized --num_steps 1000 --batch_size 1 --seq_len 2048 --lr 1e-3 --seed 123 --sparsity_target 0.3 --lambda_max 5000 --gradient_checkpointing --dataset wikitext-103 --log_every 10 --output_dir checkpoints/qwen14b_kl30_s123 --gpu 0 2>&1"
  server: westd-34887
  gpu: ['cuda:0']
  pid: 91294
  log_path: ~/runs/distill_sparse_swiglu/qwen14b_kl30_s123.log
  submitted_at: 2026-05-19T08:21:40.612Z
  submitted_via: submit_training_job
  backend: tmux
  account: root
  wall_clock_seconds: 19332.8
  gpu_hours: 5.37
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eaa505bf-7d75-4fea-96d7-6788fe8afa78",
  "isSidechain": false,
  "promptId": "de60ee45-84fe-40c7-ad5a-52baa3f09b49",
  "type": "user",
  "uuid": "771a7423-7efb-4b2c-b61d-cb05cc9e8a97",
  "toolUseResult": {
    "stdout": "=== Qwen14B GSM8K experiments ===\n\nqwen14b_kl30_s42_gsm8k_uniform:\n  gsm8k_exact_match: 0.3548\n\nqwen14b_kl30_s42_gsm8k_v2:\n  gsm8k_exact_match: 0.3571\n  gsm8k_exact_match_strict: 0.3541\n  gsm8k_exact_match_stderr: 0.0132\n\nqwen14b_kl30_s456_gsm8k:\n  gsm8k_exact_match: 0.2608\n  gsm8k_exact_match_stderr: 0.01209\n  gsm8k_exact_match_strict: 0.2547\n  gsm8k_exact_match_strict_stderr: 0.012\n\nqwen14b_kl30_s123_eval_v5:\n  (no gsm keys; all keys: ['wikitext2_ppl', 'arc_challenge_acc_norm', 'winogrande_acc', 'hellaswag_acc_norm', 'piqa_acc_norm', 'mmlu_acc', 'actual_sparsity'])\n\nqwen14b_kl30_s456_eval_v2:\n  (no gsm keys; all keys: ['wikitext2_ppl', 'arc_challenge_acc', 'arc_challenge_acc_norm', 'winogrande_acc', 'mmlu_acc', 'hellaswag_acc', 'hellaswag_acc_norm', 'piqa_acc', 'piqa_acc_norm', 'model_sparsity'])\n\nqwen14b_kl30_s456_eval_v3:\n  (no gsm keys; all keys: ['wikitext2_ppl', 'arc_challenge_acc_norm', 'winogrande_acc', 'hellaswag_acc_norm', 'piqa_acc_norm', 'mmlu_acc', 'actual_sparsity'])\n\nqwen14b_kl30_s42_eval_uniform_v3:\n  (no gsm keys; all keys: ['wikitext2_ppl', 'arc_challenge_acc', 'arc_challenge_acc_norm', 'winogrande_acc', 'mmlu_acc', 'hellaswag_acc_norm', 'piqa_acc_norm', 'actual_sparsity'])\n\nqwen14b_kl30_s123:\n  (no gsm keys; all keys: ['final_loss_kl_norm', 'final_kl_raw', 'final_sparsity', 'final_constraint', 'final_lambda', 'final_tau', 'steps', 'trainable_params'])\n\n=== Qwen14B spec ===\n\nqwen14b_kl30_s42 spec:\n  command: cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_HUB_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/train.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --loss_type kl_normalized --num_steps 1000 --batch_size 1 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.3 --lambda_max 5000 --gradient_checkpointing --dataset wikitext-103 --log_every 10 --output_dir checkpoints/qwen14b_kl30_s42 --wandb_run_name qwen14b_kl30_s42 --gpu 0\n  server: westd-34887\n  gpu: ['cuda:1']\n  pid: 50349\n  log_path: ~/runs/distill_sparse_swiglu/qwen14b_kl30_s42.log\n  submitted_at: 2026-05-17T14:28:58.095Z\n  submitted_via: submit_training_job\n  backend: tmux\n  account: root\n  wall_clock_seconds: 1278.3\n  gpu_hours: 0.36\n\nqwen14b_kl30_s123 spec:\n  command: bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export WANDB_MODE=disabled && export PYTHONUNBUFFERED=1 && python -u src/train.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --loss_type kl_normalized --num_steps 1000 --batch_size 1 --seq_len 2048 --lr 1e-3 --seed 123 --sparsity_target 0.3 --lambda_max 5000 --gradient_checkpointing --dataset wikitext-103 --log_every 10 --output_dir checkpoints/qwen14b_kl30_s123 --gpu 0 2>&1\"\n  server: westd-34887\n  gpu: ['cuda:0']\n  pid: 91294\n  log_path: ~/runs/distill_sparse_swiglu/qwen14b_kl30_s123.log\n  submitted_at: 2026-05-19T08:21:40.612Z\n  submitted_via: submit_training_job\n  backend: tmux\n  account: root\n  wall_clock_seconds: 19332.8\n  gpu_hours: 5.37",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "eaa505bf-7d75-4fea-96d7-6788fe8afa78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 74 · 2026-05-24T01:36:05.558Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01X4vpoDiLh7W87W6agGamQc`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/tmp/registry_metrics.json') as f:\n    reg = json.load(f)\n\n# 4. TEAL 30% uniform - check all related entries\nprint(\"=== TEAL 30% uniform experiments ===\")\nfor eid in ['teal_30pct_uniform_multiseed_eval', 'downstream_teal30_baseline', 'bench_teal30_uniform_6task', 'training_free_baselines', 'bench_teal30']:\n    if eid in reg:\n        m = reg[eid]['metrics']\n        print(f\"\\n{eid}:\")\n        for k in sorted(m.keys()):\n            print(f\"  {k}: {m[k]}\")\n    else:\n        print(f\"{eid}: NOT FOUND\")\n\n# 5. TEAL 28.5% sanity check\nprint(\"\\n=== TEAL 28.5% ===\")\neid = 'teal_28.5pct_sanity'\nif eid in reg:\n    m = reg[eid]['metrics']\n    print(f\"{eid}:\")\n    for k in sorted(m.keys()): print(f\"  {k}: {m[k]}\")\nelse:\n    print(f\"{eid}: NOT FOUND\")\n\n# 6. Check C4 control - HS/PIQA for WikiText-trained predictor\nprint(\"\\n=== HS/PIQA sources for KL30 uniform ===\")\nfor eid in ['kl30_uniform_hellaswag_piqa', 'kl30_uniform_hellaswag_piqa_v2', 'hellaswag_piqa_kl30_uniform', 'bench_kl30_uniform']:\n    if eid in reg:\n        m = reg[eid]['metrics']\n        hs_keys = [k for k in m.keys() if 'hella' in k.lower() or 'hs' in k.lower()]\n        piqa_keys = [k for k in m.keys() if 'piqa' in k.lower()]\n        print(f\"\\n{eid}:\")\n        for k in hs_keys: print(f\"  {k}: {m[k]}\")\n        for k in piqa_keys: print(f\"  {k}: {m[k]}\")\n    else:\n        print(f\"{eid}: NOT FOUND\")\n\nPYEOF\n",
  "description": "Check TEAL baselines and HS/PIQA sources"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "771a7423-7efb-4b2c-b61d-cb05cc9e8a97",
  "isSidechain": false,
  "requestId": "req_011CbLXxLR95Gvjr9vrTMPGW",
  "type": "assistant",
  "uuid": "30edb010-e319-4f0e-b67f-0d8dc8c92621",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RS1BHnAK2Afepx6o9vHDS6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5869,
      "cache_read_input_tokens": 90086,
      "output_tokens": 4664,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5869,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4664,
          "cache_read_input_tokens": 90086,
          "cache_creation_input_tokens": 5869,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5869
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

_source line 75 · 2026-05-24T01:36:05.630Z_

<details><summary>↩ Tool result · `toolu_01X4vpoDiLh7W87W6agGamQc`</summary>

```text
=== TEAL 30% uniform experiments ===

teal_30pct_uniform_multiseed_eval:
  arc_challenge: 0.3771
  gsm8k: 0.0879
  hellaswag: 0.6331
  mmlu: 0.4586
  piqa: 0.7198
  ppl: 10.8173
  winogrande: 0.6504

downstream_teal30_baseline:
  boolq_acc: 0.685
  hellaswag_acc: 0.4878
  hellaswag_acc_norm: 0.667
  piqa_acc: 0.7258
  piqa_acc_norm: 0.7361
bench_teal30_uniform_6task: NOT FOUND

training_free_baselines:
  dense_ppl: 6.12
  rsparse_global_ppl: 151.2
  teal_greedy_ppl: 33.47
  uniform_50pct_ppl: 23.9
  vanilla_teal_global_ppl: 23.31
  vanilla_teal_global_ppl_30pct: 10.97
  vanilla_teal_global_ppl_50pct: 23.31
  vanilla_teal_global_ppl_70pct: 100.11
  wina_global_ppl: 27.93
  wina_global_ppl_30pct: 11.45
  wina_global_ppl_50pct: 27.93
  wina_global_ppl_70pct: 137.24

bench_teal30:
  actual_sparsity: 0.3
  arc_challenge_acc_norm: 0.4232
  gsm8k_exact_match: 0.0788
  mmlu_acc: 0.3861
  wikitext2_ppl: 10.97
  winogrande_acc: 0.6606

=== TEAL 28.5% ===
teal_28.5pct_sanity:
  wikitext2_ppl: 10.3

=== HS/PIQA sources for KL30 uniform ===

kl30_uniform_hellaswag_piqa:
  hellaswag_acc_norm: 0.7085
  piqa_acc_norm: 0.7481

kl30_uniform_hellaswag_piqa_v2:
  hellaswag_acc_norm: 0.7085
  piqa_acc_norm: 0.7481
hellaswag_piqa_kl30_uniform: NOT FOUND

bench_kl30_uniform:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30edb010-e319-4f0e-b67f-0d8dc8c92621",
  "isSidechain": false,
  "promptId": "de60ee45-84fe-40c7-ad5a-52baa3f09b49",
  "type": "user",
  "uuid": "732ca4f7-5b89-4e36-b42c-edc71c1f58d6",
  "toolUseResult": {
    "stdout": "=== TEAL 30% uniform experiments ===\n\nteal_30pct_uniform_multiseed_eval:\n  arc_challenge: 0.3771\n  gsm8k: 0.0879\n  hellaswag: 0.6331\n  mmlu: 0.4586\n  piqa: 0.7198\n  ppl: 10.8173\n  winogrande: 0.6504\n\ndownstream_teal30_baseline:\n  boolq_acc: 0.685\n  hellaswag_acc: 0.4878\n  hellaswag_acc_norm: 0.667\n  piqa_acc: 0.7258\n  piqa_acc_norm: 0.7361\nbench_teal30_uniform_6task: NOT FOUND\n\ntraining_free_baselines:\n  dense_ppl: 6.12\n  rsparse_global_ppl: 151.2\n  teal_greedy_ppl: 33.47\n  uniform_50pct_ppl: 23.9\n  vanilla_teal_global_ppl: 23.31\n  vanilla_teal_global_ppl_30pct: 10.97\n  vanilla_teal_global_ppl_50pct: 23.31\n  vanilla_teal_global_ppl_70pct: 100.11\n  wina_global_ppl: 27.93\n  wina_global_ppl_30pct: 11.45\n  wina_global_ppl_50pct: 27.93\n  wina_global_ppl_70pct: 137.24\n\nbench_teal30:\n  actual_sparsity: 0.3\n  arc_challenge_acc_norm: 0.4232\n  gsm8k_exact_match: 0.0788\n  mmlu_acc: 0.3861\n  wikitext2_ppl: 10.97\n  winogrande_acc: 0.6606\n\n=== TEAL 28.5% ===\nteal_28.5pct_sanity:\n  wikitext2_ppl: 10.3\n\n=== HS/PIQA sources for KL30 uniform ===\n\nkl30_uniform_hellaswag_piqa:\n  hellaswag_acc_norm: 0.7085\n  piqa_acc_norm: 0.7481\n\nkl30_uniform_hellaswag_piqa_v2:\n  hellaswag_acc_norm: 0.7085\n  piqa_acc_norm: 0.7481\nhellaswag_piqa_kl30_uniform: NOT FOUND\n\nbench_kl30_uniform:",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "30edb010-e319-4f0e-b67f-0d8dc8c92621",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 76_

```json
{
  "type": "last-prompt",
  "leafUuid": "732ca4f7-5b89-4e36-b42c-edc71c1f58d6",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01"
}
```

---


### Runtime record

_source line 77_

```json
{
  "type": "ai-title",
  "aiTitle": "Final data consistency audit registry vs paper",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01"
}
```

---


### Assistant

_source line 78 · 2026-05-24T01:38:02.868Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have much better data to compile the final report. Let me analyze the key findings:

### KL 50% Global (Table 2 row)
Paper claims PPL 11.84±0.15. Let me check which seeds give this:

Looking at the registry:
- bench_kl50_global (s42): wikitext2_ppl = 11.7933
- kl50_global_s123_downstream_v2: no PPL
- kl50_global_s123_reeval: wikitext2_ppl = 11.7184
- kl50_s123_eval: wikitext2_ppl = 11.745


- kl50_s456_global_eval: ppl_wikitext2 = 11.8057
- kl50_s456_eval: wikitext2_ppl = 11.8614

I'm also seeing some additional runs with different configurations like mvp_kl_norm_v2 across seeds 42 and 123 showing slightly higher perplexities around 11.91-12.08. The paper references bench_kl50_global, kl50_global_s123_downstream_v2, and kl50_global_s456_eval, but the middle one doesn't have a PPL value recorded, which is problematic for computing the mean and standard deviation they report.

I found kl50_global_s123_reeval with a PPL of 11.7184, so I'm testing different combinations of seeds to see which matches the paper's reported 11.84±0.15. The closest match I'm getting is using s42=11.7933, s123=11.9128, and s456=11.8057, which gives a mean of 11.84±0.06—the mean aligns perfectly but the standard deviation is much tighter than what they report.

Now I'm trying other combinations with different model variants like mvp_kl_norm_v2 and kl50_s456_eval to see if any produce the wider uncertainty the paper shows. me check its perplexity value. I need to run another query to get that, but first let me compare the downstream metrics from the paper against what I'm seeing in the experiments. The paper reports specific scores for ARC-c, WG, MMLU, and GSM8K, and I'm finding different results across the various model checkpoints—bench_kl50_global is coming in lower than the paper's numbers, while kl50_global_s123_downstream_v2 is closer on some metrics but still not matching exactly.

Now I'm looking at the full set of results across all three runs and computing the mean and standard deviation. The paper's reported numbers sit right in the middle of my computed range, but there are some discrepancies—ARC-c is off by about 1.2 percentage points, and the other metrics show similar small gaps that suggest either different evaluation conditions or a slight mismatch in how the models were trained.

Let me check if swapping in the reeval results instead of the downstream variant changes things. With that substitution, the averaged scores shift slightly, bringing the ARC-c number closer to what the paper reports.

Actually, let me try a different seed combination altogether — using kl50_s123_eval gives me different benchmark results, but the averages still don't quite match the paper's numbers. I'm testing various combinations of seed configurations and evaluation sources to see which one produces the reported metrics. I'm trying different combinations of benchmark results to match the paper's reported values, but running into discrepancies—the ARC score comes out to 35.1 instead of the paper's 36.3, which suggests they might be using rounded intermediate values or different evaluation versions. Moving on to check the Qwen 14B GSM8K results, I'm averaging the seed variants to see if I can reconstruct their reported 32.0±5.2 figure.

Computing the mean and standard deviation from the available seeds gives me 30.9±6.8, which doesn't match the paper's claim. I'm wondering if there's a third seed (s123) that was evaluated but isn't showing up in the registry, which could explain the gap between my calculations and their reported numbers. I'm testing different combinations of seed values to see which ones would produce the reported 32.0±5.2 result. With the available registry values, I can't reconstruct that exact mean and standard deviation—the calculations consistently yield around 30.78-30.90 with slightly different standard deviations depending on which s42 variant I use. It seems like either there's a third seed value I'm missing, or the paper's reported numbers come from a different evaluation run than what's in the registry. I'm realizing there's a discrepancy—the paper might actually report "30.9±6.8" rather than "32.0±5.2" for GSM8K, which would change whether the s123 value of ~34.2% even makes sense. I need to verify which numbers the paper actually states before I can determine if this is a genuine inconsistency or just a data registration gap. I'm verifying the model configuration details—LLaMA-3.1-8B checks out at 112× with its feedforward dimension of 14336 divided by 128, and Qwen-2.5-14B should be 148× based on an intermediate size of 18944. Let me calculate the trainable parameters per layer to see if this adds up correctly.

The registry shows qwen14b_kl30_s123 has 117M trainable parameters, but when I work through the math with 40 layers (not 48 as I initially thought), I'm getting around 123.2M, which is slightly higher than the reported 117M. This suggests the feedforward dimension might be smaller than 18944—possibly 13696 instead—which would bring the per-layer calculation closer to the actual total.

I'm realizing there's ambiguity in how d_ff is defined across different sources, and I need to check the actual paper and training code to see what intermediate_size value was used for these models. be around 117M trainable parameters based on the registry spec, which suggests Qwen2.5-14B might have fewer than 40 layers or a slightly different intermediate size than I calculated. Let me verify the exact layer count for this model. I'm realizing the paper's claim of 148× might be incorrect—my calculation shows 107× based on the actual Qwen2.5-14B config. But there's a mismatch: if d_ff were actually 18,944 (148 × 128), the total parameters would be around 147.8M across 48 layers, which doesn't align with the 117M figure from the registry. I should flag this discrepancy rather than assume one source is definitively wrong. I'm verifying the intermediate_size value for Qwen2.5-14B by checking the actual configuration, since the paper's claim of 148× compression would require d_ff=18944, but the registry's 117M parameter count suggests d_ff=13696 (107× compression) instead. I'll flag this discrepancy in my report and then move on to checking another metric—the TEAL 30% uniform ARC-c score where I noticed a mismatch between what the paper reports and what's in the registry. The PIQA discrepancy follows the same pattern—the registry stores `piqa` (raw accuracy) at 71.98% while the paper reports 72.80%, which is likely the acc_norm variant. This points to a broader registry issue where metric naming is inconsistent across experiments rather than an error in the paper itself.

Let me quickly verify a few more data points before putting together the full report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "732ca4f7-5b89-4e36-b42c-edc71c1f58d6",
  "isSidechain": false,
  "requestId": "req_011CbLY47HHTfBvAAC2yS1ug",
  "type": "assistant",
  "uuid": "fa6ff4ae-9242-4362-9367-4da8e2acd513",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QipfU43ndaC96tAFusuTpj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7698,
      "cache_read_input_tokens": 95955,
      "output_tokens": 7351,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7698,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7351,
          "cache_read_input_tokens": 95955,
          "cache_creation_input_tokens": 7698,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7698
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

_source line 79 · 2026-05-24T01:38:10.030Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0179df3BqxMAGF5C3g9RE1vi`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/tmp/registry_metrics.json') as f:\n    reg = json.load(f)\n\n# Check kl50_s42_global_eval for PPL\nprint(\"=== kl50_s42_global_eval ===\")\nif 'kl50_s42_global_eval' in reg:\n    m = reg['kl50_s42_global_eval']['metrics']\n    for k in sorted(m.keys()):\n        print(f\"  {k}: {m[k]}\")\n\n# Check d030_kl50_uniform for 50% uniform PPL\nprint(\"\\n=== d030_kl50_uniform ===\")\nif 'd030_kl50_uniform' in reg:\n    m = reg['d030_kl50_uniform']['metrics']\n    for k in sorted(m.keys()):\n        print(f\"  {k}: {m[k]}\")\n\n# Check multi_seed_kl50_uniform / multi_seed_kl50_global (from paper comments)\nfor eid in ['multi_seed_kl50_uniform', 'multi_seed_kl50_global']:\n    if eid in reg:\n        print(f\"\\n=== {eid} ===\")\n        m = reg[eid]['metrics']\n        for k in sorted(m.keys()): print(f\"  {k}: {m[k]}\")\n    else:\n        print(f\"\\n{eid}: NOT FOUND\")\n\n# Try different combos for KL 50% global PPL\nprint(\"\\n=== KL 50% global PPL combinations ===\")\nimport statistics\ncombos = [\n    (\"bench_kl50_global + kl50_s123_eval + kl50_s456_eval\", \n     [11.7933, 11.745, 11.8614]),\n    (\"bench_kl50_global + kl50_global_s123_reeval + kl50_s456_global_eval\",\n     [11.7933, 11.7184, 11.8057]),\n    (\"bench_kl50_global + mvp_s123 + kl50_s456_global_eval\",\n     [11.7933, 11.9128, 11.8057]),\n    (\"mvp_s42 + mvp_s123 + kl50_s456_global_eval\",\n     [12.0776, 11.9128, 11.8057]),\n]\nfor name, vals in combos:\n    m = statistics.mean(vals)\n    s = statistics.stdev(vals)\n    print(f\"  {name}: mean={m:.2f}±{s:.2f}\")\n\nPYEOF\n",
  "description": "Check KL 50% global PPL combinations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa6ff4ae-9242-4362-9367-4da8e2acd513",
  "isSidechain": false,
  "requestId": "req_011CbLY47HHTfBvAAC2yS1ug",
  "type": "assistant",
  "uuid": "a92d594f-0be8-4c91-bbc6-50ddb15876e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QipfU43ndaC96tAFusuTpj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7698,
      "cache_read_input_tokens": 95955,
      "output_tokens": 7351,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7698,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7351,
          "cache_read_input_tokens": 95955,
          "cache_creation_input_tokens": 7698,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7698
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

_source line 80 · 2026-05-24T01:38:10.114Z_

<details><summary>↩ Tool result · `toolu_0179df3BqxMAGF5C3g9RE1vi`</summary>

```text
=== kl50_s42_global_eval ===
  arc_challenge_acc_norm: 0.3336
  gsm8k_exact_match: 0.0167
  mmlu_acc: 0.2819
  wikitext2_ppl: 11.8038
  winogrande_acc: 0.6338

=== d030_kl50_uniform ===
  actual_sparsity: 0.5
  allocation: uniform
  arc_challenge_acc_norm: 0.3276
  conclusion_note: 50% uniform 未能修复 MMLU/GSM8K collapse. Uniform allocation 的修复效应在 50% sparsity 下消失。
  gsm8k_change_vs_global: +0.91pp (0.0121 → 0.0212, not significant)
  gsm8k_exact_match: 0.0212
  mmlu_acc: 0.2777
  mmlu_change_vs_global: +1.86pp (0.2591 → 0.2777, not significant)
  per_layer_sparsity: uniform 0.500 across all 32 layers
  wikitext2_ppl: 11.96
  winogrande_acc: 0.629

multi_seed_kl50_uniform: NOT FOUND

multi_seed_kl50_global: NOT FOUND

=== KL 50% global PPL combinations ===
  bench_kl50_global + kl50_s123_eval + kl50_s456_eval: mean=11.80±0.06
  bench_kl50_global + kl50_global_s123_reeval + kl50_s456_global_eval: mean=11.77±0.05
  bench_kl50_global + mvp_s123 + kl50_s456_global_eval: mean=11.84±0.07
  mvp_s42 + mvp_s123 + kl50_s456_global_eval: mean=11.93±0.14
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a92d594f-0be8-4c91-bbc6-50ddb15876e1",
  "isSidechain": false,
  "promptId": "de60ee45-84fe-40c7-ad5a-52baa3f09b49",
  "type": "user",
  "uuid": "39b04e43-8a4d-409e-91ed-59e97ad16c52",
  "toolUseResult": {
    "stdout": "=== kl50_s42_global_eval ===\n  arc_challenge_acc_norm: 0.3336\n  gsm8k_exact_match: 0.0167\n  mmlu_acc: 0.2819\n  wikitext2_ppl: 11.8038\n  winogrande_acc: 0.6338\n\n=== d030_kl50_uniform ===\n  actual_sparsity: 0.5\n  allocation: uniform\n  arc_challenge_acc_norm: 0.3276\n  conclusion_note: 50% uniform 未能修复 MMLU/GSM8K collapse. Uniform allocation 的修复效应在 50% sparsity 下消失。\n  gsm8k_change_vs_global: +0.91pp (0.0121 → 0.0212, not significant)\n  gsm8k_exact_match: 0.0212\n  mmlu_acc: 0.2777\n  mmlu_change_vs_global: +1.86pp (0.2591 → 0.2777, not significant)\n  per_layer_sparsity: uniform 0.500 across all 32 layers\n  wikitext2_ppl: 11.96\n  winogrande_acc: 0.629\n\nmulti_seed_kl50_uniform: NOT FOUND\n\nmulti_seed_kl50_global: NOT FOUND\n\n=== KL 50% global PPL combinations ===\n  bench_kl50_global + kl50_s123_eval + kl50_s456_eval: mean=11.80±0.06\n  bench_kl50_global + kl50_global_s123_reeval + kl50_s456_global_eval: mean=11.77±0.05\n  bench_kl50_global + mvp_s123 + kl50_s456_global_eval: mean=11.84±0.07\n  mvp_s42 + mvp_s123 + kl50_s456_global_eval: mean=11.93±0.14",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "a92d594f-0be8-4c91-bbc6-50ddb15876e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 81 · 2026-05-24T01:38:20.307Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014BwhaCoK8KzpdZCTTvFPn1`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/tmp/registry_metrics.json') as f:\n    reg = json.load(f)\n\n# Check Qwen14B TEAL uniform - missing metrics\nprint(\"=== Qwen14B TEAL uniform experiments ===\")\nfor eid in ['qwen14b_teal30_uniform_hspiqa', 'qwen14b_teal30_uniform_gsm8k', 'qwen14b_teal275_uniform_eval_v3', 'qwen14b_teal275_uniform_hspiqa', 'qwen14b_teal275_hspiqa']:\n    if eid in reg:\n        m = reg[eid]['metrics']\n        print(f\"\\n{eid}:\")\n        for k in sorted(m.keys()): print(f\"  {k}: {m[k]}\")\n    else:\n        print(f\"{eid}: NOT FOUND\")\n\n# Check bce30_teal_global (BCE 30% global from main table)\nprint(\"\\n=== BCE 30% global ===\")\nfor eid in ['bce30_teal_global', 'bce_30pct_s42', 'bce_30_s42_uniform_eval', 'bce_50pct_teal_global_unified']:\n    if eid in reg:\n        m = reg[eid]['metrics']\n        print(f\"\\n{eid}:\")\n        for k in sorted(m.keys()): print(f\"  {k}: {m[k]}\")\n    else:\n        print(f\"{eid}: NOT FOUND\")\n\n# Check TEAL 50% uniform downstream\nprint(\"\\n=== TEAL 50% uniform downstream ===\")  \nfor eid in ['bench_teal50_uniform_6task', 'bench_teal50_uniform_gsm8k', 'bench_teal50', 'lm_eval_teal_50pct']:\n    if eid in reg:\n        m = reg[eid]['metrics']\n        print(f\"\\n{eid}:\")\n        for k in sorted(m.keys()): print(f\"  {k}: {m[k]}\")\n    else:\n        print(f\"{eid}: NOT FOUND\")\n\nPYEOF\n",
  "description": "Check remaining missing experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39b04e43-8a4d-409e-91ed-59e97ad16c52",
  "isSidechain": false,
  "requestId": "req_011CbLY47HHTfBvAAC2yS1ug",
  "type": "assistant",
  "uuid": "46703334-58cc-447c-9e8b-9c6c88ed6fc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QipfU43ndaC96tAFusuTpj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7698,
      "cache_read_input_tokens": 95955,
      "output_tokens": 7351,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7698,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7351,
          "cache_read_input_tokens": 95955,
          "cache_creation_input_tokens": 7698,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7698
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

_source line 82 · 2026-05-24T01:38:20.406Z_

<details><summary>↩ Tool result · `toolu_014BwhaCoK8KzpdZCTTvFPn1`</summary>

```text
=== Qwen14B TEAL uniform experiments ===

qwen14b_teal30_uniform_hspiqa:
  hellaswag_acc_norm: 0.6772
  piqa_acc_norm: 0.747

qwen14b_teal30_uniform_gsm8k:
  actual_sparsity: 0.293
  gsm8k_exact_match: 0.5208
  gsm8k_exact_match_flexible: 0.5208
  gsm8k_exact_match_stderr: 0.01376
  gsm8k_exact_match_strict: 0.5208
  sample_len: 1319

qwen14b_teal275_uniform_eval_v3:
  arc_challenge_acc_norm: 0.57
  gsm8k_exact_match: 0.5709
  mmlu_acc: 0.6738
  wikitext2_ppl: 7.7087
  winogrande_acc: 0.7167

qwen14b_teal275_uniform_hspiqa:
  hellaswag_acc: 0.5092
  hellaswag_acc_norm: 0.6993
  piqa_acc: 0.753
  piqa_acc_norm: 0.7476

qwen14b_teal275_hspiqa:
  hellaswag_acc: 0.5092
  hellaswag_acc_norm: 0.6993
  model_sparsity: 0.268
  piqa_acc: 0.753
  piqa_acc_norm: 0.7476
  runtime_seconds: 3551.3

=== BCE 30% global ===
bce30_teal_global: NOT FOUND

bce_30pct_s42:

bce_30_s42_uniform_eval:
  arc_challenge: 0.3319
  gsm8k: 0.0394
  hellaswag: 0.6156
  mmlu: 0.4237
  piqa: 0.741
  ppl: 15.7069
  winogrande: 0.618

bce_50pct_teal_global_unified:
  arc_challenge_acc_norm: 0.2765
  gsm8k_exact_match: 0.019
  mmlu_acc: 0.2614
  wikitext2_ppl: 27.97
  winogrande_acc: 0.5162

=== TEAL 50% uniform downstream ===
bench_teal50_uniform_6task: NOT FOUND

bench_teal50_uniform_gsm8k:
  gsm8k_exact_match_flexible: 0.0174

bench_teal50:
  actual_sparsity: 0.5
  arc_challenge_acc_norm: 0.2841
  gsm8k_exact_match: 0.0197
  mmlu_acc: 0.2832
  wikitext2_ppl: 23.31
  winogrande_acc: 0.5304

lm_eval_teal_50pct:
  actual_sparsity: 0.5
  arc_challenge_acc_norm: 0.291
  arc_challenge_drop_vs_dense: -0.5
  condition: TEAL 50% training-free sparsity
  gsm8k_drop_vs_dense: -0.962
  gsm8k_exact_match_flexible: 0.019
  gsm8k_exact_match_strict: 0.0114
  method: vanilla_teal
  mmlu_acc: 0.2856
  mmlu_drop_vs_dense: -0.563
  model: Llama-3.1-8B
  sparsity: 0.5
  winogrande_acc: 0.5556
  winogrande_drop_vs_dense: -0.289
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46703334-58cc-447c-9e8b-9c6c88ed6fc9",
  "isSidechain": false,
  "promptId": "de60ee45-84fe-40c7-ad5a-52baa3f09b49",
  "type": "user",
  "uuid": "a05d25c2-b27b-4f33-b6f8-e6754075047f",
  "toolUseResult": {
    "stdout": "=== Qwen14B TEAL uniform experiments ===\n\nqwen14b_teal30_uniform_hspiqa:\n  hellaswag_acc_norm: 0.6772\n  piqa_acc_norm: 0.747\n\nqwen14b_teal30_uniform_gsm8k:\n  actual_sparsity: 0.293\n  gsm8k_exact_match: 0.5208\n  gsm8k_exact_match_flexible: 0.5208\n  gsm8k_exact_match_stderr: 0.01376\n  gsm8k_exact_match_strict: 0.5208\n  sample_len: 1319\n\nqwen14b_teal275_uniform_eval_v3:\n  arc_challenge_acc_norm: 0.57\n  gsm8k_exact_match: 0.5709\n  mmlu_acc: 0.6738\n  wikitext2_ppl: 7.7087\n  winogrande_acc: 0.7167\n\nqwen14b_teal275_uniform_hspiqa:\n  hellaswag_acc: 0.5092\n  hellaswag_acc_norm: 0.6993\n  piqa_acc: 0.753\n  piqa_acc_norm: 0.7476\n\nqwen14b_teal275_hspiqa:\n  hellaswag_acc: 0.5092\n  hellaswag_acc_norm: 0.6993\n  model_sparsity: 0.268\n  piqa_acc: 0.753\n  piqa_acc_norm: 0.7476\n  runtime_seconds: 3551.3\n\n=== BCE 30% global ===\nbce30_teal_global: NOT FOUND\n\nbce_30pct_s42:\n\nbce_30_s42_uniform_eval:\n  arc_challenge: 0.3319\n  gsm8k: 0.0394\n  hellaswag: 0.6156\n  mmlu: 0.4237\n  piqa: 0.741\n  ppl: 15.7069\n  winogrande: 0.618\n\nbce_50pct_teal_global_unified:\n  arc_challenge_acc_norm: 0.2765\n  gsm8k_exact_match: 0.019\n  mmlu_acc: 0.2614\n  wikitext2_ppl: 27.97\n  winogrande_acc: 0.5162\n\n=== TEAL 50% uniform downstream ===\nbench_teal50_uniform_6task: NOT FOUND\n\nbench_teal50_uniform_gsm8k:\n  gsm8k_exact_match_flexible: 0.0174\n\nbench_teal50:\n  actual_sparsity: 0.5\n  arc_challenge_acc_norm: 0.2841\n  gsm8k_exact_match: 0.0197\n  mmlu_acc: 0.2832\n  wikitext2_ppl: 23.31\n  winogrande_acc: 0.5304\n\nlm_eval_teal_50pct:\n  actual_sparsity: 0.5\n  arc_challenge_acc_norm: 0.291\n  arc_challenge_drop_vs_dense: -0.5\n  condition: TEAL 50% training-free sparsity\n  gsm8k_drop_vs_dense: -0.962\n  gsm8k_exact_match_flexible: 0.019\n  gsm8k_exact_match_strict: 0.0114\n  method: vanilla_teal\n  mmlu_acc: 0.2856\n  mmlu_drop_vs_dense: -0.563\n  model: Llama-3.1-8B\n  sparsity: 0.5\n  winogrande_acc: 0.5556\n  winogrande_drop_vs_dense: -0.289",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "46703334-58cc-447c-9e8b-9c6c88ed6fc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 83_

```json
{
  "type": "last-prompt",
  "leafUuid": "a05d25c2-b27b-4f33-b6f8-e6754075047f",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01"
}
```

---


### Runtime record

_source line 84_

```json
{
  "type": "ai-title",
  "aiTitle": "Final data consistency audit registry vs paper",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01"
}
```

---


### Assistant

_source line 85 · 2026-05-24T01:39:51.128Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a much clearer picture. Let me compile the remaining issues:

1. **KL 50% global PPL**: The combination `bench_kl50_global + mvp_s123 + kl50_s456_global_eval` gives 11.84±0.07. The paper says 11.84±0.15. The mean matches but the std doesn't (0.07 vs 0.15). So the paper may have used a different combination, possibly involving an older s42 eval that gave a different PPL. Let me check if kl50_s42_global_eval gives 11.8038:
   
   Testing with kl50_s42_global_eval (11.8038) + mvp_s123 (11.9128) + kl50_s456_global_eval (11.8057) gives a mean of 11.84 which matches, and calculating the standard deviation across these three values yields approximately 0.0624, which is closer to the paper's reported 0.15 than my previous attempt.

Let me try other combinations to see if I can get closer to that 0.15 standard deviation. Testing mvp_s42 (12.0776) + mvp_s123 (11.9128) + kl50_s456_global_eval (11.8057) gives a mean of 11.93, which doesn't match the paper's 11.84. Trying bench_kl50_global (11.7933) + mvp_s123 (11.9128) + kl50_s456_eval (11.8614) gives 11.86, also not quite right. Let me check if using kl50_s42_global_eval (11.8038) + mvp_s123 (11.9128) + kl50_s456_eval (11.8614) works better.

That gives 11.86 as well. Switching to kl50_s42_global_eval (11.8038) + kl50_s123_eval (11.745) + kl50_s456_eval (11.8614) yields 11.80, and bench_kl50_global (11.7933) + kl50_s123_eval (11.745) + kl50_s456_global_eval (11.8057) gives 11.78. None of these combinations are hitting exactly 11.84, so I'm trying another approach with mvp_s42 (12.0776) + kl50_global_s123_reeval (11.7184) and continuing from there.

Looking at the paper's experiment IDs, I notice kl50_global_s123_downstream_v2 doesn't have PPL values available, and kl50_global_s456_eval doesn't exist in the registry—only kl50_s456_global_eval does. This is narrowing down which combinations are actually viable.

Now I'm checking what happens when I use bench_kl50_global, kl50_global_s123_downstream_v2, and kl50_s456_global_eval across the three seeds to compute the downstream metrics at 50% global. The averages I'm getting don't quite match what the paper reports—there's a consistent gap between my calculations and their published numbers. The averages still don't match the paper's reported values exactly, and the standard deviations are close but off by a few tenths of a point. It seems like the paper might have used different evaluation runs than what's in the registry, making it impossible to reproduce these numbers precisely. I should flag this KL 50% global row as having serious data provenance issues in my report, especially since the PPL value can't be reconstructed from any combination of available experiments.

Now I'm checking the Qwen 14B TEAL 30% uniform results, but the registry only has TEAL at 27.5% sparsity, not 30%. The paper reports different metrics for the 30% version, so this particular configuration appears to be missing from the registry entirely.

Let me verify the "148×" claim by examining the model parameters. The registry shows the trainable parameters are about 117M, which represents 0.793% of the base model—that works out to roughly 14.75B total parameters, consistent with Qwen2.5-14B. Now I'm trying to calculate whether 117M predictors aligns with the claimed compression ratio by working through the layer dimensions. Working backward from the 117M parameter count, I get an intermediate_size of 13,923, but the HuggingFace config shows 13,696 instead—there's a discrepancy that suggests the model might use a different intermediate_size value in practice. Let me check if Qwen2.5-14B actually uses 18,944 or if I need to look at the actual model configuration loaded from the local path in the training script. I'm testing different combinations of layer counts and feed-forward dimensions to see which configuration matches the 117M parameter count, but none of them align exactly—the discrepancy might be due to bias terms or a slightly different calculation method.

Looking at the paper's claim that d_ff/d_model = 148 for Qwen14B, that would suggest d_ff = 18944 and imply only 38 layers to reach 117M total, which doesn't match the standard Qwen2.5-14B architecture of 48 layers with d_ff around 13696. The actual ratio is probably closer to 109×, so I'll note that the 148× claim seems incorrect.

Now I'm checking the C4 control table for discrepancies in the WikiText-trained predictor's performance on HS and PIQA—the paper reports HS=69.4 and PIQA=75.5, but I need to verify these against what's in the registry.

Looking through the registry entries, the kl30_uniform_hellaswag_piqa variants show HS=70.85 and PIQA=74.81, which don't match the paper's values. I'm also checking the OOD downstream table from the appendix, which shows WikiText calibration with HS=70.9 and PIQA=74.8—closer to the registry but still not exactly matching the paper's reported numbers. These discrepancies suggest the paper's values might come from an unregistered evaluation run. I'm noticing a discrepancy in the HellaSwag and PIQA scores for WikiText KL30 uniform across the paper—the OOD downstream table shows HS=70.9 and PIQA=74.8, but the C4 control table lists HS=69.4 and PIQA=75.5, which is inconsistent by about 1.5 percentage points for HellaSwag and 0.7 for PIQA.

Looking at the source annotations, the OOD downstream table references a specific experiment ID, but the C4 control table doesn't document where its HS/PIQA values come from, making it unclear which set is correct or if they're measuring different evaluation runs. Now I'm noticing the paper uses different evaluation runs for the same metrics across tables—the OOD downstream table references a v2 evaluation while the C4 control table appears to use an older version, which creates an internal consistency problem.

I should write up the full report now that I have everything mapped out. I'll organize it by summary statistics, individual data points from each table, claims made in the prose, and then flag both critical and minor discrepancies I've found.

Before I finalize though, I want to double-check the GSM8K numbers—the abstract claims a 20.1pp gap between TEAL and KL uniform, but the registry shows different values depending on which seed average I use, and that discrepancy might affect how I characterize the magnitude of the reported differences. I've verified the math checks out—the 20.1 percentage point difference matches the reported values, and the standard deviation estimates are consistent across the abstract and introduction. Now I'm ready to write up the report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a05d25c2-b27b-4f33-b6f8-e6754075047f",
  "isSidechain": false,
  "requestId": "req_011CbLYE3NAeCN1BELz5o4Wd",
  "type": "assistant",
  "uuid": "6bb23c08-f45c-4e57-bef8-bdf75d482e7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014fNaqEXAgfn8sf78F5q33J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8906,
      "cache_read_input_tokens": 103653,
      "output_tokens": 5220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8906,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5220,
          "cache_read_input_tokens": 103653,
          "cache_creation_input_tokens": 8906,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8906
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

_source line 86 · 2026-05-24T01:39:51.130Z_

Now I have all the data. Let me compile the comprehensive report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6bb23c08-f45c-4e57-bef8-bdf75d482e7a",
  "isSidechain": false,
  "requestId": "req_011CbLYE3NAeCN1BELz5o4Wd",
  "type": "assistant",
  "uuid": "e6b8cfee-db3e-44d1-80ab-219ebb1c4847",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014fNaqEXAgfn8sf78F5q33J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8906,
      "cache_read_input_tokens": 103653,
      "output_tokens": 5220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8906,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5220,
          "cache_read_input_tokens": 103653,
          "cache_creation_input_tokens": 8906,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8906
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

_source line 87 · 2026-05-24T01:39:59.690Z_

<details open><summary>🔧 Tool call — Bash · `toolu_018yeBVkzRmsnrC6DDHzHfC6`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\nwith open('/tmp/registry_metrics.json') as f:\n    reg = json.load(f)\n\n# Final checks for report\n# 1. Qwen14B - what does the registry say for s123 GSM8K?\n# Already confirmed: not in any experiment\n\n# 2. Cross-check OOD downstream table values\nprint(\"=== c4_ood_downstream_kl30 ===\")\nif 'c4_ood_downstream_kl30' in reg:\n    m = reg['c4_ood_downstream_kl30']['metrics']\n    for k in sorted(m.keys()): print(f\"  {k}: {m[k]}\")\n\n# 3. Check constraint experiments\nprint(\"\\n=== constraint experiments ===\")\nfor eid in ['constraint_protect_late', 'constraint_remove_valley']:\n    if eid in reg:\n        m = reg[eid]['metrics']\n        print(f\"\\n{eid}:\")\n        for k in sorted(m.keys()): print(f\"  {k}: {m[k]}\")\n    else:\n        print(f\"{eid}: NOT FOUND\")\n\n# 4. C4 control eval\nprint(\"\\n=== c4_kl30_s42_eval ===\")\nif 'c4_kl30_s42_eval' in reg:\n    m = reg['c4_kl30_s42_eval']['metrics']\n    for k in sorted(m.keys()): print(f\"  {k}: {m[k]}\")\n\n# 5. Check the intro \"10.30\" TEAL matched sparsity PPL\nprint(f\"\\nteal_28.5pct_sanity PPL: {reg.get('teal_28.5pct_sanity', {}).get('metrics', {})}\")\n\n# 6. Check TEAL uniform PPL at 30% nominal (actual 29.3%)\n# Paper says \"TEAL at matched actual sparsity (8.81 vs. 10.30, both at 28.5%)\"\n# and \"Actual sparsity: KL 28.5% vs. TEAL 29.3% at 30%\"\n# So TEAL at 28.5% = 10.30\n\nPYEOF\n",
  "description": "Final verification checks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6b8cfee-db3e-44d1-80ab-219ebb1c4847",
  "isSidechain": false,
  "requestId": "req_011CbLYE3NAeCN1BELz5o4Wd",
  "type": "assistant",
  "uuid": "32222358-afc3-4607-85f6-d4243be63076",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014fNaqEXAgfn8sf78F5q33J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8906,
      "cache_read_input_tokens": 103653,
      "output_tokens": 5220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8906,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5220,
          "cache_read_input_tokens": 103653,
          "cache_creation_input_tokens": 8906,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8906
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

_source line 88 · 2026-05-24T01:39:59.769Z_

<details><summary>↩ Tool result · `toolu_018yeBVkzRmsnrC6DDHzHfC6`</summary>

```text
=== c4_ood_downstream_kl30 ===
  arc_challenge_acc_norm: 0.4036
  gsm8k_exact_match: 0.0629
  hellaswag_acc_norm: 0.7074
  mmlu_acc: 0.4137
  model_level_sparsity: 0.295
  piqa_acc_norm: 0.7399
  winogrande_acc: 0.693

=== constraint experiments ===
constraint_protect_late: NOT FOUND
constraint_remove_valley: NOT FOUND

=== c4_kl30_s42_eval ===
  arc_challenge_acc_norm: 0.4309
  gsm8k_exact_match: 0.0409
  hellaswag_acc_norm: 0.6924
  mmlu_acc: 0.3995
  piqa_acc_norm: 0.7503
  sparsity: 0.295
  wikitext2_ppl: 11.554
  winogrande_acc: 0.6867

teal_28.5pct_sanity PPL: {'wikitext2_ppl': 10.3}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32222358-afc3-4607-85f6-d4243be63076",
  "isSidechain": false,
  "promptId": "de60ee45-84fe-40c7-ad5a-52baa3f09b49",
  "type": "user",
  "uuid": "16d90a51-29b5-428d-9cf3-0aebaaf7e5b5",
  "toolUseResult": {
    "stdout": "=== c4_ood_downstream_kl30 ===\n  arc_challenge_acc_norm: 0.4036\n  gsm8k_exact_match: 0.0629\n  hellaswag_acc_norm: 0.7074\n  mmlu_acc: 0.4137\n  model_level_sparsity: 0.295\n  piqa_acc_norm: 0.7399\n  winogrande_acc: 0.693\n\n=== constraint experiments ===\nconstraint_protect_late: NOT FOUND\nconstraint_remove_valley: NOT FOUND\n\n=== c4_kl30_s42_eval ===\n  arc_challenge_acc_norm: 0.4309\n  gsm8k_exact_match: 0.0409\n  hellaswag_acc_norm: 0.6924\n  mmlu_acc: 0.3995\n  piqa_acc_norm: 0.7503\n  sparsity: 0.295\n  wikitext2_ppl: 11.554\n  winogrande_acc: 0.6867\n\nteal_28.5pct_sanity PPL: {'wikitext2_ppl': 10.3}",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "32222358-afc3-4607-85f6-d4243be63076",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 89 · 2026-05-24T01:39:59.773Z_

```json
{
  "parentUuid": "16d90a51-29b5-428d-9cf3-0aebaaf7e5b5",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "1d43fc08-2dd0-4054-a666-847121fa2efd",
  "timestamp": "2026-05-24T01:39:59.773Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---


### Assistant

_source line 90 · 2026-05-24T01:40:50.853Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have everything. Let me also check the OOD downstream table values:

Paper OOD downstream table (tab:ood_downstream):
WikiText: ARC-c=40.8, WG=68.6, MMLU=40.6, GSM8K=7.4, HS=70.9, PIQA=74.8
C4 OOD: ARC-c=40.4, WG=69.3, MMLU=41.4, GSM8K=6.3, HS=70.7, PIQA=74.0


Verifying the registry values against the paper's C4 OOD downstream results, and they're matching up correctly across all the benchmarks. Continuing to verify the WikiText calibration results—the GSM8K score rounds from 7.35 to 7.4, and both the HellaSwag and PIQA values match the paper when rounded. The OOD downstream table checks out completely, but I'm noticing the C4 control table has divergent values that need investigation.

Actually, these are measuring different things entirely. The OOD downstream table keeps the WikiText-trained predictor fixed and swaps the calibration data between WikiText and C4, while the C4 control table trains separate predictors on each dataset. So the HellaSwag and PIQA discrepancies make sense—they're from fundamentally different experimental setups.

But the C4 control table's WikiText row should match the main benchmark results since it's the same predictor. Looking at the metrics from the appendix, the perplexity and other benchmarks align perfectly with the original run, but the HS and PIQA values are showing up as 69.4 and 75.5, which I need to verify against the source data.

Now checking the C4 row itself — the perplexity, ARC-c, WG, MMLU, and GSM8K all match the c4_kl30_s42_eval run exactly, and HS checks out at 69.24, but I'm seeing a discrepancy with the PIQA value that the paper reports.

The WikiText row presents a bigger problem: those HS and PIQA scores don't correspond to any registered experiment I can find, which suggests they came from an unregistered evaluation run. This is a data provenance issue that needs flagging.

I've identified enough inconsistencies now to write up a comprehensive report. Let me organize the findings by severity, starting with the critical mismatches. Looking at the downstream table for TEAL 30% uniform, the paper reports PIQA at 72.80 but the registry shows 71.98—this might be an accuracy versus accuracy_norm discrepancy. The experiments prose claims 148× compression for Qwen14B, but calculating from the registry's trainable parameters and layer count suggests it's closer to 109×. Beyond these numerical mismatches, there are entire rows missing from the registry: BCE 30% global is completely absent, and TEAL 50% uniform is missing several benchmark results including ARC-c, WG, and MMLU.

Continuing through the tables, ARC-c values are particularly problematic since the registry stores `arc_challenge` while the paper references `arc_challenge_acc_norm`, making the reported 39.33 unverifiable against the registry's 37.71. The Qwen14B tables have similar gaps—four downstream metrics missing for BCE global, and multiple benchmarks absent for TEAL uniform. The KL uniform GSM8K entry for seed 123 doesn't exist in the registry at all, and the paper's reported 32.0±5.2 differs from what the two-seed registry average shows. Several ablation configurations like JSD 50%, RevKL 50%, and various perlayer variants are completely missing from the registry.

For the K-curve analysis, the K=4 row only has downstream results for seed 42, leaving the other seeds' PPL values unregistered. Extended downstream experiments with KL 30% uniform on HS and PIQA only have seed 42 individually registered, making the three-seed mean impossible to verify. TEAL 50% uniform is missing HS and PIQA entirely, and the constraint experiments don't appear in the registry at all. Beyond these major gaps, there are minor rounding discrepancies scattered throughout—PPL and ARC-c standard deviations off by 0.1 percentage points, and a few other metrics with similar small variations.

Now I'm ready to write up the report file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d43fc08-2dd0-4054-a666-847121fa2efd",
  "isSidechain": false,
  "requestId": "req_011CbLYMN7ygejr5tud6acd1",
  "type": "assistant",
  "uuid": "2c64d7a1-3935-4cd6-b020-1d5278fa623b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016vWJHGba6EQsyKJb6nnn1L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5620,
      "cache_read_input_tokens": 112559,
      "output_tokens": 2667,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5620,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2667,
          "cache_read_input_tokens": 112559,
          "cache_creation_input_tokens": 5620,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5620
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

_source line 91 · 2026-05-24T01:40:50.859Z_

All data collected. Writing the comprehensive report now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c64d7a1-3935-4cd6-b020-1d5278fa623b",
  "isSidechain": false,
  "requestId": "req_011CbLYMN7ygejr5tud6acd1",
  "type": "assistant",
  "uuid": "5fdc1d0a-6698-47aa-a461-5f3345cba18d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016vWJHGba6EQsyKJb6nnn1L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5620,
      "cache_read_input_tokens": 112559,
      "output_tokens": 2667,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5620,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2667,
          "cache_read_input_tokens": 112559,
          "cache_creation_input_tokens": 5620,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5620
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

_source line 92 · 2026-05-24T01:40:53.460Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Us4vEhyhJNUBVXio7cetuh`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5fdc1d0a-6698-47aa-a461-5f3345cba18d",
  "isSidechain": false,
  "requestId": "req_011CbLYMN7ygejr5tud6acd1",
  "type": "assistant",
  "uuid": "4aac73da-2b7e-4b89-b94f-faf24f59c397",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016vWJHGba6EQsyKJb6nnn1L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5620,
      "cache_read_input_tokens": 112559,
      "output_tokens": 2667,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5620,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2667,
          "cache_read_input_tokens": 112559,
          "cache_creation_input_tokens": 5620,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5620
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

_source line 93 · 2026-05-24T01:40:53.467Z_

<details><summary>↩ Tool result · `toolu_01Us4vEhyhJNUBVXio7cetuh`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4aac73da-2b7e-4b89-b94f-faf24f59c397",
  "isSidechain": false,
  "promptId": "de60ee45-84fe-40c7-ad5a-52baa3f09b49",
  "type": "user",
  "uuid": "badad183-e25c-4dd6-bdc1-574cd3698ed9",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 25
  },
  "sourceToolAssistantUUID": "4aac73da-2b7e-4b89-b94f-faf24f59c397",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 94_

```json
{
  "type": "last-prompt",
  "leafUuid": "badad183-e25c-4dd6-bdc1-574cd3698ed9",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01"
}
```

---


### Runtime record

_source line 95_

```json
{
  "type": "ai-title",
  "aiTitle": "Final data consistency audit registry vs paper",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01"
}
```

---


### Tool call

_source line 96 · 2026-05-24T01:42:25.163Z_

<details open><summary>🔧 Tool call — Write · `toolu_01PkMtJYnDJPazMq5yJhrvuC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/r28_data_consistency_report.md",
  "content": "# R28 Data Consistency Report: Registry ↔ Paper Cross-Verification\n\n**Date:** 2026-05-24\n**Scope:** All quantitative claims in paper (tables, inline prose, appendices) vs. registry experiments\n\n---\n\n## Summary\n\n| Category | Count |\n|----------|-------|\n| Total data points checked | ~284 |\n| ✅ Match (within rounding tolerance) | 237 |\n| ❌ Mismatch (value differs from registry) | 8 |\n| ⚠️ Not found / unverifiable from registry | 31 |\n| ~  Minor rounding (std off by 0.01-0.1) | 8 |\n\n---\n\n## Critical Mismatches (❌)\n\n### 1. Table 2 — KL 50% global row (4 of 5 metrics)\n\nPaper claims PPL 11.84±0.15, ARC-c 36.3±3.2, WG 63.8±0.3, GSM8K 2.7±1.3.\n\n**No single combination of 3 registry experiments reproduces these values.**\n\n| Metric | Paper | Best registry combo | Source exp_ids |\n|--------|-------|-------------------|----------------|\n| PPL | 11.84±0.15 | 11.84±0.07 | bench_kl50_global(11.79) + mvp_kl_norm_v2_s123(11.91) + kl50_s456_global_eval(11.81) |\n| ARC-c | 36.3±3.2 | 35.1±3.5 | bench_kl50_global(32.85) + kl50_global_s123_downstream_v2(39.16) + kl50_s456_global_eval(33.19) |\n| WG | 63.8±0.3 | 64.1±0.7 | same combo |\n| MMLU | 28.3±0.7 | 28.3±0.7 | ✅ matches |\n| GSM8K | 2.7±1.3 | 2.3±1.1 | same combo |\n\n**Root cause:** The paper cites `bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval` but:\n- `kl50_global_s123_downstream_v2` has no PPL (only downstream metrics)\n- `kl50_global_s456_eval` does not exist in registry (correct key: `kl50_s456_global_eval`)\n- PPL and downstream metrics appear to come from different eval runs for the same seeds, mixed inconsistently\n\n### 2. C4 control table (tab:c4_control) — WikiText row HS/PIQA\n\n| Metric | C4 control table | OOD downstream table | Registry (kl30_uniform_hellaswag_piqa_v2) |\n|--------|-----------------|---------------------|------------------------------------------|\n| HS | 69.4 | 70.9 | 70.85 |\n| PIQA | 75.5 | 74.8 | 74.81 |\n\n**Internal inconsistency:** Two tables in the same paper report different HS/PIQA values for the same WikiText-trained KL 30% uniform predictor (s42). The OOD downstream table matches the registry; the C4 control table does not. Source of 69.4/75.5 is untraced.\n\n### 3. C4 control table — C4 row PIQA\n\nPaper=74.86, registry (`c4_kl30_s42_eval`)=75.03. Off by **0.17pp**.\n\n### 4. Extended downstream table (tab:downstream) — TEAL 30% uniform PIQA\n\nPaper=72.80, registry (`teal_30pct_uniform_multiseed_eval`)=71.98. Off by **0.82pp**. Registry stores `piqa` (likely raw acc) rather than `piqa_acc_norm`; possible metric variant confusion.\n\n### 5. Experiments prose — \"148× vs. 112× compression\" for Qwen14B\n\nPaper claims Qwen-2.5-14B has d_ff/d_b = 148× (implying d_ff=18,944). Registry shows `trainable_params='117M (0.793%)'` for `qwen14b_kl30_s123`. Back-computing:\n\n- 117M / 48 layers = 2.44M per layer\n- 2.44M = (5120×128) + (128×d_ff) → d_ff ≈ 13,923\n- 13,923 / 128 ≈ **109×**, not 148×\n- LLaMA's 112× (14336/128) is correct\n\nThe 148× claim is inconsistent with the registered trainable parameter count.\n\n---\n\n## Data Provenance Issues (⚠️ — unverifiable from registry)\n\n### Table 2\n\n| Row | Missing | Notes |\n|-----|---------|-------|\n| BCE 30% global | All 5 metrics | `bce30_teal_global` absent from registry entirely |\n| TEAL 30% uniform ARC-c | acc_norm variant | Registry stores `arc_challenge`=37.71 (acc), not acc_norm; paper=39.33 plausible but unverified |\n| TEAL 50% uniform | ARC-c, WG, MMLU | No full downstream eval registered for TEAL 50% uniform |\n\n### Ablation Table (Table 4)\n\n| Row | Missing | Notes |\n|-----|---------|-------|\n| JSD 50% | PPL 12.54 | `jsd_ablation_s42` absent from registry |\n| Reverse KL 50% | PPL 12.80 | `reverse_kl_ablation_s42` absent |\n| Per-layer KL K=1 50% | PPL 34.85 | `perlayer_kl_50_s42` absent |\n| Per-layer KL K=4 30%/50% | Both PPL values | Experiments registered but metrics empty |\n| BCE + STE 50% | PPL 60.54 | `bce_ste_s42` absent |\n\nAll Δ_50 arithmetic is internally consistent (computed correctly from the stated 50% values).\n\n### Qwen-2.5-14B Table\n\n| Row | Missing | Notes |\n|-----|---------|-------|\n| BCE global | ARC-c, WG, MMLU, GSM8K | `qwen14b_bce30_s42_eval` absent |\n| TEAL uniform | PPL, ARC-c, WG, MMLU | No 4-task eval registered for TEAL 30% uniform |\n| KL uniform GSM8K | s123 value | Only s42 (35.71%) and s456 (26.08%) in registry; 2-seed mean=30.9±6.8, paper claims 32.0±5.2 (implies unregistered s123≈34.2%) |\n\n### K-curve Table\n\n| Row | Missing | Notes |\n|-----|---------|-------|\n| K=4 | PPL (s123, s456), all downstream (s123, s456) | Only s42 downstream in registry |\n\n### Other\n\n- **Constraint experiments** (`constraint_protect_late`, `constraint_remove_valley`): Not in registry. Paper claims MMLU +3.4pp, GSM8K +1.6pp from removing valley — unverifiable.\n- **Extended downstream** — KL 30% uniform HS/PIQA: Only s42 registered; 3-seed mean (71.07±0.54 / 74.95±0.25) unverifiable.\n- **Extended downstream** — TEAL 50% uniform HS/PIQA: `bench_teal50_uniform_6task` absent.\n\n---\n\n## Minor Rounding Discrepancies (~)\n\nAll means match; only std values differ by 0.01-0.1 due to rounding of pre-rounded inputs.\n\n| Location | Metric | Paper | Computed | Exact |\n|----------|--------|-------|----------|-------|\n| Table 2 MSE 30% | PPL std | 1.68 | 1.67 | 1.666 |\n| Table 2 MSE 30% | ARC-c std | 4.1 | 4.0 | 4.03 |\n| Table 2 MSE 30% | WG std | 2.6 | 2.5 | 2.54 |\n| Table 2 KL 50% uniform | PPL std | 0.07 | 0.08 | 0.076 |\n| K-curve K=8 | ARC-c std | 1.0 | 1.1 | 1.06 |\n| K-curve K=16 | MMLU std | 2.9 | 2.8 | 2.77 |\n| Mistral KL30 downstream | WG std | 1.2 | 1.1 | 1.14 |\n| Table 3 footnote | C1 s42 PPL gap | 0.65pp | 0.63pp | 0.6306 |\n\n---\n\n## Verified Tables (all data points match ✅)\n\n### Table 3 — C1 Target-Swap Ablation\n40/40 data points match exactly. All seeds (s42/s123/s456) at 30% and 50% verified.\n\n### Cross-Architecture Table (tab:cross_arch)\nAll 12 PPL values (6 KL + 6 TEAL across Mistral and LLaMA at 30/50/70%) match exactly.\n\n### Mistral Downstream Table (tab:mistral_downstream)\nAll 21 values match (dense + KL 3-seed + TEAL single-seed across 7 metrics).\n\n### Latency Table (tab:latency)\nAll 10 data points match exactly (ms/fwd and tok/s for 5 configurations).\n\n### OOD Table (tab:ood)\nAll 4 C4 PPL values match. OOD uniform 3-seed (18.22/16.37/16.36, mean 16.98±1.07) match.\n\n### OOD Downstream Table (tab:ood_downstream)\nAll 12 values match (WikiText and C4 calibration across 6 metrics).\n\n### Dense Baseline\nAll 5 metrics match exactly (PPL 6.12, ARC-c 58.28, WG 78.06, MMLU 65.27, GSM8K 48.75).\n\n### Appendix Tables\n- Bottleneck sensitivity (tab:db_sensitivity): all values match\n- Temperature schedule (tab:tau_sensitivity): all values match\n- Training convergence (tab:training_convergence): all values match\n- Lagrangian dynamics (tab:lagrangian): all values match\n\n---\n\n## Verified Inline Prose Claims\n\n| Claim | Verification | Status |\n|-------|-------------|--------|\n| \"14.5% reduction\" (8.81 vs 10.30) | (10.30−8.81)/10.30=14.47%→14.5% | ✅ |\n| \"MMLU −5.2pp on 8B\" | 45.86−40.7=5.16≈5.2 | ✅ |\n| \"GSM8K −20.1pp on 14B\" | 52.1−32.0=20.1 (if 3-seed=32.0) | ✅ (but 32.0 unverified, see above) |\n| \"7.3× MMLU σ\" | 9.5/1.3=7.31 | ✅ |\n| \"−17.3% Mistral PPL\" | (8.38−6.93)/8.38=17.3% | ✅ |\n| \"MMLU −2.8pp on 14B\" | 66.34−63.55=2.79≈2.8 | ✅ (but TEAL MMLU 66.34 unregistered) |\n| \"6.4% latency overhead\" | (126.78−119.11)/119.11=6.44% | ✅ |\n| \"2.39× worse than KL\" | 28.13/11.79=2.386 | ✅ |\n| \"F1 0.613 vs 0.540\" | registry kl_bce_f1_oracle: 0.6128/0.5397 | ✅ |\n| \"139% worse PPL\" | (28.13−11.79)/11.79=138.7%≈139% | ✅ |\n| \"33.8% STE improvement\" | (15.77−11.79)/11.79=33.8% | ✅ |\n| \"JSD +6.4%, RevKL +8.6%\" | (12.54−11.79)/11.79=6.4%, (12.80−11.79)/11.79=8.6% | ✅ |\n| \"K=16 PPL 8.67±0.02\" | registry 3-seed: 8.67±0.02 | ✅ |\n| \"coupling range 2.08 PPL\" | 10.75−8.67=2.08 | ✅ |\n| \"signal type gap 9.47 PPL\" | 18.52−9.05=9.47 | ✅ |\n| \"Jaccard 68% at 50%\" | c1_mask_overlap mean=0.6824 | ✅ |\n| \"cross-seed Jaccard 36.3%\" | appendix consistent | ✅ |\n| \"75.9M params, <1%\" | 32×2.37M=75.84M≈75.9M | ✅ |\n| \"50% PPL reduction at 50% sparsity\" | (23.90−11.92)/23.90=50.1% | ✅ |\n\n---\n\n## Recommendations\n\n### Must-fix before submission\n\n1. **KL 50% global row (Table 2):** Reconcile PPL and downstream metrics with a single consistent set of 3-seed eval runs. Document which exp_ids provide PPL vs downstream for each seed.\n\n2. **C4 control table HS/PIQA (WikiText row):** Values 69.4/75.5 are inconsistent with the OOD downstream table (70.9/74.8) and with registry (70.85/74.81). Use values from registered experiment.\n\n3. **C4 control table PIQA (C4 row):** Paper says 74.86, registry says 75.03. Verify and correct.\n\n4. **148× compression claim:** Back-computation from registered 117M params implies d_ff≈13,923 (109×), not 18,944 (148×). Verify Qwen-2.5-14B's actual intermediate_size and correct.\n\n### Should-fix\n\n5. **Qwen14B GSM8K (32.0±5.2):** Register the s123 GSM8K evaluation to make this claim verifiable. Current 2-seed data gives 30.9±6.8.\n\n6. **Extended downstream TEAL 30% uniform PIQA:** Verify whether paper uses acc_norm (72.80) while registry stored acc (71.98).\n\n7. **BCE 30% global row (Table 2):** Register the source experiment or add exp_id comment.\n\n### Nice-to-have\n\n8. Register missing ablation experiments (JSD 50%, RevKL 50%, perlayer KL 50%, BCE+STE 50%, K=4 metrics).\n9. Standardize registry metric key names (e.g. `arc_challenge` vs `arc_challenge_acc_norm`).\n10. Minor std rounding: adopt consistent rounding convention (round exact, not round pre-rounded).\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "badad183-e25c-4dd6-bdc1-574cd3698ed9",
  "isSidechain": false,
  "requestId": "req_011CbLYRLJwzSneR3QCRLE6n",
  "type": "assistant",
  "uuid": "c31fcc3d-068f-422d-9849-823e7168dd7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W8fiatA9HaCFJQsjdFFydT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3286,
      "cache_read_input_tokens": 118179,
      "output_tokens": 4100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3286,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4100,
          "cache_read_input_tokens": 118179,
          "cache_creation_input_tokens": 3286,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3286
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

_source line 97 · 2026-05-24T01:42:25.190Z_

<details><summary>↩ Tool result · `toolu_01PkMtJYnDJPazMq5yJhrvuC`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/r28_data_consistency_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c31fcc3d-068f-422d-9849-823e7168dd7f",
  "isSidechain": false,
  "promptId": "de60ee45-84fe-40c7-ad5a-52baa3f09b49",
  "type": "user",
  "uuid": "a8453a6d-4b89-44a5-8955-4660a0208c88",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/r28_data_consistency_report.md",
    "content": "# R28 Data Consistency Report: Registry ↔ Paper Cross-Verification\n\n**Date:** 2026-05-24\n**Scope:** All quantitative claims in paper (tables, inline prose, appendices) vs. registry experiments\n\n---\n\n## Summary\n\n| Category | Count |\n|----------|-------|\n| Total data points checked | ~284 |\n| ✅ Match (within rounding tolerance) | 237 |\n| ❌ Mismatch (value differs from registry) | 8 |\n| ⚠️ Not found / unverifiable from registry | 31 |\n| ~  Minor rounding (std off by 0.01-0.1) | 8 |\n\n---\n\n## Critical Mismatches (❌)\n\n### 1. Table 2 — KL 50% global row (4 of 5 metrics)\n\nPaper claims PPL 11.84±0.15, ARC-c 36.3±3.2, WG 63.8±0.3, GSM8K 2.7±1.3.\n\n**No single combination of 3 registry experiments reproduces these values.**\n\n| Metric | Paper | Best registry combo | Source exp_ids |\n|--------|-------|-------------------|----------------|\n| PPL | 11.84±0.15 | 11.84±0.07 | bench_kl50_global(11.79) + mvp_kl_norm_v2_s123(11.91) + kl50_s456_global_eval(11.81) |\n| ARC-c | 36.3±3.2 | 35.1±3.5 | bench_kl50_global(32.85) + kl50_global_s123_downstream_v2(39.16) + kl50_s456_global_eval(33.19) |\n| WG | 63.8±0.3 | 64.1±0.7 | same combo |\n| MMLU | 28.3±0.7 | 28.3±0.7 | ✅ matches |\n| GSM8K | 2.7±1.3 | 2.3±1.1 | same combo |\n\n**Root cause:** The paper cites `bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval` but:\n- `kl50_global_s123_downstream_v2` has no PPL (only downstream metrics)\n- `kl50_global_s456_eval` does not exist in registry (correct key: `kl50_s456_global_eval`)\n- PPL and downstream metrics appear to come from different eval runs for the same seeds, mixed inconsistently\n\n### 2. C4 control table (tab:c4_control) — WikiText row HS/PIQA\n\n| Metric | C4 control table | OOD downstream table | Registry (kl30_uniform_hellaswag_piqa_v2) |\n|--------|-----------------|---------------------|------------------------------------------|\n| HS | 69.4 | 70.9 | 70.85 |\n| PIQA | 75.5 | 74.8 | 74.81 |\n\n**Internal inconsistency:** Two tables in the same paper report different HS/PIQA values for the same WikiText-trained KL 30% uniform predictor (s42). The OOD downstream table matches the registry; the C4 control table does not. Source of 69.4/75.5 is untraced.\n\n### 3. C4 control table — C4 row PIQA\n\nPaper=74.86, registry (`c4_kl30_s42_eval`)=75.03. Off by **0.17pp**.\n\n### 4. Extended downstream table (tab:downstream) — TEAL 30% uniform PIQA\n\nPaper=72.80, registry (`teal_30pct_uniform_multiseed_eval`)=71.98. Off by **0.82pp**. Registry stores `piqa` (likely raw acc) rather than `piqa_acc_norm`; possible metric variant confusion.\n\n### 5. Experiments prose — \"148× vs. 112× compression\" for Qwen14B\n\nPaper claims Qwen-2.5-14B has d_ff/d_b = 148× (implying d_ff=18,944). Registry shows `trainable_params='117M (0.793%)'` for `qwen14b_kl30_s123`. Back-computing:\n\n- 117M / 48 layers = 2.44M per layer\n- 2.44M = (5120×128) + (128×d_ff) → d_ff ≈ 13,923\n- 13,923 / 128 ≈ **109×**, not 148×\n- LLaMA's 112× (14336/128) is correct\n\nThe 148× claim is inconsistent with the registered trainable parameter count.\n\n---\n\n## Data Provenance Issues (⚠️ — unverifiable from registry)\n\n### Table 2\n\n| Row | Missing | Notes |\n|-----|---------|-------|\n| BCE 30% global | All 5 metrics | `bce30_teal_global` absent from registry entirely |\n| TEAL 30% uniform ARC-c | acc_norm variant | Registry stores `arc_challenge`=37.71 (acc), not acc_norm; paper=39.33 plausible but unverified |\n| TEAL 50% uniform | ARC-c, WG, MMLU | No full downstream eval registered for TEAL 50% uniform |\n\n### Ablation Table (Table 4)\n\n| Row | Missing | Notes |\n|-----|---------|-------|\n| JSD 50% | PPL 12.54 | `jsd_ablation_s42` absent from registry |\n| Reverse KL 50% | PPL 12.80 | `reverse_kl_ablation_s42` absent |\n| Per-layer KL K=1 50% | PPL 34.85 | `perlayer_kl_50_s42` absent |\n| Per-layer KL K=4 30%/50% | Both PPL values | Experiments registered but metrics empty |\n| BCE + STE 50% | PPL 60.54 | `bce_ste_s42` absent |\n\nAll Δ_50 arithmetic is internally consistent (computed correctly from the stated 50% values).\n\n### Qwen-2.5-14B Table\n\n| Row | Missing | Notes |\n|-----|---------|-------|\n| BCE global | ARC-c, WG, MMLU, GSM8K | `qwen14b_bce30_s42_eval` absent |\n| TEAL uniform | PPL, ARC-c, WG, MMLU | No 4-task eval registered for TEAL 30% uniform |\n| KL uniform GSM8K | s123 value | Only s42 (35.71%) and s456 (26.08%) in registry; 2-seed mean=30.9±6.8, paper claims 32.0±5.2 (implies unregistered s123≈34.2%) |\n\n### K-curve Table\n\n| Row | Missing | Notes |\n|-----|---------|-------|\n| K=4 | PPL (s123, s456), all downstream (s123, s456) | Only s42 downstream in registry |\n\n### Other\n\n- **Constraint experiments** (`constraint_protect_late`, `constraint_remove_valley`): Not in registry. Paper claims MMLU +3.4pp, GSM8K +1.6pp from removing valley — unverifiable.\n- **Extended downstream** — KL 30% uniform HS/PIQA: Only s42 registered; 3-seed mean (71.07±0.54 / 74.95±0.25) unverifiable.\n- **Extended downstream** — TEAL 50% uniform HS/PIQA: `bench_teal50_uniform_6task` absent.\n\n---\n\n## Minor Rounding Discrepancies (~)\n\nAll means match; only std values differ by 0.01-0.1 due to rounding of pre-rounded inputs.\n\n| Location | Metric | Paper | Computed | Exact |\n|----------|--------|-------|----------|-------|\n| Table 2 MSE 30% | PPL std | 1.68 | 1.67 | 1.666 |\n| Table 2 MSE 30% | ARC-c std | 4.1 | 4.0 | 4.03 |\n| Table 2 MSE 30% | WG std | 2.6 | 2.5 | 2.54 |\n| Table 2 KL 50% uniform | PPL std | 0.07 | 0.08 | 0.076 |\n| K-curve K=8 | ARC-c std | 1.0 | 1.1 | 1.06 |\n| K-curve K=16 | MMLU std | 2.9 | 2.8 | 2.77 |\n| Mistral KL30 downstream | WG std | 1.2 | 1.1 | 1.14 |\n| Table 3 footnote | C1 s42 PPL gap | 0.65pp | 0.63pp | 0.6306 |\n\n---\n\n## Verified Tables (all data points match ✅)\n\n### Table 3 — C1 Target-Swap Ablation\n40/40 data points match exactly. All seeds (s42/s123/s456) at 30% and 50% verified.\n\n### Cross-Architecture Table (tab:cross_arch)\nAll 12 PPL values (6 KL + 6 TEAL across Mistral and LLaMA at 30/50/70%) match exactly.\n\n### Mistral Downstream Table (tab:mistral_downstream)\nAll 21 values match (dense + KL 3-seed + TEAL single-seed across 7 metrics).\n\n### Latency Table (tab:latency)\nAll 10 data points match exactly (ms/fwd and tok/s for 5 configurations).\n\n### OOD Table (tab:ood)\nAll 4 C4 PPL values match. OOD uniform 3-seed (18.22/16.37/16.36, mean 16.98±1.07) match.\n\n### OOD Downstream Table (tab:ood_downstream)\nAll 12 values match (WikiText and C4 calibration across 6 metrics).\n\n### Dense Baseline\nAll 5 metrics match exactly (PPL 6.12, ARC-c 58.28, WG 78.06, MMLU 65.27, GSM8K 48.75).\n\n### Appendix Tables\n- Bottleneck sensitivity (tab:db_sensitivity): all values match\n- Temperature schedule (tab:tau_sensitivity): all values match\n- Training convergence (tab:training_convergence): all values match\n- Lagrangian dynamics (tab:lagrangian): all values match\n\n---\n\n## Verified Inline Prose Claims\n\n| Claim | Verification | Status |\n|-------|-------------|--------|\n| \"14.5% reduction\" (8.81 vs 10.30) | (10.30−8.81)/10.30=14.47%→14.5% | ✅ |\n| \"MMLU −5.2pp on 8B\" | 45.86−40.7=5.16≈5.2 | ✅ |\n| \"GSM8K −20.1pp on 14B\" | 52.1−32.0=20.1 (if 3-seed=32.0) | ✅ (but 32.0 unverified, see above) |\n| \"7.3× MMLU σ\" | 9.5/1.3=7.31 | ✅ |\n| \"−17.3% Mistral PPL\" | (8.38−6.93)/8.38=17.3% | ✅ |\n| \"MMLU −2.8pp on 14B\" | 66.34−63.55=2.79≈2.8 | ✅ (but TEAL MMLU 66.34 unregistered) |\n| \"6.4% latency overhead\" | (126.78−119.11)/119.11=6.44% | ✅ |\n| \"2.39× worse than KL\" | 28.13/11.79=2.386 | ✅ |\n| \"F1 0.613 vs 0.540\" | registry kl_bce_f1_oracle: 0.6128/0.5397 | ✅ |\n| \"139% worse PPL\" | (28.13−11.79)/11.79=138.7%≈139% | ✅ |\n| \"33.8% STE improvement\" | (15.77−11.79)/11.79=33.8% | ✅ |\n| \"JSD +6.4%, RevKL +8.6%\" | (12.54−11.79)/11.79=6.4%, (12.80−11.79)/11.79=8.6% | ✅ |\n| \"K=16 PPL 8.67±0.02\" | registry 3-seed: 8.67±0.02 | ✅ |\n| \"coupling range 2.08 PPL\" | 10.75−8.67=2.08 | ✅ |\n| \"signal type gap 9.47 PPL\" | 18.52−9.05=9.47 | ✅ |\n| \"Jaccard 68% at 50%\" | c1_mask_overlap mean=0.6824 | ✅ |\n| \"cross-seed Jaccard 36.3%\" | appendix consistent | ✅ |\n| \"75.9M params, <1%\" | 32×2.37M=75.84M≈75.9M | ✅ |\n| \"50% PPL reduction at 50% sparsity\" | (23.90−11.92)/23.90=50.1% | ✅ |\n\n---\n\n## Recommendations\n\n### Must-fix before submission\n\n1. **KL 50% global row (Table 2):** Reconcile PPL and downstream metrics with a single consistent set of 3-seed eval runs. Document which exp_ids provide PPL vs downstream for each seed.\n\n2. **C4 control table HS/PIQA (WikiText row):** Values 69.4/75.5 are inconsistent with the OOD downstream table (70.9/74.8) and with registry (70.85/74.81). Use values from registered experiment.\n\n3. **C4 control table PIQA (C4 row):** Paper says 74.86, registry says 75.03. Verify and correct.\n\n4. **148× compression claim:** Back-computation from registered 117M params implies d_ff≈13,923 (109×), not 18,944 (148×). Verify Qwen-2.5-14B's actual intermediate_size and correct.\n\n### Should-fix\n\n5. **Qwen14B GSM8K (32.0±5.2):** Register the s123 GSM8K evaluation to make this claim verifiable. Current 2-seed data gives 30.9±6.8.\n\n6. **Extended downstream TEAL 30% uniform PIQA:** Verify whether paper uses acc_norm (72.80) while registry stored acc (71.98).\n\n7. **BCE 30% global row (Table 2):** Register the source experiment or add exp_id comment.\n\n### Nice-to-have\n\n8. Register missing ablation experiments (JSD 50%, RevKL 50%, perlayer KL 50%, BCE+STE 50%, K=4 metrics).\n9. Standardize registry metric key names (e.g. `arc_challenge` vs `arc_challenge_acc_norm`).\n10. Minor std rounding: adopt consistent rounding convention (round exact, not round pre-rounded).\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "c31fcc3d-068f-422d-9849-823e7168dd7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 98 · 2026-05-24T01:42:30.317Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01QgXXDtGG3xBGGRRG1KW9tc`</summary>

```json
{
  "name": "R28 Data Consistency Report",
  "type": "report",
  "description": "Registry ↔ paper full cross-verification: 284 data points checked, 5 critical mismatches, 31 unverifiable entries, 8 minor rounding issues",
  "project": "distill_sparse_swiglu",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/r28_data_consistency_report.md",
  "tags": [
    "r28",
    "data-audit",
    "pre-submission"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8453a6d-4b89-44a5-8955-4660a0208c88",
  "isSidechain": false,
  "requestId": "req_011CbLYY5sEUudufR2p4BFzL",
  "type": "assistant",
  "uuid": "f3420242-a911-44f4-8c1e-89855b7815ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Qopa3r2kLEozNpipPULkj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4162,
      "cache_read_input_tokens": 121465,
      "output_tokens": 257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4162,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 257,
          "cache_read_input_tokens": 121465,
          "cache_creation_input_tokens": 4162,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4162
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

_source line 99 · 2026-05-24T01:42:30.484Z_

<details><summary>↩ Tool result · `toolu_01QgXXDtGG3xBGGRRG1KW9tc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260524_63b011\", \"name\": \"R28 Data Consistency Report\", \"type\": \"report\", \"description\": \"Registry ↔ paper full cross-verification: 284 data points checked, 5 critical mismatches, 31 unverifiable entries, 8 minor rounding issues\", \"path\": \"projects/distill_sparse_swiglu/artifacts/_project/report/r28_data_consistency_report.md\", \"url\": null, \"project\": \"distill_sparse_swiglu\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-24T01:42:30.322734+00:00\", \"tags\": [\"r28\", \"data-audit\", \"pre-submission\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3420242-a911-44f4-8c1e-89855b7815ff",
  "isSidechain": false,
  "promptId": "de60ee45-84fe-40c7-ad5a-52baa3f09b49",
  "type": "user",
  "uuid": "601978e6-40b3-48ac-a3dc-a2d26ec17f32",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260524_63b011\\\", \\\"name\\\": \\\"R28 Data Consistency Report\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Registry ↔ paper full cross-verification: 284 data points checked, 5 critical mismatches, 31 unverifiable entries, 8 minor rounding issues\\\", \\\"path\\\": \\\"projects/distill_sparse_swiglu/artifacts/_project/report/r28_data_consistency_report.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"distill_sparse_swiglu\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-24T01:42:30.322734+00:00\\\", \\\"tags\\\": [\\\"r28\\\", \\\"data-audit\\\", \\\"pre-submission\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260524_63b011\", \"name\": \"R28 Data Consistency Report\", \"type\": \"report\", \"description\": \"Registry ↔ paper full cross-verification: 284 data points checked, 5 critical mismatches, 31 unverifiable entries, 8 minor rounding issues\", \"path\": \"projects/distill_sparse_swiglu/artifacts/_project/report/r28_data_consistency_report.md\", \"url\": null, \"project\": \"distill_sparse_swiglu\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-24T01:42:30.322734+00:00\", \"tags\": [\"r28\", \"data-audit\", \"pre-submission\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "f3420242-a911-44f4-8c1e-89855b7815ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Assistant

_source line 100 · 2026-05-24T01:42:43.717Z_

审查完成。报告已写入 `artifacts/r28_data_consistency_report.md`。

**关键发现：**

**5 个 must-fix：**

1. **Table 2 KL 50% global 行** — PPL 11.84±0.15 及 ARC-c/WG/GSM8K 无法从任何 registry 实验组合复现。PPL 的 std 最接近的组合只给出 ±0.07，downstream 值也有 1-2pp 偏差。根因：不同 seed 的 PPL 和 downstream 来自不同 eval run，混用了实验源。

2. **C4 control 表 WikiText 行 HS/PIQA** — 69.4/75.5 与同篇论文 OOD downstream 表的 70.9/74.8 矛盾（同一个 predictor），registry 支持后者。

3. **C4 control 表 C4 行 PIQA** — 论文 74.86 vs registry 75.03，差 0.17pp。

4. **Extended downstream 表 TEAL 30% uniform PIQA** — 论文 72.80 vs registry 71.98，差 0.82pp（疑似 acc vs acc_norm 混用）。

5. **"148× compression" for Qwen14B** — 从 registry 的 117M 参数量反算，d_ff≈13923（109×），不是 18944（148×）。

**大部分数据一致：** Table 3（C1 ablation）40/40 全匹配，cross-arch 表全匹配，latency 表全匹配，所有 inline 计算（14.5% reduction、7.3× σ 等）全部正确。约 83% 的数据点完全通过验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "601978e6-40b3-48ac-a3dc-a2d26ec17f32",
  "isSidechain": false,
  "requestId": "req_011CbLYYUVWfVC5wcC1adPrj",
  "type": "assistant",
  "uuid": "e01ed942-a371-453a-a3a0-79faa97d58dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018kcTh77QvQS1KY3MiTFiUE",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 551,
      "cache_read_input_tokens": 125627,
      "output_tokens": 499,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 551,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 499,
          "cache_read_input_tokens": 125627,
          "cache_creation_input_tokens": 551,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 551
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

_source line 101_

```json
{
  "type": "last-prompt",
  "leafUuid": "e01ed942-a371-453a-a3a0-79faa97d58dc",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01"
}
```

---


### Runtime record

_source line 102_

```json
{
  "type": "ai-title",
  "aiTitle": "Final data consistency audit registry vs paper",
  "sessionId": "25c2b46c-d801-46c2-86f6-e0788aa27b01"
}
```

---
