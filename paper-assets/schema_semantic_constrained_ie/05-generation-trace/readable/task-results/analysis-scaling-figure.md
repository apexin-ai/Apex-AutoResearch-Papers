# analysis scaling figure

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_scaling_figure_20260519T151243_result.json`
- **Structured JSON:** [`dbfd6c3c08a792cc7ef0.json`](../../sessions/db/dbfd6c3c08a792cc7ef0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个产出文件全部生成：

| 产出 | 路径 | 大小 |
|------|------|------|
| PDF | `artifacts/figures/scaling_analysis.pdf` | 28 KB |
| PNG | `artifacts/figures/scaling_analysis.png` | 225 KB |
| 数据表 | `artifacts/_project/report/scaling_analysis_data.md` | 3.5 KB |
| 脚本 | `artifacts/figures/plot_scaling_analysis.py` | 3.3 KB |

图表结构：2×2 子图

- **(a) SciERC ZS**: Unconstrained DR 从 15.4% (7B) → 13.3% (8B) → 6.5% (70B)；+ OntoCoDec 降至 0.93% → 0.08% → 0.0%
- **(b) DocRED ZS**: Unconstrained DR 从 18.5% (7B) → 26.1% (8B) → 13.1% (70B)；+ OntoCoDec 降至 10.2% → 2.6% → 0.0%
- **(c) SciERC LoRA**: 残余 DR 1-2%，OntoCoDec 进一步降至 ~0%
- **(d) DocRED LoRA**: 残余 DR < 1%，OntoCoDec 进一步降至 ~0.01-0.2%

Mistral-7B 因 BPE collision 问题从图中排除（数据保留在数据表中）。70B CF 值为估算值（~标记），数据表已注明来源。

---
