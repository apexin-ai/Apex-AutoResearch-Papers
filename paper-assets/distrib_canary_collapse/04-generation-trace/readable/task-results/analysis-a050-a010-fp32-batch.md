# analysis a050 a010 fp32 batch

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_a050_a010_fp32_batch_20260519T095037_result.json`
- **Structured JSON:** [`dbb04a1952d57053ee1c.json`](../../sessions/db/dbb04a1952d57053ee1c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。报告写入 `artifacts/analysis_a050_a010_fp32_batch.md`。

核心结论：

**α=0.50 明确处于"可检测"区间**：PermG=6/8（s43, s44 完全一致），k4=6/8，MMCT=0.75。3-seed drift 高度一致（d1_drift: -28.70±0.55%）。

**α=0.10 s42 确认盲区**：PermG=0/8，与已有 α=0.05 和 α=0.10 s43 一致。

**Step function 跃迁在 [0.10, 0.50] 区间内**，需要 α=0.25 或 α=0.30 数据定位精确阈值。

**待处理**：
1. a050_s42 缺少 analysis_results.json（lead-lag 分析未运行），需补跑
2. α=0.50 PermG(6/8) 高于 α=0.60(3/8)，后者是单 seed，建议多 seed 验证

---
