# analysis collect paper metrics table

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_collect_paper_metrics_table_20260516T022503_result.json`
- **Structured JSON:** [`c15847fe7d169ed518be.json`](../../sessions/c1/c15847fe7d169ed518be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/paper_metrics_table.md`，覆盖 34 个 eval 目录。

**核心结果速览：**

| 方法 | 最佳 F1 | Ign-F1 |
|------|---------|--------|
| SFT no-evidence (上界) | 48.93 | 47.36 |
| CED RSFT s43 | **46.83** | **45.85** |
| CED RSFT s44 | 46.55 | 45.51 |
| flat-NLI RSFT s42 | 45.39 | 44.49 |
| GRPO bf16 G=8 step100 | 45.49 | 45.59 |
| CED RSFT s42 r2b (max1536) | 45.04 | 44.20 |
| SFT baseline | 41.06 | 40.36 |
| DPO 1ep | 40.34 | 38.88 |

**4 项 eval 仍 pending：** CED RSFT s45、flat-NLI s45、DPO 3ep、SFT no-evidence-noquant。`rsft_flat_nli_s44` 只有 metrics.json（ign_f1 有 bug），需 v2 re-eval。

---
