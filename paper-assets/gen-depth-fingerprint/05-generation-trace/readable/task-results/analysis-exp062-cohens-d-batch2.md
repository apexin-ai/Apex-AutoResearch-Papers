# analysis exp062 cohens d batch2

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp062-cohens-d-batch2_20260521T195702_result.json`
- **Structured JSON:** [`fc02c652afdda0bce56c.json`](../../sessions/fc/fc02c652afdda0bce56c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

**Qwen3-8B greedy** (gen1=982, gen2+=2722):

| Feature | Cohen's d |
|---|---|
| entropy_mean | 0.98 |
| entropy_std | 0.71 |
| entropy_min | 0.06 |
| entropy_max | 0.01 |
| tail_decay | 0.08 |
| ttr | 0.76 |
| hapax_ratio | 0.76 |

Shape: YES, Drift: YES → **DDR: YES**

**Qwen3-0.6B top-k** (gen1=991, gen2+=2569):

| Feature | Cohen's d |
|---|---|
| entropy_mean | 0.80 |
| entropy_std | 0.30 |
| entropy_min | 0.10 |
| entropy_max | 0.02 |
| tail_decay | 0.13 |
| ttr | 0.58 |
| hapax_ratio | 0.52 |

Shape: YES, Drift: YES → **DDR: YES**

Qwen3-0.6B 在 greedy 下 hapax=0.46 未过 Drift 阈值，但 top-k 下反而 hapax=0.52 通过了——stochastic sampling 反而增强了 drift signal。

进度：**15/16**，剩余 Qwen3-8B top-k。两份 appendix tex 和两份 summary txt 已同步更新，Mean 行已重算（Greedy 8/8, Top-k 7/8）。

---
