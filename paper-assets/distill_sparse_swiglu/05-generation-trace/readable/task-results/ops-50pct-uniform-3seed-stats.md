# ops 50pct uniform 3seed stats

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_50pct-uniform-3seed-stats_20260518T115504_result.json`
- **Structured JSON:** [`9ea4ef6dc8b185c64ac8.json`](../../sessions/9e/9ea4ef6dc8b185c64ac8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

CSV 已保存。

注意：uniform 使用了 `bench_` 系列全部三个 seed（一致的评估协议）。你任务中给的 s42/s456 数值来自 `kl50_s*_uniform_eval`，与 `bench_` 系列略有差异（如 s42 arc: 0.3259 vs 0.3276）。我选择了 `bench_` 系列以保证三个 seed 的评估协议一致。

Global s123/s456 没有 `bench_` 前缀的条目，用了 `kl50_global_s123_reeval` 和 `kl50_s456_global_eval`。

**论文可粘贴格式：**

```
50% uniform: PPL 11.92±0.08, ARC 33.8±1.2, WG 62.9±0.1, MMLU 28.0±0.6, GSM8K 2.2±0.1
50%  global: PPL 11.77±0.05, ARC 34.1±1.9, WG 63.1±1.9, MMLU 28.1±0.2, GSM8K 2.0±0.7
```

核心观察：50% 下 uniform 和 global 差异不显著，两种分配都出现 downstream 严重退化（MMLU ~28%, GSM8K ~2%）。

---
