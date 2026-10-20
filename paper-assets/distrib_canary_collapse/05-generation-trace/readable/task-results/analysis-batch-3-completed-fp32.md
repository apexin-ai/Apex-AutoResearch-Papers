# analysis batch 3 completed fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_batch_3_completed_fp32_20260519T051730_result.json`
- **Structured JSON:** [`3fe99d04bbdb5336e15b.json`](../../sessions/3f/3fe99d04bbdb5336e15b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入并注册。核心结论：

- **α=0.05**: 近 null baseline，MMCT=0.0，consensus_k4=0/8，canary drift 太弱无法检测
- **α=0.60**: 强 collapse 信号，MMCT=0.875，consensus_k4=7/8，5 个 pair 达到 5-method 全票
- **Intervention α=0.75**: gen1 触发，1 代完全恢复，MMCT=0.75，consensus_k4=6/8；threshold_onset=0/8 是干预成功的标志而非方法缺陷

α=0.05 的 TY 3/8 显著结果均为 d_max=2/df_resid=1，按 C003 约束不可引用。

---
