# ops figure1 status check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_figure1_status_check_20260516T152430_result.json`
- **Structured JSON:** [`d3230b850e3c27f7699a.json`](../../sessions/d3/d3230b850e3c27f7699a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调查结果

### 论文 Figure 1 已不再是 dose_response 图

论文 `results.tex:73` 中 Figure 1（`\label{fig:hero}`）引用的是 **`fig1_ii_scatter.pdf`**，不是 `fig1_dose_response.pdf`。

### 各文件状态

| 文件 | 路径 | 修改时间 | 数据 |
|------|------|----------|------|
| **fig1_ii_scatter.pdf**（论文实际引用） | `paper/fig1_ii_scatter.pdf` | **2026-05-16 14:15**（今天） | n=496/475（从 caption 看） |
| fig1_dose_response.pdf | `figures/` | 2026-05-15 21:27 | n=496（由 `fig1_dose_response_n500.py` 生成） |
| fig1_dose_response.pdf | `paper/figures/` | 2026-05-16 10:57 | n=496（copy） |
| fig1_dose_response.pdf | `paper_figures/` | 2026-05-14 18:38 | 旧版，未更新 |

### 结论

1. **论文 Figure 1 (`fig1_ii_scatter.pdf`) 已是最新版**——今天生成，caption 明确写了 n=496/475。
2. **旧的 `fig1_dose_response.pdf`（G 指标图）已降级**——论文正文说 "G values reported in Appendix"，dose_response 图不再是 Figure 1。`figures/` 目录下的版本已由 `fig1_dose_response_n500.py` 用 n=496 数据重新生成。
3. **`paper_figures/fig1_dose_response.pdf`（5月14日）是唯一未更新的副本**，但论文不再引用它，影响不大。

ROADMAP 中 "Figure 1 PDF 生成" 可以标记为已完成。

---
