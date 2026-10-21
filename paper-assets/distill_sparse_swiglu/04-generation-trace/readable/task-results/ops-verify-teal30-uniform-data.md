# ops verify teal30 uniform data

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_teal30_uniform_data_20260520T010111_result.json`
- **Structured JSON:** [`b29a1736b82765b38d58.json`](../../sessions/b2/b29a1736b82765b38d58.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bench_teal30_uniform_6task 完整结果

**配置确认**: TEAL vanilla, sparsity=0.30, allocation=uniform, model=llama-3.1-8b, seq_len=2048, batch_size=8, 完成时间 2026-05-20 06:37:22, 耗时 2934.2s

### 逐 task 指标

| Task | Metric | 值 | Stderr |
|------|--------|-----|--------|
| **wikitext2** | word_perplexity | **10.8173** | — |
| **arc_challenge** | acc | **0.3771** | ±0.0142 |
| | acc_norm | **0.3933** | ±0.0143 |
| **winogrande** | acc | **0.6504** | ±0.0134 |
| | acc_norm | — (无此指标) | — |
| **mmlu** | acc | **0.4586** | ±0.0041 |
| | acc_norm | — (无此指标) | — |
| **hellaswag** | acc | **0.4617** | ±0.0050 |
| | acc_norm | **0.6331** | ±0.0048 |
| **piqa** | acc | **0.7198** | ±0.0105 |
| | acc_norm | **0.7280** | ±0.0104 |

### 高精度原始值（lm_eval_raw）

| Task.Metric | 精确值 |
|-------------|--------|
| arc_challenge.acc | 0.37713310580205 |
| arc_challenge.acc_norm | 0.39334470989761 |
| winogrande.acc | 0.65035516969219 |
| mmlu.acc | 0.45862412761715 |
| hellaswag.acc | 0.46166102370046 |
| hellaswag.acc_norm | 0.63314080860386 |
| piqa.acc | 0.71980413492927 |
| piqa.acc_norm | 0.72796517954298 |

### 同名实验文件清单

```
bench_teal30_uniform_6task/results.json     — 2026-05-20 07:26 (3066B) ← 本次
bench_teal30_uniform_gsm8k/results.json     — 2026-05-20 06:20 (1266B)
qwen14b_teal30_uniform_hspiqa/results.json  — 2026-05-19 22:20 (1781B)
qwen14b_teal30_uniform_hspiqa_v2/results.json — 2026-05-19 23:25 (1787B)
```

注意：winogrande 和 mmlu 只有 `acc`，无 `acc_norm`（lm-eval-harness 对这两个 task 默认不输出 acc_norm）。

---
