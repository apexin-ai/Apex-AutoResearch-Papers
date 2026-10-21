# eval collect llama70 results

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_collect_llama70_results_20260517T021010_result.json`
- **Structured JSON:** [`743cb9190463f99f48c5.json`](../../sessions/74/743cb9190463f99f48c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇报

```
KL teal_global 70% PPL = 18.5432
TEAL vanilla 70% PPL  = 125.4204
```

### 与 registry 对比

| 方法 | 本次结果 | Registry 值 | 差异 |
|------|---------|-------------|------|
| KL teal_global | 18.54 | 17.91 | +0.63 (偏高) |
| TEAL vanilla | 125.42 | 100.11 | +25.31 (显著偏高) |

两个值均高于 registry 记录。KL predictor 差异较小（+3.5%），TEAL vanilla baseline 差异显著（+25.2%）。

### 额外 benchmark 指标

| Task | KL teal_global | TEAL vanilla |
|------|---------------|--------------|
| ARC-Challenge acc_norm | 0.2474 | 0.2295 |
| MMLU acc | 0.2670 | 0.2615 |

KL predictor 在所有指标上优于 TEAL vanilla baseline，但两者在 ARC/MMLU 上均接近随机水平（70% sparsity 对下游任务破坏严重）。

TEAL vanilla PPL 与 registry 差异大，可能原因：评估配置不同（seq_len、calibration_samples）或 registry 值来自不同 checkpoint/设置，需要排查。

---
