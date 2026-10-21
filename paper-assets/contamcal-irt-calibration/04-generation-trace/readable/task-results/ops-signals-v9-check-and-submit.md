# ops signals v9 check and submit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_signals-v9-check-and-submit_20260516T060517_result.json`
- **Structured JSON:** [`8c61bc605725e90aa4cb.json`](../../sessions/8c/8c61bc605725e90aa4cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 总结

### Part 1：v9 完整性 ✓

| 文件 | 状态 |
|------|------|
| signal_s4_selfcritique_mmlu.json | 完成 (3.3MB, 140421行, 14042 items) |
| _s4_chunks_mmlu/ (15 chunks) | 完整 |
| signal_s1_embedding_mmlu.json | 已有 |
| signal_s2_minkpp_mmlu.json | 已有 |

Registry 已更新为 `success`。

### Part 2：cuda:4 无法提交

**cuda:4 仍被占用**：PID 712011 正在跑 `compute_signals.py --benchmark gsm8k --signal all` (d100_a32_s123)，占 7824 MiB。这是 v9 session 的延续——mmlu s4 完成后自动开始了 gsm8k 全信号计算。

**不提交 eval 任务**，遵守 C001/C005 约束。等 gsm8k signals 跑完 cuda:4 释放后再提交 `exp_001_eval_3B_d005_s42_para_aligned`。

---
