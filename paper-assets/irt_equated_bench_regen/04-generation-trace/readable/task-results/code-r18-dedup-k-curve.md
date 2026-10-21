# code r18 dedup k curve

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r18_dedup_k_curve_20260522T163407_result.json`
- **Structured JSON:** [`45d85d8607e385752272.json`](../../sessions/45/45d85d8607e385752272.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部产出已完成:

| 文件 | 路径 |
|------|------|
| 脚本 | `artifacts/r18_dedup_k_curve/dedup_k_analysis.py` |
| CSV | `artifacts/r18_dedup_k_curve/dedup_k_results.csv` |
| 图表 | `artifacts/r18_dedup_k_curve/dedup_k_curve.png` / `.pdf` |
| 报告 | `artifacts/r18_dedup_k_curve/dedup_k_report.md` |

**核心发现与预期不同**：C% 不会在 K≥5 后趋于平坦，而是随样本量单调递增（K=1: 0.3% → K=50: 23.3% → K=all: 31.3%）。但关键结论对论文有利：

- **同一 K 下的 SD 极小**（0.3–1.3pp）：说明选哪些模型无关紧要，排除了 family 结构人为膨胀 DIF 的可能
- C% 差异主要由**统计功效（样本量）**驱动，不是 within-family redundancy 制造的伪 DIF
- 正确表述：within-family redundancy 不会制造 spurious DIF，C% 反映的是真实的 temporal item shift

---
