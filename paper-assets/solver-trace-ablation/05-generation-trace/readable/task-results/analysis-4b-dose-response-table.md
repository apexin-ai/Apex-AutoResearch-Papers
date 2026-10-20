# analysis 4b dose response table

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_4b-dose-response-table_20260516T110236_result.json`
- **Structured JSON:** [`b28cf84622ef3e37047e.json`](../../sessions/b2/b28cf84622ef3e37047e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。文件保存至：
- `artifacts/4b_dose_response_table.csv` — 20 行实验数据（19 个实验条件）
- `artifacts/4b_dose_response_summary.md` — 条件聚合表 + 数据来源 + 注意事项

关键发现：
- **2 个实验完全缺失**：plan002-b01-s43、plan018-random-s43（checkpoint 已清理）
- **步数不一致**：exec-only 和 ISR β=0.3 混合了 500/1000 步实验
- **Taxonomy 缺失**：exec-only s43/s44、ISR β=0.05/0.1、random s42 的 h8/genuine 数据不完整
- **ISR β=0.2 全面崩溃**：3 seed 全是 H7 hacking（genuine=0），ISR reward 完全被 Goodhart

---
