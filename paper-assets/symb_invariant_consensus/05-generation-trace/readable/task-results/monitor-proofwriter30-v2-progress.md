# monitor proofwriter30 v2 progress

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_proofwriter30_v2_progress_20260516T012153_result.json`
- **Structured JSON:** [`44fef98850823feb8817.json`](../../sessions/44/44fef98850823feb8817.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## proofwriter30_v2 进度报告

**状态**: 运行中 (PID 155077, elapsed 3h02m)

### 进度
- **16/30 完成**，当前在 #17
- 平均 668s/题，预估 **~2.6h 后完成**（约 11:50 UTC）
- 无 400 错误

### 准确率 (16题)

| 方法 | 正确 | 准确率 |
|------|------|--------|
| SICA | 14/16 | 87.5% |
| SC | 15/16 | **93.75%** |

SC 暂时领先 1 题。差异来自 #11：SICA 的不变量给了 True 更高分（38 vs 27），但 gold=False。

### Multi-candidate Rate: 3/16 = 18.75%
- 3 个多候选题中 2 个不变量得分全为 0（extraction 失败）
- 99 次 "No JSON found" 警告（~51.6% trace 未产生可解析 JSON）
- 3/16 题 unique_after_dedup=0（完全无不变量）

### 核心问题
QwQ-32B 的 invariant extraction 成功率偏低，SICA 在无不变量时退化为随机 tie-break，这是 SC 暂时领先的主因。

报告已写入 `artifacts/report_proofwriter30_v2_progress.md`。

---
