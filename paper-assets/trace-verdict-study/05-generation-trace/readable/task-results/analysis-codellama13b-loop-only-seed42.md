# analysis codellama13b loop only seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_codellama13b_loop_only_seed42_20260519T185221_result.json`
- **Structured JSON:** [`cc3224036d42b4338683.json`](../../sessions/cc/cc3224036d42b4338683.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## CodeLlama-13B loop_only_seed42 结果

### 核心指标

| Metric | Value | 95% CI |
|--------|-------|--------|
| **Accuracy** | **77.06%** | [74.87%, 79.41%] |
| Majority baseline | 71.51% | — |
| Lift over majority | +5.55pp | [+2.1pp, +9.2pp] |

| Class | Precision | Recall | F1 |
|-------|-----------|--------|----|
| pass | 0.92 | 0.75 | 0.82 |
| fail | 0.57 | 0.83 | 0.67 |

### 对比

| Comparison | Accuracy | Delta |
|------------|----------|-------|
| CodeLlama-13B **ae_only** | 99.08% | **-22.02pp** |
| CodeLlama-13B **loop_only** (this) | 77.06% | — |
| Qwen-7B **loop_only** | 85.63% | **-8.57pp** |
| Qwen-7B **ae_only** | 99.92% | -22.86pp |

### Hypothesis 验证

**ae_only > loop_only 跨模型成立。** CodeLlama-13B 上 ae_only (99.08%) vs loop_only (77.06%) 差距 22pp，远超预期的 ≥10pp。Tier hierarchy 在第二个模型上得到确认。

额外发现：CodeLlama-13B loop_only (77.06%) 显著低于 Qwen-7B loop_only (85.63%)，说明 CodeLlama-13B 在 loop-only traces 上的学习能力弱于 Qwen-7B。而在 ae_only 条件下两模型表现接近（99.08% vs 99.92%），差距主要体现在困难条件上。

### 训练状态

- **正常完成**，EXIT_CODE=0
- 444 steps, 3 epochs, 训练时长 ~3h45m
- Final train loss: 0.023, eval loss epoch 2: 0.131 → epoch 3: 0.145（轻微过拟合）
- Checkpoint: `/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_loop_only_seed42/final/`
- Log: `/root/runs/trace-verdict-study/codellama13b_loop_only_seed42.log`

---
