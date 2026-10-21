# analysis exp062 extract qwen17b topk

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp062_extract_qwen17b_topk_20260521T153508_result.json`
- **Structured JSON:** [`36424d80a2e614219a54.json`](../../sessions/36/36424d80a2e614219a54.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已更新完成。

**Qwen3-1.7B top-k 结果**（gen1=988, gen2+=2640）：

| Feature | Cohen's d |
|---------|-----------|
| entropy_mean | 0.985 |
| entropy_std | 0.316 |
| entropy_max | 0.031 |
| entropy_min | 0.029 |
| tail_decay | 0.139 |
| TTR | 0.845 |
| hapax_ratio | 0.795 |

**Shape=YES, Drift=YES** — 这是目前 4 个 top-k 模型中唯一同时通过两项的。Qwen3-1.7B 在 top-k 采样下仍保留了完整的 depth fingerprint 信号，d_mean=0.99 接近其 greedy 的 1.03，衰减极小。

进度更新至 10/16 combos（greedy ×6, top-k ×4）。

---
