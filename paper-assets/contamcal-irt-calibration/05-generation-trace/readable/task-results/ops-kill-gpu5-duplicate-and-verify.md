# ops kill gpu5 duplicate and verify

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-gpu5-duplicate-and-verify_20260515T061020_result.json`
- **Structured JSON:** [`7087450f1fbd099e15a2.json`](../../sessions/70/7087450f1fbd099e15a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件完整性对比结果清晰。汇总：

### 结果报告

**Kill 状态**: PID 508118 和 508351 已自行死亡，无需手动 kill。

**GPU 5 当前状态**: 有一个新进程 PID 507968（孤儿，ppid=1，运行 40 分钟），同样是 `compute_signals.py` 写同一 output-dir。

**文件完整性对比** (exp008 vs exp002 参考值):

| 文件 | exp008 行数 | exp002 参考行数 | exp008 大小 | exp002 参考大小 | 状态 |
|------|------------|----------------|------------|----------------|------|
| signal_embedding_mmlu.json | 252,757 | 252,757 | 6.08 MB | 6.09 MB | **完整** |
| signal_minkpp_mmlu.json | 98,295 | 98,295 | 2.12 MB | 2.12 MB | **完整** |
| signal_selfcritique_mmlu.json | 112,337 | 112,337 | 2.95 MB | 2.93 MB | **完整** |
| signals_merged_mmlu.json | 112,337 | 112,337 | 2.76 MB | 2.76 MB | **完整** |

行数与参考值完全一致，文件大小高度接近（微小差异来自模型不同）。**数据未腐败，不需要删除。**

**待决**: PID 507968 仍在 GPU 5 上运行，写同一 output-dir。既然 3 个 signal 文件和 merged 文件都已完整生成，这个进程可能在做冗余计算。是否要 kill 507968？

---
