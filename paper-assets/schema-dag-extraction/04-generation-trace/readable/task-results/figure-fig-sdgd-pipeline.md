# figure fig sdgd pipeline

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_fig_sdgd_pipeline_20260523T123008_result.json`
- **Structured JSON:** [`b07c7c2db083f80d94ab.json`](../../sessions/b0/b07c7c2db083f80d94ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。

- 脚本: `scripts/gen_fig_sdgd_pipeline.py`
- PDF: `figures/paper/fig_sdgd_pipeline.pdf` (37KB)
- PNG: `figures/paper/fig_sdgd_pipeline.png` (96KB)

流程图从左到右展示 Full Schema → Decompose → Sub-schemas → Route & Extract → Merge → Final Predictions，上方红框标注 Routing Failure（RE 73% none-rate, Oracle 0.80 vs Practical 0.50），下方红框标注 Merge Amplification（NER/ED union 产生 false positives, F1 drops −19pp）。

---
