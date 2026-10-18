# code reference free baseline

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_reference_free_baseline_20260517T045516_result.json`
- **Structured JSON:** [`50513e7db17ca72ad15f.json`](../../sessions/50/50513e7db17ca72ad15f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成，结果已注册。

## 结果摘要

| 指标 | Reference-Free (7 feat) | Full (19 feat) |
|------|------------------------|----------------|
| 4-class Acc | **53.68%** [53.36, 54.01] | 78.77% |
| Delta | **-25.09 pp** | — |
| d1v2 AUC | 0.625 | — |

**Per-class recall:** d0=85.7%, d1=39.7%, d2=31.8%, d3=57.6%

**结论: NEGATIVE.** 53.68% 虽然 >2× chance (25%)，但未达到 60% 假设阈值。PPL/surprisal 特征贡献约 25pp accuracy。Token-level 统计能区分 depth 0（人类原文 vs 机器生成），但 d1/d2 中间深度的区分严重依赖 reference model 特征。

---
