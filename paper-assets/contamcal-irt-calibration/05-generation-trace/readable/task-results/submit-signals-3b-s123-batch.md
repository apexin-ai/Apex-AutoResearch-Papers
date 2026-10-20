# submit signals 3B s123 batch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_signals_3B_s123_batch_20260516T143206_result.json`
- **Structured JSON:** [`f8a9c3c40f82c39fa78a.json`](../../sessions/f8/f8a9c3c40f82c39fa78a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:0 上已经在跑目标任务**：PID 780943 正是 d000_s123_a32 的 `signal_s4_selfcritique_mmlu` 计算——这正是唯一缺失的文件。

## 汇总

| 实验 | 状态 | 详情 |
|------|------|------|
| **d000_s123** (cuda:0) | ⏳ 运行中 | PID 780943 正在计算最后缺失的 `s4_selfcritique_mmlu`，其余 8/9 信号已完成 |
| **d100_s123** (cuda:2) | ❌ C006 封禁 / ✅ 已完成 | `Qwen2.5-3B_d100_s123` alpha=16 被 C006 封禁；正确的 `d100_a32_s123` (alpha=32) 12/12 文件已完成 |
| **d025_s123** (cuda:3) | ✅ 已完成 | `Qwen2.5-3B_d025_s123` (alpha=32) 12/12 文件已完成 |

**无需提交任何新任务。** 三个实验要么已完成，要么正在运行中。

---
