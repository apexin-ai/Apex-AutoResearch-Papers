# ops read s456 eval results

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_read-s456-eval-results_20260519T124947_result.json`
- **Structured JSON:** [`d20c52e66dcd028c3949.json`](../../sessions/d2/d20c52e66dcd028c3949.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Qwen-14B KL 30% s456 eval_v2 完整结果

| 指标 | 值 |
|---|---|
| **WikiText-2 PPL** | **7.6933** |
| ARC-Challenge acc | 0.5051 |
| ARC-Challenge acc_norm | 0.5324 |
| WinoGrande acc | 0.7230 |
| HellaSwag acc | 0.5197 |
| HellaSwag acc_norm | 0.7113 |
| PIQA acc | 0.7421 |
| PIQA acc_norm | 0.7552 |
| MMLU acc | 0.6411 |

配置：sparsity_target=0.3, uniform allocation, bottleneck_size=128, seq_len=2048, batch_size=8。时间戳 2026-05-19 19:21:35。

## s123 eval 状态

- `s123_eval_v4` 目录已创建但为空（可能正在运行或刚启动）
- `s123_eval_v3` 也没有 results.json
- 尚无可用的 s123 最新完整结果

---
