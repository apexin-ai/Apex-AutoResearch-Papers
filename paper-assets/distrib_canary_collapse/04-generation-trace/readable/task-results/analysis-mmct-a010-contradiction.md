# analysis mmct a010 contradiction

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mmct_a010_contradiction_20260519T052213_result.json`
- **Structured JSON:** [`b22585c9ed988372252a.json`](../../sessions/b2/b22585c9ed988372252a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。矛盾根因:

- **4/8**: 来自 a010_s43_fp32 分析报告，将简单共识计数 (consensus_k4) **误标为 "MMCT"**。4 个通过的 pair 全部依赖 TY Granger 作为第 4 票，C003 约束排除 TY 后降为 **0/8**。
- **1/8**: 来自正式 MMCT v2 (a010_s42)，使用置换检验 + null 分布校准。仅 ece->distinct_2 显著 (p=0.04)。

不存在真正矛盾，两个数字来自不同方法。dose-response 表应使用 1/8 (MMCT v2)，待 a010_s42_fp32 完成后用 fp32 数据重算。报告已写入 `artifacts/mmct_a010_contradiction_report.md`。

---
