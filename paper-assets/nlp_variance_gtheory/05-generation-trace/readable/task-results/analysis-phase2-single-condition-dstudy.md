# analysis phase2 single condition dstudy

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase2_single_condition_dstudy_20260521T232312_result.json`
- **Structured JSON:** [`a01882a530722edeb8b5.json`](../../sessions/a0/a01882a530722edeb8b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 已保存到服务器，artifact 已注册。汇总：

## D-Study 结果（3 种设计，Spearman-Brown 投影）

| 设计 | 条件数/item | σ²_δ | n(G≥0.80) | G@116 | G@200 |
|------|-----------|------|-----------|-------|-------|
| **Multi-facet** | 1,296 | 0.00867 | **55** | 0.895 | 0.936 |
| **Partial (2p×2s)** | 4 | 0.03890 | **245** | 0.655 | 0.766 |
| **Single-condition** | 1 | 0.08770 | **552** | 0.457 | 0.592 |

### Ratios (论文 [TBD-RATIO] 数字)
- **single / multi = 552 / 55 = 10.0×**
- **partial / multi = 245 / 55 = 4.5×**

关键发现：单条件评估需要 **552 items** 才能达到 G≥0.80，是满配设计（55 items）的 **10倍**。即使用 4 条件的 partial 设计也需要 245 items（4.5倍）。MMLU 的 116 items/subject 在单条件下仅 G=0.457，远不及 0.80 阈值。

验证：multi-facet 投影与已有 `d_study` 8 个值完全吻合（diff=0.000000），单调性 3 个设计均 PASS。

---
