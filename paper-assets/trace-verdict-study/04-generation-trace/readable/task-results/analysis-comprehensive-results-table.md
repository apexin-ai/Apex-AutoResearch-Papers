# analysis comprehensive results table

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_comprehensive-results-table_20260516T175236_result.json`
- **Structured JSON:** [`fdfeb3c04bfe16684b16.json`](../../sessions/fd/fdfeb3c04bfe16684b16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入并注册 `comprehensive_results_table.md` (art_20260516_e87c5a)。

包含 7 张表：
1. **Table 1** — 4 模型 × 7 条件，exception_only 全模型 ≥99.33%
2. **Seed Robustness** — exception_only 完美稳定 (σ=0.00)，loop_only/label_only σ<1pp
3. **DebugBench 跨数据集** — exception_only 100%，VOTA 99.77%
4. **Nomarker 消融** — 去 markers 损失 2–3pp
5. **Regex Baselines** — 最佳 regex (B5) 99.33%，与 SFT 差 0.50pp (p=0.041)
6. **Lift vs no_trace** — 含 bootstrap CI
7. **Calibration** — ae_only ECE 最低 (0.0004)

空缺格标 "—"，所有数字 2 位小数，CI 用 Wilson 区间补齐。

---
