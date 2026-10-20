# research check 008d 45k

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_check_008d_45k_20260514T044622_result.json`
- **Structured JSON:** [`f103578024050c4eaf97.json`](../../sessions/f1/f103578024050c4eaf97.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据拿到了。55000 只有一个空 step 标记，eval 还没产出。

## exp_008d@45K 指标

| 指标 | @35K | @45K | 变化 |
|------|------|------|------|
| eval_return | 146.3 | **140.8** | -5.5 (-3.8%) |
| value_mean | 60.3* | **97.5** | +37.2 |
| v/e ratio | 41.2% | **69.3%** | +28.1pp |

*（@35K value_mean 由 146.3×0.412 ≈ 60.3 反推）

### 关键发现

- **eval_return 小幅下降**：140.8 vs 146.3，回落约 3.8%，基本持平。
- **v/e ratio = 69.3%，已超过 50%**：value_mean (97.5) / eval_return (140.8) = 0.693。相比 @35K 的 41.2% 大幅上升。
- **gate 完全锁死在 dt=2**：gate_dt_2_frac=1.0，gate_empirical_entropy=0.0，gate 没有自适应行为。
- **55K eval 尚未产出**，只有 step 标记行。

---
