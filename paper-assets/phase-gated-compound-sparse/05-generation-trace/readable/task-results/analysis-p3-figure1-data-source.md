# analysis p3 figure1 data source

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_p3_figure1_data_source_20260515T143058_result.json`
- **Structured JSON:** [`3949391b06c3708f19a3.json`](../../sessions/39/3949391b06c3708f19a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Figure 1 已确认更新为 n=496 数据，无需重新生成。**

- 生成脚本 `fig1_dose_response_n500.py` 明确标注 "n=496 paired problems"，数据来自 `table2_n500_full.csv`
- `paper/figures/fig1_dose_response.pdf` 已于 2026-05-15 21:27 更新

**但发现 caption/table 不一致**：
- Figure 1 caption 仍写 "from 69× to 274×"（旧 n=50 的 G 值），实际 n=496 数据是 ~7.5× 到 ~80×
- Table 1/2 仍标注 "across 50 problems"，数值未同步更新为 n=496

报告已保存至 `artifacts/p3_figure1/report.md`。

---
