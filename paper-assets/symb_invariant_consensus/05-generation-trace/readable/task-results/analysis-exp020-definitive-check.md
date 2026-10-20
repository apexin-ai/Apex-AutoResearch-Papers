# analysis exp020 definitive check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp020-definitive-check_20260517T095239_result.json`
- **Structured JSON:** [`42988c7efb5ebc197314.json`](../../sessions/42/42988c7efb5ebc197314.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-020-llama8b-folio-204 当前状态

**进度: 68/204 (33.3%) — 仍在运行，预计剩余 ~82 分钟**

| 指标 | 值 |
|---|---|
| **SICA accuracy** | 67.65% (46/68) |
| **SC accuracy** | 70.59% (48/68) |
| **Delta** | **-2.94pp** (SC 领先) |

### 统计检验 (基于当前 n=68)

| 检验 | 结果 |
|---|---|
| McNemar p-value | 0.5000 |
| SICA wins / SC wins | 0 / 2 |
| Both correct | 46 |
| Both wrong | 20 |
| Bootstrap 95% CI | [-7.35, 0.00] |
| Bootstrap P(d<=0) | 1.0000 |
| **显著 (p<0.05)** | **NO** |
| **CI excludes zero** | **NO** |

### 按 Ground Truth 类别

| GT | n | SICA | SC | Delta |
|---|---|---|---|---|
| False | 17 | 47.1% | 47.1% | +0.0pp |
| True | 24 | 75.0% | 79.2% | -4.2pp |
| Unknown | 27 | 74.1% | 77.8% | -3.7pp |

### 运行环境
- GPU: 100% 利用率, 88309/97887 MiB
- 平均每题 36.1s, 已耗时 40.9 min
- tmux session `exp-020-llama8b-folio-204` 活跃

### 中期判断

当前 68 题的部分结果中，SICA 落后 SC 2.94pp，仅 2 个 discordant pair 且全部是 SC 赢。需要等完整 204 题才能下结论，但目前趋势对 SICA 不利。

---
