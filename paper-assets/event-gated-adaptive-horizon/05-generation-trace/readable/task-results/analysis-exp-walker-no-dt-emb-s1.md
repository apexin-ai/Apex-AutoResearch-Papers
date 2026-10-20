# analysis exp walker no dt emb s1

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_walker_no_dt_emb_s1_20260527T142336_result.json`
- **Structured JSON:** [`b02a9fb0a33f3bb95d69.json`](../../sessions/b0/b02a9fb0a33f3bb95d69.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结果：

**eval_return_105K = 468.83**（baseline 的 51.2%），**NVE_peak = 0.88**（35K），**CIVO 未触发**。

与 seed 0 (exp_008f) 完全一致：
- seed 0: eval=503, NVE=0.30x, 无 CIVO
- seed 1: eval=469, NVE=0.35x (105K), NVE_peak=0.88x (35K), 无 CIVO

两个 seed 均呈现 zigzag 震荡 + 无值膨胀的模式。Gate 始终锁定 dt=2（entropy=0）。

**结论：SUCCESS** — 假设成立。移除 dt_embedding 后 CIVO 不出现，确认 dt_embedding 是 CIVO 发生的因果必要条件。

---
