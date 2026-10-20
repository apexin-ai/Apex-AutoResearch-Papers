# analysis eval flat nli seed45

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_flat_nli_seed45_20260516T030542_result.json`
- **Structured JSON:** [`47d9ce11a54177b49771.json`](../../sessions/47/47d9ce11a54177b49771.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。

## eval_flat_nli_seed45 结果摘要

### 核心指标

| Metric | s42 | s44 | **s45** | Mean ± Std |
|--------|-----|-----|---------|------------|
| rel_f1 | 0.4539 | 0.4615 | **0.4551** | **0.4568 ± 0.0033** |
| evi_f1 | 0.8043 | 0.8131 | **0.8154** | **0.8109 ± 0.0047** |
| edcr | 0.6431 | 0.6458 | **0.6521** | **0.6470 ± 0.0038** |

### 完整指标 (s45)

| Metric | Value |
|--------|-------|
| rel_p / rel_r / rel_f1 | 0.4632 / 0.4472 / 0.4551 |
| ign_f1 | 0.4551 |
| evi_p / evi_r / evi_f1 | 0.8108 / 0.8201 / 0.8154 |
| evi_f1_joint | 0.3556 |
| edcr | 0.6521 |
| predictions / tp | 15650 / 5434 |
| format_ok | 985/985 (100%) |
| truncated | 206/985 (20.9%) |
| inference time | 11867.6s (~3.3h) |

### 对比分析

- **rel_f1**: s45 (0.4551) 比 s42 高 +0.0012，比 s44 低 -0.0064，处于中间水平
- **evi_f1**: s45 (0.8154) 是三个 seed 中最高的
- **edcr**: s45 (0.6521) 也是三个 seed 最高
- **vs CED RSFT mean (~0.4596)**: flat-NLI 三 seed 均值 0.4568 略低 -0.0028，差距很小
- 三个 seed 方差极小（rel_f1 std=0.0033），训练稳定性良好
- 无 format error，truncation 比例 20.9% 属正常范围

---
