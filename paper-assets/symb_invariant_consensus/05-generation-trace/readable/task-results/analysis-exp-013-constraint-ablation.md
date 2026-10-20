# analysis exp 013 constraint ablation

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-013-constraint-ablation_20260519T235109_result.json`
- **Structured JSON:** [`b024c280cc4636b39c58.json`](../../sessions/b0/b024c280cc4636b39c58.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-013 完成。结果汇总：

| Method | Overall (804) | FOLIO (204) | PW (600) |
|---|---|---|---|
| **SICA-MaxSAT** | 42.29% | 59.31% | 36.50% |
| **SICA-count-only** | 42.16% | 56.86% | 37.17% |
| **SICA-random-weight** | 42.06%±0.42% | 55.59%±0.73% | 37.47%±0.39% |
| **SC baseline** | 43.16% | 54.41% | 39.33% |

**核心发现**：
- **MaxSAT vs count-only**: Δ = +0.12pp，agreement 94.4%。在45个分歧问题上 MaxSAT 赢18次 vs count 赢17次——基本是随机。**假设confirmed：SAT solver 几乎无贡献。**
- **所有 constraint 方法都比 SC 差**（-0.87pp to -1.09pp），说明 constraint-based scoring 的整体价值存疑。
- 分数据集看：FOLIO 上 MaxSAT 比 SC 好 +4.9pp，但 count-only 也比 SC 好 +2.5pp，Z3 只贡献 +2.4pp。PW 上所有 constraint 方法都比 SC 差。

数据和脚本保存在 `westd-25068:/root/symb_invariant_consensus/results/exp013_constraint_ablation/`，已注册 registry (exp-013-constraint-ablation, DONE)。

---
