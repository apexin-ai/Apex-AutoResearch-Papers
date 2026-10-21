# analysis matched tax data compilation

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_matched-tax-data-compilation_20260521T033625_result.json`
- **Structured JSON:** [`e2817dfbba2153b90d66.json`](../../sessions/e2/e2817dfbba2153b90d66.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总完成。关键发现：

**已齐备的 matched@2048 数据：**
- SFT s42: with-evi=0.5649, no-evi=0.5210, **raw tax=-4.39pp**（evidence helps，幅度是 @1024 的 2.7 倍）

**4 个 with-evi@2048 eval 正在跑（4 GPU 全占）：**
- SFT s43 (GPU 2, 已跑 ~2.5h), s44 (GPU 3, 已跑 ~2.5h) — 预计再 1-2h
- RSFT s42 (GPU 0, 刚启动) — 预计 ~2-3h
- 14B RSFT (GPU 1, 刚启动) — 预计 ~2-3h

**可立即执行：** SFT s42 的 fair_evidence_tax.py，两侧 @2048 predictions 都已就绪。

**待后续提交（需等 GPU 空闲）：** RSFT s42 no-evi@2048, RSFT s43/s44 双侧@2048, 14B no-evi@2048 — 共 7 个 eval job。

**fair_evidence_tax.py** 对 max_new_tokens 透明，无需修改。

---
