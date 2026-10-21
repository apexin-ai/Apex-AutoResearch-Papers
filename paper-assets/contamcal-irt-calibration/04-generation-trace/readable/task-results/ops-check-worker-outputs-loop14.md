# ops check worker outputs loop14

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_worker_outputs_loop14_20260516T033618_result.json`
- **Structured JSON:** [`86875fbda32984d83b50.json`](../../sessions/86/86875fbda32984d83b50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 1. d100_s123_a32 eval — 已完成，已入 registry ✅

`exp_001_eval_3B_d100_s123_a32_batch`: DONE/success，metrics 已填充：

| Benchmark | Aligned | Para_aligned |
|-----------|---------|-------------|
| MMLU | 0.633 | 0.660 |
| GSM8K | 0.707 | 0.575 |
| ARC | 0.825 | 0.805 |
| HumanEval | 0.116 | 0.000 |

服务器文件均有 `.done` 标记确认。无需进一步操作。

### 2. v9 signals 死因

`exp_002_signals_3B_v9`: DONE/failed。  
**死因**：PID 668217 进程消失（reconcile 连续 miss 3/5 次后自动标 failed）。完成了 1/4 任务（d025_s123 mmlu s4），其余 3 个未完成。  
**根因追溯**：前任 v8 因 OOM 死（s4_selfcritique mmlu 内存密集），v9 用 chunked 方式重试但进程同样不稳定。

### 3. 需跟进

| 事项 | 状态 |
|------|------|
| PID 689315 (d100_a32_s123 mmlu s4) on cuda:4 | 活跃运行中（12min elapsed, 1/~14 chunks done）。已更新 `exp_002_signals_3B_d100_s123_v9` → RUNNING |
| d100_a32_s123 gsm8k + arc_challenge (all signals) | 待 mmlu s4 完成后提交 |
| d025_s123 signals_merged_mmlu.json | 所有单独信号文件已就绪，缺合并步骤（快速修复） |

---
